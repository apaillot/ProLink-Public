

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
from Vue.Windows.Data.Lvl.ui_WLvlDataBaroCorrection import Ui_WLvlDataBaroCorrection

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
class UILvlDataBaroCorrection(QWidget, Ui_WLvlDataBaroCorrection):
 # -- Signal list --
 siOpen      = Signal()
 siWriteData = Signal(str, str, float)
 siClose     = Signal()

 #--------------------------------
 # Initialisation
 #--------------------------------
 def __init__(self, parent=None):
  super().__init__(parent)
  self.setupUi(self)
  self.setWindowFlags(Qt.Window|Qt.FramelessWindowHint)
  self.setWindowModality(Qt.ApplicationModal)
  # Modification correction type
  self.comboBox_CorrectionType.currentTextChanged.connect(self.vFCorrectionTypeChange)

 #-----------------------------
 # Ouverture de la fenêtre de modification de paramètre
 #-----------------------------
 def vFOpen( self, sSN, sSerie, tsBaroList, tPrj ):
  print("-- vFOpen --")
  self.siOpen.emit()
  # Modification de la taille
  #self.resize(self.width(), 175)

  # Effacement du champs
  self.comboBox_CorrectionType.clear()
  self.comboBox_CorrectionType.addItems(["None", "Logged Zeros", "Fixed"])
  # Si au moins un Baro est présent dans le projet
  if( len(tsBaroList) > 0 ):
   self.comboBox_CorrectionType.addItems(["Baro"])
   self.comboBox_BaroSelected.clear()
   self.comboBox_BaroSelected.addItems(tsBaroList)

  sBaroCorrection      = tPrj["tSensor"][sSN]["serie"][sSerie]["sBaroCorrection"]
  xBaroCorrectionValue = tPrj["tSensor"][sSN]["serie"][sSerie]["xBaroCorrectionValue"]

  # Remplissage des champs
  self.comboBox_CorrectionType.setCurrentText(sBaroCorrection)
  # Fixed
  if( sBaroCorrection == "Fixed" ):
   self.doubleSpinBox_FixedValue.setValue(float(xBaroCorrectionValue))
  # Baro
  if( sBaroCorrection == "Baro" ):
   self.comboBox_BaroSelected.setCurrentText(str(xBaroCorrectionValue))
  # Ouverture de la fenêtre
  self.show()

 #-----------------------------
 # En cas de modification
 #-----------------------------
 def vFCorrectionTypeChange( self ):
  print("-- vFCorrectionTypeChange --")

  sCorrectionType = self.comboBox_CorrectionType.currentText()
  # Si sélection None ou Logged zero
  if(  ( sCorrectionType == "None" )
    or ( sCorrectionType == "Logged Zeros" ) ):
   # Correction type
   self.widget_PartBaroSelected.setVisible( False )
   self.widget_PartFixedValue.setVisible( False )
  # Si Baro
  elif( sCorrectionType == "Baro" ):
   # Correction type
   self.widget_PartBaroSelected.setVisible( True )
   self.widget_PartFixedValue.setVisible( False )
  # Si Fixed
  elif( sCorrectionType == "Fixed" ):
   # Correction type
   self.widget_PartBaroSelected.setVisible( False )
   self.widget_PartFixedValue.setVisible( True )

 #----------------------------
 # Click sur le bouton OK
 #----------------------------
 def accept(self):
  print("ACCEPT")
  # Récupération des valeurs
  sCorrectionType = self.comboBox_CorrectionType.currentText()
  sBaroSN         = self.comboBox_BaroSelected.currentText()
  fFixedValue     = self.doubleSpinBox_FixedValue.value()
  print("sCorrectionType = %s"%sCorrectionType)
  print("sBaroSN         = %s"%sBaroSN)
  print("fFixedValue     = %.03f"%fFixedValue)

  #sTxt = self.comboBox_SetupLoggingCheck.currentText()
  #print("sTxt = %s"%sTxt)
  # Signal d'écriture
  self.siWriteData.emit( sCorrectionType, sBaroSN, fFixedValue )
  # Fermeture de la fenêtre
  self.siClose.emit()
  self.close()

 #----------------------------
 # Click sur le bouton Annuler
 #----------------------------
 def reject(self):
  print("REJECT")
  # Fermeture de la fenêtre
  self.siClose.emit()
  self.close()
