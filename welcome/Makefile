# simple make file just to generate UI file

all: ui_welcome.py

ui_welcome.py: welcome.ui
	pyuic5 -o ui_welcome.py welcome.ui

clean:
	rm -f ui_welcome.py
