"""
Then, in a file called test_fuel.py, implement two or more functions that collectively test your implementations of convert and gauge thoroughly, each of whose names should begin with test_ so that you can execute your tests with:
"""

from fuel import convert, gauge
import pytest


def test_return_E():
    assert convert("0/5") == 0 and gauge(0) == "E"
    assert convert("1/100") == 1 and gauge(1) == "E"


def test_return_F():
    assert convert("100/100") == 100 and gauge(100) == "F"
    assert convert("99/100") == 99 and gauge(99) == "F"


def test_return_num():
    assert convert("4/5") == 80 and gauge(80) == "80%"
    assert convert("4/20") == 20 and gauge(20) == "20%"


def test_return_invalid():
    with pytest.raises(
            ValueError
    ):  #this line should be separate for all convert function calls
        convert("cat")
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ValueError):
        convert("5/4")

    with pytest.raises(ZeroDivisionError):
        convert("5/0")
