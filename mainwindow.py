# This Python file uses the following encoding: utf-8

#============================================================================#
# Librairies système
#============================================================================#
import sys
#import folium
import io, csv
import serial
import serial.tools.list_ports as port_list
import time
#from maps import MapCreator
import struct
import configparser

#============================================================================#
# Librairies Qt
#============================================================================#
from PySide6.QtCore import QLibraryInfo, QTranslator, QLocale
from PySide6.QtWidgets import QApplication, QMainWindow

#============================================================================#
# Librairies Utilisateur
#============================================================================#
from ui_form import Ui_MainWindow
from Vue.VMainWindow import VMainWindow
from Model.MMainWindow import MMainWindow
from Controleur.CMainWindow import CMainWindow
import ressource_rc
from TVersion import sGlobalSoftwareVersion
from File.TINIFile import TINIFile

#============================================================================#
# Variable
#============================================================================#
# Version de l'application
sSoftwareVersion = sGlobalSoftwareVersion

#============================================================================#
# Main
#============================================================================#

if __name__ == "__main__":
 print("== START SOFTWARE ==")
 print("sSoftwareVersion = "+sSoftwareVersion)
 app = QApplication(sys.argv)
 # Paramètre application
 app.setOrganizationName("Aquaread")
 app.setOrganizationDomain("nke-group.com")
 app.setApplicationName("ProLink_V"+sSoftwareVersion)
 # Style
 # Modification du theme car problème d'affichage des spinbox dans Windows 11
 app.setStyle('windowsvista')
 #app.setStyle('Windows')
 #app.setStyle('fusion')
 #app.setStyle('macos')
 #app.setStyle('QtCurve')

 #-----------------------------
 # Lecture ini file
 #-----------------------------
 tINIFile = TINIFile()
 tINIFile.vFReadConfig()
 ## TODO - Vérif intégrité ini config

 # Récupération paramètre de langue
 sLocale = tINIFile.tConfig['GLOBAL']['location']
 # Ecriture du numéro de version du logiciel
 #tINIFile.tConfig['GLOBAL']['version'] = sSoftwareVersion
 #tINIFile.vFWriteConfig()
 # Debug
 bDebug = True if( int(tINIFile.tConfig["GLOBAL"]["debug"]) == 1 ) else False
 # Log error
 bError = True if( int(tINIFile.tConfig["GLOBAL"]["error"]) == 1 ) else False

 #-----------------------------
 # Traduction application
 #-----------------------------
 print("Chargement traduction")
 if( sLocale != "" ):
  sLocale = sLocale
 else:
  print( QLocale.system().name().split("_")[0] )
  sLocale = QLocale.system().name().split("_")[0]
 translator = QTranslator(app)

 if( translator.load(":/Aquaread_tool_"+sLocale) ):
  print("GOOD 2")
  app.installTranslator(translator)

 #----------------------------
 # Si fonctionnement en mode développement
 #----------------------------
 bQTRun = False
 for arg in sys.argv:
  print(arg)
  if("QT_RUN" in arg): bQTRun = True

 #-----------------------------
 # Capture de la sortie print vers fichier debug en release
 #-----------------------------
 if( ( bDebug or bError ) and not bQTRun ):
  if( bDebug ):
   old_stdout = sys.stdout
   log_file   = open("message.log","w")
   sys.stdout = log_file
  if( bError ):
   old_stderr = sys.stderr
   log_error_file = open("error.log","w")
   sys.stderr = log_error_file
  # Au moment de la fermeture
  def vFMyExitHandler():
   if( bDebug ):
    log_file.close()
   if( bError ):
    log_error_file.close()
  # A la fermeture de l'application
  app.aboutToQuit.connect(vFMyExitHandler)

 #-------------------------------
 # Architecture MVC
 #-------------------------------
 tModel     = MMainWindow()
 tView      = VMainWindow(tINIFile)
 tControler = CMainWindow(tView, tModel, sSoftwareVersion, tINIFile)

 #-------------------------------
 # Main loop
 #-------------------------------
 if( int(tINIFile.tConfig["GLOBAL"]["debug"]) == 1 ):
  tView.show()
 sys.exit(app.exec())
