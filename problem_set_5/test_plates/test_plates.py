"""
Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation of is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests
"""

from plates import is_valid


# All vanity plates must start with at least two letters.”
def test_starts_with_2_letters():
    assert is_valid("CS") == True
    assert is_valid("CS500") == True
    assert is_valid("C500") == False
    assert is_valid("500CS") == False
    assert is_valid("500") == False


# Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
def test_has_valid_length():
    assert is_valid("CSP50") == True
    assert is_valid("CS") == True
    assert is_valid("Csp500") == True
    assert is_valid("CSAIS50") == False
    assert is_valid("C") == False


# Numbers cannot be used in the middle of a plate; they must come at the end.
def test_nums_in_valid_place():
    assert is_valid("CS50") == True
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False


#The first number used cannot be a ‘0’.
def test_first_num_is_not_0():
    assert is_valid("CS0") == False
    assert is_valid("CS05") == False
    assert is_valid("05") == False


# No periods, spaces, or punctuation marks are allowed.
def test_special_characters():
    assert is_valid("<>?:{},./;'[]'") == False
    assert is_valid("CS_05") == False
    assert is_valid("_?;05") == False
    assert is_valid("PI3.14") == False
