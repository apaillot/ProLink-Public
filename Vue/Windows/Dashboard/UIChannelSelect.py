

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
from Vue.Windows.Dashboard.ui_WChannelSelect import Ui_WChannelSelect

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
class UIChannelSelect(QWidget, Ui_WChannelSelect):
 # -- Signal list --
 siOpen      = Signal()
 siWriteData = Signal(str, int)
 siClose     = Signal()

 #--------------------------------
 # Initialisation
 #--------------------------------
 def __init__(self, parent=None):
  super().__init__(parent)
  self.setupUi(self)
  self.setWindowFlags(Qt.Window|Qt.FramelessWindowHint)
  self.setWindowModality(Qt.ApplicationModal)

 #--------------------------------
 # Initialisation
 #--------------------------------
 def setAPLiteSelection( self ):
  print("-- setAPLiteSelection --")
  # Effacement du champs
  self.comboBox_ChannelSelect.clear()
  # Remplissage des champs
  self.comboBox_ChannelSelect.addItems(["EMPTY",
                                        "Turbidity",
                                        "Chlorophyll",
                                        "BGA-PC",
                                        "BGA-PE",
                                        "Rhodamine",
                                        "Fluorescein",
                                        "Refined Oil",
                                        "CDOM",
                                        "Crude Oil",
                                        "Tryptophan"])
  # Selection EMPTY
  self.comboBox_ChannelSelect.setCurrentText("EMPTY")

 #--------------------------------
 # Initialisation
 #--------------------------------
 def setProbeSelection( self ):
  print("-- setProbeSelection --")
  # Effacement du champs
  self.comboBox_ChannelSelect.clear()
  # Remplissage des champs
  self.comboBox_ChannelSelect.addItems(["EMPTY",
                                        "Ammonium",
                                        "Chloride",
                                        "Fluoride",
                                        "Nitrate",
                                        "Calcium",
                                        "Turbidity",
                                        "Chlorophyll",
                                        "BGA-PC",
                                        "BGA-PE",
                                        "Rhodamine",
                                        "Fluorescein",
                                        "Refined Oil",
                                        "CDOM",
                                        "Crude Oil",
                                        "Tryptophan"])
  # Selection EMPTY
  self.comboBox_ChannelSelect.setCurrentText("EMPTY")

 #-----------------------------
 # Ouverture de la fenêtre de modification de paramètre
 #-----------------------------
 def vFOpen( self, ucChannel, tChannel, tWidget ):
  print("-- vFOpen --")
  print("ucChannel = %d"%ucChannel)
  self.siOpen.emit()
  # Mémorisation des variables
  self.ucChannel = ucChannel
  self.tChannel  = tChannel
  self.tWidget   = tWidget

  # Remplissage des champs
  self.comboBox_ChannelSelect.setCurrentText(tChannel["sIndex"])
  # Ouverture de la fenêtre
  self.show()

 #----------------------------
 # Click sur le bouton OK
 #----------------------------
 def accept(self):
  print("ACCEPT")
  # Récupération des valeurs
  sChannelName = self.comboBox_ChannelSelect.currentText()
  # Emit du signal d'écriture
  self.siWriteData.emit(sChannelName, self.ucChannel)
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


