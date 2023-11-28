
import json

def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)
        Summa = 0
        for item in data:
            Summa += item['score'] * item['weight']
        return round(Summa,3)


print(task())
