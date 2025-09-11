import argparse
import datetime
import os
import jinja2
import sys


def condorSubmitFullFlow(args):
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    base_dir = os.path.join(".condor_request", timestamp)
    os.makedirs(base_dir, exist_ok=True)

    # Environment and paths
    current_working = os.getcwd()
    cmssw_base = os.environ["CMSSW_BASE"]

    # Paths
    jobFileBaseName = f"fullFlow_Run2"
    sh_path = os.path.join(base_dir, f"{jobFileBaseName}.sh")
    sub_path = os.path.join(base_dir, f"{jobFileBaseName}.sub")

    masses = args.tprimeMass.split(",")
    decayWidths = args.tprimeDecayWidth.split(",")
    combinations = [(mass, width) for mass in masses for width in decayWidths]

    # Create the job submission file
    with open(sh_path, "w") as sh:
        sh.write("#!/bin/bash\n")
        sh.write(f"cd {current_working}\n")
        sh.write(f"cmsenv\n")
        sh.write(f"source setup.sh\n")

        for idx, (mass, width) in enumerate(combinations):
            sh.write(f"\nif [ $1 -eq {idx} ]; then\n")
            with open("fullFlowRun2.jinja2") as template:
                jinjaOutput = jinja2.Template(template.read()).render(
                    pwd=current_working,
                    finalSelectionDir2016=args.finalSelectionDir2016,
                    finalSelectionDir2017=args.finalSelectionDir2017,
                    finalSelectionDir2018=args.finalSelectionDir2018,
                    finalSelectionDirData=args.finalSelectionDirData,
                    plotsOutputDir=args.plotsOutputDir,
                    TprimeProc=f"TprimeM{mass}Decay{width}pct",
                )
                jinjaOutput = ["    " + line for line in jinjaOutput.split("\n")]
                jinjaOutput = "\n".join(jinjaOutput)
                sh.write(jinjaOutput)
                sh.write("\n")
            sh.write("fi\n")
            sh.write("\n")

        sh.write("echo \"No matching index\"\n")
        sh.write("exit 1\n")

    os.chmod(sh_path, 0o755)
    print(f"Created: {sh_path}")

    with open(sub_path, "w") as sub:
        sub.write(f"executable = {current_working}/{sh_path}\n")
        sub.write("arguments = $(ProcId)\n")
        sub.write(f"output = {jobFileBaseName}.$(ClusterId).$(ProcId).out\n")
        sub.write(f"error = {jobFileBaseName}.$(ClusterId).$(ProcId).err\n")
        sub.write(f"log = {base_dir}/{jobFileBaseName}.$(ClusterId).$(ProcId).log\n")
        sub.write(f"output_destination = {base_dir}\n")
        sub.write(f'+JobFlavour = "{args.jobFlavour}"\n')
        sub.write("on_exit_remove = (ExitBySignal == False) && (ExitCode == 0)\n")
        sub.write("on_exit_hold = (ExitBySignal == True) && (ExitCode != 0)\n")
        sub.write("periodic_release = (NumJobStarts < 3) && ((CurrentTime - EnteredCurrentStatus) > 600)\n")
        sub.write("max_retries = 2\n")
        sub.write("requirements = Machine =!= LastRemoteHost\n")
        sub.write(f"queue {len(combinations)}\n")

    print(f"Created: {sub_path}")

    if not args.printOnly:
        os.system(f"condor_submit {sub_path}")


def main():
    parser = argparse.ArgumentParser(description="submit condor jobs for full flow of flashgg, see .jinja2 file", epilog="")
    parser.add_argument('--finalSelectionDir2016', required=True, help="Final selection directory i.e outputX.6-UL16")
    parser.add_argument('--finalSelectionDir2017', required=True, help="Final selection directory i.e outputX.6-UL17")
    parser.add_argument('--finalSelectionDir2018', required=True, help="Final selection directory i.e outputX.6-UL18")
    parser.add_argument('--finalSelectionDirData', required=True, help="Final selection directory i.e output.6-Run2")
    parser.add_argument('--plotsOutputDir', required=True, help="Output directory for plots")
    parser.add_argument('--tprimeMass', required=True, help="Tprime masses comma separated. Jobs for each mass,decay width combination")
    parser.add_argument('--tprimeDecayWidth', required=True, help="Tprime decay widths comma separated")
    parser.add_argument('--printOnly', action='store_true', help="Do not submit jobs, only create submission files")
    parser.add_argument('--jobFlavour', default='longlunch', help="Condor job flavour")

    args = parser.parse_args(None if sys.argv[1:] else ['--help'])
    condorSubmitFullFlow(args)

if __name__ == "__main__":
    main()
