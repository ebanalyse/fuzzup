from typing import List, Dict

from rapidfuzz.process import cdist, extract
import numpy as np
import pandas as pd
from scipy.stats import rankdata

# constants
CLUSTER_ID = 'cluster_id'

def compute_fuzzy_matrix(strings: List[str],
                         **kwargs) -> pd.DataFrame:
    """Compute Fuzzy Matrix
    
    Computes matrix with pairwise fuzzy ratios (=edit)
    distances between all strings. 
    
    The result can be thought of as a correlation 
    matrix with all diagonal elements equal to 100.
    
    Args:
        strings (List[str]): strings for clustering.
        
    Returns:
        pd.DataFrame: pairwise fuzzy ratios between
            strings.
            
    Examples:
        >>> person_names = ['Donald Trump', 'Donald Trump', 
                            'J. biden', 'joe biden', 'Biden', 
                            'Bide', 'mark esper', 
                            'Christopher c . miller', 
                            'jim mattis', 'Nancy Pelosi', 
                            'trumps', 'Trump', 'Donald', 
                            'miller']
        ....
        
    """  
    
    # subset unique strings.
    strings = list(set(strings))

    # compute edit distances
    dists = cdist(strings, strings, **kwargs) 
    
    dists = pd.DataFrame(dists, index=strings, columns=strings)
    
    return dists

def helper_clustering(m, vars, cutoff = 70):

    add_elements = vars
    nothing_to_add = False
    iteration = 0
    cluster = vars

    while len(m) > 0 and not nothing_to_add:      
        iteration += 1
        #print("iteration", iteration)
        m = m.drop(add_elements)
        l = pd.DataFrame(m[cluster] > cutoff)
        l = l.sum(axis = 1).tolist()
        l = [x >= 1 for x in l]
    
        if not any(l):
            # print("Nothing to add - stopping.")
            nothing_to_add = True
    
        from itertools import compress
        add_elements = list(compress(list(m.index), l))
        cluster.extend(add_elements)
    
    return cluster, m

def cluster_cutoff(fuzzy_matrix, 
                   cutoff=70,
                   **kwargs):
    m = fuzzy_matrix
    clusters = []
    while len(m) > 0:
        var = [m.index.tolist()[0]]
        cluster, m = helper_clustering(m, var, cutoff = cutoff)
        clusters.append(cluster)
    
    return clusters

def fuzzy_cluster(words, 
                  cutoff: int = 70, 
                  to_dataframe: bool = False,
                  merge_output: bool = True,
                  by_entity_group = False,
                  **kwargs):
    
    # TODO: implement by_entity_group

    if isinstance(words, list) and all([isinstance(x, dict) for x in words]):
        input_ner = True
        strings = [x.get('word') for x in words]
    else:
        input_ner = False
        strings = words
    
    # compute fuzzy ratios
    fuzzy_matrix = compute_fuzzy_matrix(strings, **kwargs)
    
    clusters = cluster_cutoff(fuzzy_matrix, 
                              cutoff=cutoff)
    
    # compute cluster meta data.
    cluster_ids = [max(cluster, key=len) for cluster in clusters]
    
    # organize output properly (for compatibility with transformers NER pipeline)
    output = []
    for idx, cluster in enumerate(clusters):
        output.append(pd.DataFrame.from_dict({'word': cluster, CLUSTER_ID: cluster_ids[idx]}))
    output = pd.concat(output, ignore_index=True)
    
    # merge output with original input
    if input_ner and merge_output:
        output = pd.merge(pd.DataFrame.from_dict(words), output, how="left")
                 
    if not to_dataframe:
        output = output.to_dict(orient="records")
    
    return output, fuzzy_matrix

def compute_prominence(clusters: List[Dict], 
                       to_dataframe: bool=False, 
                       merge_output: bool=True,
                       method: str="count") -> List[Dict]:
    """Compute Prominence
    
    Computes prominence of entity clusters.

    Args:
        clusters (List[Dict]): Entity clusters.
        to_dataframe (bool, optional): Export output
            as pandas dataframe? Defaults to False.
        merge_output (bool, optional): Merge resulting 
            clusters with input data. Defaults to True.
        method (str, optional): Method for computing 
            prominence. Choose from "count". Defaults 
            to "count".

    Returns:
        List[Dict]: _description_
    """
    
    clusters = pd.DataFrame.from_dict(clusters)
    counts = clusters[CLUSTER_ID].value_counts()
    ranks = rankdata(counts, method = "max")
    ranks = max(ranks) - ranks + 1
    output = pd.DataFrame.from_dict({CLUSTER_ID: counts.index,
                                    'prominence': ranks,
                                    'count': counts})  
    
    if merge_output:
        output = pd.merge(clusters, output, how="left")
        
    if not to_dataframe:
        output = output.to_dict(orient="records")
    
    return output
