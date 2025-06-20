

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
from Vue.Windows.Dashboard.ui_WEventLoggingTemperature import Ui_WEventLoggingTemperature

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
class UIEventLoggingTemperature(QWidget, Ui_WEventLoggingTemperature):
 # -- Signal list --
 siOpen      = Signal()
 siWriteData = Signal(float)
 siClose     = Signal()

 #--------------------------------
 # Initialisation
 #--------------------------------
 def __init__(self, parent=None):
  super().__init__(parent)
  self.setupUi(self)
  self.setWindowFlags(Qt.Window|Qt.FramelessWindowHint)
  self.setWindowModality(Qt.ApplicationModal)
  # Signal de changement de valeur d'activation
  self.comboBox.currentTextChanged.connect( self.vFComboboxChanged )

 #-----------------------------
 # Ouverture de la fenêtre de modification de paramètre
 #-----------------------------
 def vFOpen( self, sState, uiValue ):
  print("-- vFOpen --")
  self.siOpen.emit()
  # Remplissage des champs
  self.spinBox.setValue(uiValue)
  self.comboBox.setCurrentText(sState)
  # Ouverture de la fenêtre
  self.show()

 #-----------------------------
 # Modification de l'activation
 #-----------------------------
 def vFComboboxChanged( self ):
  print("-- vFComboboxChanged --")
  if( self.comboBox.currentText() == "Disable" ):
   self.spinBox.setValue(0)
   self.spinBox.setEnabled(False)
  else:
   self.spinBox.setEnabled(True)

 #----------------------------
 # Click sur le bouton OK
 #----------------------------
 def accept(self):
  print("ACCEPT")
  # Récupération des valeurs
  fValue = self.spinBox.value()
  print("fValue = %f"%fValue)
  # Signal d'écriture
  self.siWriteData.emit(fValue)
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
