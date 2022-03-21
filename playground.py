import timeit

from rapidfuzz.fuzz import partial_token_set_ratio
from rapidfuzz.process import cdist
import pandas as pd
import numpy as np
import boto3

from fuzzup.fuzz import (
    fuzzy_cluster, 
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

# simulate data
test_data = [{'word': 'Viborg', 'entity_group': 'LOC', 'cluster_id' : 'A'}, 
             {'word': 'Uldum', 'entity_group': 'ORG', 'cluster_id' : 'B'},
             {'word': 'Solgårde', 'entity_group': 'LOC', 'cluster_id' : 'C'}]

# cluster data
clusters = fuzzy_cluster(test_data)

# initiate relevant whitelists
c = Cities()
m = Municipalities()
n = Neighborhoods()
    
# Apply whitelists 
out = apply_whitelists([c,m,n], 
                       clusters, 
                       score_cutoff=90)

#### Format output 
# set desired columns
cols = ['neighborhood_code', 'city_code', 'municipality_code']

# format output
out = format_output(out,
                    columns = cols,
                    drop_duplicates=True)

# .. then maybe convert to strings
out.to_csv(header=None, index=False).strip('\n').split('\n')
                
                        
            
            
            
            

    
    
    



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










    


    











