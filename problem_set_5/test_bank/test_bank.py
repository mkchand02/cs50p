"""
Then, in a file called test_bank.py, implement three or more functions that collectively test your implementation of value thoroughly, each of whose names should begin with test_ so that you can execute your tests
"""

from bank import value


#value Returns 0$ if greeting startswith hello
def test_greeting_returns_0():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("Hello") == 0
    assert value("heLlO") == 0


#value Returns 20$ if greeting startswith h
def test_greeting_returns_20():
    assert value("hey") == 20
    assert value("HI there") == 20
    assert value("Hola!") == 20
    assert value("hoW you DoinG?") == 20
    assert value("hoW ARE you DoinG?") == 20


#value Returns 100$ for any other greeting
def test_greeting_returns_100():
    assert value("") == 100
    assert value("21345") == 100  #Only nums
    assert value("Yolo!!!") == 100
    assert value("What's GoinG ON?") == 100
    assert value("$???") == 100  #Only special chars
