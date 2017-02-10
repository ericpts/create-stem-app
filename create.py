#!/usr/bin/env python3
import os
import sys
import shutil
import argparse
import subprocess

base_skeleton_repo = "https://github.com/mciucu/stemjs-demo"
express_skeleton_repo = "https://github.com/ericpts/stemjs-demo"

global_requirements = ['babel-cli', 'rollup']

def colorize(text):
    COLOR_CODE = '\033[95m'
    END_CODE = '\033[0m'
    return COLOR_CODE + text + END_CODE

def main():
    parser = argparse.ArgumentParser(description='Create simple stemjs app')
    parser.add_argument('project_dir', metavar='<project-directory>')
    parser.add_argument('-e', '--express', help='Use express as server backend', action='store_true')

    args = parser.parse_args()
    project_dir = args.project_dir

    if os.path.exists(project_dir):
        print("Directory {} already exists!".format(project_dir))
        return -1

    skeleton_repo = express_skeleton_repo if args.express else base_skeleton_repo

    print("Importing skeleton from {}\n".format(skeleton_repo))
    subprocess.check_call(['git', 'clone', skeleton_repo, project_dir])
    shutil.rmtree('{}/.git'.format(project_dir))

    print("Globally installing {}\n".format(", ".join(map(colorize, global_requirements))))
    subprocess.check_call(['sudo', 'npm', 'install', '-g', *global_requirements])

    print("Installing requirements with npm\n")
    subprocess.check_call(['npm', 'update'], cwd=project_dir)

    print("Compiling using rollup... ", end='', flush=True)
    subprocess.check_call(['rollup', '-c'], cwd="{}/src".format(project_dir), stdout=open(os.devnull, "w"))
    print("OK")

    print("\nSuccessfully created project {} at {}".format(colorize(project_dir), colorize(os.path.abspath(project_dir))))
    print("Check out the README located there")
    print("\nInside that directory, you can run\n")
    print("\tnpm start")
    print("\t\tto start a simple development server\n")

    print("\tcd src; rollup -c --watch")
    print("\t\tto start rollup\n")

    print("Also try {} --help for more options (such as express backend)".format(sys.argv[0]))


if __name__ == "__main__":
    sys.exit(main())
