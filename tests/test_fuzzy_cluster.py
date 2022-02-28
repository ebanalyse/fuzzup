import pandas as pd

from fuzzup.fuzz import fuzzy_cluster

def test_fuzzy_cluster_runs():
    assert True

strings = ['biden', 'joe biden', 'donald trump', 'D. Trump']  

def test_fuzzy_cluster():
    fuzzy_cluster(strings)
    
clusters, fuzzy_matrix = fuzzy_cluster(strings)

def test_fuzzy_cluster_format():
    assert isinstance(clusters, list) and isinstance(fuzzy_matrix, pd.DataFrame)

#### SINGLE WORD
    
def test_fuzzy_cluster_single():
    clusters, fuzzy_matrix = fuzzy_cluster(["smokie"])
    assert len(clusters)==1
    assert isinstance(clusters, list) 
    assert isinstance(fuzzy_matrix, pd.DataFrame)
    assert len(fuzzy_matrix)==1
    
#### INPUT LENGTH ZERO

def test_fuzzy_cluster_none():
    clusters, fuzzy_matrix = fuzzy_cluster([])
    assert len(clusters)==0
    assert len(fuzzy_matrix)==0
    assert isinstance(clusters, list) 
    assert isinstance(fuzzy_matrix, pd.DataFrame)



