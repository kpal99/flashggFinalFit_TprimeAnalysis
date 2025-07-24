#!/bin/bash

RUN=true
# get the options passed to the script
while getopts "nhy:d:p:s:" opt;
do
case $opt in
    n) RUN=false;;
    y) YEAR=$OPTARG;;
    d) INPUTDIR=$OPTARG;;
    p) PLOTDIR=$OPTARG;;
    s) TPRIMEPROC=$OPTARG;;
    h) echo "Usage: $0 -y YEAR -d INPUTDIR -p PLOTDIR -s TPRIMEPROC [-h] [-n] [-t]"
       echo "  -h: print this help"
       echo "  -n: dry run, just print the commands to be run for any given flag"
       echo "  -y: year 2016,2017,2018,Combined"
       echo "  -d: input directory"
       echo "  -p: plot directory to sync plots to"
       echo "  -s: signal process to use, TPRIMEPROC"
       exit 0;;
    \?) exit ;;
esac
done

cd $(dirname $0)
echo python3 make_config.py --inputWS $INPUTDIR/$TPRIMEPROC/ws/allData.root --year $YEAR --ext ${TPRIMEPROC}_${YEAR}
echo python3 RunBackgroundScripts.py --inputConfig config/config_"$TPRIMEPROC"_$YEAR.py --mode fTestParallel
echo
if $RUN; then
    python3 make_config.py --inputWS $INPUTDIR/$TPRIMEPROC/ws/allData.root --year $YEAR --ext ${TPRIMEPROC}_${YEAR}
    python3 RunBackgroundScripts.py --inputConfig config/config_"$TPRIMEPROC"_$YEAR.py --mode fTestParallel
    echo   # to add new line after output of above script
fi

if [ $PLOTDIR ]; then
  mkdir -pv $PLOTDIR/${YEAR}/bkgfTest-Data/${TPRIMEPROC}
  rsync -ah --quiet --stats outdir_${TPRIMEPROC}_${YEAR}/bkgfTest-Data/ $PLOTDIR/${YEAR}/bkgfTest-Data/$TPRIMEPROC/
  cp -v $PLOTDIR/index.php $PLOTDIR/${YEAR}/bkgfTest-Data/$TPRIMEPROC
fi
