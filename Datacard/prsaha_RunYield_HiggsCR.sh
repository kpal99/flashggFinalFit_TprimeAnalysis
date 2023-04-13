#!/bin/bash

#export i=$1
INPUTDIR="/eos/user/p/prsaha/Tprime_analysis/FinalFit_inputs/UL/v2_CR2"
        echo "Running------------------YEAR:$year MASS:$mass----------------------------------------"
        echo ""
        echo ""
	python RunYields.py --ext HiggsCR --sigModelExt packaged_HiggsCR --sigModelWSDir ./Models_HiggsCR/signal --bkgModelWSDir ./Models_HiggsCR/background --cats THQHadronicTag,THQLeptonicTag --inputWSDirMap 2016=${INPUTDIR}/2016,2017=${INPUTDIR}/2017,2018=${INPUTDIR}/2018 --mergeYears --procs TTH,THQ,VBF,GG2H,VH --batch condor --queue longlunch --doSystematics #--printOnly
        echo ""
        echo ""
