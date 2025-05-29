# Creating datacards

1. Create yield `.pkl` file using `./makeYields_.sh`
```bash
Usage: ./makeYields_.sh [-n] [-h] [-t] [ -d INPUTDIR ]
  -d: input selection directory
  -n: dry run, just print the commands to be run for any given flag
  -t: run test scripts
  -h: print this help message
```

1. Create datacards using `./makeDatacard_.sh`
```bash
Usage: ./makeDatacard_.sh [-n] [-h] [-t]
  -n: dry run, just print the commands to be run for any given flag
  -t: run test scripts
  -h: print this help message
```
