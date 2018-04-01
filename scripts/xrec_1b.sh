#!/bin/bash

export DISPLAY=:2.0
export KWIN_COMPOSE=N
export XDG_RUNTIME_DIR=/run/user/1001
export KDE_FULL_SESSION=true
export XDG_SESSION_DESKTOP=KDE
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_TYPE=x11
export KDE_SESSION_UID=1001
# export KDE_SESSION_VERSION=5
export QT_ACCESSIBILITY=1
export QT_AUTO_SCREEN_SCALE_FACTOR=0

export XCURSOR_SIZE=0
export XCURSOR_THEME=oxy-zion
export XDG_CONFIG_DIRS=/etc/xdg/xdg-/usr/share/xsessions/plasma:/usr/share/kxstudio/menu:/etc/xdg

export XDG_DATA_DIRS=/usr/share//usr/share/xsessions/plasma:/usr/local/share:/usr/share:/var/lib/snapd/desktop
# export XDG_SEAT_PATH=/org/freedesktop/DisplayManager/Seat0
# export XDG_SEAT=seat0
export XDG_SESSION_CLASS=user
# export XDG_SESSION_ID=29
# export XDG_SESSION_PATH=/org/freedesktop/DisplayManager/Session11
export XDG_VTNR=1

# sudo mkdir /run/user/1001
# sudo chmod 700 /run/user/1001
# sudo chown falk:falk /run/user/1001

export $(dbus-launch)

rm -rf /home/falk/.{a,c,g,h,j,k,l,m,w}*
kxstudio-welcome --live-dvd

plasmashell
kwin_x11 &
sleep 3
kwin_x11 --replace
