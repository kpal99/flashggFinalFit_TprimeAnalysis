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

INPUTDIR=/eos/user/k/kpal/tprime_ww/test1_tprime/storeChanged
export PYTHONPATH=$PYTHONPATH:$CMSSW_BASE/src/flashggFinalFit/tools:$CMSSW_BASE/src/flashggFinalFit/Signal/tools
for m in {7,10,14,20,24}00
do
    for d in 10 30
    do
        if $MKDIR; then
            echo python RunSignalScripts.py --inputConfig config_Tprime.py --mode fTest --inputWSDir $INPUTDIR/ws_TprimeM"$m"Decay"$d"pctSch  --ext TprimeM"$m"Decay"$d"pctSch --year 2018 --analysis TprimeM"$m" --procs TprimeM"$m"Decay"$d"pctSch --modeOpts --nProcsToFTest -1 --doPlots --printOnly
            if $RUN; then
                python RunSignalScripts.py --inputConfig config_Tprime.py --mode fTest --inputWSDir $INPUTDIR/ws_TprimeM"$m"Decay"$d"pctSch  --ext TprimeM"$m"Decay"$d"pctSch --year 2018 --analysis TprimeM"$m" --procs TprimeM"$m"Decay"$d"pctSch --modeOpts --nProcsToFTest -1 --doPlots --printOnly
                echo   # to add new line after output of above script
            fi
        fi
        if $RUNCREATEDSCRIPTS; then
            for cat in THQLeptonicTag THQHadronicTag
            do
                echo python $PWD/scripts/fTest.py --cat $cat --procs TprimeM"$m"Decay"$d"pctSch --ext TprimeM"$m"Decay"$d"pctSch --inputWSDir $INPUTDIR/ws_TprimeM"$m"Decay"$d"pctSch --nProcsToFTest -1 --doPlots
                if $RUN; then
                    python $PWD/scripts/fTest.py --cat $cat --procs TprimeM"$m"Decay"$d"pctSch --ext TprimeM"$m"Decay"$d"pctSch --inputWSDir $INPUTDIR/ws_TprimeM"$m"Decay"$d"pctSch --nProcsToFTest -1 --doPlots
                    echo   # to add new line after output of above script
                fi
            done
        fi
    done
done
