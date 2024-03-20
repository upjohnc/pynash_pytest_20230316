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
## Fixtures

Fixtures are a way to reuse code.  Generally it is as input to a test.

Other examples of usage are setting up an object and tearing it down, such as setting
up a datastore and tearing it down.

Example:
[Mock Postgres](https://ryan-duve.medium.com/how-to-mock-postgresql-with-pytest-and-pytest-postgresql-26b4a5ea3c25).
Note: it uses `pytest-postgresql`, the plugin, for connection object named postgresql.

