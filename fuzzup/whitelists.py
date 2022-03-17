from typing import List, Dict
import logging

import requests
import pandas as pd
import re
import numpy as np
from rapidfuzz.process import cdist

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# helper function
def clean_string(x):
    out = re.sub(r"\([^()]*\)", "", x)
    return out

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
    assert isinstance(whitelist, (list, dict)), "'whitelist' must be a list or dit"
 
    is_dict = False   
    if isinstance(whitelist, dict):
        is_dict = True
        whitelist_dict = whitelist
        whitelist = list(whitelist.keys())
        
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
             
    if is_dict:
        mappings = []
        for match in matches:
            out = [whitelist_dict.get(x) for x in match]
            mappings.append(out)
        df['mappings'] = mappings
    
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
                              whitelist=self.whitelist, 
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
    
# c = Cities()
    
    
    
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
