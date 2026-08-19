# Config file: options for signal fitting

#_year = "2018"
#_Tmass = "600"
signalScriptCfg = {

  # Setup
  'inputWSDir':'{{ inputWSDir }}',
 'procs':'{{ procs }}Sch,{{ procs }}Tch,{{ procs }}Int,GG2H,TTH,VBF,VH',
  'cats':'Leptonic,Hadronic', # if auto: inferred automatically from (0) workspace
#  'ext':'Tprime%s_%s'%(_Tmass,_year),
  'ext':'{{ procs }}_{{ year }}',
#  'analysis':'Tprime_%s'%_Tmass, # To specify which replacement dataset mapping (defined in ./python/replacementMap.py)
  'analysis':'TprimeRun2',
  'year': '{{ year }}',
#  'massPoints':'120,125,130',
  'massPoints':'125',

  #Photon shape systematics
  'scales':'ElectonScale',
  'scalesCorr':'Material,FNUF,ShowerShape,MET', # correlated across years
  'scalesGlobal':'JecSystTotal,JerSyst', # affect all processes equally, correlated across years
  'smears':'ElectronSmearing,Smearing',
#  'scales':'HighR9EB,HighR9EE,LowR9EB,LowR9EE,Gain1EB,Gain6EB', # separate nuisance per year
#  'scalesCorr':'MaterialCentralBarrel,MaterialOuterBarrel,MaterialForward,FNUFEE,FNUFEB,ShowerShapeHighR9EE,ShowerShapeHighR9EB,ShowerShapeLowR9EE,ShowerShapeLowR9EB', # correlated across years
#  'scalesGlobal':'NonLinearity,Geant4', # affect all processes equally, correlated across years
#  'smears':'HighR9EBPhi,HighR9EBRho,HighR9EEPhi,HighR9EERho,LowR9EBPhi,LowR9EBRho,LowR9EEPhi,LowR9EERho', # separate nuisance per year

  # Job submission options
  'batch':'local', # ['condor','SGE','IC','local']
  'queue':'espresso'
}
