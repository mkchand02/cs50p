"""
implement, in a file called test_working.py, three or more functions that collectively test your implementation of convert thoroughly
"""

import pytest
from working import convert


def test_invalid_input():
    with pytest.raises(ValueError):
        convert("abc")
    with pytest.raises(ValueError):
        convert("4312")
    with pytest.raises(ValueError):
        convert("@#%$@")


def test_invalid_time_notation():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")


def test_invalid_time():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("-5 AM to 5 PM")


def test_valid_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:30 AM to 6:00 PM") == "09:30 to 18:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
