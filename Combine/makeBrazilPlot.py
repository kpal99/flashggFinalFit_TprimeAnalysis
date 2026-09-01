import argparse
import csv
import ROOT
import numpy as np
import sys
from tHgg_utils.utils import lumiMap, energyMap, getCrossSection

ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch(True)  # Disable graphical output for batch mode
ROOT.gErrorIgnoreLevel = ROOT.kWarning

def makeBrazilPlot(args):
    massList = [700, 800, 900, 1000, 1100, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600]

    try:
        decayWidthList = args.decayWidth.split(",")
    except AttributeError:
        decayWidthList = [args.decayWidth]
    decayWidthList = [int(d) for d in decayWidthList]

    year = args.year

    # Use lists instead of pre-sized numpy arrays, so we can skip
    # any mass point whose file/tree is missing or incomplete.
    x_list = []
    y_list = []
    y1SigmaLower_list = []
    y1SigmaHigher_list = []
    y2SigmaLower_list = []
    y2SigmaHigher_list = []

    for mass in massList:
        tprimeProc = f"TprimeM{mass}Decay{decayWidthList[0]}pct"
        file_name = f"higgsCombine_{tprimeProc}_{year}_withSyst.AsymptoticLimits.mH{args.mH}.root"

        file_ = ROOT.TFile.Open(file_name, "READ")
        if not file_ or file_.IsZombie():
            print(f"Error: Could not open {file_name}, skipping mass {mass}")
            continue

        tree_ = file_.Get("limit")
        if not tree_:
            print(f"Error: Could not find 'limit' tree in {file_name}, skipping mass {mass}")
            file_.Close()
            continue

        if tree_.GetEntries() < 5:
            print(f"Error: {file_name} has only {tree_.GetEntries()} entries (need 5), skipping mass {mass}")
            file_.Close()
            continue

        tree_.SetBranchStatus("*", 1)
        qlimit = np.zeros(1, dtype=np.float64)
        tree_.SetBranchAddress("limit", qlimit)

        vals = [None] * 5
        for ievent in range(5):
            tree_.GetEntry(ievent)
            vals[ievent] = qlimit[0]
        file_.Close()

        y2SigmaLower_val, y1SigmaLower_val, y_val, y1SigmaHigher_val, y2SigmaHigher_val = vals

        # Only now, having successfully read all five values, commit this mass point
        x_list.append(mass)
        y2SigmaLower_list.append(y2SigmaLower_val)
        y1SigmaLower_list.append(y1SigmaLower_val)
        y_list.append(y_val)
        y1SigmaHigher_list.append(y1SigmaHigher_val)
        y2SigmaHigher_list.append(y2SigmaHigher_val)

        print(f"{tprimeProc}: {round(y2SigmaLower_val, 2)}, {round(y1SigmaLower_val, 2)}, "
              f"{round(y_val, 2)}, {round(y1SigmaHigher_val, 2)}, {round(y2SigmaHigher_val, 2)}")

    if not x_list:
        print("Error: No valid mass points found, nothing to plot.")
        return

    # Convert to numpy arrays now that we know which masses actually succeeded
    massCount = len(x_list)
    x = np.array(x_list, dtype=np.float64)
    y = np.array(y_list, dtype=np.float64)
    y1SigmaLower = np.array(y1SigmaLower_list, dtype=np.float64)
    y1SigmaHigher = np.array(y1SigmaHigher_list, dtype=np.float64)
    y2SigmaLower = np.array(y2SigmaLower_list, dtype=np.float64)
    y2SigmaHigher = np.array(y2SigmaHigher_list, dtype=np.float64)
    massLengthZeros = np.zeros(massCount)
    tprime_xs = np.ones(massCount)

    # --- Stat-only (woSyst) overlay: fully independent pass, so a bad/missing
    # woSyst file for a given mass doesn't remove that mass from the withSyst
    # curves above, and vice versa.
    x_wo_list = []
    y_wo_list = []
    if args.woSyst:
        for mass in massList:
            tprimeProc = f"TprimeM{mass}Decay{decayWidthList[0]}pct"
            file_name_wo = f"higgsCombine_{tprimeProc}_{year}_woSyst.AsymptoticLimits.mH{args.mH}.root"

            file_wo = ROOT.TFile.Open(file_name_wo, "READ")
            if not file_wo or file_wo.IsZombie():
                print(f"Error: Could not open {file_name_wo}, skipping mass {mass} for Stat-only")
                continue

            tree_wo = file_wo.Get("limit")
            if not tree_wo:
                print(f"Error: Could not find 'limit' tree in {file_name_wo}, skipping mass {mass} for Stat-only")
                file_wo.Close()
                continue

            if tree_wo.GetEntries() < 5:
                print(f"Error: {file_name_wo} has only {tree_wo.GetEntries()} entries (need 5), "
                      f"skipping mass {mass} for Stat-only")
                file_wo.Close()
                continue

            tree_wo.SetBranchStatus("*", 1)
            qlimit_wo = np.zeros(1, dtype=np.float64)
            tree_wo.SetBranchAddress("limit", qlimit_wo)

            vals_wo = [None] * 5
            for ievent in range(5):
                tree_wo.GetEntry(ievent)
                vals_wo[ievent] = qlimit_wo[0]
            file_wo.Close()

            # Order is: -2sigma, -1sigma, central (0.5 quantile), +1sigma, +2sigma
            y_wo_val = vals_wo[2]

            x_wo_list.append(mass)
            y_wo_list.append(y_wo_val)

            print(f"{tprimeProc} (Stat-only): {round(y_wo_val, 2)}")

        if not x_wo_list:
            print("Warning: --woSyst was set but no valid Stat-only mass points were found; "
                  "skipping Stat-only overlay.")

    # got from CAT tutorial
    # https://gitlab.cern.ch/cms-analysis/analysisexamples/plotting-demo/-/blob/master/3-tutorial_CAT_limitplot.ipynb
    oneStdDevColor = ROOT.TColor.GetColor("#FFDF7Fff")
    twoStdDevColor = ROOT.TColor.GetColor("#85D1FBff")
    statOnlyColor = ROOT.TColor.GetColor("#00008B")  # dark blue

    # Create graphs
    canvas = ROOT.TCanvas("", "", 0, 0, 600, 500)
    canvas.SetGridx()
    canvas.SetGridy()
    canvas.SetLogy()

    y1SigmaLowerError = abs(y - y1SigmaLower)
    y1SigmaHigherError = abs(y - y1SigmaHigher)
    oneStdDevLine = ROOT.TGraphAsymmErrors(massCount, x, y,
                           massLengthZeros, massLengthZeros, y1SigmaLowerError, y1SigmaHigherError)
    oneStdDevLine.SetFillColor(oneStdDevColor)
    oneStdDevLine.SetLineWidth(0)

    dummy_hist = ROOT.TH1F("dummy", "", 100, 650, 2650)
    dummy_hist.SetMinimum(0.5)
    dummy_hist.SetMaximum(10000)
    dummy_hist.GetXaxis().SetTitle("T mass [GeV]")
    dummy_hist.GetYaxis().SetTitle("95% CL limit on #mu")
    dummy_hist.SetTitle("")
# Draw the dummy histogram first to define the axes
    dummy_hist.Draw()

    y2SigmaLowerError = abs(y - y2SigmaLower)
    y2SigmaHigherError = abs(y - y2SigmaHigher)
    twoStdDevLine = ROOT.TGraphAsymmErrors(massCount, x, y,
                           massLengthZeros, massLengthZeros, y2SigmaLowerError, y2SigmaHigherError)
    twoStdDevLine.SetFillColor(twoStdDevColor)
    twoStdDevLine.SetLineWidth(0)

    centralLine = ROOT.TGraph(massCount, np.array(x, dtype=np.float64), np.array(y, dtype=np.float64))
    centralLine.SetLineWidth(2)

    theoryXsLine = ROOT.TGraph(massCount, np.array(x, dtype=np.float64), np.ones(massCount))
    theoryXsLine.SetLineWidth(2)
    theoryXsLine.SetLineStyle(2)

    twoStdDevLine.Draw("SAME 3l")
    oneStdDevLine.Draw("SAME 3l")
    centralLine.Draw("SAME")
    theoryXsLine.Draw("SAME")

    # Optional overlay: Stat-only (woSyst) central limit curve
    statOnlyLine = None
    if args.woSyst and x_wo_list:
        x_wo = np.array(x_wo_list, dtype=np.float64)
        y_wo = np.array(y_wo_list, dtype=np.float64)
        statOnlyLine = ROOT.TGraph(len(x_wo_list), x_wo, y_wo)
        statOnlyLine.SetLineWidth(2)
        statOnlyLine.SetLineStyle(1)
        statOnlyLine.SetLineColor(statOnlyColor)
        statOnlyLine.Draw("SAME")

    # Optional overlay: comparison limit curve from B2G-21-007
    compareLine = None
    if args.compare:
        tprime_prsaha = [700, 800, 900, 1000, 1100, 1200]
        limit_prsaha = [1.39, 2.52, 3.28, 5.17, 6.97, 10.31]

        compareLine = ROOT.TGraph(len(tprime_prsaha),
                                   np.array(tprime_prsaha, dtype=np.float64),
                                   np.array(limit_prsaha, dtype=np.float64))
        compareLine.SetLineWidth(2)
        compareLine.SetLineStyle(1)
        compareLine.SetLineColor(ROOT.kRed)
        compareLine.Draw("SAME")

    # Canva3 and plotting
    tex1 = ROOT.TLatex()
    tex1.SetNDC()
    tex1.SetTextSize(0.05)
    tex1.DrawLatex(0.115, 0.85, "CMS #it{#bf{Preliminary}}")

    tex3 = ROOT.TLatex()
    tex3.SetNDC()
    tex3.SetTextSize(0.04)
    if year == "full":
        tex3.DrawLatex(0.385, 0.91, f"#bf{{138 fb^{{-1}} (13 TeV) + 61.8 fb^{{-1}} (13.6 TeV)}}")
    else:
        lumi = lumiMap[year]
        energy = energyMap[year]
        if energy == 13:
            tex3.DrawLatex(0.67, 0.91, f"#bf{{{lumi} fb^{{-1}} ({energy} TeV)}}")
        elif energy == 13.6:
            tex3.DrawLatex(0.66, 0.91, f"#bf{{{lumi} fb^{{-1}} ({energy} TeV)}}")

    legend = ROOT.TLegend(0.15, 0.63, 0.88, 0.84)
    legend.SetNColumns(2)
    legend.SetBorderSize(0)
    legend.SetTextSize(0.03)
    legend.SetFillStyle(0)
    legend.AddEntry(centralLine, "Expected (#mu)", "l")
    legend.AddEntry(theoryXsLine, "Theoretical (#mu)", "l")
    legend.AddEntry(oneStdDevLine, "#pm 1 std. deviation", "f")
    legend.AddEntry(twoStdDevLine, "#pm 2 std. deviation", "f")
    if args.woSyst and statOnlyLine is not None:
        legend.AddEntry(statOnlyLine, "Stat-only", "l")
    if args.compare and compareLine is not None:
        legend.AddEntry(compareLine, "B2G-21-007", "l")

    legend.Draw()
    canvas.Update()

    # Save outputs
    if args.outFile:
        fileName = f"{args.outDir}/{args.outFile}"
    else:
        fileName = f"{args.outDir}/{year}_limit_mu_decay{decayWidthList[0]}pct"
    canvas.SaveAs(f"{fileName}.png")
    canvas.SaveAs(f"{fileName}.pdf")
    canvas.SaveAs(f"{fileName}.C")
    canvas.SaveAs(f"{fileName}.root")
    print(f"Saved png, pdf, root, C: {fileName}")
    canvas.Close()

def main():
    parser = argparse.ArgumentParser(description="Used to print brazilian plots of asymptotic limits", epilog ="")

# Add the arguments
    parser.add_argument("--jsonFile", help="Name of the XS json file")
    parser.add_argument("--outDir", required=True, help="Name of the output directory")
    parser.add_argument("--outFile", help="Name of the limit file")
    parser.add_argument("--year", required=True, default="", help="Year that's written in higgAnalysis filename")
    parser.add_argument("--decayWidth", default=5, help="Decay width of Higgs used for limit extraction, default is 5")
    parser.add_argument("--mH", default=125.38, type=float, help="Mass of Higgs using during asymptotic limit calculations, default is 125.38")
    parser.add_argument("--compare", action="store_true", help="If set, overlay the B2G-21-007 comparison limit curve")
    parser.add_argument("--woSyst", action="store_true", help="If set, overlay the Stat-only (woSyst) central limit curve, read from separate woSyst files")

# Parse the arguments
    args = parser.parse_args(None if sys.argv[1:] else ['--help'])
    makeBrazilPlot(args)

# Example usage
if __name__ == "__main__":
    main()
