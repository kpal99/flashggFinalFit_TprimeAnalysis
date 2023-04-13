#!/bin/bash

for i in 600 625 650 675 700 800 900 1000 1100 1200
do
	python makeGoFPlot.py --inputFiletoysFit result_UL_v2/Models_Tprime${i}/GoF_b/higgsCombine_GoFtest_For500toys.GoodnessOfFit.mH125.123456.root --ext Tprime${i} --inputFileDataFit result_UL_v2/Models_Tprime${i}/GoF_b/higgsCombine_GoFtest_ForData.GoodnessOfFit.mH125.root
done
