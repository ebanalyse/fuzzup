import timeit

from fuzzup.gear import form_clusters_and_rank
from rapidfuzz.process import cdist, extract

person_names = ['Donald Trump', 'Donald Trump', 
                'J. biden', 'joe biden', 'Biden', 
                'Bide', 'mark esper', 'Christopher c . miller', 
                'jim mattis', 'Nancy Pelosi', 'trumps',
                'Trump', 'Donald', 'miller']

o = form_clusters_and_rank(person_names)
import pandas as pd
pd.DataFrame.from_dict(o)

x = person_names
x = list(set(x))
dists = cdist(x, x, 
              workers=1)



# extract(person_names, person_names)


def test():
    form_clusters_and_rank(person_names)

n_runs = 10
t = timeit.timeit(test, number=n_runs)/n_runs


