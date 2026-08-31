#!/bin/bash

RUN=""
TEST=false
PLOTDIR="."
# get the options passed to the script
while getopts "nhty:p:" opt;
do
case $opt in
    n) RUN="-n";;
    t) TEST=true;;
    y) YEAR=$OPTARG;;
    p) PLOTDIR=$OPTARG;;
    h) echo "Usage: $0 [-n] [-h] [-t] -y YEAR [-p PLOTDIR]"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -t: run test scripts"
       echo "  -y: year"
       echo "  -p: plot directory, default is current directory"
       echo "  -h: print this help message"
       exit 0;;
    \?) exit ;;
esac
done

if [[ -z "$YEAR" ]]; then
    echo "Error: -y YEAR is required."
    echo "Use '$0 -h' for help."
    exit 1
fi

cd $(dirname $0)
for m in  {7..12}00 {14,16,18,20,22,24,26}00
do
    for d in 5 10 20 30
    do
        TPRIMEPROC=TprimeM"$m"Decay"$d"pct
        ./makePlots_.sh -y $YEAR -s $TPRIMEPROC -p $PLOTDIR $RUN
        [ $TEST = true ] && break
    done
    [ $TEST = true ] && break
done
