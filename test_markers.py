"""
In the pyproject.toml file, the addopts pass parameters to check that the marker
is spelled correctly.
"""
import pytest


@pytest.mark.hotdog
def test_hotdog():
    assert 1 == 1


def test_other():
    assert 2 == 2


@pytest.mark.not_hotdog
def test_not_hotdog():
    assert True


# if you uncomment this test, the tests will not run
# because the marker isn't in the list of markers in pyproject.toml
# @pytest.mark.slow
# def test_bad():
#     assert 3==3
