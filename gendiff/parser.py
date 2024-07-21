import json
import yaml
import os.path


def get_file_format(path):
    root, ext = os.path.splitext(path)
    return ext[1:]


def get_file_content(path):
    with open(path) as file:
        return file.read()


def parse_data(format, content):
    if format == 'json':
        return json.loads(content)
    if format in ['yaml', 'yml']:
        return yaml.safe_load(content)
    raise ValueError(f'Unsupported formatter: {format}')


def parse_data_from_file(path):
    format = get_file_format(path)
    content = get_file_content(path)
    return parse_data(format, content)
