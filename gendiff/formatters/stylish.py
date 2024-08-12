def to_str(data):
    fix_dict = {}

    for k, v in data.items():
        match v:
            case dict(v):
                fix_dict[k] = to_str(v)
            case bool(v):
                fix_dict[k] = str(v).lower()
            case None:
                fix_dict[k] = 'null'
            case _:
                fix_dict[k] = v

    return fix_dict


def make_data_stylish(data: list) -> dict:
    diff = {}
    for item in data:
        match item.get('action'):
            case 'nested':
                diff[f'  {item["name"]}'] = make_data_stylish(item['value'])
            case 'unchanged':
                diff[f'  {item["name"]}'] = item['value']
            case 'deleted':
                diff[f'- {item["name"]}'] = item['old_value']
            case 'added':
                diff[f'+ {item["name"]}'] = item['new_value']
            case 'changed':
                diff[f'- {item["name"]}'] = item['old_value']
                diff[f'+ {item["name"]}'] = item['new_value']
            case _:
                raise ValueError(f"Unsupported action: {item.get('action')}")
    return diff


def make_str(fix_dict: dict, replacer=' ', space_count=4, _lvl=1) -> str:
    if isinstance(fix_dict, dict):
        prefix = ('  ', '+ ', '- ')
        result = '{\n'
        for el, val in fix_dict.items():
            if el.startswith(prefix):
                result += f'{replacer * (space_count * _lvl - 2)}{el}: '
                result += make_str(val, replacer, space_count, _lvl + 1) + '\n'
            elif el:
                result += f'{replacer * space_count * _lvl}{el}: '
                result += make_str(val, replacer, space_count, _lvl + 1) + '\n'
        result += replacer * space_count * (_lvl - 1) + '}'
    else:
        result = str(fix_dict)
    return result


def make_stylish(data: list) -> str:
    stylish_data = make_data_stylish(data)
    stylish_data_with_correct_value = to_str(stylish_data)
    result = make_str(stylish_data_with_correct_value)
    return result
