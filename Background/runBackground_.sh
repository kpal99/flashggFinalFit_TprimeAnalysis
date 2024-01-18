#!/bin/bash

echo "Running 600-700 background Model"

python RunBackgroundScripts.py --inputConfig config_600_700.py --mode fTestParallel

#python RunBackgroundScripts.py --inputConfig config_HiggsCR.py --mode fTestParallel


sleep 20s

echo "Running 800-1000 background Model"

python RunBackgroundScripts.py --inputConfig config_800_1000.py --mode fTestParallel

sleep 20s

echo "Running 1100-1200 background Model"

python RunBackgroundScripts.py --inputConfig config_1100_1200.py --mode fTestParallel
