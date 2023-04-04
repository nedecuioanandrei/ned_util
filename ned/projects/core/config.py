import json


def write_default_config(path: str) -> None:
    content = {
        "projects_dir": "/home/nedelcu/Projects",
        "tmux_storage": "/home/nedelcu/.ned/tmux",
    }
    with open(path, "w") as f:
        json.dump(content, f)


def get_config(path: str) -> dict:
    data = None
    with open(path, "r") as f:
        data = json.load(f)
        data = {str(key).upper(): value for key, value in data.items()}
    return data
