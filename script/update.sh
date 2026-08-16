#!/bin/bash

releasefile=/etc/os-release

if grep -iq "Arch" $releasefile
then
echo "your distro is Arch"
sleep 1
sudo pacman -Syu

elif grep -iq "ubuntu" $releasefile || grep -iq "debian" $releasefile
then
echo "your distro is debain"
sleep 1 
sudo apt update
sudo apt dist-upgrade

elif grep -iq  "rhel" $releasefile ||  grep -iq "centos" $releasefile || grep -iq "fedora" $releasefile
then 
echo "your distro is base on redhat"
sleep 1 
# sudo dnf update
sudo dnf upgrade
# sudo dnf distro-syncelse
else
    echo "Unsupported operating system"
    exit 1
fi
