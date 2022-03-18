from typing import List, Dict, Callable
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
import cvr
from pathlib import Path
from fuzzup.utils import complist

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# helper function
def clean_string(x):
    out = re.sub(r"\([^()]*\)", "", x)
    return out

## This won't work well and the quota is quickly expired...
#CVRAPI.dk attempt - can only query 1 company at a time ...
#It is quota based... bad
def get_cvrapi_company(name : str, country: str ='dk') -> Dict:
  time.sleep(0.5) # it's not nice to spam public api
  name = name.replace(' ', '-')
  name = name.replace('A/S', '%2FS')
  request_a = request.Request(
    url=f'https://cvrapi.dk/api?search={name}&country={country}',
    headers={
      'User-Agent': 'CVR opslag'})
  try:
    with contextlib.closing(request.urlopen(request_a)) as response:
            companies_json = json.loads(response.read())
            record = {companies_json['name'] : {
                'by': companies_json['city'],
                'postnr': companies_json['zipcode']}}
            return record 
  except:
      return {name : None} # nothing was found in lookup on company

def get_cvrdev_company(name: str) -> Dict:    
    time.sleep(0.5) # it's not nice to spam public api
    record_list = []
    
    #BUG : There is a bug with cvr=0.2.0, that throws an exception if specific company names are parsed.
    try:
        for virksomhed in CLIENT.cvr.virksomheder(navn=name):
            record = {virksomhed.metadata.nyeste_navn.navn : {'postnummer':virksomhed.metadata.nyeste_beliggenhedsadresse.postnummer,
                                                            'bynavn': virksomhed.metadata.nyeste_beliggenhedsadresse.bynavn,
                                                            'fritekst': virksomhed.metadata.nyeste_beliggenhedsadresse.fritekst
                                                             }
                     }
            record_list.append(record)
    except Exception:
        #We have to either skip the company or hardcode the entry. Defaultdict can't be used, because it's a problem with CVR library.
        record_list.append({name : {'postnummer': None, 'bynavn': None, 'fritekst': None}})
    return record_list
    
def get_companies(function_load: Callable = get_cvrdev_company) -> List[Dict]:
    #CVR-dev attempt
    #KEY: cvr.dev_513f54b68ebe9e83e3b2dde277d598bf
    global CLIENT
    CLIENT =  cvr.Client(api_key='cvr.dev_513f54b68ebe9e83e3b2dde277d598bf')

    company_records = {}
    
    for i in tqdm(complist):
        record = function_load(i['name'])
        for j in record:
            company_records.update(j) 
        if len(company_records) > 100:
            logging.info('Stopping early, dont spam the api')
            break
    return company_records

def get_politicians():
    """
    copy pasta from https://github.com/cfblaeb/politik
    """

    # ft.dk only allows 100 rows per call
    table='Aktør'
    url = f'http://oda.ft.dk/api/{table}'
    totalcount = int(requests.get(url, params={"$inlinecount": "allpages"}).json()['odata.count'])
    ccount = 0
    print(f"# records: {totalcount}")
    
    results = []
    while ccount < totalcount:
        r = requests.get(url, params={"$skip": ccount})
        for row in r.json()['value']:
            if all([row.get('slutdato') is None,
                    row.get('startdato') is not None,
                    row.get('fornavn') is not None,
                    row.get('efternavn') is not None]):
                results.append(row)

        ccount += 100
        if ccount % 1000 == 0:
            print(f"# records processed: {ccount}/{totalcount}")

    print(f"Number of politicians identified: {len(results)}")

    # extract names    
    names = [x.get('fornavn') + " " + x.get('efternavn') for x in results]
    names = [clean_string(x).strip() for x in names]
    names.sort()
    
    # convert to fuzzup dict format
    names = {x: {} for x in names}
    
    return names

def get_byer():
    """Get all byer in DK"""
    url = 'https://api.dataforsyningen.dk/steder?hovedtype=Bebyggelse&undertype=by'
    byer = requests.get(url).json()
    records = []
    for by in byer:
        kommuner = [kommune['navn'] for kommune in by['kommuner']]
        if len(kommuner) == 1:
            kommuner = kommuner[0]
        records.append(
            {
                'navn': by['primærtnavn'],
                'indbyggerantal': by['egenskaber']['indbyggerantal'],
                'kommune': kommuner
            }
        )
    df = pd.DataFrame(records)
    return df

def get_municipalities():
    
    kommuner = get_byer().kommune.tolist()
    kommuner = [[x] if isinstance(x, str) else x for x in kommuner]
    kommuner = [item for sublist in kommuner for item in sublist]
    kommuner = set(kommuner)
    
    # convert to fuzzup dict format
    kommuner = {x: {} for x in kommuner}
    
    return kommuner

def get_cities():
    
    df = get_byer()
    
    out = {}
    for row in df.itertuples(index=False, name="row"):
        out[row.navn] = {'municipality': row.kommune}                
    
    return out

# helper function
def aggregate_to_cluster(x):
    res = np.unique(np.concatenate(x.matches.tolist()))
    return res

def match_whitelist(words: List[Dict],
                    whitelist: List[str], 
                    score_cutoff: float=80,
                    to_dataframe: bool=False,
                    aggregate_cluster: bool=False,
                    entity_group: List[str]=None,
                    **kwargs) -> List[Dict]:
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
    assert isinstance(whitelist, list), "'whitelist' must be a list"
    
    # handle trivial case (empty list)
    if not words or not whitelist:
        if to_dataframe:
            return pd.DataFrame()
        else:
            return []
        
    if isinstance(words, list) and all([isinstance(x, dict) for x in words]):
        output_ner = True
        if entity_group is not None:
            words = [x for x in words if x.get('entity_group') in entity_group]
        strings = [x.get('word') for x in words]
    else:
        output_ner = False
        strings = words
    
    if len(strings) == 0:    
        if to_dataframe:
            return pd.DataFrame()
        else:
            return []
           
    # compute distances
    dists = cdist(whitelist, 
                  strings, 
                  score_cutoff=score_cutoff,
                  **kwargs)

    matches = [np.array(whitelist)[np.where(col)] for col in dists.T]
    
    if not output_ner:
        df = pd.DataFrame.from_dict({'word': strings, 'matches': matches}) 

    if output_ner:
        df = pd.DataFrame.from_records(words)
        df["matches"] = matches
        if aggregate_cluster:
            matches = pd.DataFrame(df.groupby(by=['cluster_id']).apply(aggregate_to_cluster), columns=['matches'], index=None)
            matches = matches.reset_index()
            df.drop('matches', axis=1, inplace=True)
            df = pd.merge(df, matches, how="left")
    
    df['matches']=[x.tolist() for x in df['matches']]    
    
    if not to_dataframe:
        df = df.to_dict(orient="records")
    
    return df

class Whitelist():
    
    def __init__(self,
                 function_load,
                 title,
                 entity_group,
                 **kwargs) -> None:
        
        self.entity_group = entity_group
        self.title = title
        logger.info(f"Loading whitelist: {title}")
        self.whitelist = function_load(**kwargs)
        logger.info("Done loading.")
        
    def __call__(self,
                 words: List[Dict],
                 **kwargs) -> List[Dict]:
        
        out = match_whitelist(words=words,
                              whitelist=list(self.whitelist.keys()), 
                              entity_group=self.entity_group,
                              **kwargs)
        
        # TODO: return mappings
        
        return out
    
class Cities(Whitelist):
    
    def __init__(self,
                 **kwargs):
        
        super().__init__(function_load=get_cities,
                         title='city',
                         entity_group=['LOC'],
                         **kwargs)
        
        
class Companies(Whitelist):
    
    def __init__(self,
                 **kwargs):
        
        super().__init__(function_load=get_companies,
                         title='company',
                         entity_group=['ORG'],
                         **kwargs
                         )
#comp = Companies()   

# class Cities():
#     
#     def __init__(self):
#         self.whitelist = get_cities()
#         self.entity_group = ["LOC"]
#         self.title = "city"
#     
#     def __call__(self,
#                  words: List[Dict],
#                  **kwargs):
#         
#         out = match_whitelist(words=words,
#                               whitelist=list(self.whitelist.keys()), 
#                               entity_group=self.entity_group,
#                               **kwargs)
#         
#         # TODO: return mappings
#         
#         return out
# 
