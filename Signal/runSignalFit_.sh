#!/bin/bash

RUN=true
MKDIR=false
RUNCREATEDSCRIPTS=false
# get the options passed to the script
while getopts "mnsh" opt;
do
case $opt in
    m) MKDIR=true;;
    n) RUN=false;;
    s) RUNCREATEDSCRIPTS=true;;
    h) echo "Usage: $0 [-m] [-n] [-s]"
       echo "  -m: create required directories for signalFit"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -s: run final scripts which are found in outdir_*"
       exit 0;;
    \?) exit ;;
esac
done

INPUTDIR=/eos/user/k/kpal/tprime_ww/test1_tprime/storeChanged
export PYTHONPATH=$PYTHONPATH:$CMSSW_BASE/src/flashggFinalFit/tools:$CMSSW_BASE/src/flashggFinalFit/Signal/tools
for m in {7,10,14,20,24}00
do
    for d in 10 30
    do
        if $MKDIR; then
            echo python RunSignalScripts.py --inputConfig config_Tprime.py --mode signalFit --inputWSDir $INPUTDIR/ws_TprimeM"$m"Decay"$d"pctSch  --ext TprimeM"$m"Decay"$d"pctSch --year 2018 --analysis TprimeM"$m"Decay"$d"pctSch --procs TprimeM"$m"Decay"$d"pctSch --printOnly --modeOpts '"--skipVertexScenarioSplit --doPlots --skipSystematics"'
            if $RUN; then
                python RunSignalScripts.py --inputConfig config_Tprime.py --mode signalFit --inputWSDir $INPUTDIR/ws_TprimeM"$m"Decay"$d"pctSch  --ext TprimeM"$m"Decay"$d"pctSch --year 2018 --analysis TprimeM"$m"Decay"$d"pctSch --procs TprimeM"$m"Decay"$d"pctSch --printOnly --modeOpts '"--skipVertexScenarioSplit --doPlots --skipSystematics"'
                echo   # to add new line after output of above script
            fi
        fi
        if $RUNCREATEDSCRIPTS; then
            for cat in THQLeptonicTag THQHadronicTag
            do
                echo python scripts/signalFit.py --inputWSDir $INPUTDIR/ws_TprimeM"$m"Decay"$d"pctSch --ext TprimeM"$m"Decay"$d"pctSch --proc TprimeM"$m"Decay"$d"pctSch --cat $cat --year 2018 --analysis TprimeM"$m"Decay"$d"pctSch --massPoints 125 --scales '"HighR9EB,HighR9EE,LowR9EB,LowR9EE,Gain1EB,Gain6EB"' --scalesCorr '"MaterialCentralBarrel,MaterialOuterBarrel,MaterialForward,FNUFEE,FNUFEB,ShowerShapeHighR9EE,ShowerShapeHighR9EB,ShowerShapeLowR9EE,ShowerShapeLowR9EB"' --scalesGlobal '"NonLinearity,Geant4"' --smears '"HighR9EBPhi,HighR9EBRho,HighR9EEPhi,HighR9EERho,LowR9EBPhi,LowR9EBRho,LowR9EEPhi,LowR9EERho"' --skipVertexScenarioSplit --doPlots --skipSystematics
                if $RUN; then
                    python scripts/signalFit.py --inputWSDir $INPUTDIR/ws_TprimeM"$m"Decay"$d"pctSch --ext TprimeM"$m"Decay"$d"pctSch --proc TprimeM"$m"Decay"$d"pctSch --cat $cat --year 2018 --analysis TprimeM"$m"Decay"$d"pctSch --massPoints 125 --scales '"HighR9EB,HighR9EE,LowR9EB,LowR9EE,Gain1EB,Gain6EB"' --scalesCorr '"MaterialCentralBarrel,MaterialOuterBarrel,MaterialForward,FNUFEE,FNUFEB,ShowerShapeHighR9EE,ShowerShapeHighR9EB,ShowerShapeLowR9EE,ShowerShapeLowR9EB"' --scalesGlobal '"NonLinearity,Geant4"' --smears '"HighR9EBPhi,HighR9EBRho,HighR9EEPhi,HighR9EERho,LowR9EBPhi,LowR9EBRho,LowR9EEPhi,LowR9EERho"' --skipVertexScenarioSplit --doPlots --skipSystematics
                    # these variables inside "" are controlled by config_Tprime.py, if you change the config file
                    # then change these lines by looking at output_*/signalFit/jobs/*.sh
                    echo   # to add new line after output of above script
                fi
            done
        fi
    done
done
