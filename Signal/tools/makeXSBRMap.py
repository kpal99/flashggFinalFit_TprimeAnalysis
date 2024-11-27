import jinja2
import pandas as pd
import sys

def xsbr(xsCSVfile):
    with open('template/xsbrmap.txt', 'r') as f:
        template = jinja2.Template(f.read())

    df = pd.read_csv(xsCSVfile)
    tprimeMassList = [700, 800, 900, 1000, 1100, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600]
    decayWidthList = [5, 10, 20, 30]
    xsVH = df[df["process"] == "VH"]["xs_pb"].values[0]
    for tprimeMass in tprimeMassList:
        for decayWidth in decayWidthList:
            process = f"TprimeM{tprimeMass}Decay{decayWidth}pct"
            xsSch = df[df["process"] == f"{process}Sch"]["xs_pb"].values[0]
            xsTch = df[df["process"] == f"{process}Tch"]["xs_pb"].values[0]
            xsInt = df[df["process"] == f"{process}Int"]["xs_pb"].values[0]
            print(template.render(
                process = process,
                xsSch = xsSch,
                xsTch = xsTch,
                xsInt = xsInt,
                xsVH = xsVH
                ))
            print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python make_xsbrmap.py <xsbr.csv>")
        sys.exit(1)
    xsbr(sys.argv[1])
