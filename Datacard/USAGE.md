# Creating datacards

1. Create yield `.pkl` file using `./makeYields_all.sh`
```bash
Usage: ./makeYields_all.sh [-n] [-h] [-t] -d INPUTDIR -y YEAR
  -d: input selection directory
  -n: dry run, just print the commands to be run for any given flag
  -t: run test scripts
  -y: year
  -h: print this help message
```

1. Create datacards using `./makeDatacard_all.sh`
```bash
Usage: ./makeDatacard_all.sh [-n] [-h] [-t] -y YEAR
  -n: dry run, just print the commands to be run for any given flag
  -t: run test scripts
  -y: year
  -h: print this help message
```
