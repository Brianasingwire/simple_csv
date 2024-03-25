"""create a csv file and put in content"""

import csv
from typing import Dict


def write_to_csv_file(name: str, content: Dict[str, int]):
    '''Function to write to csv file'''
    with open(f'{name}.csv', 'w', encoding='utf-8') as file:
        file_write = csv.writer(file, delimiter=',')
        file_write.writerows(content)
