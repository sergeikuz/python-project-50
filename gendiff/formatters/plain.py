def make_data_to_plain(data):
    diff = []

    for item in data:
        for k, v in item.items():
            if v == 'nested':
                diff.append(make_data_to_plain(item['value']))
            elif v == 'deleted':
                diff.append(
                        f"Property '{item['name']}' was removed"
                )
            elif v == 'changed':
                if isinstance(item['old_value'], dict):
                    item['old_value'] = '[complex vulue]'
                if isinstance(item['new_value'], dict):
                    item['new_value'] = '[complex vulue]'
                diff.append(
                    f"Property '{item['name']}' was updated. From '{item['old_value']}' to '{item['new_value']}'"
                )
            elif v == 'added':
                if isinstance(item['new_value'], dict):
                    item['new_value'] = '[complex vulue]'
                diff.append(
                        f"Property '{item['name']}' was added with value: '{item['new_value']}'"
                )

    return diff


def make_str(fix_dict, replacer=' ', space_count=0, _lvl=1):
    if isinstance(fix_dict, list):
        result = ''
        for el in fix_dict:
            if isinstance(el, list):
                result += make_str(el)
            else:
                result += f'{replacer*space_count*_lvl}{el}\n'
    else:
        result = str(fix_dict)
    
    return result


def make_plain(data):
    plain_list = make_data_to_plain(data)
    result = make_str(plain_list)
    return result
