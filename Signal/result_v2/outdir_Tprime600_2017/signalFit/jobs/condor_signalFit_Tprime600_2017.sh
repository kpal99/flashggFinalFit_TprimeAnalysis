#!/bin/bash
ulimit -s unlimited
set -e
cd /afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src
export SCRAM_ARCH=slc7_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
cd /afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Signal
export PYTHONPATH=$PYTHONPATH:/afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/tools:/afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Signal/tools

if [ $1 -eq 0 ]; then
  python /afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Signal/scripts/signalFit.py --inputWSDir /eos/user/p/prsaha/Tprime_analysis/FinalFit_inputs/v2/2017/M600 --ext Tprime600_2017 --proc THQ --cat THQLeptonicTag --year 2017 --analysis Tprime --massPoints 125 --scales '' --scalesCorr '' --scalesGlobal '' --smears '' --skipSystematics --skipVertexScenarioSplit --doPlots
fi
