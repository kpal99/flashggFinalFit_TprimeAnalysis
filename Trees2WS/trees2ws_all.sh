#!/bin/bash

RUN=true
TEST=false
LIST=false
# get the options passed to the script
# get inputDir as argument
while getopts "nhtld:y:" opt
do
case $opt in
    n) RUN=false;;
    d) INPUTDIR=$OPTARG;;
    y) YEAR=$OPTARG;;
    t) TEST=true;;
    l) LIST=true;;
    h) echo "Usage: $0 trees2ws_all.sh [-n] -d inputDir -y year [-t] [-h]"
       echo "  -n: dry run, do not run the script"
       echo "  -d: input directory"
       echo "  -y: year"
       echo "  -l: list the ./tree2ws_.sh to be run"
       echo "  -t: test, run for single mass, decay width"
       echo "  -h: print this message and exit"
       exit ;;
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
            echo ./trees2ws_.sh -d $INPUTDIR -y $YEAR -s $TPRIMEPROC
            [ $TEST = true ] && break
            continue
        fi

        if $RUN; then
            ./trees2ws_.sh -d $INPUTDIR -y $YEAR -s $TPRIMEPROC
        else
            ./trees2ws_.sh -d $INPUTDIR -y $YEAR -s $TPRIMEPROC -n
        fi

        [ $TEST = true ] && break
    done
    [ $TEST = true ] && break
done
