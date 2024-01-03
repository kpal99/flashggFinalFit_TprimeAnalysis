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

#Tprime Analysis
globalXSBRMap['TprimeM700Decay10pctSch'] = od()
globalXSBRMap['TprimeM700Decay10pctSch']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM700Decay10pctSch']['TprimeM700Decay10pctSch'] = {'mode':'constant','factor':0.003583}

globalXSBRMap['TprimeM700Decay30pctSch'] = od()
globalXSBRMap['TprimeM700Decay30pctSch']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM700Decay30pctSch']['TprimeM700Decay30pctSch'] = {'mode':'constant','factor':0.001175}

globalXSBRMap['TprimeM1000Decay10pctSch'] = od()
globalXSBRMap['TprimeM1000Decay10pctSch']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1000Decay10pctSch']['TprimeM1000Decay10pctSch'] = {'mode':'constant','factor':0.001369}

globalXSBRMap['TprimeM1000Decay30pctSch'] = od()
globalXSBRMap['TprimeM1000Decay30pctSch']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1000Decay30pctSch']['TprimeM1000Decay30pctSch'] = {'mode':'constant','factor':0.0005049}

globalXSBRMap['TprimeM1400Decay10pctSch'] = od()
globalXSBRMap['TprimeM1400Decay10pctSch']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1400Decay10pctSch']['TprimeM1400Decay10pctSch'] = {'mode':'constant','factor':0.0004833}

globalXSBRMap['TprimeM1400Decay30pctSch'] = od()
globalXSBRMap['TprimeM1400Decay30pctSch']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM1400Decay30pctSch']['TprimeM1400Decay30pctSch'] = {'mode':'constant','factor':0.0002052}

globalXSBRMap['TprimeM2000Decay10pctSch'] = od()
globalXSBRMap['TprimeM2000Decay10pctSch']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM2000Decay10pctSch']['TprimeM2000Decay10pctSch'] = {'mode':'constant','factor':0.0001338}

globalXSBRMap['TprimeM2000Decay30pctSch'] = od()
globalXSBRMap['TprimeM2000Decay30pctSch']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM2000Decay30pctSch']['TprimeM2000Decay30pctSch'] = {'mode':'constant','factor':0.0000748}

globalXSBRMap['TprimeM2400Decay10pctSch'] = od()
globalXSBRMap['TprimeM2400Decay10pctSch']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM2400Decay10pctSch']['TprimeM2400Decay10pctSch'] = {'mode':'constant','factor':0.00006816}

globalXSBRMap['TprimeM2400Decay30pctSch'] = od()
globalXSBRMap['TprimeM2400Decay30pctSch']['decay'] = {'mode':'hgg'}
globalXSBRMap['TprimeM2400Decay30pctSch']['TprimeM2400Decay30pctSch'] = {'mode':'constant','factor':0.00004314}

globalXSBRMap['Tprime_600'] = od()
globalXSBRMap['Tprime_600']['decay'] = {'mode':'hgg'}
globalXSBRMap['Tprime_600']['Tprime600'] = {'mode':'constant','factor':0.1764}
globalXSBRMap['Tprime_600']['THQ'] = {'mode':'tHq'}
globalXSBRMap['Tprime_600']['TTH'] = {'mode':'ttH'}
globalXSBRMap['Tprime_600']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['Tprime_600']['VBF'] = {'mode':'qqH'}
globalXSBRMap['Tprime_600']['VH'] = {'mode':'constant','factor':2.257}

globalXSBRMap['Tprime_625'] = od()
globalXSBRMap['Tprime_625']['decay'] = {'mode':'hgg'}
globalXSBRMap['Tprime_625']['Tprime625'] = {'mode':'constant','factor':0.1489}
globalXSBRMap['Tprime_625']['THQ'] = {'mode':'tHq'}
#globalXSBRMap['Tprime_625']['TTH'] = {'mode':'ttH','factor':0.5}
globalXSBRMap['Tprime_625']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['Tprime_625']['TTH'] = {'mode':'ttH'}
globalXSBRMap['Tprime_625']['VBF'] = {'mode':'qqH'}
globalXSBRMap['Tprime_625']['VH'] = {'mode':'constant','factor':2.257}

globalXSBRMap['Tprime_650'] = od()
globalXSBRMap['Tprime_650']['decay'] = {'mode':'hgg'}
globalXSBRMap['Tprime_650']['Tprime650'] = {'mode':'constant','factor':0.1213}
globalXSBRMap['Tprime_650']['THQ'] = {'mode':'tHq'}
globalXSBRMap['Tprime_650']['TTH'] = {'mode':'ttH'}
globalXSBRMap['Tprime_650']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['Tprime_650']['VBF'] = {'mode':'qqH'}
globalXSBRMap['Tprime_650']['VH'] = {'mode':'constant','factor':2.257}

globalXSBRMap['Tprime_675'] = od()
globalXSBRMap['Tprime_675']['decay'] = {'mode':'hgg'}
globalXSBRMap['Tprime_675']['Tprime675'] = {'mode':'constant','factor':0.1050}
globalXSBRMap['Tprime_675']['THQ'] = {'mode':'tHq'}
globalXSBRMap['Tprime_675']['TTH'] = {'mode':'ttH'}
globalXSBRMap['Tprime_675']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['Tprime_675']['VBF'] = {'mode':'qqH'}
globalXSBRMap['Tprime_675']['VH'] = {'mode':'constant','factor':2.257}

globalXSBRMap['Tprime_700'] = od()
globalXSBRMap['Tprime_700']['decay'] = {'mode':'hgg'}
globalXSBRMap['Tprime_700']['Tprime700'] = {'mode':'constant','factor':0.0886}
globalXSBRMap['Tprime_700']['THQ'] = {'mode':'tHq'}
globalXSBRMap['Tprime_700']['TTH'] = {'mode':'ttH'}
globalXSBRMap['Tprime_700']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['Tprime_700']['VBF'] = {'mode':'qqH'}
globalXSBRMap['Tprime_700']['VH'] = {'mode':'constant','factor':2.257}

globalXSBRMap['Tprime_800'] = od()
globalXSBRMap['Tprime_800']['decay'] = {'mode':'hgg'}
globalXSBRMap['Tprime_800']['Tprime800'] = {'mode':'constant','factor':0.0459}
globalXSBRMap['Tprime_800']['THQ'] = {'mode':'tHq'}
globalXSBRMap['Tprime_800']['TTH'] = {'mode':'ttH'}
globalXSBRMap['Tprime_800']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['Tprime_800']['VBF'] = {'mode':'qqH'}
globalXSBRMap['Tprime_800']['VH'] = {'mode':'constant','factor':2.257}

globalXSBRMap['Tprime_900'] = od()
globalXSBRMap['Tprime_900']['decay'] = {'mode':'hgg'}
globalXSBRMap['Tprime_900']['Tprime900'] = {'mode':'constant','factor':0.0251}
globalXSBRMap['Tprime_900']['THQ'] = {'mode':'tHq'}
globalXSBRMap['Tprime_900']['TTH'] = {'mode':'ttH'}
globalXSBRMap['Tprime_900']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['Tprime_900']['VBF'] = {'mode':'qqH'}
globalXSBRMap['Tprime_900']['VH'] = {'mode':'constant','factor':2.257}

globalXSBRMap['Tprime_1000'] = od()
globalXSBRMap['Tprime_1000']['decay'] = {'mode':'hgg'}
globalXSBRMap['Tprime_1000']['Tprime1000'] = {'mode':'constant','factor':0.0145}
globalXSBRMap['Tprime_1000']['THQ'] = {'mode':'tHq'}
globalXSBRMap['Tprime_1000']['TTH'] = {'mode':'ttH'}
globalXSBRMap['Tprime_1000']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['Tprime_1000']['VBF'] = {'mode':'qqH'}
globalXSBRMap['Tprime_1000']['VH'] = {'mode':'constant','factor':2.257}

globalXSBRMap['Tprime_1100'] = od()
globalXSBRMap['Tprime_1100']['decay'] = {'mode':'hgg'}
globalXSBRMap['Tprime_1100']['Tprime1100'] = {'mode':'constant','factor':0.00867}
globalXSBRMap['Tprime_1100']['THQ'] = {'mode':'tHq'}
globalXSBRMap['Tprime_1100']['TTH'] = {'mode':'ttH'}
globalXSBRMap['Tprime_1100']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['Tprime_1100']['VBF'] = {'mode':'qqH'}
globalXSBRMap['Tprime_1100']['VH'] = {'mode':'constant','factor':2.257}

globalXSBRMap['Tprime_1200'] = od()
globalXSBRMap['Tprime_1200']['decay'] = {'mode':'hgg'}
globalXSBRMap['Tprime_1200']['Tprime1200'] = {'mode':'constant','factor':0.00536}
globalXSBRMap['Tprime_1200']['THQ'] = {'mode':'tHq'}
globalXSBRMap['Tprime_1200']['TTH'] = {'mode':'ttH'}
globalXSBRMap['Tprime_1200']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['Tprime_1200']['VBF'] = {'mode':'qqH'}
globalXSBRMap['Tprime_1200']['VH'] = {'mode':'constant','factor':2.257}
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
