import argparse
import sys

from ned.projects.core.config import write_default_config
from ned.projects.core.constants import CONFIG_PATH, list_conf
from ned.projects.core.projects import create, delete, lst, workon


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers()
    list_parser = subparsers.add_parser("list", help="List projects.")
    list_parser.set_defaults(func=lst)

    workon_parser = subparsers.add_parser(
        "workon", help="Cd to target project."
    )
    workon_parser.add_argument("project", help="Project name.")
    workon_parser.add_argument(
        "--fresh", action="store_true", help="Refresh the tmux session."
    )
    workon_parser.set_defaults(func=workon)

    create_parser = subparsers.add_parser(
        "create", help="Create a new project."
    )
    create_parser.add_argument("name", help="Project name.")
    create_parser.add_argument("--git", action="store_true", help="git init")
    create_parser.set_defaults(func=create)

    delete_parser = subparsers.add_parser("delete", help="Delete a project.")
    delete_parser.add_argument("name", help="Project name")
    delete_parser.set_defaults(func=delete)

    generate_config_parser = subparsers.add_parser(
        "switch-default", help="Switch to default config."
    )
    generate_config_parser.set_defaults(
        func=lambda args: write_default_config(CONFIG_PATH)
    )

    list_config_parser = subparsers.add_parser(
        "list-conf", help="List ned-p config params."
    )
    list_config_parser.set_defaults(func=lambda args: list_conf())

    return parser


def main() -> None:
    parser = get_parser()
    args = parser.parse_args(sys.argv[1:])
    args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
