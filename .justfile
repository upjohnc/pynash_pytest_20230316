default:
    just --list

all_tests:
    pytest .

hotdog:
    pytest -m hotdog

not-hotdog:
    pytest -m not_hotdog

unmarked:
    pytest -m "not (hotdog or not_hotdog)"
