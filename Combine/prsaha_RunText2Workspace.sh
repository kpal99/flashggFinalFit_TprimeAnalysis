#!/bin/bash

for i in 600 625 650 675 700 800 900 1000 1100 1200
do
    if [ ! -d "Models_Tprime${i}" ]; then
	mkdir Models_Tprime${i}
    fi
    if [ ! -d "Models_Tprime${i}/signal" ]; then
	mkdir Models_Tprime${i}/signal
    fi
    if [ ! -d "Models_Tprime${i}/background" ]; then
	mkdir Models_Tprime${i}/background
    fi
	cp ../Signal/outdir_packaged_Tprime${i}/CMS-HGG_sigfit_packaged_Tprime${i}_*.root Models_Tprime${i}/signal/
	cp ../Background/outdir_Tprime600_700/*.root Models_Tprime${i}/background/
	python RunText2Workspace.py --mode AsymptoticLimits --ext _Tprime${i} --batch condor --queue workday
#	combine Datacard_Tprime$i\.txt -M AsymptoticLimits -m 125 --redefineSignalPOIs r --trackParameters r --freezeParameter MH -t -1 --run=blind
#	combine Datacard_Tprime$i.txt -M AsymptoticLimits -m 125 -P --PO "map=.*/tHq.*:r_tHq[1,0,10]" --PO "map=.*/ttH.*:r_ttH[1,0,10]" --redefineSignalPOIs r_tHq --trackParameters r_tHq,r_ttH --freezeParameter MH --run=blind -t -1
#	combine Datacard_Tprime${i}_AsymptoticLimits.root -M AsymptoticLimits -m 125 --redefineSignalPOIs r_tHq --trackParameters r_tHq,r_ttH --freezeParameter MH --run=blind -t -1
#	cp higgsCombineTest.AsymptoticLimits.mH125.root Models_Tprime${i}
done
