

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
    QSize, QTime, QUrl, Qt, Signal, QDate)
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QDialog

#============================================================================#
# Librairies Utilisateur
#============================================================================#
# Fenêtre modification configuration
from Vue.Windows.Dashboard.ui_WSondeDate import Ui_WSondeDate

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
class UISondeDate(QWidget, Ui_WSondeDate):
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
  # Modification de valeur
  self.dateEdit.dateChanged.connect(self.vFDateEditChanged)
  self.calendarWidget.clicked.connect(self.vFCalendarWidgetChanged)

 #--------------------------------
 # Date edit changed
 #--------------------------------
 def vFDateEditChanged(self, tDate):
  print("-- vFDateEditChanged --")
  self.calendarWidget.setSelectedDate( tDate )

 #--------------------------------
 # Calendar widget changed
 #--------------------------------
 def vFCalendarWidgetChanged(self, tDate):
  print("-- vFCalendarWidgetChanged --")
  self.dateEdit.setDate( tDate )

 #-----------------------------
 # Ouverture de la fenêtre de modification de paramètre
 #-----------------------------
 def vFOpen( self, uiDay, uiMonth, uiYear ):
  print("-- vFOpen --")
  print("uiDay   = %d"%uiDay)
  print("uiMonth = %d"%uiMonth)
  print("uiYear  = %d"%uiYear)
  self.siOpen.emit()
  # Remplissage des champs
  tDate = QDate( 2000+uiYear, uiMonth, uiDay )
  print(tDate)
  self.dateEdit.setDate( tDate )
  self.calendarWidget.setSelectedDate( tDate )
  # Ouverture de la fenêtre
  self.show()

 #----------------------------
 # Click sur le bouton OK
 #----------------------------
 def accept(self):
  print("-- ACCEPT --")
  # Récupération des valeurs
  tDate   = self.dateEdit.date()
  uiDay   = tDate.day()
  uiMonth = tDate.month()
  uiYear  = tDate.year()
  print("uiDay   = %d"%uiDay)
  print("uiMonth = %d"%uiMonth)
  print("uiYear  = %d"%uiYear)
  self.siWriteData.emit(uiDay, uiMonth, uiYear)
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
