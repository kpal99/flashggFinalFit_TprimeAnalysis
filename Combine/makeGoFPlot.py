import os, sys
import ROOT
from optparse import OptionParser
import glob
import math
#RDataFrame = ROOT.RDF.Experimental.Distributed.Spark.RDataFrame

def get_options():
  parser = OptionParser()
  parser.add_option("--inputFileDir", dest="inputFileDir", default="/afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Combine/Models_HiggsCR", help="Input file dir")
  parser.add_option("--inputFiletoysFit", dest="inputFiletoysFit", default="/afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Combine/Models_HiggsCR/higgsCombineTest_500toys_StatOnly.GoodnessOfFit.mH125.123456.root", help="Input file dir") 
  parser.add_option("--inputFileDataFit", dest="inputFileDataFit", default="/afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Combine/Models_HiggsCR/higgsCombineTest_500toys_StatOnly.GoodnessOfFit.mH125.123456.root", help="Input file dir")
  parser.add_option("--ext", dest="ext", default='', help="Extension for saving")
  return parser.parse_args()
(opt,args) = get_options()

bias_gr = ROOT.TGraphErrors()
bias_2_gr = ROOT.TGraphErrors()

ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch()

#inputFile= "%s/higgsCombineTest_500toys_StatOnly.GoodnessOfFit.mH125.123456.root"%(opt.inputFileDir)
f = ROOT.TFile("%s"%(opt.inputFiletoysFit))
tree = f.Get("limit")
h_GoF_ =ROOT.TH1D("h_GoF_","",50,250,500)
#   tree.Draw("(r-%i)/(0.5*(rHiErr+rLoErr))>>h_GoF_"%(ExpSig),"","hist")
tree.Draw("limit>>h_GoF_","","E")
h_GoF = ROOT.gDirectory.Get("h_GoF_")
h_GoF.GetXaxis().SetTitle("Best fit test statistic")
h_GoF.GetYaxis().SetTitle("n_toys")


f1 = ROOT.TFile("%s"%(opt.inputFileDataFit))
tree1 = f1.Get("limit")

#qlimit=0
#tree1.SetBranchStatus("*", 1);
#tree1.SetBranchAddress("limit", qlimit);

nentries = tree1.GetEntries();
data_GoF = 0
for i in range(0,nentries):
   tree1.GetEntry(i)  
   tree1.limit
   data_GoF += tree1.limit   
#df = ROOT.RDataFrame(tree1)

#print df
#data_GoF = df.Sum("limit").GetValue()

data_GoF_bin = h_GoF.FindBin(data_GoF) 
print data_GoF_bin
print h_GoF.Integral(data_GoF_bin, h_GoF.GetNbinsX())
print h_GoF.Integral()
print h_GoF.GetStdDev()
print h_GoF.GetMean()

p_value = h_GoF.Integral(data_GoF_bin, h_GoF.GetNbinsX())/h_GoF.Integral()

g1 = ROOT.TF1("g1","gaus", h_GoF.GetMean(), h_GoF.GetStdDev())
h_GoF.Fit("g1", "M")
print "MEAN--->Hist: %0.3f Fit: %0.3f +- %0.4f"%(h_GoF.GetMean(), g1.GetParameter(1), g1.GetParError(1))
print "SIGMA-->Hist: %0.3f Fit: %0.3f +- %0.4f"%(h_GoF.GetStdDev(), g1.GetParameter(2), g1.GetParError(2))

tex1 = ROOT.TLatex()
tex1.SetTextFont(42)
tex1.SetTextAlign(11)
tex1.SetNDC()
tex1.SetTextSize(0.06)

ar1 = ROOT.TArrow(data_GoF, 0, data_GoF, 10, 0.05, "|>")
#ar1.SetAngle(40)
ar1.SetLineWidth(3)
ar1.SetLineColor(3)

leg1 = ROOT.TLegend(0.15, 0.75, 0.35, 0.80, "")
leg1.AddEntry(h_GoF, "toy data" ,"l");
leg1.AddEntry(ar1, "Observed = %0.2f"%(data_GoF),"l");


c2 = ROOT.TCanvas("bias", "bias", 400, 400)
c2.cd()
c2.SetGridx()
#   c2.SetGridy()   
h_GoF.SetTitle("")
h_GoF.Draw("ep")
ar1.Draw("SAME")
leg1.Draw()
tex1.DrawLatex(0.65, 0.80, "#scale[0.4]{Mean: %0.2f}"%(g1.GetParameter(1)))
tex1.DrawLatex(0.65, 0.75, "#scale[0.4]{Sigma: %0.2f}"%(g1.GetParameter(2)))
tex1.DrawLatex(0.15, 0.70, "#scale[0.4]{p-value: %0.2f}"%(p_value))
tex1.DrawLatex(0.65, 0.85, "#scale[0.5]{#bf{%s}}"%(opt.ext))

c2.SaveAs("/eos/user/p/prsaha/www/Tprime_analysis/Finalfit_Lite_output/UL/result_v2_CR1/GoF_sb_%s.pdf"%(opt.ext))
c2.SaveAs("/eos/user/p/prsaha/www/Tprime_analysis/Finalfit_Lite_output/UL/result_v2_CR1/GoF_sb_%s.png"%(opt.ext))

