def for_deleted(key, value):
    return {
        'action': 'deleted',
        'name': key,
        'old_value': value
    }


def for_added(key, value):
    return {
        'action': 'added',
        'name': key,
        'new_value': value
    }


def for_changed(key, value1, value2):
    return {
        'action': 'changed',
        'name': key,
        'old_value': value1,
        'new_value': value2
    }


def for_unchanged(key, value):
    return {
        'action': 'unchanged',
        'name': key,
        'value': value
    }


def for_nested(key, value1, value2):
    return {
        'action': 'nested',
        'name': key,
        'value': generate(value1, value2)
    }


def make_value_to_str_in_dict(data):
    fix_dict = {}
    for k, v in data.items():
        if isinstance(v, dict):
            fix_dict[k] = make_value_to_str_in_dict(v)
        else:
            if isinstance(v, bool):
                fix_dict[k] = str(v).lower()
            elif v is None:
                fix_dict[k] = 'null'
            else:
                fix_dict[k] = v

    return fix_dict


def generate(dict1, dict2):
    dict1 = make_value_to_str_in_dict(dict1)
    dict2 = make_value_to_str_in_dict(dict2)

    keys = sorted(dict1.keys() | dict2.keys())
    added_keys = dict2.keys() - dict1.keys()
    deleted_keys = dict1.keys() - dict2.keys()

    diff = []

    for key in keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        if key in added_keys:
            diff.append(for_added(key, value2))
        elif key in deleted_keys:
            diff.append(for_deleted(key, value1))
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.append(for_nested(key, value1, value2))
        elif value1 != value2:
            diff.append(for_changed(key, value1, value2))
        else:
            diff.append(for_unchanged(key, value1))

    return diff
