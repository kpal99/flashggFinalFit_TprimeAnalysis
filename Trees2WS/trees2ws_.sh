#!/bin/bash

RUN=true
# get the options passed to the script
# get inputDir as argument
while getopts "nhd:y:s:" opt
do
case $opt in
    n) RUN=false;;
    d) INPUTDIR=$OPTARG;;
    y) YEAR=$OPTARG;;
    s) TPRIMEPROC=$OPTARG;;
    h) echo "Usage: $0 [-n] -d inputDir -y year [-h] -s TRPIMEPROC"
       echo "  -n: dry run, do not run the script"
       echo "  -d: input directory"
       echo "  -y: year"
       echo "  -s: signal process to use, TRPIMEPROC"
       echo "  -h: print this message and exit"
       exit ;;
    \?) exit ;;
esac
done

mkdir -pv $INPUTDIR/$TPRIMEPROC/ws
# making Tprime workspaces
for mode in Sch; # Tch Int;
do
    echo python3 trees2ws.py --inputConfig config_test.py --inputTreeFile $INPUTDIR/$TPRIMEPROC/output_M125_$TPRIMEPROC$mode.root --productionMode $TPRIMEPROC$mode --year $YEAR
    if $RUN; then
        python3 trees2ws.py --inputConfig config_test.py --inputTreeFile $INPUTDIR/$TPRIMEPROC/output_M125_$TPRIMEPROC$mode.root --productionMode $TPRIMEPROC$mode --year $YEAR
        ln -svf $INPUTDIR/$TPRIMEPROC/ws_$TPRIMEPROC$mode/output_M125_$TPRIMEPROC$mode.root $INPUTDIR/$TPRIMEPROC/ws
        echo
    fi
done

# making higgs workspaces
for higgsMode in GG2H THQ TTH VBF VH;
do
    echo python3 trees2ws.py --inputConfig config_test.py --inputTreeFile $INPUTDIR/$TPRIMEPROC/output_M125_$higgsMode.root --productionMode $higgsMode --year $YEAR
    if $RUN; then
        python3 trees2ws.py --inputConfig config_test.py --inputTreeFile $INPUTDIR/$TPRIMEPROC/output_M125_$higgsMode.root --productionMode $higgsMode --year $YEAR
        ln -svf $INPUTDIR/$TPRIMEPROC/ws_$higgsMode/output_M125_$higgsMode.root $INPUTDIR/$TPRIMEPROC/ws
        echo
    fi
done

# making data workspaces
echo python3 trees2ws_data.py --inputConfig config_test.py --inputTreeFile $INPUTDIR/$TPRIMEPROC/allData.root
if $RUN; then
    python3 trees2ws_data.py --inputConfig config_test.py --inputTreeFile $INPUTDIR/$TPRIMEPROC/allData.root
    echo
fi
