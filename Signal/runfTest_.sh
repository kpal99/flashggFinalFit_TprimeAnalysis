#!/bin/bash

RUN=true
# get the options passed to the script
while getopts "nhd:y:p:s:" opt;
do
case $opt in
    n) RUN=false;;
    d) INPUTDIR=$OPTARG;;
    y) YEAR=$OPTARG;;
    p) PLOTDIR=$OPTARG;;
    s) TPRIMEPROC=$OPTARG;;
    h) echo "Usage: $0 [-n] -d INPUTDIR -y YEAR [-h] -p PLOTDIR -s TPRIMEPROC"
       echo "  -d: input directory"
       echo "  -y: year"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -p: plot directory to sync plots to"
       echo "  -s: signal process to use, TPRIMEPROC"
       echo "  -h: print this help message"
       exit 0;;
    \?) exit ;;
esac
done

cd $(dirname $0)
echo python3 make_config.py --inputWSDir $INPUTDIR/$TPRIMEPROC/ws --procs ${TPRIMEPROC} --year ${YEAR}
# by the nature of echo and shell, we are not seeing "" in shell, but it's being passed in python correctly, thus "" in '' for echo
echo python3 RunSignalScripts.py --inputConfig config/${TPRIMEPROC}_${YEAR}.py --mode fTest --modeOpts '"--doPlots --nProcsToFTest -1 --skipWV"'
if $RUN; then
    python3 make_config.py --inputWSDir $INPUTDIR/$TPRIMEPROC/ws --procs ${TPRIMEPROC} --year ${YEAR}
    python3 RunSignalScripts.py --inputConfig config/${TPRIMEPROC}_${YEAR}.py --mode fTest --modeOpts "--doPlots --nProcsToFTest -1 --skipWV"
fi
#
mkdir -pv $PLOTDIR/fTest/$TPRIMEPROC
rsync -ah --quiet --stats outdir_${TPRIMEPROC}_${YEAR}/fTest/Plots/ $PLOTDIR/${YEAR}/fTest/$TPRIMEPROC/
cp -v $PLOTDIR/${YEAR}/fTest/index.php $PLOTDIR/${YEAR}/fTest/$TPRIMEPROC
echo   # to add new line after output of above script
