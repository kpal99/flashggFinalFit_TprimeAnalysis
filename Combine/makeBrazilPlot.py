import argparse
import csv
import ROOT
import numpy as np
import sys

ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch(True)  # Disable graphical output for batch mode
ROOT.gErrorIgnoreLevel = ROOT.kWarning

def getCrossSection(coreName, csvFile):
    with open(csvFile) as f:
        csvReader = csv.reader(f)
        for row in csvReader:
            processName, xsStr, brStr = row
            if processName == coreName:
                xs_pb = float(xsStr)
                br = float(brStr)
                break
    # convert to xs_fb times Br(H -> dipho)
    xs = xs_pb * 1000 * br
    return xs

def makeBrazilPlot(args):
    massList = [700, 800, 900, 1000, 1100, 1200]
    decayWidthList = [5]
    points = len(massList)

    x = np.zeros(points)
    y = np.zeros(points)
    y_stat = np.zeros(points)
    eyl = np.zeros(points)
    eyh = np.zeros(points)
    ey2l = np.zeros(points)
    ey2h = np.zeros(points)
    tprime_xs = np.zeros(points)

    # Read data with systematics
    print("Limit with Systematics")
    i = -1
    for mass in massList:
        i += 1
        tprimeProc = f"TprimeM{mass}Decay{decayWidthList[0]}pct"
        tprime_xs[i] = getCrossSection(f"{tprimeProc}Sch", args.csvFile)

        # Open ROOT file
        file_name = f"higgsCombine_{tprimeProc}.AsymptoticLimits.mH{args.mH}.root"
        file_ = ROOT.TFile.Open(file_name, "READ")
        if not file_ or file_.IsZombie():
            print(f"Error: Could not open {file_name}")
            continue

        tree_ = file_.Get("limit")
        if not tree_:
            print(f"Error: Could not find 'limit' tree in {file_name}")
            continue

        tree_.SetBranchStatus("*", 1)
        qlimit = np.zeros(1, dtype=np.float64)
        tree_.SetBranchAddress("limit", qlimit)

        x[i] = mass
        for ievent in range(tree_.GetEntries()):
            tree_.GetEntry(ievent)
            if ievent == 0:
                ey2l[i] = qlimit[0]
            elif ievent == 1:
                eyl[i] = qlimit[0]
            elif ievent == 2:
                y[i] = qlimit[0]
            elif ievent == 3:
                eyh[i] = qlimit[0]
            elif ievent == 4:
                ey2h[i] = qlimit[0]
        file_.Close()
        print(f"{tprimeProc}: {round(ey2l[i], 2)}, {round(eyl[i], 2)}, {round(y[i], 2)}, {round(eyh[i], 2)}, {round(ey2h[i], 2)}")

#    # Read data without systematics
#    print("\nLimit without Systematics")
#    for i in range(points):
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

    # Create graphs
    statOnlyLine = ROOT.TGraph(points, np.array(x, dtype=np.float64), np.array(y_stat, dtype=np.float64))
    statOnlyLine.SetLineColor(ROOT.kRed)

    oneStdDevLine = ROOT.TGraphAsymmErrors(points, np.array(x, dtype=np.float64), np.array(y, dtype=np.float64),
                           np.zeros(points), np.zeros(points), eyl, eyh)
    oneStdDevLine.SetFillColor(ROOT.kGreen)

    twoStdDevLine = ROOT.TGraphAsymmErrors(points, np.array(x, dtype=np.float64), np.array(y, dtype=np.float64),
                            np.zeros(points), np.zeros(points), ey2l, ey2h)
    twoStdDevLine.SetFillColor(ROOT.kYellow)

    twoStdDevLine.GetXaxis().SetTitle("T mass [GeV]")
    twoStdDevLine.GetYaxis().SetRangeUser(0.5, 500)
    #twoStdDevLine.GetYaxis().SetTitle("#sigma_{Tbq}#mathcal{B}_{T #to tH} [fb]")
    twoStdDevLine.GetYaxis().SetTitle("95% CL limit on #mu")
    twoStdDevLine.SetTitle("")

    centralLine = ROOT.TGraph(points, np.array(x, dtype=np.float64), np.array(y, dtype=np.float64))
    centralLine.SetLineWidth(2)

    theoryXsLine = ROOT.TGraph(points, np.array(x, dtype=np.float64), np.array(np.ones(points), dtype=np.float64))
    theoryXsLine.SetLineWidth(2)
    theoryXsLine.SetLineStyle(2)

    # Canvas and plotting
    tex1 = ROOT.TLatex()
    tex1.SetNDC()
    tex1.SetTextSize(0.05)
    tex1.DrawLatex(0.115, 0.85, "CMS #it{#bf{Preliminary}}")

    tex3 = ROOT.TLatex()
    tex3.SetNDC()
    tex3.SetTextSize(0.04)
    tex3.DrawLatex(0.67, 0.91, "#bf{41.5 fb^{-1} (13 TeV)}")

    legend = ROOT.TLegend(0.3, 0.75, 0.88, 0.88)
    legend.SetNColumns(2)
    legend.SetBorderSize(0)
    legend.SetTextSize(0.03)
    legend.AddEntry(centralLine, "Expected (#mu)", "l")
    legend.AddEntry(theoryXsLine, "Theoretical (#mu)", "l")
    #legend.AddEntry(statOnlyLine, "Stat. Only (Cross-section)", "l")
    legend.AddEntry(oneStdDevLine, "#pm 1 std. deviation", "f")
    legend.AddEntry(twoStdDevLine, "#pm 2 std. deviation", "f")

    canvas = ROOT.TCanvas("", "", 0, 0, 600, 500)
    canvas.SetGridx()
    canvas.SetGridy()
    canvas.SetLogy()
    twoStdDevLine.Draw("a3")
    oneStdDevLine.Draw("same3l")
    centralLine.Draw("SAME")
    theoryXsLine.Draw("SAME")
    #g_stat.Draw("L SAME")
    tex1.Draw()
    tex3.Draw()
    legend.Draw()
    canvas.Update()

    # Save outputs
    fileName = f"{args.outDir}/limit_mu_decay{decayWidthList[0]}pct"
    canvas.SaveAs(f"{fileName}.png")
    canvas.SaveAs(f"{fileName}.pdf")
    canvas.SaveAs(f"{fileName}.C")
    canvas.SaveAs(f"{fileName}.root")
    print(f"Saved png, pdf, root, C: {fileName}")

    # Adjusting to cross-section
    for line in [y, y_stat, ey2l, eyl, eyh, ey2h]:
        line *= tprime_xs

def main():
    parser = argparse.ArgumentParser(description="Used to print brazilian plots of asymptotic limits", epilog ="")

# Add the arguments
    parser.add_argument("--csvFile", required=True, help="Name of the XS csv file")
    parser.add_argument("--outDir", required=True, help="Name of the output directory")
    parser.add_argument("--mH", required=True, type=float, help="Mass of Higgs using during asymptotic limit calculations")

# Parse the arguments
    args = parser.parse_args(None if sys.argv[1:] else ['--help'])
    makeBrazilPlot(args)

# Example usage
if __name__ == "__main__":
    main()
