import timeit
from rapidfuzz.fuzz import partial_token_set_ratio

from fuzzup.fuzz import fuzz_it_up

PERSONS = ['Donald Trump', 'Donald Trump', 
           'J. biden', 'joe biden', 'Biden', 
           'Bide', 'mark esper', 'Christopher c . miller', 
           'jim mattis', 'Nancy Pelosi', 'trumps',
           'Trump', 'Donald', 'miller']

clusters, fuzzy_matrix = fuzz_it_up(PERSONS)
clusters
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




