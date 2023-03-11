"""
Adding pytest_check allows for both assertions to run.
In test_other: once the first assertion fails the test function fails

Using env var set in pyproject.toml, you do not need to patch the env vars
"""

from pytest_check import check

from add_one import add_one


def test_with_check():
    with check("First assertion"):
        assert 1 == 2

    with check("Second assertion"):
        assert 2 == 3


def test_other():
    assert 1 == 2
    assert 2 == 3


def test_add_one():
    result = add_one()
    assert 2 == result
