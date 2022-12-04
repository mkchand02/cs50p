"""
In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:

-convert expects a str in X/Y format as input, wherein each of X and Y is an integer, and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
-gauge expects an int and returns a str that is:
-"E" if that int is less than or equal to 1,
-"F" if that int is greater than or equal to 99,
and "Z%" otherwise, wherein Z is that same int.
"""


def main():
    while True:
        try:
            fuel_filled = input("enter :")
            percentage = convert(fuel_filled)
        except (ValueError, IndexError, ZeroDivisionError):
            pass
        else:
            value = gauge(percentage)
            print(value)
            break  #Break the while loop


def convert(fraction):
    """converts fraction of format "x/y" to percentage rounded to nearest int"""
    x, y = fraction.split("/")
    percentage = int(x) / int(y) * 100
    if percentage > 100:
        raise ValueError
    return round(percentage)


def gauge(percentage):
    """takes an integer percentage and returns "E" if integer <=1, "F" if integer >=1, or the integer in the format "integer%" otherwise"""
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
