def to_str_v(value):
    match value:
        case dict(value):
            return '[complex value]'
        case bool(value):
            return str(value).lower()
        case str(value):
            return f"'{value}'"
        case None:
            return 'null'
        case _:
            return str(value)


def make_data_to_plain(data: list, path='') -> list:
    diff = []

    for item in data.values():
        current_key = item.get('name')
        current_path = f"{path}.{current_key}" if path else current_key
        new_value = to_str_v(item.get('new_value'))
        old_value = to_str_v(item.get('old_value'))

        match item.get('action'):
            case 'nested':
                diff.extend(make_data_to_plain(item['value'], current_path))
            case 'deleted':
                diff.append(
                    f"Property '{current_path}' was removed"
                )
            case 'changed':
                diff.append(
                    f"Property '{current_path}' was updated. "
                    f"From {old_value} to {new_value}"
                )
            case 'added':
                diff.append(
                    f"Property '{current_path}' "
                    f"was added with value: {new_value}"
                )

    return diff


def make_plain(data: list) -> str:
    plain_list = make_data_to_plain(data)
    result_to_str = '\n'.join(plain_list)
    return result_to_str
