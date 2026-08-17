#!/bin/bash 


docker ps -a > /dev/null 2>&1 
if [ $? -eq  0 ]
then
echo "docker is running"
else
echo "docker is not running"
fi
 a=$(docker container ls -a | grep ubuntu | awk '{print $NF}'| tail -n 1)
 docker start $a
 b=$(docker container ls -a | grep ubuntu | cut -d " " -f 1 | tail -n 1)
 echo $b
 sleep 1 
 echo "here we go again"
 docker attach $b
