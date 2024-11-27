#!/bin/bash

RUN=true
TEST=false
# get the options passed to the script
while getopts "nhtd:y:p:" opt;
do
case $opt in
    n) RUN=false;;
    d) INPUTDIR=$OPTARG;;
    y) YEAR=$OPTARG;;
    t) TEST=true;;
    p) PLOTDIR=$OPTARG;;
    h) echo "Usage: $0 [-n] [-d INPUTDIR] [-y YEAR] [-t] [-h] [-p PLOTDIR]"
       echo "  -d: input directory"
       echo "  -y: year"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -t: test, run for single mass, decay width"
       echo "  -p: plot directory to sync plots to"
       echo "  -h: print this help message"
       exit 0;;
    \?) exit ;;
esac
done

# for --skipWV, see
# https://github.com/cms-analysis/flashggFinalFit/blob/dev_fggfinalfits_lite/Signal/README.md?plain=1#L37
for m in  {7..12}00 #{14,16,18,20,22,24,26}00;
do
    for d in 5 #20
    do
        TPRIMEPROC=TprimeM"$m"Decay"$d"pct
        echo python3 make_config.py --inputWSDir $INPUTDIR/$TPRIMEPROC/ws_$TPRIMEPROC --procs $TPRIMEPROC --year 2017
        # by the nature of echo and shell, we are not seeing "" in shell, but it's being passed in python correctly, thus "" in '' for echo
        echo python3 RunSignalScripts.py --inputConfig config/$TPRIMEPROC.py --mode fTest --modeOpts '"--doPlots --nProcsToFTest -1 --skipWV"'
        if $RUN; then
            python3 make_config.py --inputWSDir $INPUTDIR/$TPRIMEPROC/ws_$TPRIMEPROC --procs $TPRIMEPROC --year 2017
            python3 RunSignalScripts.py --inputConfig config/$TPRIMEPROC.py --mode fTest --modeOpts "--doPlots --nProcsToFTest -1 --skipWV"
        fi
        #
        # if PLOTDIR is defined then copy plots to PLOTDIR
        if [ $PLOTDIR ]; then
          mkdir -pv $PLOTDIR/fTest/$TPRIMEPROC
          rsync -ah --quiet --stats outdir_$TPRIMEPROC/fTest/Plots/ $PLOTDIR/fTest/$TPRIMEPROC/
          cp -v $PLOTDIR/fTest/index.php $PLOTDIR/fTest/$TPRIMEPROC
        fi
        echo   # to add new line after output of above script
        [ $TEST = true ] && break
    done
    [ $TEST = true ] && break
done
