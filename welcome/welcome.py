#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ----------------------------------------------
# Imports (Global)

from PyQt5.QtCore import pyqtSignal, QSettings, QTimer, QThread
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMessageBox, QWizard
from subprocess import getoutput
import os, sys

# ----------------------------------------------
# Imports (Custom)

import ui_welcome

# ----------------------------------------------

HOME = os.getenv("HOME")
PWD  = sys.path[0]

CONFIG_DIR       = "/usr/share/kxstudio/config"
CONFIG_THEME_DIR = "/usr/share/kxstudio/config-theme"

ID_GROUP_SETTINGS = 0
ID_GROUP_THEME    = 1
ID_GROUP_WINE     = 2
ID_GROUP_FINAL    = 3

ID_PIXMAP_QUEUE   = 0
ID_PIXMAP_PROCESS = 1
ID_PIXMAP_DONE    = 2

# ----------------------------------------------

CONFIG_SMALL = (
  "bash_aliases",
  "pulse/client.conf",
  "pulse/daemon.conf"
)

CONFIG_ALL = (
  "asoundrc",
  "bash_aliases",
  "jackdrc",
  "lmmsrc.xml",

  "akonadi/akonadiserverrc",
  "audacity-data/audacity.cfg",
  "giada/giada.conf",
  "gimp-2.8/sessionrc",
  "hydrogen/hydrogen.conf",
  "mplayer/config",
  "phasex/phasex.cfg",
  "pulse/client.conf",
  "pulse/daemon.conf",

  "config/audacious/config",
  "config/Cadence/GlobalSettings.conf",
  "config/jack/conf.xml",
  "config/KXStudio/Welcome.conf",
  "config/linuxsampler.org/Qsampler.conf",
  "config/rncbc.org/QjackCtl.conf",
  "config/rncbc.org/Qsynth.conf",
  "config/rosegardenmusic/Rosegarden.conf",
  "config/smplayer/smplayer.ini",
  "config/vlc/vlcrc",

  "config/baloofilerc",
  "config/dolphinrc",
  "config/kded5rc",
  "config/klaunchrc",
  "config/konversationrc",
  "config/krunnerrc",
  "config/ksmserverrc",
  "config/kwalletrc",
  "config/kwinrc",
  "config/systemsettingsrc",
  "config/yakuakerc",

  "config/autostart/akonaditray.desktop",
  "config/autostart/baloo_file.desktop",
  "config/autostart/kactivitymanagerd.desktop",
  "config/autostart/kaddressbookmigrator.desktop",
  "config/autostart/nepomukserver.desktop",
  "config/autostart/org.kde.kmix.desktop",

  "kde/share/config/nepomukserverrc",

  "local/share/kxmlgui5/dolphin/dolphinui.rc",
)

# forced copied
CONFIG_THEME = (
  "audacity-data/audacity.cfg",
  "hydrogen/hydrogen.conf",
  "phasex/phasex.cfg",

  "gtkrc-2.0",
  "config/fontconfig/fonts.conf",
  "config/gtk-3.0/settings.ini",
  "config/linuxsampler.org/Qsampler.conf",
  "config/ntk/theme.prefs",
  "config/rncbc.org/QjackCtl.conf",
  "config/rncbc.org/Qsynth.conf",
  "config/rncbc.org/Qtractor.conf",
  "config/rosegardenmusic/Rosegarden.conf",

  "config/breezerc",
  "config/gtkrc",
  "config/gtkrc-2.0",
  "config/katerc",
  "config/katepartrc",
  "config/kcmdisplayrc",
  "config/kcmfonts",
  "config/kcminputrc",
  "config/kdeglobals",
  "config/kscreenlockerrc",
  "config/ksplashrc",
  "config/kwinrc",
  "config/plasmarc",
  "config/Trolltech.conf",

  "kde/share/config/breezerc",
  "kde/share/config/kdeglobals",
)

CONFIG_THEME_ALL = (
  "config/konversationrc",
  "local/share/applications/defaults.list",
  "local/share/applications/mimeapps.list"
)

# ----------------------------------------------

def create_folder_for_file(sfile):
  if "/" in sfile:
    spath = sfile.rsplit("/",1)[0]
    folder = os.path.join(HOME, ".%s" % (spath))
    if not os.path.exists(folder):
      os.system("mkdir -p %s" % (folder))

def do_copy_all():
  for sfile in CONFIG_ALL:
    create_folder_for_file(sfile)
    os.system("cp '%s/%s' '%s/.%s'" % (CONFIG_DIR, sfile, HOME, sfile))
  if not os.path.exists("/usr/bin/pulseaudio"):
    os.remove("%s/.asoundrc" % (HOME,))

def do_copy_basic():
  for sfile in CONFIG_SMALL:
    create_folder_for_file(sfile)
    os.system("cp '%s/%s' '%s/.%s'" % (CONFIG_DIR, sfile, HOME, sfile))

  for sfile in CONFIG_ALL:
    create_folder_for_file(sfile)
    if not os.path.exists("%s/.%s" % (HOME, sfile)):
      os.system("cp '%s/%s' '%s/.%s'" % (CONFIG_DIR, sfile, HOME, sfile))
  if not os.path.exists("/usr/bin/pulseaudio"):
    os.remove("%s/.asoundrc" % (HOME,))

def do_copy_theme(fontSize, copy_all=False):
  for sfile in CONFIG_THEME:
    create_folder_for_file(sfile)
    os.system("cp '%s/%s' '%s/.%s'" % (CONFIG_THEME_DIR, sfile, HOME, sfile))
    os.system("sed -i s/_X-FONTSIZE-X_/%i/ '%s/.%s'" % (fontSize, HOME, sfile))

  for sfile in CONFIG_THEME_ALL:
    if copy_all or not os.path.exists("%s/.%s" % (HOME, sfile)):
      create_folder_for_file(sfile)
      os.system("cp '%s/%s' '%s/.%s'" % (CONFIG_THEME_DIR, sfile, HOME, sfile))
      os.system("sed -i s/_X-FONTSIZE-X_/%i/ '%s/.%s'" % (fontSize, HOME, sfile))

  #os.system('gconftool-2 -t str -s /apps/metacity/general/theme "KXStudio"')
  os.system('gconftool-2 -t str -s /apps/metacity/general/button_layout "close,minimize,maximize:menu"')
  os.system('gconftool-2 -t str -s /apps/metacity/general/titlebar_font "DejaVu Sans Bold %i"' % fontSize)
  os.system('gconftool-2 -t str -s /apps/nautilus/preferences/desktop_font "DejaVu Sans %i"' % fontSize)
  os.system('gconftool-2 -t str -s /desktop/gnome/interface/gtk_theme "Breeze-Dark"')
  os.system('gconftool-2 -t str -s /desktop/gnome/interface/icon_theme "breeze-dark"')
  os.system('gconftool-2 -t str -s /desktop/gnome/interface/font_name "DejaVu Sans %i"' % fontSize)
  os.system('gconftool-2 -t str -s /desktop/gnome/interface/document_font_name "DejaVu Sans %i"' % fontSize)
  os.system('gconftool-2 -t str -s /desktop/gnome/interface/monospace_font_name "DejaVu Sans Mono %i"' % fontSize)
  os.system('gconftool-2 -t bool -s /desktop/gnome/interface/buttons_have_icons true')
  os.system('gconftool-2 -t bool -s /desktop/gnome/interface/menus_have_icons true')

  # TESTING
  return

  foxFolders = getoutput("find %s/.mozilla/firefox/*.default/chrome/ -type d" % HOME).strip().split("\n")
  foxFolders.sort()
  if len(foxFolders) >= 1 and os.path.exists(foxFolders[0]):
    foxFolder = foxFolders[0]
    os.system('cp "%s/mozilla/firefox/default/chrome/userContent.css" "%s"' % (CONFIG_THEME_DIR, foxFolder))

def do_wine_stuff():
  return

  if not os.path.exists("/usr/bin/wineboot"):
    return

  os.system("wineboot")

  if os.path.exists("/usr/lib/i386-linux-gnu/wine/wineasio.dll.so"):
    os.system("regsvr32 wineasio.dll")

  if os.path.exists("/usr/lib/x86_64-linux-gnu/wine/wineasio.dll.so"):
    os.system("wine64 regsvr32 wineasio.dll")

  if os.path.exists("/usr/bin/winetricks"):
    os.system("winetricks fontfix fontsmooth-rgb nocrashdialog winxp")

def do_final_stuff():
  os.system('gconftool-2 --type string --set /system/gstreamer/0.10/default/audiosink_description "Jack"')
  os.system('gconftool-2 --type string --set /system/gstreamer/0.10/default/chataudiosink_description "Jack"')
  os.system('gconftool-2 --type string --set /system/gstreamer/0.10/default/musicaudiosink_description "Jack"')

  os.system('gconftool-2 --type string --set /system/gstreamer/1.0/default/audiosink_description "Jack"')
  os.system('gconftool-2 --type string --set /system/gstreamer/1.0/default/chataudiosink_description "Jack"')
  os.system('gconftool-2 --type string --set /system/gstreamer/1.0/default/musicaudiosink_description "Jack"')

def do_live_stuff():
  # FIXME
  desktopDir   = os.path.join(HOME, "Desktop")
  kxstudioDocs = "/usr/share/kxstudio/docs"
  ubiquityFile = "/usr/share/applications/kde4/ubiquity-kdeui.desktop"

  if not os.path.exists(desktopDir):
    os.mkdir(desktopDir)

  if os.path.exists(kxstudioDocs):
    os.system("ln -s '%s' '%s'" % (kxstudioDocs, os.path.join(desktopDir, "Docs")))

  if os.path.exists(ubiquityFile):
    os.system("cp '%s' '%s'" % (ubiquityFile, desktopDir))

# ----------------------------------------------

# Separate Thread for Copying Stuff
class CopyStuffThread(QThread):
    setLabelPixmap = pyqtSignal(int, int)

    def __init__(self, parent=None):
        super(CopyStuffThread, self).__init__(parent)

        self._copy = False
        self._copy_all = False
        self._copy_basic = False
        self._copy_theme = False
        self._font_size  = 8

    def setData(self, _font_size, _copy, _copy_all, _copy_basic, _copy_theme):
        self._copy = _copy
        self._copy_all = _copy_all
        self._copy_basic = _copy_basic
        self._copy_theme = _copy_theme
        self._font_size  = _font_size

    def run(self):
        # Settings
        self.setLabelPixmap.emit(ID_GROUP_SETTINGS, ID_PIXMAP_PROCESS)
        if self._copy:
          if self._copy_all:
            do_copy_all()
          elif self._copy_basic:
            do_copy_basic()
        self.setLabelPixmap.emit(ID_GROUP_SETTINGS, ID_PIXMAP_DONE)

        # Theme
        self.setLabelPixmap.emit(ID_GROUP_THEME, ID_PIXMAP_PROCESS)
        if self._copy_theme:
          do_copy_theme(self._font_size)
        self.setLabelPixmap.emit(ID_GROUP_THEME, ID_PIXMAP_DONE)

        # Wine
        self.setLabelPixmap.emit(ID_GROUP_WINE, ID_PIXMAP_PROCESS)
        if self._copy:
          do_wine_stuff()
        self.setLabelPixmap.emit(ID_GROUP_WINE, ID_PIXMAP_DONE)

        # Final
        self.setLabelPixmap.emit(ID_GROUP_FINAL, ID_PIXMAP_PROCESS)
        if self._copy:
          do_final_stuff()
        self.setLabelPixmap.emit(ID_GROUP_FINAL, ID_PIXMAP_DONE)

# Main Window
class WelcomeW(QWizard, ui_welcome.Ui_WelcomeW):
    def __init__(self, firstRun, parent=None):
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

        self.setWindowIcon(QIcon.fromTheme("start-here-kxstudio", QIcon(self.pixmap_kxstudio)))

        self.copyStuffThread = CopyStuffThread(self)

        self.finished.connect(self.saveSettings)
        self.currentIdChanged.connect(self.pageChanged)
        self.group_settings.clicked.connect(self.checkNext)
        self.rb_basic.clicked.connect(self.enableNext)
        self.rb_all.clicked.connect(self.enableNext)
        self.b_screenshot.clicked.connect(self.showScreenshot)
        self.copyStuffThread.setLabelPixmap.connect(self.setLabelPixmap)
        self.copyStuffThread.finished.connect(self.copyStuffFinished)

        if not os.path.exists("/usr/share/plasma/look-and-feel/org.linuxaudio.kxstudio.desktop/metadata.desktop"):
          self.group_theme.setChecked(False)
          self.group_theme.setEnabled(False)

        if firstRun:
          self.label_7.setVisible(False)

        QTimer.singleShot(0, self.disableNext)

    def checkNext(self, clicked):
        if clicked:
            self.button(QWizard.NextButton).setEnabled(self.rb_basic.isChecked() or self.rb_all.isChecked())
        else:
            self.button(QWizard.NextButton).setEnabled(True)

    def disableNext(self):
        self.button(QWizard.NextButton).setEnabled(False)

    def enableNext(self):
        self.button(QWizard.NextButton).setEnabled(True)

    def showScreenshot(self):
        box = QMessageBox(self)
        box.setIconPixmap(QPixmap(os.path.join(PWD, "icons", "screenshot.png")))
        box.setWindowTitle(self.tr("Welcome to KXStudio - Screenshot"))
        box.exec_()

    def pageChanged(self, page):
        # Initial page
        if self.previous_page == -1 and page == 0:
          pass

        # Process Stuff
        elif self.previous_page == 0 and page == 1:
          self.button(QWizard.BackButton).setEnabled(False)
          self.button(QWizard.NextButton).setEnabled(False)
          self.button(QWizard.CancelButton).setEnabled(False)
          self.progressBar.setValue(0)

          if self.group_settings.isChecked():
            self.copyStuffThread.setData(self.sb_fontSize.value(), self.group_settings.isChecked(), self.rb_all.isChecked(), self.rb_basic.isChecked(), self.group_theme.isChecked())
            self.copyStuffThread.start()
          else:
            self.previous_page = page
            self.label_7.setVisible(False)
            self.label_8.setVisible(False)
            self.label_11.setVisible(False)
            self.next()
            return

        # Final page
        elif self.previous_page == 1 and page == 2:
          self.button(QWizard.BackButton).setEnabled(False)
          self.button(QWizard.CancelButton).setEnabled(False)

        self.previous_page = page

    def setLabelPixmap(self, group_id, pixmap_id):
        label = None

        if group_id == ID_GROUP_SETTINGS:
          label = self.l_ico_settings
          self.progressBar.setValue(0)
        elif group_id == ID_GROUP_THEME:
          label = self.l_ico_theme
          self.progressBar.setValue(25)
        elif group_id == ID_GROUP_WINE:
          label = self.l_ico_wine
          self.progressBar.setValue(50)
        elif group_id == ID_GROUP_FINAL:
          label = self.l_ico_final
          self.progressBar.setValue(75)
        else:
          return

        if pixmap_id == ID_PIXMAP_QUEUE:
          label.setPixmap(self.pixmap_queque)
        elif pixmap_id == ID_PIXMAP_PROCESS:
          label.setPixmap(self.pixmap_process)
        elif pixmap_id == ID_PIXMAP_DONE:
          label.setPixmap(self.pixmap_done)

    def copyStuffFinished(self):
        self.progressBar.setValue(100)
        self.button(QWizard.NextButton).setEnabled(True)
        self.button(QWizard.CancelButton).setEnabled(True)

    def saveSettings(self):
        settings.setValue("Geometry", self.saveGeometry())
        settings.setValue("FirstRun", False)

    def loadSettings(self):
        self.restoreGeometry(settings.value("Geometry", b""))

    def closeEvent(self, event):
        self.saveSettings()
        QWizard.closeEvent(self, event)

#--------------- main ------------------
if __name__ == '__main__':

    # Live-DVD usage
    if "--live-dvd" in sys.argv:
      do_copy_all()
      do_copy_theme(8, True)
      #do_wine_stuff()
      do_final_stuff()
      do_live_stuff()
      sys.exit(0)

    # App initialization
    app = QApplication(sys.argv)
    app.setApplicationName("Welcome")
    app.setOrganizationName("KXStudio")

    settings = QSettings("KXStudio", "Welcome")

    run = True
    firstRun = False
    fullscreen = False

    if "--first-run" in app.arguments():
      firstRun = settings.value("FirstRun", True, type=bool)
      run = firstRun
    if "--fullscreen" in app.arguments():
      fullscreen = True

    # Show GUI
    if run:
      gui = WelcomeW(firstRun)
      gui.show()
      app.exec_()

    # Always exit cleanly
    sys.exit(0)
