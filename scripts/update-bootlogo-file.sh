#!/bin/bash

set -e

rm -rf bootlogo-kxstudio
mkdir bootlogo-kxstudio
cp iso-stuff/isolinux/bootlogo .

cd bootlogo-kxstudio
7z x ../bootlogo
cp ../iso-stuff/isolinux/splash.pcx .
cp ../iso-stuff/isolinux/splash.png .
cp ../iso-stuff/isolinux/txt.cfg .
ls | cpio -o > ../bootlogo
cd ..

mv bootlogo iso-stuff/isolinux/
