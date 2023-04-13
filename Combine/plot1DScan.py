#!/usr/bin/env python
import ROOT
import math
from functools import partial
import CombineHarvester.CombineTools.plotting as plot
import json
import argparse
import os.path

ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gROOT.SetBatch(ROOT.kTRUE)

plot.ModTDRStyle(width=700, l=0.13)
ROOT.gStyle.SetNdivisions(510, "XYZ")
ROOT.gStyle.SetMarkerSize(0.7)

NAMECOUNTER = 0

def read(scan, param, files, ycut):
    goodfiles = [f for f in files if plot.TFileIsGood(f)]
    limit = plot.MakeTChain(goodfiles, 'limit')
    graph = plot.TGraphFromTree(limit, param, '(2*(deltaNLL+nll+nll0))', 'quantileExpected > -1.5')
    graph.SetName(scan)
    graph.Sort()
    plot.RemoveGraphXDuplicates(graph)
    plot.RemoveGraphYAbove(graph, ycut)
    # graph.Print()
    return graph


def Eval(obj, x, params):
    return obj.Eval(x[0])


def BuildScan(scan, param, files, color, ycut):
    graph = read(scan, param, files, ycut)
    graph.SetMarkerColor(color)
    spline = ROOT.TSpline3("spline3", graph)
    global NAMECOUNTER
    func = ROOT.TF1('splinefn'+str(NAMECOUNTER), partial(Eval, spline), graph.GetX()[0], graph.GetX()[graph.GetN() - 1], 1)
    NAMECOUNTER += 1
    func.SetLineColor(color)
    func.SetLineWidth(3)
    return {
        "graph"     : graph,
        "func"      : func
    }

parser = argparse.ArgumentParser()

parser.add_argument('main', help='Main input file for the scan')
parser.add_argument('--y-cut', type=float, default=7., help='Remove points with y > y-cut')
parser.add_argument('--y-max', type=float, default=8., help='y-axis maximum')
parser.add_argument('--output', '-o', help='output name without file extension', default='scan')
parser.add_argument('--POI', help='use this parameter of interest', default='r')
parser.add_argument('--translate', default=None, help='json file with POI name translation')
parser.add_argument('--main-label', default='Observed', type=str, help='legend label for the main scan')
parser.add_argument('--main-color', default=1, type=int, help='line and marker color for main scan')
parser.add_argument('--others', nargs='*', help='add secondary scans processed as main: FILE:LABEL:COLOR')
parser.add_argument('--breakdown', help='do quadratic error subtraction using --others')
parser.add_argument('--logo', default='CMS')
parser.add_argument('--logo-sub', default='Internal')
args = parser.parse_args()

print '--------------------------------------'
print  args.output
print '--------------------------------------'

fixed_name = args.POI
if args.translate is not None:
    with open(args.translate) as jsonfile:
        name_translate = json.load(jsonfile)
    if args.POI in name_translate:
        fixed_name = name_translate[args.POI]

yvals = [1., 4.]


main_scan = BuildScan(args.output, args.POI, [args.main], args.main_color, args.y_cut)

other_scans = [ ]
other_scans_opts = [ ]
if args.others is not None:
    for oargs in args.others:
        splitargs = oargs.split(':')
        other_scans_opts.append(splitargs)
        other_scans.append(BuildScan(args.output, args.POI, [splitargs[0]], int(splitargs[2]), args.y_cut))


canv = ROOT.TCanvas(args.output, args.output)
pads = plot.OnePad()
main_scan['graph'].SetMarkerColor(1)
main_scan['graph'].Draw('AP')

axishist = plot.GetAxisHist(pads[0])

axishist.SetMaximum(args.y_max)
axishist.SetMinimum(186)

#axishist.GetYaxis().SetTitle("2 (#Delta ln L + nll + nll0)")
axishist.GetYaxis().SetTitle("2 (deltaNLL + nll + nll0)")
axishist.GetXaxis().SetTitle("%s" % fixed_name)

new_min = axishist.GetXaxis().GetXmin()
new_max = axishist.GetXaxis().GetXmax()
mins = []
maxs = []
for other in other_scans:
    print (other['graph'].GetN())
    mins.append(other['graph'].GetX()[0])
    maxs.append(other['graph'].GetX()[other['graph'].GetN()-1])

if len(other_scans) > 0:
    if min(mins) < main_scan['graph'].GetX()[0]:
        new_min = min(mins) - (main_scan['graph'].GetX()[0] - new_min)
    if max(maxs) > main_scan['graph'].GetX()[main_scan['graph'].GetN()-1]:
        new_max = max(maxs) + (new_max - main_scan['graph'].GetX()[main_scan['graph'].GetN()-1])
    axishist.GetXaxis().SetLimits(new_min, new_max)

for other in other_scans:
    if args.breakdown is not None:
        other['graph'].SetMarkerSize(0.4)
    other['graph'].Draw('PSAME')

line = ROOT.TLine()
line.SetLineColor(16)
# line.SetLineStyle(7)

main_scan['func'].Draw('same')
for other in other_scans:
    if args.breakdown is not None:
        other['func'].SetLineStyle(2)
        other['func'].SetLineWidth(2)
    other['func'].Draw('SAME')



box = ROOT.TBox(axishist.GetXaxis().GetXmin(), 0.625*args.y_max, axishist.GetXaxis().GetXmax(), args.y_max)
#box.Draw()
pads[0].GetFrame().Draw()
pads[0].RedrawAxis()


#ps textfit = '%s = %.3f{}^{#plus %.3f}_{#minus %.3f}' % (fixed_name, val_nom[0], val_nom[1], abs(val_nom[2]))


pt = ROOT.TPaveText(0.59, 0.82 - len(other_scans)*0.08, 0.95, 0.91, 'NDCNB')
#ps pt.AddText(textfit)

if args.breakdown is None:
    for i, other in enumerate(other_scans):
#ps        textfit = '#color[%s]{%s = %.3f{}^{#plus %.3f}_{#minus %.3f}}' % (other_scans_opts[i][2], fixed_name, other['val'][0], other['val'][1], abs(other['val'][2]))
#ps        pt.AddText(textfit)
        print ("Temp soln")

if args.breakdown is not None:
    pt.SetX1(0.50)
    if len(other_scans) >= 3:
        pt.SetX1(0.19)
        pt.SetX2(0.88)
        pt.SetY1(0.66)
        pt.SetY2(0.82)
    breakdown = args.breakdown.split(',')
    v_hi = [val_nom[1]]
    v_lo = [val_nom[2]]
    for other in other_scans:
        v_hi.append(other['val'][1])
        v_lo.append(other['val'][2])
    assert(len(v_hi) == len(breakdown))
    textfit = '%s = %.3f' % (fixed_name, val_nom[0])
    for i, br in enumerate(breakdown):
        if i < (len(breakdown) - 1):
            if (abs(v_hi[i+1]) > abs(v_hi[i])):
                print 'ERROR SUBTRACTION IS NEGATIVE FOR %s HI' % br
                hi = 0.
            else:
                hi = math.sqrt(v_hi[i]*v_hi[i] - v_hi[i+1]*v_hi[i+1])
            if (abs(v_lo[i+1]) > abs(v_lo[i])):
                print 'ERROR SUBTRACTION IS NEGATIVE FOR %s LO' % br
                lo = 0.
            else:
                lo = math.sqrt(v_lo[i]*v_lo[i] - v_lo[i+1]*v_lo[i+1])
        else:
            hi = v_hi[i]
            lo = v_lo[i]
        textfit += '{}^{#plus %.3f}_{#minus %.3f}(%s)' % (hi, abs(lo), br)
    pt.AddText(textfit)


pt.SetTextAlign(11)
pt.SetTextFont(42)
pt.SetFillStyle(0)
#pt.Draw()

plot.DrawCMSLogo(pads[0], args.logo, args.logo_sub, 11, 0.045, 0.035, 1.2,  cmsTextSize = 1.)

legend_l = 0.69
if len(other_scans) > 0:
    legend_l = legend_l - len(other_scans) * 0.04
legend = ROOT.TLegend(0.15, legend_l, 0.45, 0.78, '', 'NBNDC')
if len(other_scans) >= 3:
#        legend = ROOT.TLegend(0.46, 0.83, 0.95, 0.93, '', 'NBNDC')
        legend = ROOT.TLegend(0.15, 0.60, 0.60, 0.80, '', 'NBNDC')
        legend.SetNColumns(2)

legend.AddEntry(main_scan['func'], args.main_label, 'L')
for i, other in enumerate(other_scans):
    legend.AddEntry(other['func'], other_scans_opts[i][1], 'L')
legend.SetFillStyle(0)
legend.Draw()


save_graph = main_scan['graph'].Clone()
#save_graph.GetXaxis().SetTitle('%s = %.3f %+.3f/%+.3f' % (fixed_name, val_nom[0], val_nom[2], val_nom[1]))
outfile = ROOT.TFile(args.output+'.root', 'RECREATE')
outfile.WriteTObject(save_graph)
outfile.Close()
canv.Print('.pdf')
canv.Print('.png')
canv.SaveAs("/eos/user/p/prsaha/www/Tprime_analysis/Finalfit_Lite_output/Combine_TroubleShoot/"+args.output+".png")
canv.SaveAs("/eos/user/p/prsaha/www/Tprime_analysis/Finalfit_Lite_output/Combine_TroubleShoot/"+args.output+".pdf")
