

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
from Vue.Windows.Update.ui_WUpdateDetected import Ui_WUpdateDetected

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
class UIUpdateDetected(QWidget, Ui_WUpdateDetected):
 # -- Signal list --
 siAcceptUpdate = Signal()
 siClose        = Signal()

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
 def vFOpen( self, sVersion ):
  print("-- vFOpen --")
  print("-- UIIpdateDetected -- " + sVersion)
  # Mise à jour du numéro de version
  self.label_SoftwareVersion.setText(sVersion)
  # Ouverture de la fenêtre
  self.show()

 #----------------------------
 # Click sur le bouton OK
 #----------------------------
 def accept(self):
  print("ACCEPT")
  # Signal de fermeture de la fenêtre
  self.siClose.emit()
  # Signal d'écriture
  self.siAcceptUpdate.emit()
  # Fermeture effective
  self.close()

 #----------------------------
 # Click sur le bouton Annuler
 #----------------------------
 def reject(self):
  print("REJECT")
  # Fermeture de la fenêtre
  self.siClose.emit()
  self.close()
