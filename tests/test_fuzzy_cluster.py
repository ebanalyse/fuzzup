import pandas as pd

from fuzzup.fuzz import fuzzy_cluster, fuzzy_cluster_bygroup
from fuzzup.datasets import simulate_ner_data

import pytest

def test_fuzzy_cluster_runs():
    assert True

def test_fuzzy_cluster():
    strings = ['biden', 'joe biden', 'donald trump', 'D. Trump']  
    clusters = fuzzy_cluster(strings)
    assert isinstance(clusters, list)
    
#### SINGLE WORD
    
def test_fuzzy_cluster_single():
    clusters = fuzzy_cluster(["smokie"])
    assert len(clusters)==1
    assert isinstance(clusters, list) 
    
#### INPUT LENGTH ZERO

def test_fuzzy_cluster_none():
    clusters = fuzzy_cluster([])
    assert len(clusters)==0
    assert isinstance(clusters, list) 

def test_fuzzy_cluster_bygroup():
    PERSONS_NER = simulate_ner_data()
    out = fuzzy_cluster_bygroup(PERSONS_NER)
    assert len(out)==len(PERSONS_NER)
    assert fuzzy_cluster_bygroup([])==[]
    
    
if __name__ == '__main__':
    pytest.main()
    
