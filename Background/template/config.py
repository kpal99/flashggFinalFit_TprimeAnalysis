# Config file: options for signal fitting

backgroundScriptCfg = {

  # Setup
  'inputWS':'{{ inputWS }}', # location of 'allData.root' file
  'cats':'auto', # auto: automatically inferred from input ws
  'catOffset':0, # add offset to category numbers (useful for categories from different allData.root files)
  'ext':'{{ ext }}', # extension to add to output directory
  'year':'{{ year }}', # Use combined when merging all years in category (for plots)

  # Job submission options
  'batch':'local', # [condor,SGE,IC,local]
  'queue':'espresso' # for condor e.g. microcentury

}
