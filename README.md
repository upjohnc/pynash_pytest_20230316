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
## dir: src and test

You can set up your directory structure that moves source code and tests from the root directory.
This helps to keep the source directory cleaner and ideally just configuration in the root directory.

#### Pythonpath

Because the source code will have `src` as its root directory, we need to handle the imports correctly when running
tests.  One way to do that is to set the PYTHONPATH env var.
