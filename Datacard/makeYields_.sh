#!/bin/bash

RUN=true
TEST=false
# get the options passed to the script
while getopts "nhtd:" opt;
do
case $opt in
    n) RUN=false;;
    t) TEST=true;;
    d) INPUTDIR=$OPTARG;;
    h) echo "Usage: $0 [-n] [-h] [-t] [ -d INPUTDIR ]"
       echo "  -d: input selection directory"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -t: run test scripts"
       echo "  -h: print this help message"
       exit 0;;
    \?) exit ;;
esac
done

for m in  {7..12}00 {14,16,18,20} #{22,24,26}00;
do
    for d in 5 #20
    do
        TPRIMEPROC=TprimeM"$m"Decay"$d"pct
        echo python3 RunYields.py --inputWSDirMap 2017=$INPUTDIR/$TPRIMEPROC/ws/ --cats auto --procs "$TPRIMEPROC"Sch,GG2H,THQ,TTH,VBF,VH auto --ext $TPRIMEPROC --skipCOWCorr --batch local --queue espresso
        if $RUN; then
            echo   # to add new line after output of above script
            python3 RunYields.py --inputWSDirMap 2017=$INPUTDIR/$TPRIMEPROC/ws/ --cats auto --procs "$TPRIMEPROC"Sch,GG2H,THQ,TTH,VBF,VH auto --ext $TPRIMEPROC --skipCOWCorr --batch local --queue espresso
            fi
        [ $TEST = true ] && break
    done
    [ $TEST = true ] && break
done
