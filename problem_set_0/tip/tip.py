def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    money = float(d[1:])  #since i/p format is $20.00 , o/p should be 20.0
    return money


def percent_to_float(p):
    # TODO
    percent = float(p[:-1]) / 100 # since i/p format is 15% , o/p should be 0.15
    return percent

main()