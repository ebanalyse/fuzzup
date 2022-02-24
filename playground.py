import timeit

from rapidfuzz.fuzz import partial_token_set_ratio
import pandas as pd
import numpy as np

from fuzzup.fuzz import fuzzy_cluster, compute_prominence

#### SIMULATE DATA
PERSONS = ['Donald Trump', 'Donald Trump', 
           'J. biden', 'joe biden', 'Biden', 
           'Bide', 'mark esper', 'Christopher c . miller', 
           'jim mattis', 'Nancy Pelosi', 'trumps',
           'Trump', 'Donald', 'miller'
           ]
# SAME FORMAT AS FROM NER-PIPELINE
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
                              merge_output=True,
                              weight_position=.5)
pd.DataFrame.from_dict(clusters)

# PERFORMANCE TESTING
#def test():
#    return fuzzy_cluster(PERSONS, scorer=partial_token_set_ratio)
#
## computational performance
#n_trials = 100
#timeit.timeit(test, number=n_trials)/n_trials
