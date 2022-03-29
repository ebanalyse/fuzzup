from typing import List, Dict, Tuple
from itertools import compress

from rapidfuzz.process import cdist, extract
import numpy as np
import pandas as pd
from scipy.stats import rankdata

from fuzzup.utils import flatten

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
        kwargs: all optional arguments for 
            rapidfuzz.process.cdist.
        
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

def helper_clustering(m, 
                      vars, 
                      cutoff: float = 70):

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
    
        add_elements = list(compress(list(m.index), l))
        cluster.extend(add_elements)
    
    return cluster, m

def naive_cluster(fuzzy_matrix: pd.DataFrame, 
                  cutoff: float = 70,
                  **kwargs) -> list:
    """Naive Clustering
    
    Conducts naive clustering based on matrix with
    pairwise correlations, fuzzy ratios etc.

    Args:
        fuzzy_matrix (pd.DataFrame): Matrix with
            pairwise fuzzy ratios between words.
        cutoff (float, optional): Threshold for naive
            clustering algorithm with respect to 
            pairwise fuzzy ratios. Defaults to 70.

    Returns:
        list: resulting clusters.
    """
    m = fuzzy_matrix
    clusters = []
    while len(m) > 0:
        var = [m.index.tolist()[0]]
        cluster, m = helper_clustering(m, var, cutoff = cutoff)
        clusters.append(cluster)
    
    return clusters

def fuzzy_cluster(words: List[Dict], 
                  cutoff: int = 70, 
                  to_dataframe: bool = False,
                  merge_output: bool = True,
                  **kwargs) -> List[Dict]:
    """_summary_

    Args:
        words (List[Dict]): Words/entities for clustering.
        cutoff (int, optional): Cutoff threshold value for fuzzy
            ratios when forming clusters. Defaults to 70.
        to_dataframe (bool, optional): Output as dataframe?
            Defaults to True.
        merge_output (bool, optional): Merge output with 
            original input? Defaults to False.

    Returns:
        List[Dict]: Clusters of entities.
    """
    
    # TODO: implement by_entity_group
    assert isinstance(words, list), "'words' must be a list"

    # handle trivial case (empty list)
    if not words:
        if to_dataframe:
            return pd.DataFrame()
        else:
            return []
        
    if isinstance(words, list) and all([isinstance(x, dict) for x in words]):
        output_ner = True
        strings = [x.get('word') for x in words]
    else:
        output_ner = False
        strings = words
    
    # compute fuzzy ratios
    fuzzy_matrix = compute_fuzzy_matrix(strings, **kwargs)
    
    clusters = naive_cluster(fuzzy_matrix, 
                             cutoff=cutoff)
    
    # generate cluster ids (longest entity variation).
    cluster_ids = [max(cluster, key=len) for cluster in clusters]
    
    # organize output properly (for compatibility with transformers NER pipeline)
    output = []
    for idx, cluster in enumerate(clusters):
        output.append(pd.DataFrame.from_dict({'word': cluster, CLUSTER_ID: cluster_ids[idx]}))
    output = pd.concat(output, ignore_index=True)
    
    # merge output with original input
    if output_ner and merge_output:
        output = pd.merge(pd.DataFrame.from_dict(words), output, how="left")
                 
    if not to_dataframe:
        output = output.to_dict(orient="records")
    
    return output

def fuzzy_cluster_bygroup(words: List[Dict], 
                          **kwargs) -> List[Dict]:
    """Fuzzy Cluster By Group
    
    Fuzzy clustering by entity group. Simply 
    calls fuzzy_cluster() groupwise.

    Args:
        words (List[Dict]): Words/entities.
        kwargs: all optional arguments for 
            fuzzy_cluster().

    Returns:
        List[Dict]: entity clusters.
    """
    # handle trivial case.
    if len(words) == 0:
        return []
    
    words = pd.DataFrame.from_dict(words)
    words = words.groupby(['entity_group'])
    
    out = [fuzzy_cluster(words = words.get_group(group).to_dict(orient="records"), **kwargs) for group in words.groups]
    
    out = flatten(out)
    
    return out
            
def compute_prominence(clusters: List[Dict], 
                       to_dataframe: bool=False, 
                       merge_output: bool=True,
                       weight_position: float=None,
                       weight_multipliers: np.ndarray=None) -> List[Dict]:
    """Compute Prominence
    
    Computes prominence of entity clusters.

    Args:
        clusters (List[Dict]): Entity clusters.
        to_dataframe (bool, optional): Export output
            as pandas dataframe? Defaults to False.
        merge_output (bool, optional): Merge resulting 
            cluster meta data with input data. Defaults to True.
        weight_position: threshold for position-adjusted
            weight interpolation. Defaults to None implying
            no adjustment for positions in text.
        weight_multipliers: weight multipliers. 

    Returns:
        List[Dict]: clusters and their prominence.
        
    Examples:
        ...
    """
    # handle trivial case (empty list)
    if len(clusters) == 0:
        if to_dataframe:
            return pd.DataFrame()
        else:
            return []
    
    # validate inputs
    if weight_position is not None:
        assert 0 <= weight_position <= 1, "choose 'weight_position' between 0 and 1"
    if weight_multipliers is not None:
        assert len(weight_multipliers)==len(clusters), "Multipliers must have same length as number of entities"
    else:
        weight_multipliers = float(1)
        
    clusters = pd.DataFrame.from_dict(clusters)
    
    prominence = clusters.copy() 
    prominence_score = float(1)
    
    # adjust prominence score for word positions (=offsets)
    if weight_position is not None:
        if len(clusters.start) > 1:
            offset_min = min(clusters.start)
            offset_max = max(clusters.start)
            # linear interpolation
            xp = [offset_min, offset_max]
            yp = [1, weight_position]
            prominence_position = np.array([np.interp(x, xp, yp) for x in clusters.start])
    else: 
        prominence_position = float(1)
    
    prominence_score = prominence_score * prominence_position * weight_multipliers
    
    # aggregate prominence to group level
    prominence['prominence_score'] = prominence_score
    prominence = prominence.groupby(CLUSTER_ID)['prominence_score'].sum()
    
    # rank clusters by prominence
    ranks = rankdata(prominence, method = "max")
    ranks = max(ranks) - ranks + 1

    # organize output as data frame
    prominence = pd.DataFrame(prominence)
    prominence['prominence_rank'] = ranks 
    prominence.reset_index(level=0, inplace=True) 
        
    if merge_output:
        prominence = pd.merge(clusters, prominence, how="left")
        
    if not to_dataframe:
        prominence = prominence.to_dict(orient="records")
    
    return prominence

def compute_prominence_bygroup(clusters: List[Dict], 
                               **kwargs) -> List[Dict]:
    """Compute Prominence by Group
    
    Computes prominence by entity group. Simply 
    calls compute_prominence() groupwise.

    Args:
        clusters (List[Dict]): Entity clusters.
        kwargs: all optional arguments for 
            compute_prominence().

    Returns:
        List[Dict]: entity clusters with 
            prominence scores.
    """
    # handle trivial case.
    if len(clusters) == 0:
        return []
    
    clusters = pd.DataFrame.from_dict(clusters)
    clusters = clusters.groupby(['entity_group'])
    
    out = [compute_prominence(clusters = clusters.get_group(group).to_dict(orient="records"), **kwargs) for group in clusters.groups]
    
    out = flatten(out)
    
    return out

#test = {'entity_group': ["PER", "PER", "LOC"], 'word': ['abe', 'abe', 'kat']}
#tester = pd.DataFrame.from_dict(test)
#tester = tester.to_dict(orient="records")
#fuzzy_cluster_bygroup(tester)



