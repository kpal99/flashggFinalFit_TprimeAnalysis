#!/bin/bash

RUN=true
TEST=false
# get the options passed to the script
while getopts "nrht" opt;
do
case $opt in
    n) RUN=false;;
    t) TEST=true;;
    h) echo "Usage: $0 [-n] [-r] [-h]"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -r: run final Scripts which are found in outdir_*"
       echo "  -t: run test scripts"
       echo "  -h: print this help message"
       exit 0;;
    \?) exit ;;
esac
done

export PYTHONPATH=$PYTHONPATH:$CMSSW_BASE/src/flashggFinalFit/tools:$CMSSW_BASE/src/flashggFinalFit/Signal/tools
for m in  {7..12}00 #{14,16,18,20,22,24,26}00;
do
    for d in 5 #20
    do
        TPRIMEPROC=TprimeM"$m"Decay"$d"pct
        YEAR=2017
        echo python3 RunPackager.py --cats THQLeptonicTag,THQHadronicTag --exts $TPRIMEPROC --batch local --queue espresso --massPoints 125 --outputExt packaged_$TPRIMEPROC --year $YEAR
        if $RUN; then
            python3 RunPackager.py --cats THQLeptonicTag,THQHadronicTag --exts $TPRIMEPROC --batch local --queue espresso --massPoints 125 --outputExt packaged_$TPRIMEPROC --year $YEAR
            echo   # to add new line after output of above script
            fi
        [ $TEST = true ] && break
    done
    [ $TEST = true ] && break
done
