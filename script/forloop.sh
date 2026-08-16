#!/bin/bash

# for myNum in {"a","b","c"}
# do 
# echo $myNum 
# done 

# echo "loop is done"


for a in logfile/*.log
do 
# echo $file
tar -czvf $a.tar.gz $a
done