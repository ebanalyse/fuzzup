# Fuzz Up [W.I.P.] <img src="https://raw.githubusercontent.com/ebanalyse/fuzzup/main/logo.png" align="right" height=250/>

![Build status](https://github.com/ebanalyse/fuzzup/workflows/build/badge.svg)
[![codecov](https://codecov.io/gh/ebanalyse/fuzzup/branch/main/graph/badge.svg?token=OB6LGFQZYX)](https://codecov.io/gh/ebanalyse/fuzzup)
![PyPI](https://img.shields.io/pypi/v/fuzzup.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/fuzzup?color=green)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

`fuzzup` offers a simple approach for clustering string entitities based on 
[Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance) using
[Fuzzy Matching](https://en.wikipedia.org/wiki/Fuzzy_matching_(computer-assisted_translation))
in conjunction with a simple rule-based clustering method. 

`fuzzup` also provides functions for computing the prominence of the resulting 
entity clusters and to match them with entity whitelists.

An important use-case for `fuzzup` is *organizing, structuring and analyzing* output from [Named-Entity Recognition](https://en.wikipedia.org/wiki/Named-entity_recognition)(=NER).
`fuzzup` also provides (2) functions for computing the prominence of the resulting 
entity clusters resulting from (1) as well as whitelist matching (3).

`fuzzup` has been designed to fit the output from NER predictions from the [Hugging Face](https://huggingface.co/) [transformers](https://github.com/huggingface/transformers) [NER pipeline](https://huggingface.co/docs/transformers/v4.16.2/en/main_classes/pipelines#transformers.TokenClassificationPipeline) specifically.

## Installation guide
`fuzzup` can be installed from the Python Package Index (PyPI) by:

```
pip install fuzzup
```

If you want the development version then install directly from [Github](https://github.com/ebanalyse/fuzzup).

## Workflow

`fuzzup` offers functionality for:

1. Computing all of the mutual string distances (Levensteihn Distances/fuzzy ratios) between the string entities
2. Forming clusters of string entities based on the distances from (1)
3. Computing prominence of the clusters from (2) based on the number of entity occurrences, their positions in the text etc.
4. Matching entities (clusters) with entity whitelists

Together these steps constitute an end-to-end approach for organizing and structuring the output from NER. Here is an example of how to use `fuzzup` for forming entity clusters based on edit distances.




## To do

- document whitelist matching in showcase
- update readme with workflow
- tests for whitelist
- cutoff_threshold -> score_cutoff -> cdist
- ~~try and tune on junges entitites~~
- ~~run against tores list~~
- ~~document whitelist~~
- ~~update docs~~

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

