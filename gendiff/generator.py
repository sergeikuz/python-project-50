from gendiff.parser import parse_data_from_file


def make_str_bool_value_in_parse_data(path):
    parsed_data = parse_data_from_file(path)
    fix_dict = {}

    for k, v in parsed_data.items():
        if isinstance(v, bool):
            fix_dict[k] = str(v).lower()
        else:
            fix_dict[k] = v

    return fix_dict


def stringify(value, replacer=' ', space_count=2, _lvl=1):
    if isinstance(value, dict):
        result = '{\n'
        for el, val in value.items():
            result += f'{replacer*space_count*_lvl}{el}: '
            result += stringify(val, replacer, space_count, _lvl + 1) + '\n'
        result += replacer * space_count * (_lvl - 1) + '}'
    else:
        result = str(value)
    return result


def generate_diff(dict1, dict2):
    keys = sorted(dict1.keys() | dict2.keys())
    diff_dict = {}
    for key in keys:
        if key not in dict2:
            diff_dict[f'- {key}'] = dict1[key]
        elif key not in dict1:
            diff_dict[f'+ {key}'] = dict2[key]
        elif dict1[key] == dict2[key]:
            diff_dict[f'  {key}'] = dict1[key]
        else:
            diff_dict[f'- {key}'] = dict1[key]
            diff_dict[f'+ {key}'] = dict2[key]

    return stringify(diff_dict)
