"""
Whereas most countries use a 24-hour clock, the United States tends to use a 12-hour clock. Accordingly, instead of “09:00 to 17:00”, many Americans would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”), wherein “AM” is an abbreviation for “ante meridiem” and “PM” is an abbreviation for “post meridiem”, wherein “meridiem” means midday (i.e., noon).

In a file called working.py, implement a function called convert that expects a str in either of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).
"""

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    """takes a work hours time 12-hour format str and converts and returns it into 24-hour format str
    raises ValueError if not in proper format"""
    start_time, end_time = extract(s)
    if start_time and end_time:
        return format(start_time) + " to " + format(end_time)


def extract(s):
    """extract start_time and end_time from str s and return the extracted start_time and end_time tuples of the format (hours, mins, AM_or_PM)
    assumes AM/PM is as capital by default
    raises ValueError if not in proper format"""
    # write search pattern
    pattern = re.search(
        r"^([0-1]?\d):?(\d\d)? ([A-P]M) to ([0-1]?\d):?(\d\d)? ([A-P]M)$", s)
    if pattern:
        #if pattern exists , extract and return the required parts
        pieces = pattern.groups()
        start_time = (pieces[0], pieces[1], pieces[2])
        end_time = (pieces[3], pieces[4], pieces[5])

        #if start_time and end_time are valid then return them, else return None
        return start_time, end_time
    #else return None
    raise ValueError("""Time String is invalid.
Expected "hrs A/PM to hrs A/PM" 
or "hrs:mins A/PM to hrs:mins A/PM" """)


def format(time):
    """takes a tuple/list of the format (hours(int), mins(int), AM_or_PM) and returns a 24-hour time format str if hours and mins are valid
    if mins aren't provided, assume mins to be 00 and return str
    if not in proper format or type, return None
    raises ValueError if invalid hours/mins provided for 12-hr format str"""
    if time \
  and (type(time) is tuple or type(time) is list) \
  and len(time) == 3:
        #extract hrs, mins and 12-hr identifier
        hrs, mins, am_or_pm = int(
            time[0]), int(time[1]) if time[1] else 0, time[2]
        #if valid hrs and mins then proceed
        if (1 <= hrs <= 12 and 0 <= mins <= 59):
            if am_or_pm.upper() == "AM":
                #if am ,then only 12 AM changes to 00
                if hrs == 12:
                    hrs = 0
            elif am_or_pm.upper() == "PM":
                #if pm only 12 PM remains as 12 and others increase by 12
                if hrs != 12:
                    hrs += 12
            else:
                #invalid time identifier
                return None

            #return the formatted string
            return f"{hrs:02}:{mins:02}"
        else:
            raise ValueError("Either invalid hours or mins provided")
        #else return None


if __name__ == "__main__":
    main()
