import timeit
from rapidfuzz.fuzz import partial_token_set_ratio

from fuzzup.fuzz import fuzz_it_up

PERSONS = ['Donald Trump', 'Donald Trump', 
           'J. biden', 'joe biden', 'Biden', 
           'Bide', 'mark esper', 'Christopher c . miller', 
           'jim mattis', 'Nancy Pelosi', 'trumps',
           'Trump', 'Donald', 'miller']

#clusters, fuzzy_matrix = fuzz_it_up(PERSONS)
#clusters
clusters, fuzzy_matrix = fuzz_it_up(PERSONS, 
                                    scorer=partial_token_set_ratio, 
                                    workers=2,
                                    cutoff=70)
clusters

# TESTING
def test():
    return fuzz_it_up(PERSONS, scorer=partial_token_set_ratio)

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




