import argparse
import sys

from ned.git.core.commands import gloga


def get_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    gloga_parser = subparsers.add_parser(
        "gloga", help="show all git barnches."
    )
    gloga_parser.set_defaults(func=gloga)

    return parser


def main():
    parser = get_parser()
    args = parser.parse_args(sys.argv[1:])
    args.func(args)
