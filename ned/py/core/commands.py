import os
import pathlib as p

from ned.py.core.utils import create_setup_cfg, create_setup_py, create_tox_ini


def init(args):
    os.makedirs("./tests", exist_ok=True)
    create_setup_py(force=args.force)
    create_setup_cfg(force=args.force)
    create_tox_ini(force=args.force)


def create_packages(args):
    for name in args.names:
        os.makedirs("./{}".format(name), exist_ok=True)

        if p.Path("./{}/__init__.py".format(name)).exists():
            print("package already created")

        os.mknod("./{}/__init__.py".format(name))
