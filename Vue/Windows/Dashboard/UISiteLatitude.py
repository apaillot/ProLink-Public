

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
from Vue.Windows.Dashboard.ui_WSiteLatitude import Ui_WSiteLatitude

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
class UISiteLatitude(QWidget, Ui_WSiteLatitude):
 # -- Signal list --
 siOpen      = Signal()
 siWriteData = Signal(str, int, float)
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
 def vFOpen( self, sRef, uiDeg, fMin ):
  print("-- vFOpen --")
  self.siOpen.emit()
  # Remplissage des champs
  self.comboBox_Ref.setCurrentText(sRef)
  self.spinBox_Deg.setValue(uiDeg)
  self.spinBox_Min.setValue(fMin)
  # Ouverture de la fenêtre
  self.show()

 #-----------------------------
 # Ouverture de la fenêtre de pour LeveLine
 #-----------------------------
 def vFOpenLeveLine( self, sRef, uiDeg, fMin ):
  print("-- vFOpen --")
  self.siOpen.emit()
  # Nombre de décimal
  self.spinBox_Min.setDecimals(4)
  # Remplissage des champs
  self.comboBox_Ref.setCurrentText(sRef)
  self.spinBox_Deg.setValue(uiDeg)
  self.spinBox_Min.setValue(fMin)
  # Ouverture de la fenêtre
  self.show()

 #----------------------------
 # Click sur le bouton OK
 #----------------------------
 def accept(self):
  print("ACCEPT")
  # Récupération des valeurs
  sRef  = self.comboBox_Ref.currentText()
  uiDeg = self.spinBox_Deg.value()
  fMin  = self.spinBox_Min.value()
  print("sRef  = %s"%sRef)
  print("uiDeg = %u"%uiDeg)
  print("fMin  = %f"%fMin)
  # Signal d'écriture
  self.siWriteData.emit(sRef, uiDeg, fMin)
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
