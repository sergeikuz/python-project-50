import json


def stringify(value, replacer=' ', space_count=2, _lvl=1):
    if isinstance(value, list):
        result = '{\n'
        for el in value:
            result += f'{replacer*space_count*_lvl}{el}\n'
        result += replacer * space_count * (_lvl - 2) + '}'
    else:
        result = str(value)
    return result


def make_string_bull_value_in_dict(dict1):
    fix_dict = {}

    for k, v in dict1.items():
        if isinstance(v, bool):
            fix_dict[k] = str(v).lower()
        else:
            fix_dict[k] = v

    return fix_dict


def generate_diff(path_1, path_2):
    with (
        open(path_1) as f1,
        open(path_2) as f2,
    ):

        data1 = make_string_bull_value_in_dict(json.load(f1))
        data2 = make_string_bull_value_in_dict(json.load(f2))

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
