from gendiff.formatters.json import make_json
from gendiff.formatters.plain import make_plain
from gendiff.formatters.stylish import make_stylish


def choose_format_diff(diff, format_name):
    if format_name == 'stylish':
        return make_stylish(diff)
    if format_name == 'plain':
        return make_plain(diff)
    if format_name == 'json':
        return make_json(diff)
    else:
        raise ValueError(f"Unsupported formatter: {format_name}")
