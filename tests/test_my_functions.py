import pytest
import source.my_functions as my_functions


def test_add():
    assert my_functions.add(1, 2) == 3


def test_subtract():
    assert my_functions.subtract(1, 2) == -1