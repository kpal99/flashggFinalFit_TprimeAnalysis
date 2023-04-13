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

using namespace std;

void makeBrazilPlot(TString channel="", TString method="mu", TString ext=""){
gStyle->SetOptStat(0);
gROOT->SetBatch();
const int points=10;
int mass[points]	={600,	 	625, 	650, 	675, 	700, 	800, 	900, 	1000, 	1100, 	1200};
float T_xs[points] 	={0.1764,	0.1489,	0.1213,	0.1050,	0.0886,	0.0459,	0.0251,	0.0145, 0.00867,0.00536};
/*
   float Tprime600_xs= 0.1764;
   float Tprime625_xs= 0.1489;
   float Tprime650_xs= 0.1213;
   float Tprime675_xs= 0.1050;
   float Tprime700_xs= 0.0886;
   float Tprime800_xs= 0.0459;
   float Tprime900_xs= 0.0251;
   float Tprime1000_xs= 0.0145;
   float Tprime1100_xs= 0.00867;
   float Tprime1200_xs= 0.00536;
*/
//string mass_str[point]={"600", "625", "650", "675", "700"}
TString file_path="/afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Combine/Models_Tprime";
float lumi=137;
double x[points];
double y[points];
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

for(int i=0; i<points; i++)
        {
	double xs_X_Br_=1;
	if(method=="xs_X_Br")  xs_X_Br_ = T_xs[i]*1000*0.00223; //in fb
	else xs_X_Br_ =1;
        string mass_str;
        stringstream ss;
        ss << mass[i];
        ss >> mass_str;
        TFile *file_ = new TFile(file_path + mass_str+ channel +"/higgsCombine_StatOnly.AsymptoticLimits.mH125.root", "READ");
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
                if (ievent==0) ey2l[i] = qlimit*xs_X_Br_;// cout<<"ey2l[ievent] "<<qlimit<<endl;
                else if (ievent==1) eyl[i] = qlimit*xs_X_Br_;
                else if (ievent==2) {y[i]= qlimit*xs_X_Br_; cout<<"Tprime"<<mass[i]<<" mean	=	"<<qlimit<<endl;}
                else if (ievent==3) eyh[i] = qlimit*xs_X_Br_;
                else if (ievent==4) ey2h[i] = qlimit*xs_X_Br_;
				else if (ievent==5) {obsl[i] = qlimit*xs_X_Br_;}
//		else	cout<<"Limit ---  "<<qlimit<<endl;    
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
//ge2->GetYaxis()->SetRangeUser(0, 37);
ge2->GetYaxis()->SetRangeUser(0, 60);
//ge2->GetYaxis()->SetTitle("95\% CL limit on #mu");
if(method=="xs_X_Br") ge2->GetYaxis()->SetTitle("95\% CL limit on (#sigma #times Br(H #rightarrow #gamma #gamma) in fb)");
else ge2->GetYaxis()->SetTitle("95\% CL limit on #mu");
ge2->SetTitle("");
TGraph* g = new TGraph(points, x, y);
g->SetLineWidth(2);

TGraph* g_obs = new TGraph(points, x, obsl);
g_obs->SetLineWidth(2);
g_obs->SetLineStyle(2);

        TLatex * tex1 = new TLatex(0.10, 0.95,TString("#bf{CMS} #it{work in progress}"));
        tex1->SetNDC();
        tex1->SetTextAlign(13);
        tex1->SetTextFont(42);
        tex1->SetTextSize(0.04);
        tex1->SetLineWidth(2);

        TLatex * tex2 = new TLatex(0.63, 0.95,TString(Form("%.1f fb^{-1} (13 TeV)",lumi)));
        tex2->SetNDC();
        tex2->SetTextAlign(13);
        tex2->SetTextFont(42);
        tex2->SetTextSize(0.03);
        tex2->SetLineWidth(2);


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

//800in MVA1
Double_t mu_mva1x[6] = {
   600,
   625,
   650,
   675,
   700,
   800
   };
   Double_t mu_mva1y[6] = {
	1.66406,
	1.64062,
	1.77344,
	1.96094,
   2.1797,
   3.8125};
   TGraph *graph_mva1 = new TGraph(6,mu_mva1x,mu_mva1y);
   graph_mva1->SetName("expXsec");
   graph_mva1->SetTitle("");
   graph_mva1->SetFillStyle(1000);
   graph_mva1->SetLineWidth(2);
   graph_mva1->SetLineColor(kRed);
//700in MVA2
Double_t mu_mva2x[5] = {
   	700,
   	800,
	900,
	1000,
	1100};
Double_t mu_mva2y[5] = {
   	2.1328,
   	3.3438,
	4.65625,
	7.21875,
	11.9375
	};
   TGraph *graph_mva2 = new TGraph(5,mu_mva2x,mu_mva2y);
   graph_mva2->SetName("expXsec");
   graph_mva2->SetTitle("");
   graph_mva2->SetFillStyle(1000);
   graph_mva2->SetLineWidth(2);
   graph_mva2->SetLineColor(kBlue);

Double_t mu_mva3x[3] = {
   1000,
   1100,
	1200
   };
Double_t mu_mva3y[3] = {
   7.5000,
   10.9688,
   16.1875};
   TGraph *graph_mva3 = new TGraph(3,mu_mva3x,mu_mva3y);
   graph_mva3->SetName("expXsec");
   graph_mva3->SetTitle("");
   graph_mva3->SetFillStyle(1000);
   graph_mva3->SetLineWidth(2);
   graph_mva3->SetLineColor(kMagenta);

TLegend *leg1 = new TLegend(0.12, 0.75, 0.7, 0.88, "");
leg1->SetNColumns(2);
//leg1->SetFillColor(0);
//leg1->SetFillStyle(0);
leg1->SetBorderSize(0);
leg1->SetTextSize(0.03);

leg1->AddEntry(g,  "Expected(H #rightarrow #gamma #gamma)"		,"l");
//leg1->AddEntry(graph, "Expected(H #rightarrow bb)", "l");
leg1->AddEntry(ge, "#pm1 std. deviation" ,"f");
leg1->AddEntry(ge2,"#pm2 std. deviation" ,"f");

//TLegend *leg2 = new TLegend(0.1, 0.7, 0.35, 0.9, "");
//leg1->AddEntry(graph_mva1,  "Expected #mu in MVA[600,700]"        ,"l");
//leg1->AddEntry(graph_mva2,  "Expected #mu in MVA[800,1000]"        ,"l");
//leg1->AddEntry(graph_mva3,  "Expected #mu in MVA[1100,1200]"        ,"l");


TCanvas* c41 = new TCanvas("c41","c41",200,10,600,400);
c41->cd();
c41->SetGridx();
c41->SetGridy();
ge2->Draw("a3");
ge->Draw("Same3l");
g->Draw("SAME");
//g_obs->Draw("SAME");
//graph_mva1->Draw("SAME");
//graph_mva2->Draw("SAME");
//graph_mva3->Draw("SAME");
c41->Update();
//c41->SetGridx();
//c41->SetGridy();
tex1->Draw();
tex2->Draw();
leg1->Draw();
//leg2->Draw();

c41->SaveAs("/eos/user/p/prsaha/www/Tprime_analysis/Finalfit_Lite_output/result_v9/LimitTprime_StatOnly"+ method + channel + "_" + ext + ".pdf");
c41->SaveAs("/eos/user/p/prsaha/www/Tprime_analysis/Finalfit_Lite_output/result_v9/LimitTprime_StatOnly"+ method + channel + "_" + ext + ".png");
c41->SaveAs("/eos/user/p/prsaha/www/Tprime_analysis/Finalfit_Lite_output/result_v9/LimitTprime_StatOnly"+ method + channel + "_" + ext + ".root");
}


