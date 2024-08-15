import itertools
REPLACER = '  '
INDENT = '    '


def to_str(value, depth):
    match value:
        case dict(value):
            result = []
            for key, value in value.items():
                space = INDENT * (depth + 1)
                result.append(f"\n{space}{key}: {to_str(value, depth + 1)}")
            line = itertools.chain('{', result, '\n', [INDENT * depth, '}'])
            return ''.join(line)
        case bool(value):
            return str(value).lower()
        case None:
            return 'null'
        case _:
            return value


def build_line(data, key, depth: int, INDENT='  ') -> str:
    return f"{'  ' * depth}{INDENT}{data['name']}: " \
           f"{to_str(data[key], depth + 1)}"


def make_stylish(node: dict, depth=0) -> str:
    lines = []
    space = REPLACER * (depth + 1)

    for value in node.values():
        match value['action']:
            case 'nested':
                lines.append(
                    f"{space * 2}{value['name']}: "
                    f"{make_stylish(value['value'], depth + 1)}"
                )
            case 'changed':
                lines.append(
                    f"{space}"
                    f"{build_line(value, 'old_value', depth, '- ')}"
                )
                lines.append(
                    f"{space}"
                    f"{build_line(value, 'new_value', depth, '+ ')}"
                )
            case 'deleted':
                lines.append(
                    f"{space}"
                    f"{build_line(value, 'old_value', depth, '- ')}"
                )
            case 'added':
                lines.append(
                    f"{space}"
                    f"{build_line(value, 'new_value', depth, '+ ')}"
                )
            case 'unchanged':
                lines.append(
                    f"{space}"
                    f"{build_line(value, 'value', depth)}"
                )
            case _:
                raise ValueError(
                    f"Unsupported action: {value.get('action')}"
                )

    result = itertools.chain('{', lines, [INDENT * depth + '}'])
    return "\n".join(result)
