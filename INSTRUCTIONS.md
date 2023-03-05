# src test dir

You can set up your directory structure that moves source code and tests from the root directory.
This helps to keep the source directory cleaner and ideally just configuration in the root directory.

## Pythonpath

Because the source code will have `src` as its root directory, we need to handle the imports correctly when running
tests.  One way to do that is to set the PYTHONPATH env var.
