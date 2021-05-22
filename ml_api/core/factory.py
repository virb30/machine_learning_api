import json


def read_json_file(file):
    f = open(file)
    data = json.load(f)
    return json.dumps(data)