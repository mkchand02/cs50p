"""
implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.
"""

fridge = {}
while True:
    try:
        fruit = input()
        fruit = fruit.upper()
        if fruit in fridge:
            fridge[fruit] += 1
        else:
            fridge[fruit] = 1
    except EOFError:  #If this error occurs, break
        #print("End of file occured.")
        break

fruits = list(fridge.keys())
fruits.sort()

for fruit in fruits:
    print(fridge[fruit], fruit)
