#!/bin/bash

RUN=true
TEST=false
# get the options passed to the script
while getopts "nhy:p:s:" opt;
do
case $opt in
    n) RUN=false;;
    y) YEAR=$OPTARG;;
    p) PLOTDIR=$OPTARG;;
    s) TPRIMEPROC=$OPTARG;;
    h) echo "Usage: $0 [-n] -y YEAR [-h] -p PLOTDIR -s TPRIMEPROC"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -y: year"
       echo "  -p: plot directory to sync plots to"
       echo "  -s: signal process to use, TPRIMEPROC"
       echo "  -h: print this help message and exit"
       exit 0;;
    \?) exit ;;
esac
done

cd $(dirname $0)
# Uses configFile created by runfTest_.sh
echo python3 RunSignalScripts.py --inputConfig config/${TPRIMEPROC}_${YEAR}.py --mode signalFit --modeOpts '"--doPlots --skipSystematics --skipVertexScenarioSplit"'
if $RUN; then
    python3 RunSignalScripts.py --inputConfig config/${TPRIMEPROC}_${YEAR}.py --mode signalFit --modeOpts "--doPlots --skipSystematics --skipVertexScenarioSplit"
fi
# getting following error after plotting, will figure out later
## Traceback (most recent call last):
##   File "/afs/cern.ch/work/k/kpal/private/finalfits-hDNA/CMSSW_14_1_0_pre4/src/flashggFinalFit/Signal/scripts/signalFit.py", line 326, in <module>
##     plotSplines(fm,_outdir="%s/outdir_%s/signalFit/Plots"%(swd__,opt.ext),_nominalMass=MHNominal)
##   File "/afs/cern.ch/work/k/kpal/private/finalfits-hDNA/CMSSW_14_1_0_pre4/src/flashggFinalFit/Signal/tools/plottingTools.py", line 359, in plotSplines
##     for sp in splinesToPlot: xnom[sp] = _finalModel.Splines[sp].getVal()
## KeyError: 'fracRV'

mkdir -pv $PLOTDIR/$YEAR/signalFit/$TPRIMEPROC
echo rsync -ah --quiet --stats outdir_${TPRIMEPROC}_${YEAR}/signalFit/Plots/ $PLOTDIR/$YEAR/signalFit/$TPRIMEPROC/
rsync -ah --quiet --stats outdir_${TPRIMEPROC}_${YEAR}/signalFit/Plots/ $PLOTDIR/$YEAR/signalFit/$TPRIMEPROC/
cp -v $PLOTDIR/$YEAR/signalFit/index.php $PLOTDIR/$YEAR/signalFit/$TPRIMEPROC
