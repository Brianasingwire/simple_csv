"""reading and printing out contents of csv file"""

import csv


def read_csv_file(name: str):
    '''Function to read csv file'''
    all_lines = []
    with open(f'{name}.csv', 'r', encoding='utf-8') as file:
        content = csv.reader(file, delimiter=',')
        for line in content:
            all_lines.append(line)
    return all_lines
