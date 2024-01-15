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

INPUTDIR=/eos/user/k/kpal/tprime_ww/full1_bkg_h/storeChanged
export PYTHONPATH=$PYTHONPATH:$CMSSW_BASE/src/flashggFinalFit/tools:$CMSSW_BASE/src/flashggFinalFit/Signal/tools
for i in VBF TTH GG2H
do
    if $MKDIR; then
        echo python RunSignalScripts.py --inputConfig config_Tprime.py --mode fTest --inputWSDir $INPUTDIR/ws_$i  --ext $i --year 2018 --analysis Tprime --procs $i --modeOpts --nProcsToFTest -1 --doPlots --printOnly
        if $RUN; then
            python RunSignalScripts.py --inputConfig config_Tprime.py --mode fTest --inputWSDir $INPUTDIR/ws_$i  --ext $i --year 2018 --analysis Tprime --procs $i --modeOpts --nProcsToFTest -1 --doPlots --printOnly
            echo   # to add new line after output of above script
        fi
    fi
    if $RUNCREATEDSCRIPTS; then
        for cat in THQLeptonicTag THQHadronicTag
        do
            echo python $PWD/scripts/fTest.py --cat $cat --procs $i --ext $i --inputWSDir $INPUTDIR/ws_$i --nProcsToFTest -1 --doPlots
            if $RUN; then
                python $PWD/scripts/fTest.py --cat $cat --procs $i --ext $i --inputWSDir $INPUTDIR/ws_$i --nProcsToFTest -1 --doPlots
                echo   # to add new line after output of above script
            fi
        done
    fi
done
