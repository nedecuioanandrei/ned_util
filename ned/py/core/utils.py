import pathlib as p


def create_setup_py(force=False):
    if p.Path("./setup.py").exists() and not force:
        print("setup.pt already created")
        return

    with open("./setup.py", "w") as f:
        f.write(
            """from setuptools import setup 
setup()
        """
        )


def create_setup_cfg(force=False):
    if p.Path("./setup.cfg").exists() and not force:
        print("setup.cfg already created")
        return

    with open("./setup.cfg", "w") as f:
        f.write(
            """[metadata]
name = {}
version = 0.0.1 
classifiers = 
    Programming Language :: Python :: 3

[options]
zip_safe = False 
packages = find:
python_requires = >= 3.10 
install_requires = 

[options.entry_points]
"""
        )


def create_tox_ini(force=False):
    if p.Path("./tox.ini").exists() and not force:
        print("tox.ini already created")
        return

    with open("./tox.ini", "w") as f:
        f.write(
            """[tox]
min_version = 4.4.8
env_list = 
    py{310,311}
    pep8
    lint
    test

[testenv]
description = default 
allowlist_externals = 
    flake8

[testenv:pep8]
description = code quality check 
desp = 
    flake8 
commands = 
    flake8 {} 

[testenv:lint]
description = code formatting
deps = 
    black
    isort 
commands = 
    black -t py310 --line-length 79 {}  
    isort {}

[testenv:test]
description = running tests 
deps = 
    pytest 
    pytest-sugar
commands = 
    pytest tests 
"""
        )
