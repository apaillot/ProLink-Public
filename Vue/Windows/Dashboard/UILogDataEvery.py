

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
from Vue.Windows.Dashboard.ui_WLogDataEvery import Ui_WLogDataEvery

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
class UILogDataEvery(QWidget, Ui_WLogDataEvery):
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

  # Signal de changement de valeur minute
  self.spinBox_Secs.valueChanged.connect( self.vFSecondsChanged )
  self.spinBox_Mins.valueChanged.connect( self.vFMinutesChanged )
  self.spinBox_Hours.valueChanged.connect( self.vFHoursChanged )

 #-----------------------------
 # Ouverture de la fenêtre de modification de paramètre
 #-----------------------------
 def vFOpen( self, uiHour, uiMin, uiSec ):
  print("-- vFOpen --")
  self.siOpen.emit()
  # Remplissage des champs
  self.spinBox_Hours.setValue(uiHour)
  self.spinBox_Mins.setValue(uiMin)
  self.spinBox_Secs.setValue(uiSec)
  if( uiMin > 0 ):
   self.spinBox_Secs.setValue(0)
   self.spinBox_Secs.setEnabled(False)
  if(   ( uiHour == 0 )
    and ( uiMin  == 0 )
    and ( uiSec   < 2 ) ):
   self.spinBox_Secs.setValue(2)
   self.spinBox_Secs.setEnabled(True)
  # Ouverture de la fenêtre
  self.show()

 #-----------------------------
 # Changement des paramètres des secondes
 #-----------------------------
 def vFSecondsChanged( self, uiSeconds ):
  print("-- vFSecondsChanged --")
  uiHour = self.spinBox_Hours.value()
  uiMin  = self.spinBox_Mins.value()
  print("uiHour    = %d"%uiHour)
  print("uiMin     = %d"%uiMin)
  print("uiSeconds = %d"%uiSeconds)
  if(   ( uiHour == 0 )
    and ( uiMin  == 0 )
    and ( uiSeconds < 2 ) ):
   self.spinBox_Secs.setValue(2)

 #-----------------------------
 # Changement des paramètres des minutes
 #-----------------------------
 def vFMinutesChanged( self, uiMin ):
  print("-- vFMinutesChanged --")
  uiHour = self.spinBox_Hours.value()
  print("uiHour    = %d"%uiHour)
  print("uiMin     = %d"%uiMin)
  #print("uiSeconds = %d"%uiSeconds)
  if( uiMin > 0 ):
   self.spinBox_Secs.setValue(0)
   self.spinBox_Secs.setEnabled(False)
  if( ( uiHour == 0 ) and ( uiMin == 0 ) ):
   self.spinBox_Secs.setValue(2)
   self.spinBox_Secs.setEnabled(True)

 #-----------------------------
 # Changement des paramètres des heures
 #-----------------------------
 def vFHoursChanged( self, uiHour ):
  print("-- vFHoursChanged --")
  uiMin = self.spinBox_Mins.value()
  print("uiHour    = %d"%uiHour)
  print("uiMin     = %d"%uiMin)
  #print("uiSeconds = %d"%uiSeconds)
  if( uiHour > 0 ):
   self.spinBox_Secs.setValue(0)
   self.spinBox_Secs.setEnabled(False)
  if( ( uiHour == 0) and ( uiMin == 0 ) ):
   self.spinBox_Secs.setValue(2)
   self.spinBox_Secs.setEnabled(True)

 #----------------------------
 # Click sur le bouton OK
 #----------------------------
 def accept(self):
  print("ACCEPT")
  # Récupération des valeurs
  uiHour = self.spinBox_Hours.value()
  uiMin  = self.spinBox_Mins.value()
  uiSec  = self.spinBox_Secs.value()
  print("uiHour = %d"%uiHour)
  print("uiMin = %d"%uiMin)
  print("uiSec = %d"%uiSec)
  # Signal d'écriture
  self.siWriteData.emit(uiHour,uiMin,uiSec)
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
