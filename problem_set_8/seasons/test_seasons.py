"""
implement, in a file called test_seasons.py, one or more functions that test your implementation of any functions besides main in seasons.py thoroughly
"""

from seasons import date_to_mins
import pytest

def test_invalid_time():
    with pytest.raises(ValueError):
        date_to_mins("gwefwgre")
    with pytest.raises(ValueError):
        date_to_mins("2022-31-21")
    with pytest.raises(ValueError):
        date_to_mins("2022-21-21-12")
    with pytest.raises(ValueError):
        date_to_mins("January 1, 1999")
    with pytest.raises(ValueError):
        date_to_mins("2022-21-21", "January 1, 1999")

def test_valid_time():
    assert date_to_mins("2022-12-15", "2022-12-16") == "One thousand, four hundred forty minutes"
    assert date_to_mins("1970-01-01", "2000-01-01") == "Fifteen million, seven hundred seventy-eight thousand eighty minutes"
    
    assert date_to_mins("1999-01-01", "2000-01-01") == "Five hundred twenty-five thousand, six hundred minutes"
    