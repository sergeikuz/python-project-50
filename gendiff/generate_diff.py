from gendiff.generator import generate
from gendiff.parser import parse_data_from_file
from gendiff.formatters.choice_formatter import choice_format_diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    dict1 = parse_data_from_file(file_path1)
    dict2 = parse_data_from_file(file_path2)
    diff = generate(dict1, dict2)
    result = choice_format_diff(diff, format_name)

    return result
