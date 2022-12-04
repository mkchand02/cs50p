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

"Here, I had tried code to remove any comments including docstrings and multiline comments. However, the problem requires that it should be kept so keeping the same"

import sys


def main():
    is_valid_args(sys.argv)
    filename = sys.argv[1]
    count = get_LOC(filename)
    print(count)


def get_LOC(filename):
    try:
        with open(filename, 'r') as file:
            count = 0
            is_part_of_single_quote_comment = False
            is_part_of_double_quote_comment = False
            #flags to check if line of code part of multi-line comment
            for line in file.readlines():
                line = line.strip()
                #   #logic for multilinecomment with single quote starts
                #   if line.startswith("'''") \
                # and not is_part_of_single_quote_comment:
                #       #if flag False, make it True to skip multilinecomments
                #       is_part_of_single_quote_comment = True
                #   #logic for multilinecomment with single quote ends
                #   elif line.startswith("'''") \
                # and is_part_of_single_quote_comment \
                # or line.endswith("'''"):
                #       #if the flag True, make it False
                #       #to ensure we have reached end of multilinecomment
                #       is_part_of_single_quote_comment = False
                #   #same logic as above for double line quotes
                #   elif line.startswith('"""') \
                # and not is_part_of_double_quote_comment:
                #       is_part_of_double_quote_comment = True
                #   elif line.startswith('"""') \
                # and is_part_of_double_quote_comment \
                # or line.endswith('"""'):
                #       is_part_of_double_quote_comment = False
                #   #if either of the flags true,
                #   #skip and don't do anything
                #   elif is_part_of_double_quote_comment \
                # or is_part_of_single_quote_comment:
                #       pass
                #   #if not a single line comment or empty string,
                #   #increase count
                if not line.startswith("#") and not (
                        line == ''
                ):  # and not line.startswith("'") and not line.startswith('"') \
                    count += 1
        return count
    except FileNotFoundError:
        sys.exit("File does not exist")


def is_valid_args(args):
    if len(args) < 2:
        sys.exit("Too few command-line arguments")
    elif len(args) > 2:
        sys.exit("Too many command-line arguments")
    if not args[1].lower().endswith(".py"):
        sys.exit("Not a Python file")


if __name__ == "__main__":
    main()
