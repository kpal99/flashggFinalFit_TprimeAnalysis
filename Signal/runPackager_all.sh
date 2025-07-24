#!/bin/bash

RUN=true
TEST=false
# get the options passed to the script
while getopts "nrhty:" opt;
do
case $opt in
    n) RUN=false;;
    t) TEST=true;;
    y) YEAR=$OPTARG;;
    h) echo "Usage: $0 [-n] [-r] [-h] -y YEAR"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -r: run final Scripts which are found in outdir_*"
       echo "  -t: run test scripts"
       echo "  -y: year, can also take CSV i.e. '2016,2017,2018' "
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
            ./runPackager_.sh -y $YEAR -s $TPRIMEPROC
        else
            ./runPackager_.sh -y $YEAR -s $TPRIMEPROC -n
        fi
        [ $TEST = true ] && break
    done
    [ $TEST = true ] && break
done
