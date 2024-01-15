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
for i in GG2H VBF TTH
do
    if $MKDIR; then
        echo python RunSignalScripts.py --inputConfig config_Tprime.py --mode fTest --inputWSDir $INPUTDIR/ws_$i  --ext $i --year 2018 --analysis $i --procs $i --modeOpts --skipWV '"--nProcsToFTest -1 --doPlots"' --printOnly
        if $RUN; then
            python RunSignalScripts.py --inputConfig config_Tprime.py --mode fTest --inputWSDir $INPUTDIR/ws_$i  --ext $i --year 2018 --analysis $i --procs $i --modeOpts --skipWV '"--nProcsToFTest -1 --doPlots"' --printOnly
            echo   # to add new line after output of above script
        fi
    fi
    if $RUNCREATEDSCRIPTS; then
        for cat in THQLeptonicTag THQHadronicTag
        do
            echo python scripts/fTest.py --cat $cat --procs $i --ext $i --inputWSDir $INPUTDIR/ws_$i --skipWV --nProcsToFTest -1 --doPlots --threshold 10
            if $RUN; then
                python scripts/fTest.py --cat $cat --procs $i --ext $i --inputWSDir $INPUTDIR/ws_$i --skipWV --nProcsToFTest -1 --doPlots  --threshold 10
                # this threshould is 10 just for running the chain, will remove later
                echo   # to add new line after output of above script
            fi
        done
    fi
done
