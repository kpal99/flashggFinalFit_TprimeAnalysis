#!/bin/bash
INPUTDIR="/eos/user/p/prsaha/Tprime_analysis/FinalFit_inputs/UL/v2_CR2/"
EXT=""
echo $INPUTDIR
for year in 2016 2017 2018
do
#	for mass in 600 #625 650 675 700 800 900 1000 1100 1200
#	do 
	echo "Running------------------YEAR:$year----------------------------------------"
	echo ""
	echo ""
	echo "python RunSignalScripts.py --inputConfig config_Tprime.py --mode signalFit --inputWSDir $INPUTDIR/$year --ext HiggsCR_${year} --year $year --analysis Tprime_600 --modeOpts "--nProcsToFTest -1 --doPlots""
#   	python RunSignalScripts.py --inputConfig config_Tprime.py --mode calcPhotonSyst --inputWSDir $INPUTDIR/$mass/$year --ext HiggsCR_${year} --year $year --analysis Tprime_600 --procs TTH,THQ,VBF,GG2H,VH

	python RunSignalScripts.py --inputConfig config_Tprime.py --mode signalFit --inputWSDir $INPUTDIR/$year --ext HiggsCR_${year} --year $year --analysis Tprime_600 --procs TTH,THQ,VBF,GG2H,VH --groupSignalFitJobsByCat --modeOpts "--skipVertexScenarioSplit --doPlots" #--replacementThreshold 50 #--printOnly
        echo ""
        echo ""
	done
#done
