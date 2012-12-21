#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports (Global)
from PyQt4.QtCore import QSettings, QThread, SIGNAL
from PyQt4.QtGui import QApplication, QIcon, QMessageBox, QPixmap, QWizard
from subprocess import getoutput
from time import sleep
import os, sys

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

ID_PIXMAP_QUEQUE  = 0
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
  "bcast/Cinelerra_rc",
  "ccutie/Cinecutie_rc",
  "hydrogen/hydrogen.conf",
  "Loomer/Aspect.xml",
  "Loomer/Manifold.xml",
  "Loomer/Resound.xml",
  "Loomer/Sequent.xml",
  "Loomer/Shift2.xml",
  "Loomer/String.xml",
  "mplayer/config",
  "pulse/client.conf",
  "pulse/daemon.conf",
  "renoise/V2.8.0/Config.xml",
  "traverso/Traverso-DAW/Traverso.ini",

  "config/audacious/config",
  "config/Cadence/GlobalSettings.conf",
  "config/Clementine/Clementine.conf",
  "config/jack/conf.xml",
  "config/linuxsampler.org/Qsampler.conf",
  "config/Modartt/Pianoteq36 PLAY.prefs",
  "config/Modartt/Pianoteq40.prefs",
  "config/rncbc.org/QjackCtl.conf",
  "config/rncbc.org/Qsynth.conf",
  "config/rosegardenmusic/Rosegarden.conf",
  "config/smplayer/smplayer.ini",
  "config/vlc/vlcrc",
  "config/xfce4/xinitrc",

  "kde/env/qt-graphicssystem.sh",
  "kde/share/apps/dolphin/dolphinui.rc",
  "kde/share/autostart/akonaditray.desktop",
  "kde/share/autostart/kactivitymanagerd.desktop",
  "kde/share/autostart/kaddressbookmigrator.desktop",
  "kde/share/autostart/nepomukserver.desktop",
  "kde/share/config/dolphinrc",
  "kde/share/config/kdedrc",
  "kde/share/config/kdeglobals",
  "kde/share/config/kickoffrc",
  "kde/share/config/klaunchrc",
  "kde/share/config/klipperrc",
  "kde/share/config/knotifyrc",
  "kde/share/config/konversationrc",
  "kde/share/config/krunnerrc",
  "kde/share/config/ksmserverrc",
  "kde/share/config/kwalletrc",
  "kde/share/config/kwinrc",
  "kde/share/config/nepomukserverrc",
  "kde/share/config/oxygenrc",
  "kde/share/config/taskmanagerrulesrc",
  "kde/share/config/yakuakerc",

  "local/share/defaults.list",
  "local/share/mimeapps.list"
)

CONFIG_THEME = (
  "fonts.conf",
  "gtkrc-2.0-kxstudio",
  "kderc",

  "composite/composite.conf",
  "hydrogen/hydrogen.conf",
  "mozilla/firefox/default/chrome/userContent.css",
  "non-daw/options",
  "non-mixer/options",
  "phasex/phasex.cfg",
  "qt/qtrc",
  "traverso/Traverso-DAW/Traverso.ini",

  "config/gtk-3.0/settings.ini",
  "config/kde.org/systemsettings.conf",
  "config/Nokia/QtCreator.ini",
  "config/qtcurve/gtk-icons",
  "config/qtcurve/stylerc",
  "config/qtcurve/windowBorderSizes",
  "config/rncbc.org/QjackCtl.conf",
  "config/rncbc.org/Qsynth.conf",
  "config/rosegardenmusic/Rosegarden.conf",
  "config/xfce4/xinitrc",
  "config/xfce4/xfconf/xfce-perchannel-xml/xfwm4.xml",
  "config/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml",
  "config/Trolltech.conf",

  "kde/env/colibri.sh",
  "kde/env/gtk2-engines-qtcurve.rc.sh",
  "kde/share/config/colibrirc",
  "kde/share/config/glmatrixrc",
  "kde/share/config/gtkrc",
  "kde/share/config/gtkrc-2.0",
  "kde/share/config/kateschemarc",
  "kde/share/config/katesyntaxhighlightingrc",
  "kde/share/config/kcmdisplayrc",
  "kde/share/config/kcmfonts",
  "kde/share/config/kcminputrc",
  "kde/share/config/kdeglobals",
  "kde/share/config/kscreensaverrc",
  "kde/share/config/ksplashrc",
  "kde/share/config/kwinrc",
  "kde/share/config/kwinqtcurverc",
  "kde/share/config/oxygenrc",
  "kde/share/config/plasmarc"
)

CONFIG_THEME_ALL = (
  "ardour2/ardour.rc",
  "config/ardour3/ardour.rc",
  "kde/share/config/konversationrc"
)

# ----------------------------------------------

def create_folder_for_file(sfile):
  if ("/" in sfile):
    spath = sfile.rsplit("/",1)[0]
    folder = os.path.join(HOME, ".%s" % (spath))
    if not os.path.exists(folder):
      os.system("mkdir -p %s" % (folder))

def do_copy_all():
  for sfile in CONFIG_ALL:
    create_folder_for_file(sfile)
    os.system("cp '%s/%s' '%s/.%s'" % (CONFIG_DIR, sfile, HOME, sfile))

def do_copy_basic():
  for sfile in CONFIG_SMALL:
    create_folder_for_file(sfile)
    os.system("cp '%s/%s' '%s/.%s'" % (CONFIG_DIR, sfile, HOME, sfile))

  for sfile in CONFIG_ALL:
    create_folder_for_file(sfile)
    if (not os.path.exists(os.path.join(HOME, sfile))):
      os.system("cp '%s/%s' '%s/.%s'" % (CONFIG_DIR, sfile, HOME, sfile))

def do_copy_theme(fontSize, copy_all=False):
  for sfile in CONFIG_THEME:
    create_folder_for_file(sfile)
    os.system("cp '%s/%s' '%s/.%s'" % (CONFIG_THEME_DIR, sfile, HOME, sfile))
    os.system("sed -i s/_X-FONTSIZE-X_/%i/ '%s/.%s'" % (fontSize, HOME, sfile))

  for sfile in CONFIG_THEME_ALL:
    create_folder_for_file(sfile)
    if (copy_all or not os.path.exists(os.path.join(HOME, sfile))):
      os.system("cp '%s/%s' '%s/.%s'" % (CONFIG_THEME_DIR, sfile, HOME, sfile))
      os.system("sed -i s/_X-FONTSIZE-X_/%i/ '%s/.%s'" % (fontSize, HOME, sfile))

  # TESTING
  foxFolders = getoutput("find %s/.mozilla/firefox/*.default/chrome/ -type d" % HOME).strip().split("\n")
  foxFolders.sort()
  if (len(foxFolders) >= 1 and os.path.exists(foxFolders[0])):
    foxFolder = foxFolders[0]
    os.system('cp "%s/mozilla/firefox/default/chrome/userContent.css" "%s"' % (CONFIG_THEME_DIR, foxFolder))

  os.system('gconftool-2 -t str -s /apps/metacity/general/theme "KXStudio"')
  os.system('gconftool-2 -t str -s /apps/metacity/general/button_layout "close,minimize,maximize:menu"')
  os.system('gconftool-2 -t str -s /apps/metacity/general/titlebar_font "DejaVu Sans Bold %i"' % fontSize)
  os.system('gconftool-2 -t str -s /apps/nautilus/preferences/desktop_font "DejaVu Sans %i"' % fontSize)
  os.system('gconftool-2 -t str -s /desktop/gnome/interface/gtk_theme "QtCurve"')
  os.system('gconftool-2 -t str -s /desktop/gnome/interface/icon_theme "Oxygen Mono Dark"')
  os.system('gconftool-2 -t str -s /desktop/gnome/interface/font_name "DejaVu Sans %i"' % fontSize)
  os.system('gconftool-2 -t str -s /desktop/gnome/interface/document_font_name "DejaVu Sans %i"' % fontSize)
  os.system('gconftool-2 -t str -s /desktop/gnome/interface/monospace_font_name "DejaVu Sans Mono %i"' % fontSize)
  os.system('gconftool-2 -t bool -s /desktop/gnome/interface/buttons_have_icons true')
  os.system('gconftool-2 -t bool -s /desktop/gnome/interface/menus_have_icons true')

def do_wine_stuff():
  if not os.path.exists("/usr/bin/wineboot"):
    return

  os.system("wineboot")
  #os.system("sed -i 's/\[drivers32\]/\[drivers32\]\nMSACM.vorbis=vorbis.acm/' ~/.wine/drive_c/windows/system.ini")

  if (os.path.exists("/usr/lib/i386-linux-gnu/wine/wineasio.dll.so")):
    os.system("regsvr32 wineasio.dll")

  if (os.path.exists("/usr/lib/x86_64-linux-gnu/wine/wineasio.dll.so")):
    os.system("wine64 regsvr32 wineasio.dll")

  if (os.path.exists("/usr/bin/winetricks")):
    os.system("winetricks fontfix fontsmooth-rgb nocrashdialog winxp")

def do_final_stuff():
  os.system('gconftool-2 --type string --set /system/gstreamer/0.10/default/audiosink "pulsesink device=\'jack_out\'"')
  os.system('gconftool-2 --type string --set /system/gstreamer/0.10/default/audiosrc "pulsesrc"')
  os.system('gconftool-2 --type string --set /system/gstreamer/0.10/default/chataudiosink "pulsesink device=\'jack_out\'"')
  os.system('gconftool-2 --type string --set /system/gstreamer/0.10/default/musicaudiosink "pulsesink device=\'jack_out\'"')
  os.system('gconftool-2 --type string --set /system/gstreamer/0.10/default/audiosink_description "Jack"')
  os.system('gconftool-2 --type string --set /system/gstreamer/0.10/default/audiosrc_description "Pulse Audio"')
  os.system('gconftool-2 --type string --set /system/gstreamer/0.10/default/chataudiosink_description "Jack"')
  os.system('gconftool-2 --type string --set /system/gstreamer/0.10/default/musicaudiosink_description "Jack"')

def do_live_stuff():
  desktopDir   = os.path.join(HOME, "Desktop")
  ubiquityFile = "/usr/share/applications/kde4/ubiquity-kdeui.desktop"

  if (not os.path.exists(desktopDir)):
    os.mkdir(desktopDir)

  if (os.path.exists(ubiquityFile)):
    os.system("cp '%s' '%s'" % (ubiquityFile, desktopDir))

# ----------------------------------------------

# Separate Thread for Copying Stuff
class CopyStuffThread(QThread):
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
        self.emit(SIGNAL("setLabelPixmap(int, int)"), ID_GROUP_SETTINGS, ID_PIXMAP_PROCESS)
        if (self._copy):
          sleep(1)
          if (self._copy_all):
            do_copy_all()
          elif (self._copy_basic):
            do_copy_basic()
        self.emit(SIGNAL("setLabelPixmap(int, int)"), ID_GROUP_SETTINGS, ID_PIXMAP_DONE)

        # Theme
        self.emit(SIGNAL("setLabelPixmap(int, int)"), ID_GROUP_THEME, ID_PIXMAP_PROCESS)
        if (self._copy_theme):
          sleep(1)
          do_copy_theme(self._font_size)
        self.emit(SIGNAL("setLabelPixmap(int, int)"), ID_GROUP_THEME, ID_PIXMAP_DONE)

        # Wine
        self.emit(SIGNAL("setLabelPixmap(int, int)"), ID_GROUP_WINE, ID_PIXMAP_PROCESS)
        if (self._copy):
          do_wine_stuff()
        self.emit(SIGNAL("setLabelPixmap(int, int)"), ID_GROUP_WINE, ID_PIXMAP_DONE)

        # Final
        self.emit(SIGNAL("setLabelPixmap(int, int)"), ID_GROUP_FINAL, ID_PIXMAP_PROCESS)
        if (self._copy):
          sleep(1)
          do_final_stuff()
        self.emit(SIGNAL("setLabelPixmap(int, int)"), ID_GROUP_FINAL, ID_PIXMAP_DONE)

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

        self.setWindowIcon(QIcon.fromTheme("start-here-kxstudio", QIcon(self.pixmap_kxstudio)))

        self.copyStuffThread = CopyStuffThread(self)

        self.connect(self, SIGNAL("finished(int)"), self.saveSettings)
        self.connect(self, SIGNAL("currentIdChanged(int)"), self.pageChanged)
        self.connect(self.b_screenshot, SIGNAL("clicked()"), self.showScreenshot)
        self.connect(self.copyStuffThread, SIGNAL("setLabelPixmap(int, int)"), self.setLabelPixmap)
        self.connect(self.copyStuffThread, SIGNAL("finished()"), self.copyStuffFinished)

        if (not os.path.exists("/usr/share/themes/KXStudio/index.theme")):
          self.group_theme.setChecked(False)
          self.group_theme.setEnabled(False)

    def showScreenshot(self):
        box = QMessageBox(self)
        box.setIconPixmap(QPixmap(os.path.join(PWD, "icons", "screenshot.png")))
        box.setWindowTitle(self.tr("Welcome to KXStudio - Screenshot"))
        box.exec_()

    def pageChanged(self, page):
        # Initial page
        if (self.previous_page == -1 and page == 0):
          pass

        # Process Stuff
        elif (self.previous_page == 0 and page == 1):
          self.button(QWizard.BackButton).setEnabled(False)
          self.button(QWizard.NextButton).setEnabled(False)
          self.button(QWizard.CancelButton).setEnabled(False)
          self.progressBar.setValue(0)
          self.copyStuffThread.setData(self.sb_fontSize.value(), self.group_settings.isChecked(), self.rb_all.isChecked(), self.rb_basic.isChecked(), self.group_theme.isChecked())
          self.copyStuffThread.start()

        # Final page
        elif (self.previous_page == 1 and page == 2):
          self.button(QWizard.BackButton).setEnabled(False)
          self.button(QWizard.CancelButton).setEnabled(False)

        self.previous_page = page

    def setLabelPixmap(self, group_id, pixmap_id):
        label = None

        if (group_id == ID_GROUP_SETTINGS):
          label = self.l_ico_settings
          self.progressBar.setValue(0)
        elif (group_id == ID_GROUP_THEME):
          label = self.l_ico_theme
          self.progressBar.setValue(25)
        elif (group_id == ID_GROUP_WINE):
          label = self.l_ico_wine
          self.progressBar.setValue(50)
        elif (group_id == ID_GROUP_FINAL):
          label = self.l_ico_final
          self.progressBar.setValue(75)
        else:
          return

        if (pixmap_id == ID_PIXMAP_QUEQUE):
          label.setPixmap(self.pixmap_queque)
        elif (pixmap_id == ID_PIXMAP_PROCESS):
          label.setPixmap(self.pixmap_process)
        elif (pixmap_id == ID_PIXMAP_DONE):
          label.setPixmap(self.pixmap_done)

    def copyStuffFinished(self):
        self.progressBar.setValue(100)
        self.button(QWizard.NextButton).setEnabled(True)
        self.button(QWizard.CancelButton).setEnabled(True)

    def saveSettings(self):
        settings.setValue("Geometry", self.saveGeometry())
        settings.setValue("FirstRun", False)

    def loadSettings(self):
        self.restoreGeometry(settings.value("Geometry", ""))

    def closeEvent(self, event):
        self.saveSettings()
        QWizard.closeEvent(self, event)

#--------------- main ------------------
if __name__ == '__main__':

    # Live-DVD usage
    if ("--live-dvd" in sys.argv):
      do_copy_all()
      do_copy_theme()
      do_final_stuff()
      do_live_stuff()
      sys.exit(0)

    # App initialization
    app = QApplication(sys.argv)
    app.setApplicationName("Welcome")
    app.setOrganizationName("KXStudio")

    settings = QSettings("KXStudio", "Welcome")

    run = True
    if ("--first-run" in app.arguments()):
      run = settings.value("FirstRun", True, type=bool)

    # Show GUI
    if (run):
      gui = WelcomeW()
      gui.show()
      ret = app.exec_()
    else:
      ret = 0

    # Exit properly
    sys.exit(ret)
