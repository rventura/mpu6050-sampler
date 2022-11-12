#!/bin/bash
CALIB=calib-1.dat
OUT="data/record-`date +%Y%m%d-%H%M%S`.txt"
echo "Recording data to $OUT. Press CTRL-C to stop."
./sampler0.py $CALIB >$OUT
# EOF
