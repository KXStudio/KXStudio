#!/usr/bin/make -f

DESTDIR =

all:

clean:

install:
	# Make directories
	install -d $(DESTDIR)/etc/X11/Xsession.d/
	install -d $(DESTDIR)/etc/xdg/menus/applications-merged/
	install -d $(DESTDIR)/usr/share/desktop-directories/
	install -d $(DESTDIR)/usr/share/kxstudio/menu/menus/
	# Install files
	install -m 644 26kxstudio-menu $(DESTDIR)/etc/X11/Xsession.d/
	install -m 644 kxstudio-multimedia.menu $(DESTDIR)/etc/xdg/menus/applications-merged/
	install -m 644 *.directory $(DESTDIR)/usr/share/desktop-directories/
	install -m 644 applications.menu $(DESTDIR)/usr/share/kxstudio/menu/menus/
	install -m 644 xfce-applications.menu $(DESTDIR)/usr/share/kxstudio/menu/menus/
