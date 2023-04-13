#!/bin/bash

for i in 600 #625 650 675 700 800 900 1000 1100 1200
do
	python makeToysForBias.py --inputWSFile Models_Tprime${i}/Datacard_Tprime${i}_StatOnly.root --ext Tprime${i} --nToys 1000 --POIs r --batch condor --queue espresso --maxExpectSignal 2
done
