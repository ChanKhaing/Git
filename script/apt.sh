#!/bin/bash
echo "please write command"
read command
#command="htop"

if command -v $command
then
echo "$command is avliable,let run it"
else
echo  "$command is not avliable,install it"
sleep 1
sudo apt update && sudo apt install $command
fi
echo "got it"
sleep 1
$command
