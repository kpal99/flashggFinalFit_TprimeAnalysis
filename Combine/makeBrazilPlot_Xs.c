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

void makeBrazilPlot_Xs(TString channel="", TString method="mu", TString ext=""){
gStyle->SetOptStat(0);
gROOT->SetBatch();
setTDRStyle();
const int points=10;
int mass[points]	={600,	 	625, 	650, 	675, 	700, 	800, 	900, 	1000, 	1100, 	1200};
float T_xs[points] 	={0.1764,	0.1489,	0.1213,	0.1050,	0.0886,	0.0459,	0.0251,	0.0145, 0.00867,0.00536}; //in pb

TString file_path="/afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Combine/result_UL_v2/Models_Tprime";
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
	double xs_=1;
//	if(method=="xs")  xs_ = T_xs[i]*0.00227*1000; //in fb
	if(method=="xs")  xs_ = T_xs[i]*1000; //in fb
	else xs_ =1;
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
		xsBr[i] = xs_;	

        for(int ievent=0; ievent <points ; ievent++)
                {
                tree_-> GetEntry( ievent );
                if (ievent==0) ey2l[i] = qlimit*xs_;// cout<<"ey2l[ievent] "<<qlimit<<endl;
                else if (ievent==1) eyl[i] = qlimit*xs_;
                else if (ievent==2) {y[i]= qlimit*xs_; //cout<<"Tprime"<<mass[i]<<" exp =	"<<qlimit<<endl;
									}
                else if (ievent==3) eyh[i] = qlimit*xs_;
                else if (ievent==4) ey2h[i] = qlimit*xs_;
				else if (ievent==5) {obsl[i] = qlimit*xs_; /*cout<<"Tprime"<<mass[i]<<" obs =   "<<qlimit<<endl;*/}
            }
cout<<"T' mass "<<x[i]<<"\t"<<y[i]<<endl;
        }
//====================================================================================================
TString file_path_Stat="/afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Combine/result_UL_v2/Models_Tprime";
for(int i=0; i<points; i++)
        {
    	double xs_=1;
    	if(method=="xs")  xs_ = T_xs[i]*0.00223*1000; //in fb
    	else xs_ =1;
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
                if (ievent==2) 
					{	
						y_Stat[i]= qlimit*xs_; 
					}
            }

        }

for(int j=0; j<points; j++)
        {
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

//ge2->SetMaximum(10);
//ge2->SetMinimum(0.0);

if(method=="xs") {
	ge2->SetMaximum(2000);
	ge2->SetMinimum(4);
//	ge2->GetYaxis()->SetTitle("#sigma_{T'bq(T'#rightarrow tH)} #it{B}_{H #rightarrow #gamma #gamma} (fb)");
//	ge2->GetYaxis()->SetTitle("#sigma_{T'bq(T'#rightarrow tH)} (fb)");
	ge2->GetYaxis()->SetTitle("#sigma_{T'bq} #it{B}_{T'#rightarrow tH} (fb)");

	if(channel=="_Lep"){
    ge2->SetMaximum(10000);
    ge2->SetMinimum(4);
    ge2->GetYaxis()->SetTitle("#sigma_{T'bq(T'#rightarrow tH)} (fb)");
    }
	}

else {
	ge2->SetMaximum(200);
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
//Th_line->SetLineStyle(7);
Th_line->SetLineColor(kRed);
//=========================================================================================================
//ifstream myfile1;
//myfile1.open("/afs/cern.ch/work/p/prsaha/public/plotting_macro/CMSSW_9_4_9/src/Tprime/kT_Vs_Xs.txt");
const int n_kT=7;
const int n_mPts=8;
double kappaT[n_kT]={0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35};
TGraph* Th_kTVsXs[n_kT];
TMultiGraph *mg = new TMultiGraph();
//double MQ_, kT, xs;
//string line, l1, l1_;
//int j=0;
double x_[8], y_[8];
for(int i=0; i<n_kT; i++){
	ifstream myfile1;
	myfile1.open("/afs/cern.ch/work/p/prsaha/public/plotting_macro/CMSSW_9_4_9/src/Tprime/kT_Vs_Xs.txt");
    double MQ_, kT, xs;
    string line, l1, l1_;
    int j=0;
  	while(getline(myfile1,line))
    {
    if(line.find("MQ")!=std::string::npos) continue;
    l1=line;
    stringstream l1_(l1);
    l1_>>MQ_>>kT>>xs;
    if(kT==kappaT[i]){
    cout<<"test=\t"<<MQ_<<"\t"<<kT<<"\t"<<xs<<"\t"<<xs<<endl;
	if(kT==0.25 && j==7) continue;
    x_[j]=MQ_;
//    y_[j]=xs*0.00227;
	y_[j]=xs;
    j++;
    }
    }
    Th_kTVsXs[i] = new TGraph(j,x_,y_);
    Th_kTVsXs[i]->SetLineStyle(3);
    Th_kTVsXs[i]->SetLineWidth(2);
    Th_kTVsXs[i]->SetLineColor(kBlue);
//	mg->Add(Th_kTVsXs[i],"");
}
Th_kTVsXs[0]->RemovePoint(1);
Th_kTVsXs[0]->RemovePoint(1);
Th_kTVsXs[0]->RemovePoint(2);
Th_kTVsXs[1]->RemovePoint(2);
Th_kTVsXs[1]->RemovePoint(1); 
//Th_kTVsXs[4]->RemovePoint(8);

int mass_[n_mPts]    ={600,     650,    700,    800,    900,    1000,   1100,   1200};
float T_xs_[n_mPts]  ={0.1764,  0.1213, 0.0886, 0.0459, 0.0251, 0.0145, 0.00867,0.00536};
float kT_NWA[n_mPts] ={0.221,	0.202,	0.182,	0.158,	0.140,	0.125,	0.113,	0.104};

TGraph* Th_kTVsXs_fkT2[n_kT];
for(int i=0; i<n_kT; i++){
	double m[n_mPts], n[n_mPts];
	int n_pts=0;
	for(int j=0; j<n_mPts; j++)
	{
	if(kappaT[i]==0.25 && n_pts==7) continue;
	m[j]=mass_[j];
//	n[j]=((kappaT[i]*kappaT[i])/(kT_NWA[j]*kT_NWA[j]))*T_xs_[j]*0.00227*1000;
	n[j]=((kappaT[i]*kappaT[i])/(kT_NWA[j]*kT_NWA[j]))*T_xs_[j]*1000;
	n_pts++;
	}
	Th_kTVsXs_fkT2[i] = new TGraph(n_pts,m,n);
//	Th_kTVsXs_fkT2[i]->SetLineStyle(3);
    Th_kTVsXs_fkT2[i]->SetLineWidth(2);
    Th_kTVsXs_fkT2[i]->SetLineColor(kRed);
}
//===============================================================================================
TGraph* Th_WidthVsXs;
    ifstream myfile2;
    myfile2.open("/afs/cern.ch/work/p/prsaha/public/plotting_macro/CMSSW_9_4_9/src/Tprime/Width_Vs_Xs.txt");
    double MQ__, kT_, width, xs_;
    string fline, fl2, fl2_;
    int j=0;
	double x__[8], y__[8];
    while(getline(myfile2,fline))
    {
    if(fline.find("MQ")!=std::string::npos) continue;
    fl2=fline;
    stringstream fl2__(fl2);
    fl2__>>MQ__>>kT_>>width>>xs_;
    if(width==5 && MQ__ == mass_[j]){
		x__[j]=mass_[j];
		y__[j]=xs_;
		cout<<"Mass  "<<x__[j]<<"\t xs "<<y__[j]<<endl;
		j++;
		}
	}
	Th_WidthVsXs = new TGraph(j,x__,y__);	
    Th_WidthVsXs->SetLineStyle(3);
    Th_WidthVsXs->SetLineWidth(2);
    Th_WidthVsXs->SetLineColor(kBlue);

//============================================================================================================
//        TLatex * tex1 = new TLatex(0.18, 0.89, TString("#bf{CMS} #it{Preliminary}"));
		TLatex * tex1 = new TLatex(0.2, 0.89, TString("#scale[1.5]{#bf{CMS}}"));		
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

Double_t Xsec_fx1[8] = {
   600,
   650,
   700,
   800,
   900,
   1000,
   1100,
   1200};
   Double_t Xsec_fy1[8] = {
   2.8203,
   2.4297,
   2.1797,
   2.5859,
   3.4844,
   5.0469,
   6.9062,
   11.6875};
   TGraph *graph = new TGraph(8,Xsec_fx1,Xsec_fy1);
   graph->SetName("Xsec");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineWidth(2);
   graph->SetLineColor(kBlue);


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

TLegend *leg1 = new TLegend(0.4, 0.69, 0.91, 0.85, "");
//TLegend *leg1 = new TLegend(0.2, 0.67, 0.75, 0.84, "");
leg1->SetNColumns(2);
leg1->SetFillColor(0);
//leg1->SetFillStyle(0);
leg1->SetBorderSize(0);
leg1->SetTextSize(0.03);

/*leg1->AddEntry(g,  "#scale[1.1]{Exp 95\% CL}"      ,"l");
leg1->AddEntry(g_obs,  "#scale[1.1]{Obs 95\% CL upper limits}"        ,"l");
leg1->AddEntry(ge, "#scale[1.1]{#pm1 std. deviation}" ,"f");
leg1->AddEntry(ge2,"#scale[1.1]{#pm2 std. deviation}" ,"f");
//leg1->AddEntry(Th_line,"#scale[1.1]{Theory (NWA)}" ,"l");
leg1->AddEntry(Th_kTVsXs_fkT2[2],"#scale[1.1]{Theory for given #kappa_{T}}" ,"l");
//leg1->AddEntry(Th_WidthVsXs,"#scale[1.1]{Theory at fixed #Gamma/M_{T'}=5\%}" ,"l");
*/

leg1->AddEntry(g,  "#scale[1.2]{Median expected}"      ,"l");
leg1->AddEntry(g_obs,  "#scale[1.2]{Observed}"        ,"l");
leg1->AddEntry(ge, "#scale[1.2]{68\% expected}" ,"f");
leg1->AddEntry(ge2,"#scale[1.2]{95\% expected}" ,"f");
leg1->AddEntry(Th_kTVsXs_fkT2[2],"#scale[1.2]{Theory for given #kappa_{T}}" ,"l");

TCanvas* c41 = new TCanvas("c41","c41",200,10,1200,800);
c41->cd();
//gPad->SetBottomMargin(0.1);
gPad->SetTopMargin(0.075);
gPad->SetRightMargin(0.05);
//c41->SetGridx();
//c41->SetGridy();
c41->SetLogy();
ge2->SetFillColor(kYellow);
ge2->SetLineColor(0);
ge2->Draw("a3");
//ge->Draw("Same3l");
ge->SetFillColor(kGreen);
ge->SetLineColor(0);
ge->Draw("CSAME 3l");
g->Draw("CSAME");
//g_Stat->Draw("SAME");
//graph->Draw("SAME");
g_obs->Draw("CSAME");
//Th_line->Draw("CSAME");
//mg->Draw("CSAME");

//Th_kTVsXs_fkT2[0]->Draw("CSAME");
Th_kTVsXs_fkT2[1]->Draw("CSAME");
Th_kTVsXs_fkT2[2]->Draw("CSAME");
Th_kTVsXs_fkT2[3]->Draw("CSAME");
Th_kTVsXs_fkT2[4]->Draw("CSAME");
//Th_kTVsXs_fkT2[5]->Draw("CSAME");
//Th_kTVsXs_fkT2[6]->Draw("CSAME");
//Th_WidthVsXs->Draw("CSAME");

tex1->SetTextColor(kRed);

if(channel=="_Lep"){
tex1->SetTextColor(kRed);
//tex1->SetTextAngle(-17);
//tex1->DrawLatex(0.3, 0.21, "#scale[0.6]{#kappa_{T}=0.05}");
	tex1->SetTextAngle(-11);
	tex1->DrawLatex(0.77, 0.24, "#scale[1]{#kappa_{T}=0.10}");
	tex1->SetTextAngle(-12);
	tex1->DrawLatex(0.77, 0.321, "#scale[1]{#kappa_{T}=0.15}");
	tex1->DrawLatex(0.77, 0.38, "#scale[1]{#kappa_{T}=0.20}");
	tex1->DrawLatex(0.77, 0.43, "#scale[1]{#kappa_{T}=0.25}");
}

else {
	tex1->SetTextAngle(-13);
	tex1->DrawLatex(0.77, 0.255, "#scale[1]{#kappa_{T}=0.10}");
	tex1->SetTextAngle(-12);
	tex1->DrawLatex(0.77, 0.36, "#scale[1]{#kappa_{T}=0.15}");
	tex1->DrawLatex(0.77, 0.435, "#scale[1]{#kappa_{T}=0.20}");
	tex1->DrawLatex(0.77, 0.49, "#scale[1]{#kappa_{T}=0.25}");
}

tex1->SetTextAngle(0);
tex1->SetTextColor(kBlack);
tex1->Draw();
tex2->Draw();
leg1->Draw();
//tex1->DrawLatex(0.25, 0.84, "#scale[0.8]{#Gamma/m_{T'} = 1\% (NWA)}");
tex1->DrawLatex(0.41, 0.89, "#bf{95% CL upper limits}");
if(channel=="_Lep"){
	tex1->DrawLatex(0.2, 0.77, "#scale[1]{Leptonic}");
}
else if(channel=="_Had"){
	tex1->DrawLatex(0.2, 0.77, "#scale[1]{Hadronic}");
}
//else tex1->DrawLatex(0.2, 0.77, "Combined"); //tex1->DrawLatex(0.2, 0.78, "#scale[0.8]{Leptonic + Hadronic}");
else tex1->DrawLatex(0.2, 0.77, ""); //tex1->DrawLatex(0.2, 0.78, "#scale[0.8]{Leptonic + Hadronic}");

tex1->DrawLatex(0.2, 0.82, "#scale[1]{T' #rightarrow tH(H #rightarrow #gamma #gamma)}");

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


