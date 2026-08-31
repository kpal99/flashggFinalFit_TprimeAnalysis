# Script to package individual signal models for a single category in one ROOT file
# Option to merge different extensions (years)

import os, re, sys
import glob
import ROOT
from optparse import OptionParser

def get_options():
  parser = OptionParser()
  parser.add_option("--cat", dest='cat', default='RECO_0J_PTH_0_10_Tag0', help="RECO category to package")
  parser.add_option("--exts", dest='exts', default='', help="Comma separate list of extensions")
  parser.add_option("--outputExt", dest='outputExt', default='packaged', help="Output extension")
  parser.add_option("--massPoints", dest='massPoints', default='120,125,130', help="Comma separated list of mass points")
  parser.add_option("--mergeYears", dest='mergeYears', default=False, action="store_true", help="Merge specified categories across years")
  parser.add_option("--year", dest="year", default="2016", help="If not merging, then specify year for output file name")
  return parser.parse_args()
(opt,args) = get_options()

def rooiter(x):
  iter = x.iterator()
  ret = iter.Next()
  while ret:
    yield ret
    ret = iter.Next()

  
  # Extract all files to be merged
fNames = {}
for ext in opt.exts.split(","):
  pattern = "outdir_%s/signalFit/output/CMS-HGG_sigfit_%s_*_%s.root"%(ext,ext,opt.cat)
  fNames[ext] = glob.glob(pattern)
  print(" --> [INFO] Searching for files with pattern: %s"%pattern)
  if len(fNames[ext]) == 0:
    print(" --> [WARNING] No files found for ext='%s', cat='%s'"%(ext,opt.cat))
  else:
    print(" --> [INFO] Found %d file(s) for ext='%s':"%(len(fNames[ext]),ext))
    for fn in fNames[ext]: print("       %s"%fn)

# Define ouput packaged workspace
print(" --> Packaging output workspaces")
packagedWS = ROOT.RooWorkspace("wsig_13TeV","wsig_13TeV")
packagedWS.imp = getattr(packagedWS,"import")

# Extract merged datasets
data_merged = {}
data_merged_names = []
firstExt = opt.exts.split(",")[0]
if len(fNames[firstExt]) == 0:
  print(" --> [ERROR] Cannot build merged datasets: no input files found for ext='%s', cat='%s'."%(firstExt,opt.cat))
  print(" --> [ERROR] Check that outdir_%s/signalFit/output/ exists and contains files matching CMS-HGG_sigfit_%s_*_%s.root"%(firstExt,firstExt,opt.cat))
  sys.exit(1)

refFile = fNames[firstExt][0]
print(" --> [INFO] Using reference file for dataset templates: %s"%refFile)
refWS = ROOT.TFile(refFile).Get("wsig_13TeV")
if not refWS:
  print(" --> [ERROR] Could not load workspace 'wsig_13TeV' from file: %s"%refFile)
  sys.exit(1)

for mp in opt.massPoints.split(","):
  dataName = "sig_mass_m%s_%s"%(mp,opt.cat)
  print(" --> [INFO] Loading model/dataset '%s' from %s"%(dataName,refFile))
  d = refWS.data(dataName)
  if not d:
    print(" --> [ERROR] Dataset '%s' not found in workspace 'wsig_13TeV' of file %s"%(dataName,refFile))
    sys.exit(1)
  data_merged["m%s"%mp] = d.emptyClone(dataName)
  data_merged_names.append( data_merged["m%s"%mp].GetName() )

for ext, fNames_by_ext in fNames.items():
  for fName in fNames_by_ext:
    fin = ROOT.TFile(fName)
    wsin = fin.Get("wsig_13TeV")
    if not wsin:
      print(" --> [ERROR] Could not load workspace 'wsig_13TeV' from file: %s"%fName)
      continue
    for mp in opt.massPoints.split(","):
      dataName = "sig_mass_m%s_%s"%(mp,opt.cat)
      print(" --> [INFO] Merging dataset '%s' from %s"%(dataName,fName))
      d = wsin.data(dataName)
      if not d:
        print(" --> [ERROR] Dataset '%s' not found in %s, skipping"%(dataName,fName))
        continue
      for i in range(d.numEntries()):
        p = d.get(i)
        w = d.weight()
        data_merged["m%s"%mp].add(p,w)

for _data in data_merged.values(): packagedWS.imp(_data)
        
# Loop over input signal fit workspaces
for ext, fNames_by_ext in fNames.items():
  for fName in fNames_by_ext:
    fin = ROOT.TFile(fName)
    wsin = fin.Get("wsig_13TeV")
    if not wsin: continue
    allVars, allFunctions, allPdfs = {}, {}, {}
    for _var in rooiter(wsin.allVars()): allVars[_var.GetName()] = _var
    for _func in rooiter(wsin.allFunctions()): allFunctions[_func.GetName()] = _func
    for _pdf in rooiter(wsin.allPdfs()): allPdfs[_pdf.GetName()] = _pdf
    allData = wsin.allData()

    # Import objects into output workspace
    for _varName, _var in allVars.items(): packagedWS.imp(_var,ROOT.RooFit.RecycleConflictNodes(),ROOT.RooFit.Silence())
    for _funcName, _func in allFunctions.items(): packagedWS.imp(_func,ROOT.RooFit.RecycleConflictNodes(),ROOT.RooFit.Silence())
    for _pdfName, _pdf in allPdfs.items(): packagedWS.imp(_pdf,ROOT.RooFit.RecycleConflictNodes(),ROOT.RooFit.Silence())

    for _data in allData:
      # Skip merged datasets
      if _data.GetName() in data_merged_names: continue
      else: packagedWS.imp(_data)

# Save to file
if not os.path.isdir("outdir_%s"%opt.outputExt): os.system("mkdir outdir_%s"%opt.outputExt)
if opt.mergeYears:
  print(" --> Writing to: ./outdir_%s/CMS-HGG_sigfit_%s_%s.root"%(opt.outputExt,opt.outputExt,opt.cat))
  f = ROOT.TFile("./outdir_%s/CMS-HGG_sigfit_%s_%s.root"%(opt.outputExt,opt.outputExt,opt.cat),"RECREATE")
else:
  print(" --> Writing to: ./outdir_%s/CMS-HGG_sigfit_%s_%s_%s.root"%(opt.outputExt,opt.outputExt,opt.cat,opt.year))
  f = ROOT.TFile("./outdir_%s/CMS-HGG_sigfit_%s_%s_%s.root"%(opt.outputExt,opt.outputExt,opt.cat,opt.year),"RECREATE")

packagedWS.Write()
f.Close()
