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
#include "TBox.h"
#include "tdrStyle/tdrstyle.C"
#include "tdrStyle/CMS_lumi.C"

using namespace std;

void makeBrazilPlot_kappa(TString channel="", TString method="mu", TString ext=""){
gStyle->SetOptStat(0);
gROOT->SetBatch();
setTDRStyle();
const int points=8;
int mass[points]	={600,	 	650, 	700, 	800, 	900, 	1000, 	1100, 	1200};
float T_xs[points] 	={0.1764,	0.1213,	0.0886,	0.0459,	0.0251,	0.0145, 0.00867,0.00536}; //in pb

ifstream myfile;
myfile.open("/afs/cern.ch/work/p/prsaha/public/Tprime_analysis/CrossSections_BR_SingleT_NWA.txt");
ofstream kappa_of;
kappa_of.open("ExpObs_kappa.txt");
kappa_of << "MQ" <<"\t"<< "kappa_th"<<"\t"<<"kappa_Exp"<<"\t"<< "kappa_obs"<<"\t"<<"sigma_1l"<<"\t"<<"sigma_1h"<<"\t"<<"sigma_2l"<<"\t"<<"sigma_2h"<<endl;

double col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, col_10, col_11;
string line, line1, line1_; 
double sigma[8], kappa[10], xs_NLO[8],BR_tH[8];
double MQ[8]		={600, 		650, 		700, 		800, 		900, 		1000, 		1100,		1200};
double sigmaHat[8]	={67.969, 	56.1735,	50.9587, 	34.9723, 	24.5265, 	17.572, 	12.7958, 	9.44201};
int m_count=0;
while(getline(myfile,line))
	{
		if(line.find("MQ")!=std::string::npos) continue;
		line1 = line;
		stringstream line1_(line1);
		line1_>>col_1>>col_2>>col_3>>col_4>>col_5>>col_6>>col_7>>col_8>>col_9>>col_10>>col_11;	
		if(/*(col_3 == 1) &&*/ col_1 < 1201) 
			{
				kappa[m_count] 	= col_8;
				BR_tH[m_count] 	= col_11;
				xs_NLO[m_count]	= BR_tH[m_count]*sigmaHat[m_count]*pow((kappa[m_count]*0.458486), 2);
				cout<<"Cal. xs\t"<<xs_NLO[m_count]<<endl;
				m_count++;
			}	
	}

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
		double xs_X_Br_=1;
		if(method=="xs_X_Br")  xs_X_Br_ = T_xs[i]*0.00227*1000; //in fb
		else if(method=="kappa") xs_X_Br_ = 2.18109*sqrt(xs_NLO[i]/(sigmaHat[i]*BR_tH[i])); //Here xs_X_Br is actually kappa. Fix the name later
		else xs_X_Br_ =1;
        string mass_str;
        stringstream ss;
        ss << mass[i];
        ss >> mass_str;
        TFile *file_ = new TFile(file_path + mass_str+ channel +"/higgsCombine" + channel + "_Syst.AsymptoticLimits.mH125.root", "READ");
        TTree* tree_ = (TTree*)file_->Get("limit");
        Int_t nentries=(Int_t)tree_->GetEntries();
        Double_t qlimit;
        tree_->SetBranchAddress("limit", &qlimit);
		tree_->SetBranchStatus("*", 1);	
		x[i] = mass[i];
		xsBr[i] = xs_X_Br_;	

        for(int ievent=0; ievent <points ; ievent++)
			{
			tree_-> GetEntry( ievent );
//        	x[ievent] = mass[i];
			if(method=="kappa") qlimit = sqrt(qlimit);
			else qlimit = qlimit;

			if (ievent==0) ey2l[i] = qlimit*xs_X_Br_;// cout<<"ey2l[ievent] "<<qlimit<<endl;
    		else if (ievent==1) eyl[i] = qlimit*xs_X_Br_;
			else if (ievent==2) {y[i]= qlimit*xs_X_Br_; cout<<"Tprime"<<mass[i]<<" exp =	"<<qlimit<<endl;
									}
     		else if (ievent==3) eyh[i] = qlimit*xs_X_Br_;
          	else if (ievent==4) ey2h[i] = qlimit*xs_X_Br_;
			else if (ievent==5) {obsl[i] = qlimit*xs_X_Br_; /*cout<<"Tprime"<<mass[i]<<" obs =   "<<qlimit<<endl;*/}
            }
		kappa_of << mass[i] <<"    "<< xs_X_Br_ <<"   "<< y[i]<<"   "<< obsl[i]<<"   "<<eyl[i]<<"   "<<eyh[i]<<"   "<<ey2l[i]<<"   "<<ey2h[i]<<endl;
        }
kappa_of.close();
//====================================================================================================
TString file_path_Stat="/afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Combine/result_UL_v2/Models_Tprime";
for(int i=0; i<points; i++)
        {
    	double xs_X_Br_=1;
    	if(method=="xs_X_Br")  xs_X_Br_ = T_xs[i]*0.00223*1000; //in fb
    	else if(method=="kappa") xs_X_Br_ = 2.18109*sqrt(xs_NLO[i]/(sigmaHat[i]*BR_tH[i]));
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
                if (ievent==2) 
					{	
						y_Stat[i]= qlimit*xs_X_Br_; 
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
ge->SetLineColor(0);

TGraphAsymmErrors* ge2 = new TGraphAsymmErrors(points, x, y, ex2l_,ex2h_,ey2l_,ey2h_);
ge2->SetFillColor(kYellow);
ge2->SetLineColor(0);
ge2->GetXaxis()->SetTitle("M_{T'} (GeV)");
ge2->GetXaxis()->SetRangeUser(600,1200);
//ge2->GetYaxis()->SetRangeUser(0,1000);

if(method=="xs_X_Br") {
	
	ge2->SetMaximum(10);
	ge2->SetMinimum(0.01);
	ge2->GetYaxis()->SetTitle("95\% CL limit on (#sigma #times Br(H #rightarrow #gamma #gamma) in fb)");
	}

else if(method=="kappa"){
    ge2->SetMaximum(0.7);
    ge2->SetMinimum(0.05);
	ge2->GetYaxis()->SetTitle("#scale[0.75]{T' coupling strength ( #it{#kappa}_{T} )}");
    }

else{
	ge2->GetYaxis()->SetTitle("95\% CL limit on #mu");
	}	
ge2->SetTitle("");
ge2->GetYaxis()->SetTitleOffset(0.85);

TGraph* g = new TGraph(points, x, y);
g->SetLineWidth(3);
g->SetLineStyle(2);

TGraph* g_Stat = new TGraph(points, x, y_Stat);
g_Stat->SetLineWidth(2);
g_Stat->SetLineStyle(2);

TGraph* g_obs = new TGraph(points, x, obsl);
g_obs->SetLineWidth(3);
g_obs->SetLineStyle(1);

TGraph* Th_line = new TGraph(points, x, xsBr);
Th_line->SetLineWidth(2);
//Th_line->SetLineStyle(2);
Th_line->SetLineColor(kRed);

//====================================================================================
const int n_W=8;
const int n_mPts=8;
double width[n_W]={1, 2, 3, 4, 5, 10, 20, 30};
TGraph* Th_WidthVskT[n_W];
double x_[8], y_[8];
for(int i=0; i<n_W; i++){
    ifstream myfile1;
    myfile1.open("/afs/cern.ch/work/p/prsaha/public/plotting_macro/CMSSW_9_4_9/src/Tprime/width_Vs_kT.txt");
    double MQ_, width_, kT;
    string line, l1, l1_;
    int j=0;
    while(getline(myfile1,line))
    {
    if(line.find("MQ")!=std::string::npos) continue;
    l1=line;
    stringstream l1_(l1);
    l1_>>MQ_>>width_>>kT;
    if(width_==width[i]){
    cout<<"test=\t"<<MQ_<<"\t"<<width_<<"\t"<<kT<<endl;
    x_[j]=MQ_;
    y_[j]=kT;
    j++;
    }
    }
    Th_WidthVskT[i] = new TGraph(j,x_,y_);
    Th_WidthVskT[i]->SetLineStyle(7);
    Th_WidthVskT[i]->SetLineWidth(2);
    Th_WidthVskT[i]->SetLineColor(kRed);
}
//===================================================================================
//        TLatex * tex1 = new TLatex(0.18, 0.89,TString("#bf{CMS} #it{Preliminary}"));
//        TLatex * tex1 = new TLatex(0.18, 0.89,TString("#bf{CMS}"));
        TLatex * tex1 = new TLatex(0.2, 0.89, TString("#scale[1.5]{#bf{CMS}}"));
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



//TLegend *leg1 = new TLegend(0.2, 0.72, 0.7, 0.88, "");
//TLegend *leg1 = new TLegend(0.2, 0.67, 0.75, 0.84, "");
TLegend *leg1 = new TLegend(0.4, 0.69, 0.91, 0.85, "");
leg1->SetNColumns(2);
//leg1->SetFillColor(0);
leg1->SetFillStyle(0);
leg1->SetBorderSize(0);
leg1->SetTextSize(0.03);

leg1->AddEntry(g,  "#scale[1.2]{Median expected}"      ,"l");
leg1->AddEntry(g_obs,  "#scale[1.2]{Observed}"        ,"l");
leg1->AddEntry(ge, "#scale[1.2]{68\% expected}", "f");
leg1->AddEntry(ge2,"#scale[1.2]{95\% expected}", "f");
leg1->AddEntry(Th_WidthVskT[0],"#scale[1.2]{Theory for given #Gamma/M_{T'}}", "l");

/*
leg1->AddEntry(g,  "#scale[1]{Exp 95\% CL}"      ,"l");
leg1->AddEntry(g_obs,  "#scale[1]{Obs 95\% CL upper limits}"        ,"l");
leg1->AddEntry(ge, "#scale[1]{#pm1 std. deviation}", "f");
leg1->AddEntry(ge2, "#scale[1]{#pm2 std. deviation}", "f");
//leg1->AddEntry(Th_line, "#scale[1]{Theory at fixed #Gamma/M_{T'}}", "l");
leg1->AddEntry(Th_WidthVskT[0], "#scale[1]{Theory at fixed #Gamma/M_{T'}}", "l");
*/
TCanvas* c41 = new TCanvas("c41","c41",200,10,1200,800);

c41->cd();
gPad->SetTopMargin(0.075);
gPad->SetRightMargin(0.05);
gPad->SetLeftMargin(0.15);

//gPad->SetBottomMargin(0.1);
//gPad->SetLeftMargin(0.15);
//c41->SetGridx();
//c41->SetGridy();
//c41->SetLogy();
ge2->Draw("CSAME 3al");
ge->Draw("CSAME 3l");
g->Draw("CSAME");
g_obs->Draw("CSAME");
//Th_line->Draw("CSAME");

Th_WidthVskT[0]->Draw("CSAME");
Th_WidthVskT[1]->Draw("CSAME");
Th_WidthVskT[2]->Draw("CSAME");
Th_WidthVskT[3]->Draw("CSAME");
Th_WidthVskT[4]->Draw("CSAME");
//Th_WidthVskT[5]->Draw("CSAME");

//mg->Draw("CSAME");
c41->Update();

tex1->Draw();
tex2->Draw();
leg1->Draw();
//tex1->DrawLatex(0.75, 0.83, "#scale[0.9]{#Gamma/m_{T'} = 1\%(NWA)}");
//tex1->DrawLatex(0.75, 0.88, "#scale[0.9]{T' #rightarrow tH(H #rightarrow #gamma #gamma)}");
tex1->DrawLatex(0.2, 0.82, "#scale[1]{T' #rightarrow tH(H #rightarrow #gamma #gamma)}");
//tex1->PaintLatex(0.8, 0.2, 2.1, 2, "NWA");
tex1->DrawLatex(0.41, 0.89, "#bf{95% CL upper limits}");
if(channel=="_Lep"){
    tex1->DrawLatex(0.2, 0.78, "#scale[1]{Leptonic}");
}
else if(channel=="_Had"){
    tex1->DrawLatex(0.2, 0.78, "#scale[1]{Hadronic}");
}
//else tex1->DrawLatex(0.2, 0.77, "Combined");
else tex1->DrawLatex(0.2, 0.77, "");

tex1->SetTextColor(kRed);
tex1->SetTextAngle(-16);
tex1->DrawLatex(0.25, 0.345, "#scale[0.9]{#Gamma/M_{T'}=1%}");
tex1->SetTextAngle(-18);
tex1->DrawLatex(0.25, 0.42, "#scale[0.9]{#Gamma/M_{T'}=2%}");
tex1->DrawLatex(0.25, 0.48, "#scale[0.9]{#Gamma/M_{T'}=3%}");
tex1->SetTextAngle(-23);
tex1->DrawLatex(0.25, 0.55, "#scale[0.9]{#Gamma/M_{T'}=4%}");
tex1->DrawLatex(0.25, 0.61, "#scale[0.9]{#Gamma/M_{T'}=5%}");
tex1->SetTextAngle(0);
tex1->SetTextColor(kBlack);
gPad->RedrawAxis();

c41->SaveAs("/eos/user/p/prsaha/www/Tprime_analysis/Finalfit_Lite_output/UL/result_v2/LimitTprime_"+ method + channel + ext + ".pdf");
c41->SaveAs("/eos/user/p/prsaha/www/Tprime_analysis/Finalfit_Lite_output/UL/result_v2/LimitTprime_"+ method + channel + ext + ".png");
c41->SaveAs("/eos/user/p/prsaha/www/Tprime_analysis/Finalfit_Lite_output/UL/result_v2/LimitTprime_"+ method + channel + ext + ".root");
c41->SaveAs("/eos/user/p/prsaha/www/Tprime_analysis/Finalfit_Lite_output/UL/result_v2/LimitTprime_"+ method + channel + ext + ".C");
}

