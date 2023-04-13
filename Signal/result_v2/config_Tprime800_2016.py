# Config file: options for signal fitting

_year = '2016'

signalScriptCfg = {
  
  # Setup
  'inputWSDir':'/eos/user/p/prsaha/Tprime_analysis/FinalFit_inputs/v2/%s/M800'%_year,
  'procs':'THQ', # if auto: inferred automatically from filenames
  'cats':'THQLeptonicTag', # if auto: inferred automatically from (0) workspace
  'ext':'Tprime800_%s'%_year,
  'analysis':'Tprime', # To specify which replacement dataset mapping (defined in ./python/replacementMap.py)
  'year':'%s'%_year, # Use 'combined' if merging all years: not recommended
#  'massPoints':'120,125,130',
  'massPoints':'125',
  #Photon shape systematics  
#  'scales':'HighR9EB,HighR9EE,LowR9EB,LowR9EE,Gain1EB,Gain6EB', # separate nuisance per year
  'scales':'',
#  'scalesCorr':'MaterialCentralBarrel,MaterialOuterBarrel,MaterialForward,FNUFEE,FNUFEB,ShowerShapeHighR9EE,ShowerShapeHighR9EB,ShowerShapeLowR9EE,ShowerShapeLowR9EB', # correlated across years
  'scalesCorr':'',
#  'scalesGlobal':'NonLinearity,Geant4', # affect all processes equally, correlated across years
  'scalesGlobal':'',
#  'smears':'HighR9EBPhi,HighR9EBRho,HighR9EEPhi,HighR9EERho,LowR9EBPhi,LowR9EBRho,LowR9EEPhi,LowR9EERho', # separate nuisance per year
  'smears':'',
  # Job submission options
#  'batch':'IC', # ['condor','SGE','IC','local']
#  'queue':'hep.q'
  'batch':'condor', # ['condor','SGE','IC','local']
  'queue':'espresso'

}
