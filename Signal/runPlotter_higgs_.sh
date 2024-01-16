#!/bin/bash

RUN=true
MKDIR=false
RUNCREATEDSCRIPTS=false
SYNC=false
# get the options passed to the script
while getopts "nrsh" opt;
do
case $opt in
    n) RUN=false;;
    r) RUNCREATEDSCRIPTS=true;;
    s) SYNC=true;;
    h) echo "Usage: $0 [-n] [-r] [-s]"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -r: run final scripts which are found in outdir_*"
       echo "  -s: cp plots to eos, with -n for dry run"
       exit 0;;
    \?) exit ;;
esac
done

EOSDIR=/eos/user/k/kpal/www/dRjvB48p6Y/plots/finalFit
export PYTHONPATH=$PYTHONPATH:$CMSSW_BASE/src/flashggFinalFit/tools:$CMSSW_BASE/src/flashggFinalFit/Signal/tools
for i in VBF TTH #GG2H , since GG2H interal is negative
do
    for cat in THQLeptonicTag THQHadronicTag
    do
        if $RUNCREATEDSCRIPTS; then
            echo python RunPlotter.py --procs all --years 2018 --cats $cat --ext packaged_$i
            if $RUN; then
                python RunPlotter.py --procs all --years 2018 --cats $cat --ext packaged_$i
                echo   # to add new line after output of above script
            fi
        fi
        if $SYNC; then
            for extension in pdf png C
            do
                echo cp -v outdir_packaged_$i/Plots/smodel_"$cat"_2018."$extension" $EOSDIR/"$i"_smodel_"$cat"_2018."$extension"
                if $RUN; then
                    cp -v outdir_packaged_$i/Plots/smodel_"$cat"_2018."$extension" $EOSDIR/"$i"_smodel_"$cat"_2018."$extension"
                fi
            done
            echo
        fi
    done
done
