#!/bin/bash

python ___clear-dependencies.py > kxstudio_tmp.txt
cat kxstudio_tmp.txt | sort > kxstudio_new.txt
rm -f kubuntu.txt kxstudio.txt kxstudio_tmp.txt
