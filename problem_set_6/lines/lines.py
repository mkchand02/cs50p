"""
One way to measure the complexity of a program is to count its number of lines of code (LOC), excluding blank lines and comments. For instance, a program like
######
# Say hello

name = input("What's your name? ")
print(f"hello, {name}")
######
has just two lines of code, not four, since its first line is a comment, and its second line is blank (i.e., just whitespace). 
Even so, in a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.
"""