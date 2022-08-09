"""
implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:
"""
months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    try:
        date = input("enter :")
        date = date.title()
        date = date.split("/")
        m = int(date[0])
        d = int(date[1])
        y = int(date[2])
        if 1 <= m <= 12 and 1 <= d <= 31:
            break  #everything proper , lets print
    except EOFError:
        break
    except:
        try:
            #if date not in format dd/mm/yyyy and rather of format mmm... dd, yyyy
            old_date = date[0].split(" ")
            mth = old_date[0]
            if "," in old_date[1]:
                d = int(old_date[1].replace(",", ""))
            else:
                continue
            y = int(old_date[2])
            if mth in months and 1 <= d <= 31:
                m = months[mth]
                break  #everything proper , lets print
        except Exception as e:
            #if date is invalid or not of either dd/mm/yyyy and mmm.... dd, yyyy
            print(e)

print(f"{y}-{m:02}-{d:02}")
