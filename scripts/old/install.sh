#!/bin/bash

# Check if KXStudio is already installed
if [ "`dpkg -l | grep kxstudio-desktop-full`" != "" ]; then
echo "KXStudio is already installed!"
exit
fi

# Check for root
if [ $UID != 0 ]; then
echo "This script must be runned as root: 'sudo $0'"
exit
fi

# Check if the PPA is already enabled
if [ ! -f /etc/apt/sources.list.d/falk-t-j-kxstudio-lucid.list ]; then
echo "
Installing KXStudio PPA..."
sleep 1
sudo su root -c 'echo "deb http://ppa.launchpad.net/falk-t-j/kxstudio/ubuntu lucid main" > /etc/apt/sources.list.d/falk-t-j-kxstudio-lucid.list'
echo "Done!"
sleep 1
fi

# Check if the repos are already installed
if [ "`dpkg -l | grep kxstudio-repos`" == "" ]; then
echo "
Installing KXStudio Repositories..."
sudo apt-get update > /dev/null
sudo apt-get install kxstudio-repos -y --force-yes --allow-unauthenticated > /dev/null
echo "Done!"
sleep 1
fi

# Prevent unwanted packages for being downloaded/installed (300Mb of 'junk')
echo "
Preparing installation..."
sudo apt-get update > /dev/null
sudo apt-get install kxstudio-meta-conflict -y --force-yes > /dev/null
echo "Done!"
sleep 1

# Prepare user for what is about to happen...
echo "
Ready to install?"
sleep 3
sudo apt-get install kxstudio-desktop-full kxstudio-meta-conflict -m

# Error while installing ?
if [ "`dpkg -l | grep kxstudio-desktop-full`" == "" ]; then
echo "An error ocurred while installing KXStudio. Please check the errors on the screen and try to fix them.
When done, run this script again"
exit
else
echo "Done!"
sleep 1
fi

# Fix Post-Installation bug
if [ ! -f $HOME/.kde/share/config/kdeglobals ];
  sudo rm -rf $HOME/.kde
fi

# Remove conflicts and clean-up
echo "
Cleaning up..."
sudo apt-get remove kxstudio-meta-conflict -y --force-yes > /dev/null
sudo apt-get autoremove -y --force-yes > /dev/null
sudo apt-get clean
echo "Done!"
sleep 2

# The End
echo "
Installation is now complete!
Run 'sudo reboot' to restart your system"
