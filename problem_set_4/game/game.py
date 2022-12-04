"""
implement a program that:
Prompts the user for a level, n. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and n, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
"""

import random

while True:
    #this loop will get the level from user and terminate on successfully getting a valid level.
    level = input("Level :")
    try:
        level = int(level)
        if level <= 0:
            continue
        else:
            answer = random.randint(1, level)
            break
    except ValueError:
        pass

while True:
    #this loop will get the Guess from user and terminate on successfully getting a guess that is just right.
    guess_no = input("Guess :")
    try:
        guess_no = int(guess_no)
        if guess_no <= 0:
            continue
        else:
            if guess_no < answer:
                print("Too small!")
            elif guess_no > answer:
                print("Too large!")
            else:
                print("Just right!")
                break
    except ValueError:
        pass
