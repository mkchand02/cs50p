"""
implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
"""

valid_coins = {5, 10, 25}
amt_due = 50
while True:
    coin = int(input("Insert Coin:"))
    if coin in valid_coins:
        amt_due -= coin
    if amt_due > 0:
        print("Amount Due:", amt_due)
    else: #amt_due = 0 is also taken care in else
        print("Change Owed:", -1 * amt_due)
        break
