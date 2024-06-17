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

for i in GG2H THQ TTH VBF VH
do
    echo python3 trees2ws.py --inputConfig config_test.py --inputTreeFile $INPUTDIR/$i/output_M125_$i.root --productionMode $i --year $YEAR
    if $RUN; then
        python3 trees2ws.py --inputConfig config_test.py --inputTreeFile $INPUTDIR/$i/output_M125_$i.root --productionMode $i --year $YEAR
        echo
    fi
done
