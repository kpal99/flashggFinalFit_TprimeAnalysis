#!/bin/bash

RUN=true
# get the options passed to the script
while getopts "nhy:s:" opt;
do
case $opt in
    n) RUN=false;;
    y) YEAR=$OPTARG;;
    s) TPRIMEPROC=$OPTARG;;
    h) echo "Usage: $0 [-n] [-h] -y YEAR -s TPRIMEPROC"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -y: year"
       echo "  -s: signal process to use, TPRIMEPROC"
       echo "  -h: print this help message"
       exit 0;;
    \?) exit ;;
esac
done

cd $(dirname $0)
FINALFITDIR=$CMSSW_BASE/src/flashggFinalFit/

echo text2workspace.py Datacard_${TPRIMEPROC}_${YEAR}.txt -o Datacard_${TPRIMEPROC}_${YEAR}_mu_inclusive.root -m 125 higgsMassRange=122,128
echo combine --expectSignal 1 --toys -1 --saveWorkspace --freezeParameters MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --method AsymptoticLimits -m 125.38 --datacard Datacard_${TPRIMEPROC}_${YEAR}_mu_inclusive.root --name _${TPRIMEPROC}_${YEAR}
if $RUN; then
    echo   # to add new line after output of above script
    text2workspace.py Datacard_${TPRIMEPROC}_${YEAR}.txt -o Datacard_${TPRIMEPROC}_${YEAR}_mu_inclusive.root -m 125 higgsMassRange=122,128
    combine --expectSignal 1 --toys -1 --saveWorkspace --freezeParameters MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --method AsymptoticLimits -m 125.38 --datacard Datacard_${TPRIMEPROC}_${YEAR}_mu_inclusive.root --name _${TPRIMEPROC}_${YEAR}
fi
