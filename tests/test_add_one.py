"""
`src` is the root directory for the source code.
We couldn't just import `add_constant` as `from src.add_constant import add_constant`
The reason is that the imports done in the source code have `src` as the root directory.

We set the `PYTHONPATH` when running the tests so that `src` is considered the root directory
eg: `PYTHONPATH=src pytest .`
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
