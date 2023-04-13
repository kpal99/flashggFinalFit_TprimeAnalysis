#!/bin/bash

#label=_StatOnly
label=_Syst

#export i=$1
for mass in 600 625 650 675 700 800 900 1000 1100 1200
do 
		python makeDatacard.py --years 2016,2017,2018 --prune --ext Tprime${mass} --output Datacard_Tprime${mass}${label} --doSystematics
		sleep 2s
		mv Datacard_Tprime${mass}${label}\.txt Datacard_HadLep
done

echo "Making Hadronic Tag only Datacard"

for mass in 600 625 650 675 700 800 900 1000 1100 1200
do

    	if [ ! -d "yields_Tprime${mass}_Had" ]; then
        	mkdir yields_Tprime${mass}_Had
    	fi
		cp yields_Tprime${mass}/THQHadronicTag.pkl yields_Tprime${mass}_Had/
    	python makeDatacard.py --years 2016,2017,2018 --prune --ext Tprime${mass}_Had --output Datacard_Tprime${mass}_Had${label} --doSystematics
		sleep 2s
        mv Datacard_Tprime${mass}_Had${label}\.txt Datacard_Had/
done

echo "Making Leptonic Tag only Datacard"

for mass in 600 625 650 675 700 800 900 1000 1100 1200
do
        
        if [ ! -d "yields_Tprime${mass}_Lep" ]; then
                mkdir yields_Tprime${mass}_Lep
        fi  
        cp yields_Tprime${mass}/THQLeptonicTag.pkl yields_Tprime${mass}_Lep/
        python makeDatacard.py --years 2016,2017,2018 --prune --ext Tprime${mass}_Lep --output Datacard_Tprime${mass}_Lep${label} --doSystematics
        sleep 2s
        mv Datacard_Tprime${mass}_Lep${label}\.txt Datacard_Lep/
done
