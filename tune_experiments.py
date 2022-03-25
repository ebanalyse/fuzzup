import pandas as pd
from fuzzup.fuzz import fuzzy_cluster
from typing import List,Dict,Any
from tqdm import tqdm
import numpy as np
from collections import defaultdict
import logging

logger = logging
#DATASET TO TEST ON
df = pd.read_csv('./prominence_dataset.csv')

# train_test split
train=df.sample(frac=0.8,random_state=200) #random state is a seed value
train = train.dropna()
train['content_id'] = train.content_id.astype('int')
test=df.drop(train.index)

def _predict(preds:List[Dict]) -> Dict:
    res = defaultdict(lambda:{})
    fuzzy_preds = fuzzy_cluster(preds)
    for i, fuzzy_pred in enumerate(fuzzy_preds):
        res[i].update({'pred':fuzzy_pred['cluster_id'],'true_value':fuzzy_pred['true_value']})
    return res

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
            if val['pred'] == val['true_value']:
                true_preds += 1
            
    print(f'ACCURACY: {(true_preds/total_preds)*100}%')            
    print(f'\n#Correct prediction: {true_preds}')
    print(f'\n#Wrong Prediction: {total_preds-true_preds}')
preds_dict = process_dataset()
evaluate_predictions(preds_dict)
    