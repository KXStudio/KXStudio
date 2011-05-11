#!/bin/bash

OLDDIR=`pwd`
DEBS=`cat kxstudio_new.txt | awk '{printf$1" "}'`

rm -rf debs/*
rmdir debs
mkdir -p debs
cd /var/cache/apt/archives/

FINAL=""
for i in $DEBS; do
  FILTER=$i"_*"
  DEB=`find -name "$FILTER" | grep $FILTER | head -n 1 | grep -e "_all" -e "_amd64" -e "_i386"`
  FINAL+=$DEB" "
done

cp $FINAL $OLDDIR/debs/
