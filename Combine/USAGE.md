# Limit calculation and plotting

1. Limit calculation using `./runCombine_all.sh`
```bash
Usage: ./runCombine_all.sh [-n] [-h] [-t] -y YEAR
  -n: dry run, just print the commands to be run for any given flag
  -t: run test scripts
  -y: year
  -h: print this help message
```

2. 1D plots using `python3 makeBrazilPlot.py`
```bash
usage: makeBrazilPlot.py [-h] --csvFile CSVFILE --outDir OUTDIR --mH MH

Used to print brazilian plots of asymptotic limits

optional arguments:
  -h, --help         show this help message and exit
  --csvFile CSVFILE  Name of the XS csv file
  --outDir OUTDIR    Name of the output directory
  --mH MH            Mass of Higgs using during asymptotic limit calculations
```

3. 2D plots using `python3 make2DPlot.py` **TODO**
