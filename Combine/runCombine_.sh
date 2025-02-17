#!/bin/bash

RUN=true
TEST=false
# get the options passed to the script
while getopts "nht" opt;
do
case $opt in
    n) RUN=false;;
    t) TEST=true;;
    h) echo "Usage: $0 [-n] [-h] [-t]"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -t: run test scripts"
       echo "  -h: print this help message"
       exit 0;;
    \?) exit ;;
esac
done

FINALFITDIR=$CMSSW_BASE/src/flashggFinalFit/
for m in  2000 # {22,24,26}00;
#for m in  {7..12}00 {14,16,18,20}00 # {22,24,26}00;
do
    for d in 5 #20
    do
        TPRIMEPROC=TprimeM"$m"Decay"$d"pct
        echo text2workspace.py Datacard_$TPRIMEPROC.txt -o Datacard_"$TPRIMEPROC"_mu_inclusive.root -m 125 higgsMassRange=122,128
        echo combine --expectSignal 1 --toys -1 --saveWorkspace --freezeParameters MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --method AsymptoticLimits -m 125.38 --datacard Datacard_"$TPRIMEPROC"_mu_inclusive.root --name _$TPRIMEPROC
        if $RUN; then
            echo   # to add new line after output of above script
            text2workspace.py Datacard_$TPRIMEPROC.txt -o Datacard_"$TPRIMEPROC"_mu_inclusive.root -m 125 higgsMassRange=122,128
            combine --expectSignal 1 --toys -1 --saveWorkspace --freezeParameters MH --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --method AsymptoticLimits -m 125.38 --datacard Datacard_"$TPRIMEPROC"_mu_inclusive.root --name _$TPRIMEPROC
            fi
        [ $TEST = true ] && break
    done
    [ $TEST = true ] && break
done
