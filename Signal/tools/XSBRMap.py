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
globalXSBRMap['TprimeM700Decay5pct'] = od()
globalXSBRMap['TprimeM700Decay5pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM700Decay5pct']['TprimeM700Decay5pctSch'] = {'mode':'constant','factor': 0.0886}
globalXSBRMap['TprimeM700Decay5pct']['TprimeM700Decay5pctTch'] = {'mode':'constant','factor': 1.8059e-05}
globalXSBRMap['TprimeM700Decay5pct']['TprimeM700Decay5pctInt'] = {'mode':'constant','factor': -0.000264191856}
globalXSBRMap['TprimeM700Decay5pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM700Decay5pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM700Decay5pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM700Decay5pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM700Decay5pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM700Decay10pct'] = od()
globalXSBRMap['TprimeM700Decay10pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM700Decay10pct']['TprimeM700Decay10pctSch'] = {'mode':'constant','factor': 0.0035826323}
globalXSBRMap['TprimeM700Decay10pct']['TprimeM700Decay10pctTch'] = {'mode':'constant','factor': 1.8062e-05}
globalXSBRMap['TprimeM700Decay10pct']['TprimeM700Decay10pctInt'] = {'mode':'constant','factor': -0.0010938675402}
globalXSBRMap['TprimeM700Decay10pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM700Decay10pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM700Decay10pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM700Decay10pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM700Decay10pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM700Decay20pct'] = od()
globalXSBRMap['TprimeM700Decay20pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM700Decay20pct']['TprimeM700Decay20pctSch'] = {'mode':'constant','factor': 0.0017741462}
globalXSBRMap['TprimeM700Decay20pct']['TprimeM700Decay20pctTch'] = {'mode':'constant','factor': 1.8048e-05}
globalXSBRMap['TprimeM700Decay20pct']['TprimeM700Decay20pctInt'] = {'mode':'constant','factor': -0.000605615856}
globalXSBRMap['TprimeM700Decay20pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM700Decay20pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM700Decay20pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM700Decay20pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM700Decay20pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM700Decay30pct'] = od()
globalXSBRMap['TprimeM700Decay30pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM700Decay30pct']['TprimeM700Decay30pctSch'] = {'mode':'constant','factor': 0.0011754828}
globalXSBRMap['TprimeM700Decay30pct']['TprimeM700Decay30pctTch'] = {'mode':'constant','factor': 1.8013e-05}
globalXSBRMap['TprimeM700Decay30pct']['TprimeM700Decay30pctInt'] = {'mode':'constant','factor': -0.000153853608}
globalXSBRMap['TprimeM700Decay30pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM700Decay30pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM700Decay30pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM700Decay30pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM700Decay30pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM800Decay5pct'] = od()
globalXSBRMap['TprimeM800Decay5pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM800Decay5pct']['TprimeM800Decay5pctSch'] = {'mode':'constant','factor': 0.0459}
globalXSBRMap['TprimeM800Decay5pct']['TprimeM800Decay5pctTch'] = {'mode':'constant','factor': 1.5962e-05}
globalXSBRMap['TprimeM800Decay5pct']['TprimeM800Decay5pctInt'] = {'mode':'constant','factor': -0.001317628395}
globalXSBRMap['TprimeM800Decay5pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM800Decay5pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM800Decay5pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM800Decay5pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM800Decay5pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM800Decay10pct'] = od()
globalXSBRMap['TprimeM800Decay10pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM800Decay10pct']['TprimeM800Decay10pctSch'] = {'mode':'constant','factor': 0.0025633707}
globalXSBRMap['TprimeM800Decay10pct']['TprimeM800Decay10pctTch'] = {'mode':'constant','factor': 1.5971e-05}
globalXSBRMap['TprimeM800Decay10pct']['TprimeM800Decay10pctInt'] = {'mode':'constant','factor': -0.0011295635872}
globalXSBRMap['TprimeM800Decay10pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM800Decay10pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM800Decay10pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM800Decay10pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM800Decay10pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM800Decay20pct'] = od()
globalXSBRMap['TprimeM800Decay20pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM800Decay20pct']['TprimeM800Decay20pctSch'] = {'mode':'constant','factor': 0.0012909773}
globalXSBRMap['TprimeM800Decay20pct']['TprimeM800Decay20pctTch'] = {'mode':'constant','factor': 1.5918e-05}
globalXSBRMap['TprimeM800Decay20pct']['TprimeM800Decay20pctInt'] = {'mode':'constant','factor': -0.00095024217}
globalXSBRMap['TprimeM800Decay20pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM800Decay20pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM800Decay20pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM800Decay20pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM800Decay20pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM800Decay30pct'] = od()
globalXSBRMap['TprimeM800Decay30pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM800Decay30pct']['TprimeM800Decay30pctSch'] = {'mode':'constant','factor': 0.000874463}
globalXSBRMap['TprimeM800Decay30pct']['TprimeM800Decay30pctTch'] = {'mode':'constant','factor': 1.5885e-05}
globalXSBRMap['TprimeM800Decay30pct']['TprimeM800Decay30pctInt'] = {'mode':'constant','factor': -0.000772687832}
globalXSBRMap['TprimeM800Decay30pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM800Decay30pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM800Decay30pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM800Decay30pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM800Decay30pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM900Decay5pct'] = od()
globalXSBRMap['TprimeM900Decay5pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM900Decay5pct']['TprimeM900Decay5pctSch'] = {'mode':'constant','factor': 0.0251}
globalXSBRMap['TprimeM900Decay5pct']['TprimeM900Decay5pctTch'] = {'mode':'constant','factor': 1.4259e-05}
globalXSBRMap['TprimeM900Decay5pct']['TprimeM900Decay5pctInt'] = {'mode':'constant','factor': -0.0010869199726}
globalXSBRMap['TprimeM900Decay5pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM900Decay5pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM900Decay5pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM900Decay5pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM900Decay5pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM900Decay10pct'] = od()
globalXSBRMap['TprimeM900Decay10pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM900Decay10pct']['TprimeM900Decay10pctSch'] = {'mode':'constant','factor': 0.0018608778}
globalXSBRMap['TprimeM900Decay10pct']['TprimeM900Decay10pctTch'] = {'mode':'constant','factor': 1.4256e-05}
globalXSBRMap['TprimeM900Decay10pct']['TprimeM900Decay10pctInt'] = {'mode':'constant','factor': -0.001283927548}
globalXSBRMap['TprimeM900Decay10pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM900Decay10pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM900Decay10pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM900Decay10pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM900Decay10pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM900Decay20pct'] = od()
globalXSBRMap['TprimeM900Decay20pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM900Decay20pct']['TprimeM900Decay20pctSch'] = {'mode':'constant','factor': 0.00097374211}
globalXSBRMap['TprimeM900Decay20pct']['TprimeM900Decay20pctTch'] = {'mode':'constant','factor': 1.4227e-05}
globalXSBRMap['TprimeM900Decay20pct']['TprimeM900Decay20pctInt'] = {'mode':'constant','factor': -0.001088294594}
globalXSBRMap['TprimeM900Decay20pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM900Decay20pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM900Decay20pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM900Decay20pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM900Decay20pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM900Decay30pct'] = od()
globalXSBRMap['TprimeM900Decay30pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM900Decay30pct']['TprimeM900Decay30pctSch'] = {'mode':'constant','factor': 0.00065866843}
globalXSBRMap['TprimeM900Decay30pct']['TprimeM900Decay30pctTch'] = {'mode':'constant','factor': 1.4112e-05}
globalXSBRMap['TprimeM900Decay30pct']['TprimeM900Decay30pctInt'] = {'mode':'constant','factor': -0.000716119125}
globalXSBRMap['TprimeM900Decay30pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM900Decay30pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM900Decay30pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM900Decay30pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM900Decay30pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM1000Decay5pct'] = od()
globalXSBRMap['TprimeM1000Decay5pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1000Decay5pct']['TprimeM1000Decay5pctSch'] = {'mode':'constant','factor': 0.0145}
globalXSBRMap['TprimeM1000Decay5pct']['TprimeM1000Decay5pctTch'] = {'mode':'constant','factor': 1.2705e-05}
globalXSBRMap['TprimeM1000Decay5pct']['TprimeM1000Decay5pctInt'] = {'mode':'constant','factor': -0.0013717108476}
globalXSBRMap['TprimeM1000Decay5pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM1000Decay5pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM1000Decay5pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM1000Decay5pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM1000Decay5pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM1000Decay10pct'] = od()
globalXSBRMap['TprimeM1000Decay10pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1000Decay10pct']['TprimeM1000Decay10pctSch'] = {'mode':'constant','factor': 0.0013693953}
globalXSBRMap['TprimeM1000Decay10pct']['TprimeM1000Decay10pctTch'] = {'mode':'constant','factor': 1.2705e-05}
globalXSBRMap['TprimeM1000Decay10pct']['TprimeM1000Decay10pctInt'] = {'mode':'constant','factor': -0.001260345288}
globalXSBRMap['TprimeM1000Decay10pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM1000Decay10pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM1000Decay10pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM1000Decay10pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM1000Decay10pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM1000Decay20pct'] = od()
globalXSBRMap['TprimeM1000Decay20pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1000Decay20pct']['TprimeM1000Decay20pctSch'] = {'mode':'constant','factor': 0.00073076581}
globalXSBRMap['TprimeM1000Decay20pct']['TprimeM1000Decay20pctTch'] = {'mode':'constant','factor': 1.2647e-05}
globalXSBRMap['TprimeM1000Decay20pct']['TprimeM1000Decay20pctInt'] = {'mode':'constant','factor': -0.0009496318152}
globalXSBRMap['TprimeM1000Decay20pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM1000Decay20pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM1000Decay20pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM1000Decay20pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM1000Decay20pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM1000Decay30pct'] = od()
globalXSBRMap['TprimeM1000Decay30pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1000Decay30pct']['TprimeM1000Decay30pctSch'] = {'mode':'constant','factor': 0.00050494626}
globalXSBRMap['TprimeM1000Decay30pct']['TprimeM1000Decay30pctTch'] = {'mode':'constant','factor': 1.2582e-05}
globalXSBRMap['TprimeM1000Decay30pct']['TprimeM1000Decay30pctInt'] = {'mode':'constant','factor': -0.001125767079}
globalXSBRMap['TprimeM1000Decay30pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM1000Decay30pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM1000Decay30pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM1000Decay30pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM1000Decay30pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM1100Decay5pct'] = od()
globalXSBRMap['TprimeM1100Decay5pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1100Decay5pct']['TprimeM1100Decay5pctSch'] = {'mode':'constant','factor': 0.00867}
globalXSBRMap['TprimeM1100Decay5pct']['TprimeM1100Decay5pctTch'] = {'mode':'constant','factor': 1.1412e-05}
globalXSBRMap['TprimeM1100Decay5pct']['TprimeM1100Decay5pctInt'] = {'mode':'constant','factor': -0.001346053222}
globalXSBRMap['TprimeM1100Decay5pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM1100Decay5pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM1100Decay5pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM1100Decay5pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM1100Decay5pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM1100Decay10pct'] = od()
globalXSBRMap['TprimeM1100Decay10pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1100Decay10pct']['TprimeM1100Decay10pctSch'] = {'mode':'constant','factor': 0.0010252512}
globalXSBRMap['TprimeM1100Decay10pct']['TprimeM1100Decay10pctTch'] = {'mode':'constant','factor': 1.1384e-05}
globalXSBRMap['TprimeM1100Decay10pct']['TprimeM1100Decay10pctInt'] = {'mode':'constant','factor': -0.0011855645672}
globalXSBRMap['TprimeM1100Decay10pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM1100Decay10pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM1100Decay10pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM1100Decay10pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM1100Decay10pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM1100Decay20pct'] = od()
globalXSBRMap['TprimeM1100Decay20pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1100Decay20pct']['TprimeM1100Decay20pctSch'] = {'mode':'constant','factor': 0.00056846644}
globalXSBRMap['TprimeM1100Decay20pct']['TprimeM1100Decay20pctTch'] = {'mode':'constant','factor': 1.1343e-05}
globalXSBRMap['TprimeM1100Decay20pct']['TprimeM1100Decay20pctInt'] = {'mode':'constant','factor': -0.0010308489156}
globalXSBRMap['TprimeM1100Decay20pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM1100Decay20pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM1100Decay20pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM1100Decay20pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM1100Decay20pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM1100Decay30pct'] = od()
globalXSBRMap['TprimeM1100Decay30pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1100Decay30pct']['TprimeM1100Decay30pctSch'] = {'mode':'constant','factor': 0.00039152303}
globalXSBRMap['TprimeM1100Decay30pct']['TprimeM1100Decay30pctTch'] = {'mode':'constant','factor': 1.1258e-05}
globalXSBRMap['TprimeM1100Decay30pct']['TprimeM1100Decay30pctInt'] = {'mode':'constant','factor': -0.00082754683}
globalXSBRMap['TprimeM1100Decay30pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM1100Decay30pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM1100Decay30pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM1100Decay30pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM1100Decay30pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM1200Decay5pct'] = od()
globalXSBRMap['TprimeM1200Decay5pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1200Decay5pct']['TprimeM1200Decay5pctSch'] = {'mode':'constant','factor': 0.00536}
globalXSBRMap['TprimeM1200Decay5pct']['TprimeM1200Decay5pctTch'] = {'mode':'constant','factor': 1.0274e-05}
globalXSBRMap['TprimeM1200Decay5pct']['TprimeM1200Decay5pctInt'] = {'mode':'constant','factor': -0.0011203807296}
globalXSBRMap['TprimeM1200Decay5pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM1200Decay5pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM1200Decay5pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM1200Decay5pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM1200Decay5pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM1200Decay10pct'] = od()
globalXSBRMap['TprimeM1200Decay10pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1200Decay10pct']['TprimeM1200Decay10pctSch'] = {'mode':'constant','factor': 0.00079786165}
globalXSBRMap['TprimeM1200Decay10pct']['TprimeM1200Decay10pctTch'] = {'mode':'constant','factor': 1.0257e-05}
globalXSBRMap['TprimeM1200Decay10pct']['TprimeM1200Decay10pctInt'] = {'mode':'constant','factor': -0.001269849632}
globalXSBRMap['TprimeM1200Decay10pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM1200Decay10pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM1200Decay10pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM1200Decay10pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM1200Decay10pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM1200Decay20pct'] = od()
globalXSBRMap['TprimeM1200Decay20pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1200Decay20pct']['TprimeM1200Decay20pctSch'] = {'mode':'constant','factor': 0.00044261784}
globalXSBRMap['TprimeM1200Decay20pct']['TprimeM1200Decay20pctTch'] = {'mode':'constant','factor': 1.0175e-05}
globalXSBRMap['TprimeM1200Decay20pct']['TprimeM1200Decay20pctInt'] = {'mode':'constant','factor': -0.001063748595}
globalXSBRMap['TprimeM1200Decay20pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM1200Decay20pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM1200Decay20pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM1200Decay20pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM1200Decay20pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM1200Decay30pct'] = od()
globalXSBRMap['TprimeM1200Decay30pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1200Decay30pct']['TprimeM1200Decay30pctSch'] = {'mode':'constant','factor': 0.00031748181}
globalXSBRMap['TprimeM1200Decay30pct']['TprimeM1200Decay30pctTch'] = {'mode':'constant','factor': 1.0106e-05}
globalXSBRMap['TprimeM1200Decay30pct']['TprimeM1200Decay30pctInt'] = {'mode':'constant','factor': -0.0009637681196}
globalXSBRMap['TprimeM1200Decay30pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM1200Decay30pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM1200Decay30pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM1200Decay30pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM1200Decay30pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM1400Decay5pct'] = od()
globalXSBRMap['TprimeM1400Decay5pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1400Decay5pct']['TprimeM1400Decay5pctSch'] = {'mode':'constant','factor': 0.00088222038}
globalXSBRMap['TprimeM1400Decay5pct']['TprimeM1400Decay5pctTch'] = {'mode':'constant','factor': 8.3784e-06}
globalXSBRMap['TprimeM1400Decay5pct']['TprimeM1400Decay5pctInt'] = {'mode':'constant','factor': -0.000882467768}
globalXSBRMap['TprimeM1400Decay5pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM1400Decay5pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM1400Decay5pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM1400Decay5pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM1400Decay5pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM1400Decay10pct'] = od()
globalXSBRMap['TprimeM1400Decay10pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1400Decay10pct']['TprimeM1400Decay10pctSch'] = {'mode':'constant','factor': 0.00048325612}
globalXSBRMap['TprimeM1400Decay10pct']['TprimeM1400Decay10pctTch'] = {'mode':'constant','factor': 8.3636e-06}
globalXSBRMap['TprimeM1400Decay10pct']['TprimeM1400Decay10pctInt'] = {'mode':'constant','factor': -0.0011209913034}
globalXSBRMap['TprimeM1400Decay10pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM1400Decay10pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM1400Decay10pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM1400Decay10pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM1400Decay10pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM1400Decay20pct'] = od()
globalXSBRMap['TprimeM1400Decay20pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1400Decay20pct']['TprimeM1400Decay20pctSch'] = {'mode':'constant','factor': 0.00027827536}
globalXSBRMap['TprimeM1400Decay20pct']['TprimeM1400Decay20pctTch'] = {'mode':'constant','factor': 8.3033e-06}
globalXSBRMap['TprimeM1400Decay20pct']['TprimeM1400Decay20pctInt'] = {'mode':'constant','factor': -0.0009042237104}
globalXSBRMap['TprimeM1400Decay20pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM1400Decay20pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM1400Decay20pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM1400Decay20pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM1400Decay20pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM1400Decay30pct'] = od()
globalXSBRMap['TprimeM1400Decay30pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1400Decay30pct']['TprimeM1400Decay30pctSch'] = {'mode':'constant','factor': 0.00020523262}
globalXSBRMap['TprimeM1400Decay30pct']['TprimeM1400Decay30pctTch'] = {'mode':'constant','factor': 8.2059e-06}
globalXSBRMap['TprimeM1400Decay30pct']['TprimeM1400Decay30pctInt'] = {'mode':'constant','factor': -0.000956401356}
globalXSBRMap['TprimeM1400Decay30pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM1400Decay30pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM1400Decay30pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM1400Decay30pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM1400Decay30pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM1600Decay5pct'] = od()
globalXSBRMap['TprimeM1600Decay5pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1600Decay5pct']['TprimeM1600Decay5pctSch'] = {'mode':'constant','factor': 0.00052213167}
globalXSBRMap['TprimeM1600Decay5pct']['TprimeM1600Decay5pctTch'] = {'mode':'constant','factor': 6.9611e-06}
globalXSBRMap['TprimeM1600Decay5pct']['TprimeM1600Decay5pctInt'] = {'mode':'constant','factor': -0.000799906848}
globalXSBRMap['TprimeM1600Decay5pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM1600Decay5pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM1600Decay5pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM1600Decay5pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM1600Decay5pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM1600Decay10pct'] = od()
globalXSBRMap['TprimeM1600Decay10pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1600Decay10pct']['TprimeM1600Decay10pctSch'] = {'mode':'constant','factor': 0.00030337975}
globalXSBRMap['TprimeM1600Decay10pct']['TprimeM1600Decay10pctTch'] = {'mode':'constant','factor': 6.9478e-06}
globalXSBRMap['TprimeM1600Decay10pct']['TprimeM1600Decay10pctInt'] = {'mode':'constant','factor': -0.0006897165604}
globalXSBRMap['TprimeM1600Decay10pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM1600Decay10pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM1600Decay10pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM1600Decay10pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM1600Decay10pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM1600Decay20pct'] = od()
globalXSBRMap['TprimeM1600Decay20pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1600Decay20pct']['TprimeM1600Decay20pctSch'] = {'mode':'constant','factor': 0.00018522063}
globalXSBRMap['TprimeM1600Decay20pct']['TprimeM1600Decay20pctTch'] = {'mode':'constant','factor': 6.934e-06}
globalXSBRMap['TprimeM1600Decay20pct']['TprimeM1600Decay20pctInt'] = {'mode':'constant','factor': -0.0007807688184}
globalXSBRMap['TprimeM1600Decay20pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM1600Decay20pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM1600Decay20pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM1600Decay20pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM1600Decay20pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM1600Decay30pct'] = od()
globalXSBRMap['TprimeM1600Decay30pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1600Decay30pct']['TprimeM1600Decay30pctSch'] = {'mode':'constant','factor': 0.00014134351}
globalXSBRMap['TprimeM1600Decay30pct']['TprimeM1600Decay30pctTch'] = {'mode':'constant','factor': 6.8426e-06}
globalXSBRMap['TprimeM1600Decay30pct']['TprimeM1600Decay30pctInt'] = {'mode':'constant','factor': -0.0007071464088}
globalXSBRMap['TprimeM1600Decay30pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM1600Decay30pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM1600Decay30pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM1600Decay30pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM1600Decay30pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM1800Decay5pct'] = od()
globalXSBRMap['TprimeM1800Decay5pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1800Decay5pct']['TprimeM1800Decay5pctSch'] = {'mode':'constant','factor': 0.00033434225}
globalXSBRMap['TprimeM1800Decay5pct']['TprimeM1800Decay5pctTch'] = {'mode':'constant','factor': 5.8887e-06}
globalXSBRMap['TprimeM1800Decay5pct']['TprimeM1800Decay5pctInt'] = {'mode':'constant','factor': -0.0006234054228}
globalXSBRMap['TprimeM1800Decay5pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM1800Decay5pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM1800Decay5pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM1800Decay5pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM1800Decay5pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM1800Decay10pct'] = od()
globalXSBRMap['TprimeM1800Decay10pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1800Decay10pct']['TprimeM1800Decay10pctSch'] = {'mode':'constant','factor': 0.00019638078}
globalXSBRMap['TprimeM1800Decay10pct']['TprimeM1800Decay10pctTch'] = {'mode':'constant','factor': 5.8799e-06}
globalXSBRMap['TprimeM1800Decay10pct']['TprimeM1800Decay10pctInt'] = {'mode':'constant','factor': -0.0006043918064}
globalXSBRMap['TprimeM1800Decay10pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM1800Decay10pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM1800Decay10pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM1800Decay10pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM1800Decay10pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM1800Decay20pct'] = od()
globalXSBRMap['TprimeM1800Decay20pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1800Decay20pct']['TprimeM1800Decay20pctSch'] = {'mode':'constant','factor': 0.00012599554}
globalXSBRMap['TprimeM1800Decay20pct']['TprimeM1800Decay20pctTch'] = {'mode':'constant','factor': 5.7786e-06}
globalXSBRMap['TprimeM1800Decay20pct']['TprimeM1800Decay20pctInt'] = {'mode':'constant','factor': -0.0007089857412}
globalXSBRMap['TprimeM1800Decay20pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM1800Decay20pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM1800Decay20pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM1800Decay20pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM1800Decay20pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM1800Decay30pct'] = od()
globalXSBRMap['TprimeM1800Decay30pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1800Decay30pct']['TprimeM1800Decay30pctSch'] = {'mode':'constant','factor': 9.8115548e-05}
globalXSBRMap['TprimeM1800Decay30pct']['TprimeM1800Decay30pctTch'] = {'mode':'constant','factor': 5.6967e-06}
globalXSBRMap['TprimeM1800Decay30pct']['TprimeM1800Decay30pctInt'] = {'mode':'constant','factor': -0.000692885728}
globalXSBRMap['TprimeM1800Decay30pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM1800Decay30pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM1800Decay30pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM1800Decay30pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM1800Decay30pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM2000Decay5pct'] = od()
globalXSBRMap['TprimeM2000Decay5pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM2000Decay5pct']['TprimeM2000Decay5pctSch'] = {'mode':'constant','factor': 0.00021921284}
globalXSBRMap['TprimeM2000Decay5pct']['TprimeM2000Decay5pctTch'] = {'mode':'constant','factor': 4.9841e-06}
globalXSBRMap['TprimeM2000Decay5pct']['TprimeM2000Decay5pctInt'] = {'mode':'constant','factor': -0.0007299251196}
globalXSBRMap['TprimeM2000Decay5pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM2000Decay5pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM2000Decay5pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM2000Decay5pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM2000Decay5pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM2000Decay10pct'] = od()
globalXSBRMap['TprimeM2000Decay10pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM2000Decay10pct']['TprimeM2000Decay10pctSch'] = {'mode':'constant','factor': 0.00013383156}
globalXSBRMap['TprimeM2000Decay10pct']['TprimeM2000Decay10pctTch'] = {'mode':'constant','factor': 4.9834e-06}
globalXSBRMap['TprimeM2000Decay10pct']['TprimeM2000Decay10pctInt'] = {'mode':'constant','factor': -0.0006173815158}
globalXSBRMap['TprimeM2000Decay10pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM2000Decay10pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM2000Decay10pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM2000Decay10pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM2000Decay10pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM2000Decay20pct'] = od()
globalXSBRMap['TprimeM2000Decay20pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM2000Decay20pct']['TprimeM2000Decay20pctSch'] = {'mode':'constant','factor': 9.0487645e-05}
globalXSBRMap['TprimeM2000Decay20pct']['TprimeM2000Decay20pctTch'] = {'mode':'constant','factor': 4.97e-06}
globalXSBRMap['TprimeM2000Decay20pct']['TprimeM2000Decay20pctInt'] = {'mode':'constant','factor': -0.0006798876024}
globalXSBRMap['TprimeM2000Decay20pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM2000Decay20pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM2000Decay20pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM2000Decay20pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM2000Decay20pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM2000Decay30pct'] = od()
globalXSBRMap['TprimeM2000Decay30pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM2000Decay30pct']['TprimeM2000Decay30pctSch'] = {'mode':'constant','factor': 7.4844071e-05}
globalXSBRMap['TprimeM2000Decay30pct']['TprimeM2000Decay30pctTch'] = {'mode':'constant','factor': 4.876e-06}
globalXSBRMap['TprimeM2000Decay30pct']['TprimeM2000Decay30pctInt'] = {'mode':'constant','factor': -0.0005601280776}
globalXSBRMap['TprimeM2000Decay30pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM2000Decay30pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM2000Decay30pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM2000Decay30pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM2000Decay30pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM2200Decay5pct'] = od()
globalXSBRMap['TprimeM2200Decay5pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM2200Decay5pct']['TprimeM2200Decay5pctSch'] = {'mode':'constant','factor': 0.00014634228}
globalXSBRMap['TprimeM2200Decay5pct']['TprimeM2200Decay5pctTch'] = {'mode':'constant','factor': 4.297e-06}
globalXSBRMap['TprimeM2200Decay5pct']['TprimeM2200Decay5pctInt'] = {'mode':'constant','factor': -0.0005155298382}
globalXSBRMap['TprimeM2200Decay5pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM2200Decay5pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM2200Decay5pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM2200Decay5pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM2200Decay5pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM2200Decay10pct'] = od()
globalXSBRMap['TprimeM2200Decay10pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM2200Decay10pct']['TprimeM2200Decay10pctSch'] = {'mode':'constant','factor': 9.3476675e-05}
globalXSBRMap['TprimeM2200Decay10pct']['TprimeM2200Decay10pctTch'] = {'mode':'constant','factor': 4.2862e-06}
globalXSBRMap['TprimeM2200Decay10pct']['TprimeM2200Decay10pctInt'] = {'mode':'constant','factor': -0.0005842469856}
globalXSBRMap['TprimeM2200Decay10pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM2200Decay10pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM2200Decay10pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM2200Decay10pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM2200Decay10pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM2200Decay20pct'] = od()
globalXSBRMap['TprimeM2200Decay20pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM2200Decay20pct']['TprimeM2200Decay20pctSch'] = {'mode':'constant','factor': 6.6480906e-05}
globalXSBRMap['TprimeM2200Decay20pct']['TprimeM2200Decay20pctTch'] = {'mode':'constant','factor': 4.2498e-06}
globalXSBRMap['TprimeM2200Decay20pct']['TprimeM2200Decay20pctInt'] = {'mode':'constant','factor': -0.000432861073}
globalXSBRMap['TprimeM2200Decay20pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM2200Decay20pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM2200Decay20pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM2200Decay20pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM2200Decay20pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM2200Decay30pct'] = od()
globalXSBRMap['TprimeM2200Decay30pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM2200Decay30pct']['TprimeM2200Decay30pctSch'] = {'mode':'constant','factor': 5.6097924e-05}
globalXSBRMap['TprimeM2200Decay30pct']['TprimeM2200Decay30pctTch'] = {'mode':'constant','factor': 4.1761e-06}
globalXSBRMap['TprimeM2200Decay30pct']['TprimeM2200Decay30pctInt'] = {'mode':'constant','factor': -0.0005469089782}
globalXSBRMap['TprimeM2200Decay30pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM2200Decay30pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM2200Decay30pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM2200Decay30pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM2200Decay30pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM2400Decay5pct'] = od()
globalXSBRMap['TprimeM2400Decay5pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM2400Decay5pct']['TprimeM2400Decay5pctSch'] = {'mode':'constant','factor': 0.00010079917}
globalXSBRMap['TprimeM2400Decay5pct']['TprimeM2400Decay5pctTch'] = {'mode':'constant','factor': 3.7373e-06}
globalXSBRMap['TprimeM2400Decay5pct']['TprimeM2400Decay5pctInt'] = {'mode':'constant','factor': -0.000491219104}
globalXSBRMap['TprimeM2400Decay5pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM2400Decay5pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM2400Decay5pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM2400Decay5pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM2400Decay5pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM2400Decay10pct'] = od()
globalXSBRMap['TprimeM2400Decay10pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM2400Decay10pct']['TprimeM2400Decay10pctSch'] = {'mode':'constant','factor': 6.8158278e-05}
globalXSBRMap['TprimeM2400Decay10pct']['TprimeM2400Decay10pctTch'] = {'mode':'constant','factor': 3.7282e-06}
globalXSBRMap['TprimeM2400Decay10pct']['TprimeM2400Decay10pctInt'] = {'mode':'constant','factor': -0.00054231438}
globalXSBRMap['TprimeM2400Decay10pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM2400Decay10pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM2400Decay10pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM2400Decay10pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM2400Decay10pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM2400Decay20pct'] = od()
globalXSBRMap['TprimeM2400Decay20pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM2400Decay20pct']['TprimeM2400Decay20pctSch'] = {'mode':'constant','factor': 5.0504801e-05}
globalXSBRMap['TprimeM2400Decay20pct']['TprimeM2400Decay20pctTch'] = {'mode':'constant','factor': 3.6923e-06}
globalXSBRMap['TprimeM2400Decay20pct']['TprimeM2400Decay20pctInt'] = {'mode':'constant','factor': -0.0004391931348}
globalXSBRMap['TprimeM2400Decay20pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM2400Decay20pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM2400Decay20pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM2400Decay20pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM2400Decay20pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM2400Decay30pct'] = od()
globalXSBRMap['TprimeM2400Decay30pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM2400Decay30pct']['TprimeM2400Decay30pctSch'] = {'mode':'constant','factor': 4.3144529e-05}
globalXSBRMap['TprimeM2400Decay30pct']['TprimeM2400Decay30pctTch'] = {'mode':'constant','factor': 3.6269e-06}
globalXSBRMap['TprimeM2400Decay30pct']['TprimeM2400Decay30pctInt'] = {'mode':'constant','factor': -0.0004653822376}
globalXSBRMap['TprimeM2400Decay30pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM2400Decay30pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM2400Decay30pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM2400Decay30pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM2400Decay30pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM2600Decay5pct'] = od()
globalXSBRMap['TprimeM2600Decay5pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM2600Decay5pct']['TprimeM2600Decay5pctSch'] = {'mode':'constant','factor': 7.0977269e-05}
globalXSBRMap['TprimeM2600Decay5pct']['TprimeM2600Decay5pctTch'] = {'mode':'constant','factor': 3.2644e-06}
globalXSBRMap['TprimeM2600Decay5pct']['TprimeM2600Decay5pctInt'] = {'mode':'constant','factor': -0.0004106119836}
globalXSBRMap['TprimeM2600Decay5pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM2600Decay5pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM2600Decay5pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM2600Decay5pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM2600Decay5pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM2600Decay10pct'] = od()
globalXSBRMap['TprimeM2600Decay10pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM2600Decay10pct']['TprimeM2600Decay10pctSch'] = {'mode':'constant','factor': 5.1219849e-05}
globalXSBRMap['TprimeM2600Decay10pct']['TprimeM2600Decay10pctTch'] = {'mode':'constant','factor': 3.2556e-06}
globalXSBRMap['TprimeM2600Decay10pct']['TprimeM2600Decay10pctInt'] = {'mode':'constant','factor': -0.0004076551962}
globalXSBRMap['TprimeM2600Decay10pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM2600Decay10pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM2600Decay10pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM2600Decay10pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM2600Decay10pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM2600Decay20pct'] = od()
globalXSBRMap['TprimeM2600Decay20pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM2600Decay20pct']['TprimeM2600Decay20pctSch'] = {'mode':'constant','factor': 3.9448459e-05}
globalXSBRMap['TprimeM2600Decay20pct']['TprimeM2600Decay20pctTch'] = {'mode':'constant','factor': 3.2255e-06}
globalXSBRMap['TprimeM2600Decay20pct']['TprimeM2600Decay20pctInt'] = {'mode':'constant','factor': -0.000491577408}
globalXSBRMap['TprimeM2600Decay20pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM2600Decay20pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM2600Decay20pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM2600Decay20pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM2600Decay20pct']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeM2600Decay30pct'] = od()
globalXSBRMap['TprimeM2600Decay30pct']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM2600Decay30pct']['TprimeM2600Decay30pctSch'] = {'mode':'constant','factor': 3.4491092e-05}
globalXSBRMap['TprimeM2600Decay30pct']['TprimeM2600Decay30pctTch'] = {'mode':'constant','factor': 3.1687e-06}
globalXSBRMap['TprimeM2600Decay30pct']['TprimeM2600Decay30pctInt'] = {'mode':'constant','factor': -0.0004387861656}
globalXSBRMap['TprimeM2600Decay30pct']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeM2600Decay30pct']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeM2600Decay30pct']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeM2600Decay30pct']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeM2600Decay30pct']['VH'] = {'mode':'constant','factor': 2.257}

