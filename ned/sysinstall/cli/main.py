import argparse 
import sys 
from ned.sysinstall.core.install import install

def get_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    
    install_parser = subparsers.add_parser("install", help="Install tools for the given distro.")
    install_parser.add_argument("distro", help="Host distro.")
    install_parser.set_defaults(func=install)

    return parser 


def main():
    parser = get_parser()
    args = parser.parse_args(sys.argv[1:])
    args.func(args)
