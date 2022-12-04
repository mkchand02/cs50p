"""
Perhaps the most popular place for pizza in Harvard Square is Pinocchio’s Pizza & Subs, aka Noch’s, known for its Sicilian pizza, which is “a deep-dish or thick-crust pizza.”

Students tend to buy pizza by the slice, but Pinocchio’s also has whole pizzas on its menu too, per this CSV file of Sicilian pizzas, sicilian.csv, below:

Sicilian Pizza,Small,Large
Cheese,$25.50,$39.95
1 item,$27.50,$41.95
2 items,$29.50,$43.95
3 items,$31.50,$45.95
Special,$33.50,$47.95
See regular.csv for a CSV file of regular pizzas as well.
In a file called pizza.py, implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, or if the specified file does not exist, the program should instead exit via sys.exit.
"""
import sys, csv, tabulate


def main():
    is_valid_args(sys.argv)
    filename = sys.argv[1]
    data_list = get_data_list(filename)
    if data_list:
        print(tabulate.tabulate(data_list[1:], data_list[0], tablefmt="grid"))


def get_data_list(filename):
    """gets csv table data as a list of lists 
        from the csv file; returns None if File doesn't
        exists. First element of list is list of headers 
        for the csv file"""
    try:
        csv_list = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                csv_list.append(row)
        return csv_list

    except FileNotFoundError:
        sys.exit("File does not exist")


def is_valid_args(args):
    if len(args) < 2:
        sys.exit("Too few command-line arguments")
    elif len(args) > 2:
        sys.exit("Too many command-line arguments")
    if not args[1].lower().endswith(".csv"):
        sys.exit("Not a Python file")


if __name__ == "__main__":
    main()
