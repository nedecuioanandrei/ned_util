import datetime
import io
import os
import pathlib as p
import subprocess
import zipfile

import tabulate
import yaml

from ned.cp.core.constants import (CONTEST_ARCHIVE_PATH, CONTESTS_DIR,
                                   TMUX_STORAGE)


def list_contests(args):
    if not p.Path(CONTESTS_DIR).exists() or p.Path(CONTESTS_DIR).is_file():
        os.mkdir(CONTESTS_DIR)

    count = 0
    for f in os.listdir(CONTESTS_DIR):
        full_path = p.Path(CONTESTS_DIR).joinpath(f)
        if os.path.isdir(full_path):
            count += 1
            date = datetime.datetime.fromtimestamp(
                full_path.stat().st_mtime, tz=datetime.timezone.utc
            )
            print("{} {}".format(f.ljust(30, " "), date.date()))
    print("Found( {} )".format(count).ljust(30, "-"))


def create_contest(args):
    name = args.name
    path = p.Path(CONTESTS_DIR).joinpath(name)
    if path.exists():
        print("Contest tag conflict {}".format(name))
        return

    os.makedirs(path, exist_ok=True)


def join_contest(args):
    """Start a tmux session."""
    name = args.name
    if not name in os.listdir(CONTESTS_DIR):
        print("contest not found")
        return

    contest_path = p.Path(CONTESTS_DIR).joinpath(name)
    tmux_session_name = "cpc-{}".format(name)
    session_description = p.Path(TMUX_STORAGE).joinpath(
        "{}.yaml".format(tmux_session_name)
    )

    if not session_description.exists() or args.fresh:
        subprocess.run(
            "tmux kill-session -t %s" % tmux_session_name, shell=True
        )
        default_config = """session_name: ~
windows:
- focus: 'true'
  layout: e235,106x56,0,0{53x56,0,0,10,52x56,54,0,11}
  options: {}
  panes:
  - focus: 'true'
  start_directory: ~
  window_name: bash
"""
        data = yaml.safe_load(io.StringIO(default_config))
        data["session_name"] = str(tmux_session_name)
        data["windows"][0]["start_directory"] = str(contest_path)

        with open(session_description, "w") as f:
            yaml.dump(data, f)

    load_cmd = "tmuxp load -y {session_description}".format(
        **{"session_description": str(session_description)}
    )
    print(load_cmd)
    subprocess.run(load_cmd, shell=True)
    subprocess.run(
        "tmuxp freeze {session_name} -f yaml -o {session_description} --yes".format(
            **{
                "session_name": tmux_session_name,
                "session_description": str(session_description),
            }
        ),
        shell=True,
    )


def archive_contest(args):
    contest_name = args.name
    contest_path = p.Path(CONTESTS_DIR).joinpath(contest_name)
    archive_path = p.Path(CONTEST_ARCHIVE_PATH).joinpath(
        "{}.zip".format(args.name)
    )

    with zipfile.ZipFile(archive_path, "w") as f:
        for file in os.listdir(contest_path):
            full_path = p.Path(contest_path).joinpath(file)
            f.write(full_path)


def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ["bytes", "KB", "MB", "GB", "TB"]:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def list_archive(args):
    count = 0
    data = []
    for cp in os.listdir(CONTEST_ARCHIVE_PATH):
        count += 1
        st = p.Path(CONTEST_ARCHIVE_PATH).joinpath(cp).stat()
        sz = st.st_size
        sz = convert_bytes(sz)
        data.append([count, cp, sz])
    print(tabulate.tabulate(data))
    print("Found ( {} )".format(count).ljust(30, "-"))


def makra(args):
    pass


def list_problems(args):
    pass


def add_problme_test(args):
    pass


def run_test_parser(args):
    pass


def edit_source_parser(args):
    pass
