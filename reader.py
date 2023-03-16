"""reading and printing out contents of csv file"""

import csv


def read_csv_file(name):
    all_lines = []
    with open(f'{name}.csv', 'r') as file:
        content = csv.reader(file, delimiter=',')
        for line in content:
            all_lines.append(line)
    return all_lines
