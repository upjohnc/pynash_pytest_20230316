default:
    just --list

run_test:
    PYTHONPATH=src pytest .
