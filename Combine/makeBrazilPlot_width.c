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

void makeBrazilPlot_width(TString channel="", TString method="width", TString ext=""){
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
ge2->GetXaxis()->SetTitle("M_{T'} (GeV)");
ge2->GetXaxis()->SetRangeUser(600,1200);
//ge2->GetYaxis()->SetRangeUser(0,1000);

//ge2->GetYaxis()->SetRangeUser(0, 100);
//ge2->GetYaxis()->SetRangeUser(0, 2.5);
//ge2->GetYaxis()->SetTitle("95\% CL limit on #mu");

//ge2->SetMaximum(10);
//ge2->SetMinimum(0.0);

if(method=="xs_X_Br") {
	
	ge2->SetMaximum(100);
	ge2->SetMinimum(0.01);
//	ge2->GetYaxis()->SetTitle("95\% CL limit on (#sigma #times Br(H #rightarrow #gamma #gamma) in fb)");
	ge2->GetYaxis()->SetTitle("#sigma_{T'bq(T'#rightarrow tH)} #it{B}_{H #rightarrow #gamma #gamma} (fb)");
	}
else {
	ge2->SetMaximum(200);
	ge2->SetMinimum(0.1);
	ge2->GetYaxis()->SetTitle("#Gamma/M_{T'} (%)");
	}	
ge2->SetTitle("");
ge2->GetYaxis()->SetTitleOffset(0.85);

//////////Adjusted to draw shaded region===============================
double m = ge2->GetMaximum();
Double_t ey3h_[10]={m,m,m,m,m,m,m,m,m,m};
//TGraphAsymmErrors* ge2 = new TGraphAsymmErrors(points, x, y, ex2l_,ex2h_,ey2l_,ey2h_);
TGraphAsymmErrors* ge3 = new TGraphAsymmErrors(points, x, ey2h, ex2l_,ex2h_,ex2l_,ey3h_);
ge3->SetFillColorAlpha(kBlack, 0.15);
ge3->SetLineWidth(0);
//=====================================================================

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

//        TLatex * tex1 = new TLatex(0.18, 0.89, TString("#bf{CMS} #it{Preliminary}"));
		TLatex * tex1 = new TLatex(0.18, 0.89, TString("#bf{CMS}"));		
        tex1->SetNDC();
        tex1->SetTextAlign(13);
        tex1->SetTextFont(42);
        tex1->SetTextSize(0.04);
        tex1->SetLineWidth(2);

        TLatex * tex2 = new TLatex(0.75, 0.98, TString(Form("#scale[1.5]{%.0f fb^{-1} (13 TeV)}",lumi)));
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

Double_t MQ_fx1[10] = {
   600,
   625,
   650,
   675,
   700,
   800,
   900,
   1000,
   1100,
   1200};
   Double_t Had_RecoWidth_fy1[10] = {
	7.15,
	6.96,
	6.67,
	6.46,
	6.33,
	6.06,
	5.59,
	5.35,
	5.62,
	5.43};
   TGraph *Had_RecoWidth = new TGraph(10, MQ_fx1, Had_RecoWidth_fy1);
   Had_RecoWidth->SetName("Xsec");
   Had_RecoWidth->SetTitle("");
   Had_RecoWidth->SetFillStyle(1000);
   Had_RecoWidth->SetLineWidth(2);
   Had_RecoWidth->SetLineColor(kBlue);

   Double_t Lep_RecoWidth_fy1[10] = {
	6.64,
	6.64,
	6.40,
	6.26,
	6.08,
	5.69,
	5.15,
	4.81,
	4.45,
	4.16};
   TGraph *Lep_RecoWidth = new TGraph(10, MQ_fx1, Lep_RecoWidth_fy1);
   Lep_RecoWidth->SetName("Xsec");
   Lep_RecoWidth->SetTitle("");
   Lep_RecoWidth->SetFillStyle(1000);
   Lep_RecoWidth->SetLineWidth(2);
   Lep_RecoWidth->SetLineColor(kMagenta);

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
	1.19141,
	1.21484,
	1.33203,
	1.46094,
    1.67969,
    5.26562};
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
   	2.52344,
   	2.67188,
	3.65625,
	5.78125,
	11.6875
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
   5.92188,
   8.59375,
   12.6875};
   TGraph *graph_mva3 = new TGraph(3,mu_mva3x,mu_mva3y);
   graph_mva3->SetName("expXsec");
   graph_mva3->SetTitle("");
   graph_mva3->SetFillStyle(1000);
   graph_mva3->SetLineWidth(2);
   graph_mva3->SetLineColor(kMagenta);

TLegend *leg1 = new TLegend(0.2, 0.67, 0.75, 0.84, "");
leg1->SetNColumns(2);
//leg1->SetFillColor(0);
leg1->SetFillStyle(0);
leg1->SetBorderSize(0);
leg1->SetTextSize(0.03);

leg1->AddEntry(g,  "#scale[1.1]{Exp 95\% CL}"      ,"l");
//leg1->AddEntry(g_Stat,  "Expected(H #rightarrow #gamma #gamma)(StatOnly)"        ,"l");
leg1->AddEntry(g_obs,  "#scale[1.1]{Obs 95\% CL upper limits}"        ,"l");
//leg1->AddEntry(graph, "Expected(H #rightarrow bb)", "l");
leg1->AddEntry(ge, "#scale[1.1]{#pm1 std. deviation}" ,"f");
leg1->AddEntry(ge2,"#scale[1.1]{#pm2 std. deviation}" ,"f");
leg1->AddEntry(Th_line,"#scale[1.1]{Generated MC}" ,"l");
//leg1->AddEntry(Had_RecoWidth, "#scale[1.1]{Reco. M_{T'} in Had. chn.}", "l");
//leg1->AddEntry(Lep_RecoWidth, "#scale[1.1]{Reco. M_{T'} in Lep. chn.}", "l");

//TLegend *leg2 = new TLegend(0.1, 0.7, 0.35, 0.9, "");
//leg1->AddEntry(graph_mva1,  "Expected #mu in MVA[600,700]"        ,"l");
//leg1->AddEntry(graph_mva2,  "Expected #mu in MVA[800,1000]"        ,"l");
//leg1->AddEntry(graph_mva3,  "Expected #mu in MVA[1100,1200]"        ,"l");


TCanvas* c41 = new TCanvas("c41","c41",200,10,600,400);
c41->cd();
//gPad->SetBottomMargin(0.1);
gPad->SetTopMargin(0.075);
gPad->SetRightMargin(0.05);
//c41->SetGridx();
//c41->SetGridy();
c41->SetLogy();
ge2->SetFillColor(kYellow);
ge2->Draw("a3");
//ge->Draw("Same3l");
ge->SetFillColor(kGreen);
ge->Draw("CSAME 3l");
ge3->Draw("CSAME 3l");
g->Draw("CSAME");
//g_Stat->Draw("SAME");
//Lep_RecoWidth->Draw("CSAME");
//Had_RecoWidth->Draw("CSAME");
g_obs->Draw("CSAME");
Th_line->Draw("CSAME");
//graph_mva1->Draw("SAME");
//graph_mva2->Draw("SAME");
//graph_mva3->Draw("SAME");
//ge2->GetYaxis()->SetTickLength(0.02);
//c41->SetTicky();
//c41->Update();
//c41->SetGridx();
//c41->SetGridy();
tex1->Draw();
tex2->Draw();
leg1->Draw();
tex1->DrawLatex(0.75, 0.83, "#scale[0.9]{#Gamma/m_{T'} = 1\% (NWA)}");
tex1->DrawLatex(0.75, 0.88, "#scale[0.9]{T' #rightarrow tH(H #rightarrow #gamma #gamma)}");
//gPad->Modified();
//c41->Update();
//tex1->DrawLatex(0.2, 0.92, "95\% CL upper limits");
//leg2->Draw();
//setTDRStyle();
gPad->RedrawAxis();
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


