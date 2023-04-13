#!/bin/bash

cd /afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Combine

eval `scramv1 runtime -sh`

text2workspace.py Datacard_Tprime625.txt -o Datacard_Tprime625_AsymptoticLimits.root -m 125 higgsMassRange=122,128 -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO "map=.*/Tvlq.*:r_Tvlq[1,0,100]" 