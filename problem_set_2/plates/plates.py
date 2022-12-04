"""
implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
"""


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    str_len = len(s)
    if str_len < 2 or str_len > 6:
        return False
    #1st 2 characters are alphabets
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    i = 2
    prevIsAlpha = s[1].isalpha()
    for i in range(2, str_len):
        currIsAlpha = s[i].isalpha()
        currIsNum = s[i].isdigit()
        if prevIsAlpha and currIsAlpha:
            continue
        elif prevIsAlpha and currIsNum:
            if s[i] == '0' or not s[i + 1:].isdigit():
                return False
            else:
                break
        else:  #All numbers are handled in previous elif
            #This else will be entered if s[i] is a special character
            return False
        prevIsAlpha = currIsAlpha

    return True


if __name__ == "__main__":
    main()
