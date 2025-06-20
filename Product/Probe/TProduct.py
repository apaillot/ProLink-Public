# -*- coding: utf-8 -*-
#============================================================================#
# Fichier .........: "TProduct.py"
# Auteur ..........: Alexandre Paillot
# Date de création : 2024/02/19
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
import serial
import serial.tools.list_ports
import traceback
import struct

#============================================================================#
# Déclaration des librairies Qt
#============================================================================#
from PySide6.QtCore import QByteArray, Signal, QObject, QTimer

#============================================================================#
# Déclaration des librairies projet
#============================================================================#
if __name__ == '__main__':
 sys.path.insert(1, os.getcwd())
 sys.path.insert(1, "../")

#============================================================================#
# Librairies Utilisateur
#============================================================================#
from Product.Probe.TSerialQt     import TSerial
from Product.Probe.TConfigParser import TConfigParser

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
 siDetectProductEnd       = Signal(dict)
 siConfigurationReadEnd   = Signal(dict, str)
 siConfigurationReadError = Signal(str)
 siConfigSiteWriteEnd     = Signal()
 siUserSettingsWriteEnd   = Signal()
 siDateTimeSondeWriteEnd  = Signal()
 siAUXAssignementWriteEnd = Signal()
 siClearMemoryEndSuccess  = Signal()
 siNewBatteriesFittedEndSuccess = Signal()
 #-- Signal - Liveview
 siMeasureDataReadEnd     = Signal(dict)
 #-- Signal - Calibration
 siWiperStartEnd                 = Signal()
 siWiperStartError               = Signal(str)
 siCalibrationCMDPointEnd        = Signal()
 siCalibrationCMDPointError      = Signal(str)
 siCalibrationCMDRestorePointEnd = Signal()
 siCalibrationPointECIntroEnd    = Signal()
 siCalibrationStabilizeError     = Signal(str,str)
 #-- Signal - Data
 siRecordedDataReadStart           = Signal( int )
 siRecordedDataReadProgress        = Signal( int )
 siRecordedDataReadEnd             = Signal()
 siRecordedDataReadError           = Signal(str)
 siDataCalculatedParametersUpdated = Signal()
 #-- Timeout
 siRequestTimeout = Signal()
 #-- Erreur
 siError = Signal(str)

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
  self.tSerial.uliBaudrate = 19200
  self.tSerial.sPortCOM    = "COM79"
  self.uiDefaultTimeout    = 5000
  # Liste produit détecté
  self.tsProductList = []
  # Configuration du produit
  self.ttConfig = {}
  # Configuration du produit
  self.ttINIConfig = {}
  self.ttINIConfig["CALCULATED"] = {}
  self.ttINIConfig["CALCULATED"]["DEPTH"] = {}
  self.ttINIConfig["CALCULATED"]["TEMP"]  = {}
  self.ttINIConfig["CALCULATED"]["TDS"]   = {}
  self.ttINIConfig["CALCULATED"]["EC"]   = {}
  # Appel init configuration
  #self.vFConfigurationInit()
  # Init measurement data
  self.ttMeasure = []
  # Création timer loop
  self.tTimeoutWiper = QTimer()
  self.tTimeoutWiper.timeout.connect(self._vFProductWiperStartTimeout)
  # Création timer loop
  self.tTimerWiper = QTimer()
  self.tTimerWiper.timeout.connect(self._vFProductWiperStartLoop)
  # Initialisation valeur de pression
  self.bAirPressureInit = False

 #--------------------------
 # INI Config init
 #--------------------------
 def vFConfigurationInit( self ):
  print("== vFSondeList ==")
  # Configuration du produit
  self.ttConfig = {}
  # Init de la configuration
  self.tConfigParser.vFInitConfigObj(self.ttConfig)
  # Temperature unit
  self.ttConfig["CALCULATED"]["TEMP"]["bF"]     = self.ttINIConfig["CALCULATED"]["TEMP"]["bF"]
  self.ttConfig["CALCULATED"]["TEMP"]["bC"]     = self.ttINIConfig["CALCULATED"]["TEMP"]["bC"]
  # Depth unit
  self.ttConfig["CALCULATED"]["DEPTH"]["bM"]    = self.ttINIConfig["CALCULATED"]["DEPTH"]["bM"]
  self.ttConfig["CALCULATED"]["DEPTH"]["bF"]    = self.ttINIConfig["CALCULATED"]["DEPTH"]["bF"]
  # TDS Factor
  self.ttConfig["CALCULATED"]["TDS"]["fFactor"] = self.ttINIConfig["CALCULATED"]["TDS"]["fFactor"]
  # EC Temperature ref
  self.ttConfig["CALCULATED"]["EC"]["sTSelect"] = self.ttINIConfig["CALCULATED"]["EC"]["sTSelect"]
  #

 #--------------------------
 # Détection de produit
 #--------------------------
 def vFSondeList( self ):
  print("== vFSondeList ==")
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
   self.tSerial.setReadTimeout( 500 )
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self._vFProductGetSetupDataSondeDetectEnd )
   # Init objet configuration
   self.tsProductList = {}
   # Première détection
   self._vFProductGetSetupDataSondeDetect()
  # Pas de port COM de détecté
  else:
   print("Pas de port COM")
   self.ttDetectConfig = {}
   # Signal de fin de détection
   self.siDetectProductEnd.emit({})
 #----------------------------------------------
 # Requête setup data pour détection sonde
 #----------------------------------------------
 def _vFProductGetSetupDataSondeDetect( self ):
  print("== _vFProductGetSetupDataSondeDetect ==")
  try:
   print("===================================")
   print(self.tsCOMPortList[self.uiComCpt])
   print("---------------------")
   # Modification du port
   self.tSerial.vFSetPortCOM( self.tsCOMPortList[self.uiComCpt] )
   # Dummy bytes
   #self.tSerial.bFWriteDummyByte()
   #time.sleep(0.3)
   tucBytes = bytearray()
   tucBytes.append( 0xD1 )
   # Port COM
   if( self.tSerial.bFWriteRaw( tucBytes, 13, uiTimeoutCpt=0 ) ):
    print("*************")
    print("_vFProductGetSetupData > Successfully sent")
    return
  except Exception as err:
   print( err )
   print("_vFProductGetSetupData > Not successfully sent")
   try:
    self.tSerial.bFClose()
   except Exception as err2 :
    print(err2)
    print("Error: No product in this COM")
    raise Exception("Error: No product in this COM")
  self._vFProductGetSetupDataSondeDetectEnd("")
 #----------------------------------------------
 def _vFProductGetSetupDataSondeDetectEnd( self, sError ):
  print("-- _vFProductGetSetupDataSondeDetectEnd --")
  print( "sError = "+ sError )
  # Récupération résultat
  sRead = self.tSerial.tReadBuff
  print(sRead)
  print("len(sRead) = %d"%len(sRead))
  # Si reçu égal à la taille prévue
  if( len(sRead) == 13 ):
   print("AJOUT")
   # Ajout de la configuration à l'objet de réception
   self.tsProductList[ self.tsCOMPortList[self.uiComCpt] ] = sRead
  # Incrément du nombre de port COM
  self.uiComCpt = self.uiComCpt + 1
  print("self.uiComCpt = %d"% self.uiComCpt)
  # Si on a pas fini de faire la liste
  if( self.uiComCpt < len(self.tsCOMPortList) ):
   print("Relance prochain")
   # Relance avec un nouveau port
   self._vFProductGetSetupDataSondeDetect()
   # On quitte
   return

  print("_vFProductGetSetupDataSondeDetectEnd > Fin des relances")
  print(self.tsProductList)
  # Object des configurations détectées
  self.ttDetectConfig = {}

  print("Parcourt des COMs")
  # Parcourt des COMs
  for tElt in self.tsProductList:
   print(tElt)
   #
   self.ttDetectConfig[tElt] = {}
   self.tConfigParser.vFInitConfigObj( self.ttDetectConfig[tElt] )
   # Parse de la configuration
   self.tConfigParser.ttFParseSerialNumber( self.tsProductList[ tElt ],
                                            self.ttDetectConfig[tElt] )
  print( "self.ttDetectConfig" )
  print( self.ttDetectConfig )
  # Timeout
  self.tSerial.setReadTimeout( self.uiDefaultTimeout )
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self._vFProductGetSetupDataSondeDetectEnd )
  # Signal de fin de détection
  print("TProduct sonde > siDetectProductEnd.emit()")
  self.siDetectProductEnd.emit(self.ttDetectConfig)

 #----------------------------------------------
 # Requête de la configuration du produit
 #----------------------------------------------
 def vFProductGetConfiguration( self, sCOM ):
  print("-- vFProductGetConfiguration --")
  # Sauvegarde du port
  self.sCOM = sCOM
  # Modification du port
  self.tSerial.vFSetPortCOM( sCOM )
  # Première requête
  self._vFProductGetSN()
 #----------------------------------------------
 # Requête lecture SN
 #----------------------------------------------
 def _vFProductGetSN( self ):
  print("== _vFProductGetSN ==")
  # Vérification que le port est présent
  try:
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self._vFProductGetSNEnd )
   tucBytes = bytearray()
   tucBytes.append( 0xD1 )
   # Port COM
   if( self.tSerial.bFWriteRaw( tucBytes, 13 ) ):
    print("*************")
    print("_vFProductGetSN > Successfully sent")
    return
  except Exception as err:
   print("_vFProductGetSN > Exception as err")
   print( err )
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect( self._vFProductGetSNEnd )
  # Erreur
  print("_vFProductGetSN > Failed to open port")
  self.siError.emit("Failed to open port")
 #----------------------------------------------
 def _vFProductGetSNEnd( self, sError ):
  print("-- _vFProductGetSNEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self._vFProductGetSNEnd )
  # Si erreur
  if( sError != "" ):
   print( sError )
   if( sError == "Timeout" ):
    self.siRequestTimeout.emit()
   return
  print("*************")
  # Récupération résultat
  sRead = self.tSerial.tReadBuff
  # Tentative de décodage
  self.tConfigParser.ttFParseSerialNumber( sRead, self.ttConfig )
  # Test numéro version
  # Si inferieur à V4.5x sur probe autre que AquaPlus => erreur
  #If Probe_type < 7 And PSW1 < 4 And PSW2 < 5 Then GoTo SW_VER_ERROR
  if(   ( self.ttConfig["PRODUCT"]["uiModel"] != 53 )
    and ( self.ttConfig["PRODUCT"]["uiPSW1"]   <  4 )
    and ( self.ttConfig["PRODUCT"]["uiPSW2"]   <  5 ) ):
   self.siError.emit("This application does not support the software revision in your Probe. Please contact your dealer for a Probe software upgrade")
   return

  # Formattage produit
  self.ttCurrentConfig = self.ttConfig
  # Lecture donnée de calibration
  time.sleep(0.05)
  # Si AquaPlus ou old AP-700/Ap-800
  if( self.ttConfig["PRODUCT"]["uiProbeType"] > 6 ):
   # Requête suivante
   self._vFProductSetMeterVer3()
  # Autres produits
  else:
   # Requête suivante
   self._vFProductGetChecksum()
 #----------------------------------------------
 # Set Meter Ver 3 -> cf AquaCal legacy code
 #----------------------------------------------
 def _vFProductSetMeterVer3( self ):
  print("== _vFProductSetMeterVer3 ==")
  # Vérification que le port est présent
  try:
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self._vFProductSetMeterVer3End )
   tucBytes = bytearray()
   tucBytes.append( 0xE8 ) # (232)b10
   # Port COM
   if( self.tSerial.bFWriteRaw( tucBytes, 1 ) ):
    print("_vFProductSetMeterVer3 > Successfully sent")
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect( self._vFProductSetMeterVer3End )
 #----------------------------------------------
 def _vFProductSetMeterVer3End( self, sError ):
  print("-- _vFProductSetMeterVer3End --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self._vFProductSetMeterVer3End )
  # Si erreur
  if( sError != "" ):
   print( sError )
   if( sError == "Timeout" ): self.siRequestTimeout.emit()
   return
  # Récupération résultat et conversion
  txUnpacked = struct.unpack( '>B', self.tSerial.tReadBuff )
  # Vérification conformité
  if( txUnpacked[0] != 221 ):
   print("Erreur")
   # Erreur
   self.siError.emit("There was a Problem with the data transfer. Please try again")
   return
  # Lecture donnée de calibration
  time.sleep(0.05)
  self._vFProductSetMeterVer4()
 #----------------------------------------------
 # Set Meter Ver 4 -> cf AquaCal legacy code
 #----------------------------------------------
 def _vFProductSetMeterVer4( self ):
  print("== _vFProductSetMeterVer4 ==")
  # Vérification que le port est présent
  try:
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self._vFProductSetMeterVer4End )
   tucBytes = bytearray()
   tucBytes.append( 0xFF ) # (255)b10
   # Port COM
   if( self.tSerial.bFWriteRaw( tucBytes, 1 ) ):
    print("_vFProductSetMeterVer4 > Successfully sent")
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect( self._vFProductSetMeterVer4End )
 #----------------------------------------------
 def _vFProductSetMeterVer4End( self, sError ):
  print("-- _vFProductSetMeterVer4End --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self._vFProductSetMeterVer4End )
  # Si erreur
  if( sError != "" ):
   print( sError )
   if( sError == "Timeout" ): self.siRequestTimeout.emit()
   return
  # Récupération résultat et conversion
  txUnpacked = struct.unpack( '>B', self.tSerial.tReadBuff )
  # Vérification conformité
  if( txUnpacked[0] != 221 ):
   print("Erreur")
   # Erreur
   self.siError.emit("There was a Problem with the data transfer. Please try again")
   return
  # Lecture donnée de calibration
  time.sleep(0.05)
  self._vFProductGetCalibrationData()
 #----------------------------------------------
 # Requête lecture checksum (onbligatoire)
 #----------------------------------------------
 def _vFProductGetChecksum( self ):
  print("== _vFProductGetChecksum ==")
  # Vérification que le port est présent
  try:
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self._vFProductGetChecksumEnd )
   tucBytes = bytearray()

   uiPSW1 = self.ttConfig["PRODUCT"]["uiPSW1"]
   uiPSW2 = self.ttConfig["PRODUCT"]["uiPSW2"]
   uiPSW3 = self.ttConfig["PRODUCT"]["uiPSW3"]

   # Envoi 0xD0 0x01
   if(  (  ( ( uiPSW1 == 3 ) and ( uiPSW2 >= 5 ) )
        or ( ( uiPSW1 == 4 ) and ( uiPSW2 == 0 ) and ( uiPSW3 < 7 ) ) ) ):
    tucBytes.append( 0xD0 )
    tucBytes.append( 0x01 )
   # Envoi 0xD0 0x02
   elif( ( uiPSW1 == 4 ) and ( uiPSW2 >= 1 ) ):
    tucBytes.append( 0xD0 )
    tucBytes.append( 0x02 )
   # Envoi 0xD0 0x03
   elif(  (  ( ( uiPSW1 == 4 ) and ( uiPSW2 == 0 ) and ( uiPSW3 > 6 ) )
        or ( ( uiPSW1 >= 5 ) ) ) ):
    tucBytes.append( 0xD0 )
    tucBytes.append( 0x03 )
   # Si aucun de ces cas
   #else:


   # Port COM
   if( self.tSerial.bFWriteRaw( tucBytes, 1 ) ):
    print("*************")
    print("_vFProductGetChecksum > Successfully sent")
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect( self._vFProductGetChecksumEnd )
 #----------------------------------------------
 def _vFProductGetChecksumEnd( self, sError ):
  print("-- _vFProductGetChecksumEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self._vFProductGetChecksumEnd )
  # Si erreur
  if( sError != "" ):
   print( sError )
   if( sError == "Timeout" ):
    self.siRequestTimeout.emit()
   return
  print("*************")
  # Récupération résultat
  sRead = self.tSerial.tReadBuff
  # Tentative de décodage
  #self.tConfigParser.ttFParseRTCData( sRead, self.ttConfig )
  # Formattage produit
  #self.ttCurrentConfig = self.ttConfig
  # Lecture donnée de calibration
  time.sleep(0.05)
  self._vFProductGetCalibrationData()
 #----------------------------------------------
 # Requête Calibration data
 #----------------------------------------------
 def _vFProductGetCalibrationData( self ):
  print("== _vFProductGetCalibrationData ==")
  # En cas de plantage
  try:
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self._vFProductGetCalibrationDataEnd )
   # Commande
   tSendBuf = bytearray()
   tSendBuf.append(0xD6)
   # Taille attendu
   #-- AP-Lite
   if( self.ttConfig["PRODUCT"]["uiModel"] == 30 ):
    uiSize = 101
   #-- AquaPlus
   elif( self.ttConfig["PRODUCT"]["uiModel"] == 53 ):
    uiSize = 28
   #-- Autres probes
   else:
    uiSize = 146
   # Si succès on quitte
   if( self.tSerial.bFWriteRaw( tSendBuf, uiSize ) ):
    print("*************")
    print("_vFProductGetCalibrationData > Successfully sent")
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  self.tSerial.siCMDFinished.disconnect( self._vFProductGetCalibrationDataEnd )
  # Erreur
  self.siError.emit("Failed to open port")
 #----------------------------------------------
 def _vFProductGetCalibrationDataEnd( self, sError ):
  print("-- _vFProductGetCalibrationDataEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self._vFProductGetCalibrationDataEnd )
  # Si erreur
  if( sError != "" ):
   print( sError )
   if( sError == "Timeout" ):
    self.siRequestTimeout.emit()
   self.siConfigurationReadError.emit(sError)
   return
  print("*************")
  # Récupération résultat
  sRead = self.tSerial.tReadBuff
  print(sRead)
  #-- AP-Lite
  if( self.ttConfig["PRODUCT"]["uiModel"] == 30 ):
   # Tentative de décodage
   self.tConfigParser.ttFParseCalibrationDataAPLite( sRead, self.ttConfig )
  #-- AquaPlus
  elif( self.ttConfig["PRODUCT"]["uiModel"] == 53 ):
   self.tConfigParser.ttFParseCalibrationDataAquaPlus( sRead, self.ttConfig )
  #-- Autres probes
  else:
   # Tentative de décodage
   self.tConfigParser.ttFParseCalibrationData( sRead, self.ttConfig )
  # Formattage produit
  self.ttCurrentConfig = self.ttConfig
  # Délais
  time.sleep(0.1)
  # Envoi fin de commande
  ##tSendBuf = bytearray()
  ##tSendBuf.append(0x00)
  # Fin de requête
  ##if( self.tSerial.bFWriteRaw( tSendBuf, 0 ) ):
   # Délais
   ##time.sleep(0.1)
   ##self.tSerial.vFClosePort()
  print("_vFProductGetCalibrationDataEnd > self.ttConfig")
  print(self.ttConfig)
  # Signal fin de lecture
  self.siConfigurationReadEnd.emit(self.ttConfig, self.sCOM)

 #----------------------------------------------
 # Requête initiate site config write - 0x63
 #----------------------------------------------
 def bFProductInitiateSiteConfigWrite( self ):
  print("== bFProductInitiateSiteConfigWrite ==")
  # Vérification que le port est présent
  try:
   print( chr(0x63) )
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self.bFProductInitiateSiteConfigWriteEnd )
   # Commande
   tSendBuf = QByteArray()
   tSendBuf.append(0x63)
   # Si succès on quitte
   if( self.tSerial.bFWriteRaw( tSendBuf, 2 ) ):
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
   return( False )
  # Déconnexion fin
  self.tSerial.siCMDFinished.disconnect( self.bFProductInitiateSiteConfigWriteEnd )
  # Erreur
  self.siError.emit("Failed to open port")
 #----------------------------------------------
 def bFProductInitiateSiteConfigWriteEnd( self ):
  print("-- bFProductInitiateSiteConfigWriteEnd --")
  # Déconnexion fin
  self.tSerial.siCMDFinished.disconnect( self.bFProductInitiateSiteConfigWriteEnd )
  # Récupération résultat
  sRead = self.tSerial.tReadBuff
  print(sRead)
  #
  txUnpacked = struct.unpack( '>BB', sRead )
  # Vérification
  if(  ( txUnpacked[0] != 0x24 )
    or ( txUnpacked[1] != 0x63 ) ):
   print("Erreur")
   # Erreur
   self.siError.emit("Initiate config write error")
   return( False )
  #print("pause")
  #time.sleep(2)
  # On lance la requête d'écriture
  self.vFProductWriteSiteConfig()
 #----------------------------------------------
 # Requête Ecriture site config - 0x63/1
 #----------------------------------------------
 def vFProductWriteSiteConfig( self ):
  print("== vFProductWriteSiteConfig ==")
  # Protection
  try:
   # Formattage pour écriture
   txDataByte = self.tConfigParser.ttFParseWriteConfigSite( self.ttConfig )
   print("After parse")
   print(txDataByte)
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self.vFProductWriteSiteConfigEnd )
   # Port COM
   if( self.tSerial.bFWriteRaw( txDataByte, 0 ) ):
    print("*************")
    # Quitte sur succès
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  # Connexion lecture
  self.tSerial.siCMDFinished.disconnect( self.vFProductWriteSiteConfigEnd )
  # Erreur
  self.siError.emit("Failed to open port")
 #----------------------------------------------
 def vFProductWriteSiteConfigEnd( self, sError ):
  print("-- vFProductWriteSiteConfigEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self.vFProductWriteSiteConfigEnd )
  # Si erreur
  if( sError != "" ):
   print( sError )
   # Erreur
   self.siError.emit("Timeout request error")
   return
  # 0x24 0x73 normalement
  sRead = self.tSerial.tReadBuff
  print(sRead)
  time.sleep(0.2)
  # Emet signal fin
  self.siConfigSiteWriteEnd.emit()

 #----------------------------------------------
 # Requête initiate datetime sonde write - 0x74
 #----------------------------------------------
 def bFProductInitiateDateTimeSondeWrite( self ):
  print("== bFProductInitiateDateTimeSondeWrite ==")
  # Vérification que le port est présent
  try:
   print( chr(0x74) )
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self.bFProductInitiateDateTimeSondeWriteEnd )
   # Commande
   tSendBuf = QByteArray()
   tSendBuf.append(0x74)
   # Si succès on quitte
   if( self.tSerial.bFWriteRaw( tSendBuf, 2 ) ):
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
   return( False )
  # Déconnexion fin
  self.tSerial.siCMDFinished.disconnect( self.bFProductInitiateDateTimeSondeWriteEnd )
  # Erreur
  self.siError.emit("Failed to open port")
 #----------------------------------------------
 def bFProductInitiateDateTimeSondeWriteEnd( self ):
  print("-- bFProductInitiateDateTimeSondeWriteEnd --")
  # Déconnexion fin
  self.tSerial.siCMDFinished.disconnect( self.bFProductInitiateDateTimeSondeWriteEnd )
  # Récupération résultat
  sRead = self.tSerial.tReadBuff
  print(sRead)
  #
  txUnpacked = struct.unpack( '>BB', sRead )
  # Vérification
  if(  ( txUnpacked[0] != 0x24 )
    or ( txUnpacked[1] != 0x74 ) ):
   print("Erreur")
   return( False )
  time.sleep(0.2)
  # On lance la requête d'écriture
  self.vFProductWriteDateTimeSonde()
 #----------------------------------------------
 # Requête Ecriture user settings (0x74/116)
 #----------------------------------------------
 def vFProductWriteDateTimeSonde( self ):
  print("== vFProductWriteDateTimeSonde ==")
  # Protection
  try:
   # Formattage pour écriture
   txDataByte = self.tConfigParser.ttFParseWriteSondeClock( self.ttConfig )
   print("POST parse")
   print(txDataByte)
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self.vFProductWriteDateTimeSondeEnd )
   print("self.tSerial.bFWriteRaw( txDataByte, 0 )")
   print("len = %u"%len(txDataByte))
   # Port COM
   if( self.tSerial.bFWriteRaw( txDataByte, 0 ) ):
    # Quitte sur succès
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  # Déconnexion fin
  self.tSerial.siCMDFinished.disconnect( self.vFProductWriteDateTimeSondeEnd )
  # Erreur
  self.siError.emit("Failed to open port")
 #----------------------------------------------
 def vFProductWriteDateTimeSondeEnd( self, sError ):
  print("-- vFProductWriteDateTimeSondeEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self.vFProductWriteDateTimeSondeEnd )
  # Si erreur
  if( sError != "" ):
   print( sError )
   return
  # 0x24 0x74 normalement
  sRead = self.tSerial.tReadBuff
  print(sRead)
  time.sleep(0.2)
  # Emet signal fin
  self.siDateTimeSondeWriteEnd.emit()

 #----------------------------------------------
 # Requête GS sonde write - 0x74
 #----------------------------------------------
 def bFProductInitiateGSWrite( self, bGSOnly ):
  print("== bFProductInitiateGSWrite ==")
  # Sauvegarde du paramètre
  self.bGSOnly = bGSOnly

  # Si AP-Lite
  if( self.ttConfig["PRODUCT"]["uiModel"] == 30 ):
   # Appel de la requête directement
   self.bFProductWriteGS()
   return

  # Vérification que le port est présent
  try:
   print( chr(0xE1) )
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self.bFProductInitiateGSWriteEnd )
   # Commande
   tSendBuf = bytearray()
   tSendBuf.append(0xE1)
   # Si succès on quitte
   if( self.tSerial.bFWriteRaw( tSendBuf, 1 ) ):
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
   return( False )
  # Déconnexion fin
  self.tSerial.siCMDFinished.disconnect( self.bFProductInitiateGSWriteEnd )
  # Erreur
  self.siError.emit("Failed to open port")
 #----------------------------------------------
 def bFProductInitiateGSWriteEnd( self ):
  print("-- bFProductInitiateGSWriteEnd --")
  # Déconnexion fin
  self.tSerial.siCMDFinished.disconnect( self.bFProductInitiateGSWriteEnd )
  # Récupération résultat
  sRead = self.tSerial.tReadBuff
  print(sRead)
  #
  txUnpacked = struct.unpack( '>B', sRead )
  # Vérification
  if( txUnpacked[0] != 0xE1 ):
   print("Erreur")
   return( False )
  time.sleep(0.2)
  # On lance la requête d'écriture
  self.bFProductWriteGS()
 #----------------------------------------------
 # Requête Ecriture GS sonde (0xE1/225)
 #----------------------------------------------
 def bFProductWriteGS( self ):
  print("== bFProductWriteGS ==")
  # Protection
  try:
   # Formattage pour écriture
   txDataByte = self.tConfigParser.ttFParseWriteGS( self.ttConfig )
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self.bFProductWriteGSEnd )
   # Port COM
   if( self.tSerial.bFWriteRaw( txDataByte, 1 ) ):
    # Quitte sur succès
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  # Déconnexion fin
  self.tSerial.siCMDFinished.disconnect( self.bFProductWriteGSEnd )
  # Erreur
  self.siError.emit("Failed to open port")
 #----------------------------------------------
 def bFProductWriteGSEnd( self, sError ):
  print("-- bFProductWriteGSEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self.bFProductWriteGSEnd )
  # Si erreur
  if( sError != "" ):
   print( sError )
   return
  # 0x24 0x74 normalement
  sRead = self.tSerial.tReadBuff
  print(sRead)

  # Si AP-Lite
  if( self.ttConfig["PRODUCT"]["uiModel"] == 30 ):
   self.bFProductWriteAUXAssignement()
  else:
   self.bFProductInitiateAUXAssignementWrite()
 #----------------------------------------------
 # Requête AUX assignement write - 0xDA (218)
 #----------------------------------------------
 def bFProductInitiateAUXAssignementWrite( self ):
  print("== bFProductInitiateGSWrite ==")
  # Vérification que le port est présent
  try:
   print( chr(0xDA) ) # 218
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self.bFProductInitiateAUXAssignementWriteEnd )
   # Commande
   tSendBuf = bytearray()
   tSendBuf.append(0xDA) # 218
   # Si succès on quitte
   if( self.tSerial.bFWriteRaw( tSendBuf, 1 ) ):
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
   return( False )
  # Déconnexion fin
  self.tSerial.siCMDFinished.disconnect( self.bFProductInitiateAUXAssignementWriteEnd )
  # Erreur
  self.siError.emit("Failed to open port")
 #----------------------------------------------
 def bFProductInitiateAUXAssignementWriteEnd( self ):
  print("-- bFProductInitiateGSWriteEnd --")
  # Déconnexion fin
  self.tSerial.siCMDFinished.disconnect( self.bFProductInitiateAUXAssignementWriteEnd )
  # Récupération résultat
  sRead = self.tSerial.tReadBuff
  print(sRead)
  #
  txUnpacked = struct.unpack( '>B', sRead )
  # Vérification
  if( txUnpacked[0] != 0xDA ):
   print("Erreur")
   return( False )
  time.sleep(0.2)
  # On lance la requête d'écriture
  self.bFProductWriteAUXAssignement()
 #----------------------------------------------
 # Requête Ecriture GS sonde (0xE1/225)
 #----------------------------------------------
 def bFProductWriteAUXAssignement( self ):
  print("== bFProductWriteAUXAssignement ==")
  # Protection
  try:
   # Formattage pour écriture
   txDataByte = self.tConfigParser.ttFParseWriteAUXAssignement( self.ttConfig )
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self.bFProductWriteAUXAssignementEnd )
   # Port COM
   if( self.tSerial.bFWriteRaw( txDataByte, 1 ) ):
    # Quitte sur succès
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  # Déconnexion fin
  self.tSerial.siCMDFinished.disconnect( self.bFProductWriteAUXAssignementEnd )
  # Erreur
  self.siError.emit("Failed to open port")
 #----------------------------------------------
 def bFProductWriteAUXAssignementEnd( self, sError ):
  print("-- bFProductWriteAUXAssignementEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self.bFProductWriteAUXAssignementEnd )
  # Si erreur
  if( sError != "" ):
   print( sError )
   self.siError.emit("Request timeout error")
   return
  #
  sRead = self.tSerial.tReadBuff
  print(sRead)
  # Délai
  time.sleep(0.1)
  # Connexion lecture
  self.tSerial.siCMDFinished.connect( self.bFProductWriteAUXAssignementEndCMDEnd )
  # Envoi fin de commande 0x00
  tSendBuf = bytearray()
  tSendBuf.append(0x00)
  if( self.tSerial.bFWriteRaw( tSendBuf, 0 ) ):
   # Délai
   time.sleep(0.2)
   # Emet signal fin
   #self.siAUXAssignementWriteEnd.emit()
   # Quitte sur succès
   return
 #----------------------------------------------
 def bFProductWriteAUXAssignementEndCMDEnd( self, sError ):
  print("-- bFProductWriteAUXAssignementEndCMDEnd --")
  # Déconnexion lecture
  self.tSerial.siCMDFinished.disconnect( self.bFProductWriteAUXAssignementEndCMDEnd )
  # Délai
  time.sleep(0.1)
  # Emet signal fin
  self.siAUXAssignementWriteEnd.emit()

 #----------------------------------------------
 # Réinitialisation port COM
 #----------------------------------------------
 def bFProductReinitSerial( self ):
  print("-- bFProductReinitSerial --")
  #
  self.tSerial.bFClose()

 #----------------------------------------------
 # Requête Mesurement Data - 0x00 -> 0xCH (207)
 #----------------------------------------------
 def bFProductGetMeasurementData( self ):
  print("== vFProductGetMeasurementData ==")
  ucRetry = 3
  if( self.tSerial.bFIsOpen() ):
   print("Port déjà ouvert : quitte")
   return( False )
  # Vérification que le port est présent
  try:
   # Timeout : 1500
   self.tSerial.setReadTimeout(1500)
   # Connexion
   self.tSerial.siCMDFinished.connect( self.bFProductGetMeasurementDataEnd )

   print( chr(182) ) # 0xB6
   # Commande
   #tSendBuf = QByteArray()

   uiBaro = self.ttConfig["SENSOR"]["Baro"]["fResult"]
   uiREQ_Data = int( ( uiBaro - 650 ) / 2 )
   print("uiREQ_Data = %d"%uiREQ_Data)

   #-- AquaPlus : taille reponse attendue
   if( self.ttConfig["PRODUCT"]["uiModel"] == 53 ):
    uiSize = 20
   #-- Autres : taille reponse attendue
   else:
    uiSize = 39

   #tSendBuf.append(0xB6)
   # Port COM # 0xB6
   if( self.tSerial.bFWriteRaw( bytearray([uiREQ_Data]), uiSize, uiTimeoutCpt = 0 ) ):
    print("*************")
    # On quitte sur succès
    return( True )
   print("Error to bFWriteRaw")
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  # Déconnexion
  self.tSerial.siCMDFinished.disconnect( self.bFProductGetMeasurementDataEnd )
  # Erreur
  self.siError.emit("Failed to open port")
  # Timeout : 5000
  self.tSerial.setReadTimeout(self.uiDefaultTimeout)
  # On quitte
  return( False )
 #----------------------------------------------
 def bFProductGetMeasurementDataEnd( self, sError ):
  print("-- bFProductGetMeasurementDataEnd --")
  # Déconnexion
  self.tSerial.siCMDFinished.disconnect( self.bFProductGetMeasurementDataEnd )
  # Timeout : 5000
  self.tSerial.setReadTimeout(self.uiDefaultTimeout)
   # Si erreur
  if( sError != "" ):
   print( sError )
   ### Faut-il relancer la requête Direct Access
   #if(sError == "Timeout"):
   # self.bFProductGetDirectAccessMode()
   # !Pas pour la mesure
   # Erreur
   #self.siError.emit(sError)
   return
  print("*************")
  # Récupération résultat
  sRead = self.tSerial.tReadBuff
  # Vérification de la taille reçue
  if( len(sRead) == 39 ):
   # Tentative de décodage
   self.tConfigParser.ttFParseMeasurementData( sRead, self.ttConfig )
   # Valeur de pression initiale
   fDepthRaw = self.ttConfig["SENSOR"]["Baro"]["fDepthRaw"]
   fEC       = self.ttConfig["SENSOR"]["EC"]["fResult"]
   # Test si capteur à l'air libre
   if(   (   ( fDepthRaw >=  650 )
         and ( fDepthRaw <= 1060 ) )
     and ( fEC <= 0 )
     and ( self.ttConfig["SENSOR"]["DO"]["Point"][0]["uiDay"] != 0 )
     and ( not self.bAirPressureInit ) ):
    # On a initialisé la valeur de pression
    self.bAirPressureInit = True
    # Valeur par défaut
    self.ttConfig["SENSOR"]["Baro"]["fResult"] = fDepthRaw
   # Signal de fin
   self.siMeasureDataReadEnd.emit(self.ttConfig)
   return( True )
  # AquaPlus
  elif( len(sRead) == 20 ):
   # Tentative de décodage
   self.tConfigParser.ttFParseMeasurementDataAquaPlus( sRead, self.ttConfig )
   # Signal de fin
   self.siMeasureDataReadEnd.emit(self.ttConfig)
   return( True )
  # Taille incorrecte
  return( False )

 #----------------------------------------------
 # Calcul des voies calculées (MAJ)
 #----------------------------------------------
 def _vFProductUpdateCalculatedParameters( self ):
  print("-- _vFProductUpdateCalculatedParameters --")
  # Calcul des voies calculées
  self.tConfigParser.ttFCalculatedDataCalculation( self.ttConfig, self.ttMeasure )
  # Emet signal fin
  self.siDataCalculatedParametersUpdated.emit()

 #----------------------------------------------
 # Démarrage balai
 #----------------------------------------------
 def _vFProductWiperStart( self ):
  print("== _vFProductWiperStart ==")
  try:
   # Mode continue
   self.tSerial.vFSetContinuousMode()
   # Création requête
   tucBytes = bytearray()
   tucBytes.append( 0xD4 )
   # Connexion lecture
   self.tSerial.siContinuousBytesRead.connect( self._vFProductWiperStartWait )
   self.tSerial.siCMDFinished.connect( self._vFProductWiperStartError )
   # Port COM
   if( self.tSerial.bFWriteRaw( tucBytes, 0 ) ):
    print("*************")
    print("_vFProductWiperStart > Successfully sent")
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  # Déconnexion en cas d'erreur
  self.tSerial.siContinuousBytesRead.disconnect( self._vFProductWiperStartWait )
  self.tSerial.siCMDFinished.disconnect( self._vFProductWiperStartError )
  # Arret du mode continue
  self.tSerial.vFStopContinuousMode()
  # Erreur
  self.siError.emit("Failed to open port")
 #----------------------------------------------
 def _vFProductWiperStartError( self, sError ):
  print("-- bFProductCalibrationCMDPointWait --")
  print(sError)
  # Déconnexion signaux
  self.tSerial.siContinuousBytesRead.disconnect( self._vFProductWiperStartWait )
  self.tSerial.siCMDFinished.disconnect( self._vFProductWiperStartError )
  # Arret du mode continue
  self.tSerial.vFStopContinuousMode()
  # Emet le message d'erreur
  self.siError.emit(sError)
 #----------------------------------------------
 def _vFProductWiperStartWait( self, tRead ):
  print("-- _vFProductWiperStartWait --")
  #
  print(tRead)
  sError = ""

  sProto = ">"
  for uiCpt in range(len(tRead)):
   sProto = sProto + "B"
  # Unpack
  txUnpacked = struct.unpack( sProto, tRead )
  #-- Cleaning occuring
  if( txUnpacked[0] == 0x43 ):
   print("Clean occuring flag - 0x43")
   if( len(txUnpacked) == 1 ): return

  # Dans tous les cas ici on déconnecte
  self.tSerial.siContinuousBytesRead.disconnect( self._vFProductWiperStartWait )
  self.tSerial.siCMDFinished.disconnect( self._vFProductWiperStartError )
  # Stop mode continue
  self.tSerial.vFStopContinuousMode()
  #-- Clean finished
  if(  ( txUnpacked[0] == 0x44 )
    or (   ( len(txUnpacked) > 1 )
       and ( txUnpacked[1] == 0x44 ) ) ):
   print("Clean finished flag - 0x44")
   # Signal de fin succès
   self.siWiperStartEnd.emit()
   return

  #-- Clean fail
  if(  ( txUnpacked[0] == 0x52 )
    or (   ( len(txUnpacked) >  1    )
       and ( txUnpacked[1]   == 0x52 ) ) ):
   print("Clean fail flag - 0x52")
   sError = "Clean fail"
  #-- Clean fail
  if(  ( txUnpacked[0] == 0x53 )
    or (   ( len(txUnpacked) >  1    )
       and ( txUnpacked[1]   == 0x53 ) ) ):
   print("Clean fail flag - 0x53")
   sError = "Clean fail"

  # Emet le message d'erreur
  self.siError.emit(sError)

 #----------------------------------------------
 def _vFProductWiperStartEnd( self ):
  print("-- _vFProductWiperStartEnd --")
  # Déconnexion lecture
  #self.tSerial.siCMDFinished.disconnect( self._vFProductWiperStartEnd )

  # Récupération résultat
  #sRead = self.tSerial.tReadBuff
  #print(len(sRead))
  # Tentative de décodage
  #print(self.ttMeasure)
  # Lancement de la lecture de la suite
  #self._vFProductGetRTCData()
  # Emet signal fin
  #self.siWiperStartEnd.emit()
  # Démarrage timer timeout
  #self.tTimeoutWiper.start(10000);
  # Démarrage timer timeout
  #self.tTimeoutWiper.start(2000);
 #----------------------------------------------
 def _vFProductWiperStartTimeout( self ):
  print("-- _vFProductWiperStartTimeout --")
 #----------------------------------------------
 def _vFProductWiperStartLoop( self ):
  print("-- _vFProductWiperStartLoop --")

 #=======================
 # Calibration
 #=======================
 #----------------------------------------------
 # Calibration - CMD calibration point
 #----------------------------------------------
 def bFProductCalibrationWriteGSInitiate( self, uiCalibrationCode, tCalibConfigObj ):
  print("== bFProductCalibrationWriteGSInitiate ==")
  # Sauvegarde du code calibration
  self.uiCalibrationCode = uiCalibrationCode
  # Sauvegarde des paramètres
  self.tCalibConfigObj = tCalibConfigObj

  # Si AP-Lite
  if(  ( self.ttConfig["PRODUCT"]["uiModel"] == 30 )
  # ou si AquaPlus
  #  or (   ( self.ttConfig["PRODUCT"]["uiModel"] == 53 )
  #     and ( self.ttConfig["PRODUCT"]["uiPSW1"]  ==  3 )
  #     and ( self.ttConfig["PRODUCT"]["uiPSW2"]  >=  1 ) )
    #    3.x,  x >= 5
    # or 4.0x, x < 7
    # or 4.x,  x >= 1
    or ( self.ttConfig["PRODUCT"]["ProBE_SW"] == 1 )
    or ( self.ttConfig["PRODUCT"]["ProBE_SW"] == 2 ) ):
   # Appel de la requête directement
   self.bFProductCalibrationWriteGS()
   return

  # Vérification que le port est présent
  try:
   print( chr(0xE1) )
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self.bFProductCalibrationWriteGSInitiateEnd )
   # Commande
   tSendBuf = bytearray()
   tSendBuf.append(0xE1)
   # Si succès on quitte
   if( self.tSerial.bFWriteRaw( tSendBuf, 1 ) ):
    print("bFWriteRaw 0xE1 OK")
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
   return( False )
  # Déconnexion fin
  self.tSerial.siCMDFinished.disconnect( self.bFProductCalibrationWriteGSInitiateEnd )
  # Erreur
  #self.siError.emit("Failed to open port")
  self.siCalibrationStabilizeError.emit("Calibration error", "Failed to open port")
 #----------------------------------------------
 def bFProductCalibrationWriteGSInitiateEnd( self ):
  print("-- bFProductCalibrationWriteGSInitiateEnd --")
  # Déconnexion fin
  self.tSerial.siCMDFinished.disconnect( self.bFProductCalibrationWriteGSInitiateEnd )
  # Récupération résultat
  sRead = self.tSerial.tReadBuff
  print(sRead)
  try:
   #
   txUnpacked = struct.unpack( '>B', sRead )
   # Vérification
   if( txUnpacked[0] != 0xE1 ):
    print("Erreur")
    #self.siError.emit("Error wrong sonde response")
    self.siCalibrationStabilizeError.emit("Calibration error", "Calibration failed")
    return( False )
   time.sleep(0.2)
   # On lance la requête d'écriture
   self.bFProductCalibrationWriteGS()
  except Exception as err:
   print(err)
   self.siError.emit("Failed to calibrate")
 #----------------------------------------------
 # Requête Ecriture GS sonde (0xE1/225)
 #----------------------------------------------
 def bFProductCalibrationWriteGS( self ):
  print("== bFProductCalibrationWriteGS ==")
  # Protection
  try:
   # Formattage pour écriture
   txDataByte = self.tConfigParser.ttFParseWriteGS( self.ttConfig )
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self.bFProductCalibrationWriteGSEnd )
   # Port COM
   if( self.tSerial.bFWriteRaw( txDataByte, 1 ) ):
    # Quitte sur succès
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  # Déconnexion fin
  self.tSerial.siCMDFinished.disconnect( self.bFProductCalibrationWriteGSEnd )
  # Erreur
  #self.siError.emit("Failed to open port")
  self.siCalibrationStabilizeError.emit("Calibration error", "Failed to open port")
 #----------------------------------------------
 def bFProductCalibrationWriteGSEnd( self ):
  print("-- bFProductCalibrationWriteGSEnd --")
  # Déconnexion fin
  self.tSerial.siCMDFinished.disconnect( self.bFProductCalibrationWriteGSEnd )
  # Protection
  try:
   # Récupération résultat
   tRead = self.tSerial.tReadBuff
   print(tRead)
   #
   txUnpacked = struct.unpack( '>B', tRead[0] )
   # Vérification
   if( txUnpacked[0] != 0xE1 ):
    print("Erreur")
    self.siCalibrationStabilizeError.emit("Calibration error", "Wrong sonde response")
    return( False )
   time.sleep(0.2)
   # On lance la requête d'écriture
   self.bFProductCalibrationCMDPoint()
  except Exception as err:
   print(err)
   self.siCalibrationStabilizeError.emit("Calibration error", "Wrong sonde response")
 #----------------------------------------------
 # Requête Ecriture calibration CMD
 #----------------------------------------------
 def bFProductCalibrationCMDPoint( self ):
  print("== bFProductCalibrationCMDPoint ==")
  # Protection
  try:
   # Mode continue
   self.tSerial.vFSetContinuousMode()
   # Commande
   tSendBuf = bytearray()
   tSendBuf.append(self.uiCalibrationCode)
   print("After parse")
   # Connexion lecture
   self.tSerial.siContinuousBytesRead.connect( self.bFProductCalibrationCMDPointWait )
   self.tSerial.siCMDFinished.connect( self.bFProductCalibrationCMDPointError )
   # Port COM
   if( self.tSerial.bFWriteRaw( tSendBuf, 0 ) ):
    print("*************")
    # Quitte sur succès
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  # Déconnexion signaux
  self.tSerial.siContinuousBytesRead.disconnect( self.bFProductCalibrationCMDPointWait )
  self.tSerial.siCMDFinished.disconnect( self.bFProductCalibrationCMDPointError )
  # Erreur
  self.siCalibrationStabilizeError.emit("Calibration error", "Failed to open port")
 #----------------------------------------------
 def bFProductCalibrationCMDPointError( self, sError ):
  print("-- bFProductCalibrationCMDPointWait --")
  print(sError)
  # Déconnexion signaux
  self.tSerial.siContinuousBytesRead.disconnect( self.bFProductCalibrationCMDPointWait )
  self.tSerial.siCMDFinished.disconnect( self.bFProductCalibrationCMDPointError )
  # Emet le message d'erreur
  self.siCalibrationCMDPointError.emit(sError)
 #----------------------------------------------
 def bFProductCalibrationCMDPointWait( self, tRead ):
  print("-- bFProductCalibrationCMDPointWait --")
  # Protection
  try:
   #
   print(tRead)
   sError = ""
   # Init du proto
   sProto = ">"
   for uiCpt in range(len(tRead)):
    sProto = sProto + "B"
   # Unpack
   txUnpacked = struct.unpack( sProto, tRead )
   #-- Calibration occuring
   if( txUnpacked[0] == 0x43 ):
    print("Calibration occuring flag - 0x43")
    # Si AP-Lite et AUX1 P2 => Envoi de la valeur calibration
    if(   ( self.ttConfig["PRODUCT"]["uiModel"] == 30 )
      and ( self.uiCalibrationCode == 238 ) ):
     # Si AquaLite : Envoi de la valeur AUX1 P2
     # Stop mode continue
     self.tSerial.vFStopContinuousMode()
     self.bFProductCalibrationAPLiteAUX1P2Write()
     return
    # Si uniquement Flag busy : on quitte
    if( len(txUnpacked) == 1 ): return

   # Dans tous les cas ici on déconnecte
   self.tSerial.siContinuousBytesRead.disconnect( self.bFProductCalibrationCMDPointWait )
   self.tSerial.siCMDFinished.disconnect( self.bFProductCalibrationCMDPointError )
   #-- Calibration finished
   if(  ( txUnpacked[0] == 0x44 )
     or (   ( len(txUnpacked) > 1 )
        and ( txUnpacked[1] == 0x44 ) ) ):
    print("Calibration finished flag - 0x44")
    # Valide : on change la valeur du flag
    self.bFCalibrationSetCalibrationFlag( self.uiCalibrationCode, True )
    # Si RapidCal
    if( self.uiCalibrationCode == 226 ):
     # Stop mode continue
     self.tSerial.vFStopContinuousMode()
     # Dummy bytes
     time.sleep(0.3)
     self.tSerial.bFWriteDummyByte()
     time.sleep(0.5)
     # Emet signal fin
     self.siCalibrationCMDPointEnd.emit()
     return
    # Pas en Rapidcal
    else:
     # Si on a le checksum avec déjà
     if(   ( txUnpacked[0]   == 0x44 )
       and ( len(txUnpacked) == 3    ) ):
      print("bFProductCalibrationCMDPointWait > 1")
      ## Vérifier checksum ?
      time.sleep(0.5)
      print(txUnpacked)
      # Unpack
      sProto = tRead[1:3]
      ## TODO - Vérifier checksum
      self.tConfigParser.ttFParseCalibrationResult( sProto, self.ttConfig, self.uiCalibrationCode )
      # Stop mode continue
      self.tSerial.vFStopContinuousMode()
      # Emet signal fin
      self.siCalibrationCMDPointEnd.emit()
      return
     # Si on a le checksum avec déjà
     if(   ( txUnpacked[0]   == 0x43 )
       and ( txUnpacked[1]   == 0x44 )
       and ( len(txUnpacked) >=  4   ) ):
      print("bFProductCalibrationCMDPointWait > 1")
      ## Vérifier checksum ?
      time.sleep(0.5)
      print(txUnpacked)
      # Unpack
      sProto = tRead[2:4]
      ## TODO - Vérifier checksum
      self.tConfigParser.ttFParseCalibrationResult( sProto, self.ttConfig, self.uiCalibrationCode )
      # Stop mode continue
      self.tSerial.vFStopContinuousMode()
      # Emet signal fin
      self.siCalibrationCMDPointEnd.emit()
      return

     # Passage en attente de checksum
     print("Passage en attente de checksum")
     self.tSerial.siContinuousBytesRead.connect( self.bFProductCalibrationCMDPointWaitChecksum )
     return

   # Stop mode continue
   self.tSerial.vFStopContinuousMode()
   #-- EC Calibration Chk (0xD2 - SC35 / 0xE7 - RapidCal / 0xE5 - User)
   if( txUnpacked[0] == 0xDD ):
    print("EC Calibration Chk - 0xDD")
    self.siCalibrationPointECIntroEnd.emit()
    return
   #-- Range fail
   if(  ( txUnpacked[0] == 0x52 )
     or (   ( len(txUnpacked) >  1 )
        and ( txUnpacked[1]   == 0x52 ) ) ):
    print("Range fail flag - 0x52")
    sError = "Range fail"
   #-- Temperature fail
   if(  ( txUnpacked[0] == 0x54 )
     or (   ( len(txUnpacked) > 1 )
        and ( txUnpacked[1] == 0x54 ) ) ):
    print("Temperature fail flag - 0x54")
    sError = "Temperature fail"
   #-- DO fail
   if(  ( txUnpacked[0] == 0x55 )
     or (   ( len(txUnpacked) > 1 )
        and ( txUnpacked[1] == 0x55 ) ) ):
    print("DO fail flag - 0x55")
    sError = "DO fail"
   #---
   # Emet le message d'erreur
   self.siCalibrationCMDPointError.emit(sError)
  except Exception as err:
   print(err)
   print(repr(err))
   print(traceback.format_exc())
   print("Unexpected error")
   # Emet le message d'erreur
   self.siCalibrationCMDPointError.emit("Unexpected error")
 #----------------------------------------------
 def bFProductCalibrationCMDPointWaitChecksum( self, tRead ):
  print("-- bFProductCalibrationCMDPointWaitChecksum --")
  #print(sData)
  #sRead = self.tSerial.tReadBuff
  print(tRead)

  if( len( tRead ) >= 4 ):
   print("Taille sup/egal à 4")
   tRead = tRead[2:4]
  if( len( tRead ) == 3 ):
   print("Taille sup/egal à 3")
   tRead = tRead[2:4]
  if( len( tRead ) == 2 ):
   print("Taille sup/egal à 2")
  if( len( tRead ) == 1 ):
   print("Taille sup/egal à 1")
   uiResponseSize = len(self.tSerial.tReadBuff)
   if( uiResponseSize >= 2 ):
    tRead = self.tSerial.tReadBuff[ uiResponseSize-2:uiResponseSize ]


  """
  sProto = ">"
  for uiCpt in range(len(tRead)):
   sProto = sProto + "B"
  # Unpack
  txUnpacked = struct.unpack( sProto, tRead )
  """
  ## TODO - Vérifier checksum
  self.tConfigParser.ttFParseCalibrationResult( tRead, self.ttConfig, self.uiCalibrationCode )

  # Stop mode continue
  self.tSerial.vFStopContinuousMode()
  # Déconnect
  self.tSerial.siContinuousBytesRead.disconnect( self.bFProductCalibrationCMDPointWaitChecksum )
  # Dummy bytes
  #time.sleep(0.3)
  #self.tSerial.bFWriteDummyByte()
  time.sleep(0.5)
  # Emet signal fin
  self.siCalibrationCMDPointEnd.emit()

 #----------------------------------------------
 # AP-Lite - Requête Ecriture calibration AUX1 P2
 #----------------------------------------------
 def bFProductCalibrationAPLiteAUX1P2Write( self ):
  print("== bFProductCalibrationAPLiteAUX1P2Write ==")
  # Protection
  try:
   # Mode continue
   self.tSerial.vFSetContinuousMode()
   # Conversion
   uiAUX1P2CalibValue = self.tCalibConfigObj["uiAUX1P2CalibValue"]
   # Commande
   tSendBuf = bytearray()
   tSendBuf.append( ( uiAUX1P2CalibValue & 0xFF0000 ) >> 16 )
   tSendBuf.append( ( uiAUX1P2CalibValue & 0x00FF00 ) >> 8 )
   tSendBuf.append( ( uiAUX1P2CalibValue & 0x0000FF ) )
   print("After parse")
   # Connexion lecture
   #self.tSerial.siContinuousBytesRead.connect( self.bFProductCalibrationCMDPointWait )
   #self.tSerial.siCMDFinished.connect( self.bFProductCalibrationCMDPointError )
   # Port COM
   if( self.tSerial.bFWriteRaw( tSendBuf, 0 ) ):
    print("*************")
    # Quitte sur succès
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  # Déconnexion signaux
  self.tSerial.siContinuousBytesRead.disconnect( self.bFProductCalibrationCMDPointWait )
  self.tSerial.siCMDFinished.disconnect( self.bFProductCalibrationCMDPointError )
  # Erreur
  self.siCalibrationStabilizeError.emit("Calibration error", "Failed to open port")

 #----------------------------------------------
 # Requête Ecriture calibration CMD
 #----------------------------------------------
 def bFCalibrationRestoreDefault( self, uiCode ):
  print("== bFCalibrationRestoreDefault ==")
  # Conservation du code
  self.uiCalibrationCode = uiCode
  # Protection
  try:
   # Mode continue
   #self.tSerial.vFSetContinuousMode()
   # Commande
   tSendBuf = bytearray()
   tSendBuf.append(self.uiCalibrationCode)
   print("After parse")
   #print(txDataByte)
   # Connexion lecture
   self.tSerial.siCMDFinished.connect( self.bFCalibrationRestoreDefaultEnd )
   # Port COM
   if( self.tSerial.bFWriteRaw( tSendBuf, 1 ) ):
    print("*************")
    # Quitte sur succès
    return
  except Exception as err:
   print( err )
   raise Exception("Error: No product in this COM")
  # Connexion lecture
  self.tSerial.siCMDFinished.disconnect( self.bFCalibrationRestoreDefaultEnd )
 #----------------------------------------------
 def bFCalibrationRestoreDefaultEnd( self, sError ):
  print("-- bFCalibrationRestoreDefaultEnd --")
  # Dans tous les cas ici on déconnecte
  self.tSerial.siCMDFinished.disconnect( self.bFCalibrationRestoreDefaultEnd )
  try:
   # Si erreur
   if( sError != "" ):
    print( sError )
    self.siCalibrationCMDPointError.emit(sError)
    return
   # Conservation du code
   #self.uiCalibrationCode = uiCode
   self.bFCalibrationSetCalibrationFlag( self.uiCalibrationCode, False )

   # Récupération résultat
   sRead = self.tSerial.tReadBuff
   print("sRead")
   print(sRead)
   sError = ""
   # Init proto
   sProto = ">"
   for uiCpt in range(len(sRead)):
    sProto = sProto + "B"
   print("sProto")
   print(sProto)
   # Unpack
   txUnpacked = struct.unpack( sProto, sRead )
   #-- EC Calibration Chk (0xD2 - SC35 / 0xE7 - RapidCal / 0xE5 - User)
   if( txUnpacked[0] == 0xDD ):
    print("EC Calibration Chk - 0xDD")
    # Dummy bytes
    time.sleep(0.1)
    self.tSerial.bFWriteDummyByte()
    time.sleep(0.5)
    # Réinit du point
    self.tConfigParser.ttFParseCalibrationResultReinit( self.ttConfig, self.uiCalibrationCode )
    # Valide
    self.siCalibrationCMDRestorePointEnd.emit()
    return
   #-- Emet le message d'erreur
   self.siCalibrationCMDPointError.emit(sError)
  except Exception as err:
   print(err)
   print(repr(err))
   print(traceback.format_exc())

   # Message d'erreur
   self.siCalibrationCMDPointError.emit("Unexcepted error")

 #----------------------------------------------
 # Modification de l'état du flag calibration
 #----------------------------------------------
 def bFCalibrationSetCalibrationFlag( self, uiCode, bState ):
  print("== bFCalibrationSetCalibrationFlag ==")

  #-- Validation de point --
  # pH - Point 0 - 7.00
  if( uiCode == 221 ): self.ttConfig["SENSOR"]["PH"]["Point"][0]["bCalibrated"] = bState
  # pH - Point 1 - 4.01
  if( uiCode == 220 ): self.ttConfig["SENSOR"]["PH"]["Point"][1]["bCalibrated"] = bState
  # pH - Point 2 - 10.0
  if( uiCode == 219 ): self.ttConfig["SENSOR"]["PH"]["Point"][2]["bCalibrated"] = bState
  # ORP - 250mV / ORP - 229 mV
  if(  ( uiCode == 217 )
    or ( uiCode == 216 ) ): self.ttConfig["SENSOR"]["ORP"]["Point"][0]["bCalibrated"] = bState
  # DO - Point 0 - Zéro
  if( uiCode == 222 ): self.ttConfig["SENSOR"]["DO"]["Point"][0]["bCalibrated"] = bState
  # DO - Point 1 - 100%
  if( uiCode == 223 ): self.ttConfig["SENSOR"]["DO"]["Point"][1]["bCalibrated"] = bState
  # EC
  if(  ( uiCode == 231 )
    or ( uiCode == 229 )
    or ( uiCode == 210 )
    or ( uiCode == 224 ) ): self.ttConfig["SENSOR"]["EC"]["Point"][0]["bCalibrated"] = bState
  # AUX1 - Point
  if( uiCode == 237 ): self.ttConfig["SENSOR"]["AUX1"]["Point"][0]["bCalibrated"] = bState
  if( uiCode == 238 ): self.ttConfig["SENSOR"]["AUX1"]["Point"][1]["bCalibrated"] = bState
  if( uiCode == 239 ): self.ttConfig["SENSOR"]["AUX1"]["Point"][2]["bCalibrated"] = bState
  # AUX2 - Point0
  if( uiCode == 240 ): self.ttConfig["SENSOR"]["AUX2"]["Point"][0]["bCalibrated"] = bState
  if( uiCode == 241 ): self.ttConfig["SENSOR"]["AUX2"]["Point"][1]["bCalibrated"] = bState
  if( uiCode == 242 ): self.ttConfig["SENSOR"]["AUX2"]["Point"][2]["bCalibrated"] = bState
  # AUX3 - Point
  if( uiCode == 243 ): self.ttConfig["SENSOR"]["AUX3"]["Point"][0]["bCalibrated"] = bState
  if( uiCode == 244 ): self.ttConfig["SENSOR"]["AUX3"]["Point"][1]["bCalibrated"] = bState
  if( uiCode == 245 ): self.ttConfig["SENSOR"]["AUX3"]["Point"][2]["bCalibrated"] = bState
  # AUX4 - Point
  if( uiCode == 246 ): self.ttConfig["SENSOR"]["AUX4"]["Point"][0]["bCalibrated"] = bState
  if( uiCode == 247 ): self.ttConfig["SENSOR"]["AUX4"]["Point"][1]["bCalibrated"] = bState
  if( uiCode == 248 ): self.ttConfig["SENSOR"]["AUX4"]["Point"][2]["bCalibrated"] = bState
  # AUX5 - Point
  if( uiCode == 249 ): self.ttConfig["SENSOR"]["AUX5"]["Point"][0]["bCalibrated"] = bState
  if( uiCode == 250 ): self.ttConfig["SENSOR"]["AUX5"]["Point"][1]["bCalibrated"] = bState
  if( uiCode == 251 ): self.ttConfig["SENSOR"]["AUX5"]["Point"][2]["bCalibrated"] = bState
  # AUX6 - Point
  if( uiCode == 252 ): self.ttConfig["SENSOR"]["AUX6"]["Point"][0]["bCalibrated"] = bState
  if( uiCode == 253 ): self.ttConfig["SENSOR"]["AUX6"]["Point"][1]["bCalibrated"] = bState
  if( uiCode == 254 ): self.ttConfig["SENSOR"]["AUX6"]["Point"][2]["bCalibrated"] = bState

  # RapidCal
  if( uiCode == 226 ):
   self.ttConfig["SENSOR"]["PH"]["Point"][0]["bCalibrated"] = bState
   self.ttConfig["SENSOR"]["EC"]["Point"][0]["bCalibrated"] = bState

  #-- Restauration point calibration default --
  # pH - ORP
  if( uiCode == 211 ):
   self.ttConfig["SENSOR"]["PH"]["Point"][0]["bCalibrated"]  = bState
   self.ttConfig["SENSOR"]["PH"]["Point"][1]["bCalibrated"]  = bState
   self.ttConfig["SENSOR"]["PH"]["Point"][2]["bCalibrated"]  = bState
   self.ttConfig["SENSOR"]["ORP"]["Point"][0]["bCalibrated"] = bState
  # DO - EC
  if( uiCode == 213 ):
   self.ttConfig["SENSOR"]["DO"]["Point"][0]["bCalibrated"] = bState
   self.ttConfig["SENSOR"]["DO"]["Point"][1]["bCalibrated"] = bState
   self.ttConfig["SENSOR"]["EC"]["Point"][0]["bCalibrated"] = bState
  # AUX1 - Point
  if( uiCode == 227 ):
   self.ttConfig["SENSOR"]["AUX1"]["Point"][0]["bCalibrated"] = bState
   self.ttConfig["SENSOR"]["AUX1"]["Point"][1]["bCalibrated"] = bState
   self.ttConfig["SENSOR"]["AUX1"]["Point"][2]["bCalibrated"] = bState
  # AUX2 - Point0
  if( uiCode == 228 ):
   self.ttConfig["SENSOR"]["AUX2"]["Point"][0]["bCalibrated"] = bState
   self.ttConfig["SENSOR"]["AUX2"]["Point"][1]["bCalibrated"] = bState
   self.ttConfig["SENSOR"]["AUX2"]["Point"][2]["bCalibrated"] = bState
  # AUX3 - Point
  if( uiCode == 232 ):
   self.ttConfig["SENSOR"]["AUX3"]["Point"][0]["bCalibrated"] = bState
   self.ttConfig["SENSOR"]["AUX3"]["Point"][1]["bCalibrated"] = bState
   self.ttConfig["SENSOR"]["AUX3"]["Point"][2]["bCalibrated"] = bState
  # AUX4 - Point
  if( uiCode == 234 ):
   self.ttConfig["SENSOR"]["AUX4"]["Point"][0]["bCalibrated"] = bState
   self.ttConfig["SENSOR"]["AUX4"]["Point"][1]["bCalibrated"] = bState
   self.ttConfig["SENSOR"]["AUX4"]["Point"][2]["bCalibrated"] = bState
  # AUX5 - Point
  if( uiCode == 235 ):
   self.ttConfig["SENSOR"]["AUX5"]["Point"][0]["bCalibrated"] = bState
   self.ttConfig["SENSOR"]["AUX5"]["Point"][1]["bCalibrated"] = bState
   self.ttConfig["SENSOR"]["AUX5"]["Point"][2]["bCalibrated"] = bState
  # AUX6 - Point
  if( uiCode == 236 ):
   self.ttConfig["SENSOR"]["AUX6"]["Point"][0]["bCalibrated"] = bState
   self.ttConfig["SENSOR"]["AUX6"]["Point"][1]["bCalibrated"] = bState
   self.ttConfig["SENSOR"]["AUX6"]["Point"][2]["bCalibrated"] = bState


#----------------------------------------------------------------------------#
# Test unitaire
#----------------------------------------------------------------------------#
if __name__ == "__main__":
 # Déclaration produit
 tProduct = TProduct()
 # Configuration du port
 tProduct.tSerial.uliBaudrate = 19200
 tProduct.tSerial.sPortCOM    = "COM79"
 # Liste des sondes
 tProduct.vFSondeList()

 # Résultat
 print( "Sondes détectées :" )
 for sElt in tProduct.tsProductList:
  print(sElt)





