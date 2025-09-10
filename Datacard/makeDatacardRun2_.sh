#!/bin/bash

RUN=true
SYSTEMATICS=""
# get the options passed to the script
while getopts "nhts:e" opt;
do
case $opt in
    n) RUN=false;;
    t) TEST=true;;
    s) TPRIMEPROC=$OPTARG;;
    e) SYSTEMATICS="--doSystematics";;
    h) echo "Usage: $0 [-n] [-h] [-t] -y YEAR -s TPRIMEPROC"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -t: run test scripts"
       echo "  -s: sample process to use, TPRIMEPROC"
       echo "  -e: enable systematics, errors"
       echo "  -h: print this help message"
       exit 0;;
    \?) exit ;;
esac
done

cd $(dirname $0)
FINALFITDIR=$CMSSW_BASE/src/flashggFinalFit/

echo
echo ln -svf systematics_Tprime_Run2.py systematics.py
echo python3 makeDatacard.py --ext ${TPRIMEPROC}_Run2 --years 2016,2017,2018 --skipCOWCorr --doMCStatUncertainty --saveDataFrame --output Datacard_${TPRIMEPROC}_Run2 $SYSTEMATICS
if $RUN; then
    echo   # to add new line after output of above script
    ln -svf systematics_Tprime_Run2.py systematics.py
    python3 makeDatacard.py --ext ${TPRIMEPROC}_Run2 --years 2016,2017,2018 --skipCOWCorr --doMCStatUncertainty --saveDataFrame --output Datacard_${TPRIMEPROC}_Run2 $SYSTEMATICS
    mkdir -pv $FINALFITDIR/Combine/Models/Run2/$TPRIMEPROC/{signal,background}
    cp -v $FINALFITDIR/Signal/outdir_packaged_${TPRIMEPROC}_Run2/CMS-HGG_sigfit_packaged*.root $FINALFITDIR/Combine/Models/Run2/$TPRIMEPROC/signal/
    cp -v $FINALFITDIR/Background/outdir_${TPRIMEPROC}_Run2/CMS-HGG_multipdf*.root $FINALFITDIR/Combine/Models/Run2/$TPRIMEPROC/background/
    cp -v $FINALFITDIR/Datacard/Datacard_${TPRIMEPROC}_Run2.txt $FINALFITDIR/Combine/
fi
