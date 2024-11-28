import argparse
import jinja2
import os
import sys


def make_config():
    parser = argparse.ArgumentParser(description="Use to make config.py for signalFit",
                                 epilog     ="python3 make_config.py --inputWS inputWS --year year")

    parser.add_argument('--inputWS', type=str, required=True, help="input workspace")
    parser.add_argument('--year', type=str, required=True, help="Year of the sample, e.g. 20UL17")
    parser.add_argument('--ext', type=str, help="extensions in output config filename")

# Parse the arguments
    args = parser.parse_args(None if sys.argv[1:] else ['--help'])

    # read templates/config.py
    with open("template/config.py") as f:
        configTemplate = f.read()

    configText = jinja2.Template(configTemplate).render(inputWS=args.inputWS, year=args.year, ext=args.ext)
    # save configText to a file
    with open(f"config/config_{args.ext}_{args.year}.py", "w") as f:
        f.write(configText)
        print(f"Config file saved to config/config_{args.ext}_{args.year}.py")


if __name__ == '__main__':
    make_config()
