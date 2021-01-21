from fuzzup.gear import compute_fuzzy_matrix, compute_clusters
strings = ['biden', 'joe biden', 'donald trump', 'D. Trump']
ratios = compute_fuzzy_matrix(strings) 

def test_compute_clusters_runs():
    compute_clusters(ratios)

output = compute_clusters(ratios)

def test_compute_clusters_format():
    assert isinstance(output, dict)


