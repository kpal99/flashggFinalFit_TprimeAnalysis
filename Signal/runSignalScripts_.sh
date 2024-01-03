for m in {7,10,14,20,24}00; for d in 10 30; python RunSignalScripts.py --inputConfig config_Tprime.py --mode signalFit --inputWSDir ~eos/tprime_ww/test1_tprime/storeChanged/ws_TprimeM"$m"Decay"$d"pctSch  --ext TprimeM"$m"Decay"$d"pctSch --year 2018 --analysis TprimeM"$m"Decay"$d"pctSch --procs TprimeM"$m"Decay"$d"pctSch --printOnly --modeOpts "--skipVertexScenarioSplit --doPlots --skipSystematics"


