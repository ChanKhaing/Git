#!/bin/bash

#package=htop
# directory=/chankhine
# if [ -d $directory ]
# then
# echo "Directory $directory is exist"
# else 
# echo "Directory $directory is not exist"
# exit 199
# fi

# echo "exit code is $?"

package="chan"
sudo apt install $package >> package_install.log

if [ $? -eq 0 ]
then
echo "The installation of $package was successful"
echo "The new command is avaliable here:"
which "$package"
else
echo "The installation of $package was not successful" >> package_error.log
fi


