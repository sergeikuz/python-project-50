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


def stylish(fix_dict, replacer=' ', space_count=4, _lvl=1):
    if isinstance(fix_dict, dict):
        prefix = ('  ', '+ ', '- ')
        result = '{\n'
        for el, val in fix_dict.items():
            if el.startswith(prefix):
                result += f'{replacer * (space_count*_lvl - 2)}{el}: '
                result += stylish(val, replacer, space_count, _lvl + 1) + '\n'
            elif el:
                result += f'{replacer * space_count * _lvl}{el}: '
                result += stylish(val, replacer, space_count, _lvl + 1) + '\n'
        result += replacer * space_count * (_lvl - 1) + '}'
    else:
        result = str(fix_dict)
    return result
