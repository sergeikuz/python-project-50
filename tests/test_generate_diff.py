from gendiff.generate_diff import generate_diff
import os


def get_fixtures_path(name):
    return os.path.join('tests/fixtures', name)


expected_diff = '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'


path1 = get_fixtures_path('file1.json')
path2 = get_fixtures_path('file2.json')


def test_generate_diff():
    assert expected_diff == generate_diff(path1, path2)
