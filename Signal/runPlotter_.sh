#!/bin/bash

RUN=true
MKDIR=false
RUNCREATEDSCRIPTS=false
# get the options passed to the script
while getopts "nrhy:" opt;
do
case $opt in
    n) RUN=false;;
    r) RUNCREATEDSCRIPTS=true;;
    y) YEAR=$OPTARG;;
    h) echo "Usage: $0 [-n] [-r] [-h]"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -r: run final Scripts which are found in outdir_*"
       echo "  -y: year, can also take CSV i.e. '2016,2017,2018' "
       echo "  -h: print this help message"
       exit 0;;
    \?) exit ;;
esac
done

export PYTHONPATH=$PYTHONPATH:$CMSSW_BASE/src/flashggFinalFit/tools:$CMSSW_BASE/src/flashggFinalFit/Signal/tools
for m in  {7..12}00 {14,16,18,20,22,24,26}00;
do
    for d in 5 20
    do
        for mode in Sch #Tch Int
        do
            for cat in THQLeptonicTag THQHadronicTag
            do
                if $RUNCREATEDSCRIPTS; then
                    echo python3 RunPlotter.py --procs all --cats $cat --ext packaged_TprimeM"$m"Decay"$d"pct$mode --years $YEAR
                    if $RUN; then
                        python3 RunPlotter.py --procs all --cats $cat --ext packaged_TprimeM"$m"Decay"$d"pct$mode --years $YEAR
                        echo   # to add new line after output of above script
                    fi
                fi
            done
        done
    done
done
