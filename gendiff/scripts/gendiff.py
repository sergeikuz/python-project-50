#!/usr/bin/env python3


from gendiff.cli import get_information
from gendiff.generate_diff import generate_diff


def main():
    args = get_information()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)

if __name__ == '__main__':
    main()
