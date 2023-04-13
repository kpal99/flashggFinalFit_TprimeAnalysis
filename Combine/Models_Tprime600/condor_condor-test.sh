#!/bin/sh
ulimit -s unlimited
set -e
cd /afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src
export SCRAM_ARCH=slc7_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
cd /afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Combine/result_UL_v2/Models_Tprime600

if [ $1 -eq 0 ]; then
  combine -M MultiDimFit -n _paramFit_Test_BR_hgg --algo impact --redefineSignalPOIs r -P BR_hgg --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 1 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_BTagReshape_2016 --algo impact --redefineSignalPOIs r -P CMS_hgg_BTagReshape_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 2 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_BTagReshape_2017 --algo impact --redefineSignalPOIs r -P CMS_hgg_BTagReshape_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 3 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_BTagReshape_2018 --algo impact --redefineSignalPOIs r -P CMS_hgg_BTagReshape_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 4 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_ElectronID_2016 --algo impact --redefineSignalPOIs r -P CMS_hgg_ElectronID_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 5 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_ElectronID_2017 --algo impact --redefineSignalPOIs r -P CMS_hgg_ElectronID_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 6 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_ElectronID_2018 --algo impact --redefineSignalPOIs r -P CMS_hgg_ElectronID_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 7 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_ElectronReco_2016 --algo impact --redefineSignalPOIs r -P CMS_hgg_ElectronReco_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 8 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_ElectronReco_2017 --algo impact --redefineSignalPOIs r -P CMS_hgg_ElectronReco_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 9 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_ElectronReco_2018 --algo impact --redefineSignalPOIs r -P CMS_hgg_ElectronReco_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 10 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_JetHEM_2018 --algo impact --redefineSignalPOIs r -P CMS_hgg_JetHEM_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 11 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_LooseMvaSF_2016 --algo impact --redefineSignalPOIs r -P CMS_hgg_LooseMvaSF_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 12 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_LooseMvaSF_2017 --algo impact --redefineSignalPOIs r -P CMS_hgg_LooseMvaSF_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 13 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_MET_PhotonScale --algo impact --redefineSignalPOIs r -P CMS_hgg_MET_PhotonScale --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 14 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_MET_Unclustered --algo impact --redefineSignalPOIs r -P CMS_hgg_MET_Unclustered --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 15 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_MET_res_j --algo impact --redefineSignalPOIs r -P CMS_hgg_MET_res_j --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 16 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_MET_scale_j --algo impact --redefineSignalPOIs r -P CMS_hgg_MET_scale_j --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 17 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_MuonID_2016 --algo impact --redefineSignalPOIs r -P CMS_hgg_MuonID_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 18 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_MuonID_2017 --algo impact --redefineSignalPOIs r -P CMS_hgg_MuonID_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 19 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_MuonID_2018 --algo impact --redefineSignalPOIs r -P CMS_hgg_MuonID_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 20 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_MuonIso_2016 --algo impact --redefineSignalPOIs r -P CMS_hgg_MuonIso_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 21 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_MuonIso_2017 --algo impact --redefineSignalPOIs r -P CMS_hgg_MuonIso_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 22 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_MuonIso_2018 --algo impact --redefineSignalPOIs r -P CMS_hgg_MuonIso_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 23 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_PUJIDShift_2016 --algo impact --redefineSignalPOIs r -P CMS_hgg_PUJIDShift_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 24 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_PUJIDShift_2017 --algo impact --redefineSignalPOIs r -P CMS_hgg_PUJIDShift_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 25 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_PUJIDShift_2018 --algo impact --redefineSignalPOIs r -P CMS_hgg_PUJIDShift_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 26 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_PreselSF --algo impact --redefineSignalPOIs r -P CMS_hgg_PreselSF --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 27 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_SigmaEOverEShift_2016 --algo impact --redefineSignalPOIs r -P CMS_hgg_SigmaEOverEShift_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 28 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_SigmaEOverEShift_2017 --algo impact --redefineSignalPOIs r -P CMS_hgg_SigmaEOverEShift_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 29 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_SigmaEOverEShift_2018 --algo impact --redefineSignalPOIs r -P CMS_hgg_SigmaEOverEShift_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 30 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_TriggerWeight_2016 --algo impact --redefineSignalPOIs r -P CMS_hgg_TriggerWeight_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 31 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_TriggerWeight_2017 --algo impact --redefineSignalPOIs r -P CMS_hgg_TriggerWeight_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 32 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_TriggerWeight_2018 --algo impact --redefineSignalPOIs r -P CMS_hgg_TriggerWeight_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 33 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_electronVetoSF_2016 --algo impact --redefineSignalPOIs r -P CMS_hgg_electronVetoSF_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 34 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_electronVetoSF_2017 --algo impact --redefineSignalPOIs r -P CMS_hgg_electronVetoSF_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 35 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_electronVetoSF_2018 --algo impact --redefineSignalPOIs r -P CMS_hgg_electronVetoSF_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 36 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_FNUFEB_13TeVscaleCorr --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_FNUFEB_13TeVscaleCorr --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 37 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_FNUFEE_13TeVscaleCorr --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_FNUFEE_13TeVscaleCorr --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 38 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_Geant4_13TeVscale --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_Geant4_13TeVscale --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 39 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_HighR9EBPhi_13TeVsmear_2016 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_HighR9EBPhi_13TeVsmear_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 40 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_HighR9EBPhi_13TeVsmear_2017 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_HighR9EBPhi_13TeVsmear_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 41 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_HighR9EBPhi_13TeVsmear_2018 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_HighR9EBPhi_13TeVsmear_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 42 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_HighR9EBRho_13TeVsmear_2016 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_HighR9EBRho_13TeVsmear_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 43 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_HighR9EBRho_13TeVsmear_2017 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_HighR9EBRho_13TeVsmear_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 44 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_HighR9EBRho_13TeVsmear_2018 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_HighR9EBRho_13TeVsmear_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 45 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_HighR9EB_13TeVscale_2016 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_HighR9EB_13TeVscale_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 46 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_HighR9EB_13TeVscale_2017 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_HighR9EB_13TeVscale_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 47 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_HighR9EB_13TeVscale_2018 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_HighR9EB_13TeVscale_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 48 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_HighR9EEPhi_13TeVsmear_2016 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_HighR9EEPhi_13TeVsmear_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 49 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_HighR9EEPhi_13TeVsmear_2017 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_HighR9EEPhi_13TeVsmear_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 50 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_HighR9EEPhi_13TeVsmear_2018 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_HighR9EEPhi_13TeVsmear_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 51 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_HighR9EERho_13TeVsmear_2016 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_HighR9EERho_13TeVsmear_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 52 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_HighR9EERho_13TeVsmear_2017 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_HighR9EERho_13TeVsmear_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 53 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_HighR9EERho_13TeVsmear_2018 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_HighR9EERho_13TeVsmear_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 54 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_HighR9EE_13TeVscale_2016 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_HighR9EE_13TeVscale_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 55 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_HighR9EE_13TeVscale_2017 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_HighR9EE_13TeVscale_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 56 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_HighR9EE_13TeVscale_2018 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_HighR9EE_13TeVscale_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 57 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_LowR9EBPhi_13TeVsmear_2016 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_LowR9EBPhi_13TeVsmear_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 58 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_LowR9EBPhi_13TeVsmear_2017 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_LowR9EBPhi_13TeVsmear_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 59 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_LowR9EBPhi_13TeVsmear_2018 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_LowR9EBPhi_13TeVsmear_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 60 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_LowR9EBRho_13TeVsmear_2016 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_LowR9EBRho_13TeVsmear_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 61 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_LowR9EBRho_13TeVsmear_2017 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_LowR9EBRho_13TeVsmear_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 62 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_LowR9EBRho_13TeVsmear_2018 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_LowR9EBRho_13TeVsmear_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 63 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_LowR9EB_13TeVscale_2016 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_LowR9EB_13TeVscale_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 64 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_LowR9EB_13TeVscale_2017 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_LowR9EB_13TeVscale_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 65 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_LowR9EB_13TeVscale_2018 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_LowR9EB_13TeVscale_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 66 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_LowR9EEPhi_13TeVsmear_2016 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_LowR9EEPhi_13TeVsmear_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 67 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_LowR9EEPhi_13TeVsmear_2017 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_LowR9EEPhi_13TeVsmear_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 68 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_LowR9EEPhi_13TeVsmear_2018 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_LowR9EEPhi_13TeVsmear_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 69 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_LowR9EERho_13TeVsmear_2016 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_LowR9EERho_13TeVsmear_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 70 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_LowR9EERho_13TeVsmear_2017 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_LowR9EERho_13TeVsmear_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 71 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_LowR9EERho_13TeVsmear_2018 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_LowR9EERho_13TeVsmear_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 72 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_LowR9EE_13TeVscale_2016 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_LowR9EE_13TeVscale_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 73 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_LowR9EE_13TeVscale_2017 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_LowR9EE_13TeVscale_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 74 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_LowR9EE_13TeVscale_2018 --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_LowR9EE_13TeVscale_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 75 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_MaterialCentralBarrel_13TeVscaleCorr --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_MaterialCentralBarrel_13TeVscaleCorr --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 76 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_MaterialForward_13TeVscaleCorr --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_MaterialForward_13TeVscaleCorr --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 77 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_MaterialOuterBarrel_13TeVscaleCorr --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_MaterialOuterBarrel_13TeVscaleCorr --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 78 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_NonLinearity_13TeVscale --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_NonLinearity_13TeVscale --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 79 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_ShowerShapeHighR9EB_13TeVscaleCorr --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_ShowerShapeHighR9EB_13TeVscaleCorr --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 80 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_ShowerShapeHighR9EE_13TeVscaleCorr --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_ShowerShapeHighR9EE_13TeVscaleCorr --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 81 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_ShowerShapeLowR9EB_13TeVscaleCorr --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_ShowerShapeLowR9EB_13TeVscaleCorr --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 82 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_ShowerShapeLowR9EE_13TeVscaleCorr --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_ShowerShapeLowR9EE_13TeVscaleCorr --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 83 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_nuisance_deltafracright --algo impact --redefineSignalPOIs r -P CMS_hgg_nuisance_deltafracright --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 84 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_phoIdMva_2016 --algo impact --redefineSignalPOIs r -P CMS_hgg_phoIdMva_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 85 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_phoIdMva_2017 --algo impact --redefineSignalPOIs r -P CMS_hgg_phoIdMva_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 86 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hgg_phoIdMva_2018 --algo impact --redefineSignalPOIs r -P CMS_hgg_phoIdMva_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 87 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_res_j_2016 --algo impact --redefineSignalPOIs r -P CMS_res_j_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 88 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_res_j_2017 --algo impact --redefineSignalPOIs r -P CMS_res_j_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 89 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_res_j_2018 --algo impact --redefineSignalPOIs r -P CMS_res_j_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 90 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_scale_j_2016 --algo impact --redefineSignalPOIs r -P CMS_scale_j_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 91 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_scale_j_2017 --algo impact --redefineSignalPOIs r -P CMS_scale_j_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 92 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_scale_j_2018 --algo impact --redefineSignalPOIs r -P CMS_scale_j_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 93 ]; then
  combine -M MultiDimFit -n _paramFit_Test_MH --algo impact --redefineSignalPOIs r -P MH --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 94 ]; then
  combine -M MultiDimFit -n _paramFit_Test_QCDscale_VH --algo impact --redefineSignalPOIs r -P QCDscale_VH --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 95 ]; then
  combine -M MultiDimFit -n _paramFit_Test_QCDscale_ggH --algo impact --redefineSignalPOIs r -P QCDscale_ggH --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 96 ]; then
  combine -M MultiDimFit -n _paramFit_Test_QCDscale_qqH --algo impact --redefineSignalPOIs r -P QCDscale_qqH --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 97 ]; then
  combine -M MultiDimFit -n _paramFit_Test_QCDscale_tHq --algo impact --redefineSignalPOIs r -P QCDscale_tHq --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 98 ]; then
  combine -M MultiDimFit -n _paramFit_Test_QCDscale_ttH --algo impact --redefineSignalPOIs r -P QCDscale_ttH --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 99 ]; then
  combine -M MultiDimFit -n _paramFit_Test_env_pdf_0_13TeV_bern1_p0 --algo impact --redefineSignalPOIs r -P env_pdf_0_13TeV_bern1_p0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 100 ]; then
  combine -M MultiDimFit -n _paramFit_Test_env_pdf_0_13TeV_exp1_p1 --algo impact --redefineSignalPOIs r -P env_pdf_0_13TeV_exp1_p1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 101 ]; then
  combine -M MultiDimFit -n _paramFit_Test_env_pdf_0_13TeV_lau1_l1 --algo impact --redefineSignalPOIs r -P env_pdf_0_13TeV_lau1_l1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 102 ]; then
  combine -M MultiDimFit -n _paramFit_Test_env_pdf_0_13TeV_pow1_p1 --algo impact --redefineSignalPOIs r -P env_pdf_0_13TeV_pow1_p1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 103 ]; then
  combine -M MultiDimFit -n _paramFit_Test_env_pdf_1_13TeV_bern1_p0 --algo impact --redefineSignalPOIs r -P env_pdf_1_13TeV_bern1_p0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 104 ]; then
  combine -M MultiDimFit -n _paramFit_Test_env_pdf_1_13TeV_exp1_p1 --algo impact --redefineSignalPOIs r -P env_pdf_1_13TeV_exp1_p1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 105 ]; then
  combine -M MultiDimFit -n _paramFit_Test_env_pdf_1_13TeV_lau1_l1 --algo impact --redefineSignalPOIs r -P env_pdf_1_13TeV_lau1_l1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 106 ]; then
  combine -M MultiDimFit -n _paramFit_Test_env_pdf_1_13TeV_pow1_p1 --algo impact --redefineSignalPOIs r -P env_pdf_1_13TeV_pow1_p1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 107 ]; then
  combine -M MultiDimFit -n _paramFit_Test_lumi_13TeV_Correlated_2016 --algo impact --redefineSignalPOIs r -P lumi_13TeV_Correlated_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 108 ]; then
  combine -M MultiDimFit -n _paramFit_Test_lumi_13TeV_Correlated_2017 --algo impact --redefineSignalPOIs r -P lumi_13TeV_Correlated_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 109 ]; then
  combine -M MultiDimFit -n _paramFit_Test_lumi_13TeV_Correlated_2018 --algo impact --redefineSignalPOIs r -P lumi_13TeV_Correlated_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 110 ]; then
  combine -M MultiDimFit -n _paramFit_Test_pdf_Higgs_VH --algo impact --redefineSignalPOIs r -P pdf_Higgs_VH --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 111 ]; then
  combine -M MultiDimFit -n _paramFit_Test_pdf_Higgs_ggH --algo impact --redefineSignalPOIs r -P pdf_Higgs_ggH --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 112 ]; then
  combine -M MultiDimFit -n _paramFit_Test_pdf_Higgs_qqH --algo impact --redefineSignalPOIs r -P pdf_Higgs_qqH --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 113 ]; then
  combine -M MultiDimFit -n _paramFit_Test_pdf_Higgs_tHq --algo impact --redefineSignalPOIs r -P pdf_Higgs_tHq --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 114 ]; then
  combine -M MultiDimFit -n _paramFit_Test_pdf_Higgs_ttH --algo impact --redefineSignalPOIs r -P pdf_Higgs_ttH --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 115 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prefireWeight_2016 --algo impact --redefineSignalPOIs r -P prefireWeight_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 116 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prefireWeight_2017 --algo impact --redefineSignalPOIs r -P prefireWeight_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 117 ]; then
  combine -M MultiDimFit -n _paramFit_Test_shapeBkg_bkg_mass_THQHadronicTag__norm --algo impact --redefineSignalPOIs r -P shapeBkg_bkg_mass_THQHadronicTag__norm --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi
if [ $1 -eq 118 ]; then
  combine -M MultiDimFit -n _paramFit_Test_shapeBkg_bkg_mass_THQLeptonicTag__norm --algo impact --redefineSignalPOIs r -P shapeBkg_bkg_mass_THQLeptonicTag__norm --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --freezeParameter MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --rMin -100 -m 125 -d Datacard_Tprime600_Syst.root
fi