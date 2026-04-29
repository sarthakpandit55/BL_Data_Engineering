import pytest
import source.exception as with_exception

def test_divide():
    with pytest.raises(ZeroDivisionError):
        assert with_exception.divide(2,0)