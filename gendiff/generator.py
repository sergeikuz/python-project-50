def make_str_bool_value_in_parse_data(dict_d):
    fix_dict = {}

    for k, v in dict_d.items():
        if isinstance(v, dict):
            fix_dict[k] = make_str_bool_value_in_parse_data(v)
        else:
            if isinstance(v, bool):
                fix_dict[k] = str(v).lower()
            elif v == None:
                fix_dict[k] = 'null'
            else:
                fix_dict[k] = v

    return fix_dict


def stringify(value, replacer=' ', space_count=4, _lvl=1):
    if isinstance(value, dict):
        prefix = ('  ', '+ ', '- ')
        result = '{\n'
        for el, val in value.items():
            if el.startswith(prefix):
                result += f'{replacer * (space_count*_lvl - 2)}{el}: '
                result += stringify(val, replacer, space_count, _lvl + 1) + '\n'
            elif el:
                result += f'{replacer * space_count * _lvl}{el}: '
                result += stringify(val, replacer, space_count, _lvl + 1) + '\n'
        result += replacer * space_count * (_lvl - 1) + '}'
    else:
        result = str(value)
    return result


def diff(dict1, dict2):
    keys = sorted(dict1.keys() | dict2.keys())
    diff_dict = {}
    for key in keys:
        if key in dict1 and key in dict2 and isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            diff_dict[f'  {key}'] = diff(dict1[key], dict2[key])
        else:
            if key not in dict2:
                diff_dict[f'- {key}'] = dict1[key]
            elif key not in dict1:
                diff_dict[f'+ {key}'] = dict2[key]
            elif dict1[key] == dict2[key]:
                diff_dict[f'  {key}'] = dict1[key]
            else:
                diff_dict[f'- {key}'] = dict1[key]
                diff_dict[f'+ {key}'] = dict2[key]

    return diff_dict
