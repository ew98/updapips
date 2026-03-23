# UpDaPips

**UpDaPips** is a command line package to upgrade outdated PIP packages in the current environment

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install **updapips**.

```bash
pip install updapips
```

## CLI Utility

The following CLI is provided in this package.

```bash
╰─ updapips -h                                                                                                                           ─╯
usage: updapips [-h] [--version] {show.all.pip.pkgs,show.outdated.pip.pkgs,upgrade.pips} ...

-.-.-. Update PIPs utility!

positional arguments:
  {show.all.pip.pkgs,show.outdated.pip.pkgs,upgrade.pips}
    show.all.pip.pkgs   show all PIP packages installed in current virt env
    show.outdated.pip.pkgs
                        show PIP packages in virtual env that are outdated
    upgrade.pips        updgrade all outdated PIP pkgs

options:
  -h, --help            show this help message and exit
  --version             top-level package version

-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
```


## License

[MIT](https://choosealicense.com/licenses/mit/)

