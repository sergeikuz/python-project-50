import argparse


HELP_FORMAT = (
    "set format of output"
    ", you can choose formats: stylish, plain, json, "
    "(default format: stylish)")


def get_information():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument(
        "-f", "--format",type=str,
        default="stylish", help=f"{HELP_FORMAT}"
    )

    return parser.parse_args()
