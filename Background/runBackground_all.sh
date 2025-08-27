#!/bin/bash

RUN=true
TEST=false
# get the options passed to the script
while getopts "nhty:d:p:" opt;
do
case $opt in
    n) RUN=false;;
    y) YEAR=$OPTARG;;
    d) INPUTDIR=$OPTARG;;
    t) TEST=true;;
    p) PLOTDIR=$OPTARG;;
    h) echo "Usage: $0 -y YEAR -d INPUTDIR -p PLOTDIR [-h] [-n] [-t]"
       echo "  -h: print this help"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -y: year 2016,2017,2018,combined,2022,2023,22plus23"
       echo "  -d: input directory"
       echo "  -t: test, run for single mass, decay width"
       echo "  -p: plot directory to sync plots to"
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
            ./runBackground_.sh -y $YEAR -d $INPUTDIR -p $PLOTDIR -s $TPRIMEPROC
        else
            ./runBackground_.sh -y $YEAR -d $INPUTDIR -p $PLOTDIR -s $TPRIMEPROC -n
        fi
        [ $TEST = true ] && break
    done
    [ $TEST = true ] && break
done
