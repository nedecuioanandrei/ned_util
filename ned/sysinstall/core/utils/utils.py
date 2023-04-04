from typing import List
import subprocess 

def install_from_apt(apps: List[str]) -> None:
    for app in apps:
        subprocess.run("sudo apt install -y {}".format(app))
