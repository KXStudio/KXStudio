#!/bin/bash

if [ $1"0" == "0" ]; then
echo "usage: $0 <path-to-KXStudio-scripts-root-folder>"
exit
fi

if [ ! -d $1/make_alternate/debs ]; then
echo "wrong folder!"
exit
fi

cd debs

rm -rf ../../alternate-dvd_amd64/pool/extra/*
rm -rf ../../alternate-dvd_i386/pool/extra/*

FOLDERS="0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v x y z"

for i in $FOLDERS; do
mkdir -p ../../alternate-dvd_amd64/pool/extra/$i/
cp all/$i* ../../alternate-dvd_amd64/pool/extra/$i/
cp amd64/$i* ../../alternate-dvd_amd64/pool/extra/$i/
done

for j in $FOLDERS; do
mkdir -p ../../alternate-dvd_i386/pool/extra/$j/
cp all/$i* ../../alternate-dvd_i386/pool/extra/$i/
cp i386/$i* ../../alternate-dvd_i386/pool/extra/$i/
done

rmdir ../../alternate-dvd_amd64/pool/extra/*
rmdir ../../alternate-dvd_i386/pool/extra/*

cd ..

echo "Ignore all erros and continue"
