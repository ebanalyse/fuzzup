import timeit
import time
from itertools import compress

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
from fuzzup.whitelists import get_politicians, get_cities

def load_preds_from_s3(file="ner_preds_v1.pickle"):

    s3 = boto3.resource('s3')
    preds = pickle.loads(s3.Bucket("nerbonanza").Object(file).get()['Body'].read())
    
    return preds

# load ner predictions
id = None
s3 = boto3.resource('s3')
entities = pd.read_csv(s3.Bucket("nerbonanza").Object('entities.csv').get()['Body'])
articles = pd.read_csv(s3.Bucket("nerbonanza").Object('test_articles.csv').get()['Body'])

# danish company names (for white list)
def load_danish_companies(file="companies-name-municipality.json"):
    s3 = boto3.resource('s3')
    companies = pd.read_json(s3.Bucket("nerbonanza").Object(file).get()['Body'])
    return companies

#### WHITELIST EXPERIMENTS
# companies = load_danish_companies()
# whitelist = companies.name.tolist()
# whitelist = list(get_danish_politicians().keys())
whitelist = list(get_cities().keys())

# run random article
def run_random(articles, 
               entitites, 
               id=None,
               scorer=partial_token_set_ratio,
               cutoff=75
               ):
    
    if id is None:
        id = np.random.choice(articles.content_id.tolist())

    article = articles[articles.content_id == id]
    article = article[['content_id', 'title', 'lead', 'body']]
    article_ents = entities[entities.content_id == id]    
    article_ents = article_ents[article_ents.placement == "body"]
    preds = article_ents.to_dict(orient="records")

    t1 = time.time()
    
    clusters, _ = fuzzy_cluster(preds, 
                                scorer=scorer, 
                                workers=4,
                                cutoff=cutoff,
                                merge_output=True)
    #pd.DataFrame.from_dict(clusters)
    
    clusters = compute_prominence(clusters, 
                                  merge_output=True,
                                  weight_position=.5)
    
    # subset location entities (for matching with cities)
    locations = [x["entity_group"] == "LOC" for x in clusters]
    locations = list(compress(clusters, locations))
    clusters = locations
    
    clusters = match_whitelist(clusters,
                               whitelist=whitelist,
                               scorer=ratio,
                               score_cutoff=95,
                               merge_output=True,
                               aggregate_cluster=True,
                               workers=1)
    
    t2 = time.time()

    if len(clusters) > 0:
        clusters = pd.DataFrame.from_dict(clusters).sort_values(by ="prominence_rank")
    
    print(id)
    #print(article.title.tolist()[0]) 
    #print(article.lead.tolist()[0]) 
    print(article.body.tolist()[0]) 
    print(clusters)
    
    return t2-t1

run_random(articles, 
           entities,
           scorer=partial_token_set_ratio,
           cutoff=75)
#n_trials = 500
#timings = [run_random(articles, entities) for x in range(n_trials)]
#print(f"Avg. time for {n_trials} trials: {np.round(np.nanmean(timings), 4)}s")
#print(f"Median time for {n_trials} trials: {np.round(np.nanmedian(timings), 4)}s")








