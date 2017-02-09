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

    print("Importing skeleton from {}".format(skeleton_repo))
    subprocess.check_call(['git', 'clone', skeleton_repo, project_dir])
    shutil.rmtree('{}/.git'.format(project_dir))

    print("Globally installing babel-cli and rollup")
    subprocess.check_call(['sudo', 'npm', 'install', '-g', 'babel-cli', 'rollup'])

    subprocess.check_call(['npm', 'update'], cwd=project_dir)

    subprocess.check_call(['rollup', '-c'], cwd="{}/src".format(project_dir))

    print("Successfully created project {}".format(project_dir))

if __name__ == "__main__":
    sys.exit(main())
