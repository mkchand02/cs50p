"""
implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
"""

inp_str = input("Input: ")

out_list = []
vowel_set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

for ch in inp_str:
    if ch not in vowel_set:
        out_list.append(ch)

out_str = "".join(out_list)
print(out_str)
