# Config file: options for signal fitting

backgroundScriptCfg = {
  
  # Setup
  'inputWSDir':'/eos/user/k/kpal/tprime_ww/full1_data2018/ws', # location of 'allData.root' file
  'cats':'THQLeptonicTag,THQHadronicTag', # auto: automatically inferred from input ws
  'catOffset':0, # add offset to category numbers (useful for categories from different allData.root files)  
  'ext':'Tprime', # extension to add to output directory
  'year':'2018', # Use combined when merging all years in category (for plots)

  # Job submission options
  'batch':'condor', # [condor,SGE,IC,local]
  'queue':'microcentury' # for condor e.g. microcentury
  
}

