#!/usr/bin/env python3

import json
import sys
import subprocess

from quickcolor.color_def import color
from delayviewer.spinner import handle_spinner

def get_pip_list_pkgs() -> list:
    result = subprocess.run([sys.executable, '-m', 'pip', 'list', '--format=json'], capture_output=True, text=True)
    return json.loads(result.stdout)

@handle_spinner
def get_pip_list_outdated_pkgs(spinner = None) -> list:
    spinner.start(f" -- {color.CYELLOW2}Retrieving outdated packages{color.CEND} ...")
    result = subprocess.run([sys.executable, '-m', 'pip', 'list', '--outdated', '--format=json'], capture_output=True, text=True)
    spinner.stop()
    pkgList = json.loads(result.stdout)
    if len(pkgList):
        print(f"    Found {color.CCYAN}{len(pkgList)} packages{color.CEND} to upgrade!\n")
    else:
        print(f"    {color.CGREEN2}No package updates required!{color.CEND}!\n")
    return pkgList

@handle_spinner
def upgrade_pip_pkg(pkgName: str, debug: bool = False, spinner = None):
    spinner.start(f" -- Upgrading {color.CGREEN2}{pkg['name']}{color.CEND} ...")
    result = subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', pkgName], capture_output=True, text=True)
    spinner.stop()

    if result.returncode:
        print(f"{color.CRED2}Error:{color.CWHI2}{result.stderr}{color.CEND}")

    if debug:
        print(f'STDOUT: {result.stdout}')
        print(f'STDERR: {result.stderr}')
        print(f'retcode: {result.returncode}')


# python -m pip list --format=json | jq -r '.[] | [.name, .version] | @csv' > packages.csv

# pkgs = get_pip_list_pkgs()
# print(pkgs)

outdatedPkgs = get_pip_list_outdated_pkgs()
# print (outdatedPkgs)

if len(outdatedPkgs):
    # numPkgsToUpgrade = 1
    for pkg in outdatedPkgs:
        upgrade_pip_pkg(pkg['name'])
        # numPkgsToUpgrade -= 1
        # if numPkgsToUpgrade == 0:
        #     break

    print(f"\n .. Finished upgrade run for {color.CYELLOW2}{len(outdatedPkgs)} packages{color.CEND}!\n")


