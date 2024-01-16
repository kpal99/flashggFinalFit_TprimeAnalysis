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
       echo "  -m: create required directories for packaging"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -s: run final Scripts which are found in outdir_*"
       exit 0;;
    \?) exit ;;
esac
done

export PYTHONPATH=$PYTHONPATH:$CMSSW_BASE/src/flashggFinalFit/tools:$CMSSW_BASE/src/flashggFinalFit/Signal/tools
for m in {7,10,14,20,24}00
do
    for d in 10 30
    do
        if $MKDIR; then
            echo python RunPackager.py --cats THQLeptonicTag,THQHadronicTag --exts TprimeM"$m"Decay"$d"pctSch --mergeYears --batch condor --queue espresso --massPoints 125 --outputExt packaged_TprimeM"$m"Decay"$d"pctSch --printOnly
            if $RUN; then
                python RunPackager.py --cats THQLeptonicTag,THQHadronicTag --exts TprimeM"$m"Decay"$d"pctSch --mergeYears --batch condor --queue espresso --massPoints 125 --outputExt packaged_TprimeM"$m"Decay"$d"pctSch --printOnly
                echo   # to add new line after output of above script
            fi
        fi
        if $RUNCREATEDSCRIPTS; then
            for cat in THQLeptonicTag THQHadronicTag
            do
                echo python scripts/packageSignal.py --cat $cat --outputExt packaged_TprimeM"$m"Decay"$d"pctSch --massPoints 125 --exts TprimeM"$m"Decay"$d"pctSch --mergeYears
                if $RUN; then
                    python scripts/packageSignal.py --cat $cat --outputExt packaged_TprimeM"$m"Decay"$d"pctSch --massPoints 125 --exts TprimeM"$m"Decay"$d"pctSch --mergeYears
                    echo   # to add new line after output of above script
                fi
            done
        fi
    done
done
