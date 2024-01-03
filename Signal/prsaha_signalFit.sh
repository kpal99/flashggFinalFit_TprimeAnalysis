#!/bin/bash
INPUTDIR="/eos/user/p/prsaha/Tprime_analysis/FinalFit_inputs/UL/v2"
EXT=""
echo $INPUTDIR
for year in 2018
do
	for mass in 700 800 900 1000 1100 1200
	do
	echo "Running------------------YEAR:$year MASS:$mass----------------------------------------"
	#echo ""
	#echo ""
	echo "python RunSignalScripts.py --inputConfig config_Tprime.py --mode fTest --inputWSDir $INPUTDIR/$mass/$year --ext Tprime${mass}_${year} --year $year --analysis Tprime_$mass --modeOpts "--nProcsToFTest -1 --doPlots""
#	python RunSignalScripts.py --inputConfig config_Tprime.py --mode calcPhotonSyst --inputWSDir $INPUTDIR/$mass/$year --ext Tprime${mass}_${year} --year $year --analysis Tprime_$mass --procs Tprime${mass},TTH,THQ,VBF,GG2H,VH
	#python RunSignalScripts.py --inputConfig config_Tprime.py --mode signalFit --inputWSDir $INPUTDIR/$mass/$year --ext Tprime${mass}_${year} --year $year --analysis Tprime_$mass --procs Tprime${mass},TTH,THQ,VBF,GG2H,VH --modeOpts "--skipVertexScenarioSplit --doPlots" #--replacementThreshold 50 #--printOnly
#   python RunSignalScripts.py --inputConfig config_Tprime.py --mode signalFit --inputWSDir $INPUTDIR/$mass/$year --ext Tprime${mass}_${year} --year $year --analysis Tprime_$mass --procs Tprime${mass} --modeOpts "--skipVertexScenarioSplit --doPlots"
#    python RunSignalScripts.py --inputConfig config_Tprime.py --mode calcPhotonSyst --inputWSDir $INPUTDIR/$mass/$year --ext Tprime${mass}_${year} --year $year --analysis Tprime_$mass --procs Tprime${mass} #--modeOpts "--skipVertexScenarioSplit --doPlots" #--replacementThreshold 50 #--printOnly
#    python RunSignalScripts.py --inputConfig config_Tprime.py --mode signalFit --inputWSDir $INPUTDIR/$mass/$year --ext Tprime${mass}_${year} --year $year --analysis Tprime_$mass --procs Tprime${mass} --modeOpts "--skipVertexScenarioSplit --doPlots" #--replacementThreshold 50 #--printOnly
        echo ""
        echo ""
	done
done
