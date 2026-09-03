#!/bin/bash 
# run.sh - Python ကိုခေါ်မယ်

set -e  # Error ရင် ရပ်မယ်

echo "Starting Python script..."

if [[ -z "$1" ]]  ;then
echo "you should need to type input data with script"
exit 1

else
echo "you can run this script right now"

fi
echo "bingo"
python3 process.py "$1"
