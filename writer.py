"""create a csv file and put in content"""

import csv
from typing import Dict


def write_to_csv_file(name: str, content: Dict[str, int]):
    with open(f'{name}.csv', 'w') as file:
        file_write = csv.writer(file, delimiter=',')
        file_write.writerows(content)
