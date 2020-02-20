#!/bin/sh
clear
fuser -k -n tcp 5000
python3 run.py