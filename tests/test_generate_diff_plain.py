from gendiff.generate_diff import generate_diff
import os


def get_fixtures_path(name):
    return os.path.join('tests/fixtures', name)


expected_diff = open(get_fixtures_path('expected_plain.txt'))
expected_diff = expected_diff.read().strip()


path1 = get_fixtures_path('file1.json')
path2 = get_fixtures_path('file2.json')


def test_generate_diff():
    assert expected_diff == generate_diff(path1, path2, format_name="plain")
