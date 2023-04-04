import argparse
import sys

from ned.cp.core.commands import (archive_contest, create_contest,
                                  join_contest, list_archive, list_contests)


def get_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    list_contests_parser = subparsers.add_parser("ls-c", help="List contests.")
    list_contests_parser.set_defaults(func=list_contests)

    create_contest_parser = subparsers.add_parser(
        "create-contest", help="Create a new contest."
    )
    create_contest_parser.add_argument("name", help="Contes name.")
    create_contest_parser.set_defaults(func=create_contest)

    join_parser = subparsers.add_parser("join", help="Join a contest.")
    join_parser.add_argument("name", help="Contest name.")
    join_parser.add_argument(
        "--fresh", action="store_true", help="Create a fresh session."
    )
    join_parser.set_defaults(func=join_contest)

    archive_contest_parser = subparsers.add_parser(
        "archive", help="Archive a contest."
    )
    archive_contest_parser.add_argument("name", help="Contst name.")
    archive_contest_parser.set_defaults(func=archive_contest)

    list_archived_parser = subparsers.add_parser(
        "ls-arch", help="List archived parsers."
    )
    list_archived_parser.set_defaults(func=list_archive)

    makra_parser = subparsers.add_parser(
        "makra", help="Generate dfault template."
    )
    makra_parser.add_argument("problem_name", help="problem tag")
    makra_parser.add_argument("languge", help="code language")

    list_paraser = subparsers.add_parser("ls-p", help="List problems.")

    add_test_parser = subparsers.add_parser("add-t", help="Add a new test.")

    rm_test_parser = subparsers.add_parser("rm-t", help="Rm a test.")

    run_test_parser = subparsers.add_parser("run-t", help="Run against test.")

    edit_parser = subparsers.add_parser("edit", help="Edit source code.")

    return parser


def main():
    parser = get_parser()
    args = parser.parse_args(sys.argv[1:])
    args.func(args)
