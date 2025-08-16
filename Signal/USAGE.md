## Doing signal modeling

- This is driven by config file, we will make config file on the fly using template and then run RunSignalSripts.py with printOnly
- This will create scripts to be submitted to condor, we will write something to run those script interactively
1. fTest, `./runfTest_all.sh -h`
```bash
Usage: ./runfTest_all.sh [-n] -d INPUTDIR -y YEAR [-t] [-h] -p PLOTDIR
  -d: input directory
  -y: year
  -n: dry run, just print the commands to be run for any given flag
  -t: test, run for single mass, decay width
  -p: plot directory to sync plots to
  -h: print this help message
```

2. signalFit, `./runSignalFit_all.sh -h`
```bash
Usage: ./runSignalFit_all.sh [-n] -y YEAR [-t] [-h] -p PLOTDIR
  -n: dry run, just print the commands to be run for any given flag
  -y: year
  -t: test, run for single mass, decay width
  -p: plot directory to sync plots to
  -h: print this help message and exit
```

3. Packaging, `./runPackager_all.sh -h`
```bash
Usage: ./runPackager_all.sh [-n] [-r] [-h] -y YEAR
  -n: dry run, just print the commands to be run for any given flag
  -r: run final Scripts which are found in outdir_*
  -t: run test scripts
  -y: year, can also take CSV i.e. '2016,2017,2018' 
  -h: print this help message
```

4. Plotting, this is not required for us `./runPlotter_.sh -h`
```bash
Usage: ./runPlotter_.sh [-n] [-y YEAR] [-h]
  -n: dry run, just print the commands to be run for any given flag
  -y: year, can also take CSV i.e. '2016,2017,2018' 
  -t: test, run for single mass, decay width
  -h: print this help message
```

- Find these shell script in this folder

### Copy plot
- For copying output plots, do `source rsyncPlots.sh`

## Notes
  - Running following requires process in `tools/replacementMapy.py` and `tools/XSBRMap.py`
  - writing in `tools/replacementMapy.py` manually
  - For `tools/XSBRMap.py` we have process,xs file as json, thus using that generating entries for `tools/XSBRMap.py`
    - See `tools/makeXSBRMap.py` and `tools/template/xsbrmap.txt`
