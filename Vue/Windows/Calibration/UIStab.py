

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
from Vue.Windows.Calibration.ui_WStab import Ui_WStab

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
class UIStab(QWidget, Ui_WStab):
 # -- Signal list --
 #siWriteData = Signal()
 siOpen      = Signal()
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
 # Ouverture de la fenêtre
 #-----------------------------
 def vFOpen( self, uiMax ):
  print("-- vFOpen --")
  self.siOpen.emit()
  self.uiMax = uiMax
  # On démarre à 0
  self.progressBar.setValue( 0 )
  # Affectation du maximum
  self.progressBar.setMaximum( uiMax )
  # Ouverture de la fenêtre
  self.show()

 #-----------------------------
 # Mise à jour scrollbarr
 #-----------------------------
 def vFUpdate( self, uiValue ):
  #print("-- vFUpdate --")
  self.progressBar.setValue( uiValue )

 #----------------------------
 # Fermeture de la fenêtre
 #----------------------------
 def vFClose(self):
  print("CLOSE")
  # Fermeture de la fenêtre
  self.siClose.emit()
  self.close()

 #----------------------------
 # Click sur le bouton Annuler
 #----------------------------
 def accept(self):
  print("ACCEPT")
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
