#!/bin/bash

#export i=$1
	python makeDatacard.py --years 2016,2017,2018 --prune --ext HiggsCR --output Datacard_HiggsCR --doSystematics
sleep 2s
	cp Datacard_HiggsCR\.txt Datacard_HiggsCR_HadLep

echo "Making Hadronic Tag only Datacard"

    	if [ ! -d "yields_HiggsCR_Had" ]; then
        	mkdir yields_HiggsCR_Had
    	fi
	cp yields_HiggsCR/THQHadronicTag.pkl yields_HiggsCR_Had/
        python makeDatacard.py --years 2016,2017,2018 --prune --ext HiggsCR_Had --output Datacard_HiggsCR_Had --doSystematics
	sleep 2s
        mv Datacard_HiggsCR_Had\.txt Datacard_HiggsCR_Had/

echo "Making Leptonic Tag only Datacard"

        if [ ! -d "yields_HiggsCR_Lep" ]; then
                mkdir yields_HiggsCR_Lep
        fi  
        cp yields_HiggsCR/THQLeptonicTag.pkl yields_HiggsCR_Lep/
        python makeDatacard.py --years 2016,2017,2018 --prune --ext HiggsCR_Lep --output Datacard_HiggsCR_Lep --doSystematics
        sleep 2s
        mv Datacard_HiggsCR_Lep\.txt Datacard_HiggsCR_Lep/
