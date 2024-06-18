import argparse
import jinja2
import os
import sys


def make_config():
    parser = argparse.ArgumentParser(description="Use to make config.py for signalFit",
                                 epilog     ="python3 make_config.py --inputWSDir inputWSDir --procs procs --year year")

    parser.add_argument('--inputWSDir', type=str, required=True, help="input workspace directory")
    parser.add_argument('--year', type=str, required=True, help="Year of the sample, e.g. 20UL17")
    parser.add_argument('--procs', type=str, required=True, help="Process name")

# Parse the arguments
    args = parser.parse_args(None if sys.argv[1:] else ['--help'])

    # read templates/config.py
    with open("template/config_Tprime.py") as f:
        configTemplate = f.read()

    configText = jinja2.Template(configTemplate).render(inputWSDir=args.inputWSDir, year=args.year, procs=args.procs)
    # save configText to a file
    with open(f"config/{args.procs}.py", "w") as f:
        f.write(configText)


if __name__ == '__main__':
    make_config()
