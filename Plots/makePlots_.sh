#!/bin/bash

RUN=true
PLOTDIR="."

# Get the options passed to the script
while getopts "nhy:s:p:" opt; do
    case $opt in
        n) RUN=false ;;
        y) YEAR=$OPTARG ;;
        s) TPRIMEPROC=$OPTARG ;;
        p) PLOTDIR=$OPTARG ;;
        h) echo "Usage: $0 [-h] [-n] -y YEAR -s TPRIMEPROC -p PLOTDIR"
            echo "  -p: plot directory, default is current directory"
            echo "  -n: dry run, just print the command"
            echo "  -y: year, e.g. 22plus23"
            echo "  -s: signal process, e.g. TprimeM1800Decay10pct"
            echo "  -h: print this help message"
            exit 0 ;;
        \?) exit 1 ;;
    esac
done

if [[ -z "$YEAR" || -z "$TPRIMEPROC" ]]; then
    echo "Error: both -y YEAR and -s TPRIMEPROC are required."
    echo "Use '$0 -h' for help."
    exit 1
fi

cd "$(dirname "$0")" || exit 1

INPUT_WS_FILE="../Combine/Datacard_${TPRIMEPROC}_${YEAR}_woSystB_mu_inclusive.root"
EXT="${TPRIMEPROC}_${YEAR}"

echo python3 makeSplusBModelPlot.py \
    --inputWSFile "$INPUT_WS_FILE" \
    --cats all \
    --ext "$EXT"

if $RUN; then
    python3 makeSplusBModelPlot.py \
        --inputWSFile "$INPUT_WS_FILE" \
        --cats all \
        --ext "$EXT"
fi

mkdir -pv "$PLOTDIR"/SplusBModels
rsync -rtvhl SplusBModels/$EXT "$PLOTDIR"/SplusBModels/
cp -n "$PLOTDIR"/SplusBModels/index.php "$PLOTDIR"/SplusBModels/$EXT
