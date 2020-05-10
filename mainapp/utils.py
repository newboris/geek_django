import json


def read_json(path, encoding='utf-8'):
    """Open JSON file, read and return data in format dict"""
    with open(path, encoding=encoding) as file:
        data = json.loads(file.read())
    return data