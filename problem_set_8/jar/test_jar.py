"""
implement, in a file called test_jar.py, four or more functions that collectively test your implementation of Jar thoroughly
"""

from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    jar2 = Jar(5)
    assert jar2.capacity == 5
    assert jar2.size == 0 
    with pytest.raises(ValueError):
        jar3 = Jar(-5)

def test_str():
    jar = Jar()
    assert jar.__str__() == ""
    jar.deposit(3)
    assert jar.__str__() == "🍪🍪🍪"
    jar.deposit(9)
    assert jar.__str__() == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(0)
    with pytest.raises(ValueError):
        jar.deposit(-5)
    assert jar.size == 0
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(9)
    assert jar.size == 12
    with pytest.raises(ValueError):
        jar.deposit(1)

def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(0)
    with pytest.raises(ValueError):
        jar.withdraw(-5)
    assert jar.size == 0
    jar.deposit(9)
    jar.withdraw(3)
    assert jar.size == 6
    jar.withdraw(6)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(1)