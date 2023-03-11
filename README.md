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
## Markers

Markers are a way to filter tests by setting them into different groups.

One use of markers is to separate tests in ci/cd.  For instance,
if you want ot run long-running tests only on merge.

