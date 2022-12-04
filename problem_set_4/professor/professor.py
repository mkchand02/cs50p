"""
implement a program that:
Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with n digits. No need to support operations other than addition (+).
Prompts the user to solve each of those problem. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total. If the user has still not answered correctly after three tries, the program should output the correct answer.
The program should ultimately output the user’s score, a number out of 10.
"""

import random


def get_level():
    while True:
        #this loop will get the level from user and terminate on successfully getting a valid level.
        level = input("Level:")
        try:
            level = int(level)
            if level not in {1, 2, 3}:
                continue
            else:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level not in {1, 2, 3}:
        raise ValueError
    val = None
    # Python 3.10 syntax. Unfortunately, replit supports python 3.8.12 and am too lazy to update it to 3.10 😂. Hopefully in future will keep only python 3.10 syntax
    # match level:
    #   case 1:
    #     val = random.randint(0, 9)
    #   case 2:
    #     val = random.randint(10, 99)
    #   case 3:
    #     val = random.randint(100, 999)
    #   case _:
    #     raise ValueError
    if level == 1:
        val = random.randint(0, 9)
    elif level == 2:
        val = random.randint(10, 99)
    elif level == 3:
        val = random.randint(100, 999)
    else:
        raise ValueError

    return val


def main():
    user_score = 0
    level = get_level()
    #Once you have the level, ask 10 questions of the format "x + y" to the user
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        actual_ans = x + y
        answer = None
        for count in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == actual_ans:
                    user_score += 1
                    break
                print("EEE")
            except:  #User gave a non int wrong answer
                print("EEE")
        else:
            print(f"{x} + {y} = {actual_ans}")
    print(f"Score: {user_score}")  #Print score ultimately and exit program


if __name__ == "__main__":
    main()
