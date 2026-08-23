#!/bin/bash

RUN=true
systExt="withSyst"
# get the options passed to the script
while getopts "hy:s:p:" opt;
do
case $opt in
    y) YEAR=$OPTARG;;
    s) TPRIMEPROC=$OPTARG;;
    p) PLOTDIR=$OPTARG;;
    h) echo "Usage: $0 [-n] [-h] -y YEAR -s TPRIMEPROC"
       echo "  -y: year"
       echo "  -s: signal process to use, TPRIMEPROC"
       echo "  -p: plot directory"
       echo "  -h: print this help message"
       exit 0;;
    \?) exit ;;
esac
done

cd $(dirname $0)
FINALFITDIR=$CMSSW_BASE/src/flashggFinalFit/
DATACARD=Datacard_${TPRIMEPROC}_${YEAR}_${systExt}_mu_inclusive.root

mkdir -pv Impact/${TPRIMEPROC}_${YEAR}
cp -v $DATACARD Impact/${TPRIMEPROC}_${YEAR}/
cd Impact/${TPRIMEPROC}_${YEAR}

COMMON_OPTS="--cminDefaultMinimizerStrategy 0 \
--X-rtd MINIMIZER_freezeDisassociatedParams \
--X-rtd MINIMIZER_multiMin_hideConstants \
--X-rtd MINIMIZER_multiMin_maskConstraints \
--X-rtd MINIMIZER_multiMin_maskChannels=2"

# Run the initial fit to find the best-fit POI
combineTool.py -M Impacts \
    -d $DATACARD \
    -m 125.38 \
    --doInitialFit \
    --robustFit 1 \
    -t -1 \
    --setParameters r=1 \
    --setParameterRanges r=-0.5,3 \
    $COMMON_OPTS \
    --freezeParameters MH


# Run all nuisance parameter fits locally (this may take time)
combineTool.py -M Impacts \
    -d $DATACARD \
    -m 125.38 \
    --doFits \
    --robustFit 1 \
    -t -1 \
    --setParameters r=1 \
    --setParameterRanges r=-0.5,3 \
    $COMMON_OPTS \
    --freezeParameters MH

# Collect all fit results into one JSON file
combineTool.py -M Impacts \
    -d $DATACARD \
    -m 125.38 \
    -o impacts.json

# 7. Plot the initial impacts including all parameters
plotImpacts.py \
    -i impacts.json \
    -o impacts_allParams

# 8. Correct impacts JSON to drop background-model parameters
python3 ../../../Plots/correctImpacts.py \
    --impactsJson impacts.json \
    --dropBkgModelParams \
    --frozenParam MH

# 9. Plot the final impact plot (PDF + PNG)
plotImpacts.py \
    -i impacts_corrected_dropBkgModelParams.json \
    -o impacts_corrected_dropBkgModelParams

# copy to plot dir
mkdir -pv $PLOTDIR/$YEAR/$TPRIMEPROC
cp -v $PLOTDIR/index.php $PLOTDIR/$YEAR/
cp -v $PLOTDIR/index.php $PLOTDIR/$YEAR/$TPRIMEPROC

cp -v impacts_allParams.pdf $PLOTDIR/$YEAR/$TPRIMEPROC/
convert -density 300 impacts_allParams.pdf -quality 90 -background white -alpha remove -trim +repage impacts_allParams-%02d.png
convert impacts_allParams-*.png -append impacts_allParams.png
cp -v impacts_allParams.png $PLOTDIR/$YEAR/$TPRIMEPROC/

cp -v impacts_corrected_dropBkgModelParams.pdf $PLOTDIR/$YEAR/$TPRIMEPROC/
convert -density 300 impacts_corrected_dropBkgModelParams.pdf -quality 90 -background white -alpha remove -trim +repage impacts_corrected_dropBkgModelParams-%02d.png
convert impacts_corrected_dropBkgModelParams-*.png -append impacts_corrected_dropBkgModelParams.png
cp -v impacts_corrected_dropBkgModelParams.png $PLOTDIR/$YEAR/$TPRIMEPROC/
