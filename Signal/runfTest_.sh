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
for m in  {7..12}00 {14,16,18,20,22,24,26}00;
do
    for d in 5 20
    do
        for mode in Sch #Tch Int
        do
            if $MKDIR; then
                echo python3 make_config.py --inputWSDir $INPUTDIR/TprimeM"$m"Decay"$d"pct$mode/ws_TprimeM"$m"Decay"$d"pct$mode --procs TprimeM"$m"Decay"$d"pct$mode --year $YEAR
                # by the nature of echo and shell, we are not seeing "" in shell, but it's being passed in python correctly, thus "" in '' for echo
                echo python3 RunSignalScripts.py --inputConfig config/TprimeM"$m"Decay"$d"pct$mode.py --mode fTest --printOnly --modeOpts '"--doPlots --nProcsToFTest -1 --skipWV"'
                if $RUN; then
                    python3 make_config.py --inputWSDir $INPUTDIR/TprimeM"$m"Decay"$d"pct$mode/ws_TprimeM"$m"Decay"$d"pct$mode --procs TprimeM"$m"Decay"$d"pct$mode --year $YEAR
                    python3 RunSignalScripts.py --inputConfig config/TprimeM"$m"Decay"$d"pct$mode.py --mode fTest --printOnly --modeOpts "--doPlots --nProcsToFTest -1 --skipWV"
                    echo   # to add new line after output of above script
                fi
            fi
        done
    done
done
