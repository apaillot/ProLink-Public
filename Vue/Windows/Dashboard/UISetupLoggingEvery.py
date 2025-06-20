

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
from Vue.Windows.Dashboard.ui_WSetupLoggingEvery import Ui_WSetupLoggingEvery

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
class UISetupLoggingEvery(QWidget, Ui_WSetupLoggingEvery):
 # -- Signal list --
 siOpen      = Signal()
 siWriteData = Signal(int, int)
 siClose     = Signal()

 #--------------------------------
 # Initialisation
 #--------------------------------
 def __init__(self, parent=None):
  super().__init__(parent)
  self.setupUi(self)
  self.setWindowFlags(Qt.Window|Qt.FramelessWindowHint)
  self.setWindowModality(Qt.ApplicationModal)
  # Signal de changement de valeur minute
  self.spinBox_SetupLoggingEveryHours.valueChanged.connect( self.vFHoursChanged )
  self.spinBox_SetupLoggingEveryMins.valueChanged.connect( self.vFMinutesChanged )

 #-----------------------------
 # Ouverture de la fenêtre de modification de paramètre
 #-----------------------------
 def vFOpen( self, uiHours, uiMinutes ):
  print("-- vFOpen --")
  self.siOpen.emit()
  # Remplissage des champs
  self.spinBox_SetupLoggingEveryHours.setValue(uiHours)
  self.spinBox_SetupLoggingEveryMins.setValue(uiMinutes)
  # Ouverture de la fenêtre
  self.show()

 #-----------------------------
 # Changement des paramètres des minutes
 #-----------------------------
 def vFMinutesChanged( self, uiMin ):
  print("-- vFMinutesChanged --")
  uiHour = self.spinBox_SetupLoggingEveryHours.value()
  print("uiHour    = %d"%uiHour)
  print("uiMin     = %d"%uiMin)
  #print("uiSeconds = %d"%uiSeconds)
  if( ( uiHour == 0 ) and ( uiMin == 0 ) ):
   self.spinBox_SetupLoggingEveryMins.setValue(1)

 #-----------------------------
 # Changement des paramètres des heures
 #-----------------------------
 def vFHoursChanged( self, uiHour ):
  print("-- vFHoursChanged --")
  uiMin = self.spinBox_SetupLoggingEveryMins.value()
  print("uiHour    = %d"%uiHour)
  print("uiMin     = %d"%uiMin)
  #print("uiSeconds = %d"%uiSeconds)
  if( ( uiHour == 0 ) and ( uiMin == 0 ) ):
   self.spinBox_SetupLoggingEveryMins.setValue(1)

 #----------------------------
 # Click sur le bouton OK
 #----------------------------
 def accept(self):
  print("ACCEPT")
  # Récupération des valeurs
  uiHour = self.spinBox_SetupLoggingEveryHours.value()
  uiMin  = self.spinBox_SetupLoggingEveryMins.value()
  print("uiHour = %d"%uiHour)
  print("uiMin  = %d"%uiMin)
  # Signal d'écriture
  self.siWriteData.emit(uiHour, uiMin)
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
