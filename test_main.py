# test_main.py
import pytest
from main import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 10) == 0

def test_divide():
    assert divide(6, 3) == 2
    with pytest.raises(ValueError):
        divide(5, 0)
