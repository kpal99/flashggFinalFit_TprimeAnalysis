#!/bin/bash

while getopts "hy:s:" opt;
do
case $opt in
    y) YEAR=$OPTARG;;
    s) TPRIMEPROC=$OPTARG;;
    h) echo "Usage: $0 [-h] -y YEAR -s TPRIMEPROC"
       echo "  -y: year"
       echo "  -s: signal process to use, TPRIMEPROC"
       echo "  -h: print this help message"
       exit 0;;
    \?) exit ;;
esac
done

cd $(dirname "$0")

source ../../../setup.sh

echo "==> Running combineCards..."
combineCards.py \
    ../../Datacard_"$TPRIMEPROC"_"$YEAR"_withSyst.txt \
    --include-channel Hadronic \
    > ../../Datacard_"$TPRIMEPROC"_"$YEAR"_withSyst_Hadronic.txt
combineCards.py \
    ../../Datacard_"$TPRIMEPROC"_"$YEAR"_withSyst.txt \
    --include-channel Leptonic \
    > ../../Datacard_"$TPRIMEPROC"_"$YEAR"_withSyst_Leptonic.txt

echo -e "\n==> Cleaning datacard with sed..."
sed -i '/pdfindex_Leptonic/d' ../../Datacard_"$TPRIMEPROC"_"$YEAR"_withSyst_Hadronic.txt
sed -i '/pdfindex_Hadronic/d' ../../Datacard_"$TPRIMEPROC"_"$YEAR"_withSyst_Leptonic.txt

echo -e "\n==> Creating directory..."
mkdir -pv Datacard/"$TPRIMEPROC"_"$YEAR"_Hadronic/
mkdir -pv Datacard/"$TPRIMEPROC"_"$YEAR"_Leptonic/

echo -e "\n==> Converting text datacard to workspace..."
echo text2workspace.py \
    ../../Datacard_"$TPRIMEPROC"_"$YEAR"_withSyst_Hadronic.txt \
    --out Datacard/"$TPRIMEPROC"_"$YEAR"_Hadronic/Datacard_"$TPRIMEPROC"_"$YEAR"_withSyst_Hadronic.root \
    --mass 125 \
    higgsMassRange=122,128 \
    --physics-model HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
    --physics-option map=".*/Tprime.*:r[1,-1,1000]" \
    --physics-option map=".*/ggh.*:1" \
    --physics-option map=".*/VH.*:1" \
    --physics-option map=".*/tHq.*:1" \
    --physics-option map=".*/ttH.*:1" \
    --physics-option map=".*/qqH.*:1"
text2workspace.py \
    ../../Datacard_"$TPRIMEPROC"_"$YEAR"_withSyst_Hadronic.txt \
    --out Datacard/"$TPRIMEPROC"_"$YEAR"_Hadronic/Datacard_"$TPRIMEPROC"_"$YEAR"_withSyst_Hadronic.root \
    --mass 125 \
    higgsMassRange=122,128 \
    --physics-model HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
    --physics-option map=".*/Tprime.*:r[1,-1,1000]" \
    --physics-option map=".*/ggh.*:1" \
    --physics-option map=".*/VH.*:1" \
    --physics-option map=".*/tHq.*:1" \
    --physics-option map=".*/ttH.*:1" \
    --physics-option map=".*/qqH.*:1"

echo text2workspace.py \
    ../../Datacard_"$TPRIMEPROC"_"$YEAR"_withSyst_Leptonic.txt \
    --out Datacard/"$TPRIMEPROC"_"$YEAR"_Leptonic/Datacard_"$TPRIMEPROC"_"$YEAR"_withSyst_Leptonic.root \
    --mass 125 \
    higgsMassRange=122,128 \
    --physics-model HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
    --physics-option map=".*/Tprime.*:r[1,-1,1000]" \
    --physics-option map=".*/ggh.*:1" \
    --physics-option map=".*/VH.*:1" \
    --physics-option map=".*/tHq.*:1" \
    --physics-option map=".*/ttH.*:1" \
    --physics-option map=".*/qqH.*:1"
text2workspace.py \
    ../../Datacard_"$TPRIMEPROC"_"$YEAR"_withSyst_Leptonic.txt \
    --out Datacard/"$TPRIMEPROC"_"$YEAR"_Leptonic/Datacard_"$TPRIMEPROC"_"$YEAR"_withSyst_Leptonic.root \
    --mass 125 \
    higgsMassRange=122,128 \
    --physics-model HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
    --physics-option map=".*/Tprime.*:r[1,-1,1000]" \
    --physics-option map=".*/ggh.*:1" \
    --physics-option map=".*/VH.*:1" \
    --physics-option map=".*/tHq.*:1" \
    --physics-option map=".*/ttH.*:1" \
    --physics-option map=".*/qqH.*:1"

for mu in {1..10}
do
echo -e "\n==> Running bias study (toys)..."
python3 RunBiasStudy.py \
    --split 1000 \
    --datacard Datacard/"$TPRIMEPROC"_"$YEAR"_Hadronic/Datacard_"$TPRIMEPROC"_"$YEAR"_withSyst_Hadronic.root \
    --toys \
    --expectSignal 1 \
    --subDir "$TPRIMEPROC"_"$YEAR"_Hadronic_mu"$mu"
python3 RunBiasStudy.py \
    --split 1000 \
    --datacard Datacard/"$TPRIMEPROC"_"$YEAR"_Leptonic/Datacard_"$TPRIMEPROC"_"$YEAR"_withSyst_Leptonic.root \
    --toys \
    --expectSignal 1 \
    --subDir "$TPRIMEPROC"_"$YEAR"_Leptonic_mu"$mu"

echo -e "\n==> Running bias study (fits)..."
python3 RunBiasStudy.py \
    --split 1000 \
    --datacard Datacard/"$TPRIMEPROC"_"$YEAR"_Hadronic/Datacard_"$TPRIMEPROC"_"$YEAR"_withSyst_Hadronic.root \
    --fits \
    --expectSignal 1 \
    --subDir "$TPRIMEPROC"_"$YEAR"_Hadronic_mu"$mu" \
    --combineOptions "--cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --freezeParameters MH"

python3 RunBiasStudy.py \
    --split 1000 \
    --datacard Datacard/"$TPRIMEPROC"_"$YEAR"_Leptonic/Datacard_"$TPRIMEPROC"_"$YEAR"_withSyst_Leptonic.root \
    --fits \
    --expectSignal 1 \
    --subDir "$TPRIMEPROC"_"$YEAR"_Leptonic_mu"$mu" \
    --combineOptions "--cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --freezeParameters MH"

echo -e "\n==> Running bias study (plots)..."
python3 RunBiasStudy.py \
    --split 1000 \
    --datacard Datacard/"$TPRIMEPROC"_"$YEAR"_Hadronic/Datacard_"$TPRIMEPROC"_"$YEAR"_withSyst_Hadronic.root \
    --plots \
    --gaussianFit \
    --expectSignal 1 \
    --subDir "$TPRIMEPROC"_"$YEAR"_Hadronic_mu"$mu" \
    2>&1 | tee BiasPlots/output_"$TPRIMEPROC"_"$YEAR"_Hadronic_mu"$mu".log

python3 RunBiasStudy.py \
    --split 1000 \
    --datacard Datacard/"$TPRIMEPROC"_"$YEAR"_Leptonic/Datacard_"$TPRIMEPROC"_"$YEAR"_withSyst_Leptonic.root \
    --plots \
    --gaussianFit \
    --expectSignal 1 \
    --subDir "$TPRIMEPROC"_"$YEAR"_Leptonic_mu"$mu" \
    2>&1 | tee BiasPlots/output_"$TPRIMEPROC"_"$YEAR"_Leptonic_mu"$mu".log
done
