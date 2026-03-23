#!/usr/bin/env python3
# ------------------------------------------------------------------------------------------------------
# -- update PIP packages
# ------------------------------------------------------------------------------------------------------
# ======================================================================================================

import json
import sys
import subprocess

from quickcolor.color_def import color
from delayviewer.spinner import handle_spinner

# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------

def get_pip_list_pkgs() -> list:
    result = subprocess.run([sys.executable, '-m', 'pip', 'list', '--format=json'], capture_output=True, text=True)
    return json.loads(result.stdout)

# ------------------------------------------------------------------------------------------------------

@handle_spinner
def get_pip_list_outdated_pkgs(debug: bool = False, spinner = None) -> list:
    spinner.start(f" -- {color.CYELLOW2}Retrieving outdated packages{color.CEND} ...", 72)
    result = subprocess.run([sys.executable, '-m', 'pip', 'list', '--outdated', '--format=json'], capture_output=True, text=True)
    spinner.stop()
    pkgList = json.loads(result.stdout)
    if debug:
        if len(pkgList):
            print(f"    Found {color.CCYAN}{len(pkgList)} package(s){color.CEND} to upgrade!\n")
        else:
            print(f"    {color.CGREEN2}No package updates required!{color.CEND}!\n")
    return pkgList

# ------------------------------------------------------------------------------------------------------

@handle_spinner
def upgrade_pip_pkg(pkgName: str, currVer: str, latestVer: str, debug: bool = False, spinner = None):
    spinner.start(f" -- Upgrading {color.CGREEN2}{pkgName}{color.CEND} " + \
            f"from {color.CRED2}{currVer}{color.CEND} to {color.CGREEN}{latestVer}{color.CEND} ...", 90)
    result = subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', pkgName], capture_output=True, text=True)
    spinner.stop()

    if result.returncode:
        print(f"{color.CRED2}Error:{color.CWHITE2}{result.stderr}{color.CEND}")

    if debug:
        print(f'STDOUT: {result.stdout}')
        print(f'STDERR: {result.stderr}')
        print(f'retcode: {result.returncode}')

# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------

