#include <iostream>
#include <sstream>
#include "TTree.h"
#include "TH1.h"
#include "TFile.h"
#include "TNtuple.h"
#include "TLegend.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TLorentzVector.h"

#include <vector>
#include <iostream>
#include <map>
#include <algorithm>
#include <TChain.h>
#include "TMath.h"
#include "TGraphErrors.h"
#include "TGraph.h"
#include "TLatex.h"
#include "THStack.h"
#include "tdrStyle/tdrstyle.C"
#include "tdrStyle/CMS_lumi.C"

using namespace std;

void makeBrazilPlot_Comp(TString channel="", TString method="mu", TString ext=""){
gStyle->SetOptStat(0);
gROOT->SetBatch();
setTDRStyle();
const int points=10;
int mass[points]	={600,	 	625, 	650, 	675, 	700, 	800, 	900, 	1000, 	1100, 	1200};
float T_xs[points] 	={0.1764,	0.1489,	0.1213,	0.1050,	0.0886,	0.0459,	0.0251,	0.0145, 0.00867,0.00536}; //in pb

//string mass_str[point]={"600", "625", "650", "675", "700"}
TString file_path="/afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Combine/result_UL_v2/Models_Tprime";
//TString file_path="/eos/user/p/prsaha/Tprime_analysis/FinalFit_outputs/result_v13/Models_Tprime";
float lumi=138;
double x[points];
double y[points];
double y_Stat[points];
double eyl[points];
double eyh[points];
double ey2l[points];
double ey2h[points];

double exl_[points];
double exh_[points];
double ex2l_[points];
double ex2h_[points];

double eyl_[points];
double eyh_[points];
double ey2l_[points];
double ey2h_[points];

double obsl[points];
double xsBr[points];

for(int i=0; i<points; i++)
        {
	double xs_X_Br_=1;
	if(method=="xs_X_Br")  xs_X_Br_ = T_xs[i]*0.00227*1000; //in fb
	else xs_X_Br_ =1;
        string mass_str;
        stringstream ss;
        ss << mass[i];
        ss >> mass_str;
        TFile *file_ = new TFile(file_path + mass_str+ channel +"/higgsCombine" + channel + "_Syst.AsymptoticLimits.mH125.root", "READ");
        TTree* tree_ = (TTree*)file_->Get("limit");
        Int_t nentries=(Int_t)tree_->GetEntries();
//cout<<"nentries=========="<<nentries<<endl;
        Double_t qlimit;
        tree_->SetBranchAddress("limit", &qlimit);
		tree_->SetBranchStatus("*", 1);	
		x[i] = mass[i];
		xsBr[i] = xs_X_Br_;	

        for(int ievent=0; ievent <points ; ievent++)
                {
                tree_-> GetEntry( ievent );
//                x[ievent] = mass[i];
                if (ievent==0) ey2l[i] = qlimit*xs_X_Br_;// cout<<"ey2l[ievent] "<<qlimit<<endl;
                else if (ievent==1) eyl[i] = qlimit*xs_X_Br_;
                else if (ievent==2) {y[i]= qlimit*xs_X_Br_; cout<<"Tprime"<<mass[i]<<" exp =	"<<qlimit<<endl;
									}
                else if (ievent==3) eyh[i] = qlimit*xs_X_Br_;
                else if (ievent==4) ey2h[i] = qlimit*xs_X_Br_;
				else if (ievent==5) {obsl[i] = qlimit*xs_X_Br_; /*cout<<"Tprime"<<mass[i]<<" obs =   "<<qlimit<<endl;*/}
//		else	cout<<"Limit ---  "<<qlimit<<endl;    
            }
//cout<<"y[i]   "<<y[i]<<endl;

        }
//====================================================================================================
TString file_path_Stat="/afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Combine/result_UL_v2/Models_Tprime";
//TString file_path_Stat="/eos/user/p/prsaha/Tprime_analysis/FinalFit_outputs/result_v13/Models_Tprime";
for(int i=0; i<points; i++)
        {
    	double xs_X_Br_=1;
    	if(method=="xs_X_Br")  xs_X_Br_ = T_xs[i]*0.00223*1000; //in fb
    	else xs_X_Br_ =1;
        string mass_str;
        stringstream ss;
        ss << mass[i];
        ss >> mass_str;
        TFile *file_ = new TFile(file_path_Stat + mass_str+ channel +"/higgsCombine" + channel +"_StatOnly.AsymptoticLimits.mH125.root", "READ");
        TTree* tree_ = (TTree*)file_->Get("limit");
        Int_t nentries=(Int_t)tree_->GetEntries();
//cout<<"nentries=========="<<nentries<<endl;
        Double_t qlimit;
        tree_->SetBranchAddress("limit", &qlimit);
    	tree_->SetBranchStatus("*", 1);
    	x[i] = mass[i];
        for(int ievent=0; ievent <points ; ievent++)
                {
                tree_-> GetEntry( ievent );
//                x[ievent] = mass[i];
                if (ievent==2) 
					{	
						y_Stat[i]= qlimit*xs_X_Br_; 
					//	cout<<"Tprime"<<mass[i]<<" mean =   "<<qlimit<<endl;
					}
//      else    cout<<"Limit ---  "<<qlimit<<endl;
            }
//cout<<"y[i]   "<<y[i]<<endl;

        }



for(int j=0; j<points; j++)
        {
//cout<<"y[j]   "<<y[j]<<endl;
//cout<<"ey2l[j] "<<ey2l[j]<<endl;
		ex2l_[j]=0.;
		exl_[j]=0.;
		exh_[j]=0.;
		ex2h_[j]=0.;
        ey2l_[j] = y[j]-ey2l[j];
        eyl_[j] = y[j]-eyl[j];
        eyh_[j] = eyh[j]-y[j];
        ey2h_[j] = ey2h[j]-y[j];
        }

TGraphAsymmErrors* ge = new TGraphAsymmErrors(points, x, y,exl_,exh_,eyl_,eyh_);
ge->SetFillColor(kGreen);

TGraphAsymmErrors* ge2 = new TGraphAsymmErrors(points, x, y, ex2l_,ex2h_,ey2l_,ey2h_);
ge2->SetFillColor(kYellow);
ge2->GetXaxis()->SetTitle("T' mass(GeV)");

ge2->GetXaxis()->SetRangeUser(600,1200);
//ge2->GetYaxis()->SetRangeUser(0,1000);

//ge2->GetYaxis()->SetRangeUser(0, 100);
//ge2->GetYaxis()->SetRangeUser(0, 2.5);
//ge2->GetYaxis()->SetTitle("95\% CL limit on #mu");

//ge2->SetMaximum(10);
//ge2->SetMinimum(0.0);

if(method=="xs_X_Br") {
	
	ge2->SetMaximum(10);
	ge2->SetMinimum(0.01);
	ge2->GetYaxis()->SetTitle("95\% CL limit on (#sigma #times Br(H #rightarrow #gamma #gamma) in fb)");
	}
else {
	ge2->SetMaximum(2000);
	ge2->SetMinimum(0.1);
	ge2->GetYaxis()->SetTitle("#mu");
	}	
ge2->SetTitle("");
ge2->GetYaxis()->SetTitleOffset(0.85);

TGraph* g = new TGraph(points, x, y);
g->SetLineWidth(2);
g->SetLineStyle(2);

TGraph* g_Stat = new TGraph(points, x, y_Stat);
g_Stat->SetLineWidth(2);
g_Stat->SetLineStyle(2);

TGraph* g_obs = new TGraph(points, x, obsl);
g_obs->SetLineWidth(2);
g_obs->SetLineStyle(1);

TGraph* Th_line = new TGraph(points, x, xsBr);
Th_line->SetLineWidth(2);
Th_line->SetLineStyle(7);
Th_line->SetLineColor(kRed);

//        TLatex * tex1 = new TLatex(0.18, 0.89,TString("#bf{CMS} #it{Preliminary}"));
		TLatex * tex1 = new TLatex(0.18, 0.89,TString("#bf{CMS}"));
        tex1->SetNDC();
        tex1->SetTextAlign(13);
        tex1->SetTextFont(42);
        tex1->SetTextSize(0.04);
        tex1->SetLineWidth(2);

        TLatex * tex2 = new TLatex(0.75, 0.98,TString(Form("#scale[1.5]{%.0f fb^{-1} (13 TeV)}",lumi)));
        tex2->SetNDC();
        tex2->SetTextAlign(13);
        tex2->SetTextFont(42);
        tex2->SetTextSize(0.03);
        tex2->SetLineWidth(2);

/*
//Stephanie's RunII result comparison
Double_t expXsec_fx1[8] = {
   600,
   650,
   700,
   800,
   900,
   1000,
   1100,
   1200};
   Double_t expXsec_fy1[8] = {
   2.8203,
   2.4297,
   2.1797,
   2.5859,
   3.4844,
   5.0469,
   6.9062,
   11.6875};
   TGraph *graph = new TGraph(8,expXsec_fx1,expXsec_fy1);
   graph->SetName("expXsec");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineWidth(2);
   graph->SetLineColor(kRed);
*/

/*
//B2G-18-003 Observed limit(tH+tZ)
   Double_t Xsec_fx1[8] = {
   600,
//   650,
   700,
   800,
   900,
   1000,
   1100,
   1200};
   Double_t Xsec_fy1[8] = {
   38,
   5.63,
   3.01,
   5.50,
   6.30,
   11.67,
   20};

   TGraph *graph = new TGraph(7,Xsec_fx1,Xsec_fy1);
   graph->SetName("Xsec");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineWidth(2);
   graph->SetLineColor(kBlue);
*/
Double_t mu_tHtZ_x[7] = {
   600,
   700,
   800,
   900,
   1000,
   1100,
   1200};
   Double_t mu_tHtZ_y[7] = {
   10,
   5,
   5.56,
   8.44,
   8.52,
   9.44,
   12};

   TGraph *mu_tHtZ = new TGraph(7, mu_tHtZ_x, mu_tHtZ_y);
   mu_tHtZ->SetName("Xsec");
   mu_tHtZ->SetTitle("");
   mu_tHtZ->SetFillStyle(1000);
   mu_tHtZ->SetLineWidth(2);
   mu_tHtZ->SetLineColor(kBlue);



//800in MVA1
Double_t mu_tZnunu_x[7] = {
   600,
   700,
   800,
   900,
   1000,
   1100,
   1200
   };
   Double_t mu_tZnunu_y[7] = {
	6.11,
	5,
	4.5,
	4.21,
    5,
    6.88,
	6.5
	};
   TGraph *mu_tZnunu = new TGraph(7, mu_tZnunu_x, mu_tZnunu_y);
   mu_tZnunu->SetName("expXsec");
   mu_tZnunu->SetTitle("");
   mu_tZnunu->SetFillStyle(1000);
   mu_tZnunu->SetLineWidth(2);
   mu_tZnunu->SetLineColor(kRed);
//700in MVA2
Double_t mu_tHbbATLAS_x[3] = {
	1000,
	1100,
	1200};
Double_t mu_tHbbATLAS_y[3] = {
	35.38,
	9.14,
	11.76
	};
   TGraph *mu_tHbbATLAS = new TGraph(3, mu_tHbbATLAS_x, mu_tHbbATLAS_y);
   mu_tHbbATLAS->SetName("expXsec");
   mu_tHbbATLAS->SetTitle("");
   mu_tHbbATLAS->SetFillStyle(1000);
   mu_tHbbATLAS->SetLineWidth(2);
   mu_tHbbATLAS->SetLineColor(kMagenta);

Double_t mu_mva3x[3] = {
   1000,
   1100,
	1200
   };
Double_t mu_mva3y[3] = {
   5.92188,
   8.59375,
   12.6875};
   TGraph *graph_mva3 = new TGraph(3,mu_mva3x,mu_mva3y);
   graph_mva3->SetName("expXsec");
   graph_mva3->SetTitle("");
   graph_mva3->SetFillStyle(1000);
   graph_mva3->SetLineWidth(2);
   graph_mva3->SetLineColor(kMagenta);

TLegend *leg1 = new TLegend(0.2, 0.77, 0.75, 0.85, "");
TLegend *leg2 = new TLegend(0.2, 0.63, 0.45, 0.76, "");
leg1->SetNColumns(2);
//leg1->SetFillColor(0);
//leg1->SetFillStyle(0);
leg1->SetBorderSize(0);
leg1->SetTextSize(0.03);
leg2->SetBorderSize(0);
leg2->SetTextSize(0.03);

//leg1->AddEntry(g,  "Expected(H #rightarrow #gamma #gamma)(Syst)"		,"l");
//leg1->AddEntry(g,  "Expected tH(H #rightarrow #gamma #gamma)"		,"l");
//leg1->AddEntry(g_Stat,  "Expected(H #rightarrow #gamma #gamma)(StatOnly)"        ,"l");
//leg1->AddEntry(g_obs,  "Observed tH(H #rightarrow #gamma #gamma)"        ,"l");

leg1->AddEntry(g,  "Exp 95\% CL"      ,"l");
leg1->AddEntry(g_obs,  "Obs 95\% CL upper limits"        ,"l");
leg1->AddEntry(ge, "#pm1 std. deviation" ,"f");
leg1->AddEntry(ge2,"#pm2 std. deviation" ,"f");

//leg1->AddEntry(Th_line,"Theory" ,"l");

//TLegend *leg2 = new TLegend(0.1, 0.7, 0.35, 0.9, "");
leg2->AddEntry(mu_tHtZ, "Exp tH + tZ(all Had) [arXiv:1909.04721]", "l");
leg2->AddEntry(mu_tZnunu,  "Exp tZ(Z #rightarrow #nu #nu) [arXiv:2201.02227]"        ,"l");
leg2->AddEntry(mu_tHbbATLAS,  "Exp tH(H #rightarrow bb) ATLAS [arXiv:2201.07045]"        ,"l");
//leg1->AddEntry(graph_mva3,  "Expected #mu in MVA[1100,1200]"        ,"l");


TCanvas* c41 = new TCanvas("c41","c41",200,10,600,400);
c41->cd();
gPad->SetTopMargin(0.075);
gPad->SetRightMargin(0.05);
gPad->SetLeftMargin(0.15);

//c41->SetGridx();
//c41->SetGridy();
c41->SetLogy();
ge2->Draw("a3");
//ge->Draw("Same3l");
ge->Draw("CSAME 3l");
g->Draw("CSAME");
//g_Stat->Draw("SAME");
g_obs->Draw("CSAME");
//Th_line->Draw("SAME");
mu_tHtZ->Draw("CSAME");
mu_tZnunu->Draw("CSAME");
mu_tHbbATLAS->Draw("CSAME");
//graph_mva3->Draw("SAME");
c41->Update();
//c41->SetGridx();
//c41->SetGridy();
tex1->Draw();
tex2->Draw();
leg1->Draw();
leg2->Draw();

tex1->DrawLatex(0.75, 0.85, "#Gamma/m_{T'} #approx 1\%(NWA)");
//tex1->DrawLatex(0.75, 0.9, "T' #rightarrow tH(H #rightarrow #gamma #gamma) ");
//tex1->DrawLatex(0.2, 0.92, "95\% CL upper limits");

//leg2->Draw();
/*
writeExtraText = true;       // if extra text
extraText  = "       Preliminary";
lumi_13TeV = "138 fb^{-1}";
CMS_lumi( c41, 4, 0);
*/
c41->SaveAs("/eos/user/p/prsaha/www/Tprime_analysis/Finalfit_Lite_output/UL/result_v2/LimitTprime_"+ method + channel + ext + ".pdf");
c41->SaveAs("/eos/user/p/prsaha/www/Tprime_analysis/Finalfit_Lite_output/UL/result_v2/LimitTprime_"+ method + channel + ext + ".png");
c41->SaveAs("/eos/user/p/prsaha/www/Tprime_analysis/Finalfit_Lite_output/UL/result_v2/LimitTprime_"+ method + channel + ext + ".root");
c41->SaveAs("/eos/user/p/prsaha/www/Tprime_analysis/Finalfit_Lite_output/UL/result_v2/LimitTprime_"+ method + channel + ext + ".C");
}


