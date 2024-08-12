import json


def make_json(diff: list) -> str:
    return json.dumps(diff, indent=4, separators=(',', ': '))
