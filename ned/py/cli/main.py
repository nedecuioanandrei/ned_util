import argparse
import sys
from ned.py.core.commands import ( 
        init,
        create_package,
)

def get_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    init_parser = subparsers.add_parser(
        "init", help="Init the python3 project."
    )
    init_parser.add_argument("--force", action="store_true", help="Override the current files.")
    init_parser.set_defaults(func=init)

    create_package_parser = subparsers.add_parser("c-pack", help="Create a new package in the current dir.")
    create_package_parser.add_argument("name", help="Package name.")
    create_package_parser.set_defaults(func=create_package)

    return parser


def main():
    parser = get_parser()
    args = parser.parse_args(sys.argv[1:])
    args.func(args)
