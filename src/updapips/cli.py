#!/usr/bin/env python3
# ------------------------------------------------------------------------------------------------------
# -- CLI for cleaning __pycache__ nested folders from specified root path
# ------------------------------------------------------------------------------------------------------
# ======================================================================================================

# PYTHON_ARGCOMPLETE_OK
import argcomplete, argparse

import os
import sys

from quickcolor.color_def import color
from showexception.showexception import exception_details

from .updapips import get_pip_list_pkgs, get_pip_list_outdated_pkgs
from .updapips import upgrade_pip_pkg

# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------

def cli():
    try:
        parser = argparse.ArgumentParser(
                    description=f'{"-." * 3}  {color.CBLUE2}Update PIPs {color.CYELLOW2}utility!{color.CEND}',
                    epilog='-.' * 40)

        parser.add_argument('--version', action="store_true", help='top-level package version')

        subparsers = parser.add_subparsers(dest='cmd')

        p_showAllPipPkgs = subparsers.add_parser('show.all.pip.pkgs',
                                              help='show all PIP packages installed in current virt env')

        p_showOutdatedPipPkgs = subparsers.add_parser('show.outdated.pip.pkgs',
                                                   help='show PIP packages in virtual env that are outdated')

        p_upgradePipPkgs = subparsers.add_parser('upgrade.pips',
                                                help='updgrade all outdated PIP pkgs')

        argcomplete.autocomplete(parser)
        args = parser.parse_args()
        # print(args)

        if len(sys.argv) == 1:
            parser.print_help(sys.stderr)
            sys.exit(0)

        if args.version:
            from importlib.metadata import version
            import bkmeup
            print(f'{color.CGREEN}{os.path.basename(sys.argv[0])}{color.CEND} resides in package ' + \
                    f'{color.CBLUE2}{updapips.__package__}{color.CEND} ' + \
                    f'version {color.CVIOLET2}{version("updapips")}{color.CEND} ...')
            sys.exit(0)

        if args.cmd == 'show.all.pip.pkgs':
            pkgs = get_pip_list_pkgs()
            print(f"There are {color.CYELLOW2}{len(pkgs)}{color.CEND} PIP packages installed in this environment!\n")
            for idx, pkg in enumerate(pkgs):
                print(f" --> {color.CWHITE2}{idx+1:>3}. {color.CBLUE2}{pkg['name']:<30}{color.CEND} " + \
                        f"ver: {color.CYELLOW2}{pkg['version']:<15}{color.CEND}", end=" ", flush=True)
                if 'editable_project_location' in pkg.keys():
                    print(f"{color.CGREEN}{pkg['editable_project_location']:<30}{color.CEND}")
                else:
                    print()

        elif args.cmd == 'show.outdated.pip.pkgs':
            pkgs = get_pip_list_outdated_pkgs()
            if len(pkgs):
                print(f" ... Found {color.CYELLOW2}{len(pkgs)}{color.CEND} PIP packages that can be upgraded!\n")
                for idx, pkg in enumerate(pkgs):
                    print(f" --> {color.CWHITE2}{idx+1:>3}. {color.CYELLOW2}{pkg['name']:<30}{color.CEND} " + \
                            f"installed: {color.CRED2}{pkg['version']:<15}{color.CEND} " + \
                            f"available: {color.CCYAN2}{pkg['latest_version']:<15}{color.CEND}", end=" ", flush=True)
                    if 'editable_project_location' in pkg.keys():
                        print(f"{color.CGREEN}{pkg['editable_project_location']:<30}{color.CEND}")
                    else:
                        print()
            else:
                print(f"{color.CGREEN}There are no PIP packages in this environment that need to be upgraded!{color.CEND}")

        elif args.cmd == 'upgrade.pips':
            pkgs = get_pip_list_outdated_pkgs()
            if len(pkgs):
                for pkg in pkgs:
                    upgrade_pip_pkg(pkg['name'], pkg['version'], pkg['latest_version'])
                print(f"\n .. Finished upgrade run for {color.CYELLOW2}{len(pkgs)} packages{color.CEND}!\n")

            else:
                print(f"{color.CGREEN}There are no PIP packages in this environment that need to be upgraded!{color.CEND}")

    except Exception as e:
        exception_details(e, "UpDaPIPs CLI", True)

# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------

