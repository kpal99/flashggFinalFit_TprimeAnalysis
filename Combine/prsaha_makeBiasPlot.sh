#!/bin/bash

for i in 600 #625 650 675 700 800 900 1000 1100 1200
do
	python makeBiasPlot.py --inputFileDir /afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Combine/Models_Tprime${i}/toys --ext Tprime${i}
done
