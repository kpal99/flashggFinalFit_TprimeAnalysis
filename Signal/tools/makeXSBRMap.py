import jinja2
import pandas as pd
import json
import sys

def xsbr(xsJsonFile):
    with open('template/xsbrmap.txt', 'r') as f:
        template = jinja2.Template(f.read())

    with open(xsJsonFile, 'r') as f:
        xsData = json.load(f)

    tprimeMassList = [700, 800, 900, 1000, 1100, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600]
    decayWidthList = [5, 10, 20, 30]
    xsVH = eval(xsData["VH"])
    for tprimeMass in tprimeMassList:
        for decayWidth in decayWidthList:
            process = f"TprimeM{tprimeMass}Decay{decayWidth}pct"
            xsSch = eval(xsData[f"{process}Sch"])
            xsTch = eval(xsData[f"{process}Tch"])
            xsInt = eval(xsData[f"{process}Int"])
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
        print("Usage: python make_xsbrmap.py <xsbr.json>")
        sys.exit(1)
    xsbr(sys.argv[1])
