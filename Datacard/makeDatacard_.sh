#!/bin/bash

RUN=true
# get the options passed to the script
while getopts "nhts:y:" opt;
do
case $opt in
    n) RUN=false;;
    t) TEST=true;;
    y) YEAR=$OPTARG;;
    s) TPRIMEPROC=$OPTARG;;
    h) echo "Usage: $0 [-n] [-h] [-t] -y YEAR -s TPRIMEPROC"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -t: run test scripts"
       echo "  -s: sample process to use, TPRIMEPROC"
       echo "  -y: year"
       echo "  -h: print this help message"
       exit 0;;
    \?) exit ;;
esac
done

cd $(dirname $0)
FINALFITDIR=$CMSSW_BASE/src/flashggFinalFit/
echo
echo python3 makeDatacard.py --ext ${TPRIMEPROC}_${YEAR} --years $YEAR --doTrueYield --skipCOWCorr --doMCStatUncertainty --saveDataFrame --output Datacard_${TPRIMEPROC}_${YEAR}
echo sed -i "s|Models|Models/$YEAR/$TPRIMEPROC|g" Datacard_${TPRIMEPROC}_${YEAR}.txt
if $RUN; then
    echo   # to add new line after output of above script
    python3 makeDatacard.py --ext ${TPRIMEPROC}_${YEAR} --years $YEAR --doTrueYield --skipCOWCorr --doMCStatUncertainty --saveDataFrame --output Datacard_${TPRIMEPROC}_${YEAR}
    sed -i "s|Models|Models/$YEAR/$TPRIMEPROC|g" Datacard_${TPRIMEPROC}_${YEAR}.txt
    mkdir -pv $FINALFITDIR/Combine/Models/$YEAR/$TPRIMEPROC/{signal,background}
    cp -v $FINALFITDIR/Signal/outdir_packaged_${TPRIMEPROC}_${YEAR}/CMS-HGG_sigfit_packaged*.root $FINALFITDIR/Combine/Models/$YEAR/$TPRIMEPROC/signal/
    cp -v $FINALFITDIR/Background/outdir_${TPRIMEPROC}_${YEAR}/CMS-HGG_multipdf*.root $FINALFITDIR/Combine/Models/$YEAR/$TPRIMEPROC/background/
    cp -v $FINALFITDIR/Datacard/Datacard_${TPRIMEPROC}_${YEAR}.txt $FINALFITDIR/Combine/
fi
