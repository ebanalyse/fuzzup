import timeit
import time

from rapidfuzz.fuzz import (
    ratio,
    token_ratio,
    token_set_ratio,
    token_sort_ratio,
    partial_token_set_ratio,
    partial_token_sort_ratio,
    partial_ratio_alignment,
    partial_ratio,
    WRatio,
    QRatio
    )
import pandas as pd
import numpy as np
import pickle
import boto3

from fuzzup.fuzz import fuzzy_cluster, compute_prominence, match_whitelist
from fuzzup.whitelists import get_danish_politicians

def load_preds_from_s3(file="ner_preds_v1.pickle"):

    s3 = boto3.resource('s3')
    preds = pickle.loads(s3.Bucket("nerbonanza").Object(file).get()['Body'].read())
    
    return preds
   
ner_preds = load_preds_from_s3()

# danish company names (for white list)
def load_danish_companies(file="companies-name-municipality.json"):
    s3 = boto3.resource('s3')
    companies = pd.read_json(s3.Bucket("nerbonanza").Object(file).get()['Body'])
    return companies

# whitelist
# companies = load_danish_companies()
# whitelist = companies.name.tolist()
whitelist = list(get_danish_politicians().keys())

# run random article
def run_random(ner_preds):
    example = ner_preds.sample(n=1)
    preds = example['body_preds'].values[0]
    if len(preds) == 0:
        return np.nan
    text =  example.body.values[0]

    clusters, _ = fuzzy_cluster(preds, 
                                scorer=partial_token_set_ratio, 
                                workers=4,
                                cutoff=75,
                                merge_output=True)
    #pd.DataFrame.from_dict(clusters)

    clusters = compute_prominence(clusters, 
                                  merge_output=True,
                                  weight_position=.5)
    t1 = time.time()
    
    clusters = match_whitelist(clusters,
                               whitelist=whitelist,
                               score_cutoff=90,
                               merge_output=True,
                               aggregate_cluster=True,
                               workers=1)
    
    t2 = time.time()

    clusters = pd.DataFrame.from_dict(clusters).sort_values(by ="prominence_rank")
    
    print(example.content_id.tolist()[0]) 
    print(text)
    print(clusters)
    
    return t2-t1

n_trials = 500
timings = [run_random(ner_preds) for x in range(n_trials)]
print(f"Avg. time for {n_trials} trials: {np.round(np.nanmean(timings), 4)}s")
print(f"Median time for {n_trials} trials: {np.round(np.nanmedian(timings), 4)}s")








