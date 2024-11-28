#!/bin/bash

RUN=true
TEST=false
# get the options passed to the script
while getopts "nhty:d:" opt;
do
case $opt in
    n) RUN=false;;
    y) YEAR=$OPTARG;;
    d) INPUTDIR=$OPTARG;;
    t) TEST=true;;
    h) echo "Usage: $0 [-y YEAR] [-d INPUTDIR] [-h] [-n] [-t]"
       echo "  -h: print this help"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -y: year 2016,2017,2018,Combined"
       echo "  -d: input directory"
       exit 0;;
    \?) exit ;;
esac
done

for m in  {7..12}00 #{14,16,18,20,22,24,26}00;
do
    for d in 5 #20
    do
        TPRIMEPROC=TprimeM"$m"Decay"$d"pct
        echo python3 make_config.py --inputWS $INPUTDIR/$TPRIMEPROC/ws/allData.root --year $YEAR --ext $TPRIMEPROC
        echo python3 RunBackgroundScripts.py --inputConfig config/config_"$TPRIMEPROC"_$YEAR.py --mode fTestParallel
        if $RUN; then
            python3 make_config.py --inputWS $INPUTDIR/$TPRIMEPROC/ws/allData.root --year $YEAR --ext $TPRIMEPROC
            python3 RunBackgroundScripts.py --inputConfig config/config_"$TPRIMEPROC"_$YEAR.py --mode fTestParallel
            echo   # to add new line after output of above script
        fi
        [ $TEST = true ] && break
    done
    [ $TEST = true ] && break
done
