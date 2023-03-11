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
## Parametrize

Parametrize is a feature that allows you to run multiple inputs on a particular test.

You can write a test and feed it different sets of inputs along with the expected result, so you
do not have to rewrite the test many times for for the different sets of inputs.
