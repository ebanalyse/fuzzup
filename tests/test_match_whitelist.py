import pandas as pd

from fuzzup.whitelists import Cities, aggregate_to_cluster, match_whitelist
from fuzzup.fuzz import fuzzy_cluster

c = Cities()

def test_whitelist():
    test_data = [{'word': 'Viborg', 'entity_group': 'LOC', 'cluster_id' : 'ABE'}, 
                 {'word': 'Uldum', 'entity_group': 'ORG', 'cluster_id' : 'bambolino' }]
    clusters = fuzzy_cluster(test_data)
    out = c(clusters, aggregate_cluster=False)
    assert len(out) == 1
    
def test_whitelist_no_match():
    test_data = [{'word': 'Viborg', 'entity_group': 'LO', 'cluster_id' : 'ABE'}, 
                 {'word': 'Uldum', 'entity_group': 'ORG', 'cluster_id' : 'bambolino' }]
    clusters = fuzzy_cluster(test_data)
    out = c(clusters)
    assert len(out) == 0
    
def test_whitelist_no_input():
    test_data = []
    clusters = fuzzy_cluster(test_data)
    out = c(clusters)
    assert len(out) == 0
    
def test_whitelist_list_input():
    test_data = [{'word': 'Viborg', 'entity_group': 'LO', 'cluster_id' : 'ABE'}, 
                 {'word': 'Uldum', 'entity_group': 'ORG', 'cluster_id' : 'bambolino' }]
    clusters = fuzzy_cluster(test_data)
    matches = match_whitelist(clusters, whitelist=['Viborg'])
    assert len(matches) == len(test_data)
    
def test_whitelist_aggregate_cluster():
    test_data = [{'word': 'Viborg', 'entity_group': 'LOC', 'cluster_id' : 'ABE'}, 
                 {'word': 'Uldum', 'entity_group': 'ORG', 'cluster_id' : 'bambolino' }]
    clusters = fuzzy_cluster(test_data)
    out = c(clusters,
            aggregate_cluster=True)
    assert len(out) == 1