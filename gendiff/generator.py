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
