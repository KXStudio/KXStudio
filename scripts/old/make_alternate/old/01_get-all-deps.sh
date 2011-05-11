#!/bin/bash

rm -f kxstudio.txt kubuntu.txt
touch kxstudio.txt
touch kubuntu.txt
echo "kxstudio-desktop-full kxstudio-desktop kxstudio-meta-all " >> kxstudio.txt
echo "kubuntu-desktop " >> kubuntu.txt

TOP_DEPENDS=`apt-cache depends kxstudio-desktop | grep -e "Depends" -e "Recommends" | awk '{printf$2" "}'`
TOP_DEPENDS+=`apt-cache depends kxstudio-meta-all | grep -e "Depends" -e "Recommends" | awk '{printf$2" "}'`
for i in $TOP_DEPENDS; do
  MID_DEPENDS=`apt-cache depends $i | grep -e "Depends" -e "Recommends" | awk '{printf$2" "}'`
  for j in $MID_DEPENDS; do
    echo $j >> kxstudio.txt
    apt-cache depends $j | grep -e "Depends" -e "Recommends" | awk '{printf$2" "}' >> kxstudio.txt
  done
done

KUBUNTU_DEPENDS+=`apt-cache depends kubuntu-desktop | grep -e "Depends" -e "Recommends" | awk '{printf$2" "}'`
for k in $KUBUNTU_DEPENDS; do
  MID_DEPENDS=`apt-cache depends $k | grep -e "Depends" -e "Recommends" | awk '{printf$2" "}'`
  for m in $MID_DEPENDS; do
    echo $m >> kubuntu.txt
    apt-cache depends $m | grep -e "Depends" -e "Recommends" | awk '{printf$2" "}' >> kubuntu.txt
  done
done
