from gendiff.generate_diff import generate_diff
import os
import pytest


def get_fixtures_path(name):
    return os.path.join('tests/fixtures', name)


@pytest.fixture
def expected_diff():
    with open(get_fixtures_path('expected_diff.txt')) as exp:
        return exp.read().strip()


path1 = get_fixtures_path('file1.json')
path2 = get_fixtures_path('file2.json')


def test_generate_diff():
    assert expected_diff == generate_diff(path1, path2)
