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
       echo "  -m: create required directories for packaging"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -r: run final scripts which are found in outdir_*"
       exit 0;;
    \?) exit ;;
esac
done

export PYTHONPATH=$PYTHONPATH:$CMSSW_BASE/src/flashggFinalFit/tools:$CMSSW_BASE/src/flashggFinalFit/Signal/tools
for i in VBF TTH #GG2H , since GG2H interal is negative
do
    if $MKDIR; then
        echo python RunPackager.py --cats THQLeptonicTag,THQHadronicTag --exts $i --mergeYears --batch condor --queue espresso --massPoints 125 --outputExt packaged_$i --printOnly
        if $RUN; then
            python RunPackager.py --cats THQLeptonicTag,THQHadronicTag --exts $i --mergeYears --batch condor --queue espresso --massPoints 125 --outputExt packaged_$i --printOnly
            echo   # to add new line after output of above script
        fi
    fi
    if $RUNCREATEDSCRIPTS; then
        for cat in THQLeptonicTag THQHadronicTag
        do
            echo python scripts/packageSignal.py --cat $cat --outputExt packaged_$i --massPoints 125 --exts $i --mergeYears
            if $RUN; then
                python scripts/packageSignal.py --cat $cat --outputExt packaged_$i --massPoints 125 --exts $i --mergeYears
                echo   # to add new line after output of above script
            fi
        done
    fi
done

