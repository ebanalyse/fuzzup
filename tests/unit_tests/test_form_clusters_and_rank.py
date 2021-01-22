from fuzzup.gear import form_clusters_and_rank

strings = ['biden', 'joe biden', 'donald trump']

def test_form_clusters_and_rank_runs():
    form_clusters_and_rank(strings) 

output = form_clusters_and_rank(strings) 

def test_form_clusters_and_rank_format():
    assert isinstance(output, list)


