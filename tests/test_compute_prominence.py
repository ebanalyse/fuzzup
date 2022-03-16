import pandas as pd
import numpy as np

from fuzzup.fuzz import fuzzy_cluster, compute_prominence, fuzzy_cluster_bygroup, compute_prominence_bygroup
from fuzzup.datasets import simulate_ner_data

import pytest

def test_compute_prominence_multiple():
    strings = ['biden', 'joe biden', 'donald trump', 'D. Trump']  
    
    clusters = fuzzy_cluster(strings)
    clusters = compute_prominence(clusters)
    assert isinstance(clusters, list)
    assert len(clusters) > 0
    
def test_compute_prominence_single():
    clusters = fuzzy_cluster(["Biden"])
    clusters = compute_prominence(clusters)
    assert isinstance(clusters, list)
    assert len(clusters) == 1
    
def test_compute_prominence_none():
    clusters = fuzzy_cluster([])
    clusters = compute_prominence(clusters)
    assert isinstance(clusters, list)
    assert len(clusters) == 0
    
def test_compute_prominence_weight_position():
    clusters = fuzzy_cluster(simulate_ner_data())
    clusters = compute_prominence(clusters,
                                  weight_position=0.5)
    clusters  = pd.DataFrame.from_dict(clusters)
    assert isinstance(clusters.prominence_score.tolist()[0], float)
    
def test_compute_prominence_weight_multipliers():
    clusters = fuzzy_cluster(simulate_ner_data())
    clusters = compute_prominence(clusters,
                                  weight_position=0.5,
                                  weight_multipliers=np.random.rand(len(clusters)))
    clusters = pd.DataFrame.from_dict(clusters)
    assert isinstance(clusters.prominence_score.tolist()[0], float)
    
def test_compute_prominence_bygroup():
    PERSONS_NER = simulate_ner_data()
    out = fuzzy_cluster_bygroup(PERSONS_NER)
    out = compute_prominence_bygroup(out)
    assert len(out)==len(PERSONS_NER)
    assert compute_prominence_bygroup([])==[]

#strings = ['biden', 'joe biden', 'donald trump']

#def test_form_clusters_and_rank_runs():
    #form_clusters_and_rank(strings) 

#output = form_clusters_and_rank(strings) 

#def test_form_clusters_and_rank_format():
#    assert isinstance(output, list)

if __name__ == "__main__":
    pytest.main()