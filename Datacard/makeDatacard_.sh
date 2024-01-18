#!/bin/bash

RUN=true
MKDIR=false
RUNSCRIPTS=false
LABEL=StatOnly
CATEGORY=false
# get the options passed to the script
while getopts "enrch" opt;
do
case $opt in
    #this is nice, you can process everything with syst and then switch off in this script
    e) LABEL="Syst --doSystematics ";;
    n) RUN=false;;
    r) RUNSCRIPTS=true;;
    c) CATEGORY=true;;
    h) echo "Usage: $0 [-e] [-c] [-n] [-r]"
       echo "  -h: print this help"
       echo "  -e: add systematics errors in datacards as well"
       echo "  -c: make seperate datacards for categories"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -r: run final scripts which are found in yields_*"
       exit 0;;
    \?) exit ;;
esac
done

WSDIR=/eos/user/k/kpal/tprime_ww/ws_2018
export PYTHONPATH=$PYTHONPATH:$CMSSW_BASE/src/flashggFinalFit/tools:$CMSSW_BASE/src/flashggFinalFit/Signal/tools
for m in {7,10,14,20,24}00
do
    for d in 10 30
    do
        if $RUNSCRIPTS; then
            echo python makeDatacard.py --years 2018 --prune --ext TprimeM"$m"Decay"$d"pctSch --output yields_TprimeM"$m"Decay"$d"pctSch/Datacard_TprimeM"$m"Decay"$d"pctSch_$LABEL
            # procs = all higgs background
            if $RUN; then
                python makeDatacard.py --years 2018 --prune --ext TprimeM"$m"Decay"$d"pctSch --output yields_TprimeM"$m"Decay"$d"pctSch/Datacard_TprimeM"$m"Decay"$d"pctSch_$LABEL
                # don't require --doSystematics flag, incorporated in $LABEL variable, see help
                sleep 1 # else this command is not completed and we are moving to categories and they don't find files
                echo   # to add new line after output of above script
            fi
            if $CATEGORY; then
                for cat in THQLeptonicTag THQHadronicTag
                do
                    # check whether directory is present or not, if not create and cp Hadronic .pkl to it
                    if [ ! -d yields_TprimeM"$m"Decay"$d"pctSch_$cat ]; then
                        echo mkdir -v yields_TprimeM"$m"Decay"$d"pctSch_$cat
                    fi
                    echo ln -svf yields_TprimeM"$m"Decay"$d"pctSch/$cat.pkl yields_TprimeM"$m"Decay"$d"pctSch_$cat/$cat.pkl
                    echo python makeDatacard.py --years 2018 --prune --ext TprimeM"$m"Decay"$d"pctSch_$cat --output yields_TprimeM"$m"Decay"$d"pctSch_$cat/Datacard_TprimeM"$m"Decay"$d"pctSch_"$cat"_$LABEL
                    if $RUN; then
                        if [ ! -d yields_TprimeM"$m"Decay"$d"pctSch_$cat ]; then
                            mkdir -v yields_TprimeM"$m"Decay"$d"pctSch_$cat
                        fi
                        ln -svf yields_TprimeM"$m"Decay"$d"pctSch/$cat.pkl yields_TprimeM"$m"Decay"$d"pctSch_$cat/$cat.pkl
                        python makeDatacard.py --years 2018 --prune --ext TprimeM"$m"Decay"$d"pctSch_$cat --output yields_TprimeM"$m"Decay"$d"pctSch_$cat/Datacard_TprimeM"$m"Decay"$d"pctSch_"$cat"_$LABEL
                        echo   # to add new line after output of above script
                    fi
                done
            fi
        fi
    done
done
