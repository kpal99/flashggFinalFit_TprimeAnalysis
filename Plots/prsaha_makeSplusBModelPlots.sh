for i in 625 650 675 700 800 900 1000 1100 1200 #600
do
#   python RunText2Workspace.py --mode AsymptoticLimits --ext _Tprime600 --batch condor --queue workday
	python makeSplusBModelPlot.py --inputWSFile ../Combine/result_UL_v2/Models_Tprime${i}/higgsCombine_Syst.MultiDimFit.mH125.root --cats all --loadSnapshot MultiDimFit --doZeroes --ext _Tprime${i} --doSumCategories --unblind --doBands --Tmass ${i} #--unblind 
    sleep 1s
#    python makeSplusBModelPlot.py --inputWSFile ../Combine/result_UL_v2/Models_Tprime${i}_Had/higgsCombine_Had_Syst.MultiDimFit.mH125.root --cats THQHadronicTag --loadSnapshot MultiDimFit --doZeroes --ext _Tprime${i}_Had --doSumCategories --unblind #--doBands --unblind #--doBands
	sleep 1s
#	python makeSplusBModelPlot.py --inputWSFile ../Combine/result_UL_v2/Models_Tprime${i}_Lep/higgsCombine_Lep_Syst.MultiDimFit.mH125.root --cats THQLeptonicTag --loadSnapshot MultiDimFit --doZeroes --ext _Tprime${i}_Lep --doSumCategories --unblind #--doBands --unblind #--doBands
done
