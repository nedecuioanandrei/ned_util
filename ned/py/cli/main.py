import argparse
import sys

from ned.py.core.commands import create_packages, init


def get_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    init_parser = subparsers.add_parser(
        "init", help="Init the python3 project."
    )
    init_parser.add_argument(
        "--force", action="store_true", help="Override the current files."
    )
    init_parser.set_defaults(func=init)

    create_packages_parser = subparsers.add_parser(
        "c-pack", help="Create a new package in the current dir."
    )
    create_packages_parser.add_argument(
        "names", nargs="+", help="Package name."
    )
    create_packages_parser.set_defaults(func=create_packages)

    return parser


def main():
    parser = get_parser()
    args = parser.parse_args(sys.argv[1:])
    args.func(args)
