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

cd $(dirname $0)
mkdir -pv $INPUTDIR/$TPRIMEPROC/ws

SYSTEMATICS=""
if [ $YEAR = "2016" ]; then
    SYSTEMATICS="--doSystematics"
elif [ $YEAR = "2017" ]; then
    :
elif [ $YEAR = "2018" ]; then
    SYSTEMATICS="--doSystematics"
elif [ $YEAR = "2022" ]; then
    :
fi

# making Tprime workspaces
for mode in Sch Tch # Int
do
    echo python3 trees2ws.py --inputConfig config_${YEAR}.py --inputTreeFile $INPUTDIR/$TPRIMEPROC/output_M125_$TPRIMEPROC$mode.root --productionMode $TPRIMEPROC$mode --year $YEAR $SYSTEMATICS
    if $RUN; then
        python3 trees2ws.py --inputConfig config_${YEAR}.py --inputTreeFile $INPUTDIR/$TPRIMEPROC/output_M125_$TPRIMEPROC$mode.root --productionMode $TPRIMEPROC$mode --year $YEAR $SYSTEMATICS
        ln -svf $INPUTDIR/$TPRIMEPROC/ws_$TPRIMEPROC$mode/output_M125_$TPRIMEPROC$mode.root $INPUTDIR/$TPRIMEPROC/ws
        echo
    fi
done

HIGGSMODES=("GG2H" "TTH" "VBF" "VH")
if [ $YEAR = "2016" ]; then
    HIGGSMODES+=("THQ")
elif [ $YEAR = "2017" ]; then
    HIGGSMODES+=("THQ")
elif [ $YEAR = "2018" ]; then
    :
elif [ $YEAR = "2022" ]; then
    :
fi
# making higgs workspaces
for higgsMode in ${HIGGSMODES[@]};
do
    echo python3 trees2ws.py --inputConfig config_${YEAR}.py --inputTreeFile $INPUTDIR/$TPRIMEPROC/output_M125_$higgsMode.root --productionMode $higgsMode --year $YEAR $SYSTEMATICS
    if $RUN; then
        python3 trees2ws.py --inputConfig config_${YEAR}.py --inputTreeFile $INPUTDIR/$TPRIMEPROC/output_M125_$higgsMode.root --productionMode $higgsMode --year $YEAR $SYSTEMATICS
        ln -svf $INPUTDIR/$TPRIMEPROC/ws_$higgsMode/output_M125_$higgsMode.root $INPUTDIR/$TPRIMEPROC/ws
        echo
    fi
done

# making data workspaces
if [ -f $INPUTDIR/$TPRIMEPROC/allData.root ]; then
    echo python3 trees2ws_data.py --inputConfig config_${YEAR}.py --inputTreeFile $INPUTDIR/$TPRIMEPROC/allData.root
    if $RUN; then
        python3 trees2ws_data.py --inputConfig config_${YEAR}.py --inputTreeFile $INPUTDIR/$TPRIMEPROC/allData.root
        echo
    fi
fi
