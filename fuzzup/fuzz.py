from rapidfuzz.process import cdist, extract
import numpy as np
import pandas as pd
from scipy.stats import rankdata

def compute_fuzzy_matrix(strings: list,
                         **kwargs) -> pd.DataFrame:
    """Compute Matrix with pairwise edit distances
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

def fuzz_it_up(strings: str, 
               cutoff: int = 70, 
               to_dataframe: bool = True,
               **kwargs):

    # compute fuzzy ratios
    fuzzy_matrix = compute_fuzzy_matrix(strings, **kwargs)
    
    clusters = cluster_cutoff(fuzzy_matrix, 
                              cutoff=cutoff)
    
    # compute cluster meta data.
    promoted_strings = [max(cluster, key=len) for cluster in clusters]
    counts = list(map(lambda x: int(np.sum([ent in x for ent in strings])), clusters))
    ranks =  rankdata(counts, method = "max")
    ranks = max(ranks) - ranks + 1
    # convert to python native int
    ranks = [int(x) for x in ranks]

    # organize data.
    headers = ["ENTITY", "CLUSTER", "OCCURENCES", "PROMINENCE"]
    clusters = [dict(zip(headers, z)) for z in zip(promoted_strings, clusters, counts, ranks)]
    if to_dataframe:
        clusters = pd.DataFrame.from_dict(clusters)
        clusters.sort_values(by=['PROMINENCE'],
                             inplace=True)

    return clusters, fuzzy_matrix