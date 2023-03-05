"""
Because the constants are imported in the module of the function
we couldn't just import `add_constant` as `from src.add_constant import add_constant`
"""
from add_constant import add_constant


def test_add_one_3():
    expected = 4
    input_value = 3
    result = add_constant(input_value)

    assert result == expected


def test_add_one_6():
    expected = 7
    input_value = 6
    result = add_constant(input_value)

    assert result == expected
