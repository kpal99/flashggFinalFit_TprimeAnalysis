#!/bin/bash
INPUTDIR="/eos/user/p/prsaha/Tprime_analysis/FinalFit_inputs/UL/v2"
PlotDIR="/eos/user/p/prsaha/www/Tprime_analysis/Finalfit_Lite_output/UL/result_v2_"
echo $INPUTDIR
        for mass in 600 625 650 675 700 800 900 1000 1100 1200
        do
        echo "Running------------------MASS:$mass----------------------------------------"
        echo ""
        echo ""
		for proc in Tprime${mass} THQ TTH GG2H VBF VH
		do
        	echo "python RunPlotter.py --procs $proc --years 2016,2017,2018 --cats THQLeptonicTag --ext packaged_Tprime${mass}"
        	#python RunPackager.py --cats THQLeptonicTag,THQHardonicTag --exts Tprime${mass}_2016,Tprime${mass}_2017,Tprime${mass}_2018 --mergeYears --batch condor --queue espresso --massPoints 125 --outputExt packaged_Tprime${mass} #--printOnly
        	python RunPlotter.py --procs $proc --years 2016,2017,2018 --cats THQLeptonicTag --ext packaged_Tprime${mass}
        	echo ""
        	echo ""
        	echo "python RunPlotter.py --procs $proc --years 2016,2017,2018 --cats THQHadronicTag --ext packaged_Tprime${mass}"
        	python RunPlotter.py --procs ${proc} --years 2016,2017,2018 --cats THQHadronicTag --ext packaged_Tprime${mass}
		done
        	echo ""
        	echo ""
		mkdir ${PlotDIR}/outdir_packaged_Tprime${mass}
		cp ${PlotDIR}/index.php ${PlotDIR}/outdir_packaged_Tprime${mass}
		cp -r outdir_packaged_Tprime${mass}/Plots ${PlotDIR}/outdir_packaged_Tprime${mass}/ 
		cp ${PlotDIR}/outdir_packaged_Tprime${mass}/index.php ${PlotDIR}/outdir_packaged_Tprime${mass}/Plots/
        done
