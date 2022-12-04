"""
implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and n names with n−1 commas and one and, as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
"""

import inflect

p = inflect.engine()
total_names = []
final_str = "Adieu, adieu, to "
while True:
    try:
        name = input("enter :")
        total_names.append(name)
    except EOFError:
        #Break when eof error occurs
        break

name_str = p.join(total_names)
final_str = final_str + name_str
print(final_str)
