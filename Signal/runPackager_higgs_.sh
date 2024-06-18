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
for i in GG2H THQ TTH VBF VH
do
    if $MKDIR; then
        echo python3 RunPackager.py --cats THQLeptonicTag,THQHadronicTag --exts $i --mergeYears --batch condor --queue espresso --massPoints 125 --outputExt packaged_$i --printOnly
        if $RUN; then
            python3 RunPackager.py --cats THQLeptonicTag,THQHadronicTag --exts $i --mergeYears --batch condor --queue espresso --massPoints 125 --outputExt packaged_$i --printOnly
            echo   # to add new line after output of above script
        fi
    fi
    if $RUNCREATEDSCRIPTS; then
        for arg in 0 1
        do
            echo ./outdir_packaged_$i/packageSignal/jobs/condor_packageSignal_packaged_$i.sh $arg
            if $RUN; then
                ./outdir_packaged_$i/packageSignal/jobs/condor_packageSignal_packaged_$i.sh $arg
                echo   # to add new line after output of above script
            fi
        done
    fi
done
