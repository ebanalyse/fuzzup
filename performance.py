from multiprocessing.sharedctypes import Value
import pandas as pd
from collections import defaultdict
from tqdm import tqdm
from typing import List, Dict
import numpy as np
from fuzzup.fuzz import fuzzy_cluster_bygroup, fuzzy_cluster, compute_prominence_bygroup
from rapidfuzz.fuzz import partial_token_set_ratio, ratio
from bayes_opt import BayesianOptimization, UtilityFunction

PARAMS = {'weight_pos' : 0.75,
          'cutoff': 0.90,
          'scorer':ratio
          }

train = pd.read_csv('./prominence_dataset.csv')

def _predict(preds:List[Dict]) -> Dict:
    global PARAMS
    res = defaultdict(lambda:{})
    fuzzy_preds = fuzzy_cluster_bygroup(preds, cutoff = PARAMS['cutoff'], scorer=PARAMS['scorer'])
    fuzzy_preds = compute_prominence_bygroup(fuzzy_preds, weight_position = PARAMS['weight_pos'])
    
    for i, fuzzy_pred in enumerate(fuzzy_preds):
        res[i].update({'word':fuzzy_pred['word'],'pred':fuzzy_pred['cluster_id'],'true_value':fuzzy_pred['true_value'], 'prominence_rank':fuzzy_pred['prominence_rank'], 'prominent': fuzzy_pred['prominent']})
    return res

def process_dataset(train: pd.DataFrame) -> List[Dict]:
    preds_dict = defaultdict(lambda: {})
    with tqdm(total=train['content_id'].nunique()) as pbar:
        for article in np.unique(train['content_id']):
            pbar.update(1)
            preds_list = []
            for index,row in train[train['content_id']==article].iterrows():
                row['true_value'] = row['main_entity']
                preds_list.append(dict(row))
            preds_dict[article].update(_predict(preds_list))
    return preds_dict  

def evaluate_fuzzy_matching(preds_dict: Dict, mode: str = 'jaccard') -> float:
    """ Just loops through the preds dict and aggregates their evaluations"""
    
    if mode == 'jaccard':
        accuracies = {}
        diagnosis_dict = {}
        for article in preds_dict.keys():
            preds_set = set()
            true_set = set()
            for preds in preds_dict[article].values():
                preds_set.add(preds['pred'].lower())
                true_set.add(preds['true_value'].lower())
            if len(preds_set) != 0 and len(true_set) != 0:
                accuracy = round(len(preds_set.intersection(true_set))/len(preds_set.union(true_set)),2)
                if len(preds_set-true_set) != 0 :
                    diagnosis_dict[article] = {'preds_set': preds_set, 'true_set': true_set, 'misses': preds_set-true_set}
            else: 
                pass
            accuracies[article] = accuracy
        return sum(accuracies.values()) / len(accuracies), diagnosis_dict # Return the mean accuracy of all jaccard indices
       
    elif mode =='dice':
        res = {}
        
        for article in preds_dict.values():
            pred_set = set()
            true_set = set()
            for preds in article.values():            
                if preds['pred'] not in pred_set:
                    pred_set.add(preds['pred'])
                if preds['true_value'] not in true_set:
                    true_set.add(preds['true_value'])
            dice_similarity = (2 * len(np.intersect1d(pred_set,true_set)))/(len(pred_set)**2 + len(true_set)**2)
            
    else: 
        raise ValueError('Please set mode arg to either "jaccard" or "dice"')

def evaluate_prominence(preds_dict: Dict, mode: str = 'jaccard') -> float:    
    if mode == 'dice':
        pass
    
    elif mode == 'fuzzy_pred':
        pass
    
    else:
        raise ValueError('Pleaes pass mode string as either "dice" or "jaccard"')
preds_dict = process_dataset(train)
accuracy, diagnosis_dict = evaluate_fuzzy_matching(preds_dict)

