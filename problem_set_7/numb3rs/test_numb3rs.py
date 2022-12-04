"""
implement, in a file called test_numb3rs.py, two or more functions that collectively test your implementation of validate thoroughly
"""

from numb3rs import validate

def test_invalid_non_numeric_ip():
    assert validate("abc") == False
    assert validate("ae.bz.cm.dp") == False
    assert validate("123.ab.45.6") == False
    assert validate("#%$.&^*.@#$.#$@") == False
   

def test_invalid_numeric_disordered_ip():
    assert validate("123&789&45&6") == False
    assert validate("123.789.45.6.5") == False
    assert validate("123") == False
    assert validate("123.224") == False

def test_invalid_numeric_ip():
    assert validate("123.789.45.6") == False
    assert validate("-250.-19.-45.-60") == False
    assert validate("250.90.14.-0") == False

def test_valid_ip():
    assert validate("123.12.45.6") == True
    assert validate("49.49.49.49") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True