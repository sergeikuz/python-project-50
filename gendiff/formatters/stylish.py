"""def make_value_to_str(data):
    fix_dict = {}

    for k, v in data.items():
        if isinstance(v, dict):
            fix_dict[k] = make_value_to_str(v)
        else:
            if isinstance(v, bool):
                fix_dict[k] = str(v).lower()
            elif v is None:
                fix_dict[k] = 'null'
            else:
                fix_dict[k] = v

    return fix_dict
"""


def make_data_stylish(data):
    diff = {}
    for item in data:
        for k, v in item.items():
            if v == 'nested':
                diff[f'  {item["name"]}'] = make_data_stylish(item['value'])
            elif v == 'unchanged':
                diff[f'  {item["name"]}'] = item['value']
            elif v == 'deleted':
                diff[f'- {item["name"]}'] = item['old_value']
            elif v == 'added':
                diff[f'+ {item["name"]}'] = item['new_value']
            elif v == 'changed':
                diff[f'- {item["name"]}'] = item['old_value']
                diff[f'+ {item["name"]}'] = item['new_value']
    return diff


def make_str(fix_dict, replacer=' ', space_count=4, _lvl=1):
    if isinstance(fix_dict, dict):
        prefix = ('  ', '+ ', '- ')
        result = '{\n'
        for el, val in fix_dict.items():
            if el.startswith(prefix):
                result += f'{replacer * (space_count*_lvl - 2)}{el}: '
                result += make_str(val, replacer, space_count, _lvl + 1) + '\n'
            elif el:
                result += f'{replacer * space_count * _lvl}{el}: '
                result += make_str(val, replacer, space_count, _lvl + 1) + '\n'
        result += replacer * space_count * (_lvl - 1) + '}'
    else:
        result = str(fix_dict)
    return result


def make_stylish(data):
    stylish_data = make_data_stylish(data)
    result = make_str(stylish_data)
    return result
