#!/bin/bash

RUN=""
TEST=false
SYST=""
# get the options passed to the script
while getopts "nehty:" opt;
do
case $opt in
    n) RUN="-n";;
    t) TEST=true;;
    y) YEAR=$OPTARG;;
    e) SYST="-e";;
    h) echo "Usage: $0 [-n] [-h] [-t] -y YEAR"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -e: enable systematics, errors"
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
        ./runCombine_.sh -y $YEAR -s $TPRIMEPROC $RUN $SYST
        [ $TEST = true ] && break
    done
    [ $TEST = true ] && break
done
