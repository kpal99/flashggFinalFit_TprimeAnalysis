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
       echo "  -m: create required directories for fTest"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -s: run final scripts which are found in outdir_*"
       exit 0;;
    \?) exit ;;
esac
done

# for --skipWV, see
# https://github.com/cms-analysis/flashggFinalFit/blob/dev_fggfinalfits_lite/Signal/README.md?plain=1#L37
INPUTDIR=/eos/user/k/kpal/tprime_ww/full1_bkg_h/storeChanged
export PYTHONPATH=$PYTHONPATH:$CMSSW_BASE/src/flashggFinalFit/tools:$CMSSW_BASE/src/flashggFinalFit/Signal/tools
for i in VBF TTH #GG2H , since GG2H interal is negative
do
    if $MKDIR; then
        echo python RunSignalScripts.py --inputConfig config_Tprime.py --mode signalFit --inputWSDir $INPUTDIR/ws_$i  --ext $i --year 2018 --analysis $i --procs $i --printOnly --modeOpts '"--skipVertexScenarioSplit --doPlots --skipSystematics"'
        if $RUN; then
            python RunSignalScripts.py --inputConfig config_Tprime.py --mode signalFit --inputWSDir $INPUTDIR/ws_$i  --ext $i --year 2018 --analysis $i --procs $i --printOnly --modeOpts '"--skipVertexScenarioSplit --doPlots --skipSystematics"'
            echo   # to add new line after output of above script
        fi
    fi
    if $RUNCREATEDSCRIPTS; then
        for cat in THQLeptonicTag THQHadronicTag
        do
            echo python scripts/signalFit.py --inputWSDir $INPUTDIR/ws_$i --ext $i --proc $i --cat $cat --year 2018 --analysis $i --massPoints 125 --scales '"HighR9EB,HighR9EE,LowR9EB,LowR9EE,Gain1EB,Gain6EB"' --scalesCorr '"MaterialCentralBarrel,MaterialOuterBarrel,MaterialForward,FNUFEE,FNUFEB,ShowerShapeHighR9EE,ShowerShapeHighR9EB,ShowerShapeLowR9EE,ShowerShapeLowR9EB"' --scalesGlobal '"NonLinearity,Geant4"' --smears '"HighR9EBPhi,HighR9EBRho,HighR9EEPhi,HighR9EERho,LowR9EBPhi,LowR9EBRho,LowR9EEPhi,LowR9EERho"' --skipVertexScenarioSplit --doPlots --skipSystematics --replacementThreshold 10
            if $RUN; then
                python scripts/signalFit.py --inputWSDir $INPUTDIR/ws_$i --ext $i --proc $i --cat $cat --year 2018 --analysis $i --massPoints 125 --scales '"HighR9EB,HighR9EE,LowR9EB,LowR9EE,Gain1EB,Gain6EB"' --scalesCorr '"MaterialCentralBarrel,MaterialOuterBarrel,MaterialForward,FNUFEE,FNUFEB,ShowerShapeHighR9EE,ShowerShapeHighR9EB,ShowerShapeLowR9EE,ShowerShapeLowR9EB"' --scalesGlobal '"NonLinearity,Geant4"' --smears '"HighR9EBPhi,HighR9EBRho,HighR9EEPhi,HighR9EERho,LowR9EBPhi,LowR9EBRho,LowR9EEPhi,LowR9EERho"' --skipVertexScenarioSplit --doPlots --skipSystematics --replacementThreshold 10
                echo   # to add new line after output of above script
            fi
        done
    fi
done

