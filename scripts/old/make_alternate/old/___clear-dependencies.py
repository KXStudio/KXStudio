#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

kxstudio = open("./kxstudio.txt").read()
kubuntu  = open("./kubuntu.txt").read()

listR    = []
reading  = kxstudio.split()
existing = kubuntu.split()
broken   = [ 'abrowser-branding', 'calf-plugins', 'hydrogen-svn', 'kdenlive-svn', 'kdenlive-svn-data',
             'ladish-git', 'laditools-git', 'libavcodec52', 'libavdevice52', 'libavfilter0', 'libavformat52',
             'libavformat52', 'libpostproc51', 'libswscale0', 'mixxx-beta', 'mixxx-beta-data', 'libavutil49' ]

i = 0
while (i < len(reading)):
  if not "<" in reading[i]:
    if not str(reading[i]) in listR and not str(reading[i]) in kubuntu and not str(reading[i]) in broken:
      print reading[i]
    listR.append(reading[i])
  i += 1
