import json


def task() -> float:
    file_name = 'input.json'
    with open(file_name) as f:
        json_data = json.load(f)

    values_sum = sum([item['score'] * item['weight'] for item in json_data])
    return round(values_sum, 3)


print(task())
