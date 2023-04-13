#!/bin/bash

for i in 600 625 650 675 700 800 900 1000 1100 1200
do
	python makeGoFtest.py --inputWSFile Models_Tprime${i}/Datacard_Tprime${i}_Syst.root --ext Tprime${i} --nToys 500 --POIs r --batch condor --queue workday 
done
