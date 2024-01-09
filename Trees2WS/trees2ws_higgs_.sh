#!/bin/bash

RUN=true
# get the options passed to the script
while getopts "n" opt;
do
case $opt in
    n) RUN=false;;
    \?) exit ;;
esac
done

for i in vbf tth ggh
do
    echo python trees2ws.py --inputConfig config_test.py --inputTreeFile ~eos/tprime_ww/full1_bkg_h/storeChanged/output_"$i".root --productionMode "$i" --year 2018
    if $RUN; then
        python trees2ws.py --inputConfig config_test.py --inputTreeFile ~eos/tprime_ww/full1_bkg_h/storeChanged/output_"$i".root --productionMode "$i" --year 2019
    fi
done
