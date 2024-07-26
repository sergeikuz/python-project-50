from gendiff.generator import diff
from gendiff.parser import parse_data_from_file
from gendiff.formatter import stylish
from gendiff.formatter import make_str_bool_value_in_parse_data


def generate_diff(file_path1, file_path2, format='stylish'):
    dict1 = parse_data_from_file(file_path1)
    dict2 = parse_data_from_file(file_path2)
    diff_data = diff(dict1, dict2)
    diff_dict = make_str_bool_value_in_parse_data(diff_data)
    result = stylish(diff_dict)
    return result
