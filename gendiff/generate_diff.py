from gendiff.generator import get_differences
from gendiff.parser import parse_data_from_file
from gendiff.formatters.choose_formatter import choose_format_diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    dict1 = parse_data_from_file(file_path1)
    dict2 = parse_data_from_file(file_path2)
    diff = get_differences(dict1, dict2)
    result = choose_format_diff(diff, format_name)

    return result
