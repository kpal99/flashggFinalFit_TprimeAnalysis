#!/bin/bash

    if [ ! -d "Models_HiggsCR" ]; then
	mkdir Models_HiggsCR
    fi
    if [ ! -d "Models_HiggsCR/signal" ]; then
	mkdir Models_HiggsCR/signal
    fi
    if [ ! -d "Models_HiggsCR/background" ]; then
	mkdir Models_HiggsCR/background
    fi
	cp ../Signal/outdir_packaged_HiggsCR/CMS-HGG_sigfit_packaged_HiggsCR*.root Models_HiggsCR/signal/
	cp ../Background/outdir_HiggsCR/*.root Models_HiggsCR/background/
	python RunText2Workspace.py --mode mu_inclusive --ext _HiggsCR --batch condor --queue workday
#	combine Datacard_Tprime$i\.txt -M AsymptoticLimits -m 125 --redefineSignalPOIs r --trackParameters r --freezeParameter MH -t -1 --run=blind
#	combine Datacard_Tprime$i.txt -M AsymptoticLimits -m 125 -P --PO "map=.*/tHq.*:r_tHq[1,0,10]" --PO "map=.*/ttH.*:r_ttH[1,0,10]" --redefineSignalPOIs r_tHq --trackParameters r_tHq,r_ttH --freezeParameter MH --run=blind -t -1
#	combine Datacard_Tprime${i}_AsymptoticLimits.root -M AsymptoticLimits -m 125 --redefineSignalPOIs r_tHq --trackParameters r_tHq,r_ttH --freezeParameter MH --run=blind -t -1
#	cp higgsCombineTest.AsymptoticLimits.mH125.root Models_Tprime${i}

#Expected
#combine Datacard_HiggsCR_mu_inclusive.root -M MultiDimFit -m 125 --redefineSignalPOIs r --freezeParameter MH -t -1 --expectSignal 1 --saveWorkspace --cminDefaultMinimizerStrategy 0 --setParameterRanges r=-5,5 --trackParameters r --saveNLL --points=100

#Observed
#combine Datacard_HiggsCR_mu_inclusive.root -M MultiDimFit -m 125 --redefineSignalPOIs r --freezeParameter MH --saveWorkspace --cminDefaultMinimizerStrategy 0 --setParameterRanges r=-5,5 --trackParameters r --saveNLL --points=50 --algo=grid
