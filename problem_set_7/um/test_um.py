"""
implement, in a file called test_um.py, three or more functions that collectively test your implementation of count thoroughly
"""

from um import count


def test_0_ums():
    assert count("Yummy") == 0
    assert count("@$%@BDFRfeb") == 0
    assert count("123abc%#$") == 0


def test_1_ums():
    assert count("um") == 1
    assert count("Um?") == 1
    assert count("...um....") == 1


def test_multiple_ums():
    assert count("Hi,um, how are you, um?") == 2
    assert count("um? um") == 2
    assert count("um at the beginning and the end as well, um") == 2
    assert count("um.um") == 2
    assert count("um UM uM Um um") == 5
