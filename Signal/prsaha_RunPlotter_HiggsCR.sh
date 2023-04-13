#!/bin/bash
INPUTDIR="/eos/user/p/prsaha/Tprime_analysis/FinalFit_inputs/UL/v2_CR2"
PlotDIR="/eos/user/p/prsaha/www/Tprime_analysis/Finalfit_Lite_output/UL/result_v2_CR2"
echo $INPUTDIR
        echo ""
        echo ""
		for proc in THQ TTH GG2H VBF VH
		do
        	echo "python RunPlotter.py --procs $proc --years 2016,2017,2018 --cats THQLeptonicTag --ext packaged_HiggsCR"
        	#python RunPackager.py --cats THQLeptonicTag,THQHardonicTag --exts Tprime${mass}_2016,Tprime${mass}_2017,Tprime${mass}_2018 --mergeYears --batch condor --queue espresso --massPoints 125 --outputExt packaged_Tprime${mass} #--printOnly
        	python RunPlotter.py --procs ${proc} --years 2016,2017,2018 --cats THQLeptonicTag --ext packaged_HiggsCR
        	echo ""
        	echo ""
        	echo "python RunPlotter.py --procs ${proc} --years 2016,2017,2018 --cats THQHadronicTag --ext packaged_HiggsCR"
        	python RunPlotter.py --procs ${proc} --years 2016,2017,2018 --cats THQHadronicTag --ext packaged_HiggsCR
		done
        	echo ""
        	echo ""
		mkdir ${PlotDIR}/outdir_packaged_HiggsCR
		cp ${PlotDIR}/index.php ${PlotDIR}/outdir_packaged_HiggsCR
		cp -r outdir_packaged_HiggsCR/Plots ${PlotDIR}/outdir_packaged_HiggsCR/ 
		cp ${PlotDIR}/outdir_packaged_HiggsCR/index.php ${PlotDIR}/outdir_packaged_HiggsCR/Plots/
