import pandas as pd
from fuzzup.fuzz import fuzzy_cluster, fuzzy_cluster_bygroup
from typing import List,Dict,Any
from tqdm import tqdm
import numpy as np
from collections import defaultdict
import logging
from rapidfuzz.fuzz import partial_token_set_ratio, ratio
#TODO: Get accuracies for each entity_type
#TODO: Filter out observations that only occur one time, to get accuracy in complex situations.

logger = logging
#DATASET TO TEST ON
df = pd.read_csv('./prominence_dataset.csv')

# train_test split
train=df.sample(frac=.80,random_state=200) #random state is a seed value
train = train.dropna()

def filter_low_freq_entities(train: pd.DataFrame) -> pd.DataFrame:
    #Group and find all main_entity that for an article, occurs more than once.
    filter_train = train.groupby(['content_id', 'word'])['main_entity'].count().reset_index()
    
    #Filter them out
    filter_train = filter_train[filter_train.main_entity <= 1]
    
    #Get tuple groups of content_id and words that we want to keep
    filter_train = filter_train.groupby(['content_id','word']).groups

    train = train[[p not in filter_train for p in zip(train['content_id'], train['main_entity'])]]
    return train

#train = filter_low_freq_entities(train)

train['content_id'] = train.content_id.astype('int')
test=df.drop(train.index)

def _predict(preds:List[Dict]) -> Dict:
    res = defaultdict(lambda:{})
    fuzzy_preds = fuzzy_cluster_bygroup(preds, cutoff = 95, scorer=partial_token_set_ratio)
    for i, fuzzy_pred in enumerate(fuzzy_preds):
        res[i].update({'word':fuzzy_pred['word'],'pred':fuzzy_pred['cluster_id'],'true_value':fuzzy_pred['true_value']})
    return res

def _filter_single_clusters(article):
    word_freq = {}
    for index, row in article.iterrows():
        word_freq[article['word']] += 1
    
# Predict on train
def process_dataset() -> List[Dict]:
    logger.info('----------------------------------------------------------------PROCESSING DATASET ----------------------------------------------------------------')
    preds_dict = defaultdict(lambda: {})
    with tqdm(total=train['content_id'].nunique()) as pbar:
        for article in np.unique(train['content_id']):
            pbar.update(1)
            preds_list = []
            for index,row in train[train['content_id']==article].iterrows():
                pred = {'entity_group': row['entity_group'], 'word': row['word'], 'start': row['start'], 'end': row['end'], 'true_value': row['main_entity']}            
                preds_list.append(pred)
            preds_dict[article].update({'item':_predict(preds_list)})
    return preds_dict    

def evaluate_predictions(preds_dict: Dict) -> None:
    total_preds = 0
    true_preds = 0
    
    for article_id in preds_dict.keys():
        d_dict = preds_dict[article_id]['item']
        for val in d_dict.values():
            total_preds+=1
            #Lowering is kinda.. but the labelling is not always case sensitive.
            if val['pred'].lower() == val['true_value'].lower():
                true_preds += 1
            else:
                print(val)
                pass
                                
    print(f'ACCURACY: {(true_preds/total_preds)*100}%')            
    print(f'\n#Correct prediction: {true_preds}')
    print(f'\n#Wrong Prediction: {total_preds-dtrue_preds}')
preds_dict = process_dataset()
evaluate_predictions(preds_dict)
__import__('pdb').set_trace()
#{'pred': 'Hjerneskadeforeningen', 'true_value': 'Hjerteforeningen'}
#train[['content_id', 'word','main_entity']][train.content_id == 4134608]
