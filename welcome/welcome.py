#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports (Global)
from PyQt4.QtCore import QSettings, QThread, QVariant, SIGNAL
from PyQt4.QtGui import QApplication, QPixmap, QWizard
from time import sleep
import os, sys

# Imports (Custom)
import ui_welcome

HOME = os.getenv("HOME")
PWD = sys.path[0]

CONFIG_ALL = (
  "asoundrc",
  "bash_aliases",
  "jackdrc",
  "lmmsrc.xml",

  "ardour2/ardour.rc",
  "audacity-data/audacity.cfg",
  "bcast/Cinelerra_rc",
  "ccutie/Cinecutie_rc",
  "composite/composite.conf",
  "hydrogen/hydrogen.conf",
  "jost/default.conf",
  "mplayer/config",
  "non-daw/options",
  "non-mixer/options",
  "OOMidi/OOMidi.cfg",
  "openoffice.org/3/user/registry/data/org/openoffice/Office/ExtendedColorScheme.xcu",
  "openoffice.org/3/user/registry/data/org/openoffice/Office/UI.xcu",
  "phasex/phasex.cfg",
  "pulse/client.conf",
  "pulse/daemon.conf",
  "renoise/V2.6.1/Config.xml",
  "renoise/V2.7.0/Config.xml",
  "traverso/Traverso-DAW/Traverso.ini",

  "config/ardour3/ardour.rc",
  "config/audacious/config",
  "config/Clementine/Clementine.conf",
  "config/jack/conf.xml",
  "config/kde.org/libphonon.conf",
  "config/Modartt/Pianoteq36.prefs",
  "config/Modartt/Pianoteq36 PLAY.prefs",
  "config/rncbc.org/QjackCtl.conf",
  "config/rncbc.org/Qsynth.conf",
  "config/rosegardenmusic/Rosegarden.conf",
  "config/vlc/vlcrc",

  "jucetice/BitMangler.conf",
  "jucetice/EQinox.conf",
  "jucetice/Highlife.conf",
  "jucetice/Nekobee.conf",
  "jucetice/Peggy2000.conf",

  "Loomer/Aspect.xml",
  "Loomer/Manifold.xml",
  "Loomer/Resound.xml",
  "Loomer/Sequent.xml",
  "Loomer/Shift.xml",
  "Loomer/Shift2.xml",
  "Loomer/String.xml",

  "kde/env/qt-graphicssystem.sh",
  "kde/share/apps/dolphin/dolphinui.rc",
  "kde/share/config/dolphinrc",
  "kde/share/config/glmatrixrc",
  "kde/share/config/kcmfonts",
  "kde/share/config/kickoffrc",
  "kde/share/config/klipperrc",
  #"kde/share/config/konversationrc",
  "kde/share/config/kscreensaverrc",
  "kde/share/config/ksmserverrc",
  "kde/share/config/kwalletrc",
  "kde/share/config/nepomukserverrc",
)

CONFIG_SMALL = (
  "asoundrc",
  "bash_aliases",
)

CONFIG_THEME = (
  "fonts.conf",
  "gtkrc-2.0-kde4",
  "kderc",

  "qt/qtrc",

  "config/kde.org/systemsettings.conf",
  "config/qtcurve/gtk-icons",
  "config/qtcurve/stylerc",
  "config/qtcurve/windowBorderSizes",
  "config/Trolltech.conf",

  "kde/env/gtk2-engines-qtcurve.rc.sh",
  "kde/share/config/colibrirc",
  "kde/share/config/gtkrc",
  "kde/share/config/gtkrc-2.0",
  "kde/share/config/kcmdisplayrc",
  "kde/share/config/kcminputrc",
  "kde/share/config/kdeglobals",
  "kde/share/config/ksplashrc",
  "kde/share/config/kwinrc",
  "kde/share/config/oxygenrc",
  "kde/share/config/plasmarc",
)

def create_folder_for_file(sfile):
  if ("/" in sfile):
    spath = sfile.rsplit("/",1)[0]
    folder = os.path.join(HOME, "."+spath)
    if not os.path.exists(folder):
      os.system("mkdir -p %s" % (folder))

def do_remove_old_stuff():
  os.system("rm -f '%s/.kde/env/kxstudio-session-start.sh'" % (HOME))

def do_copy_all():
  for sfile in CONFIG_ALL:
    create_folder_for_file(sfile)
    os.system("cp '/usr/share/kxstudio/config/%s' '%s/.%s'" % (sfile, HOME, sfile))

def do_copy_basic():
  for sfile in CONFIG_SMALL:
    create_folder_for_file(sfile)
    os.system("cp '/usr/share/kxstudio/config/%s' '%s/.%s'" % (sfile, HOME, sfile))

  for sfile in CONFIG_ALL:
    create_folder_for_file(sfile)
    if (not os.path.exists(os.path.join(HOME, sfile))):
      os.system("cp '/usr/share/kxstudio/config/%s' '%s/.%s'" % (sfile, HOME, sfile))

def do_copy_theme():
  for sfile in CONFIG_THEME:
    create_folder_for_file(sfile)
    os.system("cp '/usr/share/kxstudio/config/%s' '%s/.%s'" % (sfile, HOME, sfile))

  os.system('gconftool-2 -t str -s /apps/metacity/general/theme "KXStudio"')
  os.system('gconftool-2 -t str -s /apps/metacity/general/button_layout "close,minimize,maximize:menu"')
  os.system('gconftool-2 -t str -s /apps/metacity/general/titlebar_font "DejaVu Sans Bold 8"')
  os.system('gconftool-2 -t str -s /apps/nautilus/preferences/desktop_font "DejaVu Sans 8"')
  os.system('gconftool-2 -t str -s /desktop/gnome/interface/gtk_theme "QtCurve"')
  os.system('gconftool-2 -t str -s /desktop/gnome/interface/icon_theme "Oxygen Mono Dark"')
  os.system('gconftool-2 -t str -s /desktop/gnome/interface/font_name "DejaVu Sans 8"')
  os.system('gconftool-2 -t str -s /desktop/gnome/interface/document_font_name "DejaVu Sans 8"')
  os.system('gconftool-2 -t str -s /desktop/gnome/interface/monospace_font_name "DejaVu Sans Mono 8"')

def do_wine_stuff():
  if (os.path.exists("/usr/bin/wineboot")):
    os.system("wineboot")
    #os.system("sed -i 's/\[drivers32\]/\[drivers32\]\nMSACM.vorbis=vorbis.acm/' ~/.wine/drive_c/windows/system.ini")

    if (os.path.exists("/usr/lib/wine/wineasio.dll.so") or os.path.exists("/usr/lib32/wine/wineasio.dll.so")):
      os.system("regsvr32 wineasio.dll")

    if (os.path.exists("/usr/bin/winetricks")):
      os.system("winetricks fontfix fontsmooth-rgb nocrashdialog winxp sound=jack")

def do_final_stuff():
  os.system('gconftool-2 --type string --set /system/gstreamer/0.10/default/audiosink "pulsesink device=\"jack_out\""')
  os.system('gconftool-2 --type string --set /system/gstreamer/0.10/default/audiosrc "pulsesrc"')
  os.system('gconftool-2 --type string --set /system/gstreamer/0.10/default/chataudiosink "pulsesink device=\"jack_out\""')
  os.system('gconftool-2 --type string --set /system/gstreamer/0.10/default/musicaudiosink "pulsesink device=\"jack_out\""')
  os.system('gconftool-2 --type string --set /system/gstreamer/0.10/default/audiosink_description "Jack"')
  os.system('gconftool-2 --type string --set /system/gstreamer/0.10/default/audiosrc_description "Pulse Audio"')
  os.system('gconftool-2 --type string --set /system/gstreamer/0.10/default/chataudiosink_description "Jack"')
  os.system('gconftool-2 --type string --set /system/gstreamer/0.10/default/musicaudiosink_description "Jack"')

# Separate Thread for Copying Stuff
class CopyStuffThread(QThread):
    def __init__(self, parent=None):
        super(CopyStuffThread, self).__init__(parent)

    def setData(self, _copy, _copy_all, _copy_basic, _copy_theme):
        self._copy = _copy
        self._copy_all = _copy_all
        self._copy_basic = _copy_basic
        self._copy_theme = _copy_theme

    def run(self):
        xself = self.parent()

        # Settings
        self.emit(SIGNAL("setLabelPixmap(int, int)"), 0, 1)
        if (self._copy):
          sleep(1)
          do_remove_old_stuff()
          if (self._copy_all):
            do_copy_all()
          elif (self._copy_basic):
            do_copy_basic()
        self.emit(SIGNAL("setLabelPixmap(int, int)"), 0, 2)

        # Theme
        self.emit(SIGNAL("setLabelPixmap(int, int)"), 1, 1)
        if (self._copy_theme):
          sleep(1)
          do_copy_theme()
        self.emit(SIGNAL("setLabelPixmap(int, int)"), 1, 2)

        # Wine
        self.emit(SIGNAL("setLabelPixmap(int, int)"), 2, 1)
        if (self._copy):
          do_wine_stuff()
        self.emit(SIGNAL("setLabelPixmap(int, int)"), 2, 2)

        # Final
        self.emit(SIGNAL("setLabelPixmap(int, int)"), 3, 1)
        if (self._copy):
          sleep(1)
          do_final_stuff()
        self.emit(SIGNAL("setLabelPixmap(int, int)"), 3, 2)

# Main Window
class WelcomeW(QWizard, ui_welcome.Ui_WelcomeW):
    def __init__(self, parent=None):
        super(WelcomeW, self).__init__(parent)
        self.setupUi(self)

        self.loadSettings()
        self.previous_page = -1

        self.pixmap_kxstudio = QPixmap(os.path.join(PWD, "icons", "start-here-kxstudio.png"))
        self.pixmap_queque = QPixmap(os.path.join(PWD, "icons", "go-next-view.png"))
        self.pixmap_process = QPixmap(os.path.join(PWD, "icons", "arrow-right.png"))
        self.pixmap_done = QPixmap(os.path.join(PWD, "icons", "dialog-ok-apply.png"))

        self.l_ico_kxstudio.setPixmap(self.pixmap_kxstudio)
        self.l_ico_settings.setPixmap(self.pixmap_queque)
        self.l_ico_theme.setPixmap(self.pixmap_queque)
        self.l_ico_wine.setPixmap(self.pixmap_queque)
        self.l_ico_final.setPixmap(self.pixmap_queque)
        self.progressBar.setValue(0)

        self.copyStuffThread = CopyStuffThread(self)

        self.connect(self, SIGNAL("finished(int)"), self.saveSettings)
        self.connect(self, SIGNAL("currentIdChanged(int)"), self.changedPage)
        self.connect(self.copyStuffThread, SIGNAL("setLabelPixmap(int, int)"), self.setLabelPixmap)
        self.connect(self.copyStuffThread, SIGNAL("finished()"), self.copyStuffFinished)

    def changedPage(self, page):
        # Initial page
        if (self.previous_page == -1 and page == 0):
          pass

        # Process Stuff
        elif (self.previous_page == 0 and page == 1):
          self.button(QWizard.BackButton).setEnabled(False)
          self.button(QWizard.NextButton).setEnabled(False)
          self.button(QWizard.CancelButton).setEnabled(False)
          self.progressBar.setValue(0)
          self.copyStuffThread.setData(self.group_settings.isChecked(), self.rb_all.isChecked(), self.rb_basic.isChecked(), self.group_theme.isChecked())
          self.copyStuffThread.start()

        # Final page
        elif (self.previous_page == 1 and page == 2):
          self.button(QWizard.BackButton).setEnabled(False)
          self.button(QWizard.CancelButton).setEnabled(False)

        self.previous_page = page

    def setLabelPixmap(self, label_id, pixmap_id):
        if (label_id == 0):
          label = self.l_ico_settings
          self.progressBar.setValue(0)
        elif (label_id == 1):
          label = self.l_ico_theme
          self.progressBar.setValue(25)
        elif (label_id == 2):
          label = self.l_ico_wine
          self.progressBar.setValue(50)
        elif (label_id == 3):
          label = self.l_ico_final
          self.progressBar.setValue(75)

        if (pixmap_id == 0):
          label.setPixmap(self.pixmap_queque)
        elif (pixmap_id == 1):
          label.setPixmap(self.pixmap_process)
        elif (pixmap_id == 2):
          label.setPixmap(self.pixmap_done)

    def copyStuffFinished(self):
        self.progressBar.setValue(100)
        self.button(QWizard.NextButton).setEnabled(True)
        self.button(QWizard.CancelButton).setEnabled(True)

    def saveSettings(self):
        settings.setValue("Geometry", QVariant(self.saveGeometry()))
        settings.setValue("FirstRun", False)

    def loadSettings(self):
        self.restoreGeometry(settings.value("Geometry").toByteArray())

    def closeEvent(self, event):
        self.saveSettings()
        QWizard.closeEvent(self, event)

#--------------- main ------------------
if __name__ == '__main__':

    # App initialization
    app = QApplication(sys.argv)
    app.setApplicationName("Welcome")
    app.setOrganizationName("KXStudio")
    #app.setWindowIcon(QIcon(":/48x48/welcome.png"))

    settings = QSettings("KXStudio", "Welcome")

    run = True
    if (app.arguments().count() > 1):
      if (app.arguments()[1] == "--first-run"):
        run = settings.value("FirstRun", True).toBool()

    # Show GUI
    if (run):
      gui = WelcomeW()
      gui.show()
      ret = app.exec_()
    else:
      ret = 0

    # Exit properly
    sys.exit(ret)
