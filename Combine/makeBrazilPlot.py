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
    massCount = len(massList)

    x = np.zeros(massCount)
    y = np.zeros(massCount)
    y_stat = np.zeros(massCount)
    y1SigmaLower = np.zeros(massCount)
    y1SigmaHigher = np.zeros(massCount)
    y2SigmaLower = np.zeros(massCount)
    y2SigmaHigher = np.zeros(massCount)
    tprime_xs = np.zeros(massCount)
    massLengthZeros = np.zeros(massCount)

    i = -1
    for mass in massList:
        i += 1
        tprimeProc = f"TprimeM{mass}Decay{decayWidthList[0]}pct"
        file_name = f"higgsCombine_{tprimeProc}_{args.year}.AsymptoticLimits.mH{args.mH}.root"
        #tprime_xs[i] = getCrossSection(f"{tprimeProc}Sch", args.jsonFile)

        # Open ROOT file
        file_ = ROOT.TFile.Open(file_name, "READ")
        if not file_ or file_.IsZombie():
            print(f"Error: Could not open {file_name}")
            continue

        tree_ = file_.Get("limit")
        if not tree_:
            print(f"Error: Could not find 'limit' tree in {file_name}")
        else:
            tree_.SetBranchStatus("*", 1)
            qlimit = np.zeros(1, dtype=np.float64)
            tree_.SetBranchAddress("limit", qlimit)

            x[i] = mass
            for ievent in range(tree_.GetEntries()):
                tree_.GetEntry(ievent)
                # switch statement in python
                if   ievent == 0: y2SigmaLower[i]  = qlimit[0]
                elif ievent == 1: y1SigmaLower[i]  = qlimit[0]
                elif ievent == 2: y[i]             = qlimit[0]
                elif ievent == 3: y1SigmaHigher[i] = qlimit[0]
                elif ievent == 4: y2SigmaHigher[i] = qlimit[0]
            file_.Close()
            print(f"{tprimeProc}: {round(y2SigmaLower[i], 2)}, {round(y1SigmaLower[i], 2)}, {round(y[i], 2)}, {round(y1SigmaHigher[i], 2)}, {round(y2SigmaHigher[i], 2)}")

#    # Read data without systematics
#    print("\nLimit without Systematics")
#    for i in range(massCount):
#        xs = T_xs[i] * 1000 * 0.00223 if method == "xs_X_Br" else 1
#
#        # Open ROOT file
#        file_name = f"{file_path}higgsCombine{mass_str[i]}_nil.AsymptoticLimits.mH120.root"
#        file_ = TFile.Open(file_name, "READ")
#        if not file_ or file_.IsZombie():
#            print(f"Error: Could not open {file_name}")
#            continue
#
#        tree_ = file_.Get("limit")
#        if not tree_:
#            print(f"Error: Could not find 'limit' tree in {file_name}")
#            continue
#
#        tree_.SetBranchStatus("*", 1)
#        qlimit = np.zeros(1, dtype=np.float64)
#        tree_.SetBranchAddress("limit", qlimit)
#
#        x[i] = mass[i]
#        for ievent in range(tree_.GetEntries()):
#            tree_.GetEntry(ievent)
#            if ievent == 2:
#                y_stat[i] = qlimit[0] * xs
#                print(f"Tprime{mass[i]} mean = {qlimit[0]}")
#        file_.Close()

    # got from CAT tutorial
    # https://gitlab.cern.ch/cms-analysis/analysisexamples/plotting-demo/-/blob/master/3-tutorial_CAT_limitplot.ipynb
    oneStdDevColor = ROOT.TColor.GetColor("#FFDF7Fff")
    twoStdDevColor = ROOT.TColor.GetColor("#85D1FBff")

    # Create graphs
    canvas = ROOT.TCanvas("", "", 0, 0, 600, 500)
    canvas.SetGridx()
    canvas.SetGridy()
    canvas.SetLogy()

    statOnlyLine = ROOT.TGraph(massCount, x, y_stat)
    statOnlyLine.SetLineColor(ROOT.kRed)


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

    #twoStdDevLine.GetYaxis().SetTitle("#sigma_{Tbq}#mathcal{B}_{T #to tH} [fb]")

    centralLine = ROOT.TGraph(massCount, np.array(x, dtype=np.float64), np.array(y, dtype=np.float64))
    centralLine.SetLineWidth(2)

    theoryXsLine = ROOT.TGraph(massCount, np.array(x, dtype=np.float64), np.ones(massCount))
    theoryXsLine.SetLineWidth(2)
    theoryXsLine.SetLineStyle(2)

    twoStdDevLine.Draw("SAME 3l")
    oneStdDevLine.Draw("SAME 3l")
    centralLine.Draw("SAME")
    theoryXsLine.Draw("SAME")

    # Canva3 and plotting
    tex1 = ROOT.TLatex()
    tex1.SetNDC()
    tex1.SetTextSize(0.05)
    tex1.DrawLatex(0.115, 0.85, "CMS #it{#bf{Preliminary}}")

    tex3 = ROOT.TLatex()
    tex3.SetNDC()
    tex3.SetTextSize(0.04)
    year = args.year
    lumi = lumiMap[year]
    energy = energyMap[year]
    if energy == 13:
        tex3.DrawLatex(0.67, 0.91, f"#bf{{{lumi} fb^{{-1}} ({energy} TeV)}}")
    elif energy == 13.6:
        tex3.DrawLatex(0.66, 0.91, f"#bf{{{lumi} fb^{{-1}} ({energy} TeV)}}")

    legend = ROOT.TLegend(0.15, 0.71, 0.88, 0.84)
    legend.SetNColumns(2)
    legend.SetBorderSize(0)
    legend.SetTextSize(0.03)
    legend.SetFillStyle(0)
    legend.AddEntry(centralLine, "Expected (#mu)", "l")
    legend.AddEntry(theoryXsLine, "Theoretical (#mu)", "l")
    #legend.AddEntry(statOnlyLine, "Stat. Only (Cross-section)", "l")
    legend.AddEntry(oneStdDevLine, "#pm 1 std. deviation", "f")
    legend.AddEntry(twoStdDevLine, "#pm 2 std. deviation", "f")

    #g_stat.Draw("L SAME")
    legend.Draw()
    canvas.Update()

    # Save outputs
    fileName = f"{args.outDir}/limit_mu_decay{decayWidthList[0]}pct"
    canvas.SaveAs(f"{fileName}.png")
    canvas.SaveAs(f"{fileName}.pdf")
    canvas.SaveAs(f"{fileName}.C")
    canvas.SaveAs(f"{fileName}.root")
    print(f"Saved png, pdf, root, C: {fileName}")
    canvas.Close()

    # Adjusting to cross-section
#    for values in [y, y_stat, y2SigmaLower, y1SigmaLower, y1SigmaHigher, y2SigmaHigher]:
#        values *= tprime_xs
#
#    canvas = ROOT.TCanvas("", "", 0, 0, 600, 500)
#    canvas.SetGridx()
#    canvas.SetGridy()
#    #canvas.SetLogy()
#
#    statOnlyLine = ROOT.TGraph(massCount, x, y_stat)
#    statOnlyLine.SetLineColor(ROOT.kRed)
#
#
#    y1SigmaLowerError = abs(y - y1SigmaLower)
#    y1SigmaHigherError = abs(y - y1SigmaHigher)
#    oneStdDevLine = ROOT.TGraphAsymmErrors(massCount, x, y,
#                           massLengthZeros, massLengthZeros, y1SigmaLowerError, y1SigmaHigherError)
#    oneStdDevLine.SetFillColor(oneStdDevColor)
#    oneStdDevLine.SetLineWidth(0)
#
#    y2SigmaLowerError = abs(y - y2SigmaLower)
#    y2SigmaHigherError = abs(y - y2SigmaHigher)
#    twoStdDevLine = ROOT.TGraphAsymmErrors(massCount, x, y,
#                           massLengthZeros, massLengthZeros, y2SigmaLowerError, y2SigmaHigherError)
#    twoStdDevLine.SetFillColor(twoStdDevColor)
#    twoStdDevLine.SetLineWidth(0)
#
#    twoStdDevLine.GetXaxis().SetTitle("T mass [GeV]")
#    #twoStdDevLine.GetYaxis().SetRangeUser(-10, 150)
#    twoStdDevLine.GetYaxis().SetRangeUser(0.0001, 50)
#    twoStdDevLine.GetYaxis().SetTitle("#sigma_{Tbq}B_{T#rightarrow tH} [fb]")
#    twoStdDevLine.SetTitle("")
#
#    centralLine = ROOT.TGraph(massCount, np.array(x, dtype=np.float64), np.array(y, dtype=np.float64))
#    centralLine.SetLineWidth(2)
#
#    theoryXsLine = ROOT.TGraph(massCount, np.array(x, dtype=np.float64), tprime_xs)
#    theoryXsLine.SetLineWidth(2)
#    theoryXsLine.SetLineStyle(2)
#
#    twoStdDevLine.Draw("a3")
#    oneStdDevLine.Draw("SAME 3l")
#    centralLine.Draw("SAME")
#    theoryXsLine.Draw("SAME")
#
#    # Canvas and plotting
#    tex1 = ROOT.TLatex()
#    tex1.SetNDC()
#    tex1.SetTextSize(0.05)
#    tex1.DrawLatex(0.115, 0.85, "CMS #it{#bf{Preliminary}}")
#
#    tex3 = ROOT.TLatex()
#    tex3.SetNDC()
#    tex3.SetTextSize(0.04)
#    year = args.year
#    lumi = lumiMap[year]
#    energy = energyMap[year]
#    if energy == 13:
#        tex3.DrawLatex(0.67, 0.91, f"#bf{{{lumi} fb^{{-1}} ({energy} TeV)}}")
#    elif energy == 13.6:
#        tex3.DrawLatex(0.66, 0.91, f"#bf{{{lumi} fb^{{-1}} ({energy} TeV)}}")
#
#    legend = ROOT.TLegend(0.15, 0.71, 0.88, 0.84)
#    legend.SetNColumns(2)
#    legend.SetBorderSize(0)
#    legend.SetTextSize(0.03)
#    legend.SetFillStyle(0)
#    legend.AddEntry(centralLine, "Expected -section)", "l")
#    legend.AddEntry(theoryXsLine, "Theoretical (Cross-section)", "l")
#    #legend.AddEntry(statOnlyLine, "Stat. Only (Cross-section)", "l")
#    legend.AddEntry(oneStdDevLine, "#pm 1 std. deviation", "f")
#    legend.AddEntry(twoStdDevLine, "#pm 2 std. deviation", "f")
#
#    #g_stat.Draw("L SAME")
#    legend.Draw()
#    canvas.Update()
#
#    # Save outputs
#    fileName = f"{args.outDir}/limit_xs_decay{decayWidthList[0]}pct"
#    canvas.SaveAs(f"{fileName}.png")
#    canvas.SaveAs(f"{fileName}.pdf")
#    canvas.SaveAs(f"{fileName}.C")
#    canvas.SaveAs(f"{fileName}.root")
#    print(f"Saved png, pdf, root, C: {fileName}")

def main():
    parser = argparse.ArgumentParser(description="Used to print brazilian plots of asymptotic limits", epilog ="")

# Add the arguments
    parser.add_argument("--jsonFile", help="Name of the XS json file")
    parser.add_argument("--outDir", required=True, help="Name of the output directory")
    parser.add_argument("--year", required=True, default="", help="Year that's written in higgAnalysis filename")
    parser.add_argument("--decayWidth", default=5, help="Decay width of Higgs used for limit extraction, default is 5")
    parser.add_argument("--mH", default=125.38, type=float, help="Mass of Higgs using during asymptotic limit calculations, default is 125.38")

# Parse the arguments
    args = parser.parse_args(None if sys.argv[1:] else ['--help'])
    makeBrazilPlot(args)

# Example usage
if __name__ == "__main__":
    main()
