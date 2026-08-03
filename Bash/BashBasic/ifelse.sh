#!/bin/bash 

Name=$(zenity --entry  --title="question"  --text="what is your name")

if [ "$Name" == "chan" ]; then
   zenity --info --title="oh!your are chankhine i heard alot of thing"
else 
    zenity --warning  --title ="sorry! i don'tknow you"
fi
