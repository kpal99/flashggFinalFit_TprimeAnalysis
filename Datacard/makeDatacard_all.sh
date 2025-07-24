#!/bin/bash

RUN=true
TEST=false
# get the options passed to the script
while getopts "nhty:" opt;
do
case $opt in
    n) RUN=false;;
    t) TEST=true;;
    y) YEAR=$OPTARG;;
    h) echo "Usage: $0 [-n] [-h] [-t] -y YEAR"
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
            ./makeDatacard_.sh -y $YEAR -s $TPRIMEPROC
        else
            ./makeDatacard_.sh -y $YEAR -s $TPRIMEPROC -n
        fi
        [ $TEST = true ] && break
    done
    [ $TEST = true ] && break
done
