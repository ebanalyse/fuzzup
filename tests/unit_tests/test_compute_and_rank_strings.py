from fuzzup.gear import cluster_and_rank_strings

strings = ['biden', 'joe biden', 'donald trump']

def test_cluster_and_rank_strings_runs():
    cluster_and_rank_strings(strings) 

output = cluster_and_rank_strings(strings) 

def test_cluster_and_rank_strings_format():
    assert isinstance(output, list)


