import pytest

from my_code import add_one


@pytest.fixture
def some_value():
    return 3


def test_add_one(some_value):
    result = add_one(some_value)
    expected = 4

    assert result == expected


# Here shows how the set up, yield, and then teardown can work
# to see the std out add `-s` to running tests: pytest -s .
@pytest.fixture
def yield_it():
    print("Start fixture 1")
    yield
    print("Start fixture 2")


def test_yield(yield_it):
    print("Inside Test")
