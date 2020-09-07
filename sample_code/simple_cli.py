#! /usr/bin/env python3
import sys
from collections import namedtuple


help_string = \
"""usage: {} [-h] [--sum] N [N ...]

Process some integers.

positional arguments:
 N           an integer for the accumulator

optional arguments:
 -h, --help  show this help message and exit
 --sum       sum the integers (default: find the max)
"""

def print_help():
    print(help_string.format(sys.argv[0]))

def pare_arguments():
    args = sys.argv[1:]
    if "-h" in args or "--help" in args:
        print_help()
        sys.exit(0)
    if "--sum" in args:
        index = args.index("--sum")
        if index != 0 or index != len(args) - 1:
            print("invalid injection of --sum")
            sys.exit(1)
        func = sum
    else:
        func = max

    values = []
    for el in args:
        try:
            values.append(int(el))
        except ValueError:
            print(f"invalid literal for int() with base 10: '{el}'")
            sys.exit(1)
    return namedtuple("Args", ["accumulate", "integers"])(func, values)


if __name__ == "__main__":
    args = pare_arguments()
    print(args.accumulate(args.integers))