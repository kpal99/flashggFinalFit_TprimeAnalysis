#!/bin/bash
ulimit -s unlimited
set -e
cd /afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Combine/Models_Tprime600/toys
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`

ExpSig=$1

#Generate command
combine /afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Combine/Models_Tprime600/Datacard_Tprime600_Syst.root -M GenerateOnly --redefineSignalPOIs r --bypassFrequentistFit -t 1000 --expectSignal ${ExpSig} --saveToys -m 125 --freezeParameters MH -n _expSignal_${ExpSig}_1000toysForBias_step

#FitDiagnostics command
combine /afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Combine/Models_Tprime600/Datacard_Tprime600_Syst.root -M FitDiagnostics -m 125 --redefineSignalPOIs r --setParameterRanges r=-90,110 --trackParameters r --toysFile higgsCombine_expSignal_${ExpSig}_1000toysForBias_step.GenerateOnly.mH125.123456.root  -t 1000 --freezeParameters MH -n _expSignal_${ExpSig}_1000toysForBias_step --cminDefaultMinimizerStrategy=0

