#!/bin/bash
INPUTDIR="/eos/user/p/prsaha/Tprime_analysis/FinalFit_inputs/UL/v2"
echo $INPUTDIR
	for mass in 600 625 650 675 700 800 900 1000 1100 1200
	do 
	echo "Running------------------MASS:$mass----------------------------------------"
	echo ""
	echo ""
	echo "python RunPackager.py --cats THQLeptonicTag,THQHadronicTag --exts Tprime${mass}_2016,Tprime${mass}_2017,Tprime${mass}_2018 --mergeYears --printOnly --batch condor --queue espresso --massPoints 125 --outputExt packaged_Tprime${mass}"
	python RunPackager.py --cats THQLeptonicTag,THQHadronicTag --exts Tprime${mass}_2016,Tprime${mass}_2017,Tprime${mass}_2018 --mergeYears --batch condor --queue espresso --massPoints 125 --outputExt packaged_Tprime${mass} #--printOnly
        echo ""
        echo ""
	done
