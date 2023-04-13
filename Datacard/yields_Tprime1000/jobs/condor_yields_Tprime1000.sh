#!/bin/bash
ulimit -s unlimited
set -e
cd /afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src
export SCRAM_ARCH=slc7_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
cd /afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Datacard
export PYTHONPATH=$PYTHONPATH:/afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/tools:/afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Datacard/tools

if [ $1 -eq 0 ]; then
  python /afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Datacard/makeYields.py --cat THQHadronicTag --procs Tprime1000,TTH,THQ,VBF,GG2H,VH --ext Tprime1000 --mass 125 --inputWSDirMap 2016=/eos/user/p/prsaha/Tprime_analysis/FinalFit_inputs/UL/v2/1000/2016,2017=/eos/user/p/prsaha/Tprime_analysis/FinalFit_inputs/UL/v2/1000/2017,2018=/eos/user/p/prsaha/Tprime_analysis/FinalFit_inputs/UL/v2/1000/2018 --sigModelWSDir ./Models_Tprime1000/signal --sigModelExt packaged_Tprime1000 --bkgModelWSDir ./Models_Tprime1000/background --bkgModelExt multipdf  --mergeYears --doSystematics
fi
if [ $1 -eq 1 ]; then
  python /afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Datacard/makeYields.py --cat THQLeptonicTag --procs Tprime1000,TTH,THQ,VBF,GG2H,VH --ext Tprime1000 --mass 125 --inputWSDirMap 2016=/eos/user/p/prsaha/Tprime_analysis/FinalFit_inputs/UL/v2/1000/2016,2017=/eos/user/p/prsaha/Tprime_analysis/FinalFit_inputs/UL/v2/1000/2017,2018=/eos/user/p/prsaha/Tprime_analysis/FinalFit_inputs/UL/v2/1000/2018 --sigModelWSDir ./Models_Tprime1000/signal --sigModelExt packaged_Tprime1000 --bkgModelWSDir ./Models_Tprime1000/background --bkgModelExt multipdf  --mergeYears --doSystematics
fi
