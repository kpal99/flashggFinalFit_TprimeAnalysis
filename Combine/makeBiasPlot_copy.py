import os, sys
import ROOT
from optparse import OptionParser
import glob
import math

def get_bias(r_fit,r,sigma_fit):
  return (r_fit-r)/sigma_fit

def get_Err_in_bias(r_fit, r, sigma_fit, dr_fit, dsigma_fit):
  a=(1/sigma_fit)*dr_fit
  b=((r_fit-r)/sigma_fit**2)*dsigma_fit
  return math.sqrt((a**2+b**2))

def draw(gr):
  gr.SetMarkerStyle(20)
  gr.SetMarkerColor(4)
  gr.SetLineColor(4)
  gr.SetLineWidth(2)
  gr.GetYaxis().SetRangeUser(-0.5, 0.5);
  gr.GetXaxis().SetTitle("Expected Signal(#hat{#mu})") 
  gr.GetYaxis().SetTitle("Bias")
  c1 = ROOT.TCanvas("bias", "bias", 600, 400);
  c1.cd()
  c1.SetGridx()
  c1.SetGridy()
  gr.Draw("APL")
  c1.SaveAs("/eos/user/p/prsaha/www/Tprime_analysis/Finalfit_Lite_output/bias_Study/bias_forM1200.png")
  c1.SaveAs("/eos/user/p/prsaha/www/Tprime_analysis/Finalfit_Lite_output/bias_Study/bias_forM1200.pdf")

def get_options():
  parser = OptionParser()
  parser.add_option("--inputFileDir", dest="inputFileDir", default="/afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Combine/Models_Tprime1200/toys", help="Input file dir")
  parser.add_option("--ext", dest="ext", default='', help="Extension for saving")
  parser.add_option("--maxExpectSignal", dest="maxExpectSignal", type='int', default=10, help="highest expectSignal parameter to generate toys for bias test")
  return parser.parse_args()
(opt,args) = get_options()

bias_gr = ROOT.TGraphErrors();

ROOT.gStyle.SetOptStat(0);
ROOT.gROOT.SetBatch();

for ExpSig in range(1,opt.maxExpectSignal+1):
   inputFile= "%s/higgsCombine_expSignal_%s_1000toysForBias_step.MultiDimFit.mH125.123456.root"%(opt.inputFileDir,ExpSig)
   f = ROOT.TFile(inputFile)
   tree = f.Get("limit")
   x_min, x_max = ExpSig-100, ExpSig+100
#   h_r =ROOT.TH1D("h_r","h_r;#hat{#mu};n_Toys",100,x_min,x_max)
   tree.Draw("r>>h_r_","","hist")
   h_r = ROOT.gDirectory.Get("h_r_");
#  h_r.Draw()
   print h_r.GetStdDev()
   print h_r.GetMean()

   g1 = ROOT.TF1("g1","gaus", h_r.GetMean(), h_r.GetStdDev())
   h_r.Fit("g1", "M")
   print "MEAN--->Hist: %0.3f Fit: %0.3f +- %0.4f"%(h_r.GetMean(), g1.GetParameter(1), g1.GetParError(1))
   print "SIGMA-->Hist: %0.3f Fit: %0.3f +- %0.4f"%(h_r.GetStdDev(), g1.GetParameter(2), g1.GetParError(2))

   tex1 = ROOT.TLatex();
   tex1.SetTextFont(42);
   tex1.SetTextAlign(11);
   tex1.SetNDC();
   tex1.SetTextSize(0.06);

   c2 = ROOT.TCanvas("bias", "bias", 400, 400);
   c2.cd()
   c2.SetGridx()
#   c2.SetGridy()   
   h_r.Draw()
   tex1.DrawLatex(0.15, 0.80, "#scale[0.6]{Mean: %0.3f}"%(g1.GetParameter(1)))
   tex1.DrawLatex(0.15, 0.75, "#scale[0.6]{Sigma: %0.3f}"%(g1.GetParameter(2)))
#   tex1.DrawLatex(0.15, 0.75, "#scale[0.75]{"Mean %0.3f"}"%(g1.GetParameter(2)))

   c2.SaveAs("/eos/user/p/prsaha/www/Tprime_analysis/Finalfit_Lite_output/bias_Study/pullMu_M1200r_%g.pdf"%(ExpSig))
   c2.SaveAs("/eos/user/p/prsaha/www/Tprime_analysis/Finalfit_Lite_output/bias_Study/pullMu_M1200r_%g.png"%(ExpSig))
   
   print get_bias(h_r.GetMean(), ExpSig, h_r.GetStdDev())   
   bias = get_bias(g1.GetParameter(1), ExpSig, g1.GetParameter(2))
   bias_Err = get_Err_in_bias(g1.GetParameter(1), ExpSig, g1.GetParameter(2), g1.GetParError(1), g1.GetParError(2) )  
   bias_gr.SetPoint(ExpSig-1, ExpSig, bias)
   bias_gr.SetPointError(ExpSig-1, 0, bias_Err)
  
draw(bias_gr) 
