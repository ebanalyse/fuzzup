import pandas as pd

from fuzzup.whitelists import match_whitelist, Cities
from fuzzup.fuzz import fuzzy_cluster
import pytest

c = Cities()

def test_whitelist():
    test_data = [{'word': 'Viborg', 'entity_group': 'LOC', 'cluster_id' : 'ABE'}, 
                 {'word': 'Uldum', 'entity_group': 'ORG', 'cluster_id' : 'bambolino' }]
    clusters = fuzzy_cluster(test_data)
    out = c(clusters)
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

if __name__ == '__main__':
    pytest.main()