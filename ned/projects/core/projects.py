import datetime
import io
import os
import pathlib as p
import shutil
import subprocess

import yaml

from ned.projects.core.constants import PROJECTS_DIR, TMUX_STORAGE


def lst(args):
    for project in os.listdir(PROJECTS_DIR):
        full_path = p.Path(PROJECTS_DIR).joinpath(project)
        if os.path.isdir(full_path):
            date = datetime.datetime.fromtimestamp(
                full_path.stat().st_mtime, tz=datetime.timezone.utc
            )
            print("{} {}".format(project.ljust(30, " "), date.date()))


def create(args):
    project_name = args.name
    current_projects = os.listdir(PROJECTS_DIR)
    if project_name in current_projects:
        print(
            "project name conflict. There is already a project with this name. {}".format(
                project_name
            )
        )
        return

    project_path = p.Path(PROJECTS_DIR).joinpath(project_name)
    os.mkdir(project_path)

    if args.git:
        cmd = "cd {} && git init".format(project_path)
        subprocess.run(cmd, shell=True)


def workon(args):
    project = args.project
    if not project in os.listdir(PROJECTS_DIR):
        print("Project not found")
        return
    project_path = p.Path(PROJECTS_DIR).joinpath(project)
    os.chdir(project_path)

    if args.kitty:
        # subprocess.run("bash", shell=True)
        # subprocess.run("kitty", shell=True)
        subprocess.run("kitty -d={}".format(project_path), shell=True)
        return

    tmux_session_name = "dev-{}".format(project)
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
        data["windows"][0]["start_directory"] = str(project_path)

        print(data)

        with open(session_description, "w") as f:
            yaml.dump(data, f)

    load_cmd = "tmuxp load -y {session_description}".format(
        **{
            "session_description": str(session_description),
        }
    )

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


def delete(args):
    project = args.name
    project_path = p.Path(PROJECTS_DIR).joinpath(project)
    y = input(
        "Are you sure you want to delete dir [yes/no]\n{} ".format(
            project_path
        )
    )

    if y == "yes":
        shutil.rmtree(project_path)
