import json


def read_from_json(argv):
    with open(argv) as f:
        devices = json.load(f)
    return devices
