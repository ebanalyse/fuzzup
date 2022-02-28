import pandas as pd

from fuzzup.fuzz import fuzzy_cluster, compute_prominence

strings = ['biden', 'joe biden', 'donald trump', 'D. Trump']  

def test_compute_prominence_multiple():
    clusters, _ = fuzzy_cluster(strings)
    clusters = compute_prominence(clusters)
    assert isinstance(clusters, list)
    assert len(clusters) > 0
    
def test_compute_prominence_single():
    clusters, _ = fuzzy_cluster(["Biden"])
    clusters = compute_prominence(clusters)
    assert isinstance(clusters, list)
    assert len(clusters) == 1
    
def test_compute_prominence_none():
    clusters, _ = fuzzy_cluster([])
    clusters = compute_prominence(clusters)
    assert isinstance(clusters, list)
    assert len(clusters) == 0

#strings = ['biden', 'joe biden', 'donald trump']

#def test_form_clusters_and_rank_runs():
    #form_clusters_and_rank(strings) 

#output = form_clusters_and_rank(strings) 

#def test_form_clusters_and_rank_format():
#    assert isinstance(output, list)


