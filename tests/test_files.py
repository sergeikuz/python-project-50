import os
from gendiff.parser import parse_data_from_file


def get_fixtures_path(name):
    return os.path.join('tests/fixtures', name)


file1_json = get_fixtures_path('file1.json')
file1_yml = get_fixtures_path('file1.yml')
file2_json = get_fixtures_path('file2.json')
file2_yml = get_fixtures_path('file2.yml')


def test_files_corresponds():
    assert parse_data_from_file(file1_json) == parse_data_from_file(file1_yml)
    assert parse_data_from_file(file2_json) == parse_data_from_file(file2_yml)
