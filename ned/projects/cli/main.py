import sys
import argparse


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers()
    list_parser = subparsers.add_parser("list", help="List projects.")
    list_parser.set_defaults(func=lambda args: print(args))
    workon_parser = subparsers.add_parser(
        "workon", help="Cd to target project."
    )
    workon_parser.set_defaults(func=lambda args: print(args))
    create_parser = subparsers.add_parser(
        "create", help="Create a new project."
    )
    create_parser.set_defaults(func=lambda args: print(args))
    delete_parser = subparsers.add_parser("delete", help="Delete a project.")
    delete_parser.set_defaults(func=lambda args: print(args))
    return parser


def main() -> None:
    parser = get_parser()
    parser.parse_args(sys.argv[1:])


if __name__ == "__main__":
    raise SystemExit(main())
