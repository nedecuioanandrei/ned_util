import subprocess


def gloga(args):
    cmd = "git log --oneline --decorate --graph --all"
    subprocess.run(cmd, shell=True)
