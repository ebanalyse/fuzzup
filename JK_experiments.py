import pandas as pd
from collections import defaultdict
from tqdm import tqdm
from typing import List, Dict
import numpy as np
from fuzzup.fuzz import fuzzy_cluster_bygroup
from rapidfuzz.fuzz import partial_token_set_ratio

# # simulate data
# data = {'word': ["Mette", "Mette Frederiksen", "Morten Messerchmidt"],
#         'cluster_pred': ['x', 'x', 'z'],
#         'cluster_true': ['a', 'a', 'b']}

# # replace 'cluster_pred' with 'cluster_id' and 'cluster_true' with 'main_entity'
# df = pd.DataFrame.from_dict(data)

ACCURACIES = {}

HITS = 0

MISSES = 0

train = pd.read_csv('./prominence_dataset.csv')

def _predict(preds:List[Dict]) -> Dict:
    res = defaultdict(lambda:{})
    fuzzy_preds = fuzzy_cluster_bygroup(preds, cutoff = 1, scorer=partial_token_set_ratio)
    for i, fuzzy_pred in enumerate(fuzzy_preds):
        res[i].update({'word':fuzzy_pred['word'],'pred':fuzzy_pred['cluster_id'],'true_value':fuzzy_pred['true_value']})
    return res

def process_dataset() -> List[Dict]:
    preds_dict = defaultdict(lambda: {})
    with tqdm(total=train['content_id'].nunique()) as pbar:
        for article in np.unique(train['content_id']):
            pbar.update(1)
            preds_list = []
            for index,row in train[train['content_id']==article].iterrows():
                pred = {'entity_group': row['entity_group'], 'word': row['word'], 'start': row['start'], 'end': row['end'], 'true_value': row['main_entity']}            
                preds_list.append(pred)
            preds_dict[article].update(_predict(preds_list))
    return preds_dict  

def process_preds_dict(preds_dict : Dict):
    global ACCURACIES
    
    for article in preds_dict.keys():
        word = []
        cluster_pred = []
        cluster_true = []
        for val in preds_dict[article].values():
            word.append(val['word'])
            cluster_pred.append(val['pred'])
            cluster_true.append(val['true_value'])
        data = {'word': word,'cluster_pred':cluster_pred,'cluster_true':cluster_true}
        ACCURACIES[article] = compute_hits_misses(data)
                
# count most frequent cluster label
def highest_frequency_group(x, col="cluster_pred"):
    out = x[col].value_counts()[0]
    return out

def compute_hits_misses(data: Dict):
    global HITS
    global MISSES
    
    df = pd.DataFrame.from_dict(data)
    
    # compute label frequencies for each true cluster
    try:
        freqs = df.groupby('cluster_true').apply(highest_frequency_group)
    except KeyError:
        return None
    hits = sum(freqs)
    misses = len(df) - hits
    
    HITS += hits
    MISSES += misses
    
    return hits, misses

preds_dict = process_dataset()  

process_preds_dict(preds_dict)

print(f"# Hits: {HITS}, # Misses: {MISSES}, Modified accuracy: {round(HITS/(HITS+MISSES), 2)}")