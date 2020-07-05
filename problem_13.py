"""
13. Write a function to write a comma-separated value (CSV) file. It
should accept a filename and a list of tuples as parameters. The
tuples should have a name, address, and age. The file should create
a header row followed by a row for each tuple. If the following list of
tuples was passed in:
[('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
it should write the following in the file:
name,address,age
George,4312 Abbey Road,22

John,54 Love Ave,21
"""

import csv


def create_csv_file(header_list, csv_data):
    with open("demo.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header_list)
        for tuple_list in csv_data:
            writer.writerow(tuple_list)

csv_header_list = ("name", "address", "age")
csv_data = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
create_csv_file(csv_header_list, csv_data)


