#!/usr/bin/env python3
import os
import sys
import shutil
import argparse
import subprocess

skeleton_repo = "https://github.com/mciucu/stemjs-demo"

def main():
    parser = argparse.ArgumentParser(description='Create simple stemjs app')
    parser.add_argument('project_dir', metavar='<project-directory>')

    args = parser.parse_args()
    project_dir = args.project_dir

    if os.path.exists(project_dir):
        print("Directory {} already exists!", project_dir)
        return -1

    print("Importing skeleton from {}\n".format(skeleton_repo))
    subprocess.check_call(['git', 'clone', skeleton_repo, project_dir])
    shutil.rmtree('{}/.git'.format(project_dir))

    print("Globally installing babel-cli and rollup\n")
    subprocess.check_call(['sudo', 'npm', 'install', '-g', 'babel-cli', 'rollup'])

    print("Installing requirements with npm\n")
    subprocess.check_call(['npm', 'update'], cwd=project_dir)

    print("Compiling using rollup... ", end='', flush=True)
    subprocess.check_call(['rollup', '-c'], cwd="{}/src".format(project_dir), stdout=open(os.devnull, "w"))
    print("OK")

    print("\nSuccessfully created project {}".format(project_dir))
    print("Check out the README located there")
    print("\nInside that directory, you can run\n")
    print("\tnpm start")
    print("\t\tto start a simple development server\n")

    print("\tcd src; rollup -c --watch")
    print("\t\tto start rollup\n")


if __name__ == "__main__":
    sys.exit(main())