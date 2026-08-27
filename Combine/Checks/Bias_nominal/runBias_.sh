echo "==> Running combineCards..."
combineCards.py \
    ../../Datacard_TprimeM1800Decay5pct_Run2_withSyst.txt \
    --include-channel Hadronic \
    > ../../Datacard_TprimeM1800Decay5pct_Run2_withSyst_Hadronic.txt
combineCards.py \
    ../../Datacard_TprimeM1800Decay5pct_Run2_withSyst.txt \
    --include-channel Leptonic \
    > ../../Datacard_TprimeM1800Decay5pct_Run2_withSyst_Leptonic.txt

echo -e "\n==> Cleaning datacard with sed..."
sed -i '/pdfindex_Leptonic/d' ../../Datacard_TprimeM1800Decay5pct_Run2_withSyst_Hadronic.txt
sed -i '/pdfindex_Hadronic/d' ../../Datacard_TprimeM1800Decay5pct_Run2_withSyst_Leptonic.txt

echo -e "\n==> Creating directory..."
mkdir -pv Datacard/TprimeM1800Decay5pct_Run2_Hadronic/
mkdir -pv Datacard/TprimeM1800Decay5pct_Run2_Leptonic/

echo -e "\n==> Converting text datacard to workspace..."
text2workspace.py \
    ../../Datacard_TprimeM1800Decay5pct_Run2_withSyst_Hadronic.txt \
    --out Datacard/TprimeM1800Decay5pct_Run2_Hadronic/Datacard_TprimeM1800Decay5pct_Run2_withSyst_Hadronic.root \
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
    ../../Datacard_TprimeM1800Decay5pct_Run2_withSyst_Leptonic.txt \
    --out Datacard/TprimeM1800Decay5pct_Run2_Leptonic/Datacard_TprimeM1800Decay5pct_Run2_withSyst_Leptonic.root \
    --mass 125 \
    higgsMassRange=122,128 \
    --physics-model HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
    --physics-option map=".*/Tprime.*:r[1,-1,1000]" \
    --physics-option map=".*/ggh.*:1" \
    --physics-option map=".*/VH.*:1" \
    --physics-option map=".*/tHq.*:1" \
    --physics-option map=".*/ttH.*:1" \
    --physics-option map=".*/qqH.*:1"

echo -e "\n==> Running bias study (toys)..."
python3 RunBiasStudy.py \
    --split 1000 \
    --datacard Datacard/TprimeM1800Decay5pct_Run2_Hadronic/Datacard_TprimeM1800Decay5pct_Run2_withSyst_Hadronic.root \
    --toys \
    --expectSignal 1 \
    --subDir TprimeM1800Decay5pctRun2_Hadronic_mu1
python3 RunBiasStudy.py \
    --split 1000 \
    --datacard Datacard/TprimeM1800Decay5pct_Run2_Leptonic/Datacard_TprimeM1800Decay5pct_Run2_withSyst_Leptonic.root \
    --toys \
    --expectSignal 1 \
    --subDir TprimeM1800Decay5pctRun2_Leptonic_mu1

echo -e "\n==> Running bias study (fits)..."
python3 RunBiasStudy.py \
    --split 1000 \
    --datacard Datacard/TprimeM1800Decay5pct_Run2_Hadronic/Datacard_TprimeM1800Decay5pct_Run2_withSyst_Hadronic.root \
    --fits \
    --expectSignal 1 \
    --subDir TprimeM1800Decay5pct_Run2_Hadronic_mu1 \
    --combineOptions "--cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --freezeParameters MH"

python3 RunBiasStudy.py \
    --split 1000 \
    --datacard Datacard/TprimeM1800Decay5pct_Run2_Leptonic/Datacard_TprimeM1800Decay5pct_Run2_withSyst_Leptonic.root \
    --fits \
    --expectSignal 1 \
    --subDir TprimeM1800Decay5pct_Run2_Leptonic_mu1 \
    --combineOptions "--cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --freezeParameters MH"

echo -e "\n==> Running bias study (plots)..."
python3 RunBiasStudy.py \
    --split 1000 \
    --datacard Datacard/TprimeM1800Decay5pct_Run2_Hadronic/Datacard_TprimeM1800Decay5pct_Run2_withSyst_Hadronic.root \
    --plots \
    --gaussianFit \
    --expectSignal 1 \
    --subDir TprimeM1800Decay5pct_Run2_Hadronic_mu1 \
    2>&1 | tee BiasPlots/output_TprimeM1800Decay5pct_Run2_Hadronic_mu1.log

python3 RunBiasStudy.py \
    --split 1000 \
    --datacard Datacard/TprimeM1800Decay5pct_Run2_Leptonic/Datacard_TprimeM1800Decay5pct_Run2_withSyst_Leptonic.root \
    --plots \
    --gaussianFit \
    --expectSignal 1 \
    --subDir TprimeM1800Decay5pct_Run2_Leptonic_mu1 \
    2>&1 | tee BiasPlots/output_TprimeM1800Decay5pct_Run2_Leptonic_mu1.log
