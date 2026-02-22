#!/bin/bash

RUN=true
SYSTEMATICS=""
PLOTDIR="./"
# get the options passed to the script
while getopts "nhts:ep:" opt;
do
case $opt in
    n) RUN=false;;
    t) TEST=true;;
    s) TPRIMEPROC=$OPTARG;;
    e) SYSTEMATICS="--doSystematics";;
    p) PLOTDIR=$OPTARG;;
    h) echo "Usage: $0 [-n] [-h] [-t] -s TPRIMEPROC [-e] [-p PLOTDIR]"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -t: run test scripts"
       echo "  -s: sample process to use, TPRIMEPROC"
       echo "  -e: enable systematics, errors"
       echo "  -p: plot directory"
       echo "  -h: print this help message"
       exit 0;;
    \?) exit ;;
esac
done

cd $(dirname $0)
FINALFITDIR=$CMSSW_BASE/src/flashggFinalFit/

echo
echo python3 makeDatacard.py --ext ${TPRIMEPROC}_22plus23 --years 2022,2023 --skipCOWCorr --doMCStatUncertainty --saveDataFrame --output Datacard_${TPRIMEPROC}_22plus23 $SYSTEMATICS --systConfig systematics_Tprime_22plus23.py
if $RUN; then
    echo   # to add new line after output of above script
    python3 makeDatacard.py --ext ${TPRIMEPROC}_22plus23 --years 2022,2023 --skipCOWCorr --doMCStatUncertainty --saveDataFrame --output Datacard_${TPRIMEPROC}_22plus23 $SYSTEMATICS --systConfig systematics_Tprime_22plus23.py
    python3 Datacard_Viewer/datacard_txt_to_html.py --output-dir $PLOTDIR/Datacard/ --datacard Datacard_${TPRIMEPROC}_22plus23.txt
    mkdir -pv $FINALFITDIR/Combine/Models/22plus23/$TPRIMEPROC/{signal,background}
    cp -v $FINALFITDIR/Signal/outdir_packaged_${TPRIMEPROC}_22plus23/CMS-HGG_sigfit_packaged*.root $FINALFITDIR/Combine/Models/22plus23/$TPRIMEPROC/signal/
    cp -v $FINALFITDIR/Background/outdir_${TPRIMEPROC}_22plus23/CMS-HGG_multipdf*.root $FINALFITDIR/Combine/Models/22plus23/$TPRIMEPROC/background/
    cp -v $FINALFITDIR/Datacard/Datacard_${TPRIMEPROC}_22plus23.txt $FINALFITDIR/Combine/
fi
