# Pynash Meetup: Pytest Features

This repo is the code examples used in the pynash talk of March 16, 2023.

You can see the different code examples under the branches in this repo.

## Set Up

in terminal, run:

``` bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
## Basic Test

Using pytest, tests are as simple as having an `assert` and the right function and method name.

- pytest naming:
    - function names that start with `test_` or end with `_test`
    - module with test in the name: `test_*.py` or `*_test.py`.
- the `assert` is the check if the test passes or fails.  If boolean check is True then the test passes else fails.

