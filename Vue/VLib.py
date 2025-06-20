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

#-----------------------------
# Ouverture/gestion popup d'attente
#-----------------------------
def vFCenterChildOnWindow(tParent, tChild):
 uiCenterWindowX = tParent.x() + tParent.frameGeometry().width() / 2
 uiCenterWindowY = tParent.y() + tParent.frameGeometry().height() / 2

 uiChildWidth  = tChild.frameGeometry().width()
 uiChildHeight = tChild.frameGeometry().height()
 tChild.setGeometry( int(uiCenterWindowX - uiChildWidth/2),
                     int(uiCenterWindowY - uiChildHeight/2),
                     tChild.frameGeometry().width(),
                     tChild.frameGeometry().height() )

#-----------------------------------------------------------------------------
# Ouverture d'une fenêtre d'alerte
#-----------------------------------------------------------------------------
def vFAlert(sParent, sTitle, sMsg):
 print("== vFAlert ==")
 msg = QMessageBox(sParent)
 msg.setIcon(QMessageBox.Information)
 msg.setText(sMsg)
 #msg.setInformativeText("This is additional information")
 msg.setWindowTitle(sTitle)
 #msg.setDetailedText("The details are as follows:")
 msg.exec()
 #vFCenterChildOnWindow(sParent, msg)

#============================================================================#
# Classe secondaire
#============================================================================#
