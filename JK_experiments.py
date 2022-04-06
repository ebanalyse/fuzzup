import pandas as pd
from collections import defaultdict
from tqdm import tqdm
from typing import List, Dict
import numpy as np
from fuzzup.fuzz import fuzzy_cluster_bygroup, fuzzy_cluster, compute_prominence_bygroup
from rapidfuzz.fuzz import partial_token_set_ratio, ratio

# simulate data
# data = {'word': ["Mette", "Mette Frederiksen", "Morten Messerchmidt"],
#         'cluster_pred': ['x', 'x', 'x'],
#         'cluster_true': ['a', 'a', 'a']}

# replace 'cluster_pred' with 'cluster_id' and 'cluster_true' with 'main_entity'
# df = pd.DataFrame.from_dict(data)

"""

Known hurdles in here..

1) If you use bygroup, it will reward the model a lot, regardless of cutoff
because there are many datapoints, where there is only 1 unique loc, per, etc. 
might need to filter out these datapoints?

Returns:
    _type_: _description_
"""
ACCURACIES = {}
HITS = 0
MISSES = 0

PROM_HIT = 0
PROM_MISS = 0

train = pd.read_csv('./prominence_dataset.csv')

# Fuzzy Params
WEIGHT_POS = 0.5
CUTOFF = 90
SCORER = ratio

def _predict(preds:List[Dict]) -> Dict:
    res = defaultdict(lambda:{})
    fuzzy_preds = fuzzy_cluster_bygroup(preds, cutoff = CUTOFF, scorer=SCORER)
    fuzzy_preds = compute_prominence_bygroup(fuzzy_preds, weight_position = None)
    
    for i, fuzzy_pred in enumerate(fuzzy_preds):
        res[i].update({'word':fuzzy_pred['word'],'pred':fuzzy_pred['cluster_id'],'true_value':fuzzy_pred['true_value'], 'prominence_rank':fuzzy_pred['prominence_rank'], 'prominent': fuzzy_pred['prominent']})
    return res

def process_dataset() -> List[Dict]:
    preds_dict = defaultdict(lambda: {})
    with tqdm(total=train['content_id'].nunique()) as pbar:
        for article in np.unique(train['content_id']):
            pbar.update(1)
            preds_list = []
            for index,row in train[train['content_id']==article].iterrows():
                pred = {'entity_group': row['entity_group'], 'word': row['word'], 'start': row['start'], 'end': row['end'], 'true_value': row['main_entity'], 'prominent': row['prominent']}            
                preds_list.append(pred)
            preds_dict[article].update(_predict(preds_list))
    return preds_dict  

def process_preds_dict(preds_dict : Dict):
    global ACCURACIES
    for article in preds_dict.keys():
        word = []
        cluster_pred = []
        cluster_true = []
        cluster_prom = []
        cluster_prom_pred = []
        for val in preds_dict[article].values():
            word.append(val['word'])
            cluster_pred.append(val['pred'])
            cluster_true.append(val['true_value'])
            cluster_prom.append(val['prominent'])
            cluster_prom_pred.append(val['prominence_rank'])
        data = {'word': word,'cluster_pred':cluster_pred,'cluster_true':cluster_true, 'prominent':cluster_prom, 'prominence_rank': cluster_prom_pred}
        ACCURACIES[article] = {'performance':compute_hits_misses(data),'mismatches': set(cluster_pred)-set(cluster_true)}
    
# count most frequent cluster label
def highest_frequency_group(x, col="cluster_pred"):
    out = x[col].value_counts()[0]
    return out

def retrieve_bow(bow_pred: List, bow_true: List):
    bow_pred = set(bow_pred)
    bow_true = set(bow_true)
    hits = 0
    misses = 0
    
    for true_val in bow_true:
        if true_val in bow_pred:
            hits += 1
        else:
            misses +=1
    if misses > 0:
        print(bow_pred - bow_true)
        pass
    return (hits, misses)

def compute_most_prominent_loc(df: pd.DataFrame):
    """This Method will compute whether the identified most prominent entity,
    really is the most prominent.

    Args:
        data (Dict): Dictionary of data to evaluate

    Returns:
        int: some measure of accuracy 
        """
    global PROM_MISS
    global PROM_HIT    
    
    #Make sure we only look at what hte model says is the most prominent.
    df = df[df['prominence_rank'] == 1]
    
    for index, row in df.iterrows():
        if int(row['prominence_rank']) == int(row['prominent']):
            PROM_HIT += 1
        else:
            PROM_MISS += 1                
        
    
def compute_hits_misses(data: Dict):
    df = pd.DataFrame.from_dict(data)
    compute_most_prominent_loc(df)
    global HITS
    global MISSES
    
    bow_pred = []
    bow_true = []
    
    # compute label frequencies for each true cluster
    for index, row in df.iterrows():
        bow_pred.append(row['cluster_pred'].lower())
        bow_true.append(row['cluster_true'].lower())
    hits, misses = retrieve_bow(bow_pred = bow_pred, bow_true = bow_true)
    HITS += hits
    MISSES += misses
    return hits, misses
preds_dict = process_dataset()  

process_preds_dict(preds_dict)

print(f"# Hits: {HITS}, # Misses: {MISSES}, Modified accuracy: {round(HITS/(HITS+MISSES), 2)}")
print(f"# Prominent hits: {PROM_HIT}, # Prominent Miss: {PROM_MISS}, Modified accuracy: {round(PROM_HIT/(PROM_HIT+PROM_MISS), 2)}")

__import__('pdb').set_trace()