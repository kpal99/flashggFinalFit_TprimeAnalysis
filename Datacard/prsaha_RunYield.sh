#!/bin/bash

#export i=$1
INPUTDIR="/eos/user/p/prsaha/Tprime_analysis/FinalFit_inputs/UL/v2"
for mass in 600 625 650 675 700 800 900 1000 1100 1200
do 
        echo "Running------------------YEAR:$year MASS:$mass----------------------------------------"
        echo ""
        echo ""
	python RunYields.py --ext Tprime${mass} --sigModelExt packaged_Tprime${mass} --sigModelWSDir ./Models_Tprime${mass}/signal --bkgModelWSDir ./Models_Tprime${mass}/background --cats THQHadronicTag,THQLeptonicTag --inputWSDirMap 2016=${INPUTDIR}/$mass/2016,2017=${INPUTDIR}/$mass/2017,2018=${INPUTDIR}/$mass/2018 --mergeYears --procs Tprime${mass},TTH,THQ,VBF,GG2H,VH --batch condor --queue longlunch --doSystematics #--printOnly
#	python RunYields.py --ext Tprime${mass} --sigModelExt packaged_Tprime${mass} --sigModelWSDir ./Models_Tprime${mass}/signal --bkgModelWSDir ./Models_Tprime${mass}/background --cats THQHadronicTag,THQLeptonicTag --inputWSDirMap 2016=${INPUTDIR}/$mass/2016,2017=${INPUTDIR}/$mass/2017,2018=${INPUTDIR}/$mass/2018 --mergeYears --procs Tprime${mass} --batch condor --queue longlunch --doSystematics
        echo ""
        echo ""
done
