import pytest

import my_code


# Create the input values once nd leverage twice
@pytest.fixture
def some_value():
    return 3


def test_add_one(some_value):
    result = my_code.add_one(some_value)
    expected = 4

    assert result == expected


def test_multiply_two(some_value):
    result = my_code.multiply_two(some_value)
    expected = 6

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
