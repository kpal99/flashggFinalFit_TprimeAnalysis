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
  python /afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Datacard/makeYields.py --cat THQLeptonicTag --procs THQ --ext test --mass 125 --inputWSDirMap 2016=/eos/user/p/prsaha/Tprime_analysis/FinalFit_inputs/v2/2016/M700,2017=/eos/user/p/prsaha/Tprime_analysis/FinalFit_inputs/v2/2017/M700,2018=/eos/user/p/prsaha/Tprime_analysis/FinalFit_inputs/v2/2018/M700  --mergeYears
fi
