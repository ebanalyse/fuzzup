from fuzzup.fuzz import compute_fuzzy_matrix
import pandas as pd

strings = ['biden', 'joe biden', 'donald trump']

def test_compute_fuzzy_matrix_runs():
    compute_fuzzy_matrix(strings) 

output = compute_fuzzy_matrix(strings) 

def test_compute_fuzzy_matrix_format():
    assert isinstance(output, pd.DataFrame)

def test_compute_fuzzy_matrix_pos_len():
    assert len(output) > 0






