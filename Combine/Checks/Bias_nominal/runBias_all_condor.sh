for M in {7,8,9,10,11,12}00 {14,16,18,20,22,24,26}00;
do
    for d in 5 10 20 30
    do
        TPRIMEPROC=TprimeM"$M"Decay"$d"pct
        condor_wrap.py --jobFlavour workday --cmsenv -- ./runBias_.sh -y Run2 -s $TPRIMEPROC
    done
done

for M in {7,8,9,10,11,12}00 {14,16,18,20,22,24,26}00;
do
    for d in 5 10 20 30
    do
        TPRIMEPROC=TprimeM"$M"Decay"$d"pct
        condor_wrap.py --jobFlavour workday --cmsenv -- ./runBias_.sh -y 22plus23 -s $TPRIMEPROC
    done
done
