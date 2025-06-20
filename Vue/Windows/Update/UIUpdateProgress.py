

#============================================================================#
# Librairies système
#============================================================================#
import sys
import os
import struct
from datetime import datetime
import time
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QDialog

#============================================================================#
# Librairies Utilisateur
#============================================================================#
# Fenêtre modification configuration
from Vue.Windows.Update.ui_WUpdateProgress import Ui_WUpdateProgress

#============================================================================#
# Variable
#============================================================================#

#===========================================================================#
# Déclaration des Types
#===========================================================================#

#===========================================================================#
# Déclaration des fonctions
#===========================================================================#

#****************************************************************************/
# Class
#****************************************************************************/

#----------------------------------------------------------------------------#
# Fenêtre modification configuration
#----------------------------------------------------------------------------#
class UIUpdateProgress(QWidget, Ui_WUpdateProgress):
 # -- Signal list --
 siAcceptUpdate = Signal()
 siClose        = Signal()

 #--------------------------------
 # Initialisation
 #--------------------------------
 def __init__(self, parent=None):
  super().__init__(parent)
  self.setupUi(self)
  self.setWindowFlags(Qt.Window|Qt.FramelessWindowHint)
  self.setWindowModality(Qt.ApplicationModal)
  self.uiTotalBytes = 0

 #-----------------------------
 # Ouverture de la fenêtre de modification de paramètre
 #-----------------------------
 def vFOpen( self ):
  print("-- vFOpen --")
  self.progressBar.setValue(0)
  # Ouverture de la fenêtre
  self.show()

 #-----------------------------
 # Ouverture de la fenêtre de modification de paramètre
 #-----------------------------
 def vFTotalProgress( self, uiBytes, sFilename, uiFileTotalCount ):
  print("-- UIUpdateProgress > vFTotalProgress --")
  # Refresh de l'avancement
  self.uiTotalBytes = uiBytes
  # Nombre total de fichier
  self.uiFileTotalCount = uiFileTotalCount
  # Nom du fichier
  self.label_FileName.setText(str(sFilename))

 #-----------------------------
 # Ouverture de la fenêtre de modification de paramètre
 #-----------------------------
 def vFProgress( self, uiBytes, uiFileCount ):
  if( self.uiTotalBytes != 0 ):
   # Calcul pourcentage
   uiPourcent = int( uiBytes * 100 / self.uiTotalBytes )
  # Mise à jour progress bar
  self.progressBar.setValue(uiPourcent)
  # Refresh de l'avancement
  self.label_FileCount.setText("("+str(uiFileCount+1)+"/"+str(self.uiFileTotalCount)+")")

 #----------------------------
 # Click sur le bouton Annuler
 #----------------------------
 def vFClose(self):
  print("-- vFClose --")
  # Fermeture de la fenêtre
  self.siClose.emit()
  self.close()
