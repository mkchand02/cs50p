"""
In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.
"""

#Challenge accepted ;)


def main():
    time = input("What time is it?\n").strip()
    time = convert(time)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    """Converts time into 24 hr format decimal"""
    hrs, mins = time.split(":")  #if this gives error time is not proper
    #We can try...catch split and int for value errors
    hrs = int(hrs)
    if len(mins) > 2:  #a.m./p.m. is provided to us and its 12 hr format
        mins, format_12_hr = mins.split(" ")
        #if this gives error, either time format isn't proper or possibly there are additional spaces.
        format_12_hr = format_12_hr.lower()
    else:  # make format_12_hr s na so we can use the same if...else ladder
        format_12_hr = "n.a."
    mins = int(mins)

    if hrs <= 12 and mins < 60:  #time is in 12 hr format
        if (format_12_hr.startswith("a.m.")
                or format_12_hr.startswith("am")):  #time is in am
            hrs = hrs  #hrs do not change
            mins = mins / 60
            return hrs + mins
        elif (format_12_hr.startswith("p.m.")
              or format_12_hr.startswith("pm")):  #time is in pm
            hrs = hrs + 12
            mins = mins / 60
            return hrs + mins
        elif format_12_hr == "n.a.":  #time is in 24 hr format
            mins = mins / 60
            return hrs + mins
    elif hrs <= 23 and mins < 60:  #time is in 24 hr format
        hrs = hrs
        mins = mins / 60
        return hrs + mins

    #You shouldn't reach this point. if reached, it means that time is not given in proper format
    return -1


if __name__ == "__main__":
    main()
