#!/bin/bash

RUN=true
TEST=false
# get the options passed to the script
while getopts "nrhy:s:" opt;
do
case $opt in
    n) RUN=false;;
    t) TEST=true;;
    y) YEAR=$OPTARG;;
    s) TPRIMEPROC=$OPTARG;;
    h) echo "Usage: $0 [-n] [-h] -y YEAR -s TPRIMEPROC"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -h: print this help message"
       echo "  -y: year, can also take CSV i.e. '2016,2017,2018' "
       echo "  -s: signal process to use, TPRIMEPROC"
       exit 0;;
    \?) exit ;;
esac
done

cd $(dirname $0)
echo python3 RunPackager.py --cats THQLeptonicTag,THQHadronicTag --exts ${TPRIMEPROC} --batch local --queue espresso --massPoints 125 --outputExt packaged_${TPRIMEPROC}_${YEAR} --year $YEAR
if $RUN; then
    python3 RunPackager.py --cats THQLeptonicTag,THQHadronicTag --exts ${TPRIMEPROC} --batch condor --queue espresso --massPoints 125 --outputExt packaged_${TPRIMEPROC}_${YEAR} --year $YEAR
    echo   # to add new line after output of above script
fi
