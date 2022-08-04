"""
In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
"""

ques = "What is the Answer to the Great Question of Life, the Universe and Everything?"
ans = input(ques).strip().lower()
if ans == "42" or ans == "forty two" or ans == "forty-two":
    print("Yes")
else:
    print("No")
