import argparse
import csv
import ROOT
import numpy as np
import sys

ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch(True)
ROOT.gErrorIgnoreLevel = ROOT.kWarning

lumiMap = {"2016": 36.3, "2017": 41.5, "2018": 59.8, "Run2": 138, "2022": 34.6, "2023": 27.2} # in fb
energyMap = {"2016": 13, "2017": 13, "2018": 13, "Run2": 13, "2022": 13.6, "2023": 13.6}

def getLimitFromFile(filename):
    try:
        file_ = ROOT.TFile.Open(filename, "READ")
    except OSError:
        return 1.0

    if not file_ or file_.IsZombie():
        print(f"Error: Could not open {filename}")
        return None

    tree_ = file_.Get("limit")
    if not tree_:
        print(f"Error: Could not find 'limit' tree in {filename}")
        return None

    qlimit = np.zeros(1, dtype=np.float64)
    tree_.SetBranchAddress("limit", qlimit)

    getEntryArray = []
    for ievent in range(tree_.GetEntries()):
        tree_.GetEntry(ievent)
        getEntryArray.append(qlimit[0])

    if len(getEntryArray) > 2:
        return round(getEntryArray[2], 1)
    else:
        return round(getEntryArray[-1], 1)

    return None

def make2DLimitPlot(args):
    massList = [700, 800, 900, 1000, 1100, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600]
    decayWidthList = [5, 10, 20, 30]

    hist = ROOT.TH2F("limit2D", ";m_{T} [GeV]; \Gamma / m_{T} [%];", len(massList), 0, len(massList), len(decayWidthList), 0, len(decayWidthList))

    hist.GetZaxis().SetTitle("95% CL limit on #mu")
    hist.GetZaxis().SetTitleOffset(1.25)

    # Label bins manually for aesthetics
    for ix, m in enumerate(massList):
        hist.GetXaxis().SetBinLabel(ix + 1, str(m))
    for iy, d in enumerate(decayWidthList):
        hist.GetYaxis().SetBinLabel(iy + 1, f"{d}%")

    for ix, mass in enumerate(massList):
        for iy, decay in enumerate(decayWidthList):
            tprimeProc = f"TprimeM{mass}Decay{decay}pct"
            file_name = f"higgsCombine_{tprimeProc}_{args.year}.AsymptoticLimits.mH{args.mH}.root"
            limit = getLimitFromFile(file_name)
            if limit is not None:
                hist.SetBinContent(ix + 1, iy + 1, limit)
                text = ROOT.TLatex(ix + 0.7, iy + 0.4, f"{limit:.1f}")
                text.SetTextSize(0.03)
                text.Draw()

    # Plotting
    canvas = ROOT.TCanvas("canvas", "", 800, 700)
    ROOT.gPad.SetRightMargin(0.15)
    hist.Draw("COLZ")

    tex1 = ROOT.TLatex()
    tex1.SetNDC()
    tex1.SetTextSize(0.045)
    tex1.DrawLatex(0.10, 0.92, "CMS #bf{Preliminary}")

    tex2 = ROOT.TLatex()
    tex2.SetNDC()
    tex2.SetTextSize(0.04)

    year = args.year
    lumi = lumiMap[year]
    energy = energyMap[year]
    if energy == 13:
        tex2.DrawLatex(0.66, 0.91, f"#bf{{{lumi} fb^{{-1}} ({energy} TeV)}}")
    elif energy == 13.6:
        tex2.DrawLatex(0.65, 0.91, f"#bf{{{lumi} fb^{{-1}} ({energy} TeV)}}")

    outputFile = f"{args.outDir}/limit_2D_{args.year}"
    canvas.SaveAs(f"{outputFile}.png")
    canvas.SaveAs(f"{outputFile}.pdf")
    canvas.SaveAs(f"{outputFile}.root")
    canvas.Close()

    print(f"Saved 2D limit plot to {outputFile}.(png/pdf/root)")


def main():
    parser = argparse.ArgumentParser(description="Plot expected asymptotic limits in 1D or 2D")
    parser.add_argument("--outDir", required=True, help="Output directory")
    parser.add_argument("--year", default="", help="Year that's written in higgAnalysis filename")
    parser.add_argument("--mH", default=125.38, type=float, help="Higgs mass used for limit extraction, default is 125.38")

    args = parser.parse_args(None if sys.argv[1:] else ['--help'])

    make2DLimitPlot(args)


if __name__ == "__main__":
    main()

