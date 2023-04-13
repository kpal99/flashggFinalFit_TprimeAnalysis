# Script to make GoF from inputWS: to be used for bias studies

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
if not os.path.isdir("./Models_%s/GoF"%(opt.ext)): os.system("mkdir ./Models_%s/GoF"%(opt.ext))
if not os.path.isdir("./Models_%s/GoF/jobs"%(opt.ext)): os.system("mkdir ./Models_%s/GoF/jobs"%(opt.ext))

# Delete all old jobs
for job in glob.glob("./Models_%s/GoF/jobs/sub*.sh"%opt.ext): os.system("rm %s"%job)

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
#  for ExpSig in range(1,opt.maxExpectSignal+1):
    # Create submission file
    fsub = open("./Models_%s/GoF/jobs/sub_GoF.sh"%(opt.ext),'w')
    fsub.write("#!/bin/bash\n")
    fsub.write("ulimit -s unlimited\n")
    fsub.write("set -e\n")
    fsub.write("cd %s/src/flashggFinalFit/Combine/Models_%s/GoF\n"%(os.environ['CMSSW_BASE'],opt.ext))
    fsub.write("source /cvmfs/cms.cern.ch/cmsset_default.sh\n")
    fsub.write("eval `scramv1 runtime -sh`\n\n")
#    fsub.write("ExpSig=$1\n\n")

    # Generate command
    fsub.write("#Generate command\n")
#ps    gen_cmd = "combine %s -M GenerateOnly --redefineSignalPOIs %s --toysNoSystematics --bypassFrequentistFit -t %g --expectSignal ${ExpSig} --saveToys -m 125 --freezeParameters MH -n _expSignal_${ExpSig}_%gtoysForBias_step -s -1"%(inputWSFile, opt.POIs.split(",")[0], opt.nToys, opt.nToys)
    GoF_cmd = "combine -M GoodnessOfFit -d %s --algo=saturated --saveWorkspace --toysFrequentist --bypassFrequentistFit -t %g --expectSignal 1 -m 125 --freezeParameter MH -n _GoFtest_For%gtoys"%(inputWSFile,opt.nToys,opt.nToys)
    fsub.write("%s\n\n"%GoF_cmd)
    GoFdata_cmd = "combine -M GoodnessOfFit --algo=saturated -d %s -m 125 --freezeParameter MH -n _GoFtest_ForData"%(inputWSFile)
    fsub.write("%s\n\n"%GoFdata_cmd)
    fsub.close()

    fcondor = open("./Models_%s/GoF/jobs/sub_GoF.sub"%(opt.ext),'w')
#    fcondor.write("\n")
    fcondor.write("universe = vanilla\n")
    fcondor.write("Executable = sub_GoF.sh\n")
#    fcondor.write("Arguments = %s\n"%ExpSig)
    fcondor.write("output                = %s/src/flashggFinalFit/Combine/Models_%s/GoF/jobs/sub_GoF.$(ClusterId).$(ProcId).out\n"%(os.environ['CMSSW_BASE'],opt.ext))
    fcondor.write("error                 = %s/src/flashggFinalFit/Combine/Models_%s/GoF/jobs/sub_GoF.$(ClusterId).$(ProcId).err\n"%(os.environ['CMSSW_BASE'],opt.ext))
    fcondor.write("log                   = %s/src/flashggFinalFit/Combine/Models_%s/GoF/jobs/sub_GoF.$(ClusterId).log\n\n"%(os.environ['CMSSW_BASE'],opt.ext))
    fcondor.write("on_exit_hold = (ExitBySignal == True) || (ExitCode != 0)\n")
    fcondor.write("periodic_release =  (NumJobStarts < 3) && ((CurrentTime - EnteredCurrentStatus) > 600)\n\n")
    fcondor.write("+JobFlavour = \"%s\"\n"%(opt.queue))
    fcondor.write("Queue\n\n")    
    fcondor.close()
    # Submission
    os.system("chmod 775 ./Models_%s/GoF/jobs/sub_GoF.sh"%(opt.ext))
    print "Submitting condor_submit sub_GoF.sub"
    if not opt.dryRun: os.system("cd ./Models_%s/GoF/jobs; source /cvmfs/cms.cern.ch/cmsset_default.sh; eval `scramv1 runtime -sh`; condor_submit sub_GoF.sub; cd ../../.."%(opt.ext))
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
