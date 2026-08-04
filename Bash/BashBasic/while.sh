#!/bin/bash

# mynum=1

# while [ $mynum -le 10 ]
# do 
#  echo "my number is $mynum"
#  mynum=$(( $mynum+1 ))
#  sleep 0.5
# #  echo $mynum
# #echo "autually mynum number is reach $11"
# done


while [ -f ~/Desktop/chan.txt ]
do
echo "Time is $(date) The file is exist"
sleep 5

done
echo "time $(date) The file is not exist"

if [ $? -eq 0 ]
then
  echo "process need  restart again  "
  cd ~/Desktop && touch chan.txt
  sleep 3
  echo "create success"
fi



