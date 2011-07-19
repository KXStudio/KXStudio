#!/bin/bash

cd debs
# rm -rf amd64 i386 all
mkdir -p amd64
mkdir -p i386
mkdir -p all

if [ -f ardour_*_i386.deb ]; then
mv `ls | grep _i386.deb | awk '{printf$1" "}'` i386
fi

if [ -f ardour_*_amd64.deb ]; then
mv `ls | grep _amd64.deb | awk '{printf$1" "}'` amd64
fi

if [ -f kxstudio-artwork_*_all.deb ]; then
mv `ls | grep _all.deb | awk '{printf$1" "}'` all
fi

cd ..

