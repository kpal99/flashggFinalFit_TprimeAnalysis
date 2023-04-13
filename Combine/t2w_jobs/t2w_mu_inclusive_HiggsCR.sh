#!/bin/bash

cd /afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Combine

eval `scramv1 runtime -sh`

text2workspace.py Datacard_HiggsCR.txt -o Datacard_HiggsCR_mu_inclusive.root -m 125 higgsMassRange=122,128 