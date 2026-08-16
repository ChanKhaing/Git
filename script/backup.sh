#!/bin/bash

if [ $# -ne 2 ]
then
echo "Usage: backup.sh <source_directory> <target_directory> "
echo "please try again"
echo "exit code 2"
else 
currentdate=$(date +%Y-%m-%d_%H-%M-%S)

# rsync_opt="-avb --backup-dir=$currentdate --delete --dry-run" 
rsync_opt="-avb --backup-dir=$currentdate --delete"
$(which rsync) $rsync_opt $1 $2/current >> back.log
echo "Changing time is $currentdate" >> back.log 
fi