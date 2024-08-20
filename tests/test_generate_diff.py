import pytest
import os
from gendiff.generate_diff import generate_diff


def get_fixtures_path(name):
    return os.path.join('tests/fixtures', name)


@pytest.mark.parametrize(
    "path1, path2, expected, format_name", [
        (
            f"{get_fixtures_path('file1.json')}",
            f"{get_fixtures_path('file2.json')}",
            f"{get_fixtures_path('exp_stylish.txt')}",
            "stylish"
        ),
        (
            f"{get_fixtures_path('file1.json')}",
            f"{get_fixtures_path('file2.json')}",
            f"{get_fixtures_path('exp_plain.txt')}",
            "plain"
        ),
        (
            f"{get_fixtures_path('file1.json')}",
            f"{get_fixtures_path('file2.json')}",
            f"{get_fixtures_path('exp_json.txt')}",
            "json"
        ),
        (
            f"{get_fixtures_path('file1.yml')}",
            f"{get_fixtures_path('file2.yml')}",
            f"{get_fixtures_path('exp_stylish.txt')}",
            "stylish"
        ),
        (
            f"{get_fixtures_path('file1.yml')}",
            f"{get_fixtures_path('file2.yml')}",
            f"{get_fixtures_path('exp_plain.txt')}",
            "plain"
        ),
        (
            f"{get_fixtures_path('file1.yml')}",
            f"{get_fixtures_path('file2.yml')}",
            f"{get_fixtures_path('exp_json.txt')}",
            "json"
        ),
    ]
)
def test_generate_diff(path1, path2, expected, format_name):
    with open(expected, "r") as expectation:
        expectation = expectation.read().strip()
        assert generate_diff(path1, path2, format_name) == expectation
