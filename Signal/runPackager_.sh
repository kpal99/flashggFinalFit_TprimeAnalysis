#!/bin/bash

RUN=true
MKDIR=false
RUNCREATEDSCRIPTS=false
# get the options passed to the script
while getopts "mnrh" opt;
do
case $opt in
    m) MKDIR=true;;
    n) RUN=false;;
    r) RUNCREATEDSCRIPTS=true;;
    a) ADDALL=true;;
    h) echo "Usage: $0 [-m] [-n] [-r] [-h]"
       echo "  -m: create required directories for packaging"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -r: run final Scripts which are found in outdir_*"
       echo "  -h: print this help message"
       exit 0;;
    \?) exit ;;
esac
done

export PYTHONPATH=$PYTHONPATH:$CMSSW_BASE/src/flashggFinalFit/tools:$CMSSW_BASE/src/flashggFinalFit/Signal/tools
for m in  {7..12}00 {14,16,18,20,22,24,26}00;
do
    for d in 5 20
    do
        for mode in Sch #Tch Int
        do
            if $MKDIR; then
                echo python3 RunPackager.py --cats THQLeptonicTag,THQHadronicTag --exts TprimeM"$m"Decay"$d"pct$mode --mergeYears --batch condor --queue espresso --massPoints 125 --outputExt packaged_TprimeM"$m"Decay"$d"pct$mode --printOnly
                if $RUN; then
                    python3 RunPackager.py --cats THQLeptonicTag,THQHadronicTag --exts TprimeM"$m"Decay"$d"pct$mode --mergeYears --batch condor --queue espresso --massPoints 125 --outputExt packaged_TprimeM"$m"Decay"$d"pct$mode --printOnly
                    echo   # to add new line after output of above script
                fi
            fi
            if $RUNCREATEDSCRIPTS; then
                for arg in 0 1
                do
                    echo ./outdir_packaged_TprimeM"$m"Decay"$d"pct$mode/packageSignal/jobs/condor_packageSignal_packaged_TprimeM"$m"Decay"$d"pct$mode.sh $arg
                    if $RUN; then
                        ./outdir_packaged_TprimeM"$m"Decay"$d"pct$mode/packageSignal/jobs/condor_packageSignal_packaged_TprimeM"$m"Decay"$d"pct$mode.sh $arg
                        echo   # to add new line after output of above script
                    fi
                done
            fi
        done
    done
done
