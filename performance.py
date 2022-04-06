from multiprocessing.sharedctypes import Value
import pandas as pd
from collections import defaultdict
from tqdm import tqdm
from typing import List, Dict, Callable
import numpy as np
from fuzzup.fuzz import fuzzy_cluster_bygroup, fuzzy_cluster, compute_prominence_bygroup
from rapidfuzz.fuzz import (
    ratio,
    partial_ratio,
    partial_ratio_alignment,
    token_sort_ratio,
    partial_token_sort_ratio,
    token_set_ratio,
    partial_token_set_ratio,
    token_ratio,
    partial_token_ratio,
    WRatio,
    QRatio,
)

FUZZUP_SCORERS = {
    0: ratio,
    1: partial_ratio,
    2: partial_token_set_ratio,
}

import matplotlib.pyplot as plt

from bayes_opt import BayesianOptimization, UtilityFunction

train = pd.read_csv('./prominence_dataset.csv')

def _predict(preds:List[Dict], cutoff,scorer, weight_pos) -> Dict:
    res = defaultdict(lambda:{})
    fuzzy_preds = fuzzy_cluster_bygroup(preds, cutoff = cutoff, scorer=FUZZUP_SCORERS[scorer])
    fuzzy_preds = compute_prominence_bygroup(fuzzy_preds, weight_position = weight_pos)
    
    for i, fuzzy_pred in enumerate(fuzzy_preds):
        res[i].update({'word':fuzzy_pred['word'],'pred':fuzzy_pred['cluster_id'],'true_value':fuzzy_pred['true_value'], 'prominence_rank':fuzzy_pred['prominence_rank'], 'prominent': fuzzy_pred['prominent']})
    return res

def process_dataset(train: pd.DataFrame, cutoff, scorer, weight_pos = 1) -> List[Dict]:
    preds_dict = defaultdict(lambda: {})
    with tqdm(total=train['content_id'].nunique()) as pbar:
        for article in np.unique(train['content_id']):
            pbar.update(1)
            preds_list = []
            for index,row in train[train['content_id']==article].iterrows():
                row['true_value'] = row['main_entity']
                preds_list.append(dict(row))
            preds_dict[article].update(_predict(preds_list, cutoff,scorer, weight_pos))
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
    hits = 0
    misses = 0
    
    for article in preds_dict.values():
        for preds in article.values():            
            if preds['prominent'] == 1:
                if preds['prominence_rank'] == 1:
                    hits += 1
                else:
                    misses+=1
            else:
                pass
            
    return round(hits/(hits+misses), 2)

def plot_results(optimizer):
    print("Best result: {}; f(x) = {:.3f}.".format(optimizer.max["params"], 
                                            optimizer.max["target"]))

    plt.figure(figsize = (15, 5))
    plt.plot(range(1, 1 + len(optimizer.space.target)), optimizer.space.target, "-o")
    plt.grid(True)
    plt.xlabel("Iteration", fontsize = 14)
    plt.ylabel("Black box function f(x)", fontsize = 14)
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
    plt.show()
    
def train_fuzzy():
    def black_box_function(cutoff: int, scorer):
        preds_dict = process_dataset(train, cutoff=cutoff, scorer=scorer)
        accuracy, diagnosis_dict = evaluate_fuzzy_matching(preds_dict)
        return accuracy
    
    pbounds = {
            "cutoff": [0,100],
            "scorer": [0,len(FUZZUP_SCORERS)-1]
            }


    optimizer = BayesianOptimization(f = black_box_function,
                                    pbounds = pbounds, verbose = 2,
                                    random_state = 4)

    utility = UtilityFunction(kind="ucb", kappa = 1.96, xi = 0.01)

    #TRAINING LOOP
    for i in range(25):
        next_point = optimizer.suggest(utility)
        
        next_point['scorer'] = int(next_point['scorer'])
        
        target = black_box_function(cutoff = next_point['cutoff'], scorer = next_point['scorer'])
        
        try:
            optimizer.register(params=next_point, target=target)
        except:
            pass    
        print(f'TARGET: {target} \n')
        print(f'cutoff: {next_point["cutoff"]} \n  scorer: {FUZZUP_SCORERS[next_point["scorer"]]} ' )

    plot_results(optimizer)

def train_prominent():
    #prominence
    def black_box_function(weight_pos:float):
        preds_dict = process_dataset(train, cutoff=96.703, scorer=1, weight_pos = weight_pos)
        accuracy= evaluate_prominence(preds_dict)
        return accuracy

    pbounds = {
            "weight_pos":[0,1]
            }


    optimizer = BayesianOptimization(f = black_box_function,
                                    pbounds = pbounds, verbose = 2,
                                    random_state = 4)

    utility = UtilityFunction(kind="ucb", kappa = 1.96, xi = 0.01)

    #TRAINING LOOP
    for i in range(25):
        next_point = optimizer.suggest(utility)
        
        target = black_box_function(weight_pos = next_point['weight_pos'])
        
        try:
            optimizer.register(params=next_point, target=target)
        except:
            pass    
        print(f'TARGET: {target} \n')
        print(f'Weight_pos: {next_point["weight_pos"]}' )

    plot_results(optimizer)

train_prominent()
    
# preds_dict = process_dataset(train, cutoff = 0, scorer=ratio)
# accuracy, diagnosis_dict = evaluate_fuzzy_matching(preds_dict)

# print(f'ACCURACY: {accuracy} \n')
# print(f'Number of articles with incorrect predictions: {len(diagnosis_dict)}')


# optimizer.maximize()
# print("Best result: {}; f(x) = {}.".format(optimizer.max["params"], optimizer.max["target"]))

# __import__('pdb').set_trace()