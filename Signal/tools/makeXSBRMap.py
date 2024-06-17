import jinja2
import pandas as pd
import sys

def xsbr(xsCSVfile):
    with open('template/xsbrmap.txt', 'r') as f:
        template = jinja2.Template(f.read())

    df = pd.read_csv(xsCSVfile)
    for row in df.itertuples():
        print(template.render(**row._asdict()))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python make_xsbrmap.py <xsbr.csv>")
        sys.exit(1)
    xsbr(sys.argv[1])
