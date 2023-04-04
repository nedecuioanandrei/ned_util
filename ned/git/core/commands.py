import subprocess


def gloga(args):
    cmd = "git log --oneline --decorate --graph --all"
    subprocess.run(cmd, shell=True)

def gss(args):
    cmd = "gss"
    subprocess.run(cmd, shell=True)
