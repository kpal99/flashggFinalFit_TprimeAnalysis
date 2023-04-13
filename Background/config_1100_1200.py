# Config file: options for signal fitting

backgroundScriptCfg = {
  
  # Setup
  'inputWSDir':'/eos/user/p/prsaha/Tprime_analysis/FinalFit_inputs/UL/v2/1100_1200/', # location of 'allData.root' file
  'cats':'THQLeptonicTag,THQHadronicTag', # auto: automatically inferred from input ws
  'catOffset':0, # add offset to category numbers (useful for categories from different allData.root files)  
  'ext':'Tprime1100_1200', # extension to add to output directory
  'year':'combined', # Use combined when merging all years in category (for plots)

  # Job submission options
  'batch':'condor', # [condor,SGE,IC,local]
  'queue':'microcentury' # for condor e.g. microcentury
  
}
