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
    y) YEAR=$OPTARG;;
    h) echo "Usage: $0 [-m] [-n] [-r] [-d INPUTDIR] [-y YEAR] [-h]"
       echo "  -m: create required directories for fTest"
       echo "  -d: input directory"
       echo "  -y: year"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -r: run final scripts which are found in outdir_*, don't require -m,-d,-y"
       echo "  -h: print this help message"
       exit 0;;
    \?) exit ;;
esac
done

# for --skipWV, see
# https://github.com/cms-analysis/flashggFinalFit/blob/dev_fggfinalfits_lite/Signal/README.md?plain=1#L37
export PYTHONPATH=$PYTHONPATH:$CMSSW_BASE/src/flashggFinalFit/tools:$CMSSW_BASE/src/flashggFinalFit/Signal/tools
for i in GG2H THQ TTH VBF VH
do
    if $MKDIR; then
        echo python3 make_config.py --inputWSDir $INPUTDIR/$i/ws_$i --procs $i --year $YEAR
        # by the nature of echo and shell, we are not seeing "" in shell, but it's being passed in python correctly, thus "" in '' for echo
        echo python3 RunSignalScripts.py --inputConfig config/$i.py --mode fTest --printOnly --modeOpts '"--doPlots --nProcsToFTest -1 --skipWV"'
        if $RUN; then
            python3 make_config.py --inputWSDir $INPUTDIR/$i/ws_$i --procs $i --year $YEAR
            python3 RunSignalScripts.py --inputConfig config/$i.py --mode fTest --printOnly --modeOpts "--doPlots --nProcsToFTest -1 --skipWV"
            echo   # to add new line after output of above script
        fi
    fi
    if $RUNCREATEDSCRIPTS; then
        for arg in 0 1
        do
            echo ./outdir_$i/fTest/jobs/condor_fTest_$i.sh $arg
            if $RUN; then
                ./outdir_$i/fTest/jobs/condor_fTest_$i.sh $arg
                echo   # to add new line after output of above script
            fi
        done
    fi
done
