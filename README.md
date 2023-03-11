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
## Plugins

Plugins are additional python libraries that can
added to your python virtualenv to extend pytest.

Two that I find valuable are:
- pytest-env : set env vars when running tests
- pytest-check : allow multiple asserts in a test function and if one assert fails the other asserts still run
