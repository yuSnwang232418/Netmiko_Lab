import json


def read_from_json():
    with open('device_list.json') as f:
        devices = json.load(f)
    return devices
