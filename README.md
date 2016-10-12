# crirm - Criteria Remove
[![PyPI version](https://badge.fury.io/py/crirm.svg)](https://badge.fury.io/py/crirm)
This is a small and neat tool to clean file system trees by removing files
matching specified criteria.

## Usage
```
usage: crirm [-h] [-r] [-f] [-a AGE] [-n NAME] [-D] [-e] [-v] path

positional arguments:
  path                  root path where the criteria will be applied

optional arguments:
  -h, --help            show this help message and exit
  -r, --recursive       apply criteria in subdirectories
  -f, --force           do not ask for confirmation on delete
  -a AGE, --age AGE     files older than the given number of days
  -n NAME, --name NAME  regular expression for the filename to match
  -D, --dry-run         print found files but do not delete
  -e, --delete-empty    delete empty directories
  -v, --verbose         verbose output
 ```
