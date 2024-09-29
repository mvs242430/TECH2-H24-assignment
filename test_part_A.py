import pytest
from part_A import std_builtin, std_loops
from util import validate_numbers
import numpy as np



param_data = pytest.mark.parametrize('data',[
    [1, 2, 3, 4, 5],  # Regular list of numbers
    [0, 0, 0, 0],     # List with zero variance
    [1.5, 2.5, 3.5],  # List of floats
])

@param_data
def test_loop(data):
    expected = std_loops(data)
    actual = np.std(data)
    assert np.isclose(actual, expected), '{} is not close to {}'.format(expected, actual)
    assert round(actual, 7) == round(expected,7), 'Rounded {} is not equalt to {}'.format(expected, actual)
  
@param_data
def test_builtin(data):
    expected = std_builtin(data)
    actual = np.std(data)
    assert np.isclose(actual, expected), '{} is not close to {}'.format(expected, actual)
    assert round(actual, 7) == round(expected,7), 'Rounded {} is not equalt to {}'.format(expected, actual)

param_edge_data = pytest.mark.parametrize('edge_cases', [
    [],               
    [1, 2, 'a', 3],
    None,
    '123',
    'i am a sequence also',
])
@param_edge_data
def test_validate_numbers_raises_error(edge_cases):
    with pytest.raises(ValueError):
        validate_numbers(edge_cases)

