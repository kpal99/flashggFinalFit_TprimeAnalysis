# Python script to hold replacement model mapping for different analyses
from collections import OrderedDict as od

# Add analyses to globalReplacementMap. See "STXS" as an example
globalReplacementMap = od()

# Example analysis which with cats Untagged_Tag0,VBF_Tag0
globalReplacementMap['example'] = od()
# For WRONG VERTEX SCENARIO:
#  * single proc x cat for wrong vertex since for dZ > 1cm shape independent of proc x cat
#  * use proc x cat with highest number of WV events
globalReplacementMap['example']['procWV'] = "GG2H"
globalReplacementMap['example']['catWV'] = "Untagged_Tag0"
# For RIGHT VERTEX SCENARIO:
#  * default you should add is diagonal process from given category 
#  * if few events in diagonal process then may need to change the category aswell (see catRVMap)
#  * map must contain entry for all cats being processed (for replacement proc and cat)
globalReplacementMap['example']['procRVMap'] = od()
globalReplacementMap["example"]["procRVMap"]["Untagged_Tag0"] = "GG2H"
globalReplacementMap["example"]["procRVMap"]["VBF_Tag0"] = "VBF"
# Replacement category for RV fit
globalReplacementMap["example"]["catRVMap"] = od()
globalReplacementMap["example"]["catRVMap"]["Untagged_Tag0"] = "Untagged_Tag0"
globalReplacementMap["example"]["catRVMap"]["VBF_Tag0"] = "VBF_Tag0"

# Tutorial analysis
globalReplacementMap['tutorial'] = od()
# For WRONG VERTEX SCENARIO:
#  * single proc x cat for wrong vertex since for dZ > 1cm shape independent of proc x cat
#  * use proc x cat with highest number of WV events
globalReplacementMap['tutorial']['procWV'] = "GG2H"
globalReplacementMap['tutorial']['catWV'] = "EBEB_highR9highR9"
# For RIGHT VERTEX SCENARIO
#  * default mapping is to use diagonal process from given category 
#  * if few events in diagonal process then may need to change the category aswell (see catRVMap)
#  * map must contain entry for all cats being processed (for replacement proc and cat)
globalReplacementMap['tutorial']['procRVMap'] = od()
globalReplacementMap["tutorial"]["procRVMap"]["EBEB_highR9highR9"] = "GG2H"
globalReplacementMap["tutorial"]["procRVMap"]["EBEB_highR9lowR9"] = "GG2H"
globalReplacementMap["tutorial"]["procRVMap"]["EBEB_lowR9highR9"] = "GG2H"
globalReplacementMap["tutorial"]["procRVMap"]["EBEE_highR9highR9"] = "GG2H"
globalReplacementMap["tutorial"]["procRVMap"]["EBEE_highR9lowR9"] = "GG2H"
globalReplacementMap["tutorial"]["procRVMap"]["EBEE_lowR9highR9"] = "GG2H"
globalReplacementMap["tutorial"]["procRVMap"]["EEEB_highR9highR9"] = "GG2H"
globalReplacementMap["tutorial"]["procRVMap"]["EEEB_highR9lowR9"] = "GG2H"
globalReplacementMap["tutorial"]["procRVMap"]["EEEB_lowR9highR9"] = "GG2H"
globalReplacementMap["tutorial"]["procRVMap"]["EEEE_incl"] = "GG2H"
globalReplacementMap['tutorial']['catRVMap'] = od()
globalReplacementMap["tutorial"]["catRVMap"]["EBEB_highR9highR9"] = "EBEB_highR9highR9"
globalReplacementMap["tutorial"]["catRVMap"]["EBEB_highR9lowR9"] = "EBEB_highR9lowR9"
globalReplacementMap["tutorial"]["catRVMap"]["EBEB_lowR9highR9"] = "EBEB_lowR9highR9"
globalReplacementMap["tutorial"]["catRVMap"]["EBEE_highR9highR9"] = "EBEE_highR9highR9"
globalReplacementMap["tutorial"]["catRVMap"]["EBEE_highR9lowR9"] = "EBEE_highR9lowR9"
globalReplacementMap["tutorial"]["catRVMap"]["EBEE_lowR9highR9"] = "EBEE_lowR9highR9"
globalReplacementMap["tutorial"]["catRVMap"]["EEEB_highR9highR9"] = "EEEB_highR9highR9"
globalReplacementMap["tutorial"]["catRVMap"]["EEEB_highR9lowR9"] = "EEEB_highR9lowR9"
globalReplacementMap["tutorial"]["catRVMap"]["EEEB_lowR9highR9"] = "EEEB_lowR9highR9"
globalReplacementMap["tutorial"]["catRVMap"]["EEEE_incl"] = "EEEE_incl"


# STXS analysis
globalReplacementMap['STXS'] = od()
# For WRONG VERTEX SCENARIO:
#  * single proc x cat for wrong vertex since for dZ > 1cm shape independent of proc x cat
#  * use proc x cat with highest number of WV events
globalReplacementMap['STXS']['procWV'] = "GG2H_0J_PTH_GT10"
globalReplacementMap['STXS']['catWV'] = "RECO_0J_PTH_GT10_Tag1"
# For RIGHT VERTEX SCENARIO:
#  * default mapping is to use diagonal process from given category 
#  * if few events in diagonal process then may need to change the category aswell (see catRVMap)
#  * map must contain entry for all cats being processed (for replacement proc and cat)
globalReplacementMap['STXS']['procRVMap'] = od()
globalReplacementMap["STXS"]["procRVMap"]["RECO_0J_PTH_0_10_Tag0"] = "GG2H_0J_PTH_0_10"
globalReplacementMap["STXS"]["procRVMap"]["RECO_0J_PTH_0_10_Tag1"] = "GG2H_0J_PTH_0_10"
globalReplacementMap["STXS"]["procRVMap"]["RECO_0J_PTH_0_10_Tag2"] = "GG2H_0J_PTH_0_10"
globalReplacementMap["STXS"]["procRVMap"]["RECO_0J_PTH_GT10_Tag0"] = "GG2H_0J_PTH_GT10"
globalReplacementMap["STXS"]["procRVMap"]["RECO_0J_PTH_GT10_Tag1"] = "GG2H_0J_PTH_GT10"
globalReplacementMap["STXS"]["procRVMap"]["RECO_0J_PTH_GT10_Tag2"] = "GG2H_0J_PTH_GT10"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_0_60_Tag0"] = "GG2H_1J_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_0_60_Tag1"] = "GG2H_1J_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_0_60_Tag2"] = "GG2H_1J_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_120_200_Tag0"] = "GG2H_1J_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_120_200_Tag1"] = "GG2H_1J_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_120_200_Tag2"] = "GG2H_1J_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_60_120_Tag0"] = "GG2H_1J_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_60_120_Tag1"] = "GG2H_1J_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_60_120_Tag2"] = "GG2H_1J_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_0_60_Tag0"] = "GG2H_GE2J_MJJ_0_350_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_0_60_Tag1"] = "GG2H_GE2J_MJJ_0_350_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_0_60_Tag2"] = "GG2H_GE2J_MJJ_0_350_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_120_200_Tag0"] = "GG2H_GE2J_MJJ_0_350_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_120_200_Tag1"] = "GG2H_GE2J_MJJ_0_350_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_120_200_Tag2"] = "GG2H_GE2J_MJJ_0_350_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_60_120_Tag0"] = "GG2H_GE2J_MJJ_0_350_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_60_120_Tag1"] = "GG2H_GE2J_MJJ_0_350_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_60_120_Tag2"] = "GG2H_GE2J_MJJ_0_350_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_PTH_200_300_Tag0"] = "GG2H_PTH_200_300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_PTH_200_300_Tag1"] = "GG2H_PTH_200_300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_PTH_300_450_Tag0"] = "GG2H_PTH_300_450"
globalReplacementMap["STXS"]["procRVMap"]["RECO_PTH_300_450_Tag1"] = "GG2H_PTH_300_450"
globalReplacementMap["STXS"]["procRVMap"]["RECO_PTH_450_650_Tag0"] = "GG2H_PTH_450_650"
globalReplacementMap["STXS"]["procRVMap"]["RECO_PTH_GT650_Tag0"] = "GG2H_PTH_GT650"
globalReplacementMap["STXS"]["procRVMap"]["RECO_THQ_LEP"] = "THQ"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag0"] = "TTH_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag1"] = "TTH_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag2"] = "TTH_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag3"] = "TTH_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag0"] = "TTH_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag1"] = "TTH_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag2"] = "TTH_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag3"] = "TTH_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_200_300_Tag0"] = "TTH_PTH_200_300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_200_300_Tag1"] = "TTH_PTH_200_300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_200_300_Tag2"] = "TTH_PTH_200_300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag0"] = "TTH_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag1"] = "TTH_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag2"] = "TTH_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag3"] = "TTH_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_GT300_Tag0"] = "TTH_PTH_GT300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_GT300_Tag1"] = "TTH_PTH_GT300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_GT300_Tag2"] = "TTH_PTH_GT300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag0"] = "TTH_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag1"] = "TTH_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag2"] = "TTH_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_120_200_Tag0"] = "TTH_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_120_200_Tag1"] = "TTH_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_200_300_Tag0"] = "TTH_PTH_200_300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_200_300_Tag1"] = "TTH_PTH_200_300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_60_120_Tag0"] = "TTH_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_60_120_Tag1"] = "TTH_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_60_120_Tag2"] = "TTH_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_GT300_Tag0"] = "TTH_PTH_GT300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFLIKEGGH_Tag0"] = "GG2H_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFLIKEGGH_Tag1"] = "GG2H_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_BSM_Tag0"] = "VBF_GE2J_MJJ_GT350_PTH_GT200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_BSM_Tag1"] = "VBF_GE2J_MJJ_GT350_PTH_GT200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag0"] = "VBF_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag1"] = "VBF_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag0"] = "VBF_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag1"] = "VBF_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3_HIGHMJJ_Tag0"] = "VBF_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3_HIGHMJJ_Tag1"] = "VBF_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3_LOWMJJ_Tag0"] = "GG2H_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3_LOWMJJ_Tag1"] = "GG2H_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_VHHAD_Tag0"] = "WH2HQQ_GE2J_MJJ_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_VHHAD_Tag1"] = "GG2H_GE2J_MJJ_0_350_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VH_MET_Tag0"] = "QQ2HLL_PTV_150_250_0J"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VH_MET_Tag1"] = "QQ2HLL_PTV_75_150"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VH_MET_Tag2"] = "QQ2HLL_PTV_75_150"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_PTV_0_75_Tag0"] = "QQ2HLNU_PTV_0_75"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_PTV_0_75_Tag1"] = "QQ2HLNU_PTV_0_75"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_PTV_75_150_Tag0"] = "QQ2HLNU_PTV_75_150"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_PTV_75_150_Tag1"] = "QQ2HLNU_PTV_75_150"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_PTV_GT150_Tag0"] = "QQ2HLNU_PTV_150_250_0J"
globalReplacementMap["STXS"]["procRVMap"]["RECO_ZH_LEP_Tag0"] = "QQ2HLL_PTV_0_75"
globalReplacementMap["STXS"]["procRVMap"]["RECO_ZH_LEP_Tag1"] = "QQ2HLL_PTV_0_75"
# Replacement category for RV fit
globalReplacementMap["STXS"]["catRVMap"] = od()
globalReplacementMap["STXS"]["catRVMap"]["RECO_0J_PTH_0_10_Tag0"] = "RECO_0J_PTH_0_10_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_0J_PTH_0_10_Tag1"] = "RECO_0J_PTH_0_10_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_0J_PTH_0_10_Tag2"] = "RECO_0J_PTH_0_10_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_0J_PTH_GT10_Tag0"] = "RECO_0J_PTH_GT10_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_0J_PTH_GT10_Tag1"] = "RECO_0J_PTH_GT10_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_0J_PTH_GT10_Tag2"] = "RECO_0J_PTH_GT10_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_0_60_Tag0"] = "RECO_1J_PTH_0_60_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_0_60_Tag1"] = "RECO_1J_PTH_0_60_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_0_60_Tag2"] = "RECO_1J_PTH_0_60_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_120_200_Tag0"] = "RECO_1J_PTH_120_200_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_120_200_Tag1"] = "RECO_1J_PTH_120_200_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_120_200_Tag2"] = "RECO_1J_PTH_120_200_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_60_120_Tag0"] = "RECO_1J_PTH_60_120_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_60_120_Tag1"] = "RECO_1J_PTH_60_120_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_60_120_Tag2"] = "RECO_1J_PTH_60_120_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_0_60_Tag0"] = "RECO_GE2J_PTH_0_60_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_0_60_Tag1"] = "RECO_GE2J_PTH_0_60_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_0_60_Tag2"] = "RECO_GE2J_PTH_0_60_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_120_200_Tag0"] = "RECO_GE2J_PTH_120_200_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_120_200_Tag1"] = "RECO_GE2J_PTH_120_200_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_120_200_Tag2"] = "RECO_GE2J_PTH_120_200_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_60_120_Tag0"] = "RECO_GE2J_PTH_60_120_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_60_120_Tag1"] = "RECO_GE2J_PTH_60_120_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_60_120_Tag2"] = "RECO_GE2J_PTH_60_120_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_PTH_200_300_Tag0"] = "RECO_PTH_200_300_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_PTH_200_300_Tag1"] = "RECO_PTH_200_300_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_PTH_300_450_Tag0"] = "RECO_PTH_300_450_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_PTH_300_450_Tag1"] = "RECO_PTH_300_450_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_PTH_450_650_Tag0"] = "RECO_PTH_450_650_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_PTH_GT650_Tag0"] = "RECO_PTH_GT650_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_THQ_LEP"] = "RECO_THQ_LEP"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag0"] = "RECO_TTH_HAD_PTH_0_60_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag1"] = "RECO_TTH_HAD_PTH_0_60_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag2"] = "RECO_TTH_HAD_PTH_0_60_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag3"] = "RECO_TTH_HAD_PTH_0_60_Tag3"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag0"] = "RECO_TTH_HAD_PTH_120_200_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag1"] = "RECO_TTH_HAD_PTH_120_200_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag2"] = "RECO_TTH_HAD_PTH_120_200_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag3"] = "RECO_TTH_HAD_PTH_120_200_Tag3"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_200_300_Tag0"] = "RECO_TTH_HAD_PTH_200_300_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_200_300_Tag1"] = "RECO_TTH_HAD_PTH_200_300_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_200_300_Tag2"] = "RECO_TTH_HAD_PTH_200_300_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag0"] = "RECO_TTH_HAD_PTH_60_120_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag1"] = "RECO_TTH_HAD_PTH_60_120_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag2"] = "RECO_TTH_HAD_PTH_60_120_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag3"] = "RECO_TTH_HAD_PTH_60_120_Tag3"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_GT300_Tag0"] = "RECO_TTH_HAD_PTH_GT300_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_GT300_Tag1"] = "RECO_TTH_HAD_PTH_GT300_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_GT300_Tag2"] = "RECO_TTH_HAD_PTH_GT300_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag0"] = "RECO_TTH_LEP_PTH_0_60_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag1"] = "RECO_TTH_LEP_PTH_0_60_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag2"] = "RECO_TTH_LEP_PTH_0_60_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_120_200_Tag0"] = "RECO_TTH_LEP_PTH_120_200_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_120_200_Tag1"] = "RECO_TTH_LEP_PTH_120_200_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_200_300_Tag0"] = "RECO_TTH_LEP_PTH_200_300_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_200_300_Tag1"] = "RECO_TTH_LEP_PTH_200_300_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_60_120_Tag0"] = "RECO_TTH_LEP_PTH_60_120_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_60_120_Tag1"] = "RECO_TTH_LEP_PTH_60_120_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_60_120_Tag2"] = "RECO_TTH_LEP_PTH_60_120_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_GT300_Tag0"] = "RECO_TTH_LEP_PTH_GT300_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFLIKEGGH_Tag0"] = "RECO_VBFLIKEGGH_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFLIKEGGH_Tag1"] = "RECO_VBFLIKEGGH_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_BSM_Tag0"] = "RECO_VBFTOPO_BSM_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_BSM_Tag1"] = "RECO_VBFTOPO_BSM_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag0"] = "RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag1"] = "RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag0"] = "RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag1"] = "RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3_HIGHMJJ_Tag0"] = "RECO_VBFTOPO_JET3_HIGHMJJ_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3_HIGHMJJ_Tag1"] = "RECO_VBFTOPO_JET3_HIGHMJJ_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3_LOWMJJ_Tag0"] = "RECO_VBFTOPO_JET3_LOWMJJ_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3_LOWMJJ_Tag1"] = "RECO_VBFTOPO_JET3_LOWMJJ_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_VHHAD_Tag0"] = "RECO_VBFTOPO_VHHAD_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_VHHAD_Tag1"] = "RECO_VBFTOPO_VHHAD_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VH_MET_Tag0"] = "RECO_VH_MET_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VH_MET_Tag1"] = "RECO_VH_MET_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VH_MET_Tag2"] = "RECO_VH_MET_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_WH_LEP_PTV_0_75_Tag0"] = "RECO_WH_LEP_PTV_0_75_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_WH_LEP_PTV_0_75_Tag1"] = "RECO_WH_LEP_PTV_0_75_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_WH_LEP_PTV_75_150_Tag0"] = "RECO_WH_LEP_PTV_75_150_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_WH_LEP_PTV_75_150_Tag1"] = "RECO_WH_LEP_PTV_75_150_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_WH_LEP_PTV_GT150_Tag0"] = "RECO_WH_LEP_PTV_GT150_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_ZH_LEP_Tag0"] = "RECO_ZH_LEP_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_ZH_LEP_Tag1"] = "RECO_ZH_LEP_Tag1"

# Tprime WW things
globalReplacementMap["TprimeM700Decay5pctSch"] = od()
globalReplacementMap["TprimeM700Decay5pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM700Decay5pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM700Decay5pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM700Decay5pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM700Decay5pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM700Decay5pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM700Decay5pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM700Decay5pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM700Decay10pctSch"] = od()
globalReplacementMap["TprimeM700Decay10pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM700Decay10pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM700Decay10pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM700Decay10pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM700Decay10pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM700Decay10pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM700Decay10pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM700Decay10pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM700Decay20pctSch"] = od()
globalReplacementMap["TprimeM700Decay20pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM700Decay20pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM700Decay20pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM700Decay20pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM700Decay20pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM700Decay20pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM700Decay20pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM700Decay20pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM700Decay30pctSch"] = od()
globalReplacementMap["TprimeM700Decay30pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM700Decay30pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM700Decay30pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM700Decay30pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM700Decay30pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM700Decay30pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM700Decay30pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM700Decay30pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM700Decay5pctTch"] = od()
globalReplacementMap["TprimeM700Decay5pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM700Decay5pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM700Decay5pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM700Decay5pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM700Decay5pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM700Decay5pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM700Decay5pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM700Decay5pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM700Decay10pctTch"] = od()
globalReplacementMap["TprimeM700Decay10pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM700Decay10pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM700Decay10pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM700Decay10pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM700Decay10pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM700Decay10pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM700Decay10pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM700Decay10pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM700Decay20pctTch"] = od()
globalReplacementMap["TprimeM700Decay20pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM700Decay20pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM700Decay20pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM700Decay20pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM700Decay20pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM700Decay20pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM700Decay20pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM700Decay20pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM700Decay30pctTch"] = od()
globalReplacementMap["TprimeM700Decay30pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM700Decay30pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM700Decay30pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM700Decay30pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM700Decay30pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM700Decay30pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM700Decay30pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM700Decay30pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM700Decay5pctInt"] = od()
globalReplacementMap["TprimeM700Decay5pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM700Decay5pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM700Decay5pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM700Decay5pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM700Decay5pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM700Decay5pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM700Decay5pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM700Decay5pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM700Decay10pctInt"] = od()
globalReplacementMap["TprimeM700Decay10pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM700Decay10pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM700Decay10pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM700Decay10pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM700Decay10pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM700Decay10pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM700Decay10pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM700Decay10pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM700Decay20pctInt"] = od()
globalReplacementMap["TprimeM700Decay20pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM700Decay20pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM700Decay20pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM700Decay20pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM700Decay20pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM700Decay20pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM700Decay20pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM700Decay20pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM700Decay30pctInt"] = od()
globalReplacementMap["TprimeM700Decay30pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM700Decay30pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM700Decay30pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM700Decay30pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM700Decay30pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM700Decay30pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM700Decay30pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM700Decay30pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM800Decay5pctSch"] = od()
globalReplacementMap["TprimeM800Decay5pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM800Decay5pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM800Decay5pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM800Decay5pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM800Decay5pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM800Decay5pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM800Decay5pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM800Decay5pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM800Decay10pctSch"] = od()
globalReplacementMap["TprimeM800Decay10pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM800Decay10pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM800Decay10pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM800Decay10pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM800Decay10pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM800Decay10pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM800Decay10pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM800Decay10pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM800Decay20pctSch"] = od()
globalReplacementMap["TprimeM800Decay20pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM800Decay20pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM800Decay20pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM800Decay20pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM800Decay20pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM800Decay20pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM800Decay20pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM800Decay20pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM800Decay30pctSch"] = od()
globalReplacementMap["TprimeM800Decay30pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM800Decay30pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM800Decay30pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM800Decay30pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM800Decay30pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM800Decay30pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM800Decay30pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM800Decay30pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM800Decay5pctTch"] = od()
globalReplacementMap["TprimeM800Decay5pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM800Decay5pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM800Decay5pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM800Decay5pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM800Decay5pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM800Decay5pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM800Decay5pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM800Decay5pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM800Decay10pctTch"] = od()
globalReplacementMap["TprimeM800Decay10pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM800Decay10pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM800Decay10pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM800Decay10pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM800Decay10pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM800Decay10pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM800Decay10pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM800Decay10pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM800Decay20pctTch"] = od()
globalReplacementMap["TprimeM800Decay20pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM800Decay20pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM800Decay20pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM800Decay20pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM800Decay20pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM800Decay20pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM800Decay20pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM800Decay20pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM800Decay30pctTch"] = od()
globalReplacementMap["TprimeM800Decay30pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM800Decay30pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM800Decay30pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM800Decay30pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM800Decay30pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM800Decay30pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM800Decay30pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM800Decay30pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM800Decay5pctInt"] = od()
globalReplacementMap["TprimeM800Decay5pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM800Decay5pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM800Decay5pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM800Decay5pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM800Decay5pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM800Decay5pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM800Decay5pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM800Decay5pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM800Decay10pctInt"] = od()
globalReplacementMap["TprimeM800Decay10pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM800Decay10pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM800Decay10pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM800Decay10pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM800Decay10pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM800Decay10pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM800Decay10pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM800Decay10pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM800Decay20pctInt"] = od()
globalReplacementMap["TprimeM800Decay20pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM800Decay20pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM800Decay20pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM800Decay20pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM800Decay20pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM800Decay20pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM800Decay20pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM800Decay20pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM800Decay30pctInt"] = od()
globalReplacementMap["TprimeM800Decay30pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM800Decay30pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM800Decay30pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM800Decay30pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM800Decay30pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM800Decay30pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM800Decay30pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM800Decay30pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM900Decay5pctSch"] = od()
globalReplacementMap["TprimeM900Decay5pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM900Decay5pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM900Decay5pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM900Decay5pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM900Decay5pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM900Decay5pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM900Decay5pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM900Decay5pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM900Decay10pctSch"] = od()
globalReplacementMap["TprimeM900Decay10pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM900Decay10pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM900Decay10pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM900Decay10pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM900Decay10pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM900Decay10pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM900Decay10pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM900Decay10pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM900Decay20pctSch"] = od()
globalReplacementMap["TprimeM900Decay20pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM900Decay20pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM900Decay20pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM900Decay20pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM900Decay20pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM900Decay20pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM900Decay20pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM900Decay20pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM900Decay30pctSch"] = od()
globalReplacementMap["TprimeM900Decay30pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM900Decay30pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM900Decay30pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM900Decay30pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM900Decay30pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM900Decay30pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM900Decay30pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM900Decay30pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM900Decay5pctTch"] = od()
globalReplacementMap["TprimeM900Decay5pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM900Decay5pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM900Decay5pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM900Decay5pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM900Decay5pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM900Decay5pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM900Decay5pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM900Decay5pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM900Decay10pctTch"] = od()
globalReplacementMap["TprimeM900Decay10pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM900Decay10pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM900Decay10pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM900Decay10pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM900Decay10pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM900Decay10pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM900Decay10pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM900Decay10pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM900Decay20pctTch"] = od()
globalReplacementMap["TprimeM900Decay20pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM900Decay20pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM900Decay20pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM900Decay20pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM900Decay20pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM900Decay20pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM900Decay20pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM900Decay20pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM900Decay30pctTch"] = od()
globalReplacementMap["TprimeM900Decay30pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM900Decay30pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM900Decay30pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM900Decay30pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM900Decay30pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM900Decay30pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM900Decay30pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM900Decay30pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM900Decay5pctInt"] = od()
globalReplacementMap["TprimeM900Decay5pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM900Decay5pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM900Decay5pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM900Decay5pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM900Decay5pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM900Decay5pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM900Decay5pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM900Decay5pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM900Decay10pctInt"] = od()
globalReplacementMap["TprimeM900Decay10pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM900Decay10pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM900Decay10pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM900Decay10pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM900Decay10pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM900Decay10pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM900Decay10pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM900Decay10pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM900Decay20pctInt"] = od()
globalReplacementMap["TprimeM900Decay20pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM900Decay20pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM900Decay20pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM900Decay20pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM900Decay20pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM900Decay20pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM900Decay20pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM900Decay20pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM900Decay30pctInt"] = od()
globalReplacementMap["TprimeM900Decay30pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM900Decay30pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM900Decay30pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM900Decay30pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM900Decay30pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM900Decay30pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM900Decay30pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM900Decay30pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1000Decay5pctSch"] = od()
globalReplacementMap["TprimeM1000Decay5pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1000Decay5pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1000Decay5pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1000Decay5pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1000Decay5pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1000Decay5pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1000Decay5pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1000Decay5pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1000Decay10pctSch"] = od()
globalReplacementMap["TprimeM1000Decay10pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1000Decay10pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1000Decay10pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1000Decay10pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1000Decay10pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1000Decay10pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1000Decay10pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1000Decay10pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1000Decay20pctSch"] = od()
globalReplacementMap["TprimeM1000Decay20pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1000Decay20pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1000Decay20pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1000Decay20pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1000Decay20pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1000Decay20pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1000Decay20pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1000Decay20pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1000Decay30pctSch"] = od()
globalReplacementMap["TprimeM1000Decay30pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1000Decay30pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1000Decay30pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1000Decay30pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1000Decay30pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1000Decay30pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1000Decay30pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1000Decay30pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1000Decay5pctTch"] = od()
globalReplacementMap["TprimeM1000Decay5pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1000Decay5pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1000Decay5pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1000Decay5pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1000Decay5pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1000Decay5pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1000Decay5pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1000Decay5pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1000Decay10pctTch"] = od()
globalReplacementMap["TprimeM1000Decay10pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1000Decay10pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1000Decay10pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1000Decay10pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1000Decay10pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1000Decay10pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1000Decay10pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1000Decay10pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1000Decay20pctTch"] = od()
globalReplacementMap["TprimeM1000Decay20pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1000Decay20pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1000Decay20pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1000Decay20pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1000Decay20pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1000Decay20pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1000Decay20pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1000Decay20pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1000Decay30pctTch"] = od()
globalReplacementMap["TprimeM1000Decay30pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1000Decay30pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1000Decay30pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1000Decay30pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1000Decay30pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1000Decay30pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1000Decay30pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1000Decay30pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1000Decay5pctInt"] = od()
globalReplacementMap["TprimeM1000Decay5pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1000Decay5pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1000Decay5pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM1000Decay5pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1000Decay5pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1000Decay5pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM1000Decay5pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1000Decay5pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1000Decay10pctInt"] = od()
globalReplacementMap["TprimeM1000Decay10pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1000Decay10pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1000Decay10pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM1000Decay10pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1000Decay10pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1000Decay10pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM1000Decay10pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1000Decay10pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1000Decay20pctInt"] = od()
globalReplacementMap["TprimeM1000Decay20pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1000Decay20pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1000Decay20pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM1000Decay20pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1000Decay20pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1000Decay20pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM1000Decay20pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1000Decay20pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1000Decay30pctInt"] = od()
globalReplacementMap["TprimeM1000Decay30pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1000Decay30pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1000Decay30pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM1000Decay30pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1000Decay30pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1000Decay30pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM1000Decay30pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1000Decay30pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1100Decay5pctSch"] = od()
globalReplacementMap["TprimeM1100Decay5pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1100Decay5pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1100Decay5pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1100Decay5pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1100Decay5pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1100Decay5pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1100Decay5pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1100Decay5pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1100Decay10pctSch"] = od()
globalReplacementMap["TprimeM1100Decay10pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1100Decay10pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1100Decay10pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1100Decay10pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1100Decay10pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1100Decay10pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1100Decay10pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1100Decay10pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1100Decay20pctSch"] = od()
globalReplacementMap["TprimeM1100Decay20pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1100Decay20pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1100Decay20pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1100Decay20pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1100Decay20pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1100Decay20pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1100Decay20pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1100Decay20pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1100Decay30pctSch"] = od()
globalReplacementMap["TprimeM1100Decay30pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1100Decay30pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1100Decay30pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1100Decay30pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1100Decay30pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1100Decay30pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1100Decay30pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1100Decay30pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1100Decay5pctTch"] = od()
globalReplacementMap["TprimeM1100Decay5pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1100Decay5pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1100Decay5pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1100Decay5pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1100Decay5pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1100Decay5pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1100Decay5pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1100Decay5pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1100Decay10pctTch"] = od()
globalReplacementMap["TprimeM1100Decay10pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1100Decay10pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1100Decay10pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1100Decay10pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1100Decay10pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1100Decay10pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1100Decay10pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1100Decay10pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1100Decay20pctTch"] = od()
globalReplacementMap["TprimeM1100Decay20pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1100Decay20pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1100Decay20pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1100Decay20pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1100Decay20pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1100Decay20pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1100Decay20pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1100Decay20pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1100Decay30pctTch"] = od()
globalReplacementMap["TprimeM1100Decay30pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1100Decay30pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1100Decay30pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1100Decay30pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1100Decay30pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1100Decay30pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1100Decay30pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1100Decay30pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1100Decay5pctInt"] = od()
globalReplacementMap["TprimeM1100Decay5pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1100Decay5pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1100Decay5pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM1100Decay5pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1100Decay5pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1100Decay5pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM1100Decay5pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1100Decay5pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1100Decay10pctInt"] = od()
globalReplacementMap["TprimeM1100Decay10pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1100Decay10pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1100Decay10pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM1100Decay10pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1100Decay10pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1100Decay10pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM1100Decay10pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1100Decay10pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1100Decay20pctInt"] = od()
globalReplacementMap["TprimeM1100Decay20pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1100Decay20pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1100Decay20pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM1100Decay20pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1100Decay20pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1100Decay20pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM1100Decay20pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1100Decay20pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1100Decay30pctInt"] = od()
globalReplacementMap["TprimeM1100Decay30pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1100Decay30pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1100Decay30pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM1100Decay30pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1100Decay30pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1100Decay30pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM1100Decay30pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1100Decay30pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1200Decay5pctSch"] = od()
globalReplacementMap["TprimeM1200Decay5pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1200Decay5pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1200Decay5pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1200Decay5pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1200Decay5pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1200Decay5pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1200Decay5pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1200Decay5pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1200Decay10pctSch"] = od()
globalReplacementMap["TprimeM1200Decay10pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1200Decay10pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1200Decay10pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1200Decay10pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1200Decay10pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1200Decay10pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1200Decay10pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1200Decay10pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1200Decay20pctSch"] = od()
globalReplacementMap["TprimeM1200Decay20pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1200Decay20pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1200Decay20pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1200Decay20pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1200Decay20pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1200Decay20pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1200Decay20pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1200Decay20pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1200Decay30pctSch"] = od()
globalReplacementMap["TprimeM1200Decay30pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1200Decay30pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1200Decay30pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1200Decay30pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1200Decay30pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1200Decay30pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1200Decay30pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1200Decay30pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1200Decay5pctTch"] = od()
globalReplacementMap["TprimeM1200Decay5pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1200Decay5pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1200Decay5pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1200Decay5pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1200Decay5pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1200Decay5pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1200Decay5pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1200Decay5pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1200Decay10pctTch"] = od()
globalReplacementMap["TprimeM1200Decay10pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1200Decay10pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1200Decay10pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1200Decay10pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1200Decay10pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1200Decay10pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1200Decay10pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1200Decay10pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1200Decay20pctTch"] = od()
globalReplacementMap["TprimeM1200Decay20pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1200Decay20pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1200Decay20pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1200Decay20pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1200Decay20pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1200Decay20pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1200Decay20pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1200Decay20pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1200Decay30pctTch"] = od()
globalReplacementMap["TprimeM1200Decay30pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1200Decay30pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1200Decay30pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1200Decay30pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1200Decay30pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1200Decay30pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1200Decay30pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1200Decay30pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1200Decay5pctInt"] = od()
globalReplacementMap["TprimeM1200Decay5pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1200Decay5pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1200Decay5pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM1200Decay5pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1200Decay5pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1200Decay5pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM1200Decay5pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1200Decay5pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1200Decay10pctInt"] = od()
globalReplacementMap["TprimeM1200Decay10pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1200Decay10pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1200Decay10pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM1200Decay10pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1200Decay10pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1200Decay10pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM1200Decay10pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1200Decay10pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1200Decay20pctInt"] = od()
globalReplacementMap["TprimeM1200Decay20pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1200Decay20pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1200Decay20pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM1200Decay20pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1200Decay20pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1200Decay20pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM1200Decay20pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1200Decay20pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1200Decay30pctInt"] = od()
globalReplacementMap["TprimeM1200Decay30pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1200Decay30pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1200Decay30pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM1200Decay30pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1200Decay30pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1200Decay30pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM1200Decay30pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1200Decay30pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1400Decay5pctSch"] = od()
globalReplacementMap["TprimeM1400Decay5pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1400Decay5pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1400Decay5pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1400Decay5pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1400Decay5pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1400Decay5pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1400Decay5pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1400Decay5pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1400Decay10pctSch"] = od()
globalReplacementMap["TprimeM1400Decay10pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1400Decay10pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1400Decay10pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1400Decay10pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1400Decay10pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1400Decay10pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1400Decay10pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1400Decay10pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1400Decay20pctSch"] = od()
globalReplacementMap["TprimeM1400Decay20pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1400Decay20pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1400Decay20pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1400Decay20pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1400Decay20pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1400Decay20pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1400Decay20pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1400Decay20pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1400Decay30pctSch"] = od()
globalReplacementMap["TprimeM1400Decay30pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1400Decay30pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1400Decay30pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1400Decay30pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1400Decay30pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1400Decay30pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1400Decay30pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1400Decay30pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1400Decay5pctTch"] = od()
globalReplacementMap["TprimeM1400Decay5pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1400Decay5pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1400Decay5pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1400Decay5pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1400Decay5pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1400Decay5pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1400Decay5pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1400Decay5pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1400Decay10pctTch"] = od()
globalReplacementMap["TprimeM1400Decay10pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1400Decay10pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1400Decay10pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1400Decay10pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1400Decay10pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1400Decay10pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1400Decay10pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1400Decay10pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1400Decay20pctTch"] = od()
globalReplacementMap["TprimeM1400Decay20pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1400Decay20pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1400Decay20pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1400Decay20pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1400Decay20pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1400Decay20pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1400Decay20pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1400Decay20pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1400Decay30pctTch"] = od()
globalReplacementMap["TprimeM1400Decay30pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1400Decay30pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1400Decay30pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1400Decay30pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1400Decay30pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1400Decay30pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1400Decay30pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1400Decay30pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1400Decay5pctInt"] = od()
globalReplacementMap["TprimeM1400Decay5pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1400Decay5pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1400Decay5pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM1400Decay5pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1400Decay5pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1400Decay5pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM1400Decay5pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1400Decay5pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1400Decay10pctInt"] = od()
globalReplacementMap["TprimeM1400Decay10pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1400Decay10pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1400Decay10pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM1400Decay10pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1400Decay10pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1400Decay10pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM1400Decay10pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1400Decay10pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1400Decay20pctInt"] = od()
globalReplacementMap["TprimeM1400Decay20pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1400Decay20pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1400Decay20pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM1400Decay20pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1400Decay20pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1400Decay20pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM1400Decay20pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1400Decay20pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1400Decay30pctInt"] = od()
globalReplacementMap["TprimeM1400Decay30pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1400Decay30pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1400Decay30pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM1400Decay30pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1400Decay30pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1400Decay30pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM1400Decay30pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1400Decay30pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1600Decay5pctSch"] = od()
globalReplacementMap["TprimeM1600Decay5pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1600Decay5pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1600Decay5pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1600Decay5pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1600Decay5pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1600Decay5pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1600Decay5pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1600Decay5pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1600Decay10pctSch"] = od()
globalReplacementMap["TprimeM1600Decay10pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1600Decay10pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1600Decay10pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1600Decay10pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1600Decay10pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1600Decay10pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1600Decay10pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1600Decay10pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1600Decay20pctSch"] = od()
globalReplacementMap["TprimeM1600Decay20pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1600Decay20pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1600Decay20pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1600Decay20pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1600Decay20pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1600Decay20pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1600Decay20pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1600Decay20pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1600Decay30pctSch"] = od()
globalReplacementMap["TprimeM1600Decay30pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1600Decay30pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1600Decay30pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1600Decay30pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1600Decay30pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1600Decay30pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1600Decay30pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1600Decay30pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1600Decay5pctTch"] = od()
globalReplacementMap["TprimeM1600Decay5pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1600Decay5pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1600Decay5pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1600Decay5pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1600Decay5pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1600Decay5pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1600Decay5pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1600Decay5pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1600Decay10pctTch"] = od()
globalReplacementMap["TprimeM1600Decay10pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1600Decay10pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1600Decay10pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1600Decay10pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1600Decay10pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1600Decay10pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1600Decay10pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1600Decay10pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1600Decay20pctTch"] = od()
globalReplacementMap["TprimeM1600Decay20pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1600Decay20pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1600Decay20pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1600Decay20pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1600Decay20pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1600Decay20pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1600Decay20pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1600Decay20pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1600Decay30pctTch"] = od()
globalReplacementMap["TprimeM1600Decay30pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1600Decay30pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1600Decay30pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1600Decay30pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1600Decay30pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1600Decay30pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1600Decay30pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1600Decay30pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1600Decay5pctInt"] = od()
globalReplacementMap["TprimeM1600Decay5pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1600Decay5pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1600Decay5pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM1600Decay5pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1600Decay5pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1600Decay5pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM1600Decay5pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1600Decay5pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1600Decay10pctInt"] = od()
globalReplacementMap["TprimeM1600Decay10pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1600Decay10pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1600Decay10pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM1600Decay10pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1600Decay10pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1600Decay10pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM1600Decay10pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1600Decay10pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1600Decay20pctInt"] = od()
globalReplacementMap["TprimeM1600Decay20pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1600Decay20pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1600Decay20pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM1600Decay20pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1600Decay20pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1600Decay20pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM1600Decay20pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1600Decay20pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1600Decay30pctInt"] = od()
globalReplacementMap["TprimeM1600Decay30pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1600Decay30pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1600Decay30pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM1600Decay30pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1600Decay30pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1600Decay30pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM1600Decay30pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1600Decay30pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1800Decay5pctSch"] = od()
globalReplacementMap["TprimeM1800Decay5pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1800Decay5pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1800Decay5pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1800Decay5pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1800Decay5pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1800Decay5pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1800Decay5pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1800Decay5pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1800Decay10pctSch"] = od()
globalReplacementMap["TprimeM1800Decay10pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1800Decay10pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1800Decay10pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1800Decay10pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1800Decay10pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1800Decay10pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1800Decay10pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1800Decay10pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1800Decay20pctSch"] = od()
globalReplacementMap["TprimeM1800Decay20pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1800Decay20pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1800Decay20pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1800Decay20pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1800Decay20pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1800Decay20pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1800Decay20pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1800Decay20pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1800Decay30pctSch"] = od()
globalReplacementMap["TprimeM1800Decay30pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1800Decay30pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1800Decay30pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1800Decay30pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1800Decay30pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1800Decay30pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1800Decay30pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1800Decay30pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1800Decay5pctTch"] = od()
globalReplacementMap["TprimeM1800Decay5pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1800Decay5pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1800Decay5pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1800Decay5pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1800Decay5pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1800Decay5pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1800Decay5pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1800Decay5pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1800Decay10pctTch"] = od()
globalReplacementMap["TprimeM1800Decay10pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1800Decay10pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1800Decay10pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1800Decay10pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1800Decay10pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1800Decay10pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1800Decay10pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1800Decay10pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1800Decay20pctTch"] = od()
globalReplacementMap["TprimeM1800Decay20pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1800Decay20pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1800Decay20pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1800Decay20pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1800Decay20pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1800Decay20pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1800Decay20pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1800Decay20pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1800Decay30pctTch"] = od()
globalReplacementMap["TprimeM1800Decay30pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1800Decay30pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1800Decay30pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM1800Decay30pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1800Decay30pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1800Decay30pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM1800Decay30pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1800Decay30pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1800Decay5pctInt"] = od()
globalReplacementMap["TprimeM1800Decay5pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1800Decay5pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1800Decay5pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM1800Decay5pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1800Decay5pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1800Decay5pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM1800Decay5pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1800Decay5pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1800Decay10pctInt"] = od()
globalReplacementMap["TprimeM1800Decay10pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1800Decay10pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1800Decay10pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM1800Decay10pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1800Decay10pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1800Decay10pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM1800Decay10pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1800Decay10pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1800Decay20pctInt"] = od()
globalReplacementMap["TprimeM1800Decay20pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1800Decay20pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1800Decay20pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM1800Decay20pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1800Decay20pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1800Decay20pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM1800Decay20pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1800Decay20pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM1800Decay30pctInt"] = od()
globalReplacementMap["TprimeM1800Decay30pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM1800Decay30pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1800Decay30pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM1800Decay30pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM1800Decay30pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM1800Decay30pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM1800Decay30pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM1800Decay30pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2000Decay5pctSch"] = od()
globalReplacementMap["TprimeM2000Decay5pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2000Decay5pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2000Decay5pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2000Decay5pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2000Decay5pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2000Decay5pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2000Decay5pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2000Decay5pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2000Decay10pctSch"] = od()
globalReplacementMap["TprimeM2000Decay10pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2000Decay10pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2000Decay10pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2000Decay10pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2000Decay10pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2000Decay10pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2000Decay10pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2000Decay10pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2000Decay20pctSch"] = od()
globalReplacementMap["TprimeM2000Decay20pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2000Decay20pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2000Decay20pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2000Decay20pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2000Decay20pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2000Decay20pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2000Decay20pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2000Decay20pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2000Decay30pctSch"] = od()
globalReplacementMap["TprimeM2000Decay30pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2000Decay30pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2000Decay30pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2000Decay30pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2000Decay30pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2000Decay30pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2000Decay30pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2000Decay30pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2000Decay5pctTch"] = od()
globalReplacementMap["TprimeM2000Decay5pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2000Decay5pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2000Decay5pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2000Decay5pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2000Decay5pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2000Decay5pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2000Decay5pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2000Decay5pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2000Decay10pctTch"] = od()
globalReplacementMap["TprimeM2000Decay10pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2000Decay10pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2000Decay10pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2000Decay10pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2000Decay10pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2000Decay10pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2000Decay10pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2000Decay10pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2000Decay20pctTch"] = od()
globalReplacementMap["TprimeM2000Decay20pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2000Decay20pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2000Decay20pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2000Decay20pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2000Decay20pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2000Decay20pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2000Decay20pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2000Decay20pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2000Decay30pctTch"] = od()
globalReplacementMap["TprimeM2000Decay30pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2000Decay30pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2000Decay30pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2000Decay30pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2000Decay30pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2000Decay30pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2000Decay30pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2000Decay30pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2000Decay5pctInt"] = od()
globalReplacementMap["TprimeM2000Decay5pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2000Decay5pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2000Decay5pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM2000Decay5pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2000Decay5pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2000Decay5pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM2000Decay5pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2000Decay5pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2000Decay10pctInt"] = od()
globalReplacementMap["TprimeM2000Decay10pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2000Decay10pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2000Decay10pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM2000Decay10pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2000Decay10pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2000Decay10pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM2000Decay10pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2000Decay10pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2000Decay20pctInt"] = od()
globalReplacementMap["TprimeM2000Decay20pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2000Decay20pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2000Decay20pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM2000Decay20pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2000Decay20pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2000Decay20pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM2000Decay20pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2000Decay20pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2000Decay30pctInt"] = od()
globalReplacementMap["TprimeM2000Decay30pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2000Decay30pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2000Decay30pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM2000Decay30pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2000Decay30pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2000Decay30pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM2000Decay30pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2000Decay30pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2200Decay5pctSch"] = od()
globalReplacementMap["TprimeM2200Decay5pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2200Decay5pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2200Decay5pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2200Decay5pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2200Decay5pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2200Decay5pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2200Decay5pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2200Decay5pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2200Decay10pctSch"] = od()
globalReplacementMap["TprimeM2200Decay10pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2200Decay10pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2200Decay10pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2200Decay10pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2200Decay10pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2200Decay10pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2200Decay10pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2200Decay10pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2200Decay20pctSch"] = od()
globalReplacementMap["TprimeM2200Decay20pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2200Decay20pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2200Decay20pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2200Decay20pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2200Decay20pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2200Decay20pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2200Decay20pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2200Decay20pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2200Decay30pctSch"] = od()
globalReplacementMap["TprimeM2200Decay30pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2200Decay30pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2200Decay30pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2200Decay30pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2200Decay30pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2200Decay30pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2200Decay30pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2200Decay30pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2200Decay5pctTch"] = od()
globalReplacementMap["TprimeM2200Decay5pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2200Decay5pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2200Decay5pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2200Decay5pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2200Decay5pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2200Decay5pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2200Decay5pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2200Decay5pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2200Decay10pctTch"] = od()
globalReplacementMap["TprimeM2200Decay10pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2200Decay10pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2200Decay10pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2200Decay10pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2200Decay10pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2200Decay10pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2200Decay10pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2200Decay10pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2200Decay20pctTch"] = od()
globalReplacementMap["TprimeM2200Decay20pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2200Decay20pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2200Decay20pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2200Decay20pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2200Decay20pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2200Decay20pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2200Decay20pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2200Decay20pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2200Decay30pctTch"] = od()
globalReplacementMap["TprimeM2200Decay30pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2200Decay30pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2200Decay30pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2200Decay30pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2200Decay30pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2200Decay30pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2200Decay30pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2200Decay30pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2200Decay5pctInt"] = od()
globalReplacementMap["TprimeM2200Decay5pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2200Decay5pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2200Decay5pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM2200Decay5pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2200Decay5pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2200Decay5pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM2200Decay5pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2200Decay5pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2200Decay10pctInt"] = od()
globalReplacementMap["TprimeM2200Decay10pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2200Decay10pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2200Decay10pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM2200Decay10pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2200Decay10pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2200Decay10pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM2200Decay10pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2200Decay10pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2200Decay20pctInt"] = od()
globalReplacementMap["TprimeM2200Decay20pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2200Decay20pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2200Decay20pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM2200Decay20pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2200Decay20pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2200Decay20pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM2200Decay20pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2200Decay20pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2200Decay30pctInt"] = od()
globalReplacementMap["TprimeM2200Decay30pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2200Decay30pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2200Decay30pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM2200Decay30pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2200Decay30pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2200Decay30pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM2200Decay30pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2200Decay30pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2400Decay5pctSch"] = od()
globalReplacementMap["TprimeM2400Decay5pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2400Decay5pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2400Decay5pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2400Decay5pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2400Decay5pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2400Decay5pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2400Decay5pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2400Decay5pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2400Decay10pctSch"] = od()
globalReplacementMap["TprimeM2400Decay10pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2400Decay10pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2400Decay10pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2400Decay10pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2400Decay10pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2400Decay10pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2400Decay10pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2400Decay10pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2400Decay20pctSch"] = od()
globalReplacementMap["TprimeM2400Decay20pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2400Decay20pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2400Decay20pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2400Decay20pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2400Decay20pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2400Decay20pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2400Decay20pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2400Decay20pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2400Decay30pctSch"] = od()
globalReplacementMap["TprimeM2400Decay30pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2400Decay30pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2400Decay30pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2400Decay30pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2400Decay30pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2400Decay30pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2400Decay30pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2400Decay30pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2400Decay5pctTch"] = od()
globalReplacementMap["TprimeM2400Decay5pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2400Decay5pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2400Decay5pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2400Decay5pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2400Decay5pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2400Decay5pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2400Decay5pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2400Decay5pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2400Decay10pctTch"] = od()
globalReplacementMap["TprimeM2400Decay10pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2400Decay10pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2400Decay10pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2400Decay10pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2400Decay10pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2400Decay10pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2400Decay10pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2400Decay10pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2400Decay20pctTch"] = od()
globalReplacementMap["TprimeM2400Decay20pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2400Decay20pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2400Decay20pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2400Decay20pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2400Decay20pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2400Decay20pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2400Decay20pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2400Decay20pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2400Decay30pctTch"] = od()
globalReplacementMap["TprimeM2400Decay30pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2400Decay30pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2400Decay30pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2400Decay30pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2400Decay30pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2400Decay30pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2400Decay30pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2400Decay30pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2400Decay5pctInt"] = od()
globalReplacementMap["TprimeM2400Decay5pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2400Decay5pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2400Decay5pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM2400Decay5pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2400Decay5pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2400Decay5pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM2400Decay5pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2400Decay5pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2400Decay10pctInt"] = od()
globalReplacementMap["TprimeM2400Decay10pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2400Decay10pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2400Decay10pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM2400Decay10pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2400Decay10pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2400Decay10pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM2400Decay10pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2400Decay10pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2400Decay20pctInt"] = od()
globalReplacementMap["TprimeM2400Decay20pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2400Decay20pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2400Decay20pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM2400Decay20pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2400Decay20pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2400Decay20pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM2400Decay20pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2400Decay20pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2400Decay30pctInt"] = od()
globalReplacementMap["TprimeM2400Decay30pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2400Decay30pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2400Decay30pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM2400Decay30pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2400Decay30pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2400Decay30pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM2400Decay30pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2400Decay30pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2600Decay5pctSch"] = od()
globalReplacementMap["TprimeM2600Decay5pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2600Decay5pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2600Decay5pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2600Decay5pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2600Decay5pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2600Decay5pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2600Decay5pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2600Decay5pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2600Decay10pctSch"] = od()
globalReplacementMap["TprimeM2600Decay10pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2600Decay10pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2600Decay10pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2600Decay10pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2600Decay10pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2600Decay10pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2600Decay10pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2600Decay10pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2600Decay20pctSch"] = od()
globalReplacementMap["TprimeM2600Decay20pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2600Decay20pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2600Decay20pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2600Decay20pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2600Decay20pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2600Decay20pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2600Decay20pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2600Decay20pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2600Decay30pctSch"] = od()
globalReplacementMap["TprimeM2600Decay30pctSch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2600Decay30pctSch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2600Decay30pctSch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2600Decay30pctSch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2600Decay30pctSch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2600Decay30pctSch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2600Decay30pctSch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2600Decay30pctSch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2600Decay5pctTch"] = od()
globalReplacementMap["TprimeM2600Decay5pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2600Decay5pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2600Decay5pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2600Decay5pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2600Decay5pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2600Decay5pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2600Decay5pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2600Decay5pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2600Decay10pctTch"] = od()
globalReplacementMap["TprimeM2600Decay10pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2600Decay10pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2600Decay10pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2600Decay10pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2600Decay10pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2600Decay10pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2600Decay10pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2600Decay10pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2600Decay20pctTch"] = od()
globalReplacementMap["TprimeM2600Decay20pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2600Decay20pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2600Decay20pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2600Decay20pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2600Decay20pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2600Decay20pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2600Decay20pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2600Decay20pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2600Decay30pctTch"] = od()
globalReplacementMap["TprimeM2600Decay30pctTch"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2600Decay30pctTch"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2600Decay30pctTch"]["procRVMap"] = od()
globalReplacementMap["TprimeM2600Decay30pctTch"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2600Decay30pctTch"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2600Decay30pctTch"]["catRVMap"] = od()
globalReplacementMap["TprimeM2600Decay30pctTch"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2600Decay30pctTch"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2600Decay5pctInt"] = od()
globalReplacementMap["TprimeM2600Decay5pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2600Decay5pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2600Decay5pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM2600Decay5pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2600Decay5pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2600Decay5pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM2600Decay5pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2600Decay5pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2600Decay10pctInt"] = od()
globalReplacementMap["TprimeM2600Decay10pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2600Decay10pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2600Decay10pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM2600Decay10pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2600Decay10pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2600Decay10pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM2600Decay10pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2600Decay10pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2600Decay20pctInt"] = od()
globalReplacementMap["TprimeM2600Decay20pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2600Decay20pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2600Decay20pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM2600Decay20pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2600Decay20pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2600Decay20pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM2600Decay20pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2600Decay20pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap["TprimeM2600Decay30pctInt"] = od()
globalReplacementMap["TprimeM2600Decay30pctInt"]["procWV"] = "THQ"
globalReplacementMap["TprimeM2600Decay30pctInt"]["catWV"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2600Decay30pctInt"]["procRVMap"] = od()
globalReplacementMap["TprimeM2600Decay30pctInt"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["TprimeM2600Decay30pctInt"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["TprimeM2600Decay30pctInt"]["catRVMap"] = od()
globalReplacementMap["TprimeM2600Decay30pctInt"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["TprimeM2600Decay30pctInt"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"
