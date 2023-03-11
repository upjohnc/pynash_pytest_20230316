"""
Example of one test with multiple input combinations

Run `pytest -v .` to see the combination information
"""

import pytest

from add_one import add_one

# define a combination of input with its expected result
input_combinations = [(2, 3), (10, 11)]


@pytest.mark.parametrize("test_input, expected", input_combinations)
def test_add_one(test_input, expected):
    result = add_one(test_input)
    assert result == expected
