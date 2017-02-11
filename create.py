#!/usr/bin/env python3
import os
import sys
import shutil
import argparse
import subprocess

skeleton_repo = "https://github.com/mciucu/stemjs-demo"

global_requirements = ['babel-cli', 'rollup']

def colorize(text):
    COLOR_CODE = '\033[95m'
    END_CODE = '\033[0m'
    return COLOR_CODE + text + END_CODE

def main():
    parser = argparse.ArgumentParser(description='Create simple stemjs app')
    parser.add_argument('project_dir', metavar='<project-directory>')

    backend = parser.add_mutually_exclusive_group()
    backend.add_argument('-e', '--express', help='Use Express as server backend', action='store_true')
    backend.add_argument('-d', '--django', help='Use Django as server backend', action='store_true')
    backend.add_argument('-s', '--simple', help='Use SimpleHTTPServer as server backend (default)', action='store_true')

    args = parser.parse_args()
    project_dir = args.project_dir

    if os.path.exists(project_dir):
        print("Directory {} already exists!".format(project_dir))
        return -1

    if args.express:
        skeleton_branch = "express"
        skeleton_type = "Express"
    elif args.django:
        skeleton_branch = "django"
        skeleton_type = "Django"
    else:
        skeleton_branch = "master"
        skeleton_type = "SimpleHTTPServer"

    print("Importing skeleton with {}\n".format(skeleton_type))

    subprocess.check_call(['git', 'clone', skeleton_repo, project_dir])
    subprocess.check_call(['git', 'checkout', skeleton_branch], cwd=project_dir)

    shutil.rmtree('{}/.git'.format(project_dir))

    print("Globally installing {}\n".format(", ".join(map(colorize, global_requirements))))
    subprocess.check_call(['sudo', 'npm', 'install', '-g'] +  global_requirements)

    print("Installing requirements with npm\n")
    subprocess.check_call(['npm', 'update'], cwd=project_dir)

    print("Compiling\n", end='', flush=True)
    subprocess.check_call(['npm', 'run-script', 'build'], cwd=project_dir)

    print("\nSuccessfully created project {} at {}".format(colorize(project_dir), colorize(os.path.abspath(project_dir))))
    print("Check out the README located there")
    print("\nInside that directory, you can run\n")
    print("\tnpm start")
    print("\t\tto start a simple development server\n")

    print("\tnpm run-script watch")
    print("\t\tto watch for changes and recompile\n")

    print("Also try {} --help for more options (such as express or django backend)".format(sys.argv[0]))


if __name__ == "__main__":
    sys.exit(main())
