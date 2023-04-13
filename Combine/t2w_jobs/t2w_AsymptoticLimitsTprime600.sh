#!/bin/bash

cd /afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Combine

eval `scramv1 runtime -sh`

text2workspace.py DatacardTprime600.txt -o DatacardTprime600_AsymptoticLimits.root -m 125 higgsMassRange=122,128 -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO "map=.*/ttH.*:r_top[1,0,10]" --PO "map=.*/tHq.*:r_top[1,0,10]"