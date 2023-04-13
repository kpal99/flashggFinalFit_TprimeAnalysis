#!/bin/bash

cd /afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Combine

eval `scramv1 runtime -sh`

text2workspace.py Datacard_Tprime675.txt -o Datacard_Tprime675_AsymptoticLimits.root -m 125 higgsMassRange=122,128 -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO "map=.*/ttH.*:r_ttH[1,0,2]" --PO "map=.*/tHq.*:r_tHq[1,0,2]" --PO "map=.*/Tvlq.*:r_Tvlq[1,0,10]" --PO "map=.*/qqH.*:r_qqH[1,0,2]" --PO "map=.*/ggH.*:r_ggH[1,0,2]" 