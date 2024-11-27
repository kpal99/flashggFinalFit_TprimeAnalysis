#!/bin/bash

RUN=true
TEST=false
# get the options passed to the script
# get inputDir as argument
while getopts "nhtd:y:" opt
do
case $opt in
    n) RUN=false;;
    d) INPUTDIR=$OPTARG;;
    y) YEAR=$OPTARG;;
    t) TEST=true;;
    h) echo "trees2ws.sh [-n] [-d inputDir] [-y year]"
       echo "  -n: dry run, do not run the script"
       echo "  -d: input directory"
       echo "  -y: year"
       echo "  -t: test, run for single mass, decay width"
       echo "  -h: print this message and exit"
       exit ;;
    \?) exit ;;
esac
done

for m in  {7..12}00; # {14,16,18,20,22,24,26}00;
do
    for d in 5; # 20;
    do
        TPRIMEPROC=TprimeM"$m"Decay"$d"pct
        mkdir -pv $INPUTDIR/$TPRIMEPROC/ws_$TPRIMEPROC
        # making Tprime workspaces
        for mode in Sch; # Tch Int;
        do
            echo python3 trees2ws.py --inputConfig config_test.py --inputTreeFile $INPUTDIR/$TPRIMEPROC/output_M125_$TPRIMEPROC$mode.root --productionMode $TPRIMEPROC$mode --year $YEAR
            if $RUN; then
                python3 trees2ws.py --inputConfig config_test.py --inputTreeFile $INPUTDIR/$TPRIMEPROC/output_M125_$TPRIMEPROC$mode.root --productionMode $TPRIMEPROC$mode --year $YEAR
                ln -svf $INPUTDIR/$TPRIMEPROC/ws_$TPRIMEPROC$mode/output_M125_$TPRIMEPROC$mode.root $INPUTDIR/$TPRIMEPROC/ws_$TPRIMEPROC
                echo
            fi
        done

        # making higgs workspaces
        for higgsMode in GG2H THQ TTH VBF VH;
        do
            echo python3 trees2ws.py --inputConfig config_test.py --inputTreeFile $INPUTDIR/$TPRIMEPROC/output_M125_$higgsMode.root --productionMode $higgsMode --year $YEAR
            if $RUN; then
                python3 trees2ws.py --inputConfig config_test.py --inputTreeFile $INPUTDIR/$TPRIMEPROC/output_M125_$higgsMode.root --productionMode $higgsMode --year $YEAR
                ln -svf $INPUTDIR/$TPRIMEPROC/ws_$higgsMode/output_M125_$higgsMode.root $INPUTDIR/$TPRIMEPROC/ws_$TPRIMEPROC
                echo
            fi
        done

        # making data workspaces
        echo python3 trees2ws_data.py --inputConfig config_test.py --inputTreeFile $INPUTDIR/$TPRIMEPROC/allData.root
        if $RUN; then
            python3 trees2ws_data.py --inputConfig config_test.py --inputTreeFile $INPUTDIR/$TPRIMEPROC/allData.root
            echo
        fi
        [ $TEST = true ] && break
    done
    [ $TEST = true ] && break
done
