import timeit
from rapidfuzz.fuzz import partial_token_set_ratio
import pandas as pd
import numpy as np
from scipy.stats import rankdata

from fuzzup.fuzz import fuzzy_cluster, compute_prominence

PERSONS = ['Donald Trump', 'Donald Trump', 
           'J. biden', 'joe biden', 'Biden', 
           'Bide', 'mark esper', 'Christopher c . miller', 
           'jim mattis', 'Nancy Pelosi', 'trumps',
           'Trump', 'Donald', 'miller']
# OUTPUT IN THE SAME FORMAT AS FROM NER-PIPELINE
n = len(PERSONS)
PERSONS_NER = pd.DataFrame(data = PERSONS, columns=['word'])
PERSONS_NER["entity_group"] = "PER"
PERSONS_NER["score"] = np.random.sample(n)
PERSONS_NER["start"] = np.random.randint(100, size=n)
PERSONS_NER["end"] = np.random.randint(100, size=n)
PERSONS_NER = PERSONS_NER.to_dict(orient="records")

clusters, _ = fuzzy_cluster(PERSONS_NER, 
                            scorer=partial_token_set_ratio, 
                            workers=2,
                            cutoff=70)

compute_prominence(clusters, merge_output=True)




    






## convert to python native int
#ranks = [int(x) for x in ranks]#
## organize data.
#headers = ["ENTITY", "CLUSTER", "OCCURENCES", "PROMINENCE"]
#clusters = [dict(zip(headers, z)) for z in zip(promoted_strings, clusters, counts, ranks)]
#if to_dataframe:
#    clusters = pd.DataFrame.from_dict(clusters)
#    clusters.sort_values(by=['PROMINENCE'],
#                         inplace=True)#
#return clusters, fuzzy_matrix





# TESTING
def test():
    return fuzzy_cluster(PERSONS, scorer=partial_token_set_ratio)

# computational performance
n_trials = 100
timeit.timeit(test, number=n_trials)/n_trials

TEXT = """
EU fremlægger som varslet nu en række muligheder for sanktioner mod Rusland.

Det fremgår af en udtalelse.

I 'pakken', som det kaldes i udtalelsen, er der specifikt fire forslag.

Sanktionerne skal ramme dem, der var involveret i den 'ulovlige' beslutning at anerkende udbryderregionerne.

Også banker, der finansierer det russiske militær og andre operationer i området skal rammes af EU's hammer.

Derudover foreslår EU at ramme Ruslands adgang til EU's kapital- og finansielle markeder for at begrænse finansieringen af 'eskalerende og aggressive tiltag'.

Til sidst vil EU også ramme handel i de to udbryderregioner til og fra EU.
"""

from transformers import pipeline
import pandas as pd
ner = pipeline(task='ner', 
                model='saattrupdan/nbailab-base-ner-scandi', 
                aggregation_strategy='first')
result = ner(TEXT)


pd.DataFrame.from_records(result)

#a = {'userid': 'def', 'name': 'laszlo', 'userid': 'abc', 'name': 'anton'}
#b = {'userid': 'abc', 'age': '15'}
#{**a, **b}
#a | b



