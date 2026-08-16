#!/bin/bash

#you should write command full path and this is best pratice and 
#narrow security risk remember some destory script can name same your command


path=/usr/bin

$path/echo "hello try again bro time is $($path/date)"
$path/echo "hello try again bro time is $($path/date)"  >> /home/chan/Desktop/script/daily.log

echo "hello"