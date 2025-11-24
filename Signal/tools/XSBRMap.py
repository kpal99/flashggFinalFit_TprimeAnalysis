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
globalXSBRMap['TprimeRun2nwa'] = od()
globalXSBRMap['TprimeRun2nwa']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeRun2nwa']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['TprimeRun2nwa']['THQ'] = {'mode':'tHq'}
globalXSBRMap['TprimeRun2nwa']['TTH'] = {'mode':'ttH'}
globalXSBRMap['TprimeRun2nwa']['VBF'] = {'mode':'qqH'}
globalXSBRMap['TprimeRun2nwa']['VH'] = {'mode':'constant','factor': 2.257}

globalXSBRMap['TprimeRun2nwa']['TprimeM700Decay5pctSch'] = {'mode':'constant','factor': 0.20112199999999997}
globalXSBRMap['TprimeRun2nwa']['TprimeM700Decay5pctTch'] = {'mode':'constant','factor': 0}
globalXSBRMap['TprimeRun2nwa']['TprimeM700Decay5pctInt'] = {'mode':'constant','factor': 0}

globalXSBRMap['TprimeRun2nwa']['TprimeM800Decay5pctSch'] = {'mode':'constant','factor': 0.104193}
globalXSBRMap['TprimeRun2nwa']['TprimeM800Decay5pctTch'] = {'mode':'constant','factor': 0}
globalXSBRMap['TprimeRun2nwa']['TprimeM800Decay5pctInt'] = {'mode':'constant','factor': 0}

globalXSBRMap['TprimeRun2nwa']['TprimeM900Decay5pctSch'] = {'mode':'constant','factor': 0.056977}
globalXSBRMap['TprimeRun2nwa']['TprimeM900Decay5pctTch'] = {'mode':'constant','factor': 0}
globalXSBRMap['TprimeRun2nwa']['TprimeM900Decay5pctInt'] = {'mode':'constant','factor': 0}

globalXSBRMap['TprimeRun2nwa']['TprimeM1000Decay5pctSch'] = {'mode':'constant','factor': 0.032915}
globalXSBRMap['TprimeRun2nwa']['TprimeM1000Decay5pctTch'] = {'mode':'constant','factor': 0}
globalXSBRMap['TprimeRun2nwa']['TprimeM1000Decay5pctInt'] = {'mode':'constant','factor': 0}

globalXSBRMap['TprimeRun2nwa']['TprimeM1100Decay5pctSch'] = {'mode':'constant','factor': 0.019680899999999998}
globalXSBRMap['TprimeRun2nwa']['TprimeM1100Decay5pctTch'] = {'mode':'constant','factor': 0}
globalXSBRMap['TprimeRun2nwa']['TprimeM1100Decay5pctInt'] = {'mode':'constant','factor': 0}

globalXSBRMap['TprimeRun2nwa']['TprimeM1200Decay5pctSch'] = {'mode':'constant','factor': 0.0121672}
globalXSBRMap['TprimeRun2nwa']['TprimeM1200Decay5pctTch'] = {'mode':'constant','factor': 0}
globalXSBRMap['TprimeRun2nwa']['TprimeM1200Decay5pctInt'] = {'mode':'constant','factor': 0}

globalXSBRMap['TprimeRun2nwa']['TprimeM1400Decay5pctSch'] = {'mode':'constant','factor': 0.0049881948097861475}
globalXSBRMap['TprimeRun2nwa']['TprimeM1400Decay5pctTch'] = {'mode':'constant','factor': 0}
globalXSBRMap['TprimeRun2nwa']['TprimeM1400Decay5pctInt'] = {'mode':'constant','factor': 0}

globalXSBRMap['TprimeRun2nwa']['TprimeM1600Decay5pctSch'] = {'mode':'constant','factor': 0.002211555284472077}
globalXSBRMap['TprimeRun2nwa']['TprimeM1600Decay5pctTch'] = {'mode':'constant','factor': 0}
globalXSBRMap['TprimeRun2nwa']['TprimeM1600Decay5pctInt'] = {'mode':'constant','factor': 0}

globalXSBRMap['TprimeRun2nwa']['TprimeM1800Decay5pctSch'] = {'mode':'constant','factor': 0.001041436809704427}
globalXSBRMap['TprimeRun2nwa']['TprimeM1800Decay5pctTch'] = {'mode':'constant','factor': 0}
globalXSBRMap['TprimeRun2nwa']['TprimeM1800Decay5pctInt'] = {'mode':'constant','factor': 0}

globalXSBRMap['TprimeRun2nwa']['TprimeM2000Decay5pctSch'] = {'mode':'constant','factor': 0.0005120643048699948}
globalXSBRMap['TprimeRun2nwa']['TprimeM2000Decay5pctTch'] = {'mode':'constant','factor': 0}
globalXSBRMap['TprimeRun2nwa']['TprimeM2000Decay5pctInt'] = {'mode':'constant','factor': 0}


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

globalXSBRMap['TprimeRun2']['TprimeM700Decay5pctSch'] = {'mode':'constant','factor': 0.09325453362566727}
globalXSBRMap['TprimeRun2']['TprimeM700Decay5pctTch'] = {'mode':'constant','factor': 0.00023466052486970654}
globalXSBRMap['TprimeRun2']['TprimeM700Decay5pctInt'] = {'mode':'constant','factor': -0.00013142734465876704}

globalXSBRMap['TprimeRun2']['TprimeM700Decay10pctSch'] = {'mode':'constant','factor': 0.04656889354794067}
globalXSBRMap['TprimeRun2']['TprimeM700Decay10pctTch'] = {'mode':'constant','factor': 0.00023466052486970654}
globalXSBRMap['TprimeRun2']['TprimeM700Decay10pctInt'] = {'mode':'constant','factor': -8.027381098233608e-05}

globalXSBRMap['TprimeRun2']['TprimeM700Decay20pctSch'] = {'mode':'constant','factor': 0.02279151698154088}
globalXSBRMap['TprimeRun2']['TprimeM700Decay20pctTch'] = {'mode':'constant','factor': 0.0002367360187325674}
globalXSBRMap['TprimeRun2']['TprimeM700Decay20pctInt'] = {'mode':'constant','factor': -6.220448157566655e-05}

globalXSBRMap['TprimeRun2']['TprimeM700Decay30pctSch'] = {'mode':'constant','factor': 0.014787893772883667}
globalXSBRMap['TprimeRun2']['TprimeM700Decay30pctTch'] = {'mode':'constant','factor': 0.00023466052486970654}
globalXSBRMap['TprimeRun2']['TprimeM700Decay30pctInt'] = {'mode':'constant','factor': -4.355171703145966e-05}

globalXSBRMap['TprimeRun2']['TprimeM800Decay5pctSch'] = {'mode':'constant','factor': 0.0660785358588328}
globalXSBRMap['TprimeRun2']['TprimeM800Decay5pctTch'] = {'mode':'constant','factor': 0.00021157065564537944}
globalXSBRMap['TprimeRun2']['TprimeM800Decay5pctInt'] = {'mode':'constant','factor': -0.00018206608262560643}

globalXSBRMap['TprimeRun2']['TprimeM800Decay10pctSch'] = {'mode':'constant','factor': 0.03332464833555978}
globalXSBRMap['TprimeRun2']['TprimeM800Decay10pctTch'] = {'mode':'constant','factor': 0.00021157065564537944}
globalXSBRMap['TprimeRun2']['TprimeM800Decay10pctInt'] = {'mode':'constant','factor': -0.00019253359538730464}

globalXSBRMap['TprimeRun2']['TprimeM800Decay20pctSch'] = {'mode':'constant','factor': 0.016681781922744207}
globalXSBRMap['TprimeRun2']['TprimeM800Decay20pctTch'] = {'mode':'constant','factor': 0.00021131121891252184}
globalXSBRMap['TprimeRun2']['TprimeM800Decay20pctInt'] = {'mode':'constant','factor': -0.00013182202136945398}

globalXSBRMap['TprimeRun2']['TprimeM800Decay30pctSch'] = {'mode':'constant','factor': 0.011146699227227136}
globalXSBRMap['TprimeRun2']['TprimeM800Decay30pctTch'] = {'mode':'constant','factor': 0.00021079234544680661}
globalXSBRMap['TprimeRun2']['TprimeM800Decay30pctInt'] = {'mode':'constant','factor': -0.000122469899311871}

globalXSBRMap['TprimeRun2']['TprimeM900Decay5pctSch'] = {'mode':'constant','factor': 0.047593668642728224}
globalXSBRMap['TprimeRun2']['TprimeM900Decay5pctTch'] = {'mode':'constant','factor': 0.0001883510680546234}
globalXSBRMap['TprimeRun2']['TprimeM900Decay5pctInt'] = {'mode':'constant','factor': -0.00020969345237369563}

globalXSBRMap['TprimeRun2']['TprimeM900Decay10pctSch'] = {'mode':'constant','factor': 0.024244362685543485}
globalXSBRMap['TprimeRun2']['TprimeM900Decay10pctTch'] = {'mode':'constant','factor': 0.00018809163132176582}
globalXSBRMap['TprimeRun2']['TprimeM900Decay10pctInt'] = {'mode':'constant','factor': -0.00019184720110784913}

globalXSBRMap['TprimeRun2']['TprimeM900Decay20pctSch'] = {'mode':'constant','factor': 0.012578789992601135}
globalXSBRMap['TprimeRun2']['TprimeM900Decay20pctTch'] = {'mode':'constant','factor': 0.0001878321945889082}
globalXSBRMap['TprimeRun2']['TprimeM900Decay20pctInt'] = {'mode':'constant','factor': -0.00016665653105182735}

globalXSBRMap['TprimeRun2']['TprimeM900Decay30pctSch'] = {'mode':'constant','factor': 0.008447260021843723}
globalXSBRMap['TprimeRun2']['TprimeM900Decay30pctTch'] = {'mode':'constant','factor': 0.0001867944476574778}
globalXSBRMap['TprimeRun2']['TprimeM900Decay30pctInt'] = {'mode':'constant','factor': -0.00014882743964296733}

globalXSBRMap['TprimeRun2']['TprimeM1000Decay5pctSch'] = {'mode':'constant','factor': 0.034881268732705424}
globalXSBRMap['TprimeRun2']['TprimeM1000Decay5pctTch'] = {'mode':'constant','factor': 0.00016902303145673164}
globalXSBRMap['TprimeRun2']['TprimeM1000Decay5pctInt'] = {'mode':'constant','factor': -0.00020866386095451202}

globalXSBRMap['TprimeRun2']['TprimeM1000Decay10pctSch'] = {'mode':'constant','factor': 0.018082740280175293}
globalXSBRMap['TprimeRun2']['TprimeM1000Decay10pctTch'] = {'mode':'constant','factor': 0.00016902303145673164}
globalXSBRMap['TprimeRun2']['TprimeM1000Decay10pctInt'] = {'mode':'constant','factor': -0.00019819634819281357}

globalXSBRMap['TprimeRun2']['TprimeM1000Decay20pctSch'] = {'mode':'constant','factor': 0.009392906913109704}
globalXSBRMap['TprimeRun2']['TprimeM1000Decay20pctTch'] = {'mode':'constant','factor': 0.00016824472125815884}
globalXSBRMap['TprimeRun2']['TprimeM1000Decay20pctInt'] = {'mode':'constant','factor': -0.00017743292123928087}

globalXSBRMap['TprimeRun2']['TprimeM1000Decay30pctSch'] = {'mode':'constant','factor': 0.006530022566025998}
globalXSBRMap['TprimeRun2']['TprimeM1000Decay30pctTch'] = {'mode':'constant','factor': 0.0001675961294260147}
globalXSBRMap['TprimeRun2']['TprimeM1000Decay30pctInt'] = {'mode':'constant','factor': -0.00015829968069945517}

globalXSBRMap['TprimeRun2']['TprimeM1100Decay5pctSch'] = {'mode':'constant','factor': 0.025956645122403702}
globalXSBRMap['TprimeRun2']['TprimeM1100Decay5pctTch'] = {'mode':'constant','factor': 0.00015215964382098697}
globalXSBRMap['TprimeRun2']['TprimeM1100Decay5pctInt'] = {'mode':'constant','factor': -0.0002091786566641038}

globalXSBRMap['TprimeRun2']['TprimeM1100Decay10pctSch'] = {'mode':'constant','factor': 0.013542597455167149}
globalXSBRMap['TprimeRun2']['TprimeM1100Decay10pctTch'] = {'mode':'constant','factor': 0.00015202992545455831}
globalXSBRMap['TprimeRun2']['TprimeM1100Decay10pctInt'] = {'mode':'constant','factor': -0.00019819634819281357}

globalXSBRMap['TprimeRun2']['TprimeM1100Decay20pctSch'] = {'mode':'constant','factor': 0.007303144029941672}
globalXSBRMap['TprimeRun2']['TprimeM1100Decay20pctTch'] = {'mode':'constant','factor': 0.0001512516152559855}
globalXSBRMap['TprimeRun2']['TprimeM1100Decay20pctInt'] = {'mode':'constant','factor': -0.00017468734412145836}

globalXSBRMap['TprimeRun2']['TprimeM1100Decay30pctSch'] = {'mode':'constant','factor': 0.005094040249659137}
globalXSBRMap['TprimeRun2']['TprimeM1100Decay30pctTch'] = {'mode':'constant','factor': 0.00015008414995812617}
globalXSBRMap['TprimeRun2']['TprimeM1100Decay30pctInt'] = {'mode':'constant','factor': -0.00015908903412082905}

globalXSBRMap['TprimeRun2']['TprimeM1200Decay5pctSch'] = {'mode':'constant','factor': 0.01949667047424926}
globalXSBRMap['TprimeRun2']['TprimeM1200Decay5pctTch'] = {'mode':'constant','factor': 0.0001369825949488171}
globalXSBRMap['TprimeRun2']['TprimeM1200Decay5pctInt'] = {'mode':'constant','factor': -0.00019527917250512712}

globalXSBRMap['TprimeRun2']['TprimeM1200Decay10pctSch'] = {'mode':'constant','factor': 0.01030093547811133}
globalXSBRMap['TprimeRun2']['TprimeM1200Decay10pctTch'] = {'mode':'constant','factor': 0.0001365934398495306}
globalXSBRMap['TprimeRun2']['TprimeM1200Decay10pctInt'] = {'mode':'constant','factor': -0.00018584125116261229}

globalXSBRMap['TprimeRun2']['TprimeM1200Decay20pctSch'] = {'mode':'constant','factor': 0.0057011222045459395}
globalXSBRMap['TprimeRun2']['TprimeM1200Decay20pctTch'] = {'mode':'constant','factor': 0.00013594484801738668}
globalXSBRMap['TprimeRun2']['TprimeM1200Decay20pctInt'] = {'mode':'constant','factor': -0.00016711984719045984}

globalXSBRMap['TprimeRun2']['TprimeM1200Decay30pctSch'] = {'mode':'constant','factor': 0.004062779236550145}
globalXSBRMap['TprimeRun2']['TprimeM1200Decay30pctTch'] = {'mode':'constant','factor': 0.00013490710108595628}
globalXSBRMap['TprimeRun2']['TprimeM1200Decay30pctInt'] = {'mode':'constant','factor': -0.00015687541256958462}

globalXSBRMap['TprimeRun2']['TprimeM1400Decay5pctSch'] = {'mode':'constant','factor': 0.011266040124341637}
globalXSBRMap['TprimeRun2']['TprimeM1400Decay5pctTch'] = {'mode':'constant','factor': 0.0001120247812479152}
globalXSBRMap['TprimeRun2']['TprimeM1400Decay5pctInt'] = {'mode':'constant','factor': -0.00016785772104087465}

globalXSBRMap['TprimeRun2']['TprimeM1400Decay10pctSch'] = {'mode':'constant','factor': 0.006051361793903712}
globalXSBRMap['TprimeRun2']['TprimeM1400Decay10pctTch'] = {'mode':'constant','factor': 0.00011185614737155771}
globalXSBRMap['TprimeRun2']['TprimeM1400Decay10pctInt'] = {'mode':'constant','factor': -0.00016329319908249488}

globalXSBRMap['TprimeRun2']['TprimeM1400Decay20pctSch'] = {'mode':'constant','factor': 0.0035776325461064178}
globalXSBRMap['TprimeRun2']['TprimeM1400Decay20pctTch'] = {'mode':'constant','factor': 0.00011093514696991322}
globalXSBRMap['TprimeRun2']['TprimeM1400Decay20pctInt'] = {'mode':'constant','factor': -0.00015102390133722547}

globalXSBRMap['TprimeRun2']['TprimeM1400Decay30pctSch'] = {'mode':'constant','factor': 0.002643660307819027}
globalXSBRMap['TprimeRun2']['TprimeM1400Decay30pctTch'] = {'mode':'constant','factor': 0.00010984551269191123}
globalXSBRMap['TprimeRun2']['TprimeM1400Decay30pctInt'] = {'mode':'constant','factor': -0.00013765637274482686}

globalXSBRMap['TprimeRun2']['TprimeM1600Decay5pctSch'] = {'mode':'constant','factor': 0.006929555134626715}
globalXSBRMap['TprimeRun2']['TprimeM1600Decay5pctTch'] = {'mode':'constant','factor': 9.333236464552454e-05}
globalXSBRMap['TprimeRun2']['TprimeM1600Decay5pctInt'] = {'mode':'constant','factor': -0.00013909780073168368}

globalXSBRMap['TprimeRun2']['TprimeM1600Decay10pctSch'] = {'mode':'constant','factor': 0.003835772095299737}
globalXSBRMap['TprimeRun2']['TprimeM1600Decay10pctTch'] = {'mode':'constant','factor': 9.264485730345186e-05}
globalXSBRMap['TprimeRun2']['TprimeM1600Decay10pctInt'] = {'mode':'constant','factor': -0.00013521967305275942}

globalXSBRMap['TprimeRun2']['TprimeM1600Decay20pctSch'] = {'mode':'constant','factor': 0.002351793983354218}
globalXSBRMap['TprimeRun2']['TprimeM1600Decay20pctTch'] = {'mode':'constant','factor': 9.108823690630624e-05}
globalXSBRMap['TprimeRun2']['TprimeM1600Decay20pctInt'] = {'mode':'constant','factor': -0.00012761785640778836}

globalXSBRMap['TprimeRun2']['TprimeM1600Decay30pctSch'] = {'mode':'constant','factor': 0.0017862219057246324}
globalXSBRMap['TprimeRun2']['TprimeM1600Decay30pctTch'] = {'mode':'constant','factor': 8.982996875194678e-05}
globalXSBRMap['TprimeRun2']['TprimeM1600Decay30pctInt'] = {'mode':'constant','factor': -0.00012008467919076264}

globalXSBRMap['TprimeRun2']['TprimeM1800Decay5pctSch'] = {'mode':'constant','factor': 0.0044195047442293555}
globalXSBRMap['TprimeRun2']['TprimeM1800Decay5pctTch'] = {'mode':'constant','factor': 7.748078026792453e-05}
globalXSBRMap['TprimeRun2']['TprimeM1800Decay5pctInt'] = {'mode':'constant','factor': -0.00012090835232610952}

globalXSBRMap['TprimeRun2']['TprimeM1800Decay10pctSch'] = {'mode':'constant','factor': 0.002462054594818702}
globalXSBRMap['TprimeRun2']['TprimeM1800Decay10pctTch'] = {'mode':'constant','factor': 7.700082231213812e-05}
globalXSBRMap['TprimeRun2']['TprimeM1800Decay10pctInt'] = {'mode':'constant','factor': -0.00011673850707841647}

globalXSBRMap['TprimeRun2']['TprimeM1800Decay20pctSch'] = {'mode':'constant','factor': 0.0016085077437171709}
globalXSBRMap['TprimeRun2']['TprimeM1800Decay20pctTch'] = {'mode':'constant','factor': 7.719539986178115e-05}
globalXSBRMap['TprimeRun2']['TprimeM1800Decay20pctInt'] = {'mode':'constant','factor': -0.00011234558368990042}

globalXSBRMap['TprimeRun2']['TprimeM1800Decay30pctSch'] = {'mode':'constant','factor': 0.0012790230929880084}
globalXSBRMap['TprimeRun2']['TprimeM1800Decay30pctTch'] = {'mode':'constant','factor': 7.605387823720782e-05}
globalXSBRMap['TprimeRun2']['TprimeM1800Decay30pctInt'] = {'mode':'constant','factor': -0.00010764378287562952}

globalXSBRMap['TprimeRun2']['TprimeM2000Decay5pctSch'] = {'mode':'constant','factor': 0.002817482918833625}
globalXSBRMap['TprimeRun2']['TprimeM2000Decay5pctTch'] = {'mode':'constant','factor': 6.570235259618925e-05}
globalXSBRMap['TprimeRun2']['TprimeM2000Decay5pctInt'] = {'mode':'constant','factor': -0.00010445204947616077}

globalXSBRMap['TprimeRun2']['TprimeM2000Decay10pctSch'] = {'mode':'constant','factor': 0.0016487204373101}
globalXSBRMap['TprimeRun2']['TprimeM2000Decay10pctTch'] = {'mode':'constant','factor': 6.565046524961769e-05}
globalXSBRMap['TprimeRun2']['TprimeM2000Decay10pctInt'] = {'mode':'constant','factor': -0.00010230706735286193}

globalXSBRMap['TprimeRun2']['TprimeM2000Decay20pctSch'] = {'mode':'constant','factor': 0.0011685030447906677}
globalXSBRMap['TprimeRun2']['TprimeM2000Decay20pctTch'] = {'mode':'constant','factor': 6.506673260068792e-05}
globalXSBRMap['TprimeRun2']['TprimeM2000Decay20pctInt'] = {'mode':'constant','factor': -9.794846367831866e-05}

globalXSBRMap['TprimeRun2']['TprimeM2000Decay30pctSch'] = {'mode':'constant','factor': 0.0009360477321502504}
globalXSBRMap['TprimeRun2']['TprimeM2000Decay30pctTch'] = {'mode':'constant','factor': 6.361388689668544e-05}
globalXSBRMap['TprimeRun2']['TprimeM2000Decay30pctInt'] = {'mode':'constant','factor': -9.561472312816937e-05}

globalXSBRMap['TprimeRun2']['TprimeM2200Decay5pctSch'] = {'mode':'constant','factor': 0.0018912937825319638}
globalXSBRMap['TprimeRun2']['TprimeM2200Decay5pctTch'] = {'mode':'constant','factor': 5.621994001024363e-05}
globalXSBRMap['TprimeRun2']['TprimeM2200Decay5pctInt'] = {'mode':'constant','factor': -9.118748002568052e-05}

globalXSBRMap['TprimeRun2']['TprimeM2200Decay10pctSch'] = {'mode':'constant','factor': 0.0012031378486271579}
globalXSBRMap['TprimeRun2']['TprimeM2200Decay10pctTch'] = {'mode':'constant','factor': 5.6051306133886154e-05}
globalXSBRMap['TprimeRun2']['TprimeM2200Decay10pctInt'] = {'mode':'constant','factor': -9.259458829856457e-05}

globalXSBRMap['TprimeRun2']['TprimeM2200Decay20pctSch'] = {'mode':'constant','factor': 0.0008536765694679597}
globalXSBRMap['TprimeRun2']['TprimeM2200Decay20pctTch'] = {'mode':'constant','factor': 5.5532432668170954e-05}
globalXSBRMap['TprimeRun2']['TprimeM2200Decay20pctInt'] = {'mode':'constant','factor': -8.828746419498058e-05}

globalXSBRMap['TprimeRun2']['TprimeM2200Decay30pctSch'] = {'mode':'constant','factor': 0.0007095594643655585}
globalXSBRMap['TprimeRun2']['TprimeM2200Decay30pctTch'] = {'mode':'constant','factor': 5.497464369252696e-05}
globalXSBRMap['TprimeRun2']['TprimeM2200Decay30pctInt'] = {'mode':'constant','factor': -8.559336664811716e-05}

globalXSBRMap['TprimeRun2']['TprimeM2400Decay5pctSch'] = {'mode':'constant','factor': 0.0013010752152809051}
globalXSBRMap['TprimeRun2']['TprimeM2400Decay5pctTch'] = {'mode':'constant','factor': 4.916326087651656e-05}
globalXSBRMap['TprimeRun2']['TprimeM2400Decay5pctInt'] = {'mode':'constant','factor': -8.188683753905683e-05}

globalXSBRMap['TprimeRun2']['TprimeM2400Decay10pctSch'] = {'mode':'constant','factor': 0.0008807877080515798}
globalXSBRMap['TprimeRun2']['TprimeM2400Decay10pctTch'] = {'mode':'constant','factor': 4.9046514346730644e-05}
globalXSBRMap['TprimeRun2']['TprimeM2400Decay10pctInt'] = {'mode':'constant','factor': -8.207559596590707e-05}

globalXSBRMap['TprimeRun2']['TprimeM2400Decay20pctSch'] = {'mode':'constant','factor': 0.0006459974648154444}
globalXSBRMap['TprimeRun2']['TprimeM2400Decay20pctTch'] = {'mode':'constant','factor': 4.850169720772966e-05}
globalXSBRMap['TprimeRun2']['TprimeM2400Decay20pctInt'] = {'mode':'constant','factor': -8.023949126836329e-05}

globalXSBRMap['TprimeRun2']['TprimeM2400Decay30pctSch'] = {'mode':'constant','factor': 0.0005559729185138543}
globalXSBRMap['TprimeRun2']['TprimeM2400Decay30pctTch'] = {'mode':'constant','factor': 4.78012180290142e-05}
globalXSBRMap['TprimeRun2']['TprimeM2400Decay30pctInt'] = {'mode':'constant','factor': -7.586372773683374e-05}

globalXSBRMap['TprimeRun2']['TprimeM2600Decay5pctSch'] = {'mode':'constant','factor': 0.0009226867404080836}
globalXSBRMap['TprimeRun2']['TprimeM2600Decay5pctTch'] = {'mode':'constant','factor': 4.3170272347505904e-05}
globalXSBRMap['TprimeRun2']['TprimeM2600Decay5pctInt'] = {'mode':'constant','factor': -7.483413631765013e-05}

globalXSBRMap['TprimeRun2']['TprimeM2600Decay10pctSch'] = {'mode':'constant','factor': 0.0006581909912597519}
globalXSBRMap['TprimeRun2']['TprimeM2600Decay10pctTch'] = {'mode':'constant','factor': 4.3053525817719995e-05}
globalXSBRMap['TprimeRun2']['TprimeM2600Decay10pctInt'] = {'mode':'constant','factor': -7.332406890284773e-05}

globalXSBRMap['TprimeRun2']['TprimeM2600Decay20pctSch'] = {'mode':'constant','factor': 0.0005040855719423326}
globalXSBRMap['TprimeRun2']['TprimeM2600Decay20pctTch'] = {'mode':'constant','factor': 4.253465235200479e-05}
globalXSBRMap['TprimeRun2']['TprimeM2600Decay20pctInt'] = {'mode':'constant','factor': -7.277495347928337e-05}

globalXSBRMap['TprimeRun2']['TprimeM2600Decay30pctSch'] = {'mode':'constant','factor': 0.0004433773764536524}
globalXSBRMap['TprimeRun2']['TprimeM2600Decay30pctTch'] = {'mode':'constant','factor': 4.192497602978946e-05}
globalXSBRMap['TprimeRun2']['TprimeM2600Decay30pctInt'] = {'mode':'constant','factor': -7.102464806667146e-05}


globalXSBRMap['TprimeRun3']['TprimeM700Decay5pctSch'] = {'mode':'constant','factor': 0.10761435678933588}
globalXSBRMap['TprimeRun3']['TprimeM700Decay5pctTch'] = {'mode':'constant','factor': 0.0002695547654390547}
globalXSBRMap['TprimeRun3']['TprimeM700Decay5pctInt'] = {'mode':'constant','factor': -0.00015426711430765325}

globalXSBRMap['TprimeRun3']['TprimeM700Decay10pctSch'] = {'mode':'constant','factor': 0.05287320615638055}
globalXSBRMap['TprimeRun3']['TprimeM700Decay10pctTch'] = {'mode':'constant','factor': 0.00026384715731618747}
globalXSBRMap['TprimeRun3']['TprimeM700Decay10pctInt'] = {'mode':'constant','factor': -0.00011855745191897396}

globalXSBRMap['TprimeRun3']['TprimeM700Decay20pctSch'] = {'mode':'constant','factor': 0.026203110018618435}
globalXSBRMap['TprimeRun3']['TprimeM700Decay20pctTch'] = {'mode':'constant','factor': 0.0002709816674697716}
globalXSBRMap['TprimeRun3']['TprimeM700Decay20pctInt'] = {'mode':'constant','factor': -0.00010210114906902521}

globalXSBRMap['TprimeRun3']['TprimeM700Decay30pctSch'] = {'mode':'constant','factor': 0.016928246818958936}
globalXSBRMap['TprimeRun3']['TprimeM700Decay30pctTch'] = {'mode':'constant','factor': 0.0002563234920633167}
globalXSBRMap['TprimeRun3']['TprimeM700Decay30pctInt'] = {'mode':'constant','factor': -8.736083191771557e-05}

globalXSBRMap['TprimeRun3']['TprimeM800Decay5pctSch'] = {'mode':'constant','factor': 0.07510693416227758}
globalXSBRMap['TprimeRun3']['TprimeM800Decay5pctTch'] = {'mode':'constant','factor': 0.0002371251738318539}
globalXSBRMap['TprimeRun3']['TprimeM800Decay5pctInt'] = {'mode':'constant','factor': -0.00024229718064783807}

globalXSBRMap['TprimeRun3']['TprimeM800Decay10pctSch'] = {'mode':'constant','factor': 0.03825394625985432}
globalXSBRMap['TprimeRun3']['TprimeM800Decay10pctTch'] = {'mode':'constant','factor': 0.00023608742690042325}
globalXSBRMap['TprimeRun3']['TprimeM800Decay10pctInt'] = {'mode':'constant','factor': -0.00022119055655457748}

globalXSBRMap['TprimeRun3']['TprimeM800Decay20pctSch'] = {'mode':'constant','factor': 0.0190037406818198}
globalXSBRMap['TprimeRun3']['TprimeM800Decay20pctTch'] = {'mode':'constant','factor': 0.00023491996160256417}
globalXSBRMap['TprimeRun3']['TprimeM800Decay20pctInt'] = {'mode':'constant','factor': -0.0001889300254201627}

globalXSBRMap['TprimeRun3']['TprimeM800Decay30pctSch'] = {'mode':'constant','factor': 0.012818768970494426}
globalXSBRMap['TprimeRun3']['TprimeM800Decay30pctTch'] = {'mode':'constant','factor': 0.0002229858718911142}
globalXSBRMap['TprimeRun3']['TprimeM800Decay30pctInt'] = {'mode':'constant','factor': -0.00015684109285561186}

globalXSBRMap['TprimeRun3']['TprimeM900Decay5pctSch'] = {'mode':'constant','factor': 0.054455770226811966}
globalXSBRMap['TprimeRun3']['TprimeM900Decay5pctTch'] = {'mode':'constant','factor': 0.0002022309332625055}
globalXSBRMap['TprimeRun3']['TprimeM900Decay5pctInt'] = {'mode':'constant','factor': -0.0002779896831795309}

globalXSBRMap['TprimeRun3']['TprimeM900Decay10pctSch'] = {'mode':'constant','factor': 0.028317519391407933}
globalXSBRMap['TprimeRun3']['TprimeM900Decay10pctTch'] = {'mode':'constant','factor': 0.00021792685560039082}
globalXSBRMap['TprimeRun3']['TprimeM900Decay10pctInt'] = {'mode':'constant','factor': -0.00025516707338763114}

globalXSBRMap['TprimeRun3']['TprimeM900Decay20pctSch'] = {'mode':'constant','factor': 0.014152273777382528}
globalXSBRMap['TprimeRun3']['TprimeM900Decay20pctTch'] = {'mode':'constant','factor': 0.00021805657396681952}
globalXSBRMap['TprimeRun3']['TprimeM900Decay20pctInt'] = {'mode':'constant','factor': -0.00022445092938199157}

globalXSBRMap['TprimeRun3']['TprimeM900Decay30pctSch'] = {'mode':'constant','factor': 0.009737957767810324}
globalXSBRMap['TprimeRun3']['TprimeM900Decay30pctTch'] = {'mode':'constant','factor': 0.00021559192500467242}
globalXSBRMap['TprimeRun3']['TprimeM900Decay30pctInt'] = {'mode':'constant','factor': -0.0001959655667845829}

globalXSBRMap['TprimeRun3']['TprimeM1000Decay5pctSch'] = {'mode':'constant','factor': 0.03970679196385693}
globalXSBRMap['TprimeRun3']['TprimeM1000Decay5pctTch'] = {'mode':'constant','factor': 0.00020586304752251194}
globalXSBRMap['TprimeRun3']['TprimeM1000Decay5pctInt'] = {'mode':'constant','factor': -0.0002850252245439511}

globalXSBRMap['TprimeRun3']['TprimeM1000Decay10pctSch'] = {'mode':'constant','factor': 0.020780882301894413}
globalXSBRMap['TprimeRun3']['TprimeM1000Decay10pctTch'] = {'mode':'constant','factor': 0.0002036578352932224}
globalXSBRMap['TprimeRun3']['TprimeM1000Decay10pctInt'] = {'mode':'constant','factor': -0.00026735057184796874}

globalXSBRMap['TprimeRun3']['TprimeM1000Decay20pctSch'] = {'mode':'constant','factor': 0.011214152777770114}
globalXSBRMap['TprimeRun3']['TprimeM1000Decay20pctTch'] = {'mode':'constant','factor': 0.00019185346394820117}
globalXSBRMap['TprimeRun3']['TprimeM1000Decay20pctInt'] = {'mode':'constant','factor': -0.00023526163928341788}

globalXSBRMap['TprimeRun3']['TprimeM1000Decay30pctSch'] = {'mode':'constant','factor': 0.007466589171641965}
globalXSBRMap['TprimeRun3']['TprimeM1000Decay30pctTch'] = {'mode':'constant','factor': 0.00018809163132176582}
globalXSBRMap['TprimeRun3']['TprimeM1000Decay30pctInt'] = {'mode':'constant','factor': -0.00021037984665315114}

globalXSBRMap['TprimeRun3']['TprimeM1100Decay5pctSch'] = {'mode':'constant','factor': 0.029575787545767333}
globalXSBRMap['TprimeRun3']['TprimeM1100Decay5pctTch'] = {'mode':'constant','factor': 0.00016863387635744533}
globalXSBRMap['TprimeRun3']['TprimeM1100Decay5pctInt'] = {'mode':'constant','factor': -0.00026975295182606334}

globalXSBRMap['TprimeRun3']['TprimeM1100Decay10pctSch'] = {'mode':'constant','factor': 0.015644034991313775}
globalXSBRMap['TprimeRun3']['TprimeM1100Decay10pctTch'] = {'mode':'constant','factor': 0.0001685041579910164}
globalXSBRMap['TprimeRun3']['TprimeM1100Decay10pctInt'] = {'mode':'constant','factor': -0.00025705465765613424}

globalXSBRMap['TprimeRun3']['TprimeM1100Decay20pctSch'] = {'mode':'constant','factor': 0.008510822021393838}
globalXSBRMap['TprimeRun3']['TprimeM1100Decay20pctTch'] = {'mode':'constant','factor': 0.00016824472125815884}
globalXSBRMap['TprimeRun3']['TprimeM1100Decay20pctInt'] = {'mode':'constant','factor': -0.00023182966788613962}

globalXSBRMap['TprimeRun3']['TprimeM1100Decay30pctSch'] = {'mode':'constant','factor': 0.005859378611589082}
globalXSBRMap['TprimeRun3']['TprimeM1100Decay30pctTch'] = {'mode':'constant','factor': 0.0001673366926931571}
globalXSBRMap['TprimeRun3']['TprimeM1100Decay30pctInt'] = {'mode':'constant','factor': -0.00020660467811614526}

globalXSBRMap['TprimeRun3']['TprimeM1200Decay5pctSch'] = {'mode':'constant','factor': 0.022778545144898}
globalXSBRMap['TprimeRun3']['TprimeM1200Decay5pctTch'] = {'mode':'constant','factor': 0.00015384598258456151}
globalXSBRMap['TprimeRun3']['TprimeM1200Decay5pctInt'] = {'mode':'constant','factor': -0.0002539658833985838}

globalXSBRMap['TprimeRun3']['TprimeM1200Decay10pctSch'] = {'mode':'constant','factor': 0.011909443221828506}
globalXSBRMap['TprimeRun3']['TprimeM1200Decay10pctTch'] = {'mode':'constant','factor': 0.0001524190805538448}
globalXSBRMap['TprimeRun3']['TprimeM1200Decay10pctInt'] = {'mode':'constant','factor': -0.0002434983706368854}

globalXSBRMap['TprimeRun3']['TprimeM1200Decay20pctSch'] = {'mode':'constant','factor': 0.006632500075504755}
globalXSBRMap['TprimeRun3']['TprimeM1200Decay20pctTch'] = {'mode':'constant','factor': 0.00015202992545455831}
globalXSBRMap['TprimeRun3']['TprimeM1200Decay20pctInt'] = {'mode':'constant','factor': -0.0002208473594148496}

globalXSBRMap['TprimeRun3']['TprimeM1200Decay30pctSch'] = {'mode':'constant','factor': 0.004634837232501172}
globalXSBRMap['TprimeRun3']['TprimeM1200Decay30pctTch'] = {'mode':'constant','factor': 0.00015202992545455831}
globalXSBRMap['TprimeRun3']['TprimeM1200Decay30pctInt'] = {'mode':'constant','factor': -0.00020248631243941151}

globalXSBRMap['TprimeRun3']['TprimeM1400Decay5pctSch'] = {'mode':'constant','factor': 0.01356854112845291}
globalXSBRMap['TprimeRun3']['TprimeM1400Decay5pctTch'] = {'mode':'constant','factor': 0.00012724074563001388}
globalXSBRMap['TprimeRun3']['TprimeM1400Decay5pctInt'] = {'mode':'constant','factor': -0.0002144982123298849}

globalXSBRMap['TprimeRun3']['TprimeM1400Decay10pctSch'] = {'mode':'constant','factor': 0.007246067948712996}
globalXSBRMap['TprimeRun3']['TprimeM1400Decay10pctTch'] = {'mode':'constant','factor': 0.00012676078767422723}
globalXSBRMap['TprimeRun3']['TprimeM1400Decay10pctInt'] = {'mode':'constant','factor': -0.00021089464236274296}

globalXSBRMap['TprimeRun3']['TprimeM1400Decay20pctSch'] = {'mode':'constant','factor': 0.004313135683757737}
globalXSBRMap['TprimeRun3']['TprimeM1400Decay20pctTch'] = {'mode':'constant','factor': 0.00012708508359029919}
globalXSBRMap['TprimeRun3']['TprimeM1400Decay20pctInt'] = {'mode':'constant','factor': -0.0001939063839462159}

globalXSBRMap['TprimeRun3']['TprimeM1400Decay30pctSch'] = {'mode':'constant','factor': 0.0030756224680269454}
globalXSBRMap['TprimeRun3']['TprimeM1400Decay30pctTch'] = {'mode':'constant','factor': 0.0001246723219747234}
globalXSBRMap['TprimeRun3']['TprimeM1400Decay30pctInt'] = {'mode':'constant','factor': -0.0001782909140886003}

globalXSBRMap['TprimeRun3']['TprimeM1600Decay5pctSch'] = {'mode':'constant','factor': 0.008228035982579044}
globalXSBRMap['TprimeRun3']['TprimeM1600Decay5pctTch'] = {'mode':'constant','factor': 0.00010448814415840171}
globalXSBRMap['TprimeRun3']['TprimeM1600Decay5pctInt'] = {'mode':'constant','factor': -0.00018309567404478983}

globalXSBRMap['TprimeRun3']['TprimeM1600Decay10pctSch'] = {'mode':'constant','factor': 0.004621865395858291}
globalXSBRMap['TprimeRun3']['TprimeM1600Decay10pctTch'] = {'mode':'constant','factor': 0.00010337256620711394}
globalXSBRMap['TprimeRun3']['TprimeM1600Decay10pctInt'] = {'mode':'constant','factor': -0.00017966370264751156}

globalXSBRMap['TprimeRun3']['TprimeM1600Decay20pctSch'] = {'mode':'constant','factor': 0.0029108801426623644}
globalXSBRMap['TprimeRun3']['TprimeM1600Decay20pctTch'] = {'mode':'constant','factor': 0.00010267208702839826}
globalXSBRMap['TprimeRun3']['TprimeM1600Decay20pctInt'] = {'mode':'constant','factor': -0.0001662790141981269}

globalXSBRMap['TprimeRun3']['TprimeM1600Decay30pctSch'] = {'mode':'constant','factor': 0.002149433331725284}
globalXSBRMap['TprimeRun3']['TprimeM1600Decay30pctTch'] = {'mode':'constant','factor': 0.00010176405846339676}
globalXSBRMap['TprimeRun3']['TprimeM1600Decay30pctInt'] = {'mode':'constant','factor': -0.00015778488498986338}

globalXSBRMap['TprimeRun3']['TprimeM1800Decay5pctSch'] = {'mode':'constant','factor': 0.00517706000417357}
globalXSBRMap['TprimeRun3']['TprimeM1800Decay5pctTch'] = {'mode':'constant','factor': 8.945378548930329e-05}
globalXSBRMap['TprimeRun3']['TprimeM1800Decay5pctInt'] = {'mode':'constant','factor': -0.00015754464699205387}

globalXSBRMap['TprimeRun3']['TprimeM1800Decay10pctSch'] = {'mode':'constant','factor': 0.0030470844274126086}
globalXSBRMap['TprimeRun3']['TprimeM1800Decay10pctTch'] = {'mode':'constant','factor': 8.980402507866101e-05}
globalXSBRMap['TprimeRun3']['TprimeM1800Decay10pctInt'] = {'mode':'constant','factor': -0.00015486770930217694}

globalXSBRMap['TprimeRun3']['TprimeM1800Decay20pctSch'] = {'mode':'constant','factor': 0.0019237233741391648}
globalXSBRMap['TprimeRun3']['TprimeM1800Decay20pctTch'] = {'mode':'constant','factor': 8.732640427987089e-05}
globalXSBRMap['TprimeRun3']['TprimeM1800Decay20pctInt'] = {'mode':'constant','factor': -0.00014649369909281826}

globalXSBRMap['TprimeRun3']['TprimeM1800Decay30pctSch'] = {'mode':'constant','factor': 0.0015202992545455842}
globalXSBRMap['TprimeRun3']['TprimeM1800Decay30pctTch'] = {'mode':'constant','factor': 8.525091041700983e-05}
globalXSBRMap['TprimeRun3']['TprimeM1800Decay30pctInt'] = {'mode':'constant','factor': -0.00013921791973058856}

globalXSBRMap['TprimeRun3']['TprimeM2000Decay5pctSch'] = {'mode':'constant','factor': 0.00341029585341326}
globalXSBRMap['TprimeRun3']['TprimeM2000Decay5pctTch'] = {'mode':'constant','factor': 7.478263824620536e-05}
globalXSBRMap['TprimeRun3']['TprimeM2000Decay5pctInt'] = {'mode':'constant','factor': -0.00013585458776125588}

globalXSBRMap['TprimeRun3']['TprimeM2000Decay10pctSch'] = {'mode':'constant','factor': 0.0020638192098822727}
globalXSBRMap['TprimeRun3']['TprimeM2000Decay10pctTch'] = {'mode':'constant','factor': 7.475669457291959e-05}
globalXSBRMap['TprimeRun3']['TprimeM2000Decay10pctInt'] = {'mode':'constant','factor': -0.0001350137547689227}

globalXSBRMap['TprimeRun3']['TprimeM2000Decay20pctSch'] = {'mode':'constant','factor': 0.0013698259494881715}
globalXSBRMap['TprimeRun3']['TprimeM2000Decay20pctTch'] = {'mode':'constant','factor': 7.426376478049016e-05}
globalXSBRMap['TprimeRun3']['TprimeM2000Decay20pctInt'] = {'mode':'constant','factor': -0.00012808117254642089}

globalXSBRMap['TprimeRun3']['TprimeM2000Decay30pctSch'] = {'mode':'constant','factor': 0.001109740624798419}
globalXSBRMap['TprimeRun3']['TprimeM2000Decay30pctTch'] = {'mode':'constant','factor': 7.31481868292024e-05}
globalXSBRMap['TprimeRun3']['TprimeM2000Decay30pctInt'] = {'mode':'constant','factor': -0.000122727297166667}

globalXSBRMap['TprimeRun3']['TprimeM2200Decay5pctSch'] = {'mode':'constant','factor': 0.0023115812897612892}
globalXSBRMap['TprimeRun3']['TprimeM2200Decay5pctTch'] = {'mode':'constant','factor': 6.440516893190102e-05}
globalXSBRMap['TprimeRun3']['TprimeM2200Decay5pctInt'] = {'mode':'constant','factor': -0.00012315629359132673}

globalXSBRMap['TprimeRun3']['TprimeM2200Decay10pctSch'] = {'mode':'constant','factor': 0.0014411710510240136}
globalXSBRMap['TprimeRun3']['TprimeM2200Decay10pctTch'] = {'mode':'constant','factor': 6.441814076854403e-05}
globalXSBRMap['TprimeRun3']['TprimeM2200Decay10pctInt'] = {'mode':'constant','factor': -0.00012180066488940176}

globalXSBRMap['TprimeRun3']['TprimeM2200Decay20pctSch'] = {'mode':'constant','factor': 0.0010539617272340332}
globalXSBRMap['TprimeRun3']['TprimeM2200Decay20pctTch'] = {'mode':'constant','factor': 6.404195750590051e-05}
globalXSBRMap['TprimeRun3']['TprimeM2200Decay20pctInt'] = {'mode':'constant','factor': -0.00011653258879457974}

globalXSBRMap['TprimeRun3']['TprimeM2200Decay30pctSch'] = {'mode':'constant','factor': 0.0008412236062907946}
globalXSBRMap['TprimeRun3']['TprimeM2200Decay30pctTch'] = {'mode':'constant','factor': 6.280963302482684e-05}
globalXSBRMap['TprimeRun3']['TprimeM2200Decay30pctInt'] = {'mode':'constant','factor': -0.00011090415570304359}

globalXSBRMap['TprimeRun3']['TprimeM2400Decay5pctSch'] = {'mode':'constant','factor': 0.0015968330907385787}
globalXSBRMap['TprimeRun3']['TprimeM2400Decay5pctTch'] = {'mode':'constant','factor': 5.664801061945871e-05}
globalXSBRMap['TprimeRun3']['TprimeM2400Decay5pctInt'] = {'mode':'constant','factor': -0.00010630531403069104}

globalXSBRMap['TprimeRun3']['TprimeM2400Decay10pctSch'] = {'mode':'constant','factor': 0.0010552589108983213}
globalXSBRMap['TprimeRun3']['TprimeM2400Decay10pctTch'] = {'mode':'constant','factor': 5.636263021331533e-05}
globalXSBRMap['TprimeRun3']['TprimeM2400Decay10pctInt'] = {'mode':'constant','factor': -0.00010733490544987443}

globalXSBRMap['TprimeRun3']['TprimeM2400Decay20pctSch'] = {'mode':'constant','factor': 0.000765338361929944}
globalXSBRMap['TprimeRun3']['TprimeM2400Decay20pctTch'] = {'mode':'constant','factor': 5.57140383811712e-05}
globalXSBRMap['TprimeRun3']['TprimeM2400Decay20pctInt'] = {'mode':'constant','factor': -0.00010191239064217499}

globalXSBRMap['TprimeRun3']['TprimeM2400Decay30pctSch'] = {'mode':'constant','factor': 0.0006596178932904689}
globalXSBRMap['TprimeRun3']['TprimeM2400Decay30pctTch'] = {'mode':'constant','factor': 5.4572516756597886e-05}
globalXSBRMap['TprimeRun3']['TprimeM2400Decay30pctInt'] = {'mode':'constant','factor': -9.736502854078127e-05}

globalXSBRMap['TprimeRun3']['TprimeM2600Decay5pctSch'] = {'mode':'constant','factor': 0.0011293280981291686}
globalXSBRMap['TprimeRun3']['TprimeM2600Decay5pctTch'] = {'mode':'constant','factor': 4.9046514346730644e-05}
globalXSBRMap['TprimeRun3']['TprimeM2600Decay5pctInt'] = {'mode':'constant','factor': -9.844609953092396e-05}

globalXSBRMap['TprimeRun3']['TprimeM2600Decay10pctSch'] = {'mode':'constant','factor': 0.0007863527372914105}
globalXSBRMap['TprimeRun3']['TprimeM2600Decay10pctTch'] = {'mode':'constant','factor': 4.9007598836802086e-05}
globalXSBRMap['TprimeRun3']['TprimeM2600Decay10pctInt'] = {'mode':'constant','factor': -9.489400913474106e-05}

globalXSBRMap['TprimeRun3']['TprimeM2600Decay20pctSch'] = {'mode':'constant','factor': 0.000592553497846777}
globalXSBRMap['TprimeRun3']['TprimeM2600Decay20pctTch'] = {'mode':'constant','factor': 4.851466904437267e-05}
globalXSBRMap['TprimeRun3']['TprimeM2600Decay20pctInt'] = {'mode':'constant','factor': -9.362417971774818e-05}

globalXSBRMap['TprimeRun3']['TprimeM2600Decay30pctSch'] = {'mode':'constant','factor': 0.0005138144494244931}
globalXSBRMap['TprimeRun3']['TprimeM2600Decay30pctTch'] = {'mode':'constant','factor': 4.777527435572842e-05}
globalXSBRMap['TprimeRun3']['TprimeM2600Decay30pctInt'] = {'mode':'constant','factor': -8.971173232485092e-05}

