

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
from Vue.Windows.Dashboard.ui_WSondeTime import Ui_WSondeTime

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
class UISondeTime(QWidget, Ui_WSondeTime):
 # -- Signal list --
 siOpen      = Signal()
 siWriteData = Signal(int, int, int)
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
 def vFOpen( self, uiHour, uiMin, uiSec ):
  print("-- vFOpen --")
  self.siOpen.emit()
  # Remplissage des champs
  tTime = QTime( uiHour, uiMin, uiSec, 0 )
  print(tTime)
  self.timeEdit.setTime(tTime)
  #self.spinBox_Hour.setValue(uiHour)
  #self.spinBox_Min.setValue(uiMin)
  #self.spinBox_Sec.setValue(uiSec)
  # Ouverture de la fenêtre
  self.show()

 #----------------------------
 # Click sur le bouton OK
 #----------------------------
 def accept(self):
  print("ACCEPT")

  tTime = self.timeEdit.time()

  # Récupération des valeurs
  uiHour = tTime.hour()
  uiMin  = tTime.minute()
  uiSec  = tTime.second()
  print("uiHour = %d"%uiHour)
  print("uiMin = %d"%uiMin)
  print("uiSec = %d"%uiSec)
  self.siWriteData.emit(uiHour, uiMin, uiSec)
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
