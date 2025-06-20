# This Python file uses the following encoding: utf-8

#============================================================================#
# Librairies système
#============================================================================#
import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import QPainter, QMovie
from Vue.Windows.ui_WaitingWindows import Ui_Form

#============================================================================#
# Variable
#============================================================================#

#============================================================================#
# Fonction
#============================================================================#

#============================================================================#
# Classe 
#============================================================================#

#-----------------------------------------------------------------------------
# Class fenêtre loader
#-----------------------------------------------------------------------------
class LoadingScreen(QWidget, Ui_Form):
 #----------------------------------------------
 # Signaux
 #----------------------------------------------
 siOpen  = Signal()
 siClose = Signal()

 #----------------------------------------------
 # Init
 #----------------------------------------------
 def __init__(self, parent=None):
  #super(LoadingScreen, self).__init__(parent=parent)
  super().__init__(parent)
  self.setupUi(self)
  self.setWindowFlags(Qt.ToolTip)
  #self.setWindowModality(Qt.ApplicationModal)
  self.setWindowModality(Qt.NonModal)

  tLabel_animation = QLabel(self)
  tLabel_animation.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
  self.movie = QMovie(":/Logo/Spinner-1s-100px (2).gif")

  self.gridLayout.addWidget(tLabel_animation,0,0,Qt.AlignVCenter)
  tLabel_animation.setMovie(self.movie)

 #----------------------------------------------
 # Show
 #----------------------------------------------
 def vFShow(self, sStatus):
  print("-- LoadingScreen > vFShow --")
  print(sStatus)
  self.siOpen.emit()
  self.label_2.setText(sStatus)
  self.movie.start()
  self.show()

 #----------------------------------------------
 # Update status
 #----------------------------------------------
 def updateStatus(self, sStatus):
  self.label_2.setText(sStatus)

 #----------------------------------------------
 # Close
 #----------------------------------------------
 def vFClose(self):
  print("-- LoadingScreen > vFClose --")
  self.siClose.emit()
  self.movie.stop()
  self.close()
