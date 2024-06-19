#!/bin/bash

RUN=true
MKDIR=false
RUNCREATEDSCRIPTS=false
# get the options passed to the script
while getopts "mnrhy:w:" opt;
do
case $opt in
    m) MKDIR=true;;
    n) RUN=false;;
    r) RUNCREATEDSCRIPTS=true;;
    y) YEAR=$OPTARG;;
    w) INPUTWS=$OPTARG;;
    h) echo "Usage: $0 [-m] [-n] [-r] [-y YEAR] [-w INPUTDIR] [-h]"
       echo "  -h: print this help"
       echo "  -m: create required directories"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -y: year 2016,2017,2018,Combined"
       echo "  -w: input directory"
       echo "  -r: run final scripts which are found in outdir_*"
       exit 0;;
    \?) exit ;;
esac
done

if $MKDIR; then
    echo python3 make_config.py --inputWS $INPUTWS --year $YEAR
    echo python3 RunBackgroundScripts.py --inputConfig config/config_$YEAR.py --mode fTestParallel --printOnly
    if $RUN; then
        python3 make_config.py --inputWS $INPUTWS --year $YEAR
        python3 RunBackgroundScripts.py --inputConfig config/config_$YEAR.py --mode fTestParallel --printOnly
        echo   # to add new line after output of above script
    fi
fi
if $RUNCREATEDSCRIPTS; then
    for arg in 0 1
    do
        echo outdir_bkg/fTestParallel/jobs/condor_fTestParallel_bkg.sh $arg
        if $RUN; then
            outdir_bkg/fTestParallel/jobs/condor_fTestParallel_bkg.sh $arg
            echo   # to add new line after output of above script
        fi
    done
fi
