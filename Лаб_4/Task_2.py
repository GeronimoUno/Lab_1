# TODO импортировать необходимые молули


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

import csv
import json

def task() -> None:

    with open(INPUT_FILENAME, 'r') as file_csv:
        reader = csv.DictReader(file_csv)
        data = [row for row in reader]
        with open(OUTPUT_FILENAME, 'w') as file_json:
            data = json.dump(data, file_json, indent=4)
    return data



if __name__ == '__main__':
    task()
    # Нужно для проверки

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
