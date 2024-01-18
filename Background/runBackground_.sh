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
    h) echo "Usage: $0 [-m] [-n] [-r]"
       echo "  -h: print this help"
       echo "  -m: create required directories for fTest"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -r: run final scripts which are found in outdir_*"
       exit 0;;
    \?) exit ;;
esac
done

if $MKDIR; then
    echo python RunBackgroundScripts.py --inputConfig config_test.py --mode fTestParallel --printOnly
    if $RUN; then
        python RunBackgroundScripts.py --inputConfig config_test.py --mode fTestParallel --printOnly
        echo   # to add new line after output of above script
    fi
fi
if $RUNCREATEDSCRIPTS; then
    for cat in THQLeptonicTag THQHadronicTag
    do
        echo ./runBackgroundScripts.sh -i /eos/user/k/kpal/tprime_ww/full1_data2018/ws/allData.root -p none -f $cat --ext bkg --catOffset 0 --intLumi 59.83 --year 2018 --batch condor --queue microcentury --sigFile none --isData --fTest
        if $RUN; then
        ./runBackgroundScripts.sh -i /eos/user/k/kpal/tprime_ww/full1_data2018/ws/allData.root -p none -f $cat --ext bkg --catOffset 0 --intLumi 59.83 --year 2018 --batch condor --queue microcentury --sigFile none --isData --fTest
            echo   # to add new line after output of above script
        fi
    done
fi
