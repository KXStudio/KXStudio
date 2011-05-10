#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports (Global)
from PyQt4.QtCore import QSettings, QVariant, SLOT
from PyQt4.QtGui import QApplication, QWizard
import os, sys

# Imports (Custom)
import ui_welcome

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

# Main Window
class WelcomeW(QWizard, ui_welcome.Ui_WelcomeW):
    def __init__(self, parent=None):
        super(WelcomeW, self).__init__(parent)
        self.setupUi(self)

        self.loadSettings()

        #self.connect(self.act_plugin_add, SIGNAL("triggered()"), self.showPluginDatabase)

    def saveSettings(self):
        settings.setValue("Geometry", QVariant(self.saveGeometry()))
        settings.setValue("FirstRun", False)

    def loadSettings(self):
        self.restoreGeometry(settings.value("Geometry").toByteArray())

    def closeEvent(self, event):
        self.saveSettings()
        QMainWindow.closeEvent(self, event)

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
      if (app.arguments()[1] == "--"):
        if (not settings.value("FirstRun", False)):
          run = False

    # Show GUI
    if (run):
      gui = WelcomeW()
      gui.show()
      ret = app.exec_()
    else:
      ret = 0

    # Exit properly
    sys.exit(ret)
