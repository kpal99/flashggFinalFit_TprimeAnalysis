#!/bin/bash
INPUTDIR="/eos/user/p/prsaha/Tprime_analysis/FinalFit_inputs/UL/v2_CR2"
	echo $INPUTDIR
	echo "Running------------------MASS:$mass----------------------------------------"
	echo ""
	echo ""
	echo "python RunPackager.py --cats THQLeptonicTag,THQHadronicTag --exts HiggsCR_2016,HiggsCR_2017,HiggsCR_2018 --mergeYears --printOnly --batch condor --queue espresso --massPoints 125 --outputExt packaged_HiggsCR"
	python RunPackager.py --cats THQLeptonicTag,THQHadronicTag --exts HiggsCR_2016,HiggsCR_2017,HiggsCR_2018 --mergeYears --batch condor --queue espresso --massPoints 125 --outputExt packaged_HiggsCR #--printOnly
	echo ""
	echo ""
