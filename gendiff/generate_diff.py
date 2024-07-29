from gendiff.generator import generate
from gendiff.parser import parse_data_from_file
from gendiff.formatters.stylish import make_stylish


def generate_diff(file_path1, file_path2, format='stylish'):
    dict1 = parse_data_from_file(file_path1)
    dict2 = parse_data_from_file(file_path2)
    diff_data = generate(dict1, dict2)
    result = make_stylish(diff_data)
    return result
