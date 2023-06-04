import json


def read_json(file_name):
    with open(file_name, 'r') as json_file:
        stock_data = json.load(json_file)
    return stock_data
