import numpy as np

from fuzzup.fuzz import fuzzy_cluster, compute_prominence_placement
from fuzzup.datasets import simulate_ner_data

NER = simulate_ner_data()

clusters = fuzzy_cluster(NER)

compute_prominence_placement(clusters)
compute_prominence_placement([])