#!/bin/bash

RUN=true
TEST=false
# get the options passed to the script
while getopts "nhtd:y:p:" opt;
do
case $opt in
    n) RUN=false;;
    d) INPUTDIR=$OPTARG;;
    y) YEAR=$OPTARG;;
    t) TEST=true;;
    p) PLOTDIR=$OPTARG;;
    h) echo "Usage: $0 [-n] -d INPUTDIR -y YEAR [-t] [-h] -p PLOTDIR"
       echo "  -d: input directory"
       echo "  -y: year"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -t: test, run for single mass, decay width"
       echo "  -p: plot directory to sync plots to"
       echo "  -h: print this help message"
       exit 0;;
    \?) exit ;;
esac
done

# for --skipWV, see
# https://github.com/cms-analysis/flashggFinalFit/blob/dev_fggfinalfits_lite/Signal/README.md?plain=1#L37
cd $(dirname $0)
for m in  {7..12}00 {14,16,18,20,22,24,26}00
do
    for d in 5 10 20 30
    do
        TPRIMEPROC=TprimeM"$m"Decay"$d"pct
        if $RUN; then
            ./runfTest_.sh -d $INPUTDIR -y $YEAR -p $PLOTDIR -s $TPRIMEPROC
        else
            ./runfTest_.sh -d $INPUTDIR -y $YEAR -p $PLOTDIR -s $TPRIMEPROC -n
        fi
        [ $TEST = true ] && break
    done
    [ $TEST = true ] && break
done
