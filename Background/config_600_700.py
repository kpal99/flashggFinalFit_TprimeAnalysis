# Config file: options for signal fitting

backgroundScriptCfg = {
  
  # Setup
  'inputWSDir':'/eos/user/p/prsaha/Tprime_analysis/FinalFit_inputs/UL/v2/600_700/', # location of 'allData.root' file
#  'inputWSDir':'/eos/user/p/prsaha/Tprime_analysis/FinalFit_inputs/v7/600_700/',
  'cats':'THQLeptonicTag,THQHadronicTag', # auto: automatically inferred from input ws
#  'cats':'THQHadronic',
  'catOffset':0, # add offset to category numbers (useful for categories from different allData.root files)  
  'ext':'Tprime600_700', # extension to add to output directory
  'year':'combined', # Use combined when merging all years in category (for plots)

  # Job submission options
  'batch':'condor', # [condor,SGE,IC,local]
  'queue':'microcentury' # for condor e.g. microcentury
  
}
