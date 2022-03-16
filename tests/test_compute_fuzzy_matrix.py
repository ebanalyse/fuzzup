import pandas as pd

from fuzzup.fuzz import compute_fuzzy_matrix

import pytest

def test_compute_fuzzy_matrix_runs():
    strings = ['biden', 'joe biden', 'donald trump']
    output = compute_fuzzy_matrix(strings) 
    assert isinstance(output, pd.DataFrame)

def test_compute_fuzzy_matrix_pos_len():
    strings = ['biden', 'joe biden', 'donald trump']
    output = compute_fuzzy_matrix(strings)
    assert len(output) > 0
    
if __name__=='__main__':
    pytest.main()






