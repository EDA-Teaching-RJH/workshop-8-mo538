import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 2) == 4
    assert add(-2, 1) == -1

def test_subtract():
    assert subtract(2, 1) == 1
    assert subtract(0, 4) == -4

def test_multiply():
    assert multiply(2, 2) == 4
    assert multiply( 0, 22) == 0

def test_divide():
    assert divide(4, 2) == 2
    with pytest .raises(ValueError):
        divide (5, 0)
