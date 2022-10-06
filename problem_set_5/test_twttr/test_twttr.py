"""
Then, in a file called test_twttr.py, implement one or more functions that collectively test your implementation of shorten thoroughly, each of whose names should begin with test_ so that you can execute your tests with:
"""

from twttr import shorten


def test_upper():
    assert shorten("HELLO") == "HLL"
    assert shorten("HEY WORLD") == "HY WRLD"


def test_lower():
    assert shorten("hello") == "hll"
    assert shorten("welcome to cs50p") == "wlcm t cs50p"


def test_both_cases():
    assert shorten("heLLo WorlD") == "hLL WrlD"
    assert shorten("ThisIsCS50P") == "ThssCS50P"


def test_numbers():
    assert shorten("12345") == "12345"
    assert shorten("Hello 123") == "Hll 123"


def test_punctuations():
    assert shorten("?:{}<>,.") == "?:{}<>,."
    assert shorten("Eric D'sa has 5$?") == "rc D's hs 5$?"
