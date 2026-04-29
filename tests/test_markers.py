import sys
import pytest

import source.my_functions as my_functions

@pytest.mark.smoke
def test_add():
    assert my_functions.add(1, 2) == 3


@pytest.mark.skip(reason="not implemented")
def test_subtract():
    assert my_functions.subtract(1, 2) == 3


@pytest.mark.skipif(sys.version_info < (3, 10), reason="requires python 3.10 or higher")
def test_divide():
    assert my_functions.divide(1, 2) == 0.5


@pytest.mark.xfail(reason="not implemented")
def test_divide():
    assert my_functions.divide(1, 2) == -1

