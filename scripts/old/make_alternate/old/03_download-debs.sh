#!/bin/bash

sudo apt-get clean
sudo apt-get update
sudo apt-get install --reinstall -d --force-yes `cat kxstudio_new.txt | awk '{printf$1" "}'`
