for m in {7,10,14,20,24}00; for d in 10 30; python RunPackager.py --cats THQLeptonicTag,THQHadronicTag --exts TprimeM"$m"Decay"$d"pctSch --mergeYears --batch condor --queue espresso --massPoints 125 --outputExt packaged_TprimeM"$m"Decay"$d"pctSch --printOnly

for m in {7,10,14,20,24}00; for d in 10 30; for cat in THQLeptonicTag THQHadronicTag; python /afs/cern.ch/work/k/kpal/private/flashggFinalFit-setup/CMSSW_10_2_13/src/flashggFinalFit/Signal/scripts/packageSignal.py --cat $cat --outputExt packaged_TprimeM"$m"Decay"$d"pctSch --massPoints 125 --exts TprimeM"$m"Decay"$d"pctSch --mergeYears
