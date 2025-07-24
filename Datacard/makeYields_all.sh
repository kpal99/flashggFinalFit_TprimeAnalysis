#!/bin/bash

RUN=true
TEST=false
# get the options passed to the script
while getopts "nhtd:y:" opt;
do
case $opt in
    n) RUN=false;;
    t) TEST=true;;
    d) INPUTDIR=$OPTARG;;
    y) YEAR=$OPTARG;;
    h) echo "Usage: $0 [-n] [-h] [-t] -d INPUTDIR -y YEAR"
       echo "  -d: input selection directory"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -t: run test scripts"
       echo "  -y: year"
       echo "  -h: print this help message"
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
        if $RUN; then
            ./makeYields_.sh -d $INPUTDIR -s $TPRIMEPROC -y $YEAR
        else
            ./makeYields_.sh -d $INPUTDIR -s $TPRIMEPROC -y $YEAR -n
        fi

        [ $TEST = true ] && break
    done
    [ $TEST = true ] && break
done
