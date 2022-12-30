"""
In a file called seasons.py, implement a program that prompts the user for their date of birth in YYYY-MM-DD format and then sings prints how old they are in minutes, rounded to the nearest integer, using English words instead of numerals, just like the song from Rent, without any and between words. Since a user might not know the time at which they were born, assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. And assume that the current time is also midnight. In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date. Use datetime.date.today to get today’s date
"""

from datetime import date
import re
import inflect, sys

def main():
    """driver code function"""
    birth_date = input("Date of Birth: ")
    try:
        print(date_to_mins(birth_date))
    except ValueError:
        sys.exit("Invalid Date")

def date_to_mins(date_str, date_2_str = None):
    """returns the time duration in minutes between the dates provided in the format "YYYY-MM-DD" as str datatype. If date_2_str is not provided then , we assume time as today's(current) date. Anything else as input param throws ValueError

    @param date_str - str input date provided in the format "YYYY-MM-DD". 
    @param date_2_str - str input date provided in the format "YYYY-MM-DD". 
    @return - the time duration in minutes between the date provided in the format "YYYY-MM-DD" as str datatype and today's(current) date.
    @raises ValueError - Invalid Date/Provided Date in Incorrect Format
    """
    date_str = date_str.strip()
    # check if data is in valid format
    # match = re.match(r"^\d{4}-[0-1]\d-[0-3]\d$",date_str)
    # if match:
    # split date into year, month and days respectively
    year, month, day = date_str.split("-")
    # convert str to int
    year, month, day = int(year), int(month), int(day)
    
    target_date = date(year, month, day) # may raise ValueError if any of the params provided are invalid
    if date_2_str:
        year2, month2, day2 = date_2_str.split("-")
        year2, month2, day2 = int(year2), int(month2), int(day2)
        today = date(year2, month2, day2)
    else:
        today = date.today() # get today's date
    time_duration = today - target_date # get the time diff.
    # get the time in secs and convert to mins
    mins = int(time_duration.total_seconds() / 60)
    # setup inflect for converting to mins
    p = inflect.engine()
    words = p.number_to_words(mins, andword="")
    # first alphabet of the string should be upper-case
    words = words.capitalize() + " minutes"
    return words
    
    
    


if __name__ == "__main__":
    main()