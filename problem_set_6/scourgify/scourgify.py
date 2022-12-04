"""
“Ah, well,” said Tonks, slamming the trunk’s lid shut, “at least it’s all in. That could do with a bit of cleaning, too.” She pointed her wand at Hedwig’s cage. “Scourgify.” A few feathers and droppings vanished.

— Harry Potter and the Order of the Phoenix
Data, too, often needs to be “cleaned,” as by reformatting it, so that values are in a consistent, if not more convenient, format. Consider, for instance, this CSV file of students, before.csv, below:
#####
name,house
"Abbott, Hannah",Hufflepuff
...
#####
Source: en.wikipedia.org/wiki/List_of_Harry_Potter_characters

In a file called scourgify.py, implement a program that:

Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.
"""

import sys, csv


def main():
    is_valid_args(sys.argv)
    read_file = sys.argv[1]
    write_file = sys.argv[2]
    data_list = get_data_list(read_file)
    if data_list: 
        #if data list is not empty, write it to write_file csv
        write_csv(write_file, data_list)


def get_data_list(filename):
    """gets csv table data as a list of lists 
        from the csv file; returns None if File doesn't
        exists. First element of list is list of headers 
        for the csv file"""
    try:
        csv_list = []
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                csv_list.append(processed_dict(reader.fieldnames, row))
        return csv_list

    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")


def get_new_fields():
    return ["first", "last", "house"]


def processed_dict(fields, row):
    """processes old field name: "last, first" to first : "first" 
    and last : "last" and returns the same if fields are not empty"""
    new_fields = get_new_fields()
    if fields:
        last, first = row[fields[0]].split(",")
        first, last = first.strip(), last.strip()
        return {
            new_fields[0]: first,
            new_fields[1]: last,
            new_fields[2]: row[fields[1]]
        }

def write_csv(filename, data_list):
    """writes csv table data taken as a list of dicts;
        returns None if File doesn't exists."""
    with open(filename, 'w') as file:
        writer = csv.DictWriter(file, fieldnames = get_new_fields())
        writer.writeheader()
        for row in data_list:
            writer.writerow(row)

def is_valid_args(args):
    """Checking if cmd-line args are valid or not"""
    if len(args) < 3:
        sys.exit("Too few command-line arguments")
    elif len(args) > 3:
        sys.exit("Too many command-line arguments")
    if not args[1].lower().endswith(".csv"):
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
