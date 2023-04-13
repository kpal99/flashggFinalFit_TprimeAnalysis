#!/bin/bash
label=_StatOnly
#label=_Syst

echo "Running combine---------"

for i in 700 800 1000 1100 #850 950 1050 1150
do

#	cp ../Datacard/Datacard_HadLep/Datacard_Tprime${i}${label}\.txt Models_Tprime${i}/
#	sleep 1s
	text2workspace.py Models_Tprime${i}/Datacard_Tprime${i}${label}\.txt
	sleep 1s
	combine Models_Tprime${i}/Datacard_Tprime${i}${label}\.root -M AsymptoticLimits -m 125 --redefineSignalPOIs r --trackParameters r --freezeParameter MH --saveWorkspace --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 -n ${label} --run=blind #-t -1 --expectSignal 1 
#	combine Datacard_Tprime$i.txt -M AsymptoticLimits -m 125 -P --PO "map=.*/tHq.*:r_tHq[1,0,10]" --PO "map=.*/ttH.*:r_ttH[1,0,10]" --redefineSignalPOIs r_tHq --trackParameters r_tHq,r_ttH --freezeParameter MH --run=blind -t -1
#	combine Datacard_Tprime${i}_AsymptoticLimits.root -M AsymptoticLimits -m 125 --redefineSignalPOIs r_Tvlq --setParameters r_tHq=1,r_ttH=1,r_qqH=1,r_ggH=1 --freezeParameter MH,r_tHq,r_ttH,r_qqH,r_ggH -t -1 #--run=blind
	sleep 1s
	mv higgsCombine${label}.AsymptoticLimits.mH125.root Models_Tprime${i}
	sleep 1s
#	combine Models_Tprime${i}/Datacard_Tprime${i}${label}\.root -M MultiDimFit -m 125 --redefineSignalPOIs r --freezeParameter MH -t -1 --setParameters r=1. --saveWorkspace --cminDefaultMinimizerStrategy 0 -n ${label}
#	sleep 1s
#	mv higgsCombine${label}.MultiDimFit.mH125.root Models_Tprime${i}

#####--------------------------------------------Hadronic---------------------------------------------
#    cp ../Datacard/Datacard_Had/Datacard_Tprime${i}_Had${label}\.txt Models_Tprime${i}_Had/
#	sleep 1s
	text2workspace.py Models_Tprime${i}_Had/Datacard_Tprime${i}_Had${label}\.txt
	sleep 1s
    combine Models_Tprime${i}_Had/Datacard_Tprime${i}_Had${label}\.root -M AsymptoticLimits -m 125 --redefineSignalPOIs r --trackParameters r --freezeParameter MH --saveWorkspace --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 -n _Had${label} --run=blind
   	sleep 3s
    mv higgsCombine_Had${label}.AsymptoticLimits.mH125.root Models_Tprime${i}_Had/
    sleep 1s

#####--------------------------------------------Leptonic---------------------------------------------
#    cp ../Datacard/Datacard_Lep/Datacard_Tprime${i}_Lep${label}\.txt Models_Tprime${i}_Lep/
#	sleep 1s
	text2workspace.py Models_Tprime${i}_Lep/Datacard_Tprime${i}_Lep${label}\.txt
    sleep 1s
	combine Models_Tprime${i}_Lep/Datacard_Tprime${i}_Lep${label}\.root -M AsymptoticLimits -m 125 --redefineSignalPOIs r --trackParameters r --freezeParameter MH --saveWorkspace --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 -n _Lep${label} --run=blind
	sleep 1s
    mv higgsCombine_Lep${label}.AsymptoticLimits.mH125.root Models_Tprime${i}_Lep
    sleep 1s
done
