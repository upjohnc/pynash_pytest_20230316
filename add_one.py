import os


def add_one():
    value = int(os.environ['BIG_THING'])
    return value + 1
