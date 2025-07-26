# Running flashggFinalFit

- To run full workflow of flashggFinalFit, use `condorSubmitFullFlow.py` using [run_condorSubmitFullFlow.sh](./run_condorSubmitFullFlow.sh)
- This script is steered by .jinja2 file
- Optimized for Tprime analysis
- Uses different set of script for running actual commands

### Tip & trick

- To see which script are being run, use `python3 condorSubmitFullFlow.py --printOnly` and inspect resulting script
