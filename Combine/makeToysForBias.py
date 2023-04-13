# Script to make toys from inputWS: to be used for bias studies

import os, sys
import re
from optparse import OptionParser
import ROOT
import glob
import time

def run(cmd):
  print "%s\n\n"%cmd
  os.system(cmd)

def get_options():
  parser = OptionParser()
  parser.add_option("--inputWSFile", dest="inputWSFile", default=None, help="Input RooWorkspace file. If loading snapshot then use a post-fit workspace where the option --saveWorkspace was set")
  parser.add_option("--loadSnapshot", dest="loadSnapshot", default=None, help="Load best-fit snapshot name")
  parser.add_option("--ext", dest="ext", default='', help="Extension for saving")
  parser.add_option("--nToys", dest="nToys", default=500, type='int', help="Number of toys")
  parser.add_option("--POIs", dest="POIs", default="r", help="Parameters of interest in fit")
  parser.add_option("--maxExpectSignal", dest="maxExpectSignal", type='int', default=1, help="highest expectSignal parameter to generate toys for bias test")
  parser.add_option("--batch", dest="batch", default="condor", help="Batch system [condor]")
  parser.add_option("--queue", dest="queue", default="workday", help="Change condor queue")
  parser.add_option('--dryRun',dest='dryRun', default=False, action="store_true", help='Dry run')
  return parser.parse_args()
(opt,args) = get_options()

# Create jobs directory
if not os.path.isdir("./Models_%s"%(opt.ext)): os.system("mkdir ./Models_%s"%(opt.ext))
if not os.path.isdir("./Models_%s/toys"%(opt.ext)): os.system("mkdir ./Models_%s/toys"%(opt.ext))
if not os.path.isdir("./Models_%s/toys/jobs"%(opt.ext)): os.system("mkdir ./Models_%s/toys/jobs"%(opt.ext))

# Delete all old jobs
for job in glob.glob("./Models_%s/toys/jobs/sub*.sh"%opt.ext): os.system("rm %s"%job)

# Open workspace and extract best fit mass and signal strength
inputWSFile = "%s/%s"%(os.environ['PWD'],opt.inputWSFile)
f = ROOT.TFile(inputWSFile)
w = f.Get("w")

if opt.loadSnapshot is not None: w.loadSnapshot(opt.loadSnapshot)
poi_bf = {}

for poi in opt.POIs.split(","): poi_bf[poi] = w.var(poi).getVal()
setParamStr = "--setParameters "
setParam0Str = "--setParameters "
for p,v in poi_bf.iteritems():
  setParamStr += "%s=%.3f,"%(p,v)
  setParam0Str += "%s=0,"%p
setParamStr = setParamStr[:-1]
setParam0Str = setParam0Str[:-1]
mh_bf = w.var("MH").getVal()
print opt.maxExpectSignal
if opt.batch == 'condor':
  for ExpSig in range(1,opt.maxExpectSignal+1):
    # Create submission file
    setParamRng = "--setParameterRanges %s=%g,%g"%(opt.POIs.split(",")[0],(ExpSig-100),(ExpSig+100))
    fsub = open("./Models_%s/toys/jobs/sub_toys_%g.sh"%(opt.ext,ExpSig),'w')
    fsub.write("#!/bin/bash\n")
    fsub.write("ulimit -s unlimited\n")
    fsub.write("set -e\n")
    fsub.write("cd %s/src/flashggFinalFit/Combine/Models_%s/toys\n"%(os.environ['CMSSW_BASE'],opt.ext))
    fsub.write("source /cvmfs/cms.cern.ch/cmsset_default.sh\n")
    fsub.write("eval `scramv1 runtime -sh`\n\n")
    fsub.write("ExpSig=$1\n\n")

    # Generate command
    fsub.write("#Generate command\n")
 #  gen_cmd = "combine %s -m %.3f -M GenerateOnly --saveWorkspace --toysNoSystematics --bypassFrequentistFit -t %s %s -s -1 -n _${itoy}_gen_step"%(inputWSFile,mh_bf,opt.nToys,setParamStr)
#    fit_cmd = "combine %s -M MultiDimFit -m 125 --redefineSignalPOIs %s %s --trackParameters %s --freezeParameter MH --saveWorkspace -t %g --toysNoSystematics --expectSignal %s -n _expSignal_${ExpSig}_%gtoysForBias_step --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2"%(inputWSFile,opt.POIs.split(",")[0],setParamRng,opt.POIs.split(",")[0],opt.nToys,ExpSig,opt.nToys)
#    fit_cmd = "combine %s -M MultiDimFit -m 125 --redefineSignalPOIs %s %s --trackParameters %s --freezeParameter MH --saveWorkspace -t %g --toysNoSystematics --expectSignal %s -n _expSignal_${ExpSig}_%gtoysForBias_step --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2"%(inputWSFile,opt.POIs.split(",")[0],setParamRng,opt.POIs.split(",")[0],opt.nToys,ExpSig,opt.nToys)
#ps    gen_cmd = "combine %s -M GenerateOnly --redefineSignalPOIs %s --toysNoSystematics -t %g --expectSignal ${ExpSig} --saveToys -m 125 --freezeParameters MH -n _expSignal_${ExpSig}_%gtoysForBias_step"%(inputWSFile, opt.POIs.split(",")[0], opt.nToys, opt.nToys)
    gen_cmd = "combine %s -M GenerateOnly --redefineSignalPOIs %s --toysNoSystematics --bypassFrequentistFit -t %g --expectSignal ${ExpSig} --saveToys -m 125 --freezeParameters MH -n _expSignal_${ExpSig}_%gtoysForBias_step -s -1"%(inputWSFile, opt.POIs.split(",")[0], opt.nToys, opt.nToys)
    fsub.write("%s\n\n"%gen_cmd)

    fsub.write("#FitDiagnostics command\n")

    fit_cmd = "combine %s -M FitDiagnostics -m 125 --redefineSignalPOIs %s %s --trackParameters %s --toysFile higgsCombine_expSignal_${ExpSig}_%gtoysForBias_step.GenerateOnly.mH125.123456.root  -t %g --freezeParameters MH -n _expSignal_${ExpSig}_%gtoysForBias_step --cminDefaultMinimizerStrategy=0"%(inputWSFile, opt.POIs.split(",")[0], setParamRng, opt.POIs.split(",")[0], opt.nToys, opt.nToys, opt.nToys)

    fsub.write("%s\n\n"%fit_cmd)
    fsub.close()

    fcondor = open("./Models_%s/toys/jobs/sub_toys_%g.sub"%(opt.ext, ExpSig),'w')
#    fcondor.write("\n")
    fcondor.write("universe = vanilla\n")
    fcondor.write("Executable = sub_toys_%g.sh\n"%(ExpSig))
    fcondor.write("Arguments = %s\n"%ExpSig)
    fcondor.write("output                = %s/src/flashggFinalFit/Combine/Models_%s/toys/jobs/sub_toys_%g.$(ClusterId).$(ProcId).out\n"%(os.environ['CMSSW_BASE'],opt.ext, ExpSig))
    fcondor.write("error                 = %s/src/flashggFinalFit/Combine/Models_%s/toys/jobs/sub_toys_%g.$(ClusterId).$(ProcId).err\n"%(os.environ['CMSSW_BASE'],opt.ext, ExpSig))
    fcondor.write("log                   = %s/src/flashggFinalFit/Combine/Models_%s/toys/jobs/sub_toys_%g.$(ClusterId).log\n\n"%(os.environ['CMSSW_BASE'],opt.ext, ExpSig))
    fcondor.write("on_exit_hold = (ExitBySignal == True) || (ExitCode != 0)\n")
    fcondor.write("periodic_release =  (NumJobStarts < 3) && ((CurrentTime - EnteredCurrentStatus) > 600)\n\n")
    fcondor.write("+JobFlavour = \"%s\"\n"%(opt.queue))
    fcondor.write("Queue\n\n")    
    fcondor.close()
    # Submission
    os.system("chmod 775 ./Models_%s/toys/jobs/sub_toys_%g.sh"%(opt.ext, ExpSig))
    print "Submitting condor_submit sub_toys_%g.sub"%(ExpSig)
    if not opt.dryRun: os.system("cd ./Models_%s/toys/jobs; source /cvmfs/cms.cern.ch/cmsset_default.sh; eval `scramv1 runtime -sh`; condor_submit sub_toys_%g.sub; cd ../../.."%(opt.ext,ExpSig))
#    if not opt.dryRun:
#        time.sleep(3) 
#        cmdLine="cd ./Models_%s/toys/jobs;pwd"%(opt.ext)
#        os.system(cmdLine)
#        os.system("condor_submit sub_toys_%g.sub"%(ExpSig))
#        os.system("cd ../../..")
#       cmdLine="cd ./Models_%s/toys/jobs; source /cvmfs/cms.cern.ch/cmsset_default.sh; eval `scramv1 runtime -sh`; condor_submit sub_toys_%g.sub; cd ../../.."%(opt.ext,ExpSig)
#       cmdLine="cd ./Models_%s/toys/jobs; condor_submit sub_toys_%g.sub;"%(opt.ext,ExpSig)
    time.sleep(3)
#    else: print " --> [DRY-RUN] jobs have not been submitted"
