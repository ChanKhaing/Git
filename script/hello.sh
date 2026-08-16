#!bin/bash

echo "hello world"
echo "what is your name"
read name
now=$(date)
echo "un "
sleep 3 
echo "$name,time is $now and i am happy to meet you"
echo "Hey i want  to calculate what you buy"
echo "enter your a value "
read a
echo "enter your amout"
read b
echo "oh!so your cost is "
expr $a \*  $b
