def fetch_deleted(key, value):
    return {
        'action': 'deleted',
        'name': key,
        'old_value': value
    }


def fetch_added(key, value):
    return {
        'action': 'added',
        'name': key,
        'new_value': value
    }


def fetch_changed(key, value1, value2):
    return {
        'action': 'changed',
        'name': key,
        'old_value': value1,
        'new_value': value2
    }


def fetch_unchanged(key, value):
    return {
        'action': 'unchanged',
        'name': key,
        'value': value
    }


def fetch_nested(key, value1, value2):
    return {
        'action': 'nested',
        'name': key,
        'value': get_differences(value1, value2)
    }


def get_differences(dict1, dict2):
    keys = sorted(dict1.keys() | dict2.keys())
    added_keys = dict2.keys() - dict1.keys()
    deleted_keys = dict1.keys() - dict2.keys()

    diff = {}

    for key in keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        if key in added_keys:
            diff[key] = fetch_added(key, value2)
        elif key in deleted_keys:
            diff[key] = fetch_deleted(key, value1)
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff[key] = fetch_nested(key, value1, value2)
        elif value1 != value2:
            diff[key] = fetch_changed(key, value1, value2)
        else:
            diff[key] = fetch_unchanged(key, value1)

    return diff
