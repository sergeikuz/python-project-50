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
                diff.extend(make_data_to_plain(item['value'], current_path))
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


def make_plain(data):
    plain_list = make_data_to_plain(data)
    result_to_str = '\n'.join(plain_list)
    return result_to_str
