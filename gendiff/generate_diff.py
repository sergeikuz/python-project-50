from gendiff.generator import diff
from gendiff.parser import parse_data_from_file
from gendiff.generator import stringify

def generate_diff(file_path1, file_path2):
    dict1 = parse_data_from_file(file_path1)
    dict2 = parse_data_from_file(file_path2)
    diff_data = diff(dict1, dict2)
    result = stringify(diff_data)
    return result
