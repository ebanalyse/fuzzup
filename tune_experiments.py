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
            if pbar.n==10:
                pass
    return preds_dict    
