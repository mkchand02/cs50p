"""
In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

- x is an integer
- y is +, -, *, or /
- z is an integer
"""

#Again, this can be done using conditionals, but we can use eval to speed up the code

expr = input("Expression:")
print(float(eval(expr)))