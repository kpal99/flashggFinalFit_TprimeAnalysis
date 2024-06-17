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
for m in  {7..12}00 {14,16,18,20,22,24,26}00;
do
    for d in 5 20
    do
        for mode in Sch #Tch Int
        do
            if $MKDIR; then
                echo python3 make_config.py --inputWSDir $INPUTDIR/TprimeM"$m"Decay"$d"pct$mode/ws_TprimeM"$m"Decay"$d"pct$mode --procs TprimeM"$m"Decay"$d"pct$mode --year $YEAR
                echo python3 RunSignalScripts.py --inputConfig config/TprimeM"$m"Decay"$d"pct$mode.py --mode fTest --modeOpts '"--doPlots"' --printOnly
                if $RUN; then
                    python3 make_config.py --inputWSDir $INPUTDIR/TprimeM"$m"Decay"$d"pct$mode/ws_TprimeM"$m"Decay"$d"pct$mode --procs TprimeM"$m"Decay"$d"pct$mode --year $YEAR
                    python3 RunSignalScripts.py --inputConfig config/TprimeM"$m"Decay"$d"pct$mode.py --mode fTest --modeOpts '"--doPlots"' --printOnly
                    echo   # to add new line after output of above script
                fi
            fi
            if $RUNCREATEDSCRIPTS; then
                for arg in 0 1
                do
                    echo ./outdir_TprimeM"$m"Decay"$d"pct$mode/fTest/jobs/condor_fTest_TprimeM"$m"Decay"$d"pct$mode.sh $arg
                    if $RUN; then
                        ./outdir_TprimeM"$m"Decay"$d"pct$mode/fTest/jobs/condor_fTest_TprimeM"$m"Decay"$d"pct$mode.sh $arg
                        echo   # to add new line after output of above script
                    fi
                done
            fi
        done
    done
done
