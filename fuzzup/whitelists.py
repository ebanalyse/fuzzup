from typing import List, Dict, Callable, Union
import logging

import requests
import pandas as pd
import re
import numpy as np
from rapidfuzz.process import cdist
import contextlib
import json
import urllib.request as request
from tqdm import tqdm
import time
from pathlib import Path

from fuzzup.utils import complist

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# helper function
def clean_string(x):
    out = re.sub(r"\([^()]*\)", "", x)
    return out


## This won't work well and the quota is quickly expired...
# CVRAPI.dk attempt - can only query 1 company at a time ...
# It is quota based... bad
def get_cvrapi_company(name: str, country: str = "dk") -> Dict:
    time.sleep(0.5)  # it's not nice to spam public api
    name = name.replace(" ", "-")
    name = name.replace("A/S", "%2FS")
    request_a = request.Request(
        url=f"https://cvrapi.dk/api?search={name}&country={country}",
        headers={"User-Agent": "CVR opslag"},
    )
    try:
        with contextlib.closing(request.urlopen(request_a)) as response:
            companies_json = json.loads(response.read())
            record = {
                companies_json["name"]: {
                    "by": companies_json["city"],
                    "postnr": companies_json["zipcode"],
                }
            }
            return record
    except:
        return {name: None}  # nothing was found in lookup on company


def get_cvrdev_company(name: str) -> Dict:
    time.sleep(0.5)  # don't spam api
    url = f"https://api.cvr.dev/api/cvr/virksomhed?navn={name}"
    auth = {"Authorization": "cvr.dev_513f54b68ebe9e83e3b2dde277d598bf"}
    record_list = []

    resp = requests.get(url, headers=auth)

    if resp.ok:
        for record in resp.json():
            res = {
                record["virksomhedMetadata"]["nyesteNavn"]["navn"]: {
                    # 'postnummer':record['virksomhedMetadata']['nyesteBeliggenhedsadresse']['postnummer'],
                    # 'vejnavn':record['virksomhedMetadata']['nyesteBeliggenhedsadresse']['vejnavn'],
                    # 'bynavn':record['virksomhedMetadata']['nyesteBeliggenhedsadresse']['bynavn'],
                    # 'fritkest':record['virksomhedMetadata']['nyesteBeliggenhedsadresse']['fritekst'],
                    "municipality": record["virksomhedMetadata"][
                        "nyesteBeliggenhedsadresse"
                    ]["kommune"]["kommuneKode"],
                    # 'kommunenavn':record['virksomhedMetadata']['nyesteBeliggenhedsadresse']['kommune']['kommuneNavn'],
                    # 'postdistrikt':record['virksomhedMetadata']['nyesteBeliggenhedsadresse']['postdistrikt']
                }
            }
            record_list.append(res)
    else:
        raise RuntimeError(resp.status_code)
    return record_list


def get_eblocal_names():
    url = "https://misty-beirut-ryz6j4qt64tt.vapor-farm-b1.com/api/eblocal_aliases?big_cities=true"
    eblocals = requests.get(url).json()
    # remove "hits"
    meta = eblocals[0]
    meta["list_type"] = "eblocal_aliases?big_cities=true"
    eblocals.pop(0)

    out = {
        x["name"]: {
            "id": x["eblocal_id"],
            "label": x["name"],
            "type": "id_eblocal",
            "version": meta.get("version"),
        }
        for x in eblocals
    }
    return out


def get_eblocal_organizations():
    url = (
        "https://misty-beirut-ryz6j4qt64tt.vapor-farm-b1.com/api/eblocal_organisations"
    )
    eblocal_organizations = requests.get(url).json()
    # remove "hits"
    meta = eblocal_organizations[0]
    meta["list_type"] = "eblocal_organisations"
    eblocal_organizations.pop(0)
    out = {
        x["name"]: {
            "id": x["eblocal_id"],
            "label": x["eblocal_name"],
            "type": "id_eblocal_organization",
            "version": str(meta.get("version_number"))
            + "_"
            + str(meta.get("list_type")),
        }
        for x in eblocal_organizations
    }
    return out


def get_companies(function_load: Callable = get_cvrdev_company) -> List[Dict]:
    company_records = {}

    for i in tqdm(complist):
        record = function_load(i["name"])
        for j in record:
            company_records.update(j)
        if len(company_records) > 100:
            logging.info("Stopping early, dont spam the api")
            break
    return company_records


def get_politicians():
    """
    copy pasta from https://github.com/cfblaeb/politik
    """

    # ft.dk only allows 100 rows per call
    table = "Aktør"
    url = f"http://oda.ft.dk/api/{table}"
    totalcount = int(
        requests.get(url, params={"$inlinecount": "allpages"}).json()["odata.count"]
    )
    ccount = 0
    print(f"# records: {totalcount}")

    results = []
    while ccount < totalcount:
        r = requests.get(url, params={"$skip": ccount})
        for row in r.json()["value"]:
            if row.get("typeid") == 5:  # Type_ID 5 = Politiker i folketinget.
                if all(
                    [
                        row.get("slutdato") is None,
                        row.get("startdato") is not None,
                        row.get("fornavn") is not None,
                        row.get("efternavn") is not None,
                    ]
                ):
                    results.append(row)
            else:
                pass

        ccount += 100
        if ccount % 1000 == 0:
            print(f"# records processed: {ccount}/{totalcount}")

    print(f"Number of politicians identified: {len(results)}")

    # extract names
    names = [x.get("fornavn") + " " + x.get("efternavn") for x in results]
    names = [clean_string(x).strip() for x in names]
    names.sort()

    # convert to fuzzup dict format
    names = {x: {} for x in names}

    return names


def _get_df():
    here = Path(__file__).parent
    fname = here / "2022.04.06-finished-eblocal_converts.csv"
    df = pd.read_csv(fname)
    return df


def get_eblocal_byer():
    df = _get_df()

    out = {}
    for row in df.itertuples(index=False, name="row"):
        out[row.name] = {
            "municipality": row.municipality_name + " Kommune",
            "eblocal_id": row.eblocal_id,
            "dawa_id": row.dawa_id,
            "lon_lat": (row.longitude, row.latitude),
        }
    return out


def get_eblocal_neighborhoods():
    df = _get_df()

    df = df[df["type"] == "bydel"]

    out = {}
    for row in df.itertuples(index=False, name="row"):
        out[row.name] = {
            "municipality": row.municipality_name,
            "eblocal_id": row.eblocal_id,
            "dawa_id": row.dawa_id,
            "lon_lat": (row.longitude, row.latitude),
        }
    return out


def get_eblocal_municipality():
    df = _get_df()

    out = {}

    for row in df.itertuples(index=False, name="row"):
        out[row.municipality_name + " Kommune"] = {
            "eblocal_id": row.eblocal_id,
            "municipality_id": row.municipality_id,
            "dawa_id": row.dawa_id,
        }
    return out


def get_municipalities():
    url = "https://api.dataforsyningen.dk/kommuner"
    meta = {"version": "1"}
    meta["list_type"] = "dawa/kommuner"
    data = requests.get(url).json()
    whitelist = {
        " ".join([x.get("navn"), "Kommune"]): {
            "id": x.get("kode"),
            "label": " ".join([x.get("navn"), "Kommune"]),
            "type": "id_municipality",
            "version": str(meta.get("version_number"))
            + "_"
            + str(meta.get("list_type")),
        }
        for x in data
    }
    return whitelist


# TODO : Add version number in eb_local -> do not pop the first entry,put it in seperate key
def get_eblocal_names():
    url = "https://misty-beirut-ryz6j4qt64tt.vapor-farm-b1.com/api/eblocal_aliases?big_cities=true"
    eblocals = requests.get(url).json()
    # remove "hits"
    meta = eblocals[0]
    meta["list_type"] = "eblocal_aliases?big_cities=true"
    eblocals.pop(0)
    out = {
        x["name"]: {
            "id": x["eblocal_id"],
            "label": x["eblocal_name"],
            "type": "id_eblocal",
            "version": str(meta.get("version_number"))
            + "_"
            + str(meta.get("list_type")),
        }
        for x in eblocals
    }
    return out


def get_neighborhoods():
    """Get all neighborhoods in DK"""
    url = "https://api.dataforsyningen.dk/steder?hovedtype=Bebyggelse&undertype=bydel"
    hoods = requests.get(url).json()
    out = {hood["primærtnavn"]: {"eblocal_code": hood["id"]} for hood in hoods}
    return out


# helper function
def aggregate_to_cluster(x):
    res = np.unique(np.concatenate(x.matches.tolist()))
    return res


# TODO: Change this method so that it can match RANK 2 entities as well ~
def match_whitelist(
    words: List[Dict],
    whitelist: List[str],
    score_cutoff: float = 80,
    to_dataframe: bool = False,
    aggregate_cluster: bool = False,
    individual_wl_match: bool = True,
    match_strategy: bool = False,
    entity_group: List[str] = None,
    **kwargs,
) -> List[Dict]:
    """Match entities with white list

    Args:
        words (List[Dict]): words/entities for matching.
        whitelist (List[str]): white list with words/entities
            to match with.
        score_cutoff (float, optional): Cutoff threshold value for
            matching. Defaults to 80.
        to_dataframe (bool, optional): Return output as data frame.
            Defaults to False.
        aggregate_cluster (bool, optional): Aggregate matches to
            cluster level. Defaults to False.
        kwargs: optinal arguments for cdist.
        entity_group: which entity groups to match.

    Returns:
        List[Dict]: words and their respective matches with the
            white list.
    """
    assert isinstance(words, list), "'words' must be a list"
    assert isinstance(whitelist, (list, dict)), "'whitelist' must be a list or dit"

    def filter_rank_df(
        df_filter: pd.DataFrame,
        df: pd.DataFrame,
        rank_limit: int = 1,
        min_count: int = 2,
    ) -> pd.DataFrame:

        rank_list = df_filter.query(
            "count >= 2 and prominence_rank == 2 or prominence_rank==1"
        ).cluster_id.tolist()
        df = df.query("cluster_id in @rank_list")
        return df

    def count_word_prominence_freq(strings: List[str]) -> pd.Series:
        """
        This function will take a list of strings, compare it to their prominence rank and
        count, in order to decide which strings should be returned.
        """
        return pd.value_counts(np.array(strings))

    def convert_version_list_to_set(row: pd.Series) -> pd.Series:
        """This method will convert any list of version numbers to a set of unique versions"""
        row["versions"] = set(row["versions"].tolist())
        return row

    # if the whitelist is a dictionary, then generate a list of keys for later use
    is_dict = False
    if isinstance(whitelist, dict):
        is_dict = True
        whitelist_dict = whitelist
        whitelist = list(whitelist.keys())
        whitelist_versions = [x.get("version") for x in whitelist_dict.values()]

    # handle trivial case (empty list)
    if not words or not whitelist:
        if to_dataframe:
            return pd.DataFrame()
        else:
            return []
    # if all words are dictionaries, it is assumed to be NER format
    if isinstance(words, list) and all([isinstance(x, dict) for x in words]):
        output_ner = True
        if entity_group is not None:
            words = [x for x in words if x.get("entity_group") in entity_group]
        strings = [x.get("word") for x in words]

    else:
        output_ner = False
        strings = words

    if len(strings) == 0:
        if to_dataframe:
            return pd.DataFrame()
        else:
            return []

    # compute distances - length of the whitelist
    # Only takes strings ~ so no information about prominence here.
    dists = cdist(whitelist, strings, score_cutoff=score_cutoff, **kwargs)

    # All matches on the whitelist ~ pass all words here to start with and then handle matches afterwards
    matches = [np.array(whitelist)[np.where(col)] for col in dists.T]
    if is_dict:
        versions = [np.array(whitelist_versions)[np.where(col)] for col in dists.T]
    if not output_ner:
        df = pd.DataFrame.from_dict({"word": strings, "matches": matches})

    if output_ner:
        df = pd.DataFrame.from_records(words)
        df["matches"] = matches
        if is_dict:
            df["versions"] = versions
            df = df.apply(convert_version_list_to_set, axis=1)

        # MATCH STRATEGY
        if "prominence_rank" in df and match_strategy is True:
            df_filter = (
                df.groupby(["cluster_id", "prominence_rank"])["word"]
                .count()
                .reset_index()
                .rename({"word": "count"}, axis=1)
            )

            # If rank 2 has an occurance of at least 2, regardless of prominence_score
            if (df_filter[df_filter["prominence_rank"] == 2]["count"] >= 2).any():
                df = filter_rank_df(
                    df_filter=df_filter, df=df, rank_limit=2, min_count=2
                )

            # Regress to match-strategy of returning rank 1 only
            else:
                df = df[df["prominence_rank"] == 1]  # return first rank only

        if individual_wl_match is True and "prominence_rank" in df:
            # here comes the funky part.. re-rank the whole thing all over again :-)
            # Each whitelist is passed exactly once, and we actually don't need the versions list. as it can only
            # match to whatever whitelist is passed...
            # simply count the passed entities and re-rank them
            # this WILL break the linear and positional weighting
            # Actually, it will make the initial prominence module obsolete...
            # Could import fuzz.py, but the **kwargs requirement would honestly turn it into a clusterfuck

            df["cluster_id"].rank()
            pass

        if aggregate_cluster:
            matches = pd.DataFrame(
                df.groupby(by=["cluster_id"]).apply(aggregate_to_cluster),
                columns=["matches"],
                index=None,
            )
            matches = matches.reset_index()
            df.drop("matches", axis=1, inplace=True)
            df = pd.merge(df, matches, how="left")

    df["matches"] = [x.tolist() for x in df["matches"]]

    if is_dict:
        mappings = []
        for match in df.matches.tolist():
            out = [whitelist_dict.get(x) for x in match]
            mappings.append(out)
        df["mappings"] = mappings

    # subset matches only
    df = df[df["matches"].astype(str) != "[]"]

    if not to_dataframe:
        df = df.to_dict(orient="records")

    return df


class Whitelist:
    """Whitelist

    Whitelist objects containing whitelists and
    relevant meta data regarding how to apply
    it.

    Attributes:
        entity_group (str): the entity group of interest
            for the given whitelist.
        title (str): title of the type of entity the
            whitelist relates to.
        whitelist (dict): whitelist with keys to
            match with. The values contain mappings
            for the given key.
    """

    def __init__(self, function_load, title, entity_group, **kwargs) -> None:

        self.entity_group = entity_group
        self.title = title
        logger.info(f"Loading whitelist: {title}")
        self.whitelist = function_load(**kwargs)
        logger.info("Done loading.")

    def __call__(self, words: List[Dict], **kwargs) -> List[Dict]:

        out = match_whitelist(
            words=words,
            whitelist=self.whitelist,
            entity_group=self.entity_group,
            **kwargs,
        )

        return out


# TODO: One of the few places we process whitelist directly
# After this, we end up with a list of dictionaries ...
def apply_whitelists(
    whitelists: List[Whitelist],
    clusters: List[Dict],
    **kwargs,
) -> pd.DataFrame:
    """Apply Multiple Whitelists

    Args:
        whitelists (List[Whitelist]): Whitelists.
        clusters (List[Dict]): Results from fuzzy clustering etc.
        kwargs: all optional arguments for whitelist matching.

    Returns:
        Dict: output from whitelist applications.
    """
    out = {wl.title: wl(clusters, **kwargs) for wl in whitelists}
    return out


def format_helper(
    x: List[Dict],
    columns: List[str] = ["neighborhood_code", "city_code", "municipality_code"],
) -> pd.DataFrame:
    output = []
    if len(x) > 0:
        for match in x:
            mappings = match.get("mappings")
            if len(mappings) > 0:
                df = pd.DataFrame.from_records(mappings)
                out = pd.DataFrame(columns=columns, index=range(len(df)))
                for col in columns:
                    if col in df:
                        out[col] = df[col]
                output.append(out)
    if len(output) == 0:
        return pd.DataFrame()
    output = pd.concat(output, ignore_index=True)
    return output


def format_output(
    results: List[Dict],
    columns: List[str] = ["neighborhood_code", "city_code", "municipality_code"],
    drop_duplicates: bool = True,
) -> pd.DataFrame:
    """Format Output

    Formats output from whitelist format by extracting
    only specific columns and converting them to
    a pandas DataFrame.

    Args:
        results (List[Dict]): Results from Fuzzy Clustering.
        columns (List[str], optional): Desired columns
            to extract. Defaults to
            ['neighborhood_code', 'city_code',
            'municipality_code'].
        drop_duplicates (bool, optional): Drop duplicate
            matches? Defaults to True.

    Returns:
        pd.DataFrame: Output in desired format.
    """
    results = [format_helper(x=results.get(x), columns=columns) for x in results]
    results = pd.concat(results, ignore_index=True)
    if drop_duplicates:
        results.drop_duplicates(inplace=True, keep="first")
    return results


class Cities(Whitelist):
    """Danish Cities

    Whitelist of names of Danish cities
    initialized from the DAWA API.
    """

    def __init__(self, **kwargs):

        super().__init__(
            function_load=get_eblocal_byer, title="city", entity_group=["LOC"], **kwargs
        )


class Municipalities(Whitelist):
    """Danish Cities

    Whitelist of names of Danish Municipalities
    initialized from the DAWA API.
    """

    def __init__(self, **kwargs):

        super().__init__(
            function_load=get_municipalities,
            title="municipality",
            entity_group=["LOC"],
            **kwargs,
        )


class EBLocalNames(Whitelist):
    """EB Local Names

    Whitelist with Ekstra Bladet Local Names.
    """

    def __init__(self, **kwargs):

        super().__init__(
            function_load=get_eblocal_names,
            title="eblocal_name",
            entity_group=["LOC"],
            **kwargs,
        )


class Neighborhoods(Whitelist):
    """Danish Neighborhoods

    Whitelist of names of Danish Neighborhoods
    initialized from the DAWA API.
    """

    def __init__(self, **kwargs):

        super().__init__(
            function_load=get_eblocal_neighborhoods,
            title="neighborhood",
            entity_group=["LOC"],
            **kwargs,
        )


class Companies(Whitelist):
    def __init__(self, **kwargs):

        super().__init__(
            function_load=get_eblocal_organizations,
            title="company",
            entity_group=["ORG"],
            **kwargs,
        )


class Politicians(Whitelist):
    def __init__(self, **kwargs):

        super().__init__(
            function_load=get_politicians,
            title="politician",
            entity_group=["PER"],
            **kwargs,
        )
