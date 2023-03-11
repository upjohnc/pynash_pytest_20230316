"""
Tests simply need:
    - an assert statement
    - in a module with test as the prefix or suffix
    - function name with test as the prefix or suffix
"""

from my_code import add_one


def test_add_one_3():
    expected = 4
    input_value = 3
    result = add_one(input_value)

    assert result == expected


def test_add_one_6():
    expected = 7
    input_value = 6
    result = add_one(input_value)

    assert result == expected
