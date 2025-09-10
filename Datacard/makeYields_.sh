#!/bin/bash

RUN=true
CATEXT='""'
# get the options passed to the script
while getopts "nhd:s:y:c:" opt;
do
case $opt in
    n) RUN=false;;
    d) INPUTDIR=$OPTARG;;
    s) TPRIMEPROC=$OPTARG;;
    y) YEAR=$OPTARG;;
    c) CATEXT=$OPTARG;;
    h) echo "Usage: $0 [-n] [-h] [-t] [ -d INPUTDIR ] -s TPRIMEPROC -y YEAR [ -c CATEXT ]"
       echo "  -d: input selection directory"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -s: sample process to use, TPRIMEPROC"
       echo "  -y: year"
       echo "  -c: category extension, CATEXT"
       echo "  -h: print this help message"
       exit 0;;
    \?) exit ;;
esac
done

cd $(dirname $0)
PROCS="$TPRIMEPROC"Sch,GG2H,TTH,VBF,VH
# if year is 2016 or 2017 change PROCS
if [ $YEAR = "2016" ]; then
    PROCS=$PROCS,THQ
elif [ $YEAR = "2017" ]; then
    PROCS=$PROCS,THQ
fi

echo ln -svf systematics_Tprime_$YEAR.py systematics.py
echo python3 RunYields.py --inputWSDirMap $YEAR=$INPUTDIR/$TPRIMEPROC/ws/ --cats auto --catExt $CATEXT --procs $PROCS --ext ${TPRIMEPROC}_${YEAR} --skipCOWCorr --batch local --sigModelWSDir ./Models/$YEAR/$TPRIMEPROC/signal --bkgModelWSDir ./Models/$YEAR/$TPRIMEPROC/background
if $RUN; then
    echo   # to add new line after output of above script
    ln -svf systematics_Tprime_$YEAR.py systematics.py
    python3 RunYields.py --inputWSDirMap $YEAR=$INPUTDIR/$TPRIMEPROC/ws/ --cats auto --catExt $CATEXT --procs $PROCS --ext ${TPRIMEPROC}_${YEAR} --skipCOWCorr --batch local --sigModelWSDir ./Models/$YEAR/$TPRIMEPROC/signal --bkgModelWSDir ./Models/$YEAR/$TPRIMEPROC/background
fi
