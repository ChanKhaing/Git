#!/bin/bash


hello() {
 echo "hello $people ! i am chankhine and nice to meet you"
}

echo "type your name"
read people

if [ $people  == "sithu" ] 
then 
hello
else 
echo "remember who you are"
fi
