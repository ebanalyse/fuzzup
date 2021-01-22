# Fuzz Up [W.I.P.] <img src="https://raw.githubusercontent.com/ebanalyse/fuzzup/main/logo.png" align="right" height=250/>

![Build status](https://github.com/ebanalyse/fuzzup/workflows/build/badge.svg)
[![codecov](https://codecov.io/gh/ebanalyse/fuzzup/branch/main/graph/badge.svg?token=OB6LGFQZYX)](https://codecov.io/gh/ebanalyse/fuzzup)
![PyPI](https://img.shields.io/pypi/v/fuzzup.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/fuzzup?color=green)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

`fuzzup` offers a simple approach for clustering strings based on 
[Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance) using
[Fuzzy Matching](https://en.wikipedia.org/wiki/Fuzzy_matching_(computer-assisted_translation))
in conjunction with [Hierarchical Clustering](https://en.wikipedia.org/wiki/Hierarchical_clustering). 

## Installation guide
`fuzzup` can be installed from the Python Package Index (PyPI) by:

```
pip install fuzzup
```

If you want the development version then install directly from [Github](https://github.com/ebanalyse/fuzzup).

## Workflow

`fuzzup` organizes strings by forming clusters from them. It does so in 3 steps:

1. Compute all of the mutual string distances (Levensteihn Distances/fuzzy ratios) between the strings
2. Form clusters of strings (using hierarchical clustering) based on the distances from (1)
3. Rank the clusters by simply counting the number of nodes(strings) in each cluster

```python
# TODO: update example with tuned model.
# strings we want to cluster
>>> person_names = ['Donald Trump', 'Donald Trump', 
                    'J. biden', 'joe biden', 'Biden', 
                    'Bide', 'mark esper', 'Christopher c . miller', 
                    'jim mattis', 'Nancy Pelosi', 'trumps',
                    'Trump', 'Donald', 'miller']

>>> from fuzzup.gear import form_clusters_and_rank
>>> form_clusters_and_rank(person_names)
[{'PROMOTED_STRING': 'Donald Trump',
  'STRINGS': ['Donald Trump', 'Trump', 'trumps'],
  'COUNT': 4,
  'RANK': 1},
 {'PROMOTED_STRING': 'joe biden',
  'STRINGS': ['Bide', 'Biden', 'J. biden', 'joe biden'],
  'COUNT': 4,
  'RANK': 1},
 {'PROMOTED_STRING': 'Christopher c . miller',
  'STRINGS': ['Christopher c . miller', 'miller'],
  'COUNT': 2,
  'RANK': 3},
 {'PROMOTED_STRING': 'Nancy Pelosi',
  'STRINGS': ['Nancy Pelosi', 'mark esper'],
  'COUNT': 2,
  'RANK': 3},
 {'PROMOTED_STRING': 'jim mattis',
  'STRINGS': ['jim mattis'],
  'COUNT': 1,
  'RANK': 5},
 {'PROMOTED_STRING': 'Donald', 'STRINGS': ['Donald'], 'COUNT': 1, 'RANK': 5}]
```

## Background
`fuzzup` is developed as a part of [Ekstra Bladet](https://ekstrabladet.dk/)’s activities on Platform Intelligence in News (PIN). PIN is an industrial research project that is carried out in collaboration between the [Technical University of Denmark](https://www.dtu.dk/), [University of Copenhagen](https://www.ku.dk/) and [Copenhagen Business School](https://www.cbs.dk/) with funding from [Innovation Fund Denmark](https://innovationsfonden.dk/). The project runs from 2020-2023 and develops recommender systems and natural language processing systems geared for news publishing, some of which are open sourced like `fuzzup`.

## Read more
The detailed documentation and motivation for `fuzzup` including code references and
extended workflow examples can be accessed [here](https://ebanalyse.github.io/fuzzup/).

## Contact
We hope, that you will find `fuzzup` useful.

Please direct any questions and feedbacks to
[us](mailto:lars.kjeldgaard@eb.dk)!

If you want to contribute (which we encourage you to), open a
[PR](https://github.com/ebanalyse/fuzzup/pulls).

If you encounter a bug or want to suggest an enhancement, please 
[open an issue](https://github.com/ebanalyse/fuzzup/issues).

