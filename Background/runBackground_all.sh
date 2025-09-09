#!/bin/bash

RUN=true
TEST=false
LIST=false
# get the options passed to the script
while getopts "nhtly:d:p:" opt;
do
case $opt in
    n) RUN=false;;
    t) TEST=true;;
    l) LIST=true;;
    y) YEAR=$OPTARG;;
    d) INPUTDIR=$OPTARG;;
    p) PLOTDIR=$OPTARG;;
    h) echo "Usage: $0 -y YEAR -d INPUTDIR -p PLOTDIR [-h] [-n] [-t]"
       echo "  -h: print this help"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -y: year 2016,2017,2018,Run2,2022,2023,22plus23"
       echo "  -d: input directory"
       echo "  -l: list of processes to run"
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
        if [ $LIST = true ]; then
            echo ./runBackground_.sh -y $YEAR -d $INPUTDIR -p $PLOTDIR -s $TPRIMEPROC
            [ $TEST = true ] && break
            continue
        fi
        if $RUN; then
            ./runBackground_.sh -y $YEAR -d $INPUTDIR -p $PLOTDIR -s $TPRIMEPROC
        else
            ./runBackground_.sh -y $YEAR -d $INPUTDIR -p $PLOTDIR -s $TPRIMEPROC -n
        fi
        [ $TEST = true ] && break
    done
    [ $TEST = true ] && break
done
