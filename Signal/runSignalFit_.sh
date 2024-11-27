#!/bin/bash

RUN=true
TEST=false
# get the options passed to the script
while getopts "nhty:p:" opt;
do
case $opt in
    n) RUN=false;;
    t) TEST=true;;
    p) PLOTDIR=$OPTARG;;
    h) echo "Usage: $0 [-n] [-y YEAR] [-t] [-h] [-p PLOTDIR]"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -y: year"
       echo "  -t: test, run for single mass, decay width"
       echo "  -p: plot directory to sync plots to"
       echo "  -h: print this help message and exit"
       exit 0;;
    \?) exit ;;
esac
done

for m in  {7..12}00 #{14,16,18,20,22,24,26}00;
do
    for d in 5 #20
    do
        # Uses configFile created by runfTest_.sh
        TPRIMEPROC=TprimeM"$m"Decay"$d"pct
        echo python3 RunSignalScripts.py --inputConfig config/$TPRIMEPROC.py --mode signalFit --modeOpts '"--doPlots --skipSystematics --skipVertexScenarioSplit"'
        if $RUN; then
            python3 RunSignalScripts.py --inputConfig config/$TPRIMEPROC.py --mode signalFit --modeOpts "--doPlots --skipSystematics --skipVertexScenarioSplit"
        fi
# getting following error after plotting, will figure out later
## Traceback (most recent call last):
##   File "/afs/cern.ch/work/k/kpal/private/finalfits-hDNA/CMSSW_14_1_0_pre4/src/flashggFinalFit/Signal/scripts/signalFit.py", line 326, in <module>
##     plotSplines(fm,_outdir="%s/outdir_%s/signalFit/Plots"%(swd__,opt.ext),_nominalMass=MHNominal)
##   File "/afs/cern.ch/work/k/kpal/private/finalfits-hDNA/CMSSW_14_1_0_pre4/src/flashggFinalFit/Signal/tools/plottingTools.py", line 359, in plotSplines
##     for sp in splinesToPlot: xnom[sp] = _finalModel.Splines[sp].getVal()
## KeyError: 'fracRV'

        if [ $PLOTDIR ]; then
          mkdir -pv $PLOTDIR/signalFit/$TPRIMEPROC
          echo rsync -ah --quiet --stats outdir_$TPRIMEPROC/signalFit/Plots/ $PLOTDIR/signalFit/$TPRIMEPROC/
          rsync -ah --quiet --stats outdir_$TPRIMEPROC/signalFit/Plots/ $PLOTDIR/signalFit/$TPRIMEPROC/
          cp -v $PLOTDIR/signalFit/index.php $PLOTDIR/signalFit/$TPRIMEPROC
        fi
        echo   # to add new line after output of above script
        [ $TEST = true ] && break
    done
    [ $TEST = true ] && break
done
