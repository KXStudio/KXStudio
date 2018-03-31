#!/bin/bash

if [ -f $HOME/.gtkrc-2.0-kde4 ]; then
  export GTK2_RC_FILES=$HOME/.gtkrc-2.0-kde4
fi
