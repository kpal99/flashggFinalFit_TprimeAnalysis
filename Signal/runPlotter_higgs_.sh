#!/bin/bash

RUN=true
MKDIR=false
RUNCREATEDSCRIPTS=false
# get the options passed to the script
while getopts "nsh" opt;
do
case $opt in
    n) RUN=false;;
    s) RUNCREATEDSCRIPTS=true;;
    h) echo "Usage: $0 [-n] [-s]"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -s: run final scripts which are found in outdir_*"
       exit 0;;
    \?) exit ;;
esac
done

export PYTHONPATH=$PYTHONPATH:$CMSSW_BASE/src/flashggFinalFit/tools:$CMSSW_BASE/src/flashggFinalFit/Signal/tools
for i in VBF TTH #GG2H , since GG2H interal is negative
do
    if $RUNCREATEDSCRIPTS; then
        for cat in THQLeptonicTag THQHadronicTag
        do
            echo python RunPlotter.py --procs all --years 2018 --cats $cat --ext packaged_$i
            if $RUN; then
                python RunPlotter.py --procs all --years 2018 --cats $cat --ext packaged_$i
                echo   # to add new line after output of above script
            fi
        done
    fi
done
