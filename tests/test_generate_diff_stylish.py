from gendiff.generate_diff import generate_diff
import os
import json


def get_fixtures_path(name):
    return os.path.join('tests/fixtures', name)


def test_generate_diff():
    expected_name_path = get_fixtures_path('expected_stylish.txt')
    with open(expected_name_path) as file:
        expected_content = file.read()
        expected_diff = json.loads(json.dumps(expected_content))

    path1 = get_fixtures_path('file1.json')
    path2 = get_fixtures_path('file2.json')

    assert expected_diff == generate_diff(path1, path2, format_name="stylish")
