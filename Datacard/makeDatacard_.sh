#!/bin/bash

RUN=true
TEST=false
# get the options passed to the script
while getopts "nht" opt;
do
case $opt in
    n) RUN=false;;
    t) TEST=true;;
    h) echo "Usage: $0 [-n] [-h] [-t]"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -t: run test scripts"
       echo "  -h: print this help message"
       exit 0;;
    \?) exit ;;
esac
done

FINALFITDIR=$CMSSW_BASE/src/flashggFinalFit/
for m in  {7..12}00 {14,16,18,20}00 #{22,24,26}00
do
    for d in 5 #20
    do
        TPRIMEPROC=TprimeM"$m"Decay"$d"pct
        echo
        echo python3 makeDatacard.py --ext $TPRIMEPROC --years 2017 --doTrueYield --skipCOWCorr --doMCStatUncertainty --saveDataFrame --output Datacard_$TPRIMEPROC
        echo sed -i "s/Models/Models\/$TPRIMEPROC/g" Datacard_$TPRIMEPROC.txt
        if $RUN; then
            echo   # to add new line after output of above script
            python3 makeDatacard.py --ext $TPRIMEPROC --years 2017 --doTrueYield --skipCOWCorr --doMCStatUncertainty --saveDataFrame --output Datacard_$TPRIMEPROC
            sed -i "s/Models/Models\/$TPRIMEPROC/g" Datacard_$TPRIMEPROC.txt
            mkdir -pv $FINALFITDIR/Combine/Models/$TPRIMEPROC/{signal,background}
            cp -v $FINALFITDIR/Signal/outdir_packaged_$TPRIMEPROC/CMS-HGG_sigfit_packaged*.root $FINALFITDIR/Combine/Models/$TPRIMEPROC/signal/
            cp -v $FINALFITDIR/Background/outdir_$TPRIMEPROC/CMS-HGG_multipdf*.root $FINALFITDIR/Combine/Models/$TPRIMEPROC/background/
            cp -v $FINALFITDIR/Datacard/Datacard_$TPRIMEPROC.txt $FINALFITDIR/Combine/
            fi
        [ $TEST = true ] && break
    done
    [ $TEST = true ] && break
done
