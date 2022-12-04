"""
implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.
"""
while True:
    try:
        fuel_filled = input("enter :")
        x, y = fuel_filled.split("/")
        percentage = int(x) / int(y) * 100
        if percentage > 100:
            raise ValueError
    except (ValueError, IndexError, ZeroDivisionError):
        pass
    else:  #If given input has no issues, then find percentage
        percentage = round(percentage)
        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{percentage}%")
        break  #Break the while loop
