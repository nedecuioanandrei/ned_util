import pathlib

from ned.projects.core.config import get_config

CONFIG_PATH = "{}/.ned/ned.conf".format(pathlib.Path.home())
PROJECTS_DIR = "/home/nedelcu/Projects/"
TMUX_STORAGE = "/home/nedelcu/.ned/tmux"

for key, value in get_config(CONFIG_PATH).items():
    vars()[key] = value


def list_conf() -> None:
    print(f"{PROJECTS_DIR=}\n{TMUX_STORAGE=}\n{CONFIG_PATH=}")
