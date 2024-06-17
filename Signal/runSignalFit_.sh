#!/bin/bash

RUN=true
MKDIR=false
RUNCREATEDSCRIPTS=false
# get the options passed to the script
while getopts "mnrhd:y:" opt;
do
case $opt in
    m) MKDIR=true;;
    n) RUN=false;;
    r) RUNCREATEDSCRIPTS=true;;
    d) INPUTDIR=$OPTARG;;
    h) echo "Usage: $0 [-m] [-n] [-r]"
       echo "  -m: create required directories for signalFit"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -r: run final scripts which are found in outdir_*"
       echo "  -y: year"
       exit 0;;
    \?) exit ;;
esac
done

export PYTHONPATH=$PYTHONPATH:$CMSSW_BASE/src/flashggFinalFit/tools:$CMSSW_BASE/src/flashggFinalFit/Signal/tools
for m in  {7..12}00 {14,16,18,20,22,24,26}00;
do
    for d in 5 20
    do
        for mode in Sch #Tch Int;
        do
            if $MKDIR; then
                # Uses configFile created by runfTest_.sh
                echo python3 RunSignalScripts.py --inputConfig config/TprimeM"$m"Decay"$d"pct$mode.py --mode signalFit --printOnly --modeOpts '"--doPlots --skipSystematics --skipVertexScenarioSplit"'
                if $RUN; then
                    python3 RunSignalScripts.py --inputConfig config/TprimeM"$m"Decay"$d"pct$mode.py --mode signalFit --printOnly --modeOpts "--doPlots --skipSystematics --skipVertexScenarioSplit"
                    echo   # to add new line after output of above script
                fi
            fi
            if $RUNCREATEDSCRIPTS; then
                for arg in 0 1
                do
                    echo ./outdir_TprimeM"$m"Decay"$d"pct$mode/signalFit/jobs/condor_signalFit_TprimeM"$m"Decay"$d"pct$mode.sh $arg
                    if $RUN; then
                        ./outdir_TprimeM"$m"Decay"$d"pct$mode/signalFit/jobs/condor_signalFit_TprimeM"$m"Decay"$d"pct$mode.sh $arg
                        # getting following error after plotting, will figure out later
## Traceback (most recent call last):
##   File "/afs/cern.ch/work/k/kpal/private/finalfits-hDNA/CMSSW_14_1_0_pre4/src/flashggFinalFit/Signal/scripts/signalFit.py", line 326, in <module>
##     plotSplines(fm,_outdir="%s/outdir_%s/signalFit/Plots"%(swd__,opt.ext),_nominalMass=MHNominal)
##   File "/afs/cern.ch/work/k/kpal/private/finalfits-hDNA/CMSSW_14_1_0_pre4/src/flashggFinalFit/Signal/tools/plottingTools.py", line 359, in plotSplines
##     for sp in splinesToPlot: xnom[sp] = _finalModel.Splines[sp].getVal()
## KeyError: 'fracRV'
                        echo   # to add new line after output of above script
                    fi
                done
            fi
        done
    done
done
