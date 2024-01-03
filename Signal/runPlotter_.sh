for m in {7,10,14,20,24}00; for d in 10 30; for cat in THQLeptonicTag THQHadronicTag; python RunPlotter.py --procs all --years 2018 --cats $cat --ext packaged_TprimeM"$m"Decay"$d"pctSch

for m in {7,10,14,20,24}00; for d in 10 30; for cat in THQLeptonicTag THQHadronicTag; for extension in pdf png C; cp -v outdir_packaged_TprimeM"$m"Decay"$d"pctSch/Plots/smodel_"$cat"_2018."$extension" ~b2g/plots/finalFit/TprimeM"$m"Decay"$d"pctSch_smodel_"$cat"_2018."$extension"
