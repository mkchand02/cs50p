"""
In a file called bank.py, reimplement Home Federal Savings Bank from Problem Set 1, restructuring your code per the below, wherein value expects a str as input and returns 0 if that str starts with “hello”, 20 if that str starts with an “h” (but not “hello”), or 100 otherwise, treating the str case-insensitively. Only main should call print.
"""


def main():
    greeting = input("Greeting")
    amt = value(greeting)
    print(f"${amt}")


def value(greeting):
    greeting = greeting.strip().lower()
    amt = None
    if greeting.startswith("hello"):
        amt = 0
    elif greeting.startswith("h"):
        amt = 20
    else:
        amt = 100
    return amt


if __name__ == "__main__":
    main()
