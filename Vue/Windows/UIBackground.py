

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
from Vue.Windows.ui_WBackground import Ui_WBackground

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
class UIBackground(QWidget, Ui_WBackground):
 #--------------------------------
 # Initialisation
 #--------------------------------
 def __init__(self, parent=None):
  super().__init__(parent)
  self.setupUi(self)
  self.setWindowFlags(Qt.Window|Qt.FramelessWindowHint)
  #self.setWindowModality(Qt.ApplicationModal)

  #self.setAttribut(Qt.WA_TranslucentBackground)
  self.setWindowOpacity(0.5)
  #self.widget_3.setStyleSheet("background-color: rgba(255, 0, 0, 255");
  #self.widget_3.setWindowOpacity(1)

  self.tParent = parent
  """
  effect = QGraphicsOpacityEffect(self)
  effect.setOpacity(0.5);
  self.setGraphicsEffect(effect)
  """

 #-----------------------------
 # Ouverture de la fenêtre de modification de paramètre
 #-----------------------------
 def vFOpen( self, tSize ):
  print("-- vFOpen --")
  #self.resize(tSize)

  uiY = self.tParent.y()
  uiX = self.tParent.x()
  print("uiY = %u"%uiY)
  print("uiX = %u"%uiX)

  self.setGeometry(uiX, uiY+31, self.tParent.width(), self.tParent.height())

  # Ouverture de la fenêtre
  self.show()

 #----------------------------
 # Click sur le bouton OK
 #----------------------------
 def accept(self):
  print("ACCEPT")
  # Fermeture de la fenêtre
  self.close()

 #----------------------------
 # Click sur le bouton Annuler
 #----------------------------
 def reject(self):
  print("REJECT")
  # Fermeture de la fenêtre
  self.close()
