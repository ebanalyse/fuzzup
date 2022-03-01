import timeit

from rapidfuzz.fuzz import partial_token_set_ratio
from rapidfuzz.process import cdist
import pandas as pd
import numpy as np

from fuzzup.fuzz import fuzzy_cluster, compute_prominence

#### SIMULATE DATA
PERSONS = ['Donald Trump', 'Donald Trump', 
           'J. biden', 'joe biden', 'Biden', 
           'Bide', 'mark esper', 'Christopher c . miller', 
           'jim mattis', 'Nancy Pelosi', 'trumps',
           'Trump', 'Donald', 'miller']

# ALIGN WITH HUGGINGFACE 'TRANSFORMERS' NER PIPELINE OUTPUT FORMAT
n = len(PERSONS)
PERSONS_NER = pd.DataFrame(data = PERSONS, columns=['word'])
PERSONS_NER["entity_group"] = "PER"
PERSONS_NER["score"] = np.random.sample(n)
PERSONS_NER["start"] = np.random.randint(100, size=n)
PERSONS_NER["end"] = np.random.randint(100, size=n)
PERSONS_NER = PERSONS_NER.to_dict(orient="records")

#### FUZZUP WORKFLOW
clusters, _ = fuzzy_cluster(PERSONS_NER, 
                            scorer=partial_token_set_ratio, 
                            workers=2,
                            cutoff=70,
                            merge_output=True)
pd.DataFrame.from_dict(clusters)

clusters = compute_prominence(clusters, 
                              merge_output=True)
pd.DataFrame.from_dict(clusters)

wl = ["Donald Trump", "Joe Biden"]

scorer = partial_token_set_ratio
words = [x.get('word') for x in clusters]

score_cutoff=80

dists = cdist(wl, 
              words, 
              scorer=scorer, 
              score_cutoff=score_cutoff)

wl = np.array(wl)

matches = [wl[np.where(col)] for col in dists.T]

df = pd.DataFrame.from_records(clusters)
df["matches"] = matches

def aggregate_to_cluster(x):
    res = np.unique(np.concatenate(x.matches.tolist()))
    return res

matches = pd.DataFrame(df.groupby(by=['cluster_id']).apply(aggregate_to_cluster), columns=['matches'], index=None)
matches = matches.reset_index()

df.drop('matches', axis=1, inplace=True)
pd.merge(df, matches, how="left")



    


    











