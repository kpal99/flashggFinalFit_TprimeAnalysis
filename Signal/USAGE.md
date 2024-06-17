## Doing signal modeling

- This is driven by config file, we will make config file on the fly using template and then run RunSignalSripts.py with printOnly
- This will create scripts to be submitted to condor, we will write something to run those script interactively

### Sidequest
  - Running following requires process in `tools/replacementMapy.py` and `tools/XSBRMap.py`
  - writing in `tools/replacementMapy.py` manually
  - For `tools/XSBRMap.py` we have process,xs file as CSV, thus using that generating entries for `tools/XSBRMap.py`
     - See `tools/makeXSBRMap.py` and `tools/template/xsbrmap.txt`

1. fTest
1. signalFit
1. Packaging
1. Plotting

- Find associated shell script in this folder


### Copy plot
- For copying output plots, do `source cp_Plots.sh`
