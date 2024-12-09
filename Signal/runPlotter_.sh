#!/bin/bash

RUN=true
TEST=false
# get the options passed to the script
while getopts "nhty:p:" opt;
do
case $opt in
    n) RUN=false;;
    y) YEAR=$OPTARG;;
    t) TEST=true;;
    p) PLOTDIR=$OPTARG;;
    h) echo "Usage: $0 [-n] [-y YEAR] [-h]"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -y: year, can also take CSV i.e. '2016,2017,2018' "
       echo "  -t: test, run for single mass, decay width"
       echo "  -h: print this help message"
       exit 0;;
    \?) exit ;;
esac
done

for m in  {7..12}00 {14,16,18,20}00 #{22,24,26}00;
do
    for d in 5 #20
    do
        TPRIMEPROC=TprimeM"$m"Decay"$d"pct
        for cat in THQLeptonicTag THQHadronicTag
        do
            echo python3 RunPlotter.py --procs all --cats $cat --ext packaged_$TPRIMEPROC --years $YEAR
            if $RUN; then
                python3 RunPlotter.py --procs all --cats $cat --ext packaged_$TPRIMEPROC --years $YEAR
                echo   # to add new line after output of above script
            fi
            if [ $PLOTDIR ] && $RUN ; then
                for extension in pdf png C root
                do
                    cp -v outdir_packaged_$TPRIMEPROC/Plots/smodel_"$cat"_$YEAR."$extension" $PLOTDIR/finalFit/"$TPRIMEPROC"_"$cat"_$YEAR."$extension"
                done
            fi
        done
        [ $TEST = true ] && break
    done
    [ $TEST = true ] && break
    echo
done
