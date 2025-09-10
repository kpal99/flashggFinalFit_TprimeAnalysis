#!/bin/bash

RUN=true
TEST=false
LIST=false
# get the options passed to the script
while getopts "nhlty:p:" opt;
do
case $opt in
    n) RUN=false;;
    t) TEST=true;;
    l) LIST=true;;
    y) YEAR=$OPTARG;;
    p) PLOTDIR=$OPTARG;;
    h) echo "Usage: $0 [-n] -y YEAR [-t] [-h] -p PLOTDIR"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -y: year"
       echo "  -t: test, run for single mass, decay width"
       echo "  -p: plot directory to sync plots to"
       echo "  -h: print this help message and exit"
       exit 0;;
    \?) exit ;;
esac
done

cd $(dirname $0)
for m in  {7..12}00 {14,16,18,20,22,24,26}00
do
    for d in 5 10 20 30
    do
        TPRIMEPROC=TprimeM"$m"Decay"$d"pct
        if $LIST; then
            echo ./runSignalFit_.sh -y $YEAR -p $PLOTDIR -s $TPRIMEPROC
            [ $TEST = true ] && break
            continue
        fi

        if $RUN; then
            ./runSignalFit_.sh -y $YEAR -p $PLOTDIR -s $TPRIMEPROC
        else
            ./runSignalFit_.sh -y $YEAR -p $PLOTDIR -s $TPRIMEPROC -n
        fi
        [ $TEST = true ] && break
    done
    [ $TEST = true ] && break
done
