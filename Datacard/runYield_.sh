#!/bin/bash

RUN=true
MKDIR=false
RUNCREATEDSCRIPTS=false
# get the options passed to the script
while getopts "mnrh" opt;
do
case $opt in
    m) MKDIR=true;;
    n) RUN=false;;
    r) RUNCREATEDSCRIPTS=true;;
    h) echo "Usage: $0 [-m] [-n] [-r]"
       echo "  -h: print this help"
       echo "  -m: create required directories for fTest"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -r: run final scripts which are found in yields_*"
       exit 0;;
    \?) exit ;;
esac
done

WSDIR=/eos/user/k/kpal/tprime_ww/ws_2018
export PYTHONPATH=$PYTHONPATH:$CMSSW_BASE/src/flashggFinalFit/tools:$CMSSW_BASE/src/flashggFinalFit/Signal/tools
for m in {7,10,14,20,24}00
do
    for d in 10 30
    do
        if $MKDIR; then
            echo python RunYields.py --inputWSDirMap 2018=$WSDIR --ext TprimeM"$m"Decay"$d"pctSch --sigModelWSDir ./models/TprimeM"$m"Decay"$d"pctSch --bkgModelWSDir ./models/background --cats auto --procs TprimeM"$m"Decay"$d"pctSch,VBF,TTH --mergeYears --batch condor --queue espresso --printOnly
            # procs = all higgs background
            if $RUN; then
                python RunYields.py --inputWSDirMap 2018=$WSDIR --ext TprimeM"$m"Decay"$d"pctSch --sigModelWSDir ./models/TprimeM"$m"Decay"$d"pctSch --bkgModelWSDir ./models/background --cats auto --procs TprimeM"$m"Decay"$d"pctSch,VBF,TTH --mergeYears --batch condor --queue espresso --printOnly
                echo   # to add new line after output of above script
            fi
        fi
        if $RUNCREATEDSCRIPTS; then
            for cat in THQLeptonicTag THQHadronicTag
            do
                echo python makeYields.py --cat $cat --procs TprimeM"$m"Decay"$d"pctSch,VBF,TTH --ext TprimeM"$m"Decay"$d"pctSch --mass 125 --inputWSDirMap 2018=$WSDIR --sigModelWSDir ./models/TprimeM"$m"Decay"$d"pctSch --sigModelExt packaged_TprimeM"$m"Decay"$d"pctSch --bkgModelWSDir ./models/background --bkgModelExt multipdf --mergeYears
                if $RUN; then
                    python makeYields.py --cat $cat --procs TprimeM"$m"Decay"$d"pctSch,VBF,TTH --ext TprimeM"$m"Decay"$d"pctSch --mass 125 --inputWSDirMap 2018=$WSDIR --sigModelWSDir ./models/TprimeM"$m"Decay"$d"pctSch --sigModelExt packaged_TprimeM"$m"Decay"$d"pctSch --bkgModelWSDir ./models/background --bkgModelExt multipdf --mergeYears
                    echo   # to add new line after output of above script
                fi
            done
        fi
    done
done
