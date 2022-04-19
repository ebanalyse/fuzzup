import timeit
import logging

from rapidfuzz.fuzz import partial_token_set_ratio, WRatio
from rapidfuzz.process import cdist
import pandas as pd
import numpy as np
import boto3
from fuzzup.utils import validate_location_distances

from fuzzup.fuzz import (
    fuzzy_cluster_bygroup, 
    compute_prominence,
)
from fuzzup.whitelists import (
    Cities, 
    Municipalities, 
    Neighborhoods, 
    apply_whitelists,
    format_output
)
from fuzzup.fuzz import fuzzy_cluster

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# simulate data
test_data = [{'word': 'Holbæk', 'entity_group': 'LOC', 'cluster_id' : 'Holbæk'}, 
             {'word': 'Vipperød', 'entity_group': 'ORG', 'cluster_id' : 'Vipperød'},
             {'word': 'Vipperød', 'entity_group': 'LOC', 'cluster_id' : 'Vipperød'}]

# cluster data
clusters = fuzzy_cluster_bygroup(test_data)

# initiate relevant whitelists
c = Cities()
m = Municipalities()
n = Neighborhoods()
    
# Apply whitelists 
out = apply_whitelists([c,m,n], 
                       clusters, 
                       score_cutoff=98,
                       scorer=WRatio)

if validate_location_distances(out, distance_treshold = 1):
    #### Format output 
    # set desired columns
    cols = ['municipality_id', 'eblocal_id', 'dawa_id']

    # format output
    out = format_output(out,
                        columns = cols,
                        drop_duplicates=True)

    # .. then maybe convert to strings
    out.to_csv(header=None, index=False).strip('\n').split('\n')
    print(out)
else:
    print('No matches found')


#### WITH NER PIPELINE

# download and unzip model
#import awswrangler as wr
#import shutil
#wr.s3.download(path='s3://auto-training-artifact-bucket/ner/0.0.8/Bizou.zip', local_file='./Bizou.zip')                        
#shutil.unpack_archive("Bizou.zip")            

# load model
from ner.inference.predicter import NERPredicter
predicter = NERPredicter()
predicter.load_model('saattrupdan/nbailab-base-ner-scandi')
predicter.predict(text='Jens Hansen har en bondegård i Skals', sentence_based=True)

def get_news_data(content_ids,
                  cols=["article_id", "title", "lead", "body"]):

    # prep params for query
    content_ids = list(filter(lambda x: x != "", content_ids))
    content_ids = set(content_ids)
    n_content_ids = len(content_ids)
    content_ids = ", ".join([str(id) for id in content_ids])

    cols = ', '.join(cols)

    # form sql query
    query = f"""
    SELECT 
    {cols}
    FROM
    manual_escenic_articles
    WHERE
    article_id IN ({content_ids})
    ORDER BY publish_time DESC
    """
    
    logger.info(f"Querying data for {n_content_ids} news articles with columnns {cols} from data lake...")
    
    # submit query
    df = wr.athena.read_sql_query(
        sql=query,
        database="manual-recsys", 
        use_threads=True,
        # chunksize=True
        )
    
    # enforce only unique article_ids
    df = df.drop_duplicates(subset=["article_id"])
    df = df[df['section_path'].str.len() > 0]
    
    logger.info(f"Extracted news data successfully for {len(df)}/{n_content_ids} content ids")
    # formatting
    df['article_id'] = df['article_id'].astype(str)   
    
    # TODO: output dict with article id as key 
    
    return df

get_news_data([9150838],
              cols=["article_id", "title", "subtitle", "body_text"])
 
            

    
    
    



# cities = c(clusters, aggregate_cluster=True, score_cutoff=95)
# municipalities = m(clusters, score_cutoff=95) 
# neighborhoods = n(clusters, score_cutoff=95) 
# 
# def load_danish_companies(file="companies-name-municipality.json"):
#     s3 = boto3.resource('s3')
#     companies = pd.read_json(s3.Bucket("nerbonanza").Object(file).get()['Body'])
#     return companies
# 
# #### SIMULATE DATA
# PERSONS = ['Donald Trump', 'Donald Trump', 
#            'J. biden', 'joe biden', 'Biden', 
#            'Bide', 'mark esper', 'Christopher c . miller', 
#            'jim mattis', 'Nancy Pelosi', 'trumps',
#            'Trump', 'Donald', 'miller']
# 
# # ALIGN WITH HUGGINGFACE 'TRANSFORMERS' NER PIPELINE OUTPUT FORMAT
# n = len(PERSONS)
# PERSONS_NER = pd.DataFrame(data = PERSONS, columns=['word'])
# PERSONS_NER["entity_group"] = "PER"
# PERSONS_NER["score"] = np.random.sample(n)
# PERSONS_NER["start"] = np.random.randint(100, size=n)
# PERSONS_NER["end"] = np.random.randint(100, size=n)
# PERSONS_NER = PERSONS_NER.to_dict(orient="records")
# 
# #### FUZZUP WORKFLOW
# clusters = fuzzy_cluster(PERSONS_NER, 
#                          scorer=partial_token_set_ratio, 
#                          workers=2,
#                          cutoff=70,
#                          merge_output=True)
# pd.DataFrame.from_dict(clusters)
# 
# clusters = compute_prominence(clusters, 
#                               merge_output=True)
# pd.DataFrame.from_dict(clusters)
# 
# whitelist = ["Donald Trump", "Joe Biden"]
#    
# companies = load_danish_companies()
# company_names = companies.name.tolist()
# 
# # match with whitelists
# match_whitelist(words=clusters, 
#                 whitelist=company_names,
#                 merge_output=True,
#                 aggregate_cluster=True,
#                 to_dataframe=True,
#                 score_cutoff=80,
#                 scorer=partial_token_set_ratio)
# 
# import pandas as pd
# d = {'x': [1,2,3], 'g': [[], [], []]}
# df = pd.DataFrame.from_dict(d)
# df[df['g'].astype(str) != '[]']










    


    











