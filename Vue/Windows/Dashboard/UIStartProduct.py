

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
from Vue.Windows.Dashboard.ui_WStartProduct import Ui_WStartProduct

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
class UIStartProduct(QWidget, Ui_WStartProduct):
 # -- Signal list --
 siOpen      = Signal()
 siWriteData = Signal(QDateTime)
 siClose     = Signal()

 #--------------------------------
 # Initialisation
 #--------------------------------
 def __init__(self, parent=None):
  super().__init__(parent)
  self.setupUi(self)
  self.setWindowFlags(Qt.Window|Qt.FramelessWindowHint)
  self.setWindowModality(Qt.ApplicationModal)
  # Signal de changement de valeur de démarrage
  self.comboBox.currentTextChanged.connect( self.vFStartValueChanged )

 #-----------------------------
 # Changement valeur de démarrage
 #-----------------------------
 def vFStartValueChanged( self ):
  print("-- vFStartValueChanged --")
  sStartValue = self.comboBox.currentText()
  #dateTimeEdit
  if( sStartValue == "Scheduled start" ):
   #self.dateTimeEdit.setEnabled(True)
   self.dateTimeEdit.setVisible(True)
   self.label_at.setVisible(True)
  else:
   #self.dateTimeEdit.setEnabled(False)
   self.dateTimeEdit.setVisible(False)
   self.label_at.setVisible(False)

 #-----------------------------
 # Ouverture de la fenêtre de modification de paramètre
 #-----------------------------
 def vFOpen( self, sStartModeType, sStartModeDate ):
  print("-- vFOpen --")
  self.siOpen.emit()
  # Debug
  print("sStartModeType"+sStartModeType)
  print("sStartModeDate"+sStartModeDate)
  # Selon le start mode en entrée
  if( sStartModeType == "Stopped" ):
   sCurrentStartModeType = "Stop"
  elif( sStartModeType == "Logging" ):
   sCurrentStartModeType = "Start"
  elif( sStartModeType == "Scheduled"  ):
   sCurrentStartModeType = "Scheduled"
  else:
   sCurrentStartModeType = "Stop"
  # Start mode
  self.comboBox.setCurrentText(sCurrentStartModeType)
  # Si en mode déploiement
  if( sCurrentStartModeType == "Scheduled start" ):
   self.dateTimeEdit.setVisible(True)
   self.label_at.setVisible(True)
  else:
   self.dateTimeEdit.setVisible(False)
   self.label_at.setVisible(False)

  # Par défaut la date de maintenant
  self.dateTimeEdit.setMinimumDateTime(QDateTime.currentDateTime())

  # Remplissage des champs
  #self.comboBox.setCurrentText(sTxt)
  # Ouverture de la fenêtre
  self.show()

 #----------------------------
 # Click sur le bouton OK
 #----------------------------
 def accept(self):
  print("ACCEPT")
  # Récupération des valeurs
  sCurrentStartModeType = self.comboBox.currentText()
  print("sCurrentStartModeType = %s"%sCurrentStartModeType)
  # Démarrage sur date
  if( sCurrentStartModeType == "Scheduled start" ):
   tdateTime = self.dateTimeEdit.dateTime()
  # Démarrage immédiat
  elif( sCurrentStartModeType == "Start now" ):
   print("UIStartProduct => Start now")
   tdateTime = QDateTime.currentDateTime()
  # Stop produit
  else:
   tdateTime = None

  # Signal d'écriture
  self.siWriteData.emit(tdateTime)
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
