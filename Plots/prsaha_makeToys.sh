for i in 675 700 800 900 1000 1100 1200
do
#   python RunText2Workspace.py --mode AsymptoticLimits --ext _Tprime600 --batch condor --queue workday

	python makeToys.py --inputWSFile ../Combine/result_UL_v2/Models_Tprime${i}_Had/higgsCombine_Had_Syst.MultiDimFit.mH125.root --loadSnapshot MultiDimFit --ext _Tprime${i}_Had --batch 'condor' --nToys 500
#	python makeToys.py --inputWSFile ../Combine/result_UL_v2/Models_Tprime${i}_Lep/higgsCombine_Lep_Syst.MultiDimFit.mH125.root --loadSnapshot MultiDimFit --ext _Tprime${i}_Lep --batch 'condor' --nToys 500
    sleep 1s
done
