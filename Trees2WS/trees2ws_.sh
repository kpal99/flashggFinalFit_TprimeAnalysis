#!/bin/bash

RUN=true
# get the options passed to the script
# get inputDir as argument
while getopts "nhd:y:" opt
do
case $opt in
    n) RUN=false;;
    d) INPUTDIR=$OPTARG;;
    y) YEAR=$OPTARG;;
    h) echo "trees2ws.sh [-n] [-d inputDir] [-y year]"
       echo "  -n: dry run, do not run the script"
       echo "  -d: input directory"
       echo "  -y: year"
       echo "  -h: print this message and exit"
       exit ;;
    \?) exit ;;
esac
done

for m in  {7..12}00 {14,16,18,20,22,24,26}00;
do
    for d in 5 20;
    do
        for mode in Sch Tch Int;
        do
            echo python3 trees2ws.py --inputConfig config_test.py --inputTreeFile $INPUTDIR/TprimeM"$m"Decay"$d"pct$mode/output_M125_TprimeM"$m"Decay"$d"pct$mode.root --productionMode TprimeM"$m"Decay"$d"pct$mode --year $YEAR
            if $RUN; then
                python3 trees2ws.py --inputConfig config_test.py --inputTreeFile $INPUTDIR/TprimeM"$m"Decay"$d"pct$mode/output_M125_TprimeM"$m"Decay"$d"pct$mode.root --productionMode TprimeM"$m"Decay"$d"pct$mode --year $YEAR
                echo
            fi
        done
    done
done
