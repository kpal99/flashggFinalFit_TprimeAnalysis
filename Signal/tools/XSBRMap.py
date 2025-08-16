# Python script to hold XS * BR for normalisation of signal models
from collections import OrderedDict as od
from commonObjects import *
  
# Add analyses to globalReplacementMap. See "STXS" as an example
globalXSBRMap = od()

# For case of fixed xs/br Use 'mode':constant 'factor':X e.g.
#globalXSBRMap['example'] = od()
#globalXSBRMap['example']['decay'] = {'mode':'constant','factor':1}
#globalXSBRMap['example']['PROCNAME'] = {'mode':'constant','factor':0.001}

# For case of inclusive production mode then have no additional factor beyond V branching ratios
globalXSBRMap['example'] = od()
globalXSBRMap['example']['decay'] = {'mode':'hgg'}
globalXSBRMap['example']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['example']['VBF'] = {'mode':'qqH'}
globalXSBRMap['example']['WH2HQQ'] = {'mode':'WH','factor':BR_W_qq}
globalXSBRMap['example']['ZH2HQQ'] = {'mode':'qqZH','factor':BR_Z_qq}
globalXSBRMap['example']['QQ2HLNU'] = {'mode':'WH','factor':BR_W_lnu}
globalXSBRMap['example']['QQ2HLL'] = {'mode':'qqZH','factor':(BR_Z_ll+BR_Z_nunu)}
globalXSBRMap['example']['GG2HQQ'] = {'mode':'ggZH','factor':BR_Z_qq}
globalXSBRMap['example']['GG2HLL'] = {'mode':'ggZH','factor':BR_Z_ll}
globalXSBRMap['example']['GG2HNUNU'] = {'mode':'ggZH','factor':BR_Z_nunu}
globalXSBRMap['example']['TTH'] = {'mode':'ttH'}
globalXSBRMap['example']['BBH'] = {'mode':'bbH'}
globalXSBRMap['example']['THQ'] = {'mode':'tHq'}
globalXSBRMap['example']['THW'] = {'mode':'tHW'}
# ...

# For tutorial analysis: use 13.6 TeV cross sections and branching fraction
# These are not yet stored in Combine, so we will use the constant-factor approach 
# Setting the values at MH=125.38 GeV
globalXSBRMap['tutorial'] = od()
globalXSBRMap['tutorial']['decay'] = {'mode':'hgg'}
globalXSBRMap['tutorial']['GG2H'] = {'mode':'constant', 'factor':51.96}
globalXSBRMap['tutorial']['VBF'] = {'mode':'constant', 'factor':4.067}

# STXS analysis: add factor for bin composition
globalXSBRMap['STXS'] = od()
globalXSBRMap['STXS']['decay'] = {'mode':'hgg'}
# ggH STXS stage 1.2 bins
globalXSBRMap['STXS']['GG2H_FWDH'] = {'mode':'ggH','factor':0.0809}
globalXSBRMap['STXS']['GG2H_PTH_200_300'] = {'mode':'ggH','factor':0.0098}
globalXSBRMap['STXS']['GG2H_PTH_300_450'] = {'mode':'ggH','factor':0.0025}
globalXSBRMap['STXS']['GG2H_PTH_450_650'] = {'mode':'ggH','factor':0.0003}
globalXSBRMap['STXS']['GG2H_PTH_GT650'] = {'mode':'ggH','factor':0.0001}
globalXSBRMap['STXS']['GG2H_0J_PTH_0_10'] = {'mode':'ggH','factor':0.1387}
globalXSBRMap['STXS']['GG2H_0J_PTH_GT10'] = {'mode':'ggH','factor':0.3940}
globalXSBRMap['STXS']['GG2H_1J_PTH_0_60'] = {'mode':'ggH','factor':0.1477}
globalXSBRMap['STXS']['GG2H_1J_PTH_60_120'] = {'mode':'ggH','factor':0.1023}
globalXSBRMap['STXS']['GG2H_1J_PTH_120_200'] = {'mode':'ggH','factor':0.0182}
globalXSBRMap['STXS']['GG2H_GE2J_MJJ_0_350_PTH_0_60'] = {'mode':'ggH','factor':0.0256}
globalXSBRMap['STXS']['GG2H_GE2J_MJJ_0_350_PTH_60_120'] = {'mode':'ggH','factor':0.0410}
globalXSBRMap['STXS']['GG2H_GE2J_MJJ_0_350_PTH_120_200'] = {'mode':'ggH','factor':0.0188}
globalXSBRMap['STXS']['GG2H_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25'] = {'mode':'ggH','factor':0.0063}
globalXSBRMap['STXS']['GG2H_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25'] = {'mode':'ggH','factor':0.0077}
globalXSBRMap['STXS']['GG2H_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25'] = {'mode':'ggH','factor':0.0028}
globalXSBRMap['STXS']['GG2H_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25'] = {'mode':'ggH','factor':0.0032}
# ggZH hadronic: merged with ggH STXS stage 1.2 bins in fit
globalXSBRMap['STXS']['GG2HQQ_FWDH'] = {'mode':'ggZH','factor':0.0273*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_PTH_200_300'] = {'mode':'ggZH','factor':0.1393*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_PTH_300_450'] = {'mode':'ggZH','factor':0.0386*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_PTH_450_650'] = {'mode':'ggZH','factor':0.0077*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_PTH_GT650'] = {'mode':'ggZH','factor':0.0020*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_0J_PTH_0_10'] = {'mode':'ggZH','factor':0.0001*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_0J_PTH_GT10'] = {'mode':'ggZH','factor':0.0029*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_1J_PTH_0_60'] = {'mode':'ggZH','factor':0.0200*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_1J_PTH_60_120'] = {'mode':'ggZH','factor':0.0534*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_1J_PTH_120_200'] = {'mode':'ggZH','factor':0.0353*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_GE2J_MJJ_0_350_PTH_0_60'] = {'mode':'ggZH','factor':0.0574*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_GE2J_MJJ_0_350_PTH_60_120'] = {'mode':'ggZH','factor':0.1963*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_GE2J_MJJ_0_350_PTH_120_200'] = {'mode':'ggZH','factor':0.2954*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25'] = {'mode':'ggZH','factor':0.0114*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25'] = {'mode':'ggZH','factor':0.0806*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25'] = {'mode':'ggZH','factor':0.0036*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25'] = {'mode':'ggZH','factor':0.0285*BR_Z_qq}
# qqH STXS stage 1.2 bins: including (qq)VH hadronic processes
globalXSBRMap['STXS']['VBF_FWDH'] = {'mode':'qqH','factor':0.0669}
globalXSBRMap['STXS']['VBF_0J'] = {'mode':'qqH','factor':0.0695}
globalXSBRMap['STXS']['VBF_1J'] = {'mode':'qqH','factor':0.3283}
globalXSBRMap['STXS']['VBF_GE2J_MJJ_0_60'] = {'mode':'qqH','factor':0.0136}
globalXSBRMap['STXS']['VBF_GE2J_MJJ_60_120'] = {'mode':'qqH','factor':0.0240}
globalXSBRMap['STXS']['VBF_GE2J_MJJ_120_350'] = {'mode':'qqH','factor':0.1234}
globalXSBRMap['STXS']['VBF_GE2J_MJJ_GT350_PTH_GT200'] = {'mode':'qqH','factor':0.0398}
globalXSBRMap['STXS']['VBF_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25'] = {'mode':'qqH','factor':0.1026}
globalXSBRMap['STXS']['VBF_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25'] = {'mode':'qqH','factor':0.0385}
globalXSBRMap['STXS']['VBF_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25'] = {'mode':'qqH','factor':0.1509}
globalXSBRMap['STXS']['VBF_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25'] = {'mode':'qqH','factor':0.0425}
globalXSBRMap['STXS']['WH2HQQ_FWDH'] = {'mode':'WH','factor':0.1257*BR_W_qq}
globalXSBRMap['STXS']['WH2HQQ_0J'] = {'mode':'WH','factor':0.0570*BR_W_qq}
globalXSBRMap['STXS']['WH2HQQ_1J'] = {'mode':'WH','factor':0.3113*BR_W_qq}
globalXSBRMap['STXS']['WH2HQQ_GE2J_MJJ_0_60'] = {'mode':'WH','factor':0.0358*BR_W_qq}
globalXSBRMap['STXS']['WH2HQQ_GE2J_MJJ_60_120'] = {'mode':'WH','factor':0.2943*BR_W_qq}
globalXSBRMap['STXS']['WH2HQQ_GE2J_MJJ_120_350'] = {'mode':'WH','factor':0.1392*BR_W_qq}
globalXSBRMap['STXS']['WH2HQQ_GE2J_MJJ_GT350_PTH_GT200'] = {'mode':'WH','factor':0.0088*BR_W_qq}
globalXSBRMap['STXS']['WH2HQQ_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25'] = {'mode':'WH','factor':0.0044*BR_W_qq}
globalXSBRMap['STXS']['WH2HQQ_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25'] = {'mode':'WH','factor':0.0186*BR_W_qq}
globalXSBRMap['STXS']['WH2HQQ_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25'] = {'mode':'WH','factor':0.0009*BR_W_qq}
globalXSBRMap['STXS']['WH2HQQ_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25'] = {'mode':'WH','factor':0.0040*BR_W_qq}
globalXSBRMap['STXS']['ZH2HQQ_FWDH'] = {'mode':'qqZH','factor':0.1143*BR_Z_qq}
globalXSBRMap['STXS']['ZH2HQQ_0J'] = {'mode':'qqZH','factor':0.0433*BR_Z_qq}
globalXSBRMap['STXS']['ZH2HQQ_1J'] = {'mode':'qqZH','factor':0.2906*BR_Z_qq}
globalXSBRMap['STXS']['ZH2HQQ_GE2J_MJJ_0_60'] = {'mode':'qqZH','factor':0.0316*BR_Z_qq}
globalXSBRMap['STXS']['ZH2HQQ_GE2J_MJJ_60_120'] = {'mode':'qqZH','factor':0.3360*BR_Z_qq}
globalXSBRMap['STXS']['ZH2HQQ_GE2J_MJJ_120_350'] = {'mode':'qqZH','factor':0.1462*BR_Z_qq}
globalXSBRMap['STXS']['ZH2HQQ_GE2J_MJJ_GT350_PTH_GT200'] = {'mode':'qqZH','factor':0.0083*BR_Z_qq}
globalXSBRMap['STXS']['ZH2HQQ_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25'] = {'mode':'qqZH','factor':0.0041*BR_Z_qq}
globalXSBRMap['STXS']['ZH2HQQ_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25'] = {'mode':'qqZH','factor':0.0202*BR_Z_qq}
globalXSBRMap['STXS']['ZH2HQQ_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25'] = {'mode':'qqZH','factor':0.0009*BR_Z_qq}
globalXSBRMap['STXS']['ZH2HQQ_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25'] = {'mode':'qqZH','factor':0.0045*BR_Z_qq}
# WH lep STXS stage 1.2 bins
globalXSBRMap['STXS']['QQ2HLNU_FWDH'] = {'mode':'WH','factor':0.1213*BR_W_lnu}
globalXSBRMap['STXS']['QQ2HLNU_PTV_0_75'] = {'mode':'WH','factor':0.4655*BR_W_lnu}
globalXSBRMap['STXS']['QQ2HLNU_PTV_75_150'] = {'mode':'WH','factor':0.2930*BR_W_lnu}
globalXSBRMap['STXS']['QQ2HLNU_PTV_150_250_0J'] = {'mode':'WH','factor':0.0510*BR_W_lnu}
globalXSBRMap['STXS']['QQ2HLNU_PTV_150_250_GE1J'] = {'mode':'WH','factor':0.0397*BR_W_lnu}
globalXSBRMap['STXS']['QQ2HLNU_PTV_GT250'] = {'mode':'WH','factor':0.0295*BR_W_lnu}
# (qq)ZH lep STXS stage 1.2 bins
globalXSBRMap['STXS']['QQ2HLL_FWDH'] = {'mode':'qqZH','factor':0.1121*(BR_Z_ll+BR_Z_nunu)}
globalXSBRMap['STXS']['QQ2HLL_PTV_0_75'] = {'mode':'qqZH','factor':0.4565*(BR_Z_ll+BR_Z_nunu)}
globalXSBRMap['STXS']['QQ2HLL_PTV_75_150'] = {'mode':'qqZH','factor':0.3070*(BR_Z_ll+BR_Z_nunu)}
globalXSBRMap['STXS']['QQ2HLL_PTV_150_250_0J'] = {'mode':'qqZH','factor':0.0516*(BR_Z_ll+BR_Z_nunu)}
globalXSBRMap['STXS']['QQ2HLL_PTV_150_250_GE1J'] = {'mode':'qqZH','factor':0.0427*(BR_Z_ll+BR_Z_nunu)}
globalXSBRMap['STXS']['QQ2HLL_PTV_GT250'] = {'mode':'qqZH','factor':0.0301*(BR_Z_ll+BR_Z_nunu)}
# gg(ZH) lep STXS stage 1.2 bins: separate processes for ll and nunu decays
globalXSBRMap['STXS']['GG2HLL_FWDH'] = {'mode':'ggZH','factor':0.0270*BR_Z_ll}
globalXSBRMap['STXS']['GG2HLL_PTV_0_75'] = {'mode':'ggZH','factor':0.1605*BR_Z_ll}
globalXSBRMap['STXS']['GG2HLL_PTV_75_150'] = {'mode':'ggZH','factor':0.4325*BR_Z_ll}
globalXSBRMap['STXS']['GG2HLL_PTV_150_250_0J'] = {'mode':'ggZH','factor':0.0913*BR_Z_ll}
globalXSBRMap['STXS']['GG2HLL_PTV_150_250_GE1J'] = {'mode':'ggZH','factor':0.2044*BR_Z_ll}
globalXSBRMap['STXS']['GG2HLL_PTV_GT250'] = {'mode':'ggZH','factor':0.0844*BR_Z_ll}
globalXSBRMap['STXS']['GG2HNUNU_FWDH'] = {'mode':'ggZH','factor':0.0271*BR_Z_nunu}
globalXSBRMap['STXS']['GG2HNUNU_PTV_0_75'] = {'mode':'ggZH','factor':0.1591*BR_Z_nunu}
globalXSBRMap['STXS']['GG2HNUNU_PTV_75_150'] = {'mode':'ggZH','factor':0.4336*BR_Z_nunu}
globalXSBRMap['STXS']['GG2HNUNU_PTV_150_250_0J'] = {'mode':'ggZH','factor':0.0905*BR_Z_nunu}
globalXSBRMap['STXS']['GG2HNUNU_PTV_150_250_GE1J'] = {'mode':'ggZH','factor':0.2051*BR_Z_nunu}
globalXSBRMap['STXS']['GG2HNUNU_PTV_GT250'] = {'mode':'ggZH','factor':0.0845*BR_Z_nunu}
# ttH STXS stage 1.2 bins
globalXSBRMap['STXS']['TTH_FWDH'] = {'mode':'ttH','factor':0.0135}
globalXSBRMap['STXS']['TTH_PTH_0_60'] = {'mode':'ttH','factor':0.2250}
globalXSBRMap['STXS']['TTH_PTH_60_120'] = {'mode':'ttH','factor':0.3473}
globalXSBRMap['STXS']['TTH_PTH_120_200'] = {'mode':'ttH','factor':0.2569}
globalXSBRMap['STXS']['TTH_PTH_200_300'] = {'mode':'ttH','factor':0.1076}
globalXSBRMap['STXS']['TTH_PTH_GT300'] = {'mode':'ttH','factor':0.0533}
# bbH STXS stage 1.2 bins
globalXSBRMap['STXS']['BBH_FWDH'] = {'mode':'bbH','factor':0.0487}
globalXSBRMap['STXS']['BBH'] = {'mode':'bbH','factor':0.9513}
# tH STXS stage 1.2 bins: tHq + tHW
globalXSBRMap['STXS']['THQ_FWDH'] = {'mode':'tHq','factor':0.0279}
globalXSBRMap['STXS']['THQ'] = {'mode':'tHq','factor':0.9721}
globalXSBRMap['STXS']['THW_FWDH'] = {'mode':'tHW','factor':0.0106}
globalXSBRMap['STXS']['THW'] = {'mode':'tHW','factor':0.9894}
#
#
# Tprime things
globalXSBRMap['TprimeRun2'] = od()
globalXSBRMap['TprimeRun2']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeRun2']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeRun2']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeRun2']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeRun2']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeRun2']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeRun3'] = od()
globalXSBRMap['TprimeRun3']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeRun3']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeRun3']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeRun3']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeRun3']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeRun3']['VH'] = {'mode':'constant','factor': 2.401}

globalXSBRMap['TprimeRun2']['TprimeM700Decay5pctSch'] = {'mode':'constant','factor': 0.016287445901}
globalXSBRMap['TprimeRun2']['TprimeM700Decay5pctTch'] = {'mode':'constant','factor': 4.099393e-05}
globalXSBRMap['TprimeRun2']['TprimeM700Decay5pctInt'] = {'mode':'constant','factor': -0.00059971551312}

globalXSBRMap['TprimeRun2']['TprimeM700Decay10pctSch'] = {'mode':'constant','factor': 0.008132575321}
globalXSBRMap['TprimeRun2']['TprimeM700Decay10pctTch'] = {'mode':'constant','factor': 4.1000740000000005e-05}
globalXSBRMap['TprimeRun2']['TprimeM700Decay10pctInt'] = {'mode':'constant','factor': -0.002483079316254}

globalXSBRMap['TprimeRun2']['TprimeM700Decay20pctSch'] = {'mode':'constant','factor': 0.0040273118739999995}
globalXSBRMap['TprimeRun2']['TprimeM700Decay20pctTch'] = {'mode':'constant','factor': 4.0968960000000004e-05}
globalXSBRMap['TprimeRun2']['TprimeM700Decay20pctInt'] = {'mode':'constant','factor': -0.00137474799312}

globalXSBRMap['TprimeRun2']['TprimeM700Decay30pctSch'] = {'mode':'constant','factor': 0.0026683459560000004}
globalXSBRMap['TprimeRun2']['TprimeM700Decay30pctTch'] = {'mode':'constant','factor': 4.0889509999999996e-05}
globalXSBRMap['TprimeRun2']['TprimeM700Decay30pctInt'] = {'mode':'constant','factor': -0.00034924769015999996}

globalXSBRMap['TprimeRun2']['TprimeM800Decay5pctSch'] = {'mode':'constant','factor': 0.011618786613999997}
globalXSBRMap['TprimeRun2']['TprimeM800Decay5pctTch'] = {'mode':'constant','factor': 3.623374e-05}
globalXSBRMap['TprimeRun2']['TprimeM800Decay5pctInt'] = {'mode':'constant','factor': -0.00299101645665}

globalXSBRMap['TprimeRun2']['TprimeM800Decay10pctSch'] = {'mode':'constant','factor': 0.005818851489}
globalXSBRMap['TprimeRun2']['TprimeM800Decay10pctTch'] = {'mode':'constant','factor': 3.6254169999999994e-05}
globalXSBRMap['TprimeRun2']['TprimeM800Decay10pctInt'] = {'mode':'constant','factor': -0.002564109342944}

globalXSBRMap['TprimeRun2']['TprimeM800Decay20pctSch'] = {'mode':'constant','factor': 0.002930518471}
globalXSBRMap['TprimeRun2']['TprimeM800Decay20pctTch'] = {'mode':'constant','factor': 3.6133859999999994e-05}
globalXSBRMap['TprimeRun2']['TprimeM800Decay20pctInt'] = {'mode':'constant','factor': -0.0021570497258999997}

globalXSBRMap['TprimeRun2']['TprimeM800Decay30pctSch'] = {'mode':'constant','factor': 0.00198503101}
globalXSBRMap['TprimeRun2']['TprimeM800Decay30pctTch'] = {'mode':'constant','factor': 3.605895e-05}
globalXSBRMap['TprimeRun2']['TprimeM800Decay30pctInt'] = {'mode':'constant','factor': -0.00175400137864}

globalXSBRMap['TprimeRun2']['TprimeM900Decay5pctSch'] = {'mode':'constant','factor': 0.008390941954}
globalXSBRMap['TprimeRun2']['TprimeM900Decay5pctTch'] = {'mode':'constant','factor': 3.236793e-05}
globalXSBRMap['TprimeRun2']['TprimeM900Decay5pctInt'] = {'mode':'constant','factor': -0.002467308337802}

globalXSBRMap['TprimeRun2']['TprimeM900Decay10pctSch'] = {'mode':'constant','factor': 0.004224192605999999}
globalXSBRMap['TprimeRun2']['TprimeM900Decay10pctTch'] = {'mode':'constant','factor': 3.236112e-05}
globalXSBRMap['TprimeRun2']['TprimeM900Decay10pctInt'] = {'mode':'constant','factor': -0.0029145155339600002}

globalXSBRMap['TprimeRun2']['TprimeM900Decay20pctSch'] = {'mode':'constant','factor': 0.0022103945897}
globalXSBRMap['TprimeRun2']['TprimeM900Decay20pctTch'] = {'mode':'constant','factor': 3.229529e-05}
globalXSBRMap['TprimeRun2']['TprimeM900Decay20pctInt'] = {'mode':'constant','factor': -0.00247042872838}

globalXSBRMap['TprimeRun2']['TprimeM900Decay30pctSch'] = {'mode':'constant','factor': 0.0014951773361}
globalXSBRMap['TprimeRun2']['TprimeM900Decay30pctTch'] = {'mode':'constant','factor': 3.2034239999999995e-05}
globalXSBRMap['TprimeRun2']['TprimeM900Decay30pctInt'] = {'mode':'constant','factor': -0.0016255904137499999}

globalXSBRMap['TprimeRun2']['TprimeM1000Decay5pctSch'] = {'mode':'constant','factor': 0.006044841338999999}
globalXSBRMap['TprimeRun2']['TprimeM1000Decay5pctTch'] = {'mode':'constant','factor': 2.8840349999999996e-05}
globalXSBRMap['TprimeRun2']['TprimeM1000Decay5pctInt'] = {'mode':'constant','factor': -0.003113783624052}

globalXSBRMap['TprimeRun2']['TprimeM1000Decay10pctSch'] = {'mode':'constant','factor': 0.0031085273309999994}
globalXSBRMap['TprimeRun2']['TprimeM1000Decay10pctTch'] = {'mode':'constant','factor': 2.8840349999999996e-05}
globalXSBRMap['TprimeRun2']['TprimeM1000Decay10pctInt'] = {'mode':'constant','factor': -0.00286098380376}

globalXSBRMap['TprimeRun2']['TprimeM1000Decay20pctSch'] = {'mode':'constant','factor': 0.0016588383886999999}
globalXSBRMap['TprimeRun2']['TprimeM1000Decay20pctTch'] = {'mode':'constant','factor': 2.8708689999999994e-05}
globalXSBRMap['TprimeRun2']['TprimeM1000Decay20pctInt'] = {'mode':'constant','factor': -0.002155664220504}

globalXSBRMap['TprimeRun2']['TprimeM1000Decay30pctSch'] = {'mode':'constant','factor': 0.0011462280102}
globalXSBRMap['TprimeRun2']['TprimeM1000Decay30pctTch'] = {'mode':'constant','factor': 2.8561140000000003e-05}
globalXSBRMap['TprimeRun2']['TprimeM1000Decay30pctInt'] = {'mode':'constant','factor': -0.00255549126933}

globalXSBRMap['TprimeRun2']['TprimeM1100Decay5pctSch'] = {'mode':'constant','factor': 0.004453623776}
globalXSBRMap['TprimeRun2']['TprimeM1100Decay5pctTch'] = {'mode':'constant','factor': 2.590524e-05}
globalXSBRMap['TprimeRun2']['TprimeM1100Decay5pctInt'] = {'mode':'constant','factor': -0.0030555408139400003}

globalXSBRMap['TprimeRun2']['TprimeM1100Decay10pctSch'] = {'mode':'constant','factor': 0.002327320224}
globalXSBRMap['TprimeRun2']['TprimeM1100Decay10pctTch'] = {'mode':'constant','factor': 2.584168e-05}
globalXSBRMap['TprimeRun2']['TprimeM1100Decay10pctInt'] = {'mode':'constant','factor': -0.0026912315675439997}

globalXSBRMap['TprimeRun2']['TprimeM1100Decay20pctSch'] = {'mode':'constant','factor': 0.0012904188188}
globalXSBRMap['TprimeRun2']['TprimeM1100Decay20pctTch'] = {'mode':'constant','factor': 2.5748609999999997e-05}
globalXSBRMap['TprimeRun2']['TprimeM1100Decay20pctInt'] = {'mode':'constant','factor': -0.0023400270384119994}

globalXSBRMap['TprimeRun2']['TprimeM1100Decay30pctSch'] = {'mode':'constant','factor': 0.0008887572781}
globalXSBRMap['TprimeRun2']['TprimeM1100Decay30pctTch'] = {'mode':'constant','factor': 2.5555659999999997e-05}
globalXSBRMap['TprimeRun2']['TprimeM1100Decay30pctInt'] = {'mode':'constant','factor': -0.0018785313041}

globalXSBRMap['TprimeRun2']['TprimeM1200Decay5pctSch'] = {'mode':'constant','factor': 0.0033687274429999997}
globalXSBRMap['TprimeRun2']['TprimeM1200Decay5pctTch'] = {'mode':'constant','factor': 2.332198e-05}
globalXSBRMap['TprimeRun2']['TprimeM1200Decay5pctInt'] = {'mode':'constant','factor': -0.0025432642561920003}

globalXSBRMap['TprimeRun2']['TprimeM1200Decay10pctSch'] = {'mode':'constant','factor': 0.0018111459454999998}
globalXSBRMap['TprimeRun2']['TprimeM1200Decay10pctTch'] = {'mode':'constant','factor': 2.328339e-05}
globalXSBRMap['TprimeRun2']['TprimeM1200Decay10pctInt'] = {'mode':'constant','factor': -0.00288255866464}

globalXSBRMap['TprimeRun2']['TprimeM1200Decay20pctSch'] = {'mode':'constant','factor': 0.0010047424968}
globalXSBRMap['TprimeRun2']['TprimeM1200Decay20pctTch'] = {'mode':'constant','factor': 2.309725e-05}
globalXSBRMap['TprimeRun2']['TprimeM1200Decay20pctInt'] = {'mode':'constant','factor': -0.00241470931065}

globalXSBRMap['TprimeRun2']['TprimeM1200Decay30pctSch'] = {'mode':'constant','factor': 0.0007206837087}
globalXSBRMap['TprimeRun2']['TprimeM1200Decay30pctTch'] = {'mode':'constant','factor': 2.2940619999999997e-05}
globalXSBRMap['TprimeRun2']['TprimeM1200Decay30pctInt'] = {'mode':'constant','factor': -0.002187753631492}

globalXSBRMap['TprimeRun2']['TprimeM1400Decay5pctSch'] = {'mode':'constant','factor': 0.0020026402626}
globalXSBRMap['TprimeRun2']['TprimeM1400Decay5pctTch'] = {'mode':'constant','factor': 1.9018967999999998e-05}
globalXSBRMap['TprimeRun2']['TprimeM1400Decay5pctInt'] = {'mode':'constant','factor': -0.00200320183336}

globalXSBRMap['TprimeRun2']['TprimeM1400Decay10pctSch'] = {'mode':'constant','factor': 0.0010969913924}
globalXSBRMap['TprimeRun2']['TprimeM1400Decay10pctTch'] = {'mode':'constant','factor': 1.8985372e-05}
globalXSBRMap['TprimeRun2']['TprimeM1400Decay10pctInt'] = {'mode':'constant','factor': -0.002544650258718}

globalXSBRMap['TprimeRun2']['TprimeM1400Decay20pctSch'] = {'mode':'constant','factor': 0.0006316850671999999}
globalXSBRMap['TprimeRun2']['TprimeM1400Decay20pctTch'] = {'mode':'constant','factor': 1.8848491000000003e-05}
globalXSBRMap['TprimeRun2']['TprimeM1400Decay20pctInt'] = {'mode':'constant','factor': -0.002052587822608}

globalXSBRMap['TprimeRun2']['TprimeM1400Decay30pctSch'] = {'mode':'constant','factor': 0.00046587804739999997}
globalXSBRMap['TprimeRun2']['TprimeM1400Decay30pctTch'] = {'mode':'constant','factor': 1.8627393e-05}
globalXSBRMap['TprimeRun2']['TprimeM1400Decay30pctInt'] = {'mode':'constant','factor': -0.00217103107812}

globalXSBRMap['TprimeRun2']['TprimeM1600Decay5pctSch'] = {'mode':'constant','factor': 0.0011852388909}
globalXSBRMap['TprimeRun2']['TprimeM1600Decay5pctTch'] = {'mode':'constant','factor': 1.5801697e-05}
globalXSBRMap['TprimeRun2']['TprimeM1600Decay5pctInt'] = {'mode':'constant','factor': -0.00181578854496}

globalXSBRMap['TprimeRun2']['TprimeM1600Decay10pctSch'] = {'mode':'constant','factor': 0.0006886720325}
globalXSBRMap['TprimeRun2']['TprimeM1600Decay10pctTch'] = {'mode':'constant','factor': 1.5771506e-05}
globalXSBRMap['TprimeRun2']['TprimeM1600Decay10pctInt'] = {'mode':'constant','factor': -0.001565656592108}

globalXSBRMap['TprimeRun2']['TprimeM1600Decay20pctSch'] = {'mode':'constant','factor': 0.00042045083009999997}
globalXSBRMap['TprimeRun2']['TprimeM1600Decay20pctTch'] = {'mode':'constant','factor': 1.574018e-05}
globalXSBRMap['TprimeRun2']['TprimeM1600Decay20pctInt'] = {'mode':'constant','factor': -0.0017723452177679999}

globalXSBRMap['TprimeRun2']['TprimeM1600Decay30pctSch'] = {'mode':'constant','factor': 0.00032084976769999993}
globalXSBRMap['TprimeRun2']['TprimeM1600Decay30pctTch'] = {'mode':'constant','factor': 1.5532702e-05}
globalXSBRMap['TprimeRun2']['TprimeM1600Decay30pctInt'] = {'mode':'constant','factor': -0.001605222347976}

globalXSBRMap['TprimeRun2']['TprimeM1800Decay5pctSch'] = {'mode':'constant','factor': 0.0007589569074999999}
globalXSBRMap['TprimeRun2']['TprimeM1800Decay5pctTch'] = {'mode':'constant','factor': 1.3367348999999999e-05}
globalXSBRMap['TprimeRun2']['TprimeM1800Decay5pctInt'] = {'mode':'constant','factor': -0.0014151303097559998}

globalXSBRMap['TprimeRun2']['TprimeM1800Decay10pctSch'] = {'mode':'constant','factor': 0.0004457843705999999}
globalXSBRMap['TprimeRun2']['TprimeM1800Decay10pctTch'] = {'mode':'constant','factor': 1.3347373e-05}
globalXSBRMap['TprimeRun2']['TprimeM1800Decay10pctInt'] = {'mode':'constant','factor': -0.0013719694005279999}

globalXSBRMap['TprimeRun2']['TprimeM1800Decay20pctSch'] = {'mode':'constant','factor': 0.0002860098758}
globalXSBRMap['TprimeRun2']['TprimeM1800Decay20pctTch'] = {'mode':'constant','factor': 1.3117422e-05}
globalXSBRMap['TprimeRun2']['TprimeM1800Decay20pctInt'] = {'mode':'constant','factor': -0.001609397632524}

globalXSBRMap['TprimeRun2']['TprimeM1800Decay30pctSch'] = {'mode':'constant','factor': 0.00022272229396}
globalXSBRMap['TprimeRun2']['TprimeM1800Decay30pctTch'] = {'mode':'constant','factor': 1.2931509e-05}
globalXSBRMap['TprimeRun2']['TprimeM1800Decay30pctInt'] = {'mode':'constant','factor': -0.00157285060256}

globalXSBRMap['TprimeRun2']['TprimeM2000Decay5pctSch'] = {'mode':'constant','factor': 0.0004976131467999999}
globalXSBRMap['TprimeRun2']['TprimeM2000Decay5pctTch'] = {'mode':'constant','factor': 1.1313907e-05}
globalXSBRMap['TprimeRun2']['TprimeM2000Decay5pctInt'] = {'mode':'constant','factor': -0.001656930021492}

globalXSBRMap['TprimeRun2']['TprimeM2000Decay10pctSch'] = {'mode':'constant','factor': 0.0003037976412}
globalXSBRMap['TprimeRun2']['TprimeM2000Decay10pctTch'] = {'mode':'constant','factor': 1.1312318e-05}
globalXSBRMap['TprimeRun2']['TprimeM2000Decay10pctInt'] = {'mode':'constant','factor': -0.001401456040866}

globalXSBRMap['TprimeRun2']['TprimeM2000Decay20pctSch'] = {'mode':'constant','factor': 0.00020540695415}
globalXSBRMap['TprimeRun2']['TprimeM2000Decay20pctTch'] = {'mode':'constant','factor': 1.1281899999999998e-05}
globalXSBRMap['TprimeRun2']['TprimeM2000Decay20pctInt'] = {'mode':'constant','factor': -0.0015433448574479999}

globalXSBRMap['TprimeRun2']['TprimeM2000Decay30pctSch'] = {'mode':'constant','factor': 0.00016989604117}
globalXSBRMap['TprimeRun2']['TprimeM2000Decay30pctTch'] = {'mode':'constant','factor': 1.106852e-05}
globalXSBRMap['TprimeRun2']['TprimeM2000Decay30pctInt'] = {'mode':'constant','factor': -0.0012714907361520002}

globalXSBRMap['TprimeRun2']['TprimeM2200Decay5pctSch'] = {'mode':'constant','factor': 0.0003321969756}
globalXSBRMap['TprimeRun2']['TprimeM2200Decay5pctTch'] = {'mode':'constant','factor': 9.754189999999998e-06}
globalXSBRMap['TprimeRun2']['TprimeM2200Decay5pctInt'] = {'mode':'constant','factor': -0.0011702527327139998}

globalXSBRMap['TprimeRun2']['TprimeM2200Decay10pctSch'] = {'mode':'constant','factor': 0.00021219205224999997}
globalXSBRMap['TprimeRun2']['TprimeM2200Decay10pctTch'] = {'mode':'constant','factor': 9.729673999999998e-06}
globalXSBRMap['TprimeRun2']['TprimeM2200Decay10pctInt'] = {'mode':'constant','factor': -0.001326240657312}

globalXSBRMap['TprimeRun2']['TprimeM2200Decay20pctSch'] = {'mode':'constant','factor': 0.00015091165661999998}
globalXSBRMap['TprimeRun2']['TprimeM2200Decay20pctTch'] = {'mode':'constant','factor': 9.647046e-06}
globalXSBRMap['TprimeRun2']['TprimeM2200Decay20pctInt'] = {'mode':'constant','factor': -0.00098259463571}

globalXSBRMap['TprimeRun2']['TprimeM2200Decay30pctSch'] = {'mode':'constant','factor': 0.00012734228748}
globalXSBRMap['TprimeRun2']['TprimeM2200Decay30pctTch'] = {'mode':'constant','factor': 9.479746999999999e-06}
globalXSBRMap['TprimeRun2']['TprimeM2200Decay30pctInt'] = {'mode':'constant','factor': -0.001241483380514}

globalXSBRMap['TprimeRun2']['TprimeM2400Decay5pctSch'] = {'mode':'constant','factor': 0.00022881411589999997}
globalXSBRMap['TprimeRun2']['TprimeM2400Decay5pctTch'] = {'mode':'constant','factor': 8.483671e-06}
globalXSBRMap['TprimeRun2']['TprimeM2400Decay5pctInt'] = {'mode':'constant','factor': -0.00111506736608}

globalXSBRMap['TprimeRun2']['TprimeM2400Decay10pctSch'] = {'mode':'constant','factor': 0.00015471929105999996}
globalXSBRMap['TprimeRun2']['TprimeM2400Decay10pctTch'] = {'mode':'constant','factor': 8.463014e-06}
globalXSBRMap['TprimeRun2']['TprimeM2400Decay10pctInt'] = {'mode':'constant','factor': -0.0012310536425999999}

globalXSBRMap['TprimeRun2']['TprimeM2400Decay20pctSch'] = {'mode':'constant','factor': 0.00011464589826999999}
globalXSBRMap['TprimeRun2']['TprimeM2400Decay20pctTch'] = {'mode':'constant','factor': 8.381521e-06}
globalXSBRMap['TprimeRun2']['TprimeM2400Decay20pctInt'] = {'mode':'constant','factor': -0.000996968415996}

globalXSBRMap['TprimeRun2']['TprimeM2400Decay30pctSch'] = {'mode':'constant','factor': 9.793808083e-05}
globalXSBRMap['TprimeRun2']['TprimeM2400Decay30pctTch'] = {'mode':'constant','factor': 8.233063e-06}
globalXSBRMap['TprimeRun2']['TprimeM2400Decay30pctInt'] = {'mode':'constant','factor': -0.0010564176793519998}

globalXSBRMap['TprimeRun2']['TprimeM2600Decay5pctSch'] = {'mode':'constant','factor': 0.00016111840063}
globalXSBRMap['TprimeRun2']['TprimeM2600Decay5pctTch'] = {'mode':'constant','factor': 7.410188e-06}
globalXSBRMap['TprimeRun2']['TprimeM2600Decay5pctInt'] = {'mode':'constant','factor': -0.000932089202772}

globalXSBRMap['TprimeRun2']['TprimeM2600Decay10pctSch'] = {'mode':'constant','factor': 0.00011626905722999999}
globalXSBRMap['TprimeRun2']['TprimeM2600Decay10pctTch'] = {'mode':'constant','factor': 7.3902119999999995e-06}
globalXSBRMap['TprimeRun2']['TprimeM2600Decay10pctInt'] = {'mode':'constant','factor': -0.000925377295374}

globalXSBRMap['TprimeRun2']['TprimeM2600Decay20pctSch'] = {'mode':'constant','factor': 8.954800192999999e-05}
globalXSBRMap['TprimeRun2']['TprimeM2600Decay20pctTch'] = {'mode':'constant','factor': 7.321885e-06}
globalXSBRMap['TprimeRun2']['TprimeM2600Decay20pctInt'] = {'mode':'constant','factor': -0.0011158807161599999}

globalXSBRMap['TprimeRun2']['TprimeM2600Decay30pctSch'] = {'mode':'constant','factor': 7.829477883999999e-05}
globalXSBRMap['TprimeRun2']['TprimeM2600Decay30pctTch'] = {'mode':'constant','factor': 7.192948999999999e-06}
globalXSBRMap['TprimeRun2']['TprimeM2600Decay30pctInt'] = {'mode':'constant','factor': -0.000996044595912}

globalXSBRMap['TprimeRun3']['TprimeM700Decay5pctSch'] = {'mode':'constant','factor': 0.0185406122619999}
globalXSBRMap['TprimeRun3']['TprimeM700Decay5pctTch'] = {'mode':'constant','factor': 4.6364750000000004e-05}
globalXSBRMap['TprimeRun3']['TprimeM700Decay5pctInt'] = {'mode':'constant','factor': -0.0027101894562000036}

globalXSBRMap['TprimeRun3']['TprimeM700Decay10pctSch'] = {'mode':'constant','factor': 0.009213883918999926}
globalXSBRMap['TprimeRun3']['TprimeM700Decay10pctTch'] = {'mode':'constant','factor': 4.6103700000000316e-05}
globalXSBRMap['TprimeRun3']['TprimeM700Decay10pctInt'] = {'mode':'constant','factor': -0.0013106786232799992}

globalXSBRMap['TprimeRun3']['TprimeM700Decay20pctSch'] = {'mode':'constant','factor': 0.004559243243999936}
globalXSBRMap['TprimeRun3']['TprimeM700Decay20pctTch'] = {'mode':'constant','factor': 4.582449000000037e-05}
globalXSBRMap['TprimeRun3']['TprimeM700Decay20pctInt'] = {'mode':'constant','factor': -0.0013128953277660004}

globalXSBRMap['TprimeRun3']['TprimeM700Decay30pctSch'] = {'mode':'constant','factor': 0.0029635008899999682}
globalXSBRMap['TprimeRun3']['TprimeM700Decay30pctTch'] = {'mode':'constant','factor': 4.6364750000000004e-05}
globalXSBRMap['TprimeRun3']['TprimeM700Decay30pctInt'] = {'mode':'constant','factor': -0.0011599403810399987}

globalXSBRMap['TprimeRun3']['TprimeM800Decay5pctSch'] = {'mode':'constant','factor': 0.01329801366599988}
globalXSBRMap['TprimeRun3']['TprimeM800Decay5pctTch'] = {'mode':'constant','factor': 4.143204000000031e-05}
globalXSBRMap['TprimeRun3']['TprimeM800Decay5pctInt'] = {'mode':'constant','factor': -0.004347794105999978}

globalXSBRMap['TprimeRun3']['TprimeM800Decay10pctSch'] = {'mode':'constant','factor': 0.006641913536999927}
globalXSBRMap['TprimeRun3']['TprimeM800Decay10pctTch'] = {'mode':'constant','factor': 4.1411610000000355e-05}
globalXSBRMap['TprimeRun3']['TprimeM800Decay10pctInt'] = {'mode':'constant','factor': -0.0035803187633580047}

globalXSBRMap['TprimeRun3']['TprimeM800Decay20pctSch'] = {'mode':'constant','factor': 0.0033483791630000443}
globalXSBRMap['TprimeRun3']['TprimeM800Decay20pctTch'] = {'mode':'constant','factor': 4.180886000000007e-05}
globalXSBRMap['TprimeRun3']['TprimeM800Decay20pctInt'] = {'mode':'constant','factor': -0.002130610504719995}

globalXSBRMap['TprimeRun3']['TprimeM800Decay30pctSch'] = {'mode':'constant','factor': 0.002212808416899984}
globalXSBRMap['TprimeRun3']['TprimeM800Decay30pctTch'] = {'mode':'constant','factor': 4.1767999999999455e-05}
globalXSBRMap['TprimeRun3']['TprimeM800Decay30pctInt'] = {'mode':'constant','factor': -0.0016753551765600002}

globalXSBRMap['TprimeRun3']['TprimeM900Decay5pctSch'] = {'mode':'constant','factor': 0.009650586972999793}
globalXSBRMap['TprimeRun3']['TprimeM900Decay5pctTch'] = {'mode':'constant','factor': 3.6976029999999914e-05}
globalXSBRMap['TprimeRun3']['TprimeM900Decay5pctInt'] = {'mode':'constant','factor': -0.0028125516503520035}

globalXSBRMap['TprimeRun3']['TprimeM900Decay10pctSch'] = {'mode':'constant','factor': 0.004914987656000083}
globalXSBRMap['TprimeRun3']['TprimeM900Decay10pctTch'] = {'mode':'constant','factor': 3.662417999999957e-05}
globalXSBRMap['TprimeRun3']['TprimeM900Decay10pctInt'] = {'mode':'constant','factor': -0.0034876375267359956}

globalXSBRMap['TprimeRun3']['TprimeM900Decay20pctSch'] = {'mode':'constant','factor': 0.0024897044470000252}
globalXSBRMap['TprimeRun3']['TprimeM900Decay20pctTch'] = {'mode':'constant','factor': 3.6319999999999754e-05}
globalXSBRMap['TprimeRun3']['TprimeM900Decay20pctInt'] = {'mode':'constant','factor': -0.0026105122216800074}

globalXSBRMap['TprimeRun3']['TprimeM900Decay30pctSch'] = {'mode':'constant','factor': 0.0016999862246999723}
globalXSBRMap['TprimeRun3']['TprimeM900Decay30pctTch'] = {'mode':'constant','factor': 3.6546999999999764e-05}
globalXSBRMap['TprimeRun3']['TprimeM900Decay30pctInt'] = {'mode':'constant','factor': -0.002421710134567995}

globalXSBRMap['TprimeRun3']['TprimeM1000Decay5pctSch'] = {'mode':'constant','factor': 0.007061841290999886}
globalXSBRMap['TprimeRun3']['TprimeM1000Decay5pctTch'] = {'mode':'constant','factor': 3.292408000000047e-05}
globalXSBRMap['TprimeRun3']['TprimeM1000Decay5pctInt'] = {'mode':'constant','factor': -0.0037256739448500074}

globalXSBRMap['TprimeRun3']['TprimeM1000Decay10pctSch'] = {'mode':'constant','factor': 0.0036081164220000774}
globalXSBRMap['TprimeRun3']['TprimeM1000Decay10pctTch'] = {'mode':'constant','factor': 3.282874000000058e-05}
globalXSBRMap['TprimeRun3']['TprimeM1000Decay10pctInt'] = {'mode':'constant','factor': -0.0033665693204040187}

globalXSBRMap['TprimeRun3']['TprimeM1000Decay20pctSch'] = {'mode':'constant','factor': 0.0018934104731000356}
globalXSBRMap['TprimeRun3']['TprimeM1000Decay20pctTch'] = {'mode':'constant','factor': 3.3464339999999865e-05}
globalXSBRMap['TprimeRun3']['TprimeM1000Decay20pctInt'] = {'mode':'constant','factor': -0.0026760821091899954}

globalXSBRMap['TprimeRun3']['TprimeM1000Decay30pctSch'] = {'mode':'constant','factor': 0.0012897373420999757}
globalXSBRMap['TprimeRun3']['TprimeM1000Decay30pctTch'] = {'mode':'constant','factor': 3.3166969999999825e-05}
globalXSBRMap['TprimeRun3']['TprimeM1000Decay30pctInt'] = {'mode':'constant','factor': -0.002052124178286005}

globalXSBRMap['TprimeRun3']['TprimeM1100Decay5pctSch'] = {'mode':'constant','factor': 0.005253661668000051}
globalXSBRMap['TprimeRun3']['TprimeM1100Decay5pctTch'] = {'mode':'constant','factor': 3.000032000000043e-05}
globalXSBRMap['TprimeRun3']['TprimeM1100Decay5pctInt'] = {'mode':'constant','factor': -0.003591429384140016}

globalXSBRMap['TprimeRun3']['TprimeM1100Decay10pctSch'] = {'mode':'constant','factor': 0.002734780684000017}
globalXSBRMap['TprimeRun3']['TprimeM1100Decay10pctTch'] = {'mode':'constant','factor': 2.9936760000000456e-05}
globalXSBRMap['TprimeRun3']['TprimeM1100Decay10pctInt'] = {'mode':'constant','factor': -0.003535108809119989}

globalXSBRMap['TprimeRun3']['TprimeM1100Decay20pctSch'] = {'mode':'constant','factor': 0.0014640793349000245}
globalXSBRMap['TprimeRun3']['TprimeM1100Decay20pctTch'] = {'mode':'constant','factor': 2.9857309999999804e-05}
globalXSBRMap['TprimeRun3']['TprimeM1100Decay20pctInt'] = {'mode':'constant','factor': -0.003213601878689979}

globalXSBRMap['TprimeRun3']['TprimeM1100Decay30pctSch'] = {'mode':'constant','factor': 0.0010199659339999903}
globalXSBRMap['TprimeRun3']['TprimeM1100Decay30pctTch'] = {'mode':'constant','factor': 2.9657549999999236e-05}
globalXSBRMap['TprimeRun3']['TprimeM1100Decay30pctInt'] = {'mode':'constant','factor': -0.0023284918617999992}

globalXSBRMap['TprimeRun3']['TprimeM1200Decay5pctSch'] = {'mode':'constant','factor': 0.003946195920999935}
globalXSBRMap['TprimeRun3']['TprimeM1200Decay5pctTch'] = {'mode':'constant','factor': 2.698803000000034e-05}
globalXSBRMap['TprimeRun3']['TprimeM1200Decay5pctInt'] = {'mode':'constant','factor': -0.0032699755512799774}

globalXSBRMap['TprimeRun3']['TprimeM1200Decay10pctSch'] = {'mode':'constant','factor': 0.0020989281010999794}
globalXSBRMap['TprimeRun3']['TprimeM1200Decay10pctTch'] = {'mode':'constant','factor': 2.6994840000000116e-05}
globalXSBRMap['TprimeRun3']['TprimeM1200Decay10pctInt'] = {'mode':'constant','factor': -0.002843389644390004}

globalXSBRMap['TprimeRun3']['TprimeM1200Decay20pctSch'] = {'mode':'constant','factor': 0.001138030654299988}
globalXSBRMap['TprimeRun3']['TprimeM1200Decay20pctTch'] = {'mode':'constant','factor': 2.6919930000000344e-05}
globalXSBRMap['TprimeRun3']['TprimeM1200Decay20pctInt'] = {'mode':'constant','factor': -0.0029317010919680084}

globalXSBRMap['TprimeRun3']['TprimeM1200Decay30pctSch'] = {'mode':'constant','factor': 0.0008068840757999824}
globalXSBRMap['TprimeRun3']['TprimeM1200Decay30pctTch'] = {'mode':'constant','factor': 2.6742870000000273e-05}
globalXSBRMap['TprimeRun3']['TprimeM1200Decay30pctInt'] = {'mode':'constant','factor': -0.002711435694372007}

globalXSBRMap['TprimeRun3']['TprimeM1400Decay5pctSch'] = {'mode':'constant','factor': 0.0023642860390000074}
globalXSBRMap['TprimeRun3']['TprimeM1400Decay5pctTch'] = {'mode':'constant','factor': 2.2301160999999894e-05}
globalXSBRMap['TprimeRun3']['TprimeM1400Decay5pctInt'] = {'mode':'constant','factor': -0.002915792837081993}

globalXSBRMap['TprimeRun3']['TprimeM1400Decay10pctSch'] = {'mode':'constant','factor': 0.001270854074700005}
globalXSBRMap['TprimeRun3']['TprimeM1400Decay10pctTch'] = {'mode':'constant','factor': 2.223896299999957e-05}
globalXSBRMap['TprimeRun3']['TprimeM1400Decay10pctInt'] = {'mode':'constant','factor': -0.0024770904819440024}

globalXSBRMap['TprimeRun3']['TprimeM1400Decay20pctSch'] = {'mode':'constant','factor': 0.0007259916951000125}
globalXSBRMap['TprimeRun3']['TprimeM1400Decay20pctTch'] = {'mode':'constant','factor': 2.2049190999999533e-05}
globalXSBRMap['TprimeRun3']['TprimeM1400Decay20pctInt'] = {'mode':'constant','factor': -0.0025990236018599996}

globalXSBRMap['TprimeRun3']['TprimeM1400Decay30pctSch'] = {'mode':'constant','factor': 0.0005361656236999951}
globalXSBRMap['TprimeRun3']['TprimeM1400Decay30pctTch'] = {'mode':'constant','factor': 2.1856922000000333e-05}
globalXSBRMap['TprimeRun3']['TprimeM1400Decay30pctInt'] = {'mode':'constant','factor': -0.00215595422662399}

globalXSBRMap['TprimeRun3']['TprimeM1600Decay5pctSch'] = {'mode':'constant','factor': 0.0014325738913999978}
globalXSBRMap['TprimeRun3']['TprimeM1600Decay5pctTch'] = {'mode':'constant','factor': 1.8482793999999874e-05}
globalXSBRMap['TprimeRun3']['TprimeM1600Decay5pctInt'] = {'mode':'constant','factor': -0.0022839159916559887}

globalXSBRMap['TprimeRun3']['TprimeM1600Decay10pctSch'] = {'mode':'constant','factor': 0.0008062823669000083}
globalXSBRMap['TprimeRun3']['TprimeM1600Decay10pctTch'] = {'mode':'constant','factor': 1.844647400000024e-05}
globalXSBRMap['TprimeRun3']['TprimeM1600Decay10pctInt'] = {'mode':'constant','factor': -0.0023101128195119917}

globalXSBRMap['TprimeRun3']['TprimeM1600Decay20pctSch'] = {'mode':'constant','factor': 0.00047933201959999243}
globalXSBRMap['TprimeRun3']['TprimeM1600Decay20pctTch'] = {'mode':'constant','factor': 1.8106200999999796e-05}
globalXSBRMap['TprimeRun3']['TprimeM1600Decay20pctInt'] = {'mode':'constant','factor': -0.0019785810742220136}

globalXSBRMap['TprimeRun3']['TprimeM1600Decay30pctSch'] = {'mode':'constant','factor': 0.00036510900189999786}
globalXSBRMap['TprimeRun3']['TprimeM1600Decay30pctTch'] = {'mode':'constant','factor': 1.7840610999999702e-05}
globalXSBRMap['TprimeRun3']['TprimeM1600Decay30pctInt'] = {'mode':'constant','factor': -0.0016693274294560024}

globalXSBRMap['TprimeRun3']['TprimeM1800Decay5pctSch'] = {'mode':'constant','factor': 0.0009125979758000121}
globalXSBRMap['TprimeRun3']['TprimeM1800Decay5pctTch'] = {'mode':'constant','factor': 1.5663226999999722e-05}
globalXSBRMap['TprimeRun3']['TprimeM1800Decay5pctInt'] = {'mode':'constant','factor': -0.001989516141376005}

globalXSBRMap['TprimeRun3']['TprimeM1800Decay10pctSch'] = {'mode':'constant','factor': 0.0005314127658000058}
globalXSBRMap['TprimeRun3']['TprimeM1800Decay10pctTch'] = {'mode':'constant','factor': 1.5544960000000215e-05}
globalXSBRMap['TprimeRun3']['TprimeM1800Decay10pctInt'] = {'mode':'constant','factor': -0.001797865838048002}

globalXSBRMap['TprimeRun3']['TprimeM1800Decay20pctSch'] = {'mode':'constant','factor': 0.00033568208389999623}
globalXSBRMap['TprimeRun3']['TprimeM1800Decay20pctTch'] = {'mode':'constant','factor': 1.543690800000018e-05}
globalXSBRMap['TprimeRun3']['TprimeM1800Decay20pctInt'] = {'mode':'constant','factor': -0.0020112682084439852}

globalXSBRMap['TprimeRun3']['TprimeM1800Decay30pctSch'] = {'mode':'constant','factor': 0.0002600146076000044}
globalXSBRMap['TprimeRun3']['TprimeM1800Decay30pctTch'] = {'mode':'constant','factor': 1.5250541000000282e-05}
globalXSBRMap['TprimeRun3']['TprimeM1800Decay30pctInt'] = {'mode':'constant','factor': -0.0018433076913999926}

globalXSBRMap['TprimeRun3']['TprimeM2000Decay5pctSch'] = {'mode':'constant','factor': 0.0005970984618999911}
globalXSBRMap['TprimeRun3']['TprimeM2000Decay5pctTch'] = {'mode':'constant','factor': 1.3172356000000008e-05}
globalXSBRMap['TprimeRun3']['TprimeM2000Decay5pctInt'] = {'mode':'constant','factor': -0.0018835370427239858}

globalXSBRMap['TprimeRun3']['TprimeM2000Decay10pctSch'] = {'mode':'constant','factor': 0.00036365663320000725}
globalXSBRMap['TprimeRun3']['TprimeM2000Decay10pctTch'] = {'mode':'constant','factor': 1.3132630999999776e-05}
globalXSBRMap['TprimeRun3']['TprimeM2000Decay10pctInt'] = {'mode':'constant','factor': -0.0017236555782600077}

globalXSBRMap['TprimeRun3']['TprimeM2000Decay20pctSch'] = {'mode':'constant','factor': 0.00023878509089999514}
globalXSBRMap['TprimeRun3']['TprimeM2000Decay20pctTch'] = {'mode':'constant','factor': 1.2989847999999907e-05}
globalXSBRMap['TprimeRun3']['TprimeM2000Decay20pctInt'] = {'mode':'constant','factor': -0.0018616353463360154}

globalXSBRMap['TprimeRun3']['TprimeM2000Decay30pctSch'] = {'mode':'constant','factor': 0.0001918348942799982}
globalXSBRMap['TprimeRun3']['TprimeM2000Decay30pctTch'] = {'mode':'constant','factor': 1.286182000000016e-05}
globalXSBRMap['TprimeRun3']['TprimeM2000Decay30pctInt'] = {'mode':'constant','factor': -0.001760588049230005}

globalXSBRMap['TprimeRun3']['TprimeM2200Decay5pctSch'] = {'mode':'constant','factor': 0.0004031378805999952}
globalXSBRMap['TprimeRun3']['TprimeM2200Decay5pctTch'] = {'mode':'constant','factor': 1.1362258000000098e-05}
globalXSBRMap['TprimeRun3']['TprimeM2200Decay5pctInt'] = {'mode':'constant','factor': -0.0015883832196620042}

globalXSBRMap['TprimeRun3']['TprimeM2200Decay10pctSch'] = {'mode':'constant','factor': 0.00025310027840000506}
globalXSBRMap['TprimeRun3']['TprimeM2200Decay10pctTch'] = {'mode':'constant','factor': 1.1362711999999893e-05}
globalXSBRMap['TprimeRun3']['TprimeM2200Decay10pctInt'] = {'mode':'constant','factor': -0.001780820409864001}

globalXSBRMap['TprimeRun3']['TprimeM2200Decay20pctSch'] = {'mode':'constant','factor': 0.000177400974430001}
globalXSBRMap['TprimeRun3']['TprimeM2200Decay20pctTch'] = {'mode':'constant','factor': 1.1220836999999731e-05}
globalXSBRMap['TprimeRun3']['TprimeM2200Decay20pctInt'] = {'mode':'constant','factor': -0.001634631696176008}

globalXSBRMap['TprimeRun3']['TprimeM2200Decay30pctSch'] = {'mode':'constant','factor': 0.00014588899787}
globalXSBRMap['TprimeRun3']['TprimeM2200Decay30pctTch'] = {'mode':'constant','factor': 1.1080551000000149e-05}
globalXSBRMap['TprimeRun3']['TprimeM2200Decay30pctInt'] = {'mode':'constant','factor': -0.0015131659311239949}

globalXSBRMap['TprimeRun3']['TprimeM2400Decay5pctSch'] = {'mode':'constant','factor': 0.00027898415770000694}
globalXSBRMap['TprimeRun3']['TprimeM2400Decay5pctTch'] = {'mode':'constant','factor': 9.843401000000126e-06}
globalXSBRMap['TprimeRun3']['TprimeM2400Decay5pctInt'] = {'mode':'constant','factor': -0.0012942635559360014}

globalXSBRMap['TprimeRun3']['TprimeM2400Decay10pctSch'] = {'mode':'constant','factor': 0.00018312564202999817}
globalXSBRMap['TprimeRun3']['TprimeM2400Decay10pctTch'] = {'mode':'constant','factor': 9.756687000000099e-06}
globalXSBRMap['TprimeRun3']['TprimeM2400Decay10pctInt'] = {'mode':'constant','factor': -0.001486791931583996}

globalXSBRMap['TprimeRun3']['TprimeM2400Decay20pctSch'] = {'mode':'constant','factor': 0.00013330399982999842}
globalXSBRMap['TprimeRun3']['TprimeM2400Decay20pctTch'] = {'mode':'constant','factor': 9.738527000000238e-06}
globalXSBRMap['TprimeRun3']['TprimeM2400Decay20pctInt'] = {'mode':'constant','factor': -0.0015274351992479993}

globalXSBRMap['TprimeRun3']['TprimeM2400Decay30pctSch'] = {'mode':'constant','factor': 0.00011359386903999883}
globalXSBRMap['TprimeRun3']['TprimeM2400Decay30pctTch'] = {'mode':'constant','factor': 9.594836000000019e-06}
globalXSBRMap['TprimeRun3']['TprimeM2400Decay30pctInt'] = {'mode':'constant','factor': -0.001408139022108011}

globalXSBRMap['TprimeRun3']['TprimeM2600Decay5pctSch'] = {'mode':'constant','factor': 0.00020143929605999621}
globalXSBRMap['TprimeRun3']['TprimeM2600Decay5pctTch'] = {'mode':'constant','factor': 8.584685999999854e-06}
globalXSBRMap['TprimeRun3']['TprimeM2600Decay5pctInt'] = {'mode':'constant','factor': -0.0011801875379880017}

globalXSBRMap['TprimeRun3']['TprimeM2600Decay10pctSch'] = {'mode':'constant','factor': 0.00013847897785000283}
globalXSBRMap['TprimeRun3']['TprimeM2600Decay10pctTch'] = {'mode':'constant','factor': 8.596490000000121e-06}
globalXSBRMap['TprimeRun3']['TprimeM2600Decay10pctInt'] = {'mode':'constant','factor': -0.001399951232441993}

globalXSBRMap['TprimeRun3']['TprimeM2600Decay20pctSch'] = {'mode':'constant','factor': 0.00010481250796999875}
globalXSBRMap['TprimeRun3']['TprimeM2600Decay20pctTch'] = {'mode':'constant','factor': 8.53202200000006e-06}
globalXSBRMap['TprimeRun3']['TprimeM2600Decay20pctInt'] = {'mode':'constant','factor': -0.0012555624158279968}

globalXSBRMap['TprimeRun3']['TprimeM2600Decay30pctSch'] = {'mode':'constant','factor': 9.180542612999847e-05}
globalXSBRMap['TprimeRun3']['TprimeM2600Decay30pctTch'] = {'mode':'constant','factor': 8.376754000000149e-06}
globalXSBRMap['TprimeRun3']['TprimeM2600Decay30pctInt'] = {'mode':'constant','factor': -0.00118278507765}

