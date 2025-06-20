# -*- coding: utf-8 -*-
#============================================================================#
# Fichier .........: "TProduct.py"
# Auteur ..........: Alexandre Paillot
# Date de création : 2024/11/18
#----------------------------------------------------------------------------#
''' Description :
    Class generic pour produit aquaread.
    Les différents produits doivent pouvoir hériter de cette classe.

'''
#============================================================================#

#============================================================================#
# Déclaration des librairies standart
#============================================================================#
import os
import sys
import time
import datetime
import serial, io
import serial.tools.list_ports
import traceback
import struct

#============================================================================#
# Déclaration des librairies Qt
#============================================================================#
from PySide6.QtCore import QByteArray, Signal, QObject, QTimer
from PySide6.QtCore import QIODevice
from PySide6.QtSerialPort  import *
from PySide6 import QtSerialPort

#============================================================================#
# Déclaration des librairies projet
#============================================================================#
if __name__ == '__main__':
 # Debug
 from PySide6.QtWidgets import QApplication
 sys.path.insert(1, os.getcwd())
 sys.path.insert(1, "../")

#============================================================================#
# Librairies Utilisateur
#============================================================================#
from Product.LeveLine.TSerialQt     import TSerial
from Product.LeveLine.TConfigParser import TConfigParser

#============================================================================#
# Déclaration des fonctions
#============================================================================#

#============================================================================#
# Déclaration des classes
#============================================================================#

#-------------------------------------------------------
# Gestion de la liaison série bas niveau
#-------------------------------------------------------
class TProduct(QObject):
 # Déclaration des signaux
 siError                  = Signal(str)
 #siRequestTimeout         = Signal(str)
 siDetectProductEnd       = Signal(dict)
 siConfigurationReadEnd   = Signal(dict, str)
 siConfigurationReadError = Signal(str)
 #-- Dashboard
 siDateTimeSondeWriteEnd = Signal()
 siSiteIDWriteEnd        = Signal()
 siPositionWriteEnd      = Signal()
 siLogIntervalWriteEnd   = Signal()
 siLogDataForWriteEnd    = Signal()
 siEventLogCheckPeriodWriteEnd = Signal()
 siEventLogCheckLimitWriteEnd  = Signal()
 siClearMemoryEnd        = Signal()
 siResetLeveLineEnd      = Signal()
 #-- Signal - Liveview
 siMeasureDataReadEnd     = Signal(dict)
 #-- Calibration
 siCalibrationCMDPointEnd = Signal()
 #siCalibrateECEnd

 #--------------------------
 # Constructeur de ma classe
 #--------------------------
 def __init__( self, parent=None ):
  # Init QObject
  super(TProduct, self).__init__(parent=parent)
  # Création port COM
  self.tSerial = TSerial()
  # Parser de config
  self.tConfigParser = TConfigParser()
  # Configuration port COM
  self.tSerial.uliBaudrate = 115200
  self.tSerial.sPortCOM    = "COM79"
  # Configuration des produits détecté
  self.ttDetectedProduct = {}
  # Configuration du produit
  self.ttConfig = {}
  # Init de la configuration
  self.tConfigParser.vFInitConfigObj(self.ttConfig)
  # Liste des requêtes init
  self.uiInitRequestCpt = 0
  self.tInitRequest = []
  self.tInitRequest.append({ "sReq":"$R", "uiResponseSize": 18, "bFDecode":self.tConfigParser.bFParseSerialNumber })
  self.tInitRequest.append({ "sReq":"$T", "uiResponseSize": 10, "bFDecode":self.tConfigParser.bFParseSensorType })
  self.tInitRequest.append({ "sReq":"$O", "uiResponseSize": 18, "bFDecode":self.tConfigParser.bFParseCalDate })
  self.tInitRequest.append({ "sReq":"$W", "uiResponseSize": 47, "bFDecode":self.tConfigParser.bFParseIdentAndPosition })
  self.tInitRequest.append({ "sReq":"$B", "uiResponseSize": 13, "bFDecode":self.tConfigParser.bFParseLogInterval })
  self.tInitRequest.append({ "sReq":"$J", "uiResponseSize": 18, "bFDecode":self.tConfigParser.bFParseLogStartDatetime })
  self.tInitRequest.append({ "sReq":"$L", "uiResponseSize": 11, "bFDecode":self.tConfigParser.bFParseLogDuration })
  self.tInitRequest.append({ "sReq":"$D", "uiResponseSize": 13, "bFDecode":self.tConfigParser.bFParseEventInterval })
  self.tInitRequest.append({ "sReq":"$F", "uiResponseSize": 15, "bFDecode":self.tConfigParser.bFParseEventLimits })
  self.tInitRequest.append({ "sReq":"$H", "uiResponseSize": 18, "bFDecode":self.tConfigParser.bFParseDatetime })
  self.tInitRequest.append({ "sReq":"$b", "uiResponseSize": 18, "bFDecode":self.tConfigParser.bFParseLiveData })
  self.tInitRequest.append({ "sReq":"$P", "uiResponseSize": 16, "bFDecode":self.tConfigParser.bFParseStatus })

 #--------------------------
 # Détection de produit
 #--------------------------
 def vFSondeList( self ):
  print("== bFCOMPortList ==")
  # Lancement de la détection des ports COM présent
  self.tsCOMPortList = self.tSerial.tsFCOMPortList()
  ##TODO - Debug forçage
  #self.tsCOMPortList = []
  # Vérification qu'au moins un port COM détecté
  if( len(self.tsCOMPortList) > 0 ):
   self.uiComCpt = 0
   print(self.tsCOMPortList)
   print(self.tsCOMPortList[self.uiComCpt])
   # Timeout
   self.tSerial.setReadTimeout( 1000 )
   # Connexion lecture
   #self.tSerial.siCMDFinished.connect( self._vFProductGetSetupDataSondeDetectEnd )
   # Init objet configuration
   self.tsProductList = {}
   # Première détection
   #self._vFProductGetSondeDetectSDI12()
   self._vFProductDetectSondeStart()
  # Pas de port COM de détecté
  else:
   print("Pas de port COM")
   self.ttDetectConfig = {}
   # Signal de fin de détection
   self.siDetectProductEnd.emit()

 #----------------------------------------------
 # Passage en SDI12
 #----------------------------------------------
 def _vFProductSetSDI12Params( self ):
  print("== _vFProductSetSDI12Params ==")
  self.tSerial.tSerial.setBaudRate(QSerialPort.BaudRate.Baud1200)
  self.tSerial.tSerial.setParity(QSerialPort.Parity.EvenParity)
  self.tSerial.tSerial.setDataBits(QSerialPort.DataBits.Data7)
  self.tSerial.tSerial.setStopBits(QSerialPort.StopBits.OneStop)

 #----------------------------------------------
 # Passage en PC Mode
 #----------------------------------------------
 def _vFProductSetPCModeParams( self ):
  print("== _vFProductSetPCModeParams ==")
  self.tSerial.tSerial.setBaudRate(QSerialPort.BaudRate.Baud115200)
  self.tSerial.tSerial.setParity(QSerialPort.Parity.NoParity)
  self.tSerial.tSerial.setDataBits(QSerialPort.DataBits.Data8)
  self.tSerial.tSerial.setStopBits(QSerialPort.StopBits.OneStop)

 #----------------------------------------------
 # Requête numéro de série
 #----------------------------------------------
 def _vFProductDetectSondeStart( self ):
  print("-- _vFProductDetectSondeStart --")
  # Init du compteur
  self.uiRequestCpt = 0
  # Com port actuel
  self.sCOM = self.tsCOMPortList[self.uiRequestCpt]
  self.tSerial.vFSetPortCOM(self.sCOM)
  # Lancement de la requête
  self._vFProductGetSondeDetectSDI12()

 #----------------------------------------------
 def _vFProductDetectSondeContinue( self ):
  print("-- _vFProductDetectSondeContinue --")
  # Incrément du compteur
  self.uiRequestCpt += 1
  # Test si fin du tableau des ports séries trouvés
  if( self.uiRequestCpt < len(self.tsCOMPortList) ):
   print("------------------------------------")
   print("NOUVELLE DETECTION : "+self.tsCOMPortList[self.uiRequestCpt])
   # Com port actuel
   self.sCOM = self.tsCOMPortList[self.uiRequestCpt]
   self.tSerial.vFSetPortCOM(self.sCOM)
   # Lancement de la requête
   self._vFProductGetSondeDetectSDI12()
   return
  # Fin de détection
  print("END OF DETECTION")
  print(self.ttDetectedProduct)
  # Signal de fin de détection
  self.siDetectProductEnd.emit(self.ttDetectedProduct)
 #----------------------------------------------
 #----------------------------------------------
 # Détection en mode SDI-12
 #----------------------------------------------
 def _vFProductGetSondeDetectSDI12( self ):
  print("-- _vFProductGetSondeDetectSDI12 --")
  # Vérification que le port est présent
  try:
   # Passage en mode SDI-12
   self._vFProductSetSDI12Params()
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self._vFProductGetSondeDetectSDI12End )
   # Port COM
   if( self.tSerial.bFWriteSDIInit( b'?I!', 30 ) ):
    print("_vFProductGetSerialNumber > Successfully sent")
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect( self._vFProductGetSondeDetectSDI12End )
  #self.siError.emit("Failed to open port 1")
  # Passage au port suivant
  self._vFProductDetectSondeContinue()
 #----------------------------------------------
 def _vFProductGetSondeDetectSDI12End( self, sError ):
  print("-- _vFProductGetSondeDetectSDI12End --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self._vFProductGetSondeDetectSDI12End )
  # Si erreur
  if( sError != "" ):
   print( sError )
   # On va tenter en mode PC
   self._vFProductSetPCModeParams()
   # Lancement de la requête
   self._vFProductGetSondeDetectPCMode()
   # On quitte ici
   return
  print("*************")
  # Récupération résultat
  sRead = self.tSerial.tReadBuff
  print(sRead)
  sRead = sRead[:30]
  # 013 AQUAREADLL-CTD 301 20434031 0
  txUnpacked = struct.unpack( '>3s14s3s8s1s1s', sRead )
  # Extraction de la réponse
  sProductName     = str(txUnpacked[1].decode())
  sFirmwareVersion = str(txUnpacked[2].decode())[0] + "." + str(txUnpacked[2].decode())[1:2]
  sSerialNumber    = str(txUnpacked[3].decode())
  sProbeMeterInd   = str(txUnpacked[4].decode())
  print("sFirmwareVersion = "+sFirmwareVersion)
  print("sSerialNumber    = "+sSerialNumber)
  print("sProbeMeterInd   = "+sProbeMeterInd)
  # Lecture donnée de calibration
  time.sleep(0.05)
  # Continue sur le prochain port com
  self._vFProductSwitchToPCMode()
 #----------------------------------------------
 def _vFProductSwitchToPCMode( self ):
  print("-- _vFProductSwitchToPCMode --")
  #
  self.tSerial.siCMDFinished.connect(self._vFProductSwitchToPCModeEnd)
  if( self.tSerial.bFWriteSDIInit( b'?XQ0!', 2 ) ):
   print("*************")
   print("_vFProductSwitchToPCMode > Successfully sent ?XQ0!")
   return
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect(self._vFProductSwitchToPCModeEnd)
 #----------------------------------------------
 def _vFProductSwitchToPCModeEnd( self, sError ):
  print("_vFProductSwitchToPCModeEnd")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect(self._vFProductSwitchToPCModeEnd)
  # Si erreur
  if( sError != "" ):
   # Erreur sur le port : on passe au suivant
   self._vFProductDetectSondeContinue()
   return
  print("*************")
  # Récupération résultat
  sRead = self.tSerial.tReadBuff
  # Tentative de décodage
  # self.tConfigParser.ttFParseRTCData( sRead, self.ttConfig )
  # Formattage produit
  # self.ttCurrentConfig = self.ttConfig
  # Délais
  time.sleep(0.05)

  # On passe en mode PC
  self._vFProductGetSondeDetectPCMode()
  # On interroge
  #self._vFProductGetSerialNumber()
  #self._vFProductInitRequestStart()
 #----------------------------------------------
 # Détection en mode PC
 #----------------------------------------------
 def _vFProductGetSondeDetectPCMode( self ):
  print("-- _vFProductGetSondeDetectPCMode --")
  # Vérification que le port est présent
  try:
   # Passage en mode PC
   self._vFProductSetPCModeParams()
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self._vFProductGetSondeDetectPCModeEnd )
   sCMD = self.sFTProductGenerateCMD("$R")
   # Port COM
   if( self.tSerial.bFWriteRaw( sCMD, 18 ) ):
    print("_vFProductGetSerialNumber > Successfully sent")
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect( self._vFProductGetSondeDetectPCModeEnd )
 #----------------------------------------------
 def _vFProductGetSondeDetectPCModeEnd( self, sError ):
  print("-- _vFProductGetSondeDetectPCModeEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self._vFProductGetSondeDetectPCModeEnd )
  # Si erreur
  if( sError != "" ):
   # Pas détecté sur le port : on passe au suivant
   self._vFProductDetectSondeContinue()
   return
  print("*************")
  # Récupération résultat
  sRead = self.tSerial.tReadBuff

  # Création et init de l'objet de configuration
  self.ttDetectedProduct[self.sCOM] = {}
  self.tConfigParser.vFInitConfigObj(self.ttDetectedProduct[self.sCOM])
  # Tentative de décodage
  self.tConfigParser.bFParseSerialNumber( sRead, self.ttDetectedProduct[self.sCOM] )
  # Lecture donnée de calibration
  time.sleep(0.05)
  self._vFProductGetSensorType()
 #----------------------------------------------
 # Requête numéro de série
 #----------------------------------------------
 def _vFProductGetSensorType( self ):
  print("-- _vFProductGetSensorType --")
  # Vérification que le port est présent
  try:
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self._vFProductGetSensorTypeEnd )
   sCMD = self.sFTProductGenerateCMD("$T")
   # Port COM
   if( self.tSerial.bFWriteRaw( sCMD, 10 ) ):
    print("_vFProductGetSensorType > Successfully sent")
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect( self._vFProductGetSensorTypeEnd )
 #----------------------------------------------
 def _vFProductGetSensorTypeEnd( self, sError ):
  print("-- _vFProductGetSensorTypeEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self._vFProductGetSensorTypeEnd )
  # Si erreur
  if( sError != "" ):
   print( sError )
   if( sError == "Timeout" ):
    self.siRequestTimeout.emit()
    # Passe au port COM suivant
    self._vFProductDetectSondeContinue()
   return
  print("*************")
  # Récupération résultat
  sRead = self.tSerial.tReadBuff
  # $TA010*24<LF>
  # Tentative de décodage
  self.tConfigParser.bFParseSensorType( sRead, self.ttDetectedProduct[self.sCOM] )
  # Lecture donnée de calibration
  time.sleep(0.05)
  # Passe au port COM suivant
  self._vFProductDetectSondeContinue()


 #----------------------------------------------
 # Start Request
 #----------------------------------------------
 def vFProductGetConfiguration(self, sCOM):
  print("-- vFProductGetConfiguration --")
  # Définit le COM utilisé
  self.sCOM = sCOM
  self.tSerial.vFSetPortCOM(self.sCOM)
  # Init du compteur
  self.uiInitRequestCpt = 0
  # Démarrage
  self._vFProductInitRequest()
 #----------------------------------------------
 def _vFProductInitRequest(self):
  print("-- _vFProductInitRequest --")
  # Parcourt
  self._vFProductGetCMD( self.tInitRequest[self.uiInitRequestCpt]["sReq"],
                         self.tInitRequest[self.uiInitRequestCpt]["uiResponseSize"],
                         self.tInitRequest[self.uiInitRequestCpt]["bFDecode"] )
 #----------------------------------------------
 def _vFProductInitRequestEnd( self ):
  print("-- _vFProductInitRequestEnd --")
  # Incrément du compteur
  self.uiInitRequestCpt += 1
  # Si pas fini
  if( self.uiInitRequestCpt < len(self.tInitRequest) ):
   # Relance
   self._vFProductInitRequest()
  else:
   print("FIN DE BOUCLE")
   # Signal fin de lecture
   self.siConfigurationReadEnd.emit(self.ttConfig, self.sCOM)

 #----------------------------------------------
 # Requête generique pour l'initialisation
 #----------------------------------------------
 def _vFProductGetCMD(self, sCMD, uiResponseSize, bFDecode):
  print("-- _vFProductGetCMD --")
  print(sCMD)
  self.bFDecode = bFDecode
  # Vérification que le port est présent
  try:
   # Connexion lecture
   self.tSerial.siCMDFinished.connect(self._vFProductGetCMDEnd)
   sCMD = self.sFTProductGenerateCMD(sCMD)
   # Port COM
   if (self.tSerial.bFWriteRaw(sCMD, uiResponseSize)):
    print("_vFProductGetCMDEnd > Successfully sent")
    return
  except Exception as err:
   print(err)
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect(self._vFProductGetCMDEnd)
 # ----------------------------------------------
 def _vFProductGetCMDEnd(self, sError):
  print("-- _vFProductGetCMDEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect(self._vFProductGetCMDEnd)
  # Si erreur
  if( sError != "" ):
   print(sError)
   if( sError == "Timeout" ):
    self.siError.emit("Timeout")
   return
  print("*************")
  # Récupération résultat
  sRead = self.tSerial.tReadBuff
  # $O130224130224*4F<LF>
  # Tentative de décodage
  # self.tConfigParser.ttFParseRTCData( sRead, self.ttConfig )
  if( self.bFDecode != None ):
   self.bFDecode( sRead, self.ttConfig )
  # Lecture donnée de calibration
  time.sleep(0.005)
  # Fin
  self._vFProductInitRequestEnd()


 #----------------------------------------------
 # Append a checksum and line feed to a PC comms mode command string
 #----------------------------------------------
 def sFTProductGenerateCMD( self, sCMD ):
  sCMD += "*" + str(self.uiFPcAppendChk(sCMD)) + "\n"
  sCMD = sCMD.encode("utf-8")
  return( sCMD )

 #----------------------------------------------
 # Append a checksum and line feed to a PC comms mode command string
 #----------------------------------------------
 def uiFPcAppendChk( self, Cmd ):
  # Calculate checksum of command
  packet = Cmd[1:]
  # Init
  xor = 0
  i = 0
  while i < len(packet):
   xor = xor ^ ord(packet[i])
   i += 1
  print("%X"%xor)
  return("%X"%xor)

 #----------------------------------------------
 # Requête mesure
 #----------------------------------------------
 def bFProductGetLiveData( self ):
  print("-- bFProductGetLiveData --")
  # Vérification que le port est présent
  try:
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self._vFProductGetLiveDataEnd )
   sCMD = self.sFTProductGenerateCMD("$b")
   # Port COM
   if( self.tSerial.bFWriteRaw( sCMD, 18 ) ):
    print("_vFProductGetLiveData > Successfully sent")
    return( True )
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect( self._vFProductGetLiveDataEnd )
  return( False )
 #----------------------------------------------
 def _vFProductGetLiveDataEnd( self, sError ):
  print("-- _vFProductGetLiveDataEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self._vFProductGetLiveDataEnd )
  # Si erreur
  if( sError != "" ):
   print( sError )
   if( sError == "Timeout" ):
    self.siRequestTimeout.emit()
   return( False )
  print("*************")
  # Récupération résultat
  sRead = self.tSerial.tReadBuff
  # $R204340310301*53<LF>
  # Tentative de décodage
  self.tConfigParser.bFParseLiveData( sRead, self.ttConfig )
  # Lecture donnée de calibration
  time.sleep(0.05)
  #self._vFProductGetSensorType()
  # Signal de fin
  self.siMeasureDataReadEnd.emit(self.ttConfig)


 # ----------------------------------------------
 # Requête numéro de série
 # ----------------------------------------------
 def _vFProductGetSerialNumber( self ):
  print("-- _vFProductGetSerialNumber --")
  # Vérification que le port est présent
  try:
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self._vFProductGetSerialNumberEnd )
   sCMD = self.sFTProductGenerateCMD("$R")
   # Port COM
   if( self.tSerial.bFWriteRaw( sCMD, 18 ) ):
    print("_vFProductGetSerialNumber > Successfully sent")
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect( self._vFProductGetSerialNumberEnd )
 #----------------------------------------------
 def _vFProductGetSerialNumberEnd( self, sError ):
  print("-- _vFProductGetSerialNumberEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self._vFProductGetSerialNumberEnd )
  # Si erreur
  if( sError != "" ):
   print( sError )
   if( sError == "Timeout" ):
    self.siRequestTimeout.emit()
   return
  print("*************")
  # Récupération résultat
  sRead = self.tSerial.tReadBuff
  # $R204340310301*53<LF>
  # Tentative de décodage
  #self.tConfigParser.ttFParseRTCData( sRead, self.ttConfig )
  # Lecture donnée de calibration
  time.sleep(0.05)
  self._vFProductGetSensorType()
 #----------------------------------------------
 # Requête Cal date
 #----------------------------------------------
 def _vFProductGetCalDate( self ):
  print("-- _vFProductGetCalDate --")
  # Vérification que le port est présent
  try:
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self._vFProductGetCalDateEnd )
   sCMD = self.sFTProductGenerateCMD("$O")
   # Port COM
   if( self.tSerial.bFWriteRaw( sCMD, 18 ) ):
    print("_vFProductGetCalDateEnd > Successfully sent")
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect( self._vFProductGetCalDateEnd )
 #----------------------------------------------
 def _vFProductGetCalDateEnd( self, sError ):
  print("-- _vFProductGetCalDateEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self._vFProductGetCalDateEnd )
  # Si erreur
  if( sError != "" ):
   print( sError )
   if( sError == "Timeout" ):
    self.siRequestTimeout.emit()
   return
  print("*************")
  # Récupération résultat
  sRead = self.tSerial.tReadBuff
  # $O130224130224*4F<LF>
  # Tentative de décodage
  #self.tConfigParser.ttFParseRTCData( sRead, self.ttConfig )
  # Lecture donnée de calibration
  time.sleep(0.05)
  #self._vFProductGetCalibrationData()
 #----------------------------------------------
 # Requête Cal date
 #----------------------------------------------
 def _vFProductGetCalDate( self ):
  print("-- _vFProductGetCalDate --")
  # Vérification que le port est présent
  try:
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self._vFProductGetCalDateEnd )
   sCMD = self.sFTProductGenerateCMD("$O")
   # Port COM
   if( self.tSerial.bFWriteRaw( sCMD, 18 ) ):
    print("_vFProductGetCalDateEnd > Successfully sent")
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect( self._vFProductGetCalDateEnd )
 #----------------------------------------------
 def _vFProductGetCalDateEnd( self, sError ):
  print("-- _vFProductGetCalDateEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self._vFProductGetCalDateEnd )
  # Si erreur
  if( sError != "" ):
   print( sError )
   if( sError == "Timeout" ):
    self.siRequestTimeout.emit()
   return
  print("*************")
  # Récupération résultat
  sRead = self.tSerial.tReadBuff
  # $O130224130224*4F<LF>
  # Tentative de décodage
  #self.tConfigParser.ttFParseRTCData( sRead, self.ttConfig )
  # Lecture donnée de calibration
  time.sleep(0.05)
  #self._vFProductGetCalibrationData()

 #=============================================================================
 # Ecriture
 #=============================================================================
 #----------------------------------------------
 # Ecriture datetime
 #----------------------------------------------
 def bFProductDateTimeWrite( self ):
  print("-- bFProductDateTimeWrite --")
  # Vérification que le port est présent
  try:
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self.bFProductDateTimeWriteEnd )
   # Generation de la commande
   sCMD  = "$G"
   sCMD += "%02u"%self.ttConfig["PRODUCT"]["uiHour"]
   sCMD += "%02u"%self.ttConfig["PRODUCT"]["uiMin"]
   sCMD += "%02u"%self.ttConfig["PRODUCT"]["uiSec"]
   sCMD += "%02u"%self.ttConfig["PRODUCT"]["uiDay"]
   sCMD += "%02u"%self.ttConfig["PRODUCT"]["uiMonth"]
   sCMD += "%02u"%self.ttConfig["PRODUCT"]["uiYear"]
   sCMD = self.sFTProductGenerateCMD(sCMD)
   # Port COM
   if( self.tSerial.bFWriteRaw( sCMD, 6 ) ):
    print("_vFProductGetSensorType > Successfully sent")
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect( self.bFProductDateTimeWriteEnd )
 #----------------------------------------------
 def bFProductDateTimeWriteEnd( self, sError ):
  print("-- bFProductDateTimeWriteEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self.bFProductDateTimeWriteEnd )
  # Si erreur
  if( sError != "" ):
   print( sError )
   if( sError == "Timeout" ):
    self.siRequestTimeout.emit()
    # Passe au port COM suivant
    self.siError.emit("Datetime writing error")
   return
  print("*************")
  # Récupération résultat
  sRead = str(self.tSerial.tReadBuff)
  print(sRead)
  # Vérification réponse
  if( not "$G*47" in sRead ):
   print("Good")
   self.siError.emit("Datetime writing error")
  else:
   # Lecture donnée de calibration
   time.sleep(0.05)
   # Passe au port COM suivant
   self.siDateTimeSondeWriteEnd.emit()

 #----------------------------------------------
 # Ecriture site ID
 #----------------------------------------------
 def bFProductSiteIDWrite( self ):
  print("-- bFProductSiteIDWrite --")
  # Vérification que le port est présent
  try:
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self.bFProductSiteIDWriteEnd )
   # Generation de la commande
   sSiteID   = self.ttConfig["PRODUCT"]["sSiteID"]
   print("sSiteID   = "+sSiteID)
   # Ajout d'espace pour faire 16 octets
   for uiCpt in range(len(sSiteID), 16):
    sSiteID += " "
   print("len( sSiteID ) = %d"%len(sSiteID))
   # Generation de la commande
   sCMD  = "$V"
   sCMD += sSiteID
   sCMD  = self.sFTProductGenerateCMD(sCMD)
   print(sCMD)
   # Port COM
   if( self.tSerial.bFWriteRaw( sCMD, 6 ) ):
    print("bFProductSiteIDWrite > Successfully sent")
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect( self.bFProductSiteIDWriteEnd )
 #----------------------------------------------
 def bFProductSiteIDWriteEnd( self, sError ):
  print("-- bFProductSiteIDWriteEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self.bFProductSiteIDWriteEnd )
  # Si erreur
  if( sError != "" ):
   print( sError )
   if( sError == "Timeout" ):
    self.siRequestTimeout.emit()
    # Passe au port COM suivant
    self.siError.emit("Site ID writing error")
   return
  print("*************")
  # Récupération résultat
  sRead = str(self.tSerial.tReadBuff)
  print(sRead)
  # Vérification réponse
  if( not "$V*56" in sRead ):
   print("Good")
   self.siError.emit("Site ID writing error")
  else:
   # Lecture donnée de calibration
   time.sleep(0.05)
   # Passe au port COM suivant
   self.siSiteIDWriteEnd.emit()

 #----------------------------------------------
 # Ecriture position
 #----------------------------------------------
 def bFProductPositionWrite( self ):
  print("-- bFProductPositionWrite --")
  # Vérification que le port est présent
  try:
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self.bFProductPositionWriteEnd )
   # Generation de la commande
   sSiteLat  = self.ttConfig["PRODUCT"]["sLatitudeRaw"]
   sSiteLong = self.ttConfig["PRODUCT"]["sLongitudeRaw"]
   sAltitude = self.ttConfig["PRODUCT"]["sAltitudeRaw"]
   print("sSiteLat  = "+sSiteLat)
   print("sSiteLong = "+sSiteLong)
   print("sAltitude = "+sAltitude)
   # Commande
   sCMD  = "$U"
   sCMD += sSiteLat
   sCMD += sSiteLong
   sCMD += sAltitude
   sCMD = self.sFTProductGenerateCMD(sCMD)
   print(sCMD)
   # Port COM
   if( self.tSerial.bFWriteRaw( sCMD, 6 ) ):
    print("_vFProductGetSensorType > Successfully sent")
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect( self.bFProductPositionWriteEnd )
 #----------------------------------------------
 def bFProductPositionWriteEnd( self, sError ):
  print("-- bFProductPositionWriteEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self.bFProductPositionWriteEnd )
  # Si erreur
  if( sError != "" ):
   print( sError )
   if( sError == "Timeout" ):
    self.siRequestTimeout.emit()
    # Passe au port COM suivant
    self.siError.emit("Datetime writing error")
   return
  print("*************")
  # Récupération résultat
  sRead = str(self.tSerial.tReadBuff)
  print(sRead)
  # Vérification réponse
  if( not "$U*55" in sRead ):
   print("Good")
   self.siError.emit("Position writing error")
  else:
   # Lecture donnée de calibration
   time.sleep(0.05)
   # Passe au port COM suivant
   self.siPositionWriteEnd.emit()

 #----------------------------------------------
 # Ecriture log interval
 #----------------------------------------------
 def bFProductLogIntervalWrite( self ):
  print("-- bFProductLogIntervalWrite --")
  # Vérification que le port est présent
  try:
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self.bFProductLogIntervalWriteEnd )
   # Generation de la commande
   uiLogSec = self.ttConfig["PRODUCT"]["uiLogInterval"]
   print("uiLogSec = %07d"%uiLogSec)
   sLogSec = "%07u"%uiLogSec
   # Generation de la commande
   sCMD  = "$A"
   sCMD += sLogSec
   sCMD  = self.sFTProductGenerateCMD(sCMD)
   print(sCMD)
   # Port COM
   if( self.tSerial.bFWriteRaw( sCMD, 6 ) ):
    print("bFProductLogIntervalWrite > Successfully sent")
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect( self.bFProductLogIntervalWriteEnd )
 #----------------------------------------------
 def bFProductLogIntervalWriteEnd( self, sError ):
  print("-- bFProductLogIntervalWriteEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self.bFProductLogIntervalWriteEnd )
  # Si erreur
  if( sError != "" ):
   print( sError )
   if( sError == "Timeout" ):
    self.siRequestTimeout.emit()
    # Passe au port COM suivant
    self.siError.emit("Log interval writing error")
   return
  print("*************")
  # Récupération résultat
  sRead = str(self.tSerial.tReadBuff)
  print(sRead)
  # Vérification réponse
  if( not "$A*41" in sRead ):
   print("Good")
   self.siError.emit("Log interval writing error")
  else:
   # Lecture donnée de calibration
   time.sleep(0.05)
   # Passe au port COM suivant
   self.siLogIntervalWriteEnd.emit()

 #----------------------------------------------
 # Ecriture log date time
 #----------------------------------------------
 def bFProductLogDateTimeWrite( self ):
  print("-- bFProductLogDateTimeWrite --")
  # Vérification que le port est présent
  try:
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self.bFProductLogDateTimeWriteEnd )
   # Generation de la commande
   uiLogSec = self.ttConfig["PRODUCT"]["uiLogInterval"]
   print("uiLogSec = %07d"%uiLogSec)
   sLogSec = "%07u"%uiLogSec
   # Generation de la commande
   sCMD  = "$A"
   sCMD += sLogSec
   sCMD  = self.sFTProductGenerateCMD(sCMD)
   print(sCMD)
   # Port COM
   if( self.tSerial.bFWriteRaw( sCMD, 6 ) ):
    print("bFProductLogIntervalWrite > Successfully sent")
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect( self.bFProductLogDateTimeWriteEnd )
 #----------------------------------------------
 def bFProductLogDateTimeWriteEnd( self, sError ):
  print("-- bFProductLogDateTimeWriteEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self.bFProductLogDateTimeWriteEnd )
  # Si erreur
  if( sError != "" ):
   print( sError )
   if( sError == "Timeout" ):
    self.siRequestTimeout.emit()
    # Passe au port COM suivant
    self.siError.emit("Log interval writing error")
   return
  print("*************")
  # Récupération résultat
  sRead = str(self.tSerial.tReadBuff)
  print(sRead)
  # Vérification réponse
  if( not "$A*41" in sRead ):
   print("Good")
   self.siError.emit("Log interval writing error")
  else:
   # Lecture donnée de calibration
   time.sleep(0.05)
   # Passe au port COM suivant
   self.siLogIntervalWriteEnd.emit()

 #----------------------------------------------
 # Ecriture log date time
 #----------------------------------------------
 def bFProductLogDataForWrite( self ):
  print("-- bFProductLogDateTimeWrite --")
  # Vérification que le port est présent
  try:
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self.bFProductLogDataForWriteEnd )
   # Generation de la commande
   uiLogDuration = self.ttConfig["PRODUCT"]["uiLogDuration"]
   print("uiLogDuration = %05d"%uiLogDuration)
   sLogHour = "%05u"%uiLogDuration
   # Generation de la commande
   sCMD  = "$K"
   sCMD += sLogHour
   sCMD  = self.sFTProductGenerateCMD(sCMD)
   print(sCMD)
   # Port COM
   if( self.tSerial.bFWriteRaw( sCMD, 6 ) ):
    print("bFProductLogIntervalWrite > Successfully sent")
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect( self.bFProductLogDataForWriteEnd )
 #----------------------------------------------
 def bFProductLogDataForWriteEnd( self, sError ):
  print("-- bFProductLogDataForWriteEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self.bFProductLogDataForWriteEnd )
  # Si erreur
  if( sError != "" ):
   print( sError )
   if( sError == "Timeout" ):
    self.siRequestTimeout.emit()
    # Passe au port COM suivant
    self.siError.emit("Log duration writing error")
   return
  print("*************")
  # Récupération résultat
  sRead = str(self.tSerial.tReadBuff)
  print(sRead)
  # Vérification réponse
  if( not "$K*4B" in sRead ):
   print("Good")
   self.siError.emit("Log duration writing error")
  else:
   # Lecture donnée de calibration
   time.sleep(0.05)
   # Passe au port COM suivant
   self.siLogDataForWriteEnd.emit()

 #----------------------------------------------
 # Ecriture log date time
 #----------------------------------------------
 def bFProductLogDataForWrite( self ):
  print("-- bFProductLogDateTimeWrite --")
  # Vérification que le port est présent
  try:
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self.bFProductLogDataForWriteEnd )
   # Generation de la commande
   uiLogDuration = self.ttConfig["PRODUCT"]["uiLogDuration"]
   print("uiLogDuration = %05d"%uiLogDuration)
   sLogHour = "%05u"%uiLogDuration
   # Generation de la commande
   sCMD  = "$K"
   sCMD += sLogHour
   sCMD  = self.sFTProductGenerateCMD(sCMD)
   print(sCMD)
   # Port COM
   if( self.tSerial.bFWriteRaw( sCMD, 6 ) ):
    print("bFProductLogIntervalWrite > Successfully sent")
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect( self.bFProductLogDataForWriteEnd )
 #----------------------------------------------
 def bFProductLogDataForWriteEnd( self, sError ):
  print("-- bFProductLogDataForWriteEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self.bFProductLogDataForWriteEnd )
  # Si erreur
  if( sError != "" ):
   print( sError )
   if( sError == "Timeout" ):
    self.siRequestTimeout.emit()
    # Passe au port COM suivant
    self.siError.emit("Log duration writing error")
   return
  print("*************")
  # Récupération résultat
  sRead = str(self.tSerial.tReadBuff)
  print(sRead)
  # Vérification réponse
  if( not "$K*4B" in sRead ):
   print("Good")
   self.siError.emit("Log duration writing error")
  else:
   # Lecture donnée de calibration
   time.sleep(0.05)
   # Passe au port COM suivant
   self.siLogDataForWriteEnd.emit()

 #----------------------------------------------
 # Ecriture event log check period
 #----------------------------------------------
 def bFProductEventLogCheckPeriodWrite( self ):
  print("-- bFProductEventLogCheckPeriodWrite --")
  # Vérification que le port est présent
  try:
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self.bFProductEventLogCheckPeriodWriteEnd )
   # Generation de la commande
   uiEventInterval = self.ttConfig["PRODUCT"]["uiEventInterval"]
   print("uiEventInterval = %05d"%uiEventInterval)
   sEventInterval = "%07u"%uiEventInterval
   # Generation de la commande
   sCMD  = "$C"
   sCMD += sEventInterval
   sCMD  = self.sFTProductGenerateCMD(sCMD)
   print(sCMD)
   # Port COM
   if( self.tSerial.bFWriteRaw( sCMD, 6 ) ):
    print("bFProductEventLogCheckPeriodWrite > Successfully sent")
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect( self.bFProductEventLogCheckPeriodWriteEnd )
 #----------------------------------------------
 def bFProductEventLogCheckPeriodWriteEnd( self, sError ):
  print("-- bFProductEventLogCheckPeriodWriteEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self.bFProductEventLogCheckPeriodWriteEnd )
  # Si erreur
  if( sError != "" ):
   print( sError )
   if( sError == "Timeout" ):
    self.siRequestTimeout.emit()
    # Passe au port COM suivant
    self.siError.emit("Event log check period writing error")
   return
  print("*************")
  # Récupération résultat
  sRead = str(self.tSerial.tReadBuff)
  print(sRead)
  # Vérification réponse
  if( not "$C*43" in sRead ):
   print("Good")
   self.siError.emit("Event log check period writing error")
  else:
   # Lecture donnée de calibration
   time.sleep(0.05)
   # Passe au port COM suivant
   self.siLogDataForWriteEnd.emit()

 #----------------------------------------------
 # Ecriture event log check period
 #----------------------------------------------
 def bFProductEventLogCheckPeriodWrite( self ):
  print("-- bFProductEventLogCheckPeriodWrite --")
  # Vérification que le port est présent
  try:
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self.bFProductEventLogCheckPeriodWriteEnd )
   # Generation de la commande
   uiEventInterval = self.ttConfig["PRODUCT"]["uiEventInterval"]
   print("uiEventInterval = %05d"%uiEventInterval)
   sLogHour = "%07u"%uiEventInterval
   # Generation de la commande
   sCMD  = "$C"
   sCMD += sLogHour
   sCMD  = self.sFTProductGenerateCMD(sCMD)
   print(sCMD)
   # Port COM
   if( self.tSerial.bFWriteRaw( sCMD, 6 ) ):
    print("bFProductEventLogCheckPeriodWrite > Successfully sent")
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect( self.bFProductEventLogCheckPeriodWriteEnd )
 #----------------------------------------------
 def bFProductEventLogCheckPeriodWriteEnd( self, sError ):
  print("-- bFProductEventLogCheckPeriodWriteEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self.bFProductEventLogCheckPeriodWriteEnd )
  # Si erreur
  if( sError != "" ):
   print( sError )
   if( sError == "Timeout" ):
    self.siRequestTimeout.emit()
    # Passe au port COM suivant
    self.siError.emit("Event log check period writing error")
   return
  print("*************")
  # Récupération résultat
  sRead = str(self.tSerial.tReadBuff)
  print(sRead)
  # Vérification réponse
  if( not "$C*43" in sRead ):
   print("Good")
   self.siError.emit("Event log check period writing error")
  else:
   # Lecture donnée de calibration
   time.sleep(0.05)
   # Passe au port COM suivant
   self.siEventLogCheckPeriodWriteEnd.emit()

 #----------------------------------------------
 # Ecriture event log event limit
 #----------------------------------------------
 def bFProductEventLogLimitWrite( self ):
  print("-- bFProductEventLogLimitWrite --")
  # Vérification que le port est présent
  try:
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self.bFProductEventLogLimitWriteEnd )
   # Generation de la commande
   uiPressureLimit = self.ttConfig["PRODUCT"]["uiPressureLimit"]
   sPressureLimit = "%06u"%uiPressureLimit
   # Si CTD
   if( self.ttConfig["PRODUCT"]["bECSensor"] ):
    uiSalinityLimit = self.ttConfig["PRODUCT"]["uiSalinityLimit"]
    sSecondLimit  = "%03u"%uiSalinityLimit
   else:
    uiTemperatureLimit = self.ttConfig["PRODUCT"]["uiTempLimit"]
    sSecondLimit  = "%03u"%uiTemperatureLimit
   # Generation de la commande
   sCMD  = "$E"
   sCMD += sPressureLimit
   sCMD += sSecondLimit
   sCMD  = self.sFTProductGenerateCMD(sCMD)
   print(sCMD)
   # Port COM
   if( self.tSerial.bFWriteRaw( sCMD, 6 ) ):
    print("bFProductEventLogCheckPeriodWrite > Successfully sent")
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect( self.bFProductEventLogLimitWriteEnd )
 #----------------------------------------------
 def bFProductEventLogLimitWriteEnd( self, sError ):
  print("-- bFProductEventLogLimitWriteEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self.bFProductEventLogLimitWriteEnd )
  # Si erreur
  if( sError != "" ):
   print( sError )
   if( sError == "Timeout" ):
    self.siRequestTimeout.emit()
    # Passe au port COM suivant
    self.siError.emit("Event log check limit writing error")
   return
  print("*************")
  # Récupération résultat
  sRead = str(self.tSerial.tReadBuff)
  print(sRead)
  # Vérification réponse
  if( not "$E*45" in sRead ):
   print("Good")
   self.siError.emit("Event log check limit writing error")
  else:
   # Lecture donnée de calibration
   time.sleep(0.05)
   # Passe au port COM suivant
   self.siEventLogCheckLimitWriteEnd.emit()

 #----------------------------------------------
 # Ecriture Start/Stop product - Start date
 #----------------------------------------------
 def bFProductLogStartDateWrite( self ):
  print("-- bFProductLogStartDateWrite --")
  # Vérification que le port est présent
  try:
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self.bFProductLogStartDateWriteEnd )
   # Generation de la commande
   sLogDateRaw = self.ttConfig["PRODUCT"]["sLogDateRaw"]

   # Generation de la commande
   sCMD  = "$I"
   sCMD += sLogDateRaw
   sCMD  = self.sFTProductGenerateCMD(sCMD)
   print(sCMD)
   # Port COM
   if( self.tSerial.bFWriteRaw( sCMD, 6 ) ):
    print("bFProductLogStartDateWrite > Successfully sent")
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect( self.bFProductLogStartDateWriteEnd )
 #----------------------------------------------
 def bFProductLogStartDateWriteEnd( self, sError ):
  print("-- bFProductLogStartDateWriteEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self.bFProductLogStartDateWriteEnd )
  # Si erreur
  if( sError != "" ):
   print( sError )
   if( sError == "Timeout" ):
    self.siRequestTimeout.emit()
    # Passe au port COM suivant
    self.siError.emit("Start log date writing error")
   return
  print("*************")
  # Récupération résultat
  sRead = str(self.tSerial.tReadBuff)
  print(sRead)
  # Vérification réponse
  if( not "$I*49" in sRead ):
   print("Good")
   self.siError.emit("Start log date writing error")
  else:
   # Lecture donnée de calibration
   time.sleep(0.05)
   # Passe au port COM suivant
   self.siEventLogCheckLimitWriteEnd.emit()


 #----------------------------------------------
 # Clear memory
 #----------------------------------------------
 def bFProductClearMemory( self ):
  print("-- bFProductClearMemory --")
  # Vérification que le port est présent
  try:
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self.bFProductClearMemoryEnd )

   # Generation de la commande
   sCMD  = "$X"
   sCMD  = self.sFTProductGenerateCMD(sCMD)
   print(sCMD)
   # Port COM
   if( self.tSerial.bFWriteRaw( sCMD, 6 ) ):
    print("bFProductClearMemory > Successfully sent")
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect( self.bFProductClearMemoryEnd )
 #----------------------------------------------
 def bFProductClearMemoryEnd( self, sError ):
  print("-- bFProductClearMemoryEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self.bFProductClearMemoryEnd )
  # Si erreur
  if( sError != "" ):
   print( sError )
   if( sError == "Timeout" ):
    self.siRequestTimeout.emit()
    # Passe au port COM suivant
    self.siError.emit("Clear memory error")
   return
  print("*************")
  # Récupération résultat
  sRead = str(self.tSerial.tReadBuff)
  print(sRead)
  # Vérification réponse
  if( not "$X*58" in sRead ):
   print("Good")
   self.siError.emit("Clear memory error")
  else:
   # Lecture donnée de calibration
   time.sleep(0.05)
   # Passe au port COM suivant
   self.siClearMemoryEnd.emit()

 #----------------------------------------------
 # Reset LeveLine
 #----------------------------------------------
 def bFProductResetLeveLine( self ):
  print("-- bFProductResetLeveLine --")
  # Vérification que le port est présent
  try:
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self.bFProductResetLeveLineEnd )

   # Generation de la commande
   sCMD  = "$c"
   sCMD  = self.sFTProductGenerateCMD(sCMD)
   print(sCMD)
   # Port COM
   if( self.tSerial.bFWriteRaw( sCMD, 6 ) ):
    print("bFProductResetLeveLine > Successfully sent")
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect( self.bFProductResetLeveLineEnd )
 #----------------------------------------------
 def bFProductResetLeveLineEnd( self, sError ):
  print("-- bFProductResetLeveLineEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self.bFProductResetLeveLineEnd )
  # Si erreur
  if( sError != "" ):
   print( sError )
   if( sError == "Timeout" ):
    self.siRequestTimeout.emit()
    # Passe au port COM suivant
    self.siError.emit("Reset LeveLine error")
   return
  print("*************")
  # Récupération résultat
  sRead = str(self.tSerial.tReadBuff)
  print(sRead)
  # Vérification réponse
  if( not "$c*63" in sRead ):
   print("Good")
   self.siError.emit("Reset LeveLine error")
  else:
   # Lecture donnée de calibration
   time.sleep(0.05)
   # Passe au port COM suivant
   self.siResetLeveLineEnd.emit()

 #----------------------------------------------
 # Calibrate EC
 #----------------------------------------------
 def bFProductCalibrateEC( self ):
  print("-- bFProductCalibrateEC --")
  # Vérification que le port est présent
  try:
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self.bFProductCalibrateECEnd )

   # Generation de la commande
   sCMD  = "$e"
   sCMD += sLogDateRaw
   sCMD  = self.sFTProductGenerateCMD(sCMD)
   print(sCMD)
   # Port COM
   if( self.tSerial.bFWriteRaw( sCMD, 6 ) ):
    print("bFProductCalibrateEC > Successfully sent")
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect( self.bFProductCalibrateECEnd )
 #----------------------------------------------
 def bFProductCalibrateECEnd( self, sError ):
  print("-- bFProductCalibrateECEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self.bFProductCalibrateECEnd )
  # Si erreur
  if( sError != "" ):
   print( sError )
   if( sError == "Timeout" ):
    self.siRequestTimeout.emit()
    # Passe au port COM suivant
    self.siError.emit("Calibrate EC error")
   return
  print("*************")
  # Récupération résultat
  sRead = str(self.tSerial.tReadBuff)
  print(sRead)
  # Vérification réponse
  if( not "$e*63" in sRead ):
   print("Good")
   self.siError.emit("Reset LeveLine error")
  else:
   # Lecture donnée de calibration
   time.sleep(0.05)
   # Passe au port COM suivant
   self.siCalibrateECEnd.emit()
   self.siCalibrationCMDPointEnd.emit()

#----------------------------------------------------------------------------#
# Test unitaire
#----------------------------------------------------------------------------#
if __name__ == '__main__':
 print("Test unitaire")
 app = QApplication(sys.argv)

 # Déclaration objet
 tProduct = TProduct()
 # Liste des produits
 tProduct.vFSondeList()

 # Execution file
 sys.exit(app.exec())


