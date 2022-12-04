"""
implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.
"""

camel_case = input("camelCase").strip()
snake_case_list = []

for ch in camel_case:
    if ch.isupper():  #you may also use ch>="A" and ch<="Z" since it is unicode
        snake_case_list.append("_" +
                               ch.lower())  #chr(ord(ch)-32) also works here
    else:
        snake_case_list.append(ch)
print("".join(snake_case_list))
