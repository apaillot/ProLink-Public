# -*- coding: utf-8 -*-
#============================================================================#
# Fichier .........: "QuectelSerial.py"
# Auteur ..........: Alexandre Paillot
# Date de création : 2021.10.08
#----------------------------------------------------------------------------#
''' Description :
    Gestion bas niveau du port série.
'''
#============================================================================#

#============================================================================#
# Déclaration des librairies standart
#============================================================================#
import os
import sys
import time
import datetime
import serial
import glob
import serial.tools.list_ports
import traceback
from datetime import datetime

#============================================================================#
# Déclaration des librairies Qt
#============================================================================#
from PySide6.QtCore import Slot, QByteArray, Signal, QObject, QIODevice, QTimer
from PySide6.QtSerialPort  import *
from PySide6 import QtSerialPort

#============================================================================#
# Déclaration des librairies projet
#============================================================================#
if __name__ == '__main__':
 sys.path.insert(1, os.getcwd())
 sys.path.insert(1, "../")
#from Composants.TLog import *

#============================================================================#
# Déclaration des fonctions
#============================================================================#

#----------------------------------------------------------------------------#
# Test si un port COM existe
#----------------------------------------------------------------------------#
def bFIsCOMPortExist( sCOM ):
 comlist = serial.tools.list_ports.comports()
 connected = []
 for element in comlist:
  connected.append( element.device )
  if( sCOM == element.device ): return( True )
 #print( "Connected COM ports: " + str( connected ) )
 return( False )

#============================================================================#
# Déclaration des classes
#============================================================================#

#-------------------------------------------------------
# Gestion de la liaison série bas niveau
#-------------------------------------------------------
class TSerial(QObject):
 # Déclaration des signaux
 siCMDFinished         = Signal(str)
 siError               = Signal(str)
 siContinuousBytesRead = Signal(bytes)
 siProgress            = Signal(int)

 #--------------------------
 # Constructeur de ma classe
 #--------------------------
 def __init__( self, parent=None ):
  super().__init__(parent)
  # Handler du port série
  self.m_tPort = None
  # Configuration
  self.sPortCOM    = ""
  self.uliBaudrate = 19200
  # Data flow control
  self.m_bRtsCts   = True
  # Request/Send flow control
  self.m_bDsrDtr   = True
  # Timeout
  #self.m_uiTimeout = 0.25
  self.m_uiTimeout = 0.5
  # Mode lecture continue
  self.bContinuousMode = False
  # Open serial port
  self.tSerial = QtSerialPort.QSerialPort()
  self.tSerial.setPortName(self.sPortCOM)
  self.tSerial.setBaudRate(QSerialPort.BaudRate.Baud19200)
  self.tSerial.setParity(QSerialPort.Parity.NoParity)
  self.tSerial.setDataBits(QSerialPort.DataBits.Data8)
  self.tSerial.setStopBits(QSerialPort.StopBits.OneStop)
  # Test ajout
  self.tSerial.readyRead.connect(self.vFReadFromSerial)
  print("self.tSerial.readBufferSize = %d"%self.tSerial.readBufferSize())
  # Timeout entre écriture et lecture
  self.uiReadTimeout = 5000
  self.tTimeoutTimer = QTimer()
  self.tTimeoutTimer.setSingleShot(True)
  self.tTimeoutTimer.setInterval(self.uiReadTimeout)
  self.tTimeoutTimer.timeout.connect(self.vFReqTimeout)
  # Buffer de lecture
  self.tReadBuff = []

 #--------------------------
 # Durée du timeout
 #--------------------------
 def setReadTimeout( self, uiTimeout ):
  self.uiReadTimeout = uiTimeout
  self.tTimeoutTimer.setInterval(self.uiReadTimeout)

 #--------------------------
 # Ouverture du port
 #--------------------------
 def tsFCOMPortList( self ):
  comlist = serial.tools.list_ports.comports()
  tsCOMPortList = []
  for element in comlist:
   tsCOMPortList.append( element.device )
  print( "Connected COM ports: " + str( tsCOMPortList ) )
  # On retourne les ports COM
  return( tsCOMPortList )

 #--------------------------
 # Port COM
 #--------------------------
 def vFSetPortCOM( self, sCOM ):
  self.sPortCOM    = sCOM
  self.tSerial.setPortName(self.sPortCOM)

 #--------------------------
 # Ouverture du port
 #--------------------------
 def bFOpen( self ):
  print("-- bFOpen --")
  print(self.sPortCOM)
  print(self.uliBaudrate)
  # Open serial port
  if( self.tSerial.open(QIODevice.ReadWrite) ):
   return( True )
  else:
   print("TSerialQt non ouvert")
   return(False)

 #--------------------------
 # Ouverture du port
 #--------------------------
 def bFIsOpen( self ):
  # Test si port ouvert
  return( self.m_tPort.isOpen() )

 #--------------------------
 # Ouverture du port
 #--------------------------
 def bFClose( self ):
  print("===== bFClose ======")
  # Test si port ouvert
  return( self.tSerial.close() )

 #--------------------------
 # Passage en mode continue
 #--------------------------
 def vFSetContinuousMode( self ):
  print("-- vFSetContinuousMode --")
  # Test si port ouvert
  self.bContinuousMode = True
  # Timeout
  self.setReadTimeout(8000)

 #--------------------------
 # Passage en mode continue
 #--------------------------
 def vFStopContinuousMode( self ):
  print("-- vFStopContinuousMode --")
  # Test si port ouvert
  self.bContinuousMode = False
  # Timeout
  self.setReadTimeout(3000)
  # Stop du timeout
  self.tTimeoutTimer.stop()
  # Fermeture
  self.tSerial.close()


 #--------------------------
 # Envoi d'une commande
 #--------------------------
 def bFWriteSDIInit( self, tucBytes, uiResponseSize ):
   # Conservation de la taille de réponse
   self.uiTotalResponseSize = uiResponseSize
   self.uiReceivedSize = 0
   self.uiRetryCpt = 0
   self.tReadBuff = QByteArray()
   try:
    # Open serial port
    if (not self.tSerial.open(QIODevice.ReadWrite)):
     print("TSerialQt non ouvert")
     return (False)
    self.tTimeoutTimer.start()  # Debug
    print(tucBytes)
    self.tSerial.clear()
    self.tSerial.setBreakEnabled(True)
    time.sleep(0.1)
    self.tSerial.setBreakEnabled(False)
    time.sleep(0.01)
    self.tSerial.write(tucBytes)
    self.tSerial.waitForBytesWritten(100)
    # Si pas d'octet à lire
    if (self.uiTotalResponseSize == 0):
     print("self.uiTotalResponseSize == 0")
    # Fin de réponse attendue
    return (True)
   # Gestion des erreurs
   except Exception as err1:
    # Erreur
    print(repr(err1))
    print(traceback.format_exc())
    # Fin de réponse attendue
    return (False)

 #--------------------------
 # Envoi d'une commande
 #--------------------------
 def bFWrite( self, tucBytes, uiResponseSize ):
  print("-- TSerialQt > bFWrite --")
  # Conservation de la taille de réponse
  self.uiTotalResponseSize = uiResponseSize
  self.uiReceivedSize = 0
  self.tReadBuff = QByteArray()
  try:
   # Open serial port
   if( not self.tSerial.open(QIODevice.ReadWrite) ):
    print("TSerialQt non ouvert")
    return(False)

   if( self.uiTotalResponseSize < 512 ):
    print( tucBytes )
    print( tucBytes.encode() )

   # Formattage binaire
   txRTCData = tucBytes.encode()
   # Ecriture
   self.tSerial.clear()
   self.tSerial.write( txRTCData )
   # Attente envoi octets
   self.tSerial.waitForBytesWritten(10)
   self.tTimeoutTimer.start()
   return( True )
  # Gestion des erreurs
  except Exception as err1:
   # Erreur
   print( repr( err1 ) )
   print( traceback.format_exc() )
   # Fin de réponse attendue
   return( False )

 #--------------------------
 # Envoi octet reveil
 #--------------------------
 def bFWriteDummyByte(self):
  try:
   # Open serial port
   if( not self.tSerial.open(QIODevice.ReadWrite) ):
    print("TSerialQt non ouvert")
    return(False)
   tAwakeByte = bytearray()
   tAwakeByte.append(0x0)
   self.tSerial.write( tAwakeByte )
   self.tSerial.waitForBytesWritten(10)
   #time.sleep(0.01)
   # Fermeture
   self.tSerial.close()
  # Gestion des erreurs
  except Exception as err1:
   # Erreur
   print( repr( err1 ) )
   print( traceback.format_exc() )
   # Fin de réponse attendue
   return( False )

 #--------------------------
 # Envoi d'une commande
 #--------------------------
 def bFWriteRaw( self, tucBytes, uiResponseSize ):
  # Conservation de la taille de réponse
  self.uiTotalResponseSize = uiResponseSize
  self.uiReceivedSize = 0
  self.uiRetryCpt     = 0
  self.tReadBuff = QByteArray()
  try:
   # Open serial port
   if( not self.tSerial.open(QIODevice.ReadWrite) ):
    print("TSerialQt non ouvert")
    return(False)
   self.tTimeoutTimer.start() # Debug
   print( tucBytes )
   self.tSerial.clear()
   self.tSerial.write( tucBytes )
   self.tSerial.waitForBytesWritten(100)
   # Si pas d'octet à lire
   if( self.uiTotalResponseSize == 0 ):
    print("self.uiTotalResponseSize == 0")
   # Fin de réponse attendue
   return( True )
  # Gestion des erreurs
  except Exception as err1:
   # Erreur
   print( repr( err1 ) )
   print( traceback.format_exc() )
   # Fin de réponse attendue
   return( False )

 #--------------------------
 # Callback lecture de donnée
 #--------------------------
 def vFReadFromSerial( self ):
  # Si gros paquet : pas de print
  #if( self.uiTotalResponseSize < 512 ):
  # print("-- vFReadFromSerial --")
  # print( datetime.now() )
  # Lecture de la donnée
  tReadBuff = self.tSerial.readAll()
  self.uiReceivedSize = self.uiReceivedSize + len(tReadBuff)
  # Visu
  #print(tReadBuff)
  #print(len(tReadBuff))
  #
  self.tReadBuff.append(tReadBuff)

  # Si petit paquet uniquement : Print
  """
  if( self.uiTotalResponseSize < 512 ):
   print("TOTAL")
   print(len(self.tReadBuff))
   print(self.tReadBuff)
  else:
   self.siProgress.emit(self.uiReceivedSize)
  """

  # Si mode lecture continue
  if( self.bContinuousMode ):
   # Signal de lecture
   self.siContinuousBytesRead.emit(tReadBuff)
   return

  # Controle la taille
  if(   not self.bContinuousMode
    and (  ( self.uiTotalResponseSize == 0 )
        or ( self.uiReceivedSize >= self.uiTotalResponseSize ) ) ):
   print( "vFReadFromSerial OUT" )
   print( "self.uiReceivedSize = %u"%self.uiReceivedSize )
   print( "self.uiTotalResponseSize = %u"%self.uiTotalResponseSize )
   # Stop du timeout
   self.tTimeoutTimer.stop()
   # Déconnexion
   #self.tSerial.readyRead.disconnect(self.vFReadFromSerial)
   # Fermeture
   self.tSerial.close()
   #
   self.siCMDFinished.emit("")
  # Pas fini
  else:
   # Relance timeout
   self.tTimeoutTimer.stop()
   self.tTimeoutTimer.start()

 #--------------------------
 # Timeout
 #--------------------------
 def vFReqTimeout( self ):
  print("-- vFReqTimeout --")

  # Déconnexion
  #self.tSerial.readyRead.disconnect(self.vFReadFromSerial)
  # Fermeture
  self.tSerial.close()
  # Si octet à lire
  if( self.uiTotalResponseSize != 0 ):
   # Fin de requête
   self.siCMDFinished.emit("Timeout")
  else:
   # Fin de requête
   self.siCMDFinished.emit("")

 #--------------------------
 # Fermeture du port
 #--------------------------
 def vFClosePort( self ):
  print("-- vFClosePort --")
  # Fermeture
  self.tSerial.close()
  self.tTimeoutTimer.stop()

 #--------------------------
 # Démarrage d'une lecture en continue
 #--------------------------
 def vFReadContinuousStart( self ):
  print("-- vFReadContinuousStart --")
  # Try
  try:
   # Open serial port
   if( not self.tSerial.open(QIODevice.ReadWrite) ):
    print("TSerialQt non ouvert")
    return(False)
   # Réinit du compteur
   self.uiReceivedSize = 0
   # Mode continue
   self.bContinuousRead = True
  # Gestion des erreurs
  except Exception as err1:
   # Erreur
   print( repr( err1 ) )
   print( traceback.format_exc() )
   # Fin de réponse attendue
   return( False )
 #--------------------------
 # Stop de la lecture en continue
 #--------------------------
 def vFReadContinuousStop( self ):
  print("-- vFReadContinuousStop --")
  # Reinit mode continue
  self.bContinuousRead = False
  # Déconnexion
  #self.tSerial.readyRead.disconnect(self.vFReadFromSerial)
  # Fermeture
  #self.tSerial.close()
  # Fin de requête
  self.siCMDFinished.emit("Timeout")

#----------------------------------------------------------------------------#
# Test unitaire
#----------------------------------------------------------------------------#
if __name__ == '__main__':
 # Constructeur
 m_tSerial = TSerial()
 m_tSerial.bFCOMPortList()
 print("Test si port COM79 existe")
 if( bFIsCOMPortExist("COM79") ):
  print("Exist")
 else:
  print("Not exist")
 '''
 print("Test si port /dev/ttyUSB2 existe")
 if( bFIsCOMPortExist("/dev/ttyUSB2") ):
  print("Exist")
 else:
  print("Not exist")
 '''
