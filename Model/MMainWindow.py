# This Python file uses the following encoding: utf-8

#============================================================================#
# Librairies système
#============================================================================#
import sys
import io, csv
import serial
import serial.tools.list_ports as port_list
import time
import struct
import random
import logging
from datetime import datetime
import copy

#============================================================================#
# Librairies Qt
#============================================================================#
from PySide6.QtCore import QObject, QThread, Signal, Slot, QTimer, QDateTime

#============================================================================#
# Librairies Utilisateur
#============================================================================#
from Product.Sonde.TProduct import TProduct
from Model.MSonde           import MSonde
from Model.MProbe           import MProbe
from Model.MLeveLine        import MLeveLine

#============================================================================#
# Variable
#============================================================================#

#============================================================================#
# Classe
#============================================================================#

#------------------------------------------------------------------------
# Thread
#------------------------------------------------------------------------
#--------------------------------------------
# Détection produit
#--------------------------------------------
'''
class DetectProductWorker(QObject):
 siFinished = Signal()
 """Long-running task."""
 @Slot(TProduct)
 def run(self, tProduct):
  # Lancement d'une détection automatique
  tProduct.vFSondeList()
  #self.progress.emit(i + 1)
  self.siFinished.emit()
'''

#------------------------------------------------------------------------
# Main Windows
#------------------------------------------------------------------------
class MMainWindow(QObject):
 #----------------------------------------------
 # Signaux
 #----------------------------------------------
 #-- General
 siErrorMsg                     = Signal(str, str)
 #-- Connexion
 siDetectProductEnd             = Signal(dict)

 #----------------------------------------------
 # Init
 #----------------------------------------------
 def __init__(self, parent=None):
  # Init QObject
  super(MMainWindow, self).__init__(parent=parent)
  # Initialisation avec objet generique
  #self.tProduct = TProduct()
  # Port com
  self.sCom = "COM8"

  # Déclaration modèle pour sonde
  self.tMSonde = MSonde()
  # Déclaration modèle pour sonde
  self.tMProbe = MProbe()
  # Déclaration modèle pour LeveLine
  self.tMLeveLine = MLeveLine()



