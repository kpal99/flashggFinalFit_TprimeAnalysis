#!/bin/bash

RUN=true
MKDIR=false
RUNCREATEDSCRIPTS=false
# get the options passed to the script
while getopts "nsh" opt;
do
case $opt in
    m) MKDIR=true;;
    n) RUN=false;;
    s) RUNCREATEDSCRIPTS=true;;
    h) echo "Usage: $0 [-n] [-s]"
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
        if $RUNCREATEDSCRIPTS; then
            for cat in THQLeptonicTag THQHadronicTag
            do
                echo python RunPlotter.py --procs all --years 2018 --cats $cat --ext packaged_TprimeM"$m"Decay"$d"pctSch
                if $RUN; then
                    python RunPlotter.py --procs all --years 2018 --cats $cat --ext packaged_TprimeM"$m"Decay"$d"pctSch
                    echo   # to add new line after output of above script
                fi
            done
        fi
    done
done

# to sync output
#for m in {7,10,14,20,24}00; for d in 10 30; for cat in THQLeptonicTag THQHadronicTag; for extension in pdf png C; cp -v outdir_packaged_TprimeM"$m"Decay"$d"pctSch/Plots/smodel_"$cat"_2018."$extension" ~b2g/plots/finalFit/TprimeM"$m"Decay"$d"pctSch_smodel_"$cat"_2018."$extension"
