import time
from writer import write_to_csv_file
from reader import read_csv_file


def run():
    records = [
        ['name', 'score'],
        ['luke', 30],
        ['phil', 29],
        ['claire', 32]
    ]

    file_name = 'video_game_scores'

    write_to_csv_file(file_name, records)
    print('written to csv file')
    time.sleep(2)
    print('reading csv file')
    time.sleep(2)
    all_lines = read_csv_file(file_name)
    print(all_lines)


run()
