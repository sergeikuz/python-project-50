from gendiff.parser import parse_data_from_file


def stringify(value, replacer=' ', space_count=2, _lvl=1):
    if isinstance(value, list):
        result = '{\n'
        for el in value:
            result += f'{replacer*space_count*_lvl}{el}\n'
        result += replacer * space_count * (_lvl - 2) + '}'
    else:
        result = str(value)
    return result


def make_str_bool_value_in_parse_data(path):
    parsed_data = parse_data_from_file(path)
    fix_dict = {}

    for k, v in parsed_data.items():
        if isinstance(v, bool):
            fix_dict[k] = str(v).lower()
        else:
            fix_dict[k] = v

    return fix_dict


def diff(path1, path2):
    data1 = make_str_bool_value_in_parse_data(path1)
    data2 = make_str_bool_value_in_parse_data(path2)
    list_keys = sorted((data1 | data2).keys())
    diff_list = []

    for key in list_keys:
        if key in data1.keys() and key in data2.keys():
            if data1[key] == data2[key]:
                for k1, v1 in data1.items():
                    if key == k1:
                        diff_list.append(f'  {k1}: {v1}')
            if data1[key] != data2[key]:
                for k1, v1 in data1.items():
                    if key == k1:
                        diff_list.append(f'- {k1}: {v1}')
                for k2, v2 in data2.items():
                    if key == k2:
                        diff_list.append(f'+ {k2}: {v2}')
        elif key in data1.keys():
            for k1, v1 in data1.items():
                if key == k1:
                    diff_list.append(f'- {k1}: {v1}')
        elif key in data2.keys():
            for k2, v2 in data2.items():
                if key == k2:
                    diff_list.append(f'+ {k2}: {v2}')

    diff_string = stringify(diff_list)

    return diff_string
