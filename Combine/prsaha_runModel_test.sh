#!/bin/bash
#label=_StatOnly
label=_Syst

echo "Running combine---------"

for i in 600 625 650 675 700 #800 900 1000 1100 1200
do

	combine Models_Tprime${i}/Datacard_Tprime${i}${label}\.root -M AsymptoticLimits -m 125 --redefineSignalPOIs r --trackParameters r --saveWorkspace --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 -n ${label} --freezeParameter MH #--setParameterRanges MH=115,135 #--freezeParameter MH #--run=blind #-t -1 --expectSignal 1 
#	combine Datacard_Tprime$i.txt -M AsymptoticLimits -m 125 -P --PO "map=.*/tHq.*:r_tHq[1,0,10]" --PO "map=.*/ttH.*:r_ttH[1,0,10]" --redefineSignalPOIs r_tHq --trackParameters r_tHq,r_ttH --freezeParameter MH --run=blind -t -1
#	combine Datacard_Tprime${i}_AsymptoticLimits.root -M AsymptoticLimits -m 125 --redefineSignalPOIs r_Tvlq --setParameters r_tHq=1,r_ttH=1,r_qqH=1,r_ggH=1 --freezeParameter MH,r_tHq,r_ttH,r_qqH,r_ggH -t -1 #--run=blind
	sleep 1s
	mv higgsCombine${label}.AsymptoticLimits.mH125.root Models_Tprime${i}
	sleep 1s
	combine Models_Tprime${i}/Datacard_Tprime${i}${label}\.root -M MultiDimFit -m 125 --redefineSignalPOIs r --freezeParameter MH --saveWorkspace --cminDefaultMinimizerStrategy 0 -n ${label}
#	combine Models_Tprime${i}/Datacard_Tprime${i}${label}\.root -M MultiDimFit -m 125 --redefineSignalPOIs r --saveWorkspace --cminDefaultMinimizerStrategy 0 -n ${label} --freezeParameter MH #--setParameterRanges MH=115,135 
#	sleep 1s
	mv higgsCombine${label}.MultiDimFit.mH125.root Models_Tprime${i}

#####--------------------------------------------Hadronic---------------------------------------------
    combine Models_Tprime${i}_Had/Datacard_Tprime${i}_Had${label}\.root -M AsymptoticLimits -m 125 --redefineSignalPOIs r --trackParameters r --saveWorkspace --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 -n _Had${label} --freezeParameter MH #--setParameterRanges MH=115,135 #--freezeParameter MH #--run=blind
   	sleep 1s
    mv higgsCombine_Had${label}.AsymptoticLimits.mH125.root Models_Tprime${i}_Had/
    sleep 1s
    combine Models_Tprime${i}_Had/Datacard_Tprime${i}_Had${label}\.root -M MultiDimFit -m 125 --redefineSignalPOIs r --saveWorkspace --cminDefaultMinimizerStrategy 0 -n _Had${label} --freezeParameter MH #--setParameterRanges MH=115,135

	sleep 1s
	mv higgsCombine_Had${label}.MultiDimFit.mH125.root Models_Tprime${i}_Had
#####--------------------------------------------Leptonic---------------------------------------------
	combine Models_Tprime${i}_Lep/Datacard_Tprime${i}_Lep${label}\.root -M AsymptoticLimits -m 125 --redefineSignalPOIs r --trackParameters r --saveWorkspace --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 -n _Lep${label} --freezeParameter MH #--setParameterRanges MH=115,135 #--freezeParameter MH #--run=blind	sleep 1s
	sleep 1s
    mv higgsCombine_Lep${label}.AsymptoticLimits.mH125.root Models_Tprime${i}_Lep
    sleep 1s
	combine Models_Tprime${i}_Lep/Datacard_Tprime${i}_Lep${label}\.root -M MultiDimFit -m 125 --redefineSignalPOIs r --saveWorkspace --cminDefaultMinimizerStrategy 0 -n _Lep${label} --freezeParameter MH #--setParameterRanges MH=115,135
	sleep 1s
	mv higgsCombine_Lep${label}.MultiDimFit.mH125.root Models_Tprime${i}_Lep
done
