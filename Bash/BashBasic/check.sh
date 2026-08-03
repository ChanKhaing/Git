#!/bin/bash

echo "want to find and type"
path="$HOME/Desktop"

read file

if [[ -f "$path/$file" ]] 
then
echo "The file is exist"
sleep 1
cat "$path/$file"

elif [ -d ~/Desktop/"$file" ]
then
echo "The folder is exist "
sleep 2 
ls ~/Desktop/"$file"
else 
echo "you type $file and this is not exist"
fi 
