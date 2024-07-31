def to_str_v(value):
    if isinstance(value, (dict, list)):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    else:
        return str(value)


def make_data_to_plain(data, path=''):
    diff = []

    for item in data:
        current_key = item.get('name')
        current_path = f"{path}.{current_key}" if path else current_key
        new_value = to_str_v(item.get('new_value'))
        old_value = to_str_v(item.get('old_value'))

        for k, v in item.items():
            if v == 'nested':
                diff.append(make_data_to_plain(item['value'], current_path))
            elif v == 'deleted':
                diff.append(
                    f"Property '{current_path}' was removed"
                )
            elif v == 'changed':
                diff.append(
                    f"Property '{current_path}' was updated. "
                    f"From {old_value} to {new_value}"
                )
            elif v == 'added':
                diff.append(
                    f"Property '{current_path}' "
                    f"was added with value: {new_value}"
                )

    return diff


def make_str(fix_dict, replacer=' ', space_count=0, _lvl=1):
    if isinstance(fix_dict, list):
        result = []
        for el in fix_dict:
            if isinstance(el, list):
                result.append(make_str(el))
            else:
                result.append(str(el))

    return '\n'.join(result)


def make_plain(data):
    plain_list = make_data_to_plain(data)
    result = make_str(plain_list)
    return result
