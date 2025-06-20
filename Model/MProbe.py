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
from Product.Probe.TProduct import TProduct

#============================================================================#
# Variable
#============================================================================#

#============================================================================#
# Classe
#============================================================================#

#------------------------------------------------------------------------
# Main Windows
#------------------------------------------------------------------------
class MProbe(QObject):
 #----------------------------------------------
 # Signaux
 #----------------------------------------------
 #-- General
 siErrorMsg                     = Signal(str, str)
 #siError                        = Signal(str)
 #-- Connexion
 siDetectProductEnd             = Signal(dict)
 siConfigurationReadError       = Signal(str)
 #-- Dashboard
 siConfigSiteWriteEnd           = Signal(dict)
 siUserSettingsWriteEnd         = Signal(dict)
 siDateTimeSondeWriteEnd        = Signal(dict)
 siAUXAssignementWriteEnd       = Signal()
 siClearMemoryEndSuccess        = Signal()
 # New batteries fitted
 siNewBatteriesFittedStart      = Signal()
 siNewBatteriesFittedEndSuccess = Signal()
 #-- Liveview
 siMeasureDataReadEnd           = Signal(dict)
 siMeasureDataReadStop          = Signal()
 #-- Data
 siRecordedDataReadEnd          = Signal()
 #-- Calibration
 siWiperStart                   = Signal()
 siWiperStartEnd                = Signal()
 siCalibrationCMDPointError     = Signal(str)
 siCalibrationStabStart         = Signal(int)
 siCalibrationStabProgress      = Signal(int)
 siCalibrationStabStop          = Signal()
 siCalibrationStabilizeError    = Signal(str, str)

 #----------------------------------------------
 # Init
 #----------------------------------------------
 def __init__(self, parent=None):
  # Init QObject
  super(MProbe, self).__init__(parent=parent)
  # Initialisation avec objet generique
  self.tProduct = TProduct()
  # Port com
  self.sCom = "COM8"
  # Déclaration des signaux fixes
  self.tProduct.siConfigurationReadError.connect(self.siConfigurationReadError)
  self.tProduct.siMeasureDataReadEnd.connect(self.tsFMeasureDataReadEnd)
  self.tProduct.siRecordedDataReadEnd.connect(self.vFRecordedDataReadEnd)
  self.tProduct.siClearMemoryEndSuccess.connect(self.siClearMemoryEndSuccess)
  #-- Calibration
  self.tProduct.siCalibrationCMDPointError.connect( self.slotWriteCalibrationErrorMsg )
  self.tProduct.siCalibrationPointECIntroEnd.connect( self.slotWriteCalibrationPointECIntroEnd )
  # Erreur
  #self.tProduct.siError(self.siError)

  # Timer measure
  self.tTimerMeasure = QTimer()
  self.tTimerMeasure.timeout.connect(self.tsFMeasureDataRead)
  self.uiMeasureInterval = 2000
  # Init variable
  self.uiCode = 0
  self.tCalibConfigObj = {}

 #----------------------------------------------
 # Requête mesure data
 #----------------------------------------------
 def vFMeasureDataReadStart(self):
  print("== vFMeasureDataReadStart ==")
  # Démarrage d'un timer de mesure
  self.tTimerMeasure.setInterval(self.uiMeasureInterval)
  self.tTimerMeasure.start()
  # Init variable
  self.uiMeasureErrorCpt = 0
  # Première requête
  self.tProduct.bFProductGetMeasurementData()
 #----------------------------------------------
 # Appelé périodiquement
 def tsFMeasureDataRead(self):
  print("== tsFMeasureDataRead == "+QDateTime.currentDateTime().toString("yyyy-MM-ddTHH:mm:ss.zzz"))
  # Démarrage mesure
  if( not self.tProduct.bFProductGetMeasurementData() ):
   # Stop du timer
   #self.tTimerMeasure.stop()
   # Tentative de sauvetage
   print("MProbe > Erreur port ouvert")
   self.uiMeasureErrorCpt += 1
   # Si suppérieur à 3
   if( self.uiMeasureErrorCpt > 3 ):
    # Tentative de rescue
    self.bFProductReinitSerial()
   # Si supérieur à 5 : HS
   if( self.uiMeasureErrorCpt > 5 ):
    # HS
    print("HS")
    # Stop du timer
    #self.tTimerMeasure.stop()
  # OK
  else:
   self.uiMeasureErrorCpt = 0


 #----------------------------------------------
 def tsFMeasureDataReadEnd(self):
  print("== tsFMeasureDataReadEnd ==")
  # Fin une détection automatique
  self.siMeasureDataReadEnd.emit( self.tProduct.ttConfig )
 #----------------------------------------------
 # Requête mesure data
 #----------------------------------------------
 def vFMeasureDataReadStop(self):
  print("---------------------------")
  print("-- vFMeasureDataReadStop --")
  print("---------------------------")
  # Stop du timer
  self.tTimerMeasure.stop()
  # Signal fin de mesure
  self.siMeasureDataReadStop.emit()

 #----------------------------------------------
 # Requête configuration produit
 #----------------------------------------------
 def vFRecordedDataReadStart(self):
  print("== vFRecordedDataReadStart ==")
  print('self.tProduct.ttConfig["PRODUCT"]["uiMemRecords"] = %d'%self.tProduct.ttConfig["PRODUCT"]["uiMemRecords"])
  # Vérification si il y a des données à lire
  if( self.tProduct.ttConfig["PRODUCT"]["uiMemRecords"] == 0 ):
   self.siErrorMsg.emit("Warning", "No data to read")
   return
  # Lancement de la lecture configuration
  self.tProduct._vFProductGetRecordedData()
 #----------------------------------------------
 def vFRecordedDataReadEnd(self):
  print("== vFRecordedDataReadEnd ==")
  #print(self.tProduct.ttMeasure)
  # Fin de lecture de configuration
  self.siRecordedDataReadEnd.emit()

 #----------------------------------------------
 # Requête configuration produit
 #----------------------------------------------
 def vFModelClearMemoryCMD(self):
  print("== vFModelClearMemoryCMD ==")
  # Lancement de la lecture configuration
  self.tProduct.bFProductClearMemoryCMDWrite()
 #----------------------------------------------
 def vFModelClearMemoryCMDEndSuccess(self):
  print("== vFRecordedDataReadEnd ==")
  print(self.tProduct.ttMeasure)
  # Fin de lecture de configuration
  self.siClearMemoryEndSuccess.emit( self.tProduct.ttMeasure )

 #==================================================================
 # Ecriture paramètrage
 #==================================================================

 #----------------------------------------------
 # DASHBOARD - Ecriture AUX channel assignement
 #----------------------------------------------
 #@Slot(str)
 def slotWriteAUXChannelSelect(self, sChannel, uiChannel):
  print("== slotWriteAUXChannelSelect ==")
  print("sChannel = " + sChannel )
  # Test grab sample factor
  if(   ( self.tProduct.ttConfig["SENSOR"]["AUX"+str(uiChannel+1)]["sIndex"] == "EMPTY" )
    and ( sChannel != "EMPTY" ) ):
   # Ajout du coefficient sur la voie attribuée
   self.tProduct.ttConfig["SENSOR"]["AUX"+str(uiChannel+1)]["fGS"] = 1.00

  # Assignement de la voie
  self.tProduct.ttConfig["SENSOR"]["AUX"+str(uiChannel+1)]["sIndex"]  = sChannel
  uiIndex = self.tProduct.tConfigParser.uiFGetIDWithChannelNameWith(sChannel)
  self.tProduct.ttConfig["SENSOR"]["AUX"+str(uiChannel+1)]["uiIndex"] = uiIndex
  ##TODO - Test d'intégrité
  print("sAux1Assign = "+self.tProduct.ttConfig["SENSOR"]["AUX1"]["sIndex"])
  print("sAux2Assign = "+self.tProduct.ttConfig["SENSOR"]["AUX2"]["sIndex"])
  print("sAux3Assign = "+self.tProduct.ttConfig["SENSOR"]["AUX3"]["sIndex"])
  print("sAux4Assign = "+self.tProduct.ttConfig["SENSOR"]["AUX4"]["sIndex"])
  print("sAux5Assign = "+self.tProduct.ttConfig["SENSOR"]["AUX5"]["sIndex"])
  print("sAux6Assign = "+self.tProduct.ttConfig["SENSOR"]["AUX6"]["sIndex"])
  # Sonde datetime écriture
  self.tProduct.bFProductInitiateGSWrite( bGSOnly=False )

 #----------------------------------------------
 # DASHBOARD - Ecriture Optical averaging
 #----------------------------------------------
 @Slot(int)
 def slotWriteOpticalAverage(self, uiAvgValue):
  print("== slotWriteOpticalAverage ==")
  print("uiAvgValue %u" % uiAvgValue )

  if( ( uiAvgValue % 16 ) != 0 ): uiAvgValue = uiAvgValue - ( uiAvgValue % 16 )
  if( uiAvgValue > 192 ): uiAvgValue = 192
  if( uiAvgValue <  16 ): uiAvgValue = 16
  print("uiAvgValue %s" % uiAvgValue )

  self.tProduct.ttConfig["PRODUCT"]["uiOpticalAvg"] = uiAvgValue
  # Lancement écriture vers sonde
  self.tProduct.bFProductInitiateGSWrite( bGSOnly=True )

 #----------------------------------------------
 # LIVEVIEW - Ecriture Baro value
 #----------------------------------------------
 @Slot(int)
 def slotWriteBaroValue(self, uiValue):
  print("== slotWriteBaroValue ==")
  print("Baro value %u" % uiValue )
  # Test intégrité
  if(  ( uiValue < 650 )
    or ( uiValue > 1060 ) ): return
  # Modification de la valeur
  self.tProduct.ttConfig["SENSOR"]["Baro"]["fResult"] = float(uiValue)
  # Lancement écriture vers sonde
  #self.tProduct.bFProductInitiateGSWrite( bGSOnly=True )

 #----------------------------------------------
 # CALIBRATION - Test si calibration autorisé pour point demandé
 #----------------------------------------------
 def bFCalibrationIsCalibrationAllowed( self, sConfigName, ucChannel, tChannel, uiPoint ):
  print("== bFCalibrationIsCalibrationAllowed ==")

  # pH Calibration point 4.01 ou 10.0
  if(   ( sConfigName == "PH" )
    and (  ( uiPoint  == 1 )
        or ( uiPoint  == 2 ) ) ):
   # Test si point 7.00 fait avant dans la session
   if( not tChannel["Point"][0]["bCalibrated"] ):
    # Message d'erreur
    self.siErrorMsg.emit("Calibration error", "You must calibrate the pH7.00 point first within this session")
    # Pas calibré : on refuse
    return( False )

  # AUX Calibration point 2 ou point 3
  if(   ( "AUX" in sConfigName )
    and (  ( uiPoint  == 1 )
        or ( uiPoint  == 2 ) ) ):
   # Test si point 1 fait avant dans la session
   if( not tChannel["Point"][0]["bCalibrated"] ):
    # Message d'erreur
    self.siErrorMsg.emit("Calibration error", "You must calibrate the Point 1 first within this session")
    #### DEBUG ####
    return( True )
    ###############
    # Pas calibré : on refuse
    return( False )

  # Ok c'est valide
  return( True )

 #----------------------------------------------
 # CALIBRATION - Fin d'écriture calibration point EC première étape
 #----------------------------------------------
 def slotWriteCalibrationPointECIntroEnd( self ):
  print("== slotWriteCalibrationPointECIntroEnd ==")
  print("sPointName    = " + self.sPointName )
  print("uiPointNumber = " + str(self.uiPointNumber) )
  # Lancement de la stabilisation
  self.slotWriteCalibrationPoint(self.sPointName, 4, self.tCalibConfigObj)

 #----------------------------------------------
 # CALIBRATION - Ecriture calibration point
 #----------------------------------------------
 def slotWriteCalibrationPoint(self, sPointName, uiPointNumber, tCalibConfigObj ):
  print("== slotWriteCalibrationPoint ==")
  print("sPointName    = " + sPointName )
  print("uiPointNumber = " + str(uiPointNumber) )

  self.sPointName      = sPointName
  self.uiPointNumber   = uiPointNumber
  self.tCalibConfigObj = tCalibConfigObj

  self.uiStabDuration = 6
  uiCode = 0

  # Conversion du nom du point
  if( ( sPointName == "PH" ) and ( uiPointNumber == 0 ) ): uiCode = 221
  if( ( sPointName == "PH" ) and ( uiPointNumber == 1 ) ): uiCode = 220
  if( ( sPointName == "PH" ) and ( uiPointNumber == 2 ) ): uiCode = 219

  if( ( sPointName == "ORP" ) and ( uiPointNumber == 0 ) ):
   if( tCalibConfigObj["sORPCalValue"] == "250 mV" ): uiCode = 217
   if( tCalibConfigObj["sORPCalValue"] == "229 mV" ): uiCode = 216
  if( ( sPointName == "DO"  ) and ( uiPointNumber == 0 ) ): uiCode = 222
  if( ( sPointName == "DO"  ) and ( uiPointNumber == 1 ) ): uiCode = 223
  # EC première phase de requête
  if( ( sPointName == "EC"  ) and ( uiPointNumber == 0 ) ):
   #uiCode = 224
   print("-- tCalibConfigObj --")
   print(tCalibConfigObj)

   # EC_STD_BOX
   if( self.tProduct.ttConfig["PRODUCT"]["ProBE_SW"] < 3 ):
    # Selon le mode
    if( tCalibConfigObj["sECCalValue"] == "RapidCal"  ): uiCode = 231 # 0xE7
    if( tCalibConfigObj["sECCalValue"] == "1413 uS"   ): uiCode = 229 # 0xE5
    if( tCalibConfigObj["sECCalValue"] == "12,880 uS" ): uiCode = 230 # 0xE6
    if( tCalibConfigObj["sECCalValue"] == "SC-35"     ): uiCode = 210 # 0xD2
   # EC_STD_BOX_V5
   if( self.tProduct.ttConfig["PRODUCT"]["ProBE_SW"] == 3 ):
    # Selon le mode
    if( tCalibConfigObj["sECCalValue"] == "RapidCal" ): uiCode = 231 # 0xE7
    if( tCalibConfigObj["sECCalValue"] == "User"     ): uiCode = 229 # 0xE5
    if( tCalibConfigObj["sECCalValue"] == "SC-35"    ): uiCode = 210 # 0xD2
   # AQUAPLUS_EC_BOX
   if(   ( self.tProduct.ttConfig["PRODUCT"]["uiModel"] == 53 )
     and ( self.tProduct.ttConfig["PRODUCT"]["uiPSW1"]  ==  3 )
     and ( self.tProduct.ttConfig["PRODUCT"]["uiPSW2"]  >=  1 ) ):
    # Selon le mode
    if( tCalibConfigObj["sECCalValue"] == "RapidCal" ): uiCode = 231 # 0xE7
    if( tCalibConfigObj["sECCalValue"] == "User"     ): uiCode = 229 # 0xE5
    if( tCalibConfigObj["sECCalValue"] == "SC-35"    ): uiCode = 230 # 0xE6

   # Modification configuration
   self.tProduct.ttConfig["SENSOR"]["EC"]["uiUserCalValue"] = tCalibConfigObj["uiECCalUserValue"]
   # Stop de la mesure
   self.vFMeasureDataReadStop()
   self.tProduct.bFProductCalibrationWriteGSInitiate(uiCode, tCalibConfigObj)
   return
  # Calibration EC - 2ieme requête après avoir soumis l'étalon
  if( ( sPointName == "EC"    ) and ( uiPointNumber == 4 ) ): uiCode = 224
  # Aux
  # Si Tbd sur AP-800 : code différent
  if(  ( self.tProduct.ttConfig["PRODUCT"]["uiModel"] == 50 )
    or ( self.tProduct.ttConfig["PRODUCT"]["uiModel"] == 70 ) ):
   if( ( sPointName == "AUX1"  ) and ( uiPointNumber == 0 ) ): uiCode = 216
  else:
   if( ( sPointName == "AUX1"  ) and ( uiPointNumber == 0 ) ): uiCode = 237
  if( ( sPointName == "AUX1"  ) and ( uiPointNumber == 1 ) ): uiCode = 238
  if( ( sPointName == "AUX1"  ) and ( uiPointNumber == 2 ) ): uiCode = 239
  if( ( sPointName == "AUX2"  ) and ( uiPointNumber == 0 ) ): uiCode = 240
  if( ( sPointName == "AUX2"  ) and ( uiPointNumber == 1 ) ): uiCode = 241
  if( ( sPointName == "AUX2"  ) and ( uiPointNumber == 2 ) ): uiCode = 242
  if( ( sPointName == "AUX3"  ) and ( uiPointNumber == 0 ) ): uiCode = 243
  if( ( sPointName == "AUX3"  ) and ( uiPointNumber == 1 ) ): uiCode = 244
  if( ( sPointName == "AUX3"  ) and ( uiPointNumber == 2 ) ): uiCode = 245
  if( ( sPointName == "AUX4"  ) and ( uiPointNumber == 0 ) ): uiCode = 246
  if( ( sPointName == "AUX4"  ) and ( uiPointNumber == 1 ) ): uiCode = 247
  if( ( sPointName == "AUX4"  ) and ( uiPointNumber == 2 ) ): uiCode = 248
  if( ( sPointName == "AUX5"  ) and ( uiPointNumber == 0 ) ): uiCode = 249
  if( ( sPointName == "AUX5"  ) and ( uiPointNumber == 1 ) ): uiCode = 250
  if( ( sPointName == "AUX5"  ) and ( uiPointNumber == 2 ) ): uiCode = 251
  if( ( sPointName == "AUX6"  ) and ( uiPointNumber == 0 ) ): uiCode = 252
  if( ( sPointName == "AUX6"  ) and ( uiPointNumber == 1 ) ): uiCode = 253
  if( ( sPointName == "AUX6"  ) and ( uiPointNumber == 2 ) ): uiCode = 254


  print("uiCode = %d"%uiCode)
  # Sauvegarde du code
  self.uiCode = uiCode
  # Lancement de l'init de la calibration
  self.slotWriteCalibrationStabInit()

 #----------------------------------------------
 # CALIBRATION - RapidCal - Ecriture calibration point
 #----------------------------------------------
 def slotWriteCalibrationPointRapidCal( self ):
  # Init
  self.sPointName    = "RapidCal"
  self.uiPointNumber = 0
  # Sauvegarde du code
  self.uiCode = 226
  # Lancement de l'init de la calibration
  self.slotWriteCalibrationStabInit()

 #-----------------------------------------------
 # CALIBRATION - Stabilisation de la mesure avant calibration
 #-----------------------------------------------
 def slotWriteCalibrationStabInit( self ):
  # Compteur d'échantillon de stabilisation
  self.uiStabCpt = 0
  # Init des valeurs pour analyse stabilisation
  self.fTemp_T4 = 0
  self.fTemp_T3 = 0
  self.fTemp_T2 = 0
  self.fTemp_T1 = 0
  self.EC_T4    = 0
  self.EC_T3    = 0
  self.EC_T2    = 0
  self.EC_T1    = 0
  self.D_T4     = 0
  self.D_T3     = 0
  self.D_T2     = 0
  self.D_T1     = 0
  self.DO_T4    = 0
  self.DO_T3    = 0
  self.DO_T2    = 0
  self.DO_T1    = 0
  self.PH_T4    = 0
  self.PH_T3    = 0
  self.PH_T2    = 0
  self.PH_T1    = 0
  self.ORP_T4   = 0
  self.ORP_T3   = 0
  self.ORP_T2   = 0
  self.ORP_T1   = 0
  self.TURB_T4  = 0
  self.TURB_T3  = 0
  self.TURB_T2  = 0
  self.TURB_T1  = 0
  # Start de la mesure
  self.vFMeasureDataReadStart()
  # Démarrage de la stablisation (pour fenêtre)
  self.siCalibrationStabStart.emit(40)
  # Stabilisation de la mesure
  self.tProduct.siMeasureDataReadEnd.connect(self.slotWriteCalibrationStab)

 #-----------------------------------------------
 # CALIBRATION - Stabilisation de la mesure avant calibration
 #-----------------------------------------------
 # Appelé à chaque échantillon mesuré pendant la durée de stabilisation
 def slotWriteCalibrationStab( self ):
  print("== slotWriteCalibrationStab ==")
  # Mesure résultat
  ttConfig = self.tProduct.ttConfig

  fTEMP  = ttConfig["SENSOR"]["TEMP"]["fResult"]
  fEC    = ttConfig["SENSOR"]["EC"]["fResult"]
  fDO    = ttConfig["SENSOR"]["DO"]["fResult"]
  fDOsat = ttConfig["SENSOR"]["DO Sat"]["fResult"]
  fPH    = ttConfig["SENSOR"]["PH"]["fResult"]
  fPHmv  = ttConfig["SENSOR"]["PHmv"]["fResult"]
  fORP   = ttConfig["SENSOR"]["ORP"]["fResult"]
  fDepth = ttConfig["SENSOR"]["Depth"]["fResult"]
  fAUX1  = ttConfig["SENSOR"]["AUX1"]["fResult"]
  fAUX2  = ttConfig["SENSOR"]["AUX2"]["fResult"]
  fAUX3  = ttConfig["SENSOR"]["AUX3"]["fResult"]
  fAUX4  = ttConfig["SENSOR"]["AUX4"]["fResult"]
  fAUX5  = ttConfig["SENSOR"]["AUX5"]["fResult"]
  fAUX6  = ttConfig["SENSOR"]["AUX6"]["fResult"]
  fAUX7  = ttConfig["SENSOR"]["AUX7"]["fResult"]

  # Stabilisation de la mesure
  #self.tProduct.siMeasureDataReadEnd.disconnect(self.slotWriteCalibrationStab)
  #self.vFMeasureDataReadStop()
  #self.siErrorMsg.emit("Stablisation error", "Error")

  # Vérification valeur température
  if(  ( fTEMP < 5.1  )
    or ( fTEMP > 39.9 ) ):
   # Suppression du lien
   self.tProduct.siMeasureDataReadEnd.disconnect(self.slotWriteCalibrationStab)
   # Arrêt mesure
   self.vFMeasureDataReadStop()

   Cal_Flag = 0
   Cal_Start = 0
   sErrorBoxTitle = "Calibration error!"
   sErrorBoxText  = "Temperature must be above 5C\n" + "Please warm and start again"
   if( fTEMP > 39.9 ): sErrorBoxText = "Temperature must be below 40C\n" + "Please cool and start again"
   # Message d'erreur
   self.siCalibrationStabilizeError.emit(sErrorBoxTitle, sErrorBoxText)
   # Sort
   return

  #-- Temperature trend --
  self.fTemp_T4 = self.fTemp_T3
  self.fTemp_T3 = self.fTemp_T2
  self.fTemp_T2 = self.fTemp_T1
  self.fTemp_T1 = fTEMP
  iTempTrend = 0
  if( self.fTemp_T4 - fTEMP < 0 ): iTempTrend = 1
  if( self.fTemp_T4 - fTEMP > 0 ): iTempTrend = -1

  #-- EC trend --
  self.EC_T4 = self.EC_T3
  self.EC_T3 = self.EC_T2
  self.EC_T2 = self.EC_T1
  self.EC_T1 = fEC
  EC_trend = 0
  # Trend set to +/- 1%
  if( fEC >= 500 ):
   if( fEC > ( self.EC_T4 * 1.01 ) ): EC_trend = 1
   if( fEC < ( self.EC_T4 * 0.99 ) ): EC_trend = -1
  # Trend set to +/- 5uS
  if( fEC < 500 ):
   if( fEC > ( self.EC_T4 + 5 ) ): EC_trend = 1
   if( fEC < ( self.EC_T4 - 5 ) ): EC_trend = -1

  #-- Depth trend --
  self.D_T4 = self.D_T3
  self.D_T3 = self.D_T2
  self.D_T2 = self.D_T1
  self.D_T1 = int(fDepth * 100) + 10
  if( self.D_T1 < 0 ): self.D_T1 = self.D_T1 * -1
  Depth_trend = 0
  if( self.D_T1 > ( self.D_T4 * 1.01 ) ): Depth_trend = 1
  if( self.D_T1 < ( self.D_T4 * 0.99 ) ): Depth_trend = -1

  #-- DO trend --
  self.DO_T4 = self.DO_T3
  self.DO_T3 = self.DO_T2
  self.DO_T2 = self.DO_T1
  self.DO_T1 = fDOsat
  DO_trend = 0
  if( fDOsat > ( self.DO_T4 + 1 ) ): DO_trend = 1
  if( fDOsat < ( self.DO_T4 - 1 ) ): DO_trend = -1

  #-- pH trend --
  self.PH_T4 = self.PH_T3
  self.PH_T3 = self.PH_T2
  self.PH_T2 = self.PH_T1
  self.PH_T1 = fPH
  PH_trend = 0
  if( ( self.PH_T4 - fPH ) < 0 ): PH_trend = 1
  if( ( self.PH_T4 - fPH ) > 0 ): PH_trend = -1

  #-- ORP trend --
  self.ORP_T4 = self.ORP_T3
  self.ORP_T3 = self.ORP_T2
  self.ORP_T2 = self.ORP_T1
  self.ORP_T1 = fORP + 2000 # Allow for negative values
  ORP_trend = 0
  if( ( fORP + 2000 ) > ( self.ORP_T4 + 1 ) ): ORP_trend = 1
  if( ( fORP + 2000 ) < ( self.ORP_T4 - 1 ) ): ORP_trend = -1

  #-- Tbd trend for AP-800 --
  self.TURB_T4 = self.TURB_T3
  self.TURB_T3 = self.TURB_T2
  self.TURB_T2 = self.TURB_T1
  self.TURB_T1 = fAUX1
  Turb_Trend = 0
  if( fAUX1 > ( self.TURB_T4 + 1 ) ): Turb_Trend = 1
  if( fAUX1 < ( self.TURB_T4 - 1 ) ): Turb_Trend = -1

  #-- AUX trend --
  AUX1_TREND = ttConfig["SENSOR"]["AUX1"]["iTrend"]
  AUX2_TREND = ttConfig["SENSOR"]["AUX2"]["iTrend"]
  AUX3_TREND = ttConfig["SENSOR"]["AUX3"]["iTrend"]
  AUX4_TREND = ttConfig["SENSOR"]["AUX4"]["iTrend"]
  AUX5_TREND = ttConfig["SENSOR"]["AUX5"]["iTrend"]
  AUX6_TREND = ttConfig["SENSOR"]["AUX6"]["iTrend"]
  AUX7_TREND = ttConfig["SENSOR"]["AUX7"]["iTrend"]

  self.uiStabCpt = self.uiStabCpt + 1
  # Mise à jour de la loading bar
  if( self.uiStabCpt < 39 ): self.siCalibrationStabProgress.emit( self.uiStabCpt )

  Cal_Start = 0
  uiCode = self.uiCode
  #-- ORP --
  if(   ( uiCode     == 217 )
    and ( iTempTrend == 0   )
    and ( ORP_trend  == 0   )
    and ( self.uiStabCpt > self.uiStabDuration  ) ): Cal_Start = 1
  #-- pH --
  if(   (  ( uiCode == 219 )
        or ( uiCode == 220 )
        or ( uiCode == 221 ) )
    and ( iTempTrend == 0 )
    and ( PH_trend   == 0 )
    and ( self.uiStabCpt > self.uiStabDuration ) ): Cal_Start = 1
  #-- DO --
  if(   (  ( uiCode == 222 )
        or ( uiCode == 223 ) )
    and ( iTempTrend == 0 )
    and ( DO_trend == 0 )
    and ( self.uiStabCpt > self.uiStabDuration ) ): Cal_Start = 1
  #-- EC --
  if(   ( uiCode     == 224 )
    and ( iTempTrend == 0 )
    and ( EC_trend   == 0 )
    and ( self.uiStabCpt > self.uiStabDuration ) ): Cal_Start = 1
  #-- AUX1 --
  if(   (  ( uiCode == 237 )
        or ( uiCode == 238 )
        or ( uiCode == 239 ) )
    and ( iTempTrend == 0  )
    and ( AUX1_TREND == 0  )
    and ( self.uiStabCpt > self.uiStabDuration ) ): Cal_Start = 1
  #-- AUX1 as TURB for AP-800 --
  if(   (  ( uiCode == 216 )
        or ( uiCode == 219 )
        or ( uiCode == 239 ) )
    and ( iTempTrend == 0 )
    and ( Turb_Trend == 0 )
    and ( self.uiStabCpt > self.uiStabDuration ) ): Cal_Start = 1
  #-- AUX2 --
  if(   (  ( uiCode == 240 )
        or ( uiCode == 241 )
        or ( uiCode == 242 ) )
    and ( iTempTrend == 0 )
    and ( AUX2_TREND == 0 )
    and ( self.uiStabCpt > self.uiStabDuration ) ): Cal_Start = 1
  #-- AUX3 --
  if(   (  ( uiCode == 243 )
        or ( uiCode == 244 )
        or ( uiCode == 245 ) )
    and ( iTempTrend == 0 )
    and ( AUX3_TREND == 0 )
    and ( self.uiStabCpt > self.uiStabDuration ) ): Cal_Start = 1
  #-- AUX4 --
  if(   (  ( uiCode == 246 )
        or ( uiCode == 247 )
        or ( uiCode == 248 ) )
    and ( iTempTrend == 0  )
    and ( AUX4_TREND == 0  )
    and ( self.uiStabCpt > self.uiStabDuration ) ): Cal_Start = 1
  #-- AUX5 --
  if(   (  ( uiCode == 249 )
        or ( uiCode == 250 )
        or ( uiCode == 251 ) )
    and ( iTempTrend == 0  )
    and ( AUX5_TREND == 0  )
    and ( self.uiStabCpt > self.uiStabDuration ) ): Cal_Start = 1
  #-- AUX6 --
  if(   (  ( uiCode == 252 )
        or ( uiCode == 253 )
        or ( uiCode == 254 ) )
    and ( iTempTrend == 0  )
    and ( AUX6_TREND == 0  )
    and ( self.uiStabCpt > self.uiStabDuration ) ): Cal_Start = 1
  #-- Depth --
  if(   ( uiCode      == 233 )
    and ( iTempTrend  == 0   )
    and ( Depth_trend == 0   )
    and ( self.uiStabCpt > self.uiStabDuration ) ): Cal_Start = 1

  AUX1_TYP = ttConfig["SENSOR"]["AUX1"]["uiIndex"]
  AUX2_TYP = ttConfig["SENSOR"]["AUX2"]["uiIndex"]
  AUX3_TYP = ttConfig["SENSOR"]["AUX3"]["uiIndex"]
  AUX4_TYP = ttConfig["SENSOR"]["AUX4"]["uiIndex"]
  AUX5_TYP = ttConfig["SENSOR"]["AUX5"]["uiIndex"]
  AUX6_TYP = ttConfig["SENSOR"]["AUX6"]["uiIndex"]

  # RapidCal
  if( ( uiCode == 226 ) and ( EC_trend == 0 ) and ( iTempTrend == 0 ) and ( PH_trend == 0 ) and ( self.uiStabCpt > 30 ) ): Cal_Start = 1
  if( ( uiCode == 226 ) and ( AUX1_TYP > 5 )  and ( AUX1_TREND != 0 ) ): Cal_Start = 0
  if( ( uiCode == 216 ) and ( AUX1_TYP == 6 ) and ( Turb_Trend != 0 ) ): Cal_Start = 0 # AP-800 Turb
  if( ( uiCode == 226 ) and ( AUX2_TYP > 5 )  and ( AUX2_TREND != 0 ) ): Cal_Start = 0
  if( ( uiCode == 226 ) and ( AUX3_TYP > 5 )  and ( AUX3_TREND != 0 ) ): Cal_Start = 0
  if( ( uiCode == 226 ) and ( AUX4_TYP > 5 )  and ( AUX4_TREND != 0 ) ): Cal_Start = 0
  if( ( uiCode == 226 ) and ( AUX5_TYP > 5 )  and ( AUX5_TREND != 0 ) ): Cal_Start = 0
  if( ( uiCode == 226 ) and ( AUX6_TYP > 5 )  and ( AUX6_TREND != 0 ) ): Cal_Start = 0

  # Si mesure stabilisé suffisamment pour calibration
  if( Cal_Start == 1 ):
   # Arrêt mesure
   self.vFMeasureDataReadStop()
   # Changement jauge
   self.siCalibrationStabProgress.emit( 40 )
   # Ajout d'une attente pour fin de mesure de 2 secondes (cadence de mesure sonde)
   time.sleep(0.5)
   self.siCalibrationStabProgress.emit( 50 )
   time.sleep(0.5)
   self.siCalibrationStabProgress.emit( 60 )
   time.sleep(0.5)
   self.siCalibrationStabProgress.emit( 70 )
   time.sleep(0.5)
   self.siCalibrationStabProgress.emit( 100 )
   # Fermeture fenêtre
   self.siCalibrationStabStop.emit()
   # Suppression du lien
   self.tProduct.siMeasureDataReadEnd.disconnect(self.slotWriteCalibrationStab)

   print("CALIBRATE")
   # Envoi de la commande
   ##self.tCalibConfigObj
   self.tProduct.bFProductCalibrationWriteGSInitiate( self.uiCode, self.tCalibConfigObj )
   # On quitte ici
   return

  # Atteinte du timeout
  if( self.uiStabCpt == 60 ):
   # Suppression du lien
   self.tProduct.siMeasureDataReadEnd.disconnect(self.slotWriteCalibrationStab)
   # Arrêt mesure
   self.vFMeasureDataReadStop()
   #Cal_Flag = 0
   #Cal_Start = 0
   sErrorBoxTitle = "Calibration error!"
   sErrorBoxText  = "The readings will not stabilise" + "\nPlease investigate and try again"
   # Signal d'erreur stabilisation
   self.siCalibrationStabilizeError.emit(sErrorBoxTitle, sErrorBoxText)
   return

 #----------------------------------------------
 # Ecriture AUX channel assignement
 #----------------------------------------------
 #@Slot(str)
 def slotWriteGSFactor(self, sChannel, uiChannel, fValue):
  print("== slotWriteGSFactor ==")
  print("sChannel = " + sChannel )
  print("fValue   = %f"%fValue)
  # Test grab sample factor
  if(   ( self.tProduct.ttConfig["SENSOR"]["AUX"+str(uiChannel+1)]["sIndex"] != "EMPTY" )
    and ( sChannel != "EMPTY" ) ):
   # Ajout du coefficient sur la voie attribuée
   self.tProduct.ttConfig["SENSOR"]["AUX"+str(uiChannel+1)]["fGS"] = fValue
  # Ecriture dans sonde
  self.tProduct.bFProductInitiateGSWrite( bGSOnly=True )

 #----------------------------------------------
 # Calibration - Ecriture point Restore default
 #----------------------------------------------
 def slotWriteCalibrationPointRestoreDefault( self, sChannelName ):
  print("== slotWriteCalibrationPointRestoreDefault ==")
  print("sChannelName = " + sChannelName )
  # Conservation variable
  self.sChannelName = sChannelName
  uiCode = 0
  # Conversion du nom du point
  if( sChannelName == "PH"   ): uiCode = 211 # 0xD3
  if( sChannelName == "ORP"  ): uiCode = 211 # 0xD3
  if( sChannelName == "DO"   ): uiCode = 213 # 0xD5
  if( sChannelName == "EC"   ): uiCode = 213 # 0xD5
  if( sChannelName == "AUX1" ): uiCode = 227 # 0xE3
  if( sChannelName == "AUX2" ): uiCode = 228 # 0xE4
  if( sChannelName == "AUX3" ): uiCode = 232 # 0xE8
  if( sChannelName == "AUX4" ): uiCode = 234 # 0xEA
  if( sChannelName == "AUX5" ): uiCode = 235 # 0xEB
  if( sChannelName == "AUX6" ): uiCode = 236 # 0xEC
  # Si code bien trouvé
  if( uiCode != 0 ):
   # Envoi du direct access mode
   #self.tProduct.bFGetDirectAccessMode_CalibrationRestoreDefault( uiCode )
   self.tProduct.bFCalibrationRestoreDefault( uiCode )

 #----------------------------------------------
 # Calibration - Ecriture point Restore default
 #----------------------------------------------
 def slotWriteCalibrationErrorMsg( self, sError ):

  uiPointNumber = self.uiPointNumber
  uiCode        = self.uiCode
  # Etat initial du message
  sMessage = sError

  #-- Temperature fail --
  if( sError == "Temperature fail" ):
   sMessage = "The temperature is outside the calibration limits\nPlease investigate and try again"
   # Si point 2
   if( uiPointNumber == 1 ):
    sMessage = "The temperature of Point 2 must be within 1C of Point 1\nPlease correct and try again"
   # Si point 3
   if( uiPointNumber == 2 ):
     sMessage = "The temperature of Point 3 must be at least 10C cooler than Point 1\nPlease correct and try again"

  #-- Range fail --
  if( sError == "Range fail" ):
   sMessage = "The readings are outside the calibration limits\nCheck you are using the correct standard and try again"
   # RapidCal
   if( uiCode == 226 ):
    sMessage = "One or more of the readings are outside the calibration limits\nCheck you are using fresh RapidCal and that all electrodes are covered"

  #-- DO fail --
  if( sError == "DO fail" ):
   sMessage = "There is a problem with the DO sensor.\nPlease investigate and try again"

  # Emet le message d'erreur
  self.siCalibrationCMDPointError.emit(sMessage)


 #----------------------------------------------
 # Calibration - Ecriture point Restore default
 #----------------------------------------------
 def vFCALIBSaveTemperatureCalibEnd( self ):
  ttConfig = self.tProduct.ttConfig
  #-- Temperature
  # pH
  if( self.uiCode == 221 ): ttConfig["SENSOR"]["PH"]["Point"][0]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  if( self.uiCode == 220 ): ttConfig["SENSOR"]["PH"]["Point"][1]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  if( self.uiCode == 219 ): ttConfig["SENSOR"]["PH"]["Point"][2]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  # ORP
  if( self.uiCode == 217 ): ttConfig["SENSOR"]["ORP"]["Point"][0]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  if( self.uiCode == 216 ): ttConfig["SENSOR"]["ORP"]["Point"][0]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  # DO
  if( self.uiCode == 222 ): ttConfig["SENSOR"]["DO"]["Point"][0]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  if( self.uiCode == 223 ): ttConfig["SENSOR"]["DO"]["Point"][1]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  # EC
  if( self.uiCode == 231 ): ttConfig["SENSOR"]["EC"]["Point"][0]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  if( self.uiCode == 229 ): ttConfig["SENSOR"]["EC"]["Point"][0]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  if( self.uiCode == 210 ): ttConfig["SENSOR"]["EC"]["Point"][0]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  if( self.uiCode == 224 ): ttConfig["SENSOR"]["EC"]["Point"][0]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  # AUX1
  if( self.uiCode == 237 ): ttConfig["SENSOR"]["AUX1"]["Point"][0]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  if( self.uiCode == 238 ): ttConfig["SENSOR"]["AUX1"]["Point"][1]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  if( self.uiCode == 239 ): ttConfig["SENSOR"]["AUX1"]["Point"][2]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  # AUX2
  if( self.uiCode == 240 ): ttConfig["SENSOR"]["AUX2"]["Point"][0]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  if( self.uiCode == 241 ): ttConfig["SENSOR"]["AUX2"]["Point"][1]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  if( self.uiCode == 242 ): ttConfig["SENSOR"]["AUX2"]["Point"][2]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  # AUX3
  if( self.uiCode == 243 ): ttConfig["SENSOR"]["AUX3"]["Point"][0]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  if( self.uiCode == 244 ): ttConfig["SENSOR"]["AUX3"]["Point"][1]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  if( self.uiCode == 245 ): ttConfig["SENSOR"]["AUX3"]["Point"][2]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  # AUX4
  if( self.uiCode == 246 ): ttConfig["SENSOR"]["AUX4"]["Point"][0]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  if( self.uiCode == 247 ): ttConfig["SENSOR"]["AUX4"]["Point"][1]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  if( self.uiCode == 248 ): ttConfig["SENSOR"]["AUX4"]["Point"][2]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  # AUX5
  if( self.uiCode == 249 ): ttConfig["SENSOR"]["AUX5"]["Point"][0]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  if( self.uiCode == 250 ): ttConfig["SENSOR"]["AUX5"]["Point"][1]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  if( self.uiCode == 251 ): ttConfig["SENSOR"]["AUX5"]["Point"][2]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  # AUX6
  if( self.uiCode == 252 ): ttConfig["SENSOR"]["AUX4"]["Point"][0]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  if( self.uiCode == 253 ): ttConfig["SENSOR"]["AUX4"]["Point"][1]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  if( self.uiCode == 254 ): ttConfig["SENSOR"]["AUX4"]["Point"][2]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  #-- Pression
  # pH
  if( self.uiCode == 221 ): ttConfig["SENSOR"]["PH"]["Point"][0]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  if( self.uiCode == 220 ): ttConfig["SENSOR"]["PH"]["Point"][1]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  if( self.uiCode == 219 ): ttConfig["SENSOR"]["PH"]["Point"][2]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  # ORP
  if( self.uiCode == 217 ): ttConfig["SENSOR"]["ORP"]["Point"][0]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  if( self.uiCode == 216 ): ttConfig["SENSOR"]["ORP"]["Point"][0]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  # DO
  if( self.uiCode == 222 ): ttConfig["SENSOR"]["DO"]["Point"][0]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  if( self.uiCode == 223 ): ttConfig["SENSOR"]["DO"]["Point"][1]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  # EC
  if( self.uiCode == 231 ): ttConfig["SENSOR"]["EC"]["Point"][0]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  if( self.uiCode == 229 ): ttConfig["SENSOR"]["EC"]["Point"][0]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  if( self.uiCode == 210 ): ttConfig["SENSOR"]["EC"]["Point"][0]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  if( self.uiCode == 224 ): ttConfig["SENSOR"]["EC"]["Point"][0]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  # AUX1
  if( self.uiCode == 237 ): ttConfig["SENSOR"]["AUX1"]["Point"][0]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  if( self.uiCode == 238 ): ttConfig["SENSOR"]["AUX1"]["Point"][1]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  if( self.uiCode == 239 ): ttConfig["SENSOR"]["AUX1"]["Point"][2]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  # AUX2
  if( self.uiCode == 240 ): ttConfig["SENSOR"]["AUX2"]["Point"][0]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  if( self.uiCode == 241 ): ttConfig["SENSOR"]["AUX2"]["Point"][1]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  if( self.uiCode == 242 ): ttConfig["SENSOR"]["AUX2"]["Point"][2]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  # AUX3
  if( self.uiCode == 243 ): ttConfig["SENSOR"]["AUX3"]["Point"][0]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  if( self.uiCode == 244 ): ttConfig["SENSOR"]["AUX3"]["Point"][1]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  if( self.uiCode == 245 ): ttConfig["SENSOR"]["AUX3"]["Point"][2]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  # AUX4
  if( self.uiCode == 246 ): ttConfig["SENSOR"]["AUX4"]["Point"][0]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  if( self.uiCode == 247 ): ttConfig["SENSOR"]["AUX4"]["Point"][1]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  if( self.uiCode == 248 ): ttConfig["SENSOR"]["AUX4"]["Point"][2]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  # AUX5
  if( self.uiCode == 249 ): ttConfig["SENSOR"]["AUX5"]["Point"][0]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  if( self.uiCode == 250 ): ttConfig["SENSOR"]["AUX5"]["Point"][1]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  if( self.uiCode == 251 ): ttConfig["SENSOR"]["AUX5"]["Point"][2]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  # AUX6
  if( self.uiCode == 252 ): ttConfig["SENSOR"]["AUX4"]["Point"][0]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  if( self.uiCode == 253 ): ttConfig["SENSOR"]["AUX4"]["Point"][1]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]
  if( self.uiCode == 254 ): ttConfig["SENSOR"]["AUX4"]["Point"][2]["fPressure"] = ttConfig["SENSOR"]["Baro"]["fResult"]

