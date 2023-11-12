# TODO решите задачу
import json


def task() -> float:
    with open('input.json') as f:
        data = json.load(f)
        return round(sum([data['score']*data['weight'] for data in data]),3)

print(task())
