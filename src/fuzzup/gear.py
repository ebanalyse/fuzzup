import pandas as pd
from fuzzywuzzy import fuzz
import numpy as np
import scipy.cluster.hierarchy as spc
from scipy.stats import rankdata
from itertools import compress
from typing import Callable

def compute_fuzzy_matrix(strings: list, ratio: Callable = None) -> pd.DataFrame:
    """Compute Matrix with Fuzzy Ratios

    Computes matrix with mutual fuzzy ratios for strings.

    Args:
        strings (list): Strings to compute mutual fuzzy ratios
            for.
        ratio (Callable, optional): What type of fuzzy ratios
            to compute. Defaults to None, in which case 
            `fuzz.partial_ratio` from `fuzzywuzzy` is applied.

    Returns:
        pd.DataFrame: Cross-tabular matrix with mutual fuzzy
        ratios for strings.

    Examples:
        >>> from fuzzup.gear import compute_fuzzy_matrix
        >>> strings = ['biden', 'joe biden', 'donald trump']
        >>> compute_fuzzy_matrix(strings) 

    """  

    if ratio is None:
        ratio = fuzz.partial_ratio

    # subset unique strings.
    strings = list(set(strings))

    # create data frame with strings and corresponding ids.
    df = pd.DataFrame({'id': np.arange(len(strings)),
                       'strings' : strings})

    # pre-allocate Cross-Tabular data frame.
    ct = pd.crosstab(df['strings'], df['strings'])

    # compute fuzzy ratios and fill out matrix.
    ct = ct.apply(lambda col: [ratio(col.name, x) for x in col.index])

    return ct

def form_clusters(df: pd.DataFrame, 
                  args_cluster: dict = {'criterion': 'distance'},
                  args_linkage: dict = {'method': 'complete',
                                        'metric': 'euclidean'},
                  args_pdist: dict = {'metric': 'euclidean'}, 
                  flatten_coef: float = 0.5) -> list:
    """Forms Clusters of Strings

    Forms clusters of strings from fuzzy ratios using 
    hierarchical clustering.

    Args:
        df (pd.DataFrame): Matrix with mutual fuzzy ratios between
            strings.
        args_cluster (dict, optional): Arbitrary arguments for 
            hierarchical clustering algorithm 
            `scipy.cluster.hierarchy.fcluster`.
            Defaults to {'criterion': 'distance'}.
        args_linkage (dict, optional): Arguments for how to
            compute linkage between clusters with 
            `scipy.cluster.hierarchy.linkage`. Defaults to 
            {'method': 'complete', 'metric': 'euclidean'}.
        args_pdist (dict, optional): Arguments for how to
            compute pairwise distances between observations with
            `scipy.cluster.hierarchy.distance.pdist`. Defaults 
            to {'metric': 'euclidean'}.
        flatten_coef (float, optional): Threshold value for deciding 
            the number of clusters to form. The generic threshold
            is computed as this coefficient multiplied with the 
            maximum pairwise distance between two observations. 
            Defaults to 0.5.

    Returns:
        list: clusters of strings.

    Examples:
        >>> from fuzzup.gear import compute_fuzzy_matrix, form_clusters
        >>> strings = ['biden', 'joe biden', 'donald trump', 'D. Trump']
        >>> ratios = compute_fuzzy_matrix(strings) 
        >>> form_clusters(ratios)
    """

    # compute pairwise distances between observations.
    pdist = spc.distance.pdist(df.values, **args_pdist)
    
    # perform hierarchical clustering.
    linkage = spc.linkage(pdist, **args_linkage)
    
    # form flat clusters from hierarchical clustering.
    cluster_idx = spc.fcluster(linkage, flatten_coef * pdist.max(), **args_cluster)

    # extract entities from column names.
    ents = df.columns.values

    # organize entities in clusters.
    clusters = []
    unique_clusters = set(cluster_idx)
    for i in unique_clusters:
        belongs_to_cluster = cluster_idx == i
        cluster = list(compress(ents, belongs_to_cluster))
        clusters.append(list(cluster))

    return clusters

def form_clusters_and_rank(strings: list, 
                           ratio: Callable = None, 
                           args_cluster: dict = {'criterion': 'distance'},
                           args_linkage: dict = {'method': 'complete',
                                                 'metric': 'euclidean'},
                           args_pdist: dict = {'metric': 'euclidean'},
                           flatten_coef: float = 0.5) -> list:
    """Form and Rank Clusters of Strings

    Form clusters of strings using Fuzzy Matching in 
    conjunction with hierarchical clustering. Clusters are
    then ranked by counting number of nodes (strings) in 
    each cluster.
    
    Args:
        strings (list): strings to form clusters from.
        ratio (function, optional): Defaults to None, in which case 
            `fuzz.partial_ratio` from `fuzzywuzzy` is applied. 
        args_cluster (dict, optional): Arbitrary arguments for 
            hierarchical clustering algorithm 
            `scipy.cluster.hierarchy.fcluster`.
            Defaults to {'criterion': 'distance'}.
        args_linkage (dict, optional): Arguments for how to
            compute linkage between clusters with 
            `scipy.cluster.hierarchy.linkage`. Defaults to 
            {'method': 'complete', 'metric': 'euclidean'}.
        args_pdist (dict, optional): Arguments for how to
            compute pairwise distances between observations with
            `scipy.cluster.hierarchy.distance.pdist`. Defaults 
            to {'metric': 'euclidean'}.
        flatten_coef (float, optional): Threshold value for deciding 
            the number of clusters to form. The generic threshold
            is computed as this coefficient multiplied with the 
            maximum pairwise distance between two observations. 
            Defaults to 0.5.
        
    Returns:
        list: clusters of strings.

    Examples:
        >>> from fuzzup.gear import form_clusters_and_rank
        >>> strings = ['biden', 'joe biden', 'donald trump']
        >>> form_clusters_and_rank(strings) 
    """

    if ratio is None:
        ratio = fuzz.partial_ratio

    # extract unique strings
    strings_unique = list(set(strings))

    if len(strings_unique) > 1:
        # compute matrix with fuzzy ratios.
        fuzzy_matrix = compute_fuzzy_matrix(strings_unique, ratio)
    
        strings_clusters = form_clusters(fuzzy_matrix, 
                                         args_cluster = args_cluster,
                                         args_pdist = args_pdist,
                                         args_linkage = args_linkage,
                                         flatten_coef = flatten_coef)
    else:
        # handle trivial case of only one entity.
        strings_clusters = [strings]

    # compute cluster meta data.
    promoted_strings = [max(cluster, key = len) for cluster in strings_clusters]
    counts = list(map(lambda x: np.sum([ent in x for ent in strings]), strings_clusters))
    ranks =  rankdata(counts, method = "min")
    ranks = max(ranks) - ranks + 1

    # organize data.
    headers = ["PROMOTED_STRING", "STRINGS", "COUNT", "RANK"]
    clusters = [dict(zip(headers, z)) for z in zip(promoted_strings, strings_clusters, counts, ranks)]

    return clusters

if __name__ == '__main__':
    strings = ['biden', 'joe biden', 'donald trump']
    form_clusters_and_rank(strings) 
