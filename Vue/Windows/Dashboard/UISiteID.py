

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
from Vue.Windows.Dashboard.ui_WSiteID import Ui_WSiteID

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
class UISiteID(QWidget, Ui_WSiteID):
 # -- Signal list --
 siOpen      = Signal()
 siWriteData = Signal(str)
 siClose     = Signal()

 #--------------------------------
 # Initialisation
 #--------------------------------
 def __init__(self, parent=None):
  super().__init__(parent)
  self.setupUi(self)
  self.setWindowFlags(Qt.Window|Qt.FramelessWindowHint)
  self.setWindowModality(Qt.ApplicationModal)

 #-----------------------------
 # Ouverture de la fenêtre de modification de paramètre
 #-----------------------------
 def vFOpen( self, sTxt ):
  print("-- vFOpen --")
  self.siOpen.emit()
  # Remplissage des champs
  self.lineEdit_SiteID.setText(sTxt)
  # Ouverture de la fenêtre
  self.show()

 #----------------------------
 # Click sur le bouton OK
 #----------------------------
 def accept(self):
  print("ACCEPT")
  # Récupération des valeurs
  sTxt = self.lineEdit_SiteID.text()
  print("sTxt = %s"%sTxt)
  # Signal d'écriture
  self.siWriteData.emit(sTxt)
  # Fermeture de la fenêtre
  #self.siClose.emit()
  self.close()

 #----------------------------
 # Click sur le bouton Annuler
 #----------------------------
 def reject(self):
  print("REJECT")
  # Fermeture de la fenêtre
  self.siClose.emit()
  self.close()
