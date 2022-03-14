import pandas as pd

from fuzzup.fuzz import fuzzy_cluster, fuzzy_cluster_bygroup
from fuzzup.datasets import simulate_ner_data

def test_fuzzy_cluster_runs():
    assert True

strings = ['biden', 'joe biden', 'donald trump', 'D. Trump']  

def test_fuzzy_cluster():
    fuzzy_cluster(strings)
    
clusters = fuzzy_cluster(strings)

def test_fuzzy_cluster_format():
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
    
