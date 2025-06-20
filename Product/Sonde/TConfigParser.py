# -*- coding: utf-8 -*-
#============================================================================#
# Fichier .........: "TConfigParser.py"
# Auteur ..........: Alexandre Paillot
# Date de création : 2024/06/12
#----------------------------------------------------------------------------#
''' Description :
    Analyse et extraction des paramètres de la configuration.

'''
#============================================================================#

#============================================================================#
# Déclaration des librairies standart
#============================================================================#
import os
import sys
import time
import datetime
import traceback
import struct
from datetime import datetime

#============================================================================#
# Déclaration des librairies Qt
#============================================================================#
from PySide6.QtCore import QByteArray, Signal, QObject

#============================================================================#
# Déclaration des librairies projet
#============================================================================#
from Vue.VMainWindowLib import *

#============================================================================#
# Librairies Utilisateur
#============================================================================#

#============================================================================#
# Déclaration des fonctions
#============================================================================#

#============================================================================#
# Déclaration des classes
#============================================================================#

#-------------------------------------------------------
# Gestion de la liaison série bas niveau
#-------------------------------------------------------
class TConfigParser:
 #--------------------------
 # Constructeur de ma classe
 #--------------------------
 def __init__( self ):
  pass
 #--------------------------
 # Constructeur de ma classe
 #--------------------------
 def vFInitConfigObj( self, ttConfig ):
  print("-- vFInitConfigObj --")

  ttConfig["PRODUCT"]          = {}
  ttConfig["SENSOR"]           = {}
  ttConfig["CALCULATED"]       = {}
  ttConfig["SENSOR"]["TEMP"]   = {}
  ttConfig["SENSOR"]["EC"]     = {}
  ttConfig["SENSOR"]["DO"]     = {}
  ttConfig["SENSOR"]["DO Sat"]  = {}
  ttConfig["SENSOR"]["PH"]     = {}
  ttConfig["SENSOR"]["PHmv"]   = {}
  ttConfig["SENSOR"]["ORP"]    = {}
  ttConfig["SENSOR"]["Depth"]  = {}
  ttConfig["SENSOR"]["Baro"]   = {}
  ttConfig["SENSOR"]["Baro"]["fResult"] = 0
  ttConfig["SENSOR"]["AUX1"]   = {}
  ttConfig["SENSOR"]["AUX2"]   = {}
  ttConfig["SENSOR"]["AUX3"]   = {}
  ttConfig["SENSOR"]["AUX4"]   = {}
  ttConfig["SENSOR"]["AUX5"]   = {}
  ttConfig["SENSOR"]["AUX6"]   = {}
  ttConfig["SENSOR"]["AUX7"]   = {}

  ttConfig["SENSOR"]["PH"]["Point"]   = []
  ttConfig["SENSOR"]["PH"]["Point"].append({})   # PH 7
  ttConfig["SENSOR"]["PH"]["Point"].append({})   # PH 4.01
  ttConfig["SENSOR"]["PH"]["Point"].append({})   # PH 10.0
  ttConfig["SENSOR"]["ORP"]["Point"]  = []
  ttConfig["SENSOR"]["ORP"]["Point"].append({})  # ORP Cal
  ttConfig["SENSOR"]["DO"]["Point"]   = []
  ttConfig["SENSOR"]["DO"]["Point"].append({})   # Zero cal
  ttConfig["SENSOR"]["DO"]["Point"].append({})   # 100% cal
  ttConfig["SENSOR"]["EC"]["Point"]   = []
  ttConfig["SENSOR"]["EC"]["Point"].append({})   # EC cal
  ttConfig["SENSOR"]["AUX1"]["Point"] = []
  ttConfig["SENSOR"]["AUX1"]["Point"].append({}) # PT1
  ttConfig["SENSOR"]["AUX1"]["Point"].append({}) # PT2
  ttConfig["SENSOR"]["AUX1"]["Point"].append({}) # PT3
  ttConfig["SENSOR"]["AUX2"]["Point"] = []
  ttConfig["SENSOR"]["AUX2"]["Point"].append({}) # PT1
  ttConfig["SENSOR"]["AUX2"]["Point"].append({}) # PT2
  ttConfig["SENSOR"]["AUX2"]["Point"].append({}) # PT3
  ttConfig["SENSOR"]["AUX3"]["Point"] = []
  ttConfig["SENSOR"]["AUX3"]["Point"].append({}) # PT1
  ttConfig["SENSOR"]["AUX3"]["Point"].append({}) # PT2
  ttConfig["SENSOR"]["AUX3"]["Point"].append({}) # PT3
  ttConfig["SENSOR"]["AUX4"]["Point"] = []
  ttConfig["SENSOR"]["AUX4"]["Point"].append({}) # PT1
  ttConfig["SENSOR"]["AUX4"]["Point"].append({}) # PT2
  ttConfig["SENSOR"]["AUX4"]["Point"].append({}) # PT3
  ttConfig["SENSOR"]["AUX5"]["Point"] = []
  ttConfig["SENSOR"]["AUX5"]["Point"].append({}) # PT1
  ttConfig["SENSOR"]["AUX5"]["Point"].append({}) # PT2
  ttConfig["SENSOR"]["AUX5"]["Point"].append({}) # PT3
  ttConfig["SENSOR"]["AUX6"]["Point"] = []
  ttConfig["SENSOR"]["AUX6"]["Point"].append({}) # PT1
  ttConfig["SENSOR"]["AUX6"]["Point"].append({}) # PT2
  ttConfig["SENSOR"]["AUX6"]["Point"].append({}) # PT3
  # Calculated
  ttConfig["CALCULATED"]["AMMONIA"] = {}
  ttConfig["CALCULATED"]["EC"]      = {}
  ttConfig["CALCULATED"]["TEMP"]    = {}
  ttConfig["CALCULATED"]["DEPTH"]   = {}

  ttConfig["CALCULATED"]["Salinity"] = {}
  ttConfig["CALCULATED"]["SSG"]      = {}
  ttConfig["CALCULATED"]["TDS"]      = {}

  ttConfig["CALCULATED"]["TEMP"]["bC"]  = True
  ttConfig["CALCULATED"]["TEMP"]["bF"]  = False
  ttConfig["CALCULATED"]["DEPTH"]["bM"] = True
  ttConfig["CALCULATED"]["DEPTH"]["bF"] = False

  # Voies fixes (index manuel négatif)
  ttConfig["SENSOR"]["TEMP"  ]["uiIndex"] = -1
  ttConfig["SENSOR"]["EC"    ]["uiIndex"] = -2
  ttConfig["SENSOR"]["DO"    ]["uiIndex"] = -3
  ttConfig["SENSOR"]["DO Sat"]["uiIndex"] = -4
  ttConfig["SENSOR"]["PH"    ]["uiIndex"] = -5
  ttConfig["SENSOR"]["PHmv"  ]["uiIndex"] = -6
  ttConfig["SENSOR"]["ORP"   ]["uiIndex"] = -7
  ttConfig["SENSOR"]["Depth" ]["uiIndex"] = -8
  ttConfig["SENSOR"]["Baro"  ]["uiIndex"] = -9
  # Nom de voie : fixed
  ttConfig["SENSOR"]["TEMP"  ]["sIndex"] = "Temperature"
  ttConfig["SENSOR"]["EC"    ]["sIndex"] = "EC"
  ttConfig["SENSOR"]["DO"    ]["sIndex"] = "DO"
  ttConfig["SENSOR"]["DO Sat"]["sIndex"] = "DO Sat"
  ttConfig["SENSOR"]["PH"    ]["sIndex"] = "pH"
  ttConfig["SENSOR"]["PHmv"  ]["sIndex"] = "pH mV"
  ttConfig["SENSOR"]["ORP"   ]["sIndex"] = "ORP"
  ttConfig["SENSOR"]["Depth" ]["sIndex"] = "Depth"
  ttConfig["SENSOR"]["Baro"  ]["sIndex"] = "Baro"
  # Unité
  ttConfig["SENSOR"]["TEMP"  ]["sUnit"] = "degC"
  ttConfig["SENSOR"]["EC"    ]["sUnit"] = "uS/cm"
  ttConfig["SENSOR"]["DO"    ]["sUnit"] = "mg/L"
  ttConfig["SENSOR"]["DO Sat"]["sUnit"] = "%Sat"
  ttConfig["SENSOR"]["PH"    ]["sUnit"] = "pH"
  ttConfig["SENSOR"]["PHmv"  ]["sUnit"] = "mV"
  ttConfig["SENSOR"]["ORP"   ]["sUnit"] = "mV"
  ttConfig["SENSOR"]["Depth" ]["sUnit"] = "m"
  ttConfig["SENSOR"]["Baro"  ]["sUnit"] = "mB"
  # Nom de voie : fixed
  ttConfig["SENSOR"]["TEMP"  ]["sIndexCSV"] = "Temp"
  ttConfig["SENSOR"]["Depth" ]["sIndexCSV"] = "Depth"
  ttConfig["SENSOR"]["Baro"  ]["sIndexCSV"] = "Baro"
  ttConfig["SENSOR"]["PH"    ]["sIndexCSV"] = "pH"
  ttConfig["SENSOR"]["PHmv"  ]["sIndexCSV"] = "pH mV"
  ttConfig["SENSOR"]["ORP"   ]["sIndexCSV"] = "ORP"
  ttConfig["SENSOR"]["DO Sat"]["sIndexCSV"] = "DO"
  ttConfig["SENSOR"]["DO"    ]["sIndexCSV"] = "DO"
  ttConfig["SENSOR"]["EC"    ]["sIndexCSV"] = "EC"
  # Unité
  ttConfig["SENSOR"]["TEMP"  ]["sUnitCSV"] = "C"
  ttConfig["SENSOR"]["Depth" ]["sUnitCSV"] = "m"
  ttConfig["SENSOR"]["Baro"  ]["sUnitCSV"] = "mB"
  ttConfig["SENSOR"]["PH"    ]["sUnitCSV"] = ""
  ttConfig["SENSOR"]["PHmv"  ]["sUnitCSV"] = "mV"
  ttConfig["SENSOR"]["ORP"   ]["sUnitCSV"] = "mV"
  ttConfig["SENSOR"]["DO Sat"]["sUnitCSV"] = "%Sat"
  ttConfig["SENSOR"]["DO"    ]["sUnitCSV"] = "mg/L"
  ttConfig["SENSOR"]["EC"    ]["sUnitCSV"] = "uS/cm"
  # Etat de la calibration
  ttConfig["SENSOR"]["PH"]["Point"][0]["bCalibrated"]    = False # PH 7
  ttConfig["SENSOR"]["PH"]["Point"][1]["bCalibrated"]    = False # PH 4.01
  ttConfig["SENSOR"]["PH"]["Point"][2]["bCalibrated"]    = False # PH 10.0
  ttConfig["SENSOR"]["ORP"]["Point"][0]["bCalibrated"]   = False # ORP Cal
  ttConfig["SENSOR"]["DO"]["Point"][0]["bCalibrated"]    = False # Zero cal
  ttConfig["SENSOR"]["DO"]["Point"][0]["bCalibrated"]    = False # 100% cal
  ttConfig["SENSOR"]["EC"]["Point"][0]["bCalibrated"]    = False # EC cal
  ttConfig["SENSOR"]["AUX1"]["Point"][0]["bCalibrated"]  = False # AUX1 - PT1
  ttConfig["SENSOR"]["AUX1"]["Point"][1]["bCalibrated"]  = False # AUX1 - PT2
  ttConfig["SENSOR"]["AUX1"]["Point"][2]["bCalibrated"]  = False # AUX1 - PT3
  ttConfig["SENSOR"]["AUX2"]["Point"][0]["bCalibrated"]  = False # AUX2 - PT1
  ttConfig["SENSOR"]["AUX2"]["Point"][1]["bCalibrated"]  = False # AUX2 - PT2
  ttConfig["SENSOR"]["AUX2"]["Point"][2]["bCalibrated"]  = False # AUX2 - PT3
  ttConfig["SENSOR"]["AUX3"]["Point"][0]["bCalibrated"]  = False # AUX3 - PT1
  ttConfig["SENSOR"]["AUX3"]["Point"][1]["bCalibrated"]  = False # AUX3 - PT2
  ttConfig["SENSOR"]["AUX3"]["Point"][2]["bCalibrated"]  = False # AUX3 - PT3
  ttConfig["SENSOR"]["AUX4"]["Point"][0]["bCalibrated"]  = False # AUX4 - PT1
  ttConfig["SENSOR"]["AUX4"]["Point"][1]["bCalibrated"]  = False # AUX4 - PT2
  ttConfig["SENSOR"]["AUX4"]["Point"][2]["bCalibrated"]  = False # AUX4 - PT3
  ttConfig["SENSOR"]["AUX5"]["Point"][0]["bCalibrated"]  = False # AUX5 - PT1
  ttConfig["SENSOR"]["AUX5"]["Point"][1]["bCalibrated"]  = False # AUX5 - PT2
  ttConfig["SENSOR"]["AUX5"]["Point"][2]["bCalibrated"]  = False # AUX5 - PT3
  ttConfig["SENSOR"]["AUX6"]["Point"][0]["bCalibrated"]  = False # AUX6 - PT1
  ttConfig["SENSOR"]["AUX6"]["Point"][1]["bCalibrated"]  = False # AUX6 - PT2
  ttConfig["SENSOR"]["AUX6"]["Point"][2]["bCalibrated"]  = False # AUX6 - PT3

 #--------------------------
 # Extraction des champs Setup Data
 #--------------------------
 def ttFParseSetupData( self, sDataRead, ttConfig ):
  print("-- ttFParseSetupData --")
  print("len(sDataRead) = %d"%len(sDataRead))
  #                             112112112219 3 6 3 3 16 7 8
  txUnpacked = struct.unpack( '>BBHBBBHBBHB9B3B6B3B3B16s7s8s', sDataRead )
  print(txUnpacked)
  uiCpt = 0

  uiTMP1        = txUnpacked[uiCpt]; uiCpt+=1
  uiTMP2        = txUnpacked[uiCpt]; uiCpt+=1
  uiLogMin      = txUnpacked[uiCpt]; uiCpt+=1
  uiLogSec      = txUnpacked[uiCpt]; uiCpt+=1
  uiLogEvent    = txUnpacked[uiCpt]; uiCpt+=1
  uiLogSensor   = txUnpacked[uiCpt]; uiCpt+=1
  uiEventMin    = txUnpacked[uiCpt]; uiCpt+=1
  uiCleanHR     = txUnpacked[uiCpt]; uiCpt+=1
  uiEventChange = txUnpacked[uiCpt]; uiCpt+=1
  uiBatt        = txUnpacked[uiCpt]; uiCpt+=1; fBatt = float(uiBatt) / 102.3
  uiBattPC      = txUnpacked[uiCpt]; uiCpt+=1

  # Si flag seconde
  if( uiLogSec == 1 ):
   uiLogSec = uiLogMin
   uiLogMin = 0
  ttConfig["PRODUCT"]["uiLOG_HOUR"]     = int( uiLogMin / 60 )
  ttConfig["PRODUCT"]["uiLOG_MIN"]      = int( uiLogMin % 60 )
  ttConfig["PRODUCT"]["uiLOG_SEC"]      = uiLogSec
  ttConfig["PRODUCT"]["uiLOG_EVENT"]    = uiLogEvent
  ttConfig["PRODUCT"]["uiLOG_SENSOR"]   = uiLogSensor
  ttConfig["PRODUCT"]["sLOG_SENSOR"]    = self.sFGetLogSensorNameWithIndex(uiLogSensor)
  ttConfig["PRODUCT"]["uiCLEAN_HR"]     = uiCleanHR
  ttConfig["PRODUCT"]["uiEVENT_CHANGE"] = uiEventChange
  ttConfig["PRODUCT"]["uiBatt"]         = uiBatt
  ttConfig["PRODUCT"]["fBATT"]          = fBatt
  ttConfig["PRODUCT"]["uiBATT_PC"]      = uiBattPC
  ttConfig["PRODUCT"]["uiEVENT_HOUR"]   = int( uiEventMin / 60 )
  ttConfig["PRODUCT"]["uiEVENT_MIN"]    = int( uiEventMin % 60 )

  print("uiLogSec = %d"%uiLogSec)
  print("uiLOG_MIN = %d"%ttConfig["PRODUCT"]["uiLOG_MIN"])

  uiPSN1      = txUnpacked[uiCpt]; uiCpt+=1
  uiPSN2      = txUnpacked[uiCpt]; uiCpt+=1
  uiPSN3      = txUnpacked[uiCpt]; uiCpt+=1
  uiPSN4      = txUnpacked[uiCpt]; uiCpt+=1
  uiPSN5      = txUnpacked[uiCpt]; uiCpt+=1
  uiPSN6      = txUnpacked[uiCpt]; uiCpt+=1
  uiPSN7      = txUnpacked[uiCpt]; uiCpt+=1
  uiPSN8      = txUnpacked[uiCpt]; uiCpt+=1
  uiPSN9      = txUnpacked[uiCpt]; uiCpt+=1
  uiPSW1      = txUnpacked[uiCpt]; uiCpt+=1
  uiPSW2      = txUnpacked[uiCpt]; uiCpt+=1
  uiPSW3      = txUnpacked[uiCpt]; uiCpt+=1

  sPSN1 = str(uiPSN1)+str(uiPSN2)+str(uiPSN3)+str(uiPSN4)+str(uiPSN5)+str(uiPSN6)+str(uiPSN7)+str(uiPSN8)+str(uiPSN9)
  uiModel = int( str(uiPSN8) + "" + str(uiPSN9) )
  print("Model: %u"% uiModel )
  ttConfig["PRODUCT"]["sPSN1"]   = sPSN1
  ttConfig["PRODUCT"]["uiModel"] = uiModel
  sModel = self.sFGetProductNameWithID(uiModel)
  ttConfig["PRODUCT"]["sModel"]      = sModel
  ttConfig["PRODUCT"]["uiAUXNumber"] = self.sFGetAUXNumberWithID(uiModel)
  # Numéro de version court
  uiPSW = int(str(uiPSW1)+str(uiPSW2)+str(uiPSW3))
  ttConfig["PRODUCT"]["uiPSW"] = uiPSW

  # Modèle
  print( ttConfig["PRODUCT"]["sModel"] )

  uiAux1Assign = txUnpacked[uiCpt]; uiCpt+=1
  uiAux2Assign = txUnpacked[uiCpt]; uiCpt+=1
  uiAux3Assign = txUnpacked[uiCpt]; uiCpt+=1
  uiAux4Assign = txUnpacked[uiCpt]; uiCpt+=1
  uiAux5Assign = txUnpacked[uiCpt]; uiCpt+=1
  uiAux6Assign = txUnpacked[uiCpt]; uiCpt+=1

  ttConfig["SENSOR"]["AUX1"]["uiIndex"]  = uiAux1Assign
  ttConfig["SENSOR"]["AUX2"]["uiIndex"]  = uiAux2Assign
  ttConfig["SENSOR"]["AUX3"]["uiIndex"]  = uiAux3Assign
  ttConfig["SENSOR"]["AUX4"]["uiIndex"]  = uiAux4Assign
  ttConfig["SENSOR"]["AUX5"]["uiIndex"]  = uiAux5Assign
  ttConfig["SENSOR"]["AUX6"]["uiIndex"]  = uiAux6Assign
  ttConfig["SENSOR"]["AUX7"]["uiIndex"]  = 254
  ttConfig["SENSOR"]["AUX1"]["sIndex"]   = self.sFGetChannelNameWithID(uiAux1Assign)
  ttConfig["SENSOR"]["AUX2"]["sIndex"]   = self.sFGetChannelNameWithID(uiAux2Assign)
  ttConfig["SENSOR"]["AUX3"]["sIndex"]   = self.sFGetChannelNameWithID(uiAux3Assign)
  ttConfig["SENSOR"]["AUX4"]["sIndex"]   = self.sFGetChannelNameWithID(uiAux4Assign)
  ttConfig["SENSOR"]["AUX5"]["sIndex"]   = self.sFGetChannelNameWithID(uiAux5Assign)
  ttConfig["SENSOR"]["AUX6"]["sIndex"]   = self.sFGetChannelNameWithID(uiAux6Assign)
  ttConfig["SENSOR"]["AUX7"]["sIndex"]   = self.sFGetChannelNameWithID(254)
  # Unité
  ttConfig["SENSOR"]["AUX1"]["sUnit"]   = self.sFGetChannelUnitWithID(uiAux1Assign)
  ttConfig["SENSOR"]["AUX2"]["sUnit"]   = self.sFGetChannelUnitWithID(uiAux2Assign)
  ttConfig["SENSOR"]["AUX3"]["sUnit"]   = self.sFGetChannelUnitWithID(uiAux3Assign)
  ttConfig["SENSOR"]["AUX4"]["sUnit"]   = self.sFGetChannelUnitWithID(uiAux4Assign)
  ttConfig["SENSOR"]["AUX5"]["sUnit"]   = self.sFGetChannelUnitWithID(uiAux5Assign)
  ttConfig["SENSOR"]["AUX6"]["sUnit"]   = self.sFGetChannelUnitWithID(uiAux6Assign)
  ttConfig["SENSOR"]["AUX7"]["sUnit"]   = self.sFGetChannelUnitWithID(254)

  uiFWR1       = txUnpacked[uiCpt]; uiCpt+=1
  uiFWR2       = txUnpacked[uiCpt]; uiCpt+=1
  uiFWR3       = txUnpacked[uiCpt]; uiCpt+=1
  uiMemHSB     = txUnpacked[uiCpt]; uiCpt+=1
  uiMemMSB     = txUnpacked[uiCpt]; uiCpt+=1
  uiMemLSB     = txUnpacked[uiCpt]; uiCpt+=1
  #sSiteID      = txUnpacked[uiCpt]; uiCpt+=1
  sSiteID      = txUnpacked[uiCpt].decode(); uiCpt+=1
  tucSiteLat   = txUnpacked[uiCpt]; uiCpt+=1
  tucSiteLong  = txUnpacked[uiCpt]; uiCpt+=1

  print(sSiteID)

  sPSW1        = str(uiPSW1)+"."+str(uiPSW2)+str(uiPSW3)+"."+str(uiFWR1)+"."+str(uiFWR2)+str(uiFWR3)
  uiMemRecords = ( ( uiMemHSB * 65536 ) + ( uiMemMSB * 256 ) + uiMemLSB ) / 55
  print("uiMemRecords = %d"%uiMemRecords)
  ttConfig["PRODUCT"]["sPSW1"]          = sPSW1
  ttConfig["PRODUCT"]["uiMemRecords"]   = int(uiMemRecords)

  sSiteLat  = ""+chr(tucSiteLat[0])+" "+str(tucSiteLat[1])+str(tucSiteLat[2])+"°"+str(tucSiteLat[3])+str(tucSiteLat[4])+"."+str(tucSiteLat[5])+str(tucSiteLat[6])+"'"
  sSiteLong = ""+chr(tucSiteLong[0])+" "+str(tucSiteLong[1])+str(tucSiteLong[2])+str(tucSiteLong[3])+"°"+str(tucSiteLong[4])+str(tucSiteLong[5])+"."+str(tucSiteLong[6])+str(tucSiteLong[7])+"'"

  uiMemRemaining = ( 150000 - uiMemRecords )
  ttConfig["PRODUCT"]["uiMemRemaining"]   = int(uiMemRemaining)
  ttConfig["PRODUCT"]["uiMemRemainingPC"] = int( uiMemRemaining * 100 / 150000 )
  ttConfig["PRODUCT"]["sSiteID"]        = sSiteID.strip()
  ttConfig["PRODUCT"]["sSiteLat"]       = sSiteLat
  ttConfig["PRODUCT"]["sSiteLong"]      = sSiteLong
  ttConfig["PRODUCT"]["tucSiteID"]      = sSiteID
  ttConfig["PRODUCT"]["tucSiteLat"]     = tucSiteLat
  ttConfig["PRODUCT"]["tucSiteLong"]    = tucSiteLong

  # Test si voie calculée ammonia
  if(  ( uiAux1Assign == 0x01 )
    or ( uiAux2Assign == 0x01 )
    or ( uiAux3Assign == 0x01 )
    or ( uiAux4Assign == 0x01 )
    or ( uiAux5Assign == 0x01 )
    or ( uiAux6Assign == 0x01 ) ):
   # Ammonia
   ttConfig["CALCULATED"]["AMMONIA"]["bActivated"] = True
  # Pas de voie Ammonia
  else:
   ttConfig["CALCULATED"]["AMMONIA"]["bActivated"] = False

  # - Estimatif Mémoire -
  # Durée acquisition
  uiLogIntBatt = ( uiLogMin * 60 ) + uiLogSec
  # Autonomie mémoire
  ttConfig["PRODUCT"]["uiMemFullDay"] = int( uiMemRemaining / ( 86400 / uiLogIntBatt ) )

  # -------------------
  # - Estimatif conso -
  # -------------------
  uiBattDayLife = self.uiFLifetimeCalculation(ttConfig)
  # Nombre de jours avant fin batterie
  ttConfig["PRODUCT"]["uiBattDeadDay"]  = uiBattDayLife

  return( ttConfig )

 #------------------------------------------------------------------------------
 # Extraction des champs RTC Data
 #------------------------------------------------------------------------------
 def ttFParseRTCData( self, sDataRead, ttConfig ):
  print("-- ttFParseRTCData --")
  print(sDataRead)
  # Decryptage de la donnée binaire
  txUnpacked = struct.unpack( '>8B', sDataRead )
  print(txUnpacked)
  uiCpt = 0
  # Extraction des champs
  uiTMP1        = txUnpacked[uiCpt]; uiCpt+=1
  uiTMP2        = txUnpacked[uiCpt]; uiCpt+=1
  uiRTCHour     = txUnpacked[uiCpt]; uiCpt+=1
  uiRTCMin      = txUnpacked[uiCpt]; uiCpt+=1
  uiRTCSec      = txUnpacked[uiCpt]; uiCpt+=1
  uiRTCDays     = txUnpacked[uiCpt]; uiCpt+=1
  uiRTCMonth    = txUnpacked[uiCpt]; uiCpt+=1
  uiRTCYear     = txUnpacked[uiCpt]; uiCpt+=1
  print("uiRTCHour  = %d" % uiRTCHour)
  print("uiRTCMin   = %d" % uiRTCMin)
  print("uiRTCSec   = %d" % uiRTCSec)
  print("uiRTCDays  = %d" % uiRTCDays)
  print("uiRTCMonth = %d" % uiRTCMonth)
  print("uiRTCYear  = %d" % uiRTCYear)

  # Placement dans l'objet de configuration
  ttConfig["PRODUCT"]["uiRTCHour"]    = uiRTCHour
  ttConfig["PRODUCT"]["uiRTCMin"]     = uiRTCMin
  ttConfig["PRODUCT"]["uiRTCSec"]     = uiRTCSec
  ttConfig["PRODUCT"]["uiRTCDays"]    = uiRTCDays
  ttConfig["PRODUCT"]["uiRTCMonth"]   = uiRTCMonth
  ttConfig["PRODUCT"]["uiRTCYear"]    = uiRTCYear
  # Formatage des dates
  sRTCDate = ("%02u"%uiRTCDays)+"/"+("%02u"%uiRTCMonth)+"/20"+("%02u"%uiRTCYear)
  sRTCTime = ("%02u"%uiRTCHour)+":"+("%02u"%uiRTCMin)+":"+("%02u"%uiRTCSec)
  # Objet conf
  ttConfig["PRODUCT"]["sRTCDate"]   = sRTCDate
  ttConfig["PRODUCT"]["sRTCTime"]   = sRTCTime
  # Retour de la config
  return( ttConfig )

 #------------------------------------------------------------------------------
 # Extraction des champs Calibration Data
 #------------------------------------------------------------------------------
 def ttFParseCalibrationData( self, sDataRead, ttConfig ):
  print("-- ttFParseCalibrationData --")
  print(sDataRead)
  # Decryptage de la donnée binaire => "<" LSB first
  # B : unsigned char (1 Byte)
  # H : unsigned short (2 Byte)
  txUnpacked = struct.unpack( "<73B 6B 6H 25H 4B B", sDataRead )
  print(txUnpacked)
  uiCpt = 0
  # Extraction des champs

  #self.ttConfig["SENSOR"]["PH"]["Point"][0]["uiValue"]
  #self.ttConfig["SENSOR"]["PH"]["Point"].append({})    # PH 4.01
  #self.ttConfig["SENSOR"]["PH"]["Point"].append({})    # PH 10.0
  uiPH4_10_Day   = txUnpacked[uiCpt]; uiCpt+=1
  uiPH4_10_Month = txUnpacked[uiCpt]; uiCpt+=1
  uiPH4_10_Year  = txUnpacked[uiCpt]; uiCpt+=1
  uiPH7_Day      = txUnpacked[uiCpt]; uiCpt+=1
  uiPH7_Month    = txUnpacked[uiCpt]; uiCpt+=1
  uiPH7_Year     = txUnpacked[uiCpt]; uiCpt+=1
  uiORP_Day      = txUnpacked[uiCpt]; uiCpt+=1
  uiORP_Month    = txUnpacked[uiCpt]; uiCpt+=1
  uiORP_Year     = txUnpacked[uiCpt]; uiCpt+=1
  uiCal_Param_10 = txUnpacked[uiCpt]; uiCpt+=1 # Plusieurs paramètres
  uiDO100_Day    = txUnpacked[uiCpt]; uiCpt+=1
  uiDO100_Month  = txUnpacked[uiCpt]; uiCpt+=1
  uiDO100_Year   = txUnpacked[uiCpt]; uiCpt+=1
  uiDO0_Day      = txUnpacked[uiCpt]; uiCpt+=1
  uiDO0_Month    = txUnpacked[uiCpt]; uiCpt+=1
  uiDO0_Year     = txUnpacked[uiCpt]; uiCpt+=1
  uiEC_Day       = txUnpacked[uiCpt]; uiCpt+=1
  uiEC_Month     = txUnpacked[uiCpt]; uiCpt+=1
  uiEC_Year      = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX1_P1_Day    = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX1_P1_Month  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX1_P1_Year   = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX1_P2_Day    = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX1_P2_Month  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX1_P2_Year   = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX1_P3_Day    = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX1_P3_Month  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX1_P3_Year   = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX2_P1_Day    = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX2_P1_Month  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX2_P1_Year   = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX2_P2_Day    = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX2_P2_Month  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX2_P2_Year   = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX2_P3_Day    = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX2_P3_Month  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX2_P3_Year   = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX3_P1_Day    = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX3_P1_Month  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX3_P1_Year   = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX3_P2_Day    = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX3_P2_Month  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX3_P2_Year   = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX3_P3_Day    = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX3_P3_Month  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX3_P3_Year   = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX4_P1_Day    = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX4_P1_Month  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX4_P1_Year   = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX4_P2_Day    = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX4_P2_Month  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX4_P2_Year   = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX4_P3_Day    = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX4_P3_Month  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX4_P3_Year   = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX5_P1_Day    = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX5_P1_Month  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX5_P1_Year   = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX5_P2_Day    = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX5_P2_Month  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX5_P2_Year   = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX5_P3_Day    = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX5_P3_Month  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX5_P3_Year   = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX6_P1_Day    = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX6_P1_Month  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX6_P1_Year   = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX6_P2_Day    = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX6_P2_Month  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX6_P2_Year   = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX6_P3_Day    = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX6_P3_Month  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX6_P3_Year   = txUnpacked[uiCpt]; uiCpt+=1
  # Assignement
  uiAUX1_Assign  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX2_Assign  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX3_Assign  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX4_Assign  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX5_Assign  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX6_Assign  = txUnpacked[uiCpt]; uiCpt+=1
  sAUX1_Assign   = self.sFGetChannelNameWithID(uiAUX1_Assign)
  sAUX2_Assign   = self.sFGetChannelNameWithID(uiAUX2_Assign)
  sAUX3_Assign   = self.sFGetChannelNameWithID(uiAUX3_Assign)
  sAUX4_Assign   = self.sFGetChannelNameWithID(uiAUX4_Assign)
  sAUX5_Assign   = self.sFGetChannelNameWithID(uiAUX5_Assign)
  sAUX6_Assign   = self.sFGetChannelNameWithID(uiAUX6_Assign)
  # Grab sample factor
  uiAUX1_GS  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX2_GS  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX3_GS  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX4_GS  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX5_GS  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX6_GS  = txUnpacked[uiCpt]; uiCpt+=1
  print("After GS : %d"%uiCpt)
  print("uiAUX1_GS = %d"%uiAUX1_GS)
  print("uiAUX2_GS = %d"%uiAUX2_GS)
  print("uiAUX3_GS = %d"%uiAUX3_GS)
  print("uiAUX4_GS = %d"%uiAUX4_GS)
  print("uiAUX5_GS = %d"%uiAUX5_GS)
  print("uiAUX6_GS = %d"%uiAUX6_GS)
  # Grab sample factor
  uiORP_CalReport      = txUnpacked[uiCpt]; uiCpt+=1
  uiPH7_CalReport      = txUnpacked[uiCpt]; uiCpt+=1
  uiPH4_CalReport      = txUnpacked[uiCpt]; uiCpt+=1
  uiPH10_CalReport     = txUnpacked[uiCpt]; uiCpt+=1
  uiEC_CalReport       = txUnpacked[uiCpt]; uiCpt+=1
  uiDO0_CalReport      = txUnpacked[uiCpt]; uiCpt+=1
  uiDO100_CalReport    = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX1_P1_CalReport  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX1_P2_CalReport  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX1_P3_CalReport  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX2_P1_CalReport  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX2_P2_CalReport  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX2_P3_CalReport  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX3_P1_CalReport  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX3_P2_CalReport  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX3_P3_CalReport  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX4_P1_CalReport  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX4_P2_CalReport  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX4_P3_CalReport  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX5_P1_CalReport  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX5_P2_CalReport  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX5_P3_CalReport  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX6_P1_CalReport  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX6_P2_CalReport  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX6_P3_CalReport  = txUnpacked[uiCpt]; uiCpt+=1
  uiEC_UserCalValue_LSB = txUnpacked[uiCpt]; uiCpt+=1
  uiEC_UserCalValue_MSB = txUnpacked[uiCpt]; uiCpt+=1
  uiEC_UserCalValue_HSB = txUnpacked[uiCpt]; uiCpt+=1
  uiEC_UserCalValue     = ( uiEC_UserCalValue_HSB << 16 ) + ( uiEC_UserCalValue_MSB << 8 ) + uiEC_UserCalValue_LSB
  uiTEMP_CalOffset      = txUnpacked[uiCpt]; uiCpt+=1


  # EC calibration standard
  if( ( uiCal_Param_10 & 0x0F ) == 1 ): sECCalValue = "RapidCal"
  if( ( uiCal_Param_10 & 0x0F) == 2 ):  sECCalValue = "User"
  if( ( uiCal_Param_10 & 0x0F) >= 4 ):  sECCalValue = "SC-35"
  if( ( uiCal_Param_10 & 0x0F) >= 4 ):  bEC_SC35_flag = True
  else:                                 bEC_SC35_flag = False

  print( "( uiCal_Param_10 & 0x0F)   = %u"%( uiCal_Param_10 & 0x0F  ) )
  print( "( uiCal_Param_10 & 0xFFF0) = %u"%( uiCal_Param_10 & 0xFFF0) )

  # Si version >= 5.11
  if( ttConfig["PRODUCT"]["uiPSW"] >= 511 ):
   # Optical averaging constant
   uiOpticalAvg = ( uiCal_Param_10 & 0xFFF0 )
   if( uiOpticalAvg > 192 ): uiOpticalAvg = 192
   if( uiOpticalAvg < 16  ): uiOpticalAvg = 16

  print("=====================")
  print( "uiCal_Param_10 = %u"%uiCal_Param_10 )
  print("=====================")
  # Placement dans l'objet de configuration
  # pH
  ttConfig["SENSOR"]["PH"]["ucPoint"] = 3
  ttConfig["SENSOR"]["PH"]["Point"][0]["sName"]          = tCalibChannelInfo["pH"]["Point"][0]["sName"]
  ttConfig["SENSOR"]["PH"]["Point"][0]["sCalReportUnit"] = tCalibChannelInfo["pH"]["Point"][0]["sCalReportUnit"]
  ttConfig["SENSOR"]["PH"]["Point"][0]["uiDay"]          = uiPH7_Day
  ttConfig["SENSOR"]["PH"]["Point"][0]["uiMonth"]        = uiPH7_Month
  ttConfig["SENSOR"]["PH"]["Point"][0]["uiYear"]         = uiPH7_Year
  ttConfig["SENSOR"]["PH"]["Point"][0]["uiCalReport"]    = ( ( uiPH7_CalReport & 0x7FFF ) / -10 ) if( uiPH7_CalReport & 0x8000 ) else ( uiPH7_CalReport / 10 )
  ttConfig["SENSOR"]["PH"]["Point"][1]["sName"]          = tCalibChannelInfo["pH"]["Point"][1]["sName"]
  ttConfig["SENSOR"]["PH"]["Point"][1]["sCalReportUnit"] = tCalibChannelInfo["pH"]["Point"][1]["sCalReportUnit"]
  ttConfig["SENSOR"]["PH"]["Point"][1]["uiDay"]          = uiPH4_10_Day
  ttConfig["SENSOR"]["PH"]["Point"][1]["uiMonth"]        = uiPH4_10_Month
  ttConfig["SENSOR"]["PH"]["Point"][1]["uiYear"]         = uiPH4_10_Year
  ttConfig["SENSOR"]["PH"]["Point"][1]["uiCalReport"]    = uiPH4_CalReport / 10
  ttConfig["SENSOR"]["PH"]["Point"][2]["sName"]          = tCalibChannelInfo["pH"]["Point"][2]["sName"]
  ttConfig["SENSOR"]["PH"]["Point"][2]["sCalReportUnit"] = tCalibChannelInfo["pH"]["Point"][2]["sCalReportUnit"]
  ttConfig["SENSOR"]["PH"]["Point"][2]["uiDay"]          = uiPH4_10_Day
  ttConfig["SENSOR"]["PH"]["Point"][2]["uiMonth"]        = uiPH4_10_Month
  ttConfig["SENSOR"]["PH"]["Point"][2]["uiYear"]         = uiPH4_10_Year
  ttConfig["SENSOR"]["PH"]["Point"][2]["uiCalReport"]    = uiPH10_CalReport / 10

  # ORP
  ttConfig["SENSOR"]["ORP"]["ucPoint"] = 1
  ttConfig["SENSOR"]["ORP"]["Point"][0]["sName"]          = tCalibChannelInfo["ORP"]["Point"][0]["sName"]
  ttConfig["SENSOR"]["ORP"]["Point"][0]["sCalReportUnit"] = tCalibChannelInfo["ORP"]["Point"][0]["sCalReportUnit"]
  ttConfig["SENSOR"]["ORP"]["Point"][0]["uiDay"]          = uiORP_Day
  ttConfig["SENSOR"]["ORP"]["Point"][0]["uiMonth"]        = ( uiORP_Month & 0x7F )
  ttConfig["SENSOR"]["ORP"]["Point"][0]["uiYear"]         = uiORP_Year
  ttConfig["SENSOR"]["ORP"]["Point"][0]["uiCalReport"]    = ( ( uiORP_CalReport & 0x7FFF ) / -10 ) if(uiORP_CalReport & 0x8000) else (uiORP_CalReport / 10)
  ttConfig["SENSOR"]["ORP"]["Point"][0]["uiCalValueRef"]  = 229 if( ( uiORP_Month & 0x80 ) == 0x80 ) else 250

  # DO
  ttConfig["SENSOR"]["DO"]["ucPoint"] = 2
  ttConfig["SENSOR"]["DO"]["Point"][0]["sName"]          = tCalibChannelInfo["DO"]["Point"][0]["sName"]
  ttConfig["SENSOR"]["DO"]["Point"][0]["sCalReportUnit"] = tCalibChannelInfo["DO"]["Point"][0]["sCalReportUnit"]
  ttConfig["SENSOR"]["DO"]["Point"][0]["uiDay"]          = uiDO0_Day
  ttConfig["SENSOR"]["DO"]["Point"][0]["uiMonth"]        = uiDO0_Month
  ttConfig["SENSOR"]["DO"]["Point"][0]["uiYear"]         = uiDO0_Year
  ttConfig["SENSOR"]["DO"]["Point"][0]["uiCalReport"]    = uiDO0_CalReport / 10
  ttConfig["SENSOR"]["DO"]["Point"][1]["sName"]          = tCalibChannelInfo["DO"]["Point"][1]["sName"]
  ttConfig["SENSOR"]["DO"]["Point"][1]["sCalReportUnit"] = tCalibChannelInfo["DO"]["Point"][1]["sCalReportUnit"]
  ttConfig["SENSOR"]["DO"]["Point"][1]["uiDay"]          = uiDO100_Day
  ttConfig["SENSOR"]["DO"]["Point"][1]["uiMonth"]        = uiDO100_Month
  ttConfig["SENSOR"]["DO"]["Point"][1]["uiYear"]         = uiDO100_Year
  ttConfig["SENSOR"]["DO"]["Point"][1]["uiCalReport"]    = uiDO100_CalReport / 10

  # EC
  ttConfig["SENSOR"]["EC"]["ucPoint"] = 1
  ttConfig["SENSOR"]["EC"]["sCalValue"]      = sECCalValue
  #ttConfig["SENSOR"]["EC"]["uiUserCalValue"] = uiEC_UserCalValue
  ttConfig["SENSOR"]["EC"]["bSC35_flag"]     = bEC_SC35_flag
  ttConfig["SENSOR"]["EC"]["uiUserCalValue"] = uiEC_UserCalValue
  ttConfig["SENSOR"]["EC"]["Point"][0]["sName"]          = tCalibChannelInfo["EC"]["Point"][0]["sName"]
  ttConfig["SENSOR"]["EC"]["Point"][0]["sCalReportUnit"] = tCalibChannelInfo["EC"]["Point"][0]["sCalReportUnit"]
  ttConfig["SENSOR"]["EC"]["Point"][0]["uiDay"]          = uiEC_Day
  ttConfig["SENSOR"]["EC"]["Point"][0]["uiMonth"]        = uiEC_Month
  ttConfig["SENSOR"]["EC"]["Point"][0]["uiYear"]         = uiEC_Year
  ttConfig["SENSOR"]["EC"]["Point"][0]["uiCalReport"]    = uiEC_CalReport / 100
  ttConfig["SENSOR"]["EC"]["Point"][0]["uiCalValueRef"]  = 229 if( ( uiORP_Month & 0x80 ) == 0x80 ) else 250

  # AUX1
  if( sAUX1_Assign != "EMPTY" ):
   ttConfig["SENSOR"]["AUX1"]["ucPoint"] = tCalibChannelInfo[sAUX1_Assign]["ucPoint"]
   ttConfig["SENSOR"]["AUX1"]["Point"][0]["sName"]          = tCalibChannelInfo[sAUX1_Assign]["Point"][0]["sName"]
   ttConfig["SENSOR"]["AUX1"]["Point"][0]["sCalReportUnit"] = tCalibChannelInfo[sAUX1_Assign]["Point"][0]["sCalReportUnit"]
   ttConfig["SENSOR"]["AUX1"]["Point"][0]["uiDay"]          = uiAUX1_P1_Day
   ttConfig["SENSOR"]["AUX1"]["Point"][0]["uiMonth"]        = uiAUX1_P1_Month
   ttConfig["SENSOR"]["AUX1"]["Point"][0]["uiYear"]         = uiAUX1_P1_Year
   ttConfig["SENSOR"]["AUX1"]["Point"][0]["uiCalReport"]    = ( ( uiAUX1_P1_CalReport & 0x7FFF ) * -1 ) if(uiAUX1_P1_CalReport & 0x8000) else uiAUX1_P1_CalReport
   if( tCalibChannelInfo[sAUX1_Assign]["ucPoint"] > 1 ):
    ttConfig["SENSOR"]["AUX1"]["Point"][1]["sName"]          = tCalibChannelInfo[sAUX1_Assign]["Point"][1]["sName"]
    ttConfig["SENSOR"]["AUX1"]["Point"][1]["sCalReportUnit"] = tCalibChannelInfo[sAUX1_Assign]["Point"][1]["sCalReportUnit"]
    ttConfig["SENSOR"]["AUX1"]["Point"][1]["uiDay"]          = uiAUX1_P2_Day
    ttConfig["SENSOR"]["AUX1"]["Point"][1]["uiMonth"]        = uiAUX1_P2_Month
    ttConfig["SENSOR"]["AUX1"]["Point"][1]["uiYear"]         = uiAUX1_P2_Year
    ttConfig["SENSOR"]["AUX1"]["Point"][1]["uiCalReport"]    = ( ( uiAUX1_P2_CalReport & 0x7FFF ) * -1 ) if(uiAUX1_P2_CalReport & 0x8000) else uiAUX1_P2_CalReport
   if( tCalibChannelInfo[sAUX1_Assign]["ucPoint"] > 2 ):
    ttConfig["SENSOR"]["AUX1"]["Point"][2]["sName"]          = tCalibChannelInfo[sAUX1_Assign]["Point"][2]["sName"]
    ttConfig["SENSOR"]["AUX1"]["Point"][2]["sCalReportUnit"] = tCalibChannelInfo[sAUX1_Assign]["Point"][2]["sCalReportUnit"]
    ttConfig["SENSOR"]["AUX1"]["Point"][2]["uiDay"]          = uiAUX1_P3_Day
    ttConfig["SENSOR"]["AUX1"]["Point"][2]["uiMonth"]        = uiAUX1_P3_Month
    ttConfig["SENSOR"]["AUX1"]["Point"][2]["uiYear"]         = uiAUX1_P3_Year
    ttConfig["SENSOR"]["AUX1"]["Point"][2]["uiCalReport"]    = ( ( uiAUX1_P3_CalReport & 0x7FFF ) * -1 ) if(uiAUX1_P3_CalReport & 0x8000) else uiAUX1_P3_CalReport
  # GS
  ttConfig["SENSOR"]["AUX1"]["fGS"]        = uiAUX1_GS / 100

  # AUX2
  if( sAUX2_Assign != "EMPTY" ):
   ttConfig["SENSOR"]["AUX2"]["ucPoint"] = tCalibChannelInfo[sAUX2_Assign]["ucPoint"]
   ttConfig["SENSOR"]["AUX2"]["Point"][0]["sName"]          = tCalibChannelInfo[sAUX2_Assign]["Point"][0]["sName"]
   ttConfig["SENSOR"]["AUX2"]["Point"][0]["sCalReportUnit"] = tCalibChannelInfo[sAUX2_Assign]["Point"][0]["sCalReportUnit"]
   ttConfig["SENSOR"]["AUX2"]["Point"][0]["uiDay"]          = uiAUX2_P1_Day
   ttConfig["SENSOR"]["AUX2"]["Point"][0]["uiMonth"]        = uiAUX2_P1_Month
   ttConfig["SENSOR"]["AUX2"]["Point"][0]["uiYear"]         = uiAUX2_P1_Year
   ttConfig["SENSOR"]["AUX2"]["Point"][0]["uiCalReport"]    = ( ( uiAUX2_P1_CalReport & 0x7FFF ) * -1 ) if(uiAUX2_P1_CalReport & 0x8000) else uiAUX2_P1_CalReport
   if( tCalibChannelInfo[sAUX2_Assign]["ucPoint"] > 1 ):
    ttConfig["SENSOR"]["AUX2"]["Point"][1]["sName"]          = tCalibChannelInfo[sAUX2_Assign]["Point"][1]["sName"]
    ttConfig["SENSOR"]["AUX2"]["Point"][1]["sCalReportUnit"] = tCalibChannelInfo[sAUX2_Assign]["Point"][1]["sCalReportUnit"]
    ttConfig["SENSOR"]["AUX2"]["Point"][1]["uiDay"]          = uiAUX2_P2_Day
    ttConfig["SENSOR"]["AUX2"]["Point"][1]["uiMonth"]        = uiAUX2_P2_Month
    ttConfig["SENSOR"]["AUX2"]["Point"][1]["uiYear"]         = uiAUX2_P2_Year
    ttConfig["SENSOR"]["AUX2"]["Point"][1]["uiCalReport"]    = ( ( uiAUX2_P2_CalReport & 0x7FFF ) * -1 ) if(uiAUX2_P2_CalReport & 0x8000) else uiAUX2_P2_CalReport
   if( tCalibChannelInfo[sAUX2_Assign]["ucPoint"] > 2 ):
    ttConfig["SENSOR"]["AUX2"]["Point"][2]["sName"]          = tCalibChannelInfo[sAUX2_Assign]["Point"][2]["sName"]
    ttConfig["SENSOR"]["AUX2"]["Point"][2]["sCalReportUnit"] = tCalibChannelInfo[sAUX2_Assign]["Point"][2]["sCalReportUnit"]
    ttConfig["SENSOR"]["AUX2"]["Point"][2]["uiDay"]          = uiAUX2_P3_Day
    ttConfig["SENSOR"]["AUX2"]["Point"][2]["uiMonth"]        = uiAUX2_P3_Month
    ttConfig["SENSOR"]["AUX2"]["Point"][2]["uiYear"]         = uiAUX2_P3_Year
    ttConfig["SENSOR"]["AUX2"]["Point"][2]["uiCalReport"]    = ( ( uiAUX2_P3_CalReport & 0x7FFF ) * -1 ) if(uiAUX2_P3_CalReport & 0x8000) else uiAUX2_P3_CalReport
  # GS
  ttConfig["SENSOR"]["AUX2"]["fGS"]   = uiAUX2_GS / 100

  # AUX3
  if( sAUX3_Assign != "EMPTY" ):
   ttConfig["SENSOR"]["AUX3"]["ucPoint"] = tCalibChannelInfo[sAUX3_Assign]["ucPoint"]
   ttConfig["SENSOR"]["AUX3"]["Point"][0]["sName"]          = tCalibChannelInfo[sAUX3_Assign]["Point"][0]["sName"]
   ttConfig["SENSOR"]["AUX3"]["Point"][0]["sCalReportUnit"] = tCalibChannelInfo[sAUX3_Assign]["Point"][0]["sCalReportUnit"]
   ttConfig["SENSOR"]["AUX3"]["Point"][0]["uiDay"]          = uiAUX3_P1_Day
   ttConfig["SENSOR"]["AUX3"]["Point"][0]["uiMonth"]        = uiAUX3_P1_Month
   ttConfig["SENSOR"]["AUX3"]["Point"][0]["uiYear"]         = uiAUX3_P1_Year
   ttConfig["SENSOR"]["AUX3"]["Point"][0]["uiCalReport"]    = ( ( uiAUX3_P1_CalReport & 0x7FFF ) * -1 ) if(uiAUX3_P1_CalReport & 0x8000) else uiAUX3_P1_CalReport
   if( tCalibChannelInfo[sAUX3_Assign]["ucPoint"] > 1 ):
    ttConfig["SENSOR"]["AUX3"]["Point"][1]["sName"]          = tCalibChannelInfo[sAUX3_Assign]["Point"][1]["sName"]
    ttConfig["SENSOR"]["AUX3"]["Point"][1]["sCalReportUnit"] = tCalibChannelInfo[sAUX3_Assign]["Point"][1]["sCalReportUnit"]
    ttConfig["SENSOR"]["AUX3"]["Point"][1]["uiDay"]          = uiAUX3_P2_Day
    ttConfig["SENSOR"]["AUX3"]["Point"][1]["uiMonth"]        = uiAUX3_P2_Month
    ttConfig["SENSOR"]["AUX3"]["Point"][1]["uiYear"]         = uiAUX3_P2_Year
    ttConfig["SENSOR"]["AUX3"]["Point"][1]["uiCalReport"]    = ( ( uiAUX3_P2_CalReport & 0x7FFF ) * -1 ) if(uiAUX3_P2_CalReport & 0x8000) else uiAUX3_P2_CalReport
   if( tCalibChannelInfo[sAUX3_Assign]["ucPoint"] > 2 ):
    ttConfig["SENSOR"]["AUX3"]["Point"][2]["sName"]          = tCalibChannelInfo[sAUX3_Assign]["Point"][2]["sName"]
    ttConfig["SENSOR"]["AUX3"]["Point"][2]["sCalReportUnit"] = tCalibChannelInfo[sAUX3_Assign]["Point"][2]["sCalReportUnit"]
    ttConfig["SENSOR"]["AUX3"]["Point"][2]["uiDay"]          = uiAUX3_P3_Day
    ttConfig["SENSOR"]["AUX3"]["Point"][2]["uiMonth"]        = uiAUX3_P3_Month
    ttConfig["SENSOR"]["AUX3"]["Point"][2]["uiYear"]         = uiAUX3_P3_Year
    ttConfig["SENSOR"]["AUX3"]["Point"][2]["uiCalReport"]    = ( ( uiAUX3_P3_CalReport & 0x7FFF ) * -1 ) if(uiAUX3_P3_CalReport & 0x8000) else uiAUX3_P3_CalReport
  # GS
  ttConfig["SENSOR"]["AUX3"]["fGS"]   = uiAUX3_GS / 100

  # AUX4
  if( sAUX4_Assign != "EMPTY" ):
   ttConfig["SENSOR"]["AUX4"]["ucPoint"] = tCalibChannelInfo[sAUX4_Assign]["ucPoint"]
   ttConfig["SENSOR"]["AUX4"]["Point"][0]["sName"]          = tCalibChannelInfo[sAUX4_Assign]["Point"][0]["sName"]
   ttConfig["SENSOR"]["AUX4"]["Point"][0]["sCalReportUnit"] = tCalibChannelInfo[sAUX4_Assign]["Point"][0]["sCalReportUnit"]
   ttConfig["SENSOR"]["AUX4"]["Point"][0]["uiDay"]          = uiAUX4_P1_Day
   ttConfig["SENSOR"]["AUX4"]["Point"][0]["uiMonth"]        = uiAUX4_P1_Month
   ttConfig["SENSOR"]["AUX4"]["Point"][0]["uiYear"]         = uiAUX4_P1_Year
   ttConfig["SENSOR"]["AUX4"]["Point"][0]["uiCalReport"]    = uiAUX4_P1_CalReport
   ttConfig["SENSOR"]["AUX4"]["Point"][0]["uiCalReport"]    = ( ( uiAUX4_P1_CalReport & 0x7FFF ) * -1 ) if(uiAUX4_P1_CalReport & 0x8000) else uiAUX4_P1_CalReport
   if( tCalibChannelInfo[sAUX4_Assign]["ucPoint"] > 1 ):
    ttConfig["SENSOR"]["AUX4"]["Point"][1]["sName"]          = tCalibChannelInfo[sAUX4_Assign]["Point"][1]["sName"]
    ttConfig["SENSOR"]["AUX4"]["Point"][1]["sCalReportUnit"] = tCalibChannelInfo[sAUX4_Assign]["Point"][1]["sCalReportUnit"]
    ttConfig["SENSOR"]["AUX4"]["Point"][1]["uiDay"]          = uiAUX4_P2_Day
    ttConfig["SENSOR"]["AUX4"]["Point"][1]["uiMonth"]        = uiAUX4_P2_Month
    ttConfig["SENSOR"]["AUX4"]["Point"][1]["uiYear"]         = uiAUX4_P2_Year
    ttConfig["SENSOR"]["AUX4"]["Point"][1]["uiCalReport"]    = ( ( uiAUX4_P2_CalReport & 0x7FFF ) * -1 ) if(uiAUX4_P2_CalReport & 0x8000) else uiAUX4_P2_CalReport
   if( tCalibChannelInfo[sAUX4_Assign]["ucPoint"] > 2 ):
    ttConfig["SENSOR"]["AUX4"]["Point"][2]["sName"]          = tCalibChannelInfo[sAUX4_Assign]["Point"][2]["sName"]
    ttConfig["SENSOR"]["AUX4"]["Point"][2]["sCalReportUnit"] = tCalibChannelInfo[sAUX4_Assign]["Point"][2]["sCalReportUnit"]
    ttConfig["SENSOR"]["AUX4"]["Point"][2]["uiDay"]          = uiAUX4_P3_Day
    ttConfig["SENSOR"]["AUX4"]["Point"][2]["uiMonth"]        = uiAUX4_P3_Month
    ttConfig["SENSOR"]["AUX4"]["Point"][2]["uiYear"]         = uiAUX4_P3_Year
    ttConfig["SENSOR"]["AUX4"]["Point"][2]["uiCalReport"]    = ( ( uiAUX4_P3_CalReport & 0x7FFF ) * -1 ) if(uiAUX4_P3_CalReport & 0x8000) else uiAUX4_P3_CalReport
  # GS
  ttConfig["SENSOR"]["AUX4"]["fGS"]   = uiAUX4_GS / 100

  # AUX5
  if( sAUX5_Assign != "EMPTY" ):
   ttConfig["SENSOR"]["AUX5"]["ucPoint"] = tCalibChannelInfo[sAUX5_Assign]["ucPoint"]
   ttConfig["SENSOR"]["AUX5"]["Point"][0]["sName"]          = tCalibChannelInfo[sAUX5_Assign]["Point"][0]["sName"]
   ttConfig["SENSOR"]["AUX5"]["Point"][0]["sCalReportUnit"] = tCalibChannelInfo[sAUX5_Assign]["Point"][0]["sCalReportUnit"]
   ttConfig["SENSOR"]["AUX5"]["Point"][0]["uiDay"]          = uiAUX5_P1_Day
   ttConfig["SENSOR"]["AUX5"]["Point"][0]["uiMonth"]        = uiAUX5_P1_Month
   ttConfig["SENSOR"]["AUX5"]["Point"][0]["uiYear"]         = uiAUX5_P1_Year
   ttConfig["SENSOR"]["AUX5"]["Point"][0]["uiCalReport"]    = ( ( uiAUX5_P1_CalReport & 0x7FFF ) * -1 ) if(uiAUX5_P1_CalReport & 0x8000) else uiAUX5_P1_CalReport
   if( tCalibChannelInfo[sAUX5_Assign]["ucPoint"] > 1 ):
    ttConfig["SENSOR"]["AUX5"]["Point"][1]["sName"]          = tCalibChannelInfo[sAUX5_Assign]["Point"][1]["sName"]
    ttConfig["SENSOR"]["AUX5"]["Point"][1]["sCalReportUnit"] = tCalibChannelInfo[sAUX5_Assign]["Point"][1]["sCalReportUnit"]
    ttConfig["SENSOR"]["AUX5"]["Point"][1]["uiDay"]          = uiAUX5_P2_Day
    ttConfig["SENSOR"]["AUX5"]["Point"][1]["uiMonth"]        = uiAUX5_P2_Month
    ttConfig["SENSOR"]["AUX5"]["Point"][1]["uiYear"]         = uiAUX5_P2_Year
    ttConfig["SENSOR"]["AUX5"]["Point"][1]["uiCalReport"]    = uiAUX5_P2_CalReport
    ttConfig["SENSOR"]["AUX5"]["Point"][1]["uiCalReport"]    = ( ( uiAUX5_P2_CalReport & 0x7FFF ) * -1 ) if(uiAUX5_P2_CalReport & 0x8000) else uiAUX5_P2_CalReport
   if( tCalibChannelInfo[sAUX5_Assign]["ucPoint"] > 2 ):
    ttConfig["SENSOR"]["AUX5"]["Point"][2]["sName"]          = tCalibChannelInfo[sAUX5_Assign]["Point"][2]["sName"]
    ttConfig["SENSOR"]["AUX5"]["Point"][2]["sCalReportUnit"] = tCalibChannelInfo[sAUX5_Assign]["Point"][2]["sCalReportUnit"]
    ttConfig["SENSOR"]["AUX5"]["Point"][2]["uiDay"]          = uiAUX5_P3_Day
    ttConfig["SENSOR"]["AUX5"]["Point"][2]["uiMonth"]        = uiAUX5_P3_Month
    ttConfig["SENSOR"]["AUX5"]["Point"][2]["uiYear"]         = uiAUX5_P3_Year
    ttConfig["SENSOR"]["AUX5"]["Point"][2]["uiCalReport"]    = uiAUX5_P3_CalReport
    ttConfig["SENSOR"]["AUX5"]["Point"][2]["uiCalReport"]    = ( ( uiAUX5_P3_CalReport & 0x7FFF ) * -1 ) if(uiAUX5_P3_CalReport & 0x8000) else uiAUX5_P3_CalReport
  # GS
  ttConfig["SENSOR"]["AUX5"]["fGS"]   = uiAUX5_GS / 100

  # AUX6
  if( sAUX6_Assign != "EMPTY" ):
   ttConfig["SENSOR"]["AUX6"]["ucPoint"] = tCalibChannelInfo[sAUX6_Assign]["ucPoint"]
   ttConfig["SENSOR"]["AUX6"]["Point"][0]["sName"]          = tCalibChannelInfo[sAUX6_Assign]["Point"][0]["sName"]
   ttConfig["SENSOR"]["AUX6"]["Point"][0]["sCalReportUnit"] = tCalibChannelInfo[sAUX6_Assign]["Point"][0]["sCalReportUnit"]
   ttConfig["SENSOR"]["AUX6"]["Point"][0]["uiDay"]          = uiAUX6_P1_Day
   ttConfig["SENSOR"]["AUX6"]["Point"][0]["uiMonth"]        = uiAUX6_P1_Month
   ttConfig["SENSOR"]["AUX6"]["Point"][0]["uiYear"]         = uiAUX6_P1_Year
   ttConfig["SENSOR"]["AUX6"]["Point"][0]["uiCalReport"]    = uiAUX6_P1_CalReport
   ttConfig["SENSOR"]["AUX6"]["Point"][0]["uiCalReport"]    = ( ( uiAUX6_P1_CalReport & 0x7FFF ) * -1 ) if(uiAUX6_P1_CalReport & 0x8000) else uiAUX6_P1_CalReport
   if( tCalibChannelInfo[sAUX6_Assign]["ucPoint"] > 1 ):
    ttConfig["SENSOR"]["AUX6"]["Point"][1]["sName"]          = tCalibChannelInfo[sAUX6_Assign]["Point"][1]["sName"]
    ttConfig["SENSOR"]["AUX6"]["Point"][1]["sCalReportUnit"] = tCalibChannelInfo[sAUX6_Assign]["Point"][1]["sCalReportUnit"]
    ttConfig["SENSOR"]["AUX6"]["Point"][1]["uiDay"]          = uiAUX6_P2_Day
    ttConfig["SENSOR"]["AUX6"]["Point"][1]["uiMonth"]        = uiAUX6_P2_Month
    ttConfig["SENSOR"]["AUX6"]["Point"][1]["uiYear"]         = uiAUX6_P2_Year
    ttConfig["SENSOR"]["AUX6"]["Point"][1]["uiCalReport"]    = uiAUX6_P2_CalReport
    ttConfig["SENSOR"]["AUX6"]["Point"][1]["uiCalReport"]    = ( ( uiAUX6_P2_CalReport & 0x7FFF ) * -1 ) if(uiAUX6_P2_CalReport & 0x8000) else uiAUX6_P2_CalReport
   if( tCalibChannelInfo[sAUX6_Assign]["ucPoint"] > 2 ):
    ttConfig["SENSOR"]["AUX6"]["Point"][2]["sName"]          = tCalibChannelInfo[sAUX6_Assign]["Point"][2]["sName"]
    ttConfig["SENSOR"]["AUX6"]["Point"][2]["sCalReportUnit"] = tCalibChannelInfo[sAUX6_Assign]["Point"][2]["sCalReportUnit"]
    ttConfig["SENSOR"]["AUX6"]["Point"][2]["uiDay"]          = uiAUX6_P3_Day
    ttConfig["SENSOR"]["AUX6"]["Point"][2]["uiMonth"]        = uiAUX6_P3_Month
    ttConfig["SENSOR"]["AUX6"]["Point"][2]["uiYear"]         = uiAUX6_P3_Year
    ttConfig["SENSOR"]["AUX6"]["Point"][2]["uiCalReport"]    = uiAUX6_P3_CalReport
    ttConfig["SENSOR"]["AUX6"]["Point"][2]["uiCalReport"]    = ( ( uiAUX6_P3_CalReport & 0x7FFF ) * -1 ) if(uiAUX6_P3_CalReport & 0x8000) else uiAUX6_P3_CalReport
  # GS
  ttConfig["SENSOR"]["AUX6"]["fGS"]   = uiAUX6_GS / 100

  # Offset en température
  ttConfig["SENSOR"]["TEMP"]["uiTEMP_CalOffset"] = uiTEMP_CalOffset
  # Si version >= 5.11
  if( ttConfig["PRODUCT"]["uiPSW"] >= 511 ):
   # Optical averaging constant
   ttConfig["PRODUCT"]["uiOpticalAvg"] = uiOpticalAvg

  # Retour de la config
  return( ttConfig )

 #--------------------------
 # Extraction des champs direct access mode
 #--------------------------
 def ttFParseDirectAccessMode( self, sDataRead, ttConfig ):
  print("-- ttFParseDirectAccessMode --")
  print(sDataRead)
  #print(sDataRead.hex())
  # Decryptage de la donnée binaire
  txUnpacked = struct.unpack( '>2B1H', sDataRead )
  print(txUnpacked)
  uiCpt = 0
  # Extraction des champs
  uiCHK        = txUnpacked[uiCpt]; uiCpt+=1
  uiCMD        = txUnpacked[uiCpt]; uiCpt+=1
  uiBaro       = txUnpacked[uiCpt]; uiCpt+=1
  print("uiCHK   = %d" % uiCHK)
  print("uiCMD   = %d" % uiCMD)
  print("uiBaro  = %d" % uiBaro)
  # Placement dans l'objet de configuration
  ttConfig["SENSOR"]["Baro"]["fResult"] = float(uiBaro)
  # Retour de la config
  return( { uiCHK, uiCMD } )

 #--------------------------
 # Extraction des champs Measurement data
 #--------------------------
 def ttFParseMeasurementData( self, sDataRead, ttConfig  ):
  # Decryptage de la donnée binaire
  txUnpacked = struct.unpack( '>39B', sDataRead )
  print(txUnpacked)
  uiCpt = 0
  # Extraction des champs
  uiEC_HSB    = txUnpacked[uiCpt]; uiCpt+=1 #  0 - EC_HSB - Flag bit 7
  uiTEMP_LSB  = txUnpacked[uiCpt]; uiCpt+=1 #  1 - TEMP_LSB
  uiEC_MSB    = txUnpacked[uiCpt]; uiCpt+=1 #  2 - EC_MSB
  uiPH_MSB    = txUnpacked[uiCpt]; uiCpt+=1 #  3 - PH_MSB - Flag bit 6 et 7
  uiPHmv_LSB  = txUnpacked[uiCpt]; uiCpt+=1 #  4 - MV_LSB
  uiDO_LSB    = txUnpacked[uiCpt]; uiCpt+=1 #  5 - DO_LSB
  uiTEMP_MSB  = txUnpacked[uiCpt]; uiCpt+=1 #  6 - TEMP_MSB - Flag bit 7
  uiEC_LSB    = txUnpacked[uiCpt]; uiCpt+=1 #  7 - EC_LSB
  uiDO_MSB    = txUnpacked[uiCpt]; uiCpt+=1 #  8 - DO_MSB - Flag bit 7
  uiPH_LSB    = txUnpacked[uiCpt]; uiCpt+=1 #  9 - PH_LSB
  uiPHmv_MSB  = txUnpacked[uiCpt]; uiCpt+=1 # 10 - MV_MSB - Flag bit 7
  uiDOsat_LSB = txUnpacked[uiCpt]; uiCpt+=1 # 11 - DO_PC_LSB
  uiDOsat_MSB = txUnpacked[uiCpt]; uiCpt+=1 # 12 - DO_PC_MSB
  uiORP_MSB   = txUnpacked[uiCpt]; uiCpt+=1 # 13 - ORP_MSB
  uiORP_LSB   = txUnpacked[uiCpt]; uiCpt+=1 # 14 - ORP_LSB
  uiDepth_MSB = txUnpacked[uiCpt]; uiCpt+=1 # 15 - DEPTH_MSB
  uiDepth_LSB = txUnpacked[uiCpt]; uiCpt+=1 # 16 - DEPTH_LSB
  uiAUX1_HSB  = txUnpacked[uiCpt]; uiCpt+=1 # 17 - AUX1_HSB - Bits 3 - 7
  uiAUX1_MSB  = txUnpacked[uiCpt]; uiCpt+=1 # 18 - AUX1_MSB
  uiAUX1_LSB  = txUnpacked[uiCpt]; uiCpt+=1 # 19 - AUX1_LSB
  uiAUX2_HSB  = txUnpacked[uiCpt]; uiCpt+=1 # 20 - AUX2_HSB - Bits 3 - 7
  uiAUX2_MSB  = txUnpacked[uiCpt]; uiCpt+=1 # 21 - AUX2_MSB
  uiAUX2_LSB  = txUnpacked[uiCpt]; uiCpt+=1 # 22 - AUX2_LSB
  uiAUX3_HSB  = txUnpacked[uiCpt]; uiCpt+=1 # 23 - AUX3_HSB - Bits 3 - 7
  uiAUX3_MSB  = txUnpacked[uiCpt]; uiCpt+=1 # 24 - AUX3_HSB
  uiAUX3_LSB  = txUnpacked[uiCpt]; uiCpt+=1 # 25 - AUX3_HSB
  uiAUX4_HSB  = txUnpacked[uiCpt]; uiCpt+=1 # 26 - AUX4_HSB - Bits 3 - 7
  uiAUX4_MSB  = txUnpacked[uiCpt]; uiCpt+=1 # 27 - AUX4_MSB
  uiAUX4_LSB  = txUnpacked[uiCpt]; uiCpt+=1 # 28 - AUX4_LSB
  uiAUX5_HSB  = txUnpacked[uiCpt]; uiCpt+=1 # 29 - AUX5_HSB - Bits 3 - 7
  uiAUX5_MSB  = txUnpacked[uiCpt]; uiCpt+=1 # 30 - AUX5_MSB
  uiAUX5_LSB  = txUnpacked[uiCpt]; uiCpt+=1 # 31 - AUX5_LSB
  uiAUX6_HSB  = txUnpacked[uiCpt]; uiCpt+=1 # 32 - AUX6_HSB - Bits 3 - 7
  uiAUX6_MSB  = txUnpacked[uiCpt]; uiCpt+=1 # 33 - AUX6_MSB
  uiAUX6_LSB  = txUnpacked[uiCpt]; uiCpt+=1 # 34 - AUX6_LSB
  uiAUX7_HSB  = txUnpacked[uiCpt]; uiCpt+=1 # 35 - AUX7_HSB - Bits 3 - 7
  uiAUX7_MSB  = txUnpacked[uiCpt]; uiCpt+=1 # 36 - AUX7_MSB
  uiAUX7_LSB  = txUnpacked[uiCpt]; uiCpt+=1 # 37 - AUX7_LSB
  uiCRC       = txUnpacked[uiCpt]; uiCpt+=1 # 38 - CRC

  uiTEMP  = ( ( uiTEMP_MSB  & 0x7F ) << 8  ) + uiTEMP_LSB
  uiEC    = ( ( uiEC_HSB    & 0x7F ) << 16 ) + ( uiEC_MSB << 8 ) + uiEC_LSB
  uiDO    = ( ( uiDO_MSB    & 0x7F ) << 8  ) + uiDO_LSB
  uiDOsat = ( ( uiDOsat_MSB & 0x7F ) << 8  ) + uiDOsat_LSB
  uiPH    = ( ( uiPH_MSB    & 0x3F ) << 8  ) + uiPH_LSB
  uiPHmv  = ( ( uiPHmv_MSB  & 0x7F ) << 8  ) + uiPHmv_LSB
  uiORP   = ( ( uiORP_MSB   & 0x7F ) << 8  ) + uiORP_LSB
  uiDepth = ( ( uiDepth_MSB & 0x7F ) << 8  ) + uiDepth_LSB
  uiAUX1  = ( ( uiAUX1_HSB  & 0x07 ) << 16 ) + ( uiAUX1_MSB << 8 ) + uiAUX1_LSB
  uiAUX2  = ( ( uiAUX2_HSB  & 0x07 ) << 16 ) + ( uiAUX2_MSB << 8 ) + uiAUX2_LSB
  uiAUX3  = ( ( uiAUX3_HSB  & 0x07 ) << 16 ) + ( uiAUX3_MSB << 8 ) + uiAUX3_LSB
  uiAUX4  = ( ( uiAUX4_HSB  & 0x07 ) << 16 ) + ( uiAUX4_MSB << 8 ) + uiAUX4_LSB
  uiAUX5  = ( ( uiAUX5_HSB  & 0x07 ) << 16 ) + ( uiAUX5_MSB << 8 ) + uiAUX5_LSB
  uiAUX6  = ( ( uiAUX6_HSB  & 0x07 ) << 16 ) + ( uiAUX6_MSB << 8 ) + uiAUX6_LSB
  uiAUX7  = ( ( uiAUX7_HSB  & 0x07 ) << 16 ) + ( uiAUX7_MSB << 8 ) + uiAUX7_LSB

  print("uiTEMP  = %d" % uiTEMP)
  print("uiEC    = %d" % uiEC)
  print("uiDO    = %d" % uiDO)
  print("uiDOsat = %d" % uiDOsat)
  print("uiPH    = %d" % uiPH)
  print("uiPHmv  = %d" % uiPHmv)
  print("uiORP   = %d" % uiORP)
  print("uiDepth = %d" % uiDepth)

  uiTEMP = ( -uiTEMP ) if( uiTEMP_MSB & 0x80 ) else uiTEMP
  fTEMP  = float( uiTEMP  ) / 100
  fEC    = float( uiEC    )
  fDO    = float( uiDO    ) / 100
  fDOsat = float( uiDOsat ) / 10
  fPH    = float( uiPH    ) / 100
  uiPHmv = ( -uiPHmv ) if( uiPHmv_MSB & 0x80 ) else uiPHmv
  fPHmv  = float( uiPHmv  ) / 10
  uiORP  = ( -uiORP ) if( uiORP_MSB & 0x80 ) else uiORP
  fORP   = float( uiORP   ) / 10
  fDepth = float( uiDepth )

  fBaro = ttConfig["SENSOR"]["Baro"]["fResult"]

  Den_R0 = 3.9863
  Den_R1 = 288.9414
  Den_R2 = 68.12963
  Den_R3 = 508.9292
  fDensity = 1000.0 - (fTEMP - Den_R0) ** 2 * (fTEMP + Den_R1) / (fTEMP + Den_R2) / Den_R3

  if( fEC == 0 ): fDepthOffset = fDepth - fBaro
  else:           fDepthOffset = 0

  fDepth = (((fDepth - fDepthOffset) - fBaro) * 100) / (9.81 * fDensity)

  uiAUX1  = ( -uiAUX1 ) if( uiAUX1_HSB & 0x08 ) else uiAUX1
  uiAUX2  = ( -uiAUX2 ) if( uiAUX2_HSB & 0x08 ) else uiAUX2
  uiAUX3  = ( -uiAUX3 ) if( uiAUX3_HSB & 0x08 ) else uiAUX3
  uiAUX4  = ( -uiAUX4 ) if( uiAUX4_HSB & 0x08 ) else uiAUX4
  uiAUX5  = ( -uiAUX5 ) if( uiAUX5_HSB & 0x08 ) else uiAUX5
  uiAUX6  = ( -uiAUX6 ) if( uiAUX6_HSB & 0x08 ) else uiAUX6
  uiAUX7  = ( -uiAUX7 ) if( uiAUX7_HSB & 0x08 ) else uiAUX7
  # AUX1 decimal
  if( ( uiAUX1_HSB & 0x30 ) == 0x00 ): fAUX1 = float( uiAUX1 ) / 1
  if( ( uiAUX1_HSB & 0x30 ) == 0x10 ): fAUX1 = float( uiAUX1 ) / 10
  if( ( uiAUX1_HSB & 0x30 ) == 0x20 ): fAUX1 = float( uiAUX1 ) / 100
  if( ( uiAUX1_HSB & 0x30 ) == 0x30 ): fAUX1 = float( uiAUX1 ) / 1000
  # AUX2 decimal
  if( ( uiAUX2_HSB & 0x30 ) == 0x00 ): fAUX2 = float( uiAUX2 ) / 1
  if( ( uiAUX2_HSB & 0x30 ) == 0x10 ): fAUX2 = float( uiAUX2 ) / 10
  if( ( uiAUX2_HSB & 0x30 ) == 0x20 ): fAUX2 = float( uiAUX2 ) / 100
  if( ( uiAUX2_HSB & 0x30 ) == 0x30 ): fAUX2 = float( uiAUX2 ) / 1000
  # AUX3 decimal
  if( ( uiAUX3_HSB & 0x30 ) == 0x00 ): fAUX3 = float( uiAUX3 ) / 1
  if( ( uiAUX3_HSB & 0x30 ) == 0x10 ): fAUX3 = float( uiAUX3 ) / 10
  if( ( uiAUX3_HSB & 0x30 ) == 0x20 ): fAUX3 = float( uiAUX3 ) / 100
  if( ( uiAUX3_HSB & 0x30 ) == 0x30 ): fAUX3 = float( uiAUX3 ) / 1000
  # AUX4 decimal
  if( ( uiAUX4_HSB & 0x30 ) == 0x00 ): fAUX4 = float( uiAUX4 ) / 1
  if( ( uiAUX4_HSB & 0x30 ) == 0x10 ): fAUX4 = float( uiAUX4 ) / 10
  if( ( uiAUX4_HSB & 0x30 ) == 0x20 ): fAUX4 = float( uiAUX4 ) / 100
  if( ( uiAUX4_HSB & 0x30 ) == 0x30 ): fAUX4 = float( uiAUX4 ) / 1000
  # AUX5 decimal
  if( ( uiAUX5_HSB & 0x30 ) == 0x00 ): fAUX5 = float( uiAUX5 ) / 1
  if( ( uiAUX5_HSB & 0x30 ) == 0x10 ): fAUX5 = float( uiAUX5 ) / 10
  if( ( uiAUX5_HSB & 0x30 ) == 0x20 ): fAUX5 = float( uiAUX5 ) / 100
  if( ( uiAUX5_HSB & 0x30 ) == 0x30 ): fAUX5 = float( uiAUX5 ) / 1000
  # AUX6 decimal
  if( ( uiAUX6_HSB & 0x30 ) == 0x00 ): fAUX6 = float( uiAUX6 ) / 1
  if( ( uiAUX6_HSB & 0x30 ) == 0x10 ): fAUX6 = float( uiAUX6 ) / 10
  if( ( uiAUX6_HSB & 0x30 ) == 0x20 ): fAUX6 = float( uiAUX6 ) / 100
  if( ( uiAUX6_HSB & 0x30 ) == 0x30 ): fAUX6 = float( uiAUX6 ) / 1000
  # AUX7 decimal
  if( ( uiAUX7_HSB & 0x30 ) == 0x00 ): fAUX7 = float( uiAUX7 ) / 1
  if( ( uiAUX7_HSB & 0x30 ) == 0x10 ): fAUX7 = float( uiAUX7 ) / 10
  if( ( uiAUX7_HSB & 0x30 ) == 0x20 ): fAUX7 = float( uiAUX7 ) / 100
  if( ( uiAUX7_HSB & 0x30 ) == 0x30 ): fAUX7 = float( uiAUX7 ) / 1000

  print("fTEMP  = %f" % fTEMP)
  print("fEC    = %f" % fEC)
  print("fDO    = %f" % fDO)
  print("fDOsat = %f" % fDOsat)
  print("fPH    = %f" % fPH)
  print("fPHmv  = %f" % fPHmv)
  print("fORP   = %f" % fORP)
  print("fDepth = %f" % fDepth)


  ttConfig["SENSOR"]["TEMP"]["fResult"]   = fTEMP
  ttConfig["SENSOR"]["EC"]["fResult"]     = fEC
  ttConfig["SENSOR"]["DO"]["fResult"]     = fDO
  ttConfig["SENSOR"]["DO Sat"]["fResult"] = fDOsat
  ttConfig["SENSOR"]["PH"]["fResult"]     = fPH
  ttConfig["SENSOR"]["PHmv"]["fResult"]   = fPHmv
  ttConfig["SENSOR"]["ORP"]["fResult"]    = fORP
  ttConfig["SENSOR"]["Depth"]["fResult"]  = fDepth
  ttConfig["SENSOR"]["AUX1"]["fResult"]   = fAUX1
  ttConfig["SENSOR"]["AUX2"]["fResult"]   = fAUX2
  ttConfig["SENSOR"]["AUX3"]["fResult"]   = fAUX3
  ttConfig["SENSOR"]["AUX4"]["fResult"]   = fAUX4
  ttConfig["SENSOR"]["AUX5"]["fResult"]   = fAUX5
  ttConfig["SENSOR"]["AUX6"]["fResult"]   = fAUX6
  ttConfig["SENSOR"]["AUX7"]["fResult"]   = fAUX7

  ttConfig["CALCULATED"]["EC"]["fEC_20"]    = fEC / ( ( ( fTEMP - 20 ) * 0.0191 ) + 1 )
  if( ttConfig["SENSOR"]["EC"]["bSC35_flag"] ):
   ttConfig["CALCULATED"]["EC"]["fEC_25"]     = fEC / ( ( ( fTEMP - 25 ) * 0.0181 ) + 1 )
  else:
   ttConfig["CALCULATED"]["EC"]["fEC_25"]     = fEC / ( ( ( fTEMP - 25 ) * 0.0191 ) + 1 )
  ttConfig["CALCULATED"]["TEMP"]["fTempF"]     = fTEMP * 1.8 + 32
  ttConfig["CALCULATED"]["DEPTH"]["fDepthF"]   = fDepth * 3.28083
  ttConfig["CALCULATED"]["AMMONIA"]["fResult"] = fAUX7

  # Salinity
  fSal_K0 = 0.012
  fSal_K1 = -0.2174
  fSal_K2 = 25.3283
  fSal_K3 = 13.7714
  fSal_K4 = -6.4788
  fSal_K5 = 2.5842
  fSal_Sea_EC25 = 53087
  r = ttConfig["CALCULATED"]["EC"]["fEC_25"] / fSal_Sea_EC25
  fSalinity = fSal_K0 + fSal_K1 * r ** 0.5 + fSal_K2 * r + fSal_K3 * r ** 1.5 + fSal_K4 * r ** 2 + fSal_K5 * r ** 2.5
  if( fEC == 0 ): fSalinity = 0
  ttConfig["CALCULATED"]["Salinity"]["fResult"] = fSalinity

  # SSG
  fDen_R0  = 3.9863
  fDen_R1  = 288.9414
  fDen_R2  = 68.12963
  fDen_R3  = 508.9292
  fDen_K00 = 0.824493
  fDen_K01 = -0.0040899
  fDen_K02 = 0.000076438
  fDen_K03 = -0.00000082467
  fDen_K04 = 0.0000000053675
  fDen_K10 = -0.005724
  fDen_K11 = 0.00010227
  fDen_K12 = -0.0000016546
  fDen_K20 = 0.00048314
  fDensity = 1000.0 - (fTEMP - fDen_R0) ** 2 * (fTEMP + fDen_R1) / (fTEMP + fDen_R2) / fDen_R3
  fA0      = fDen_K00 + fDen_K01 * fTEMP + fDen_K02 * fTEMP ** 2 + fDen_K03 * fTEMP ** 3 + fDen_K04 * fTEMP ** 4
  fA1      = fDen_K10 + fDen_K11 * fTEMP + fDen_K12 * fTEMP ** 2
  fDensity = fDensity + fA0 * fSalinity + fA1 * fSalinity ** 1.5 + fDen_K20 * fSalinity ** 2
  fSSG     = fDensity - 1000
  if( fEC == 0 ): fSSG = 0
  ttConfig["CALCULATED"]["SSG"]["fResult"] = fSSG

  # TDS
  fTDSFactor = ttConfig["CALCULATED"]["TDS"]["fFactor"]
  fTDS = fEC * fTDSFactor
  ttConfig["CALCULATED"]["TDS"]["fResult"]      = fTDS

  ttConfig["SENSOR"]["AUX1"]["iTrend"]  = 1 if( ( uiAUX1_HSB & 0xC0 ) == 0x10 ) else ( -1 if( ( uiAUX1_HSB & 0xC0 ) == 0x20 ) else 0 )
  ttConfig["SENSOR"]["AUX2"]["iTrend"]  = 1 if( ( uiAUX2_HSB & 0xC0 ) == 0x10 ) else ( -1 if( ( uiAUX2_HSB & 0xC0 ) == 0x20 ) else 0 )
  ttConfig["SENSOR"]["AUX3"]["iTrend"]  = 1 if( ( uiAUX3_HSB & 0xC0 ) == 0x10 ) else ( -1 if( ( uiAUX3_HSB & 0xC0 ) == 0x20 ) else 0 )
  ttConfig["SENSOR"]["AUX4"]["iTrend"]  = 1 if( ( uiAUX4_HSB & 0xC0 ) == 0x10 ) else ( -1 if( ( uiAUX4_HSB & 0xC0 ) == 0x20 ) else 0 )
  ttConfig["SENSOR"]["AUX5"]["iTrend"]  = 1 if( ( uiAUX5_HSB & 0xC0 ) == 0x10 ) else ( -1 if( ( uiAUX5_HSB & 0xC0 ) == 0x20 ) else 0 )
  ttConfig["SENSOR"]["AUX6"]["iTrend"]  = 1 if( ( uiAUX6_HSB & 0xC0 ) == 0x10 ) else ( -1 if( ( uiAUX6_HSB & 0xC0 ) == 0x20 ) else 0 )
  ttConfig["SENSOR"]["AUX7"]["iTrend"]  = 1 if( ( uiAUX7_HSB & 0xC0 ) == 0x10 ) else ( -1 if( ( uiAUX7_HSB & 0xC0 ) == 0x20 ) else 0 )

  # Retour de la donnée
  return( ttConfig["SENSOR"] )

 #--------------------------
 # Formattage pour écriture config site
 #--------------------------
 def ttFParseWriteConfigSite( self, ttConfig ):
  #-- Parse de la data --
  # Récupération des valeurs
  sSiteID   = ttConfig["PRODUCT"]["sSiteID"]
  sSiteLat  = ttConfig["PRODUCT"]["sSiteLat"]
  sSiteLong = ttConfig["PRODUCT"]["sSiteLong"]
  # Adaptation chaine
  if( len(sSiteID) < 16 ):
   ucCpt = len(sSiteID)
   for ucCpt2 in range( ucCpt, 16 ):
    sSiteID = sSiteID + " "
  # Site latitude
  tucSiteLat = QByteArray()
  tucSiteLat.append(sSiteLat[0])
  print("len(sSiteLat)")
  print(len(sSiteLat))
  print(sSiteLat)
  for ucCpt in range(1,len(sSiteLat)):
   # SUppression des caractères de formattage
   if( not sSiteLat[ucCpt].isdigit() ): continue
   # Ajout à notre tableau de la donnée
   tucSiteLat.append(int(sSiteLat[ucCpt]))
  # Site Longitude
  tucSiteLong = QByteArray()
  tucSiteLong.append(sSiteLong[0])
  for ucCpt in range(1,len(sSiteLong)):
   # SUppression des caractères de formattage
   if( not sSiteLong[ucCpt].isdigit() ): continue
   # Ajout à notre tableau de la donnée
   tucSiteLong.append(int(sSiteLong[ucCpt]))

  # Formattage à partir du prototype
  txDataByte = struct.pack( ">16s7c8c",
                            sSiteID.encode('utf-8'),
                            tucSiteLat[0],
                            tucSiteLat[1],
                            tucSiteLat[2],
                            tucSiteLat[3],
                            tucSiteLat[4],
                            tucSiteLat[5],
                            tucSiteLat[6],
                            tucSiteLong[0],
                            tucSiteLong[1],
                            tucSiteLong[2],
                            tucSiteLong[3],
                            tucSiteLong[4],
                            tucSiteLong[5],
                            tucSiteLong[6],
                            tucSiteLong[7]
                            )
  # Retourne buffer
  return( txDataByte )

 #--------------------------
 # Formattage pour écriture user settings
 #--------------------------
 def ttFParseWriteUserSettings( self, ttConfig ):
  #-- Parse de la data --
  # Récupération des valeurs
  uiLogMin  = ( ttConfig["PRODUCT"]["uiLOG_HOUR"] * 60 ) + ttConfig["PRODUCT"]["uiLOG_MIN"]
  uiLogSec  = ttConfig["PRODUCT"]["uiLOG_SEC"]
  # Si minute à 0
  if( uiLogMin == 0 ):
   # Cas normalement impossible d'avoir h/m/s à 0 en même temps : forçage 20 min en cadence
   if( uiLogSec == 0 ):
    uiLogSec = 0
    uiLogMin = 20
   else:
    # Activation du mode seconde
    uiLogSec = 1
    # Les secondes sont stockées dans le registre minute
    uiLogMin = ttConfig["PRODUCT"]["uiLOG_SEC"]
  # Minutes ou heures définit : secondes à 0
  else:
   uiLogSec = 0

  uiLogEvent    = ttConfig["PRODUCT"]["uiLOG_EVENT"]
  uiLogSensor   = ttConfig["PRODUCT"]["uiLOG_SENSOR"]
  uiEventMin    = ( ttConfig["PRODUCT"]["uiEVENT_HOUR"] * 60 ) + ttConfig["PRODUCT"]["uiEVENT_MIN"]
  uiCleanHR     = ttConfig["PRODUCT"]["uiCLEAN_HR"]
  uiEventChange = ttConfig["PRODUCT"]["uiEVENT_CHANGE"]

  print("uiLogMin      = %d"%uiLogMin)
  print("uiLogSec      = %d"%uiLogSec)
  print("uiLogEvent    = %d"%uiLogEvent)
  print("uiLogSensor   = %d"%uiLogSensor)
  print("uiEventMin    = %d"%uiEventMin)
  print("uiCleanHR     = %d"%uiCleanHR)
  print("uiEventChange = %d"%uiEventChange)

  # Formattage à partir du prototype
  txDataByte = struct.pack( ">H3BH2B",
                            uiLogMin,
                            uiLogSec,
                            uiLogEvent,
                            uiLogSensor,
                            uiEventMin,
                            uiCleanHR,
                            uiEventChange
                            )
  # Retourne buffer
  return( txDataByte )

 #--------------------------
 # Formattage pour écriture sonde clock
 #--------------------------
 def ttFParseWriteSondeClock( self, ttConfig ):
  print("-- ttFParseWriteSondeClock --")
  #-- Parse de la data --
  # Récupération des valeurs
  uiRTCYear  = ttConfig["PRODUCT"]["uiRTCYear"]
  uiRTCMonth = ttConfig["PRODUCT"]["uiRTCMonth"]
  uiRTCDays  = ttConfig["PRODUCT"]["uiRTCDays"]
  uiRTCHour  = ttConfig["PRODUCT"]["uiRTCHour"]
  uiRTCMin   = ttConfig["PRODUCT"]["uiRTCMin"]
  uiRTCSec   = ttConfig["PRODUCT"]["uiRTCSec"]
  print("uiRTCYear   = %d"%uiRTCYear)
  print("uiRTCMonth  = %d"%uiRTCMonth)
  print("uiRTCDays   = %d"%uiRTCDays)
  print("uiRTCHour   = %d"%uiRTCHour)
  print("uiRTCMin    = %d"%uiRTCMin)
  print("uiRTCSec    = %d"%uiRTCSec)
  # Formattage à partir du prototype
  txDataByte = struct.pack( ">6B",
                            uiRTCHour,
                            uiRTCMin,
                            uiRTCSec,
                            uiRTCDays,
                            uiRTCMonth,
                            uiRTCYear
                            )
  print( txDataByte )
  print( txDataByte.hex() )
  # Retourne buffer
  return( txDataByte )

 #--------------------------
 # Formattage pour écriture AUX Assignement
 #--------------------------
 def ttFParseWriteGS( self, ttConfig ):
  #-- Parse de la data --
  # Récupération des valeurs
  uiAux1Assign  = self.uiFGetIDWithChannelNameWith( ttConfig["SENSOR"]["AUX1"]["sIndex"] )
  uiAux2Assign  = self.uiFGetIDWithChannelNameWith( ttConfig["SENSOR"]["AUX2"]["sIndex"] )
  uiAux3Assign  = self.uiFGetIDWithChannelNameWith( ttConfig["SENSOR"]["AUX3"]["sIndex"] )
  uiAux4Assign  = self.uiFGetIDWithChannelNameWith( ttConfig["SENSOR"]["AUX4"]["sIndex"] )
  uiAux5Assign  = self.uiFGetIDWithChannelNameWith( ttConfig["SENSOR"]["AUX5"]["sIndex"] )
  uiAux6Assign  = self.uiFGetIDWithChannelNameWith( ttConfig["SENSOR"]["AUX6"]["sIndex"] )

  print("uiAux1Assign = %d"%uiAux1Assign)
  print("uiAux2Assign = %d"%uiAux2Assign)
  print("uiAux3Assign = %d"%uiAux3Assign)
  print("uiAux4Assign = %d"%uiAux4Assign)
  print("uiAux5Assign = %d"%uiAux5Assign)
  print("uiAux6Assign = %d"%uiAux6Assign)

  print(ttConfig)

  print('ttConfig["SENSOR"]["AUX1"]["fGS"] = %d'%ttConfig["SENSOR"]["AUX1"]["fGS"])
  print('ttConfig["SENSOR"]["AUX2"]["fGS"] = %d'%ttConfig["SENSOR"]["AUX2"]["fGS"])
  print('ttConfig["SENSOR"]["AUX3"]["fGS"] = %d'%ttConfig["SENSOR"]["AUX3"]["fGS"])
  print('ttConfig["SENSOR"]["AUX4"]["fGS"] = %d'%ttConfig["SENSOR"]["AUX4"]["fGS"])
  print('ttConfig["SENSOR"]["AUX5"]["fGS"] = %d'%ttConfig["SENSOR"]["AUX5"]["fGS"])
  print('ttConfig["SENSOR"]["AUX6"]["fGS"] = %d'%ttConfig["SENSOR"]["AUX6"]["fGS"])

  fAUX1GS = ttConfig["SENSOR"]["AUX1"]["fGS"]
  fAUX2GS = ttConfig["SENSOR"]["AUX2"]["fGS"]
  fAUX3GS = ttConfig["SENSOR"]["AUX3"]["fGS"]
  fAUX4GS = ttConfig["SENSOR"]["AUX4"]["fGS"]
  fAUX5GS = ttConfig["SENSOR"]["AUX5"]["fGS"]
  fAUX6GS = ttConfig["SENSOR"]["AUX6"]["fGS"]

  if( uiAux1Assign == 0 ): fAUX1GS = 0
  if( uiAux2Assign == 0 ): fAUX2GS = 0
  if( uiAux3Assign == 0 ): fAUX3GS = 0
  if( uiAux4Assign == 0 ): fAUX4GS = 0
  if( uiAux5Assign == 0 ): fAUX5GS = 0
  if( uiAux6Assign == 0 ): fAUX6GS = 0

  tCurrentDateTime = datetime.now()
  #tCurrentDateTime = datetime(2015, 9, 15)

  print("%d/%d/%d"%(tCurrentDateTime.day,
                    tCurrentDateTime.month,
                    tCurrentDateTime.year-2000))

  # Si version >= 5.11
  if( ttConfig["PRODUCT"]["uiPSW"] >= 511 ):
   # Ajout de l'optical avg au mois
   uiMonth = tCurrentDateTime.month + ttConfig["PRODUCT"]["uiOpticalAvg"]
  else:
   # Ajout de l'optical avg au mois
   uiMonth = tCurrentDateTime.month

  # Formattage à partir du prototype
  txDataByte = struct.pack( ">19B",
                            tCurrentDateTime.day,
                            uiMonth,
                            tCurrentDateTime.year-2000,
                            ( ( ttConfig["SENSOR"]["EC"]["uiUserCalValue"]       ) & 0xFF ),
                            ( ( ttConfig["SENSOR"]["EC"]["uiUserCalValue"] >> 8  ) & 0xFF ),
                            ( ( ttConfig["SENSOR"]["EC"]["uiUserCalValue"] >> 16 ) & 0xFF ),
                            ( ( int( fAUX1GS * 100 )      ) & 0xFF ),
                            ( ( int( fAUX1GS * 100 ) >> 8 ) & 0xFF ),
                            ( ( int( fAUX2GS * 100 )      ) & 0xFF ),
                            ( ( int( fAUX2GS * 100 ) >> 8 ) & 0xFF ),
                            ( ( int( fAUX3GS * 100 )      ) & 0xFF ),
                            ( ( int( fAUX3GS * 100 ) >> 8 ) & 0xFF ),
                            ( ( int( fAUX4GS * 100 )      ) & 0xFF ),
                            ( ( int( fAUX4GS * 100 ) >> 8 ) & 0xFF ),
                            ( ( int( fAUX5GS * 100 )      ) & 0xFF ),
                            ( ( int( fAUX5GS * 100 ) >> 8 ) & 0xFF ),
                            ( ( int( fAUX6GS * 100 )      ) & 0xFF ),
                            ( ( int( fAUX6GS * 100 ) >> 8 ) & 0xFF ),
                            ttConfig["SENSOR"]["TEMP"]["uiTEMP_CalOffset"]
                            )
  # Retourne buffer
  return( txDataByte )

 #--------------------------
 # Formattage pour écriture AUX Assignement
 #--------------------------
 def ttFParseWriteAUXAssignement( self, ttConfig ):
  #-- Parse de la data --
  # Récupération des valeurs
  uiAux1Assign  = self.uiFGetIDWithChannelNameWith( ttConfig["SENSOR"]["AUX1"]["sIndex"] )
  uiAux2Assign  = self.uiFGetIDWithChannelNameWith( ttConfig["SENSOR"]["AUX2"]["sIndex"] )
  uiAux3Assign  = self.uiFGetIDWithChannelNameWith( ttConfig["SENSOR"]["AUX3"]["sIndex"] )
  uiAux4Assign  = self.uiFGetIDWithChannelNameWith( ttConfig["SENSOR"]["AUX4"]["sIndex"] )
  uiAux5Assign  = self.uiFGetIDWithChannelNameWith( ttConfig["SENSOR"]["AUX5"]["sIndex"] )
  uiAux6Assign  = self.uiFGetIDWithChannelNameWith( ttConfig["SENSOR"]["AUX6"]["sIndex"] )

  print("uiAux1Assign = %d"%uiAux1Assign)
  print("uiAux2Assign = %d"%uiAux2Assign)
  print("uiAux3Assign = %d"%uiAux3Assign)
  print("uiAux4Assign = %d"%uiAux4Assign)
  print("uiAux5Assign = %d"%uiAux5Assign)
  print("uiAux6Assign = %d"%uiAux6Assign)

  # Formattage à partir du prototype
  txDataByte = struct.pack( ">6B",
                            uiAux1Assign,
                            uiAux2Assign,
                            uiAux3Assign,
                            uiAux4Assign,
                            uiAux5Assign,
                            uiAux6Assign
                            )
  # Retourne buffer
  return( txDataByte )

 #--------------------------
 # Formattage pour écriture sonde clock
 #--------------------------
 def ttFParseRecordedData( self, ttConfig, txData ):
  print("-- ttFParseRecordedData --")
  #-- Parse de la data --
  # Calcul de la taille de la data
  uiTotalSize = len(txData)
  # On retire le CRC
  uiTotalDataSize = uiTotalSize - 4
  # Nombre de paquets de donnée
  uiMemRecords = ttConfig["PRODUCT"]["uiMemRecords"]
  # Taille des paquets
  uiPacketSize = 55

  # Debug
  print( "uiTotalDataSize = %d"%uiTotalDataSize )
  print( "uiMemRecords = %d"%uiMemRecords )
  print( "uiPacketSize = %d"%uiPacketSize )
  print( "uiMemRecords * uiPacketSize = %d"%(uiMemRecords * uiPacketSize) )

  # Controle de la taille des paquets
  if( uiTotalDataSize != ( uiMemRecords * uiPacketSize ) ):
   print("Erreur taille des paquets")
   return( None )
  # Ok
  print("Taille des paquets conformes")

  # Formattage du prototype de donnée
  sProto = '>2B'
  for uiCpt in range(uiMemRecords):
   #print("Loop %d"%uiCpt)
   sProto = sProto + str(uiPacketSize) + "s"
  # Ajout des CRC
  sProto = sProto + "2B"

  # Decryptage de la donnée binaire
  txUnpacked = struct.unpack( sProto, txData )

  ttMeasure = []
  # Unpack de chaque packet de données
  for uiCpt in range(uiMemRecords):
   #print("Loop %d"%uiCpt)
   ttMeasure.append({})
   #
   ttData = struct.unpack( "55B", txUnpacked[uiCpt+2] )
   uiCptData = 0

   # Datetime
   uiDay      = ttData[uiCptData]; uiCptData+=1
   uiMonth    = ttData[uiCptData]; uiCptData+=1
   uiYear     = ttData[uiCptData]; uiCptData+=1
   uiHour     = ttData[uiCptData]; uiCptData+=1
   uiMinute   = ttData[uiCptData]; uiCptData+=1
   uiSecond   = ttData[uiCptData]; uiCptData+=1
   # Temperature
   uiTempMSB  = ttData[uiCptData]; uiCptData+=1
   uiTempLSB  = ttData[uiCptData]; uiCptData+=1
   # pH
   uipHMSB    = ttData[uiCptData]; uiCptData+=1
   uipHLSB    = ttData[uiCptData]; uiCptData+=1
   # DO
   uiDoMSB    = ttData[uiCptData]; uiCptData+=1
   uiDoLSB    = ttData[uiCptData]; uiCptData+=1
   # EC
   uiEcHSB    = ttData[uiCptData]; uiCptData+=1
   uiEcMSB    = ttData[uiCptData]; uiCptData+=1
   uiEcLSB    = ttData[uiCptData]; uiCptData+=1
   # DO Sat
   uiDoPCMSB  = ttData[uiCptData]; uiCptData+=1
   uiDoPCLSB  = ttData[uiCptData]; uiCptData+=1
   # Baro
   uiBaroMSB  = ttData[uiCptData]; uiCptData+=1
   uiBaroLSB  = ttData[uiCptData]; uiCptData+=1
   # pH mV
   uipHmVMSB  = ttData[uiCptData]; uiCptData+=1
   uipHmVLSB  = ttData[uiCptData]; uiCptData+=1
   # ORP
   uiOrpMSB   = ttData[uiCptData]; uiCptData+=1
   uiOrpLSB   = ttData[uiCptData]; uiCptData+=1
   # Depth
   uiDepthMSB = ttData[uiCptData]; uiCptData+=1
   uiDepthLSB = ttData[uiCptData]; uiCptData+=1
   # AUX 1
   uiAux1HSB      = ttData[uiCptData]; uiCptData+=1
   uiAux1MSB      = ttData[uiCptData]; uiCptData+=1
   uiAux1LSB      = ttData[uiCptData]; uiCptData+=1
   uiAux1ASSign   = ttData[uiCptData]; uiCptData+=1
   # AUX 2
   uiAux2HSB      = ttData[uiCptData]; uiCptData+=1
   uiAux2MSB      = ttData[uiCptData]; uiCptData+=1
   uiAux2LSB      = ttData[uiCptData]; uiCptData+=1
   uiAux2ASSign   = ttData[uiCptData]; uiCptData+=1
   # AUX 3
   uiAux3HSB      = ttData[uiCptData]; uiCptData+=1
   uiAux3MSB      = ttData[uiCptData]; uiCptData+=1
   uiAux3LSB      = ttData[uiCptData]; uiCptData+=1
   uiAux3ASSign   = ttData[uiCptData]; uiCptData+=1
   # AUX 4
   uiAux4HSB      = ttData[uiCptData]; uiCptData+=1
   uiAux4MSB      = ttData[uiCptData]; uiCptData+=1
   uiAux4LSB      = ttData[uiCptData]; uiCptData+=1
   uiAux4ASSign   = ttData[uiCptData]; uiCptData+=1
   # AUX 5
   uiAux5HSB      = ttData[uiCptData]; uiCptData+=1
   uiAux5MSB      = ttData[uiCptData]; uiCptData+=1
   uiAux5LSB      = ttData[uiCptData]; uiCptData+=1
   uiAux5ASSign   = ttData[uiCptData]; uiCptData+=1
   # AUX 6
   uiAux6HSB      = ttData[uiCptData]; uiCptData+=1
   uiAux6MSB      = ttData[uiCptData]; uiCptData+=1
   uiAux6LSB      = ttData[uiCptData]; uiCptData+=1
   uiAux6ASSign   = ttData[uiCptData]; uiCptData+=1
   # AUX 7
   uiAux7HSB      = ttData[uiCptData]; uiCptData+=1
   uiAux7MSB      = ttData[uiCptData]; uiCptData+=1
   uiAux7LSB      = ttData[uiCptData]; uiCptData+=1
   # Clean flag
   uiCleanFlag    = ttData[uiCptData]; uiCptData+=1
   # Batt level
   uiBattLevelMSB = ttData[uiCptData]; uiCptData+=1
   uiBattLevelLSB = ttData[uiCptData]; uiCptData+=1
   #
   #print(ttData[0])
   # Remplissage du tableau de donnée
   ttMeasure[uiCpt]["bShow"]     = True
   ttMeasure[uiCpt]["uiDay"]     = uiDay
   ttMeasure[uiCpt]["uiMonth"]   = uiMonth
   ttMeasure[uiCpt]["uiYear"]    = uiYear
   ttMeasure[uiCpt]["sDay"]      = ( ("0"+str(uiDay))   if( uiDay<10 )   else str(uiDay) )
   ttMeasure[uiCpt]["sMonth"]    = ( ("0"+str(uiMonth)) if( uiMonth<10 ) else str(uiMonth) )
   ttMeasure[uiCpt]["sYear"]     = ( ("0"+str(uiYear))  if( uiYear<10 )  else str(uiYear) )
   ttMeasure[uiCpt]["sDate"]     = "20"+ttMeasure[uiCpt]["sYear"]+"/"+ttMeasure[uiCpt]["sMonth"]+"/"+ttMeasure[uiCpt]["sDay"]
   ttMeasure[uiCpt]["uiHour"]    = uiHour
   ttMeasure[uiCpt]["uiMinute"]  = uiMinute
   ttMeasure[uiCpt]["uiSecond"]  = uiSecond
   ttMeasure[uiCpt]["sHour"]     = ( ("0"+str(uiHour))   if( uiHour<10 )   else str(uiHour) )
   ttMeasure[uiCpt]["sMinute"]   = ( ("0"+str(uiMinute)) if( uiMinute<10 ) else str(uiMinute) )
   ttMeasure[uiCpt]["sSecond"]   = ( ("0"+str(uiSecond)) if( uiSecond<10 ) else str(uiSecond) )
   ttMeasure[uiCpt]["sTime"]     = ttMeasure[uiCpt]["sHour"]+":"+ttMeasure[uiCpt]["sMinute"]+":"+ttMeasure[uiCpt]["sSecond"]
   ttMeasure[uiCpt]["sDateTime"] = ttMeasure[uiCpt]["sDate"] + " " + ttMeasure[uiCpt]["sTime"]
   ttMeasure[uiCpt]["tDateTime"] = ttMeasure[uiCpt]["sDate"] + " " + ttMeasure[uiCpt]["sTime"]
   # Température
   #ttMeasure[uiCpt]["bTemperature"] = True
   fTemperature = ( -1 if( uiTempMSB & 0x80 ) else 1 ) * ( ( ( uiTempMSB & 0x7F ) << 8 ) + uiTempLSB ) / 100
   ttMeasure[uiCpt]["fTempC"] = fTemperature
   ttMeasure[uiCpt]["fTempF"] = fTemperature * 1.8 + 32
   ttMeasure[uiCpt]["sTempC"] = ( "%.2f" % fTemperature )
   ttMeasure[uiCpt]["sTempF"] = ( "%.2f" % ( fTemperature * 1.8 + 32 ) )
   # Depth
   ttMeasure[uiCpt]["fDepthM"] = float( ( -1 if( uiDepthMSB & 0x80 ) else 1 ) * ( ( ( uiDepthMSB & 0x7F ) << 8 ) + uiDepthLSB ) / 100 )
   ttMeasure[uiCpt]["fDepthF"] = float( ( -1 if( uiDepthMSB & 0x80 ) else 1 ) * ( ( ( uiDepthMSB & 0x7F ) << 8 ) + uiDepthLSB ) / 100 ) * 3.28083
   ttMeasure[uiCpt]["sDepthM"] = ( "%.3f" % ttMeasure[uiCpt]["fDepthM"] )
   ttMeasure[uiCpt]["sDepthF"] = ( "%.3f" % ttMeasure[uiCpt]["fDepthF"] )
   # BARO
   ttMeasure[uiCpt]["fBaro"] = ( ( uiBaroMSB << 8 ) + uiBaroLSB )
   ttMeasure[uiCpt]["sBaro"] = ( "%.0f" % ttMeasure[uiCpt]["fBaro"] )
   # pH
   ttMeasure[uiCpt]["fpH"] = ( ( ( uipHMSB & 0x7F ) << 8 ) + uipHLSB ) / 100
   ttMeasure[uiCpt]["bpH_RangeFlag"] = uipHMSB & 0x80 # PH_RANGE_FLAG ???
   ttMeasure[uiCpt]["spH"] = ( "%.2f" % ttMeasure[uiCpt]["fpH"] ) if( not ttMeasure[uiCpt]["bpH_RangeFlag"] ) else "--.--"
   # pH mV
   ttMeasure[uiCpt]["fpHmV"] = ( -1 if( uipHmVMSB & 0x80 ) else 1 ) * ( ( ( uipHmVMSB & 0x7F ) << 8 ) + uipHmVLSB ) / 10
   ttMeasure[uiCpt]["spHmV"] = ( "%.1f" % ttMeasure[uiCpt]["fpHmV"] )
   # ORP
   ttMeasure[uiCpt]["fORP"] = ( -1 if( uiOrpMSB & 0x80 ) else 1 ) * ( ( ( uiOrpMSB & 0x7F ) << 8 ) + uiOrpLSB ) / 10
   ttMeasure[uiCpt]["sORP"] = ( "%.1f" % ttMeasure[uiCpt]["fORP"] )
   # DO_PC
   ttMeasure[uiCpt]["fDO_PC"] = ( ( uiDoPCMSB << 8 ) + uiDoPCLSB ) / 10
   ttMeasure[uiCpt]["sDO_PC"] = ( "%.1f" % ttMeasure[uiCpt]["fDO_PC"] )
   # DO
   ttMeasure[uiCpt]["fDO"] = ( ( ( uiDoMSB & 0x7F ) << 8 ) + uiDoLSB ) / 100
   ttMeasure[uiCpt]["bDOCap"] = uiDoMSB & 0x80
   ttMeasure[uiCpt]["sDO"] = ( "%.2f" % ttMeasure[uiCpt]["fDO"] )
   # EC
   fEC = ( -1 if( uiEcHSB & 0x80 ) else 1 ) * ( ( ( uiEcHSB & 0x7F ) << 16 ) + ( uiEcMSB << 8 ) + uiEcLSB )
   ttMeasure[uiCpt]["fEC"] = fEC
   ttMeasure[uiCpt]["sEC"] = ( "%.0f" % ttMeasure[uiCpt]["fEC"] )
   # EC_25
   ttMeasure[uiCpt]["fEC_25"] = ttMeasure[uiCpt]["fEC"] / ( ( ( fTemperature - 25 ) * 0.0191 ) + 1 )
   ttMeasure[uiCpt]["sEC_25"] = ( "%.0f" % ttMeasure[uiCpt]["fEC_25"] )
   # EC_20
   ttMeasure[uiCpt]["fEC_20"] = ttMeasure[uiCpt]["fEC"] / ( ( ( fTemperature - 20 ) * 0.0191 ) + 1 )
   ttMeasure[uiCpt]["sEC_20"] = ( "%.0f" % ttMeasure[uiCpt]["fEC_20"] )

   #-- AUX1
   if( ttConfig["PRODUCT"]["uiAUXNumber"] > 0 ):
    # DP nombre de décimal
    uiAUX1_DP = ( ( uiAux1HSB & 0x30 ) >> 4 )
    fAUX1 = ( -1 if( uiAux1HSB & 0x8 ) else 1 ) * ( ( ( uiAux1HSB & 0x7 ) << 16 ) + ( uiAux1MSB << 8 ) + uiAux1LSB )
    if( uiAUX1_DP == 0 ):
     ttMeasure[uiCpt]["fAUX1"] = fAUX1
     ttMeasure[uiCpt]["sAUX1"] = ( "%.0f" % ttMeasure[uiCpt]["fAUX1"] )
    if( uiAUX1_DP == 1 ):
     ttMeasure[uiCpt]["fAUX1"] = fAUX1 / 10
     ttMeasure[uiCpt]["sAUX1"] = ( "%.1f" % ttMeasure[uiCpt]["fAUX1"] )
    if( uiAUX1_DP == 2 ):
     ttMeasure[uiCpt]["fAUX1"] = fAUX1 / 100
     ttMeasure[uiCpt]["sAUX1"] = ( "%.2f" % ttMeasure[uiCpt]["fAUX1"] )
    if( uiAUX1_DP == 3 ):
     ttMeasure[uiCpt]["fAUX1"] = -9999
     ttMeasure[uiCpt]["sAUX1"] = "----"
    # Assign
    ttMeasure[uiCpt]["uiAUX1_Assign"] = uiAux1ASSign
    ttMeasure[uiCpt]["sAUX1_Assign"]  = self.sFGetChannelNameWithID( uiAux1ASSign )

   #-- AUX2
   if( ttConfig["PRODUCT"]["uiAUXNumber"] > 1 ):
    # DP nombre de décimal
    uiAUX2_DP = ( ( uiAux2HSB & 0x30 ) >> 4 )
    fAUX2 = ( -1 if( uiAux2HSB & 0x8 ) else 1 ) * ( ( ( uiAux2HSB & 0x7 ) << 16 ) + ( uiAux2MSB << 8 ) + uiAux2LSB )
    if( uiAUX2_DP == 0 ):
     ttMeasure[uiCpt]["fAUX2"] = fAUX2
     ttMeasure[uiCpt]["sAUX2"] = ( "%.0f" % ttMeasure[uiCpt]["fAUX2"] )
    if( uiAUX2_DP == 1 ):
     ttMeasure[uiCpt]["fAUX2"] = fAUX2 / 10
     ttMeasure[uiCpt]["sAUX2"] = ( "%.1f" % ttMeasure[uiCpt]["fAUX2"] )
    if( uiAUX2_DP == 2 ):
     ttMeasure[uiCpt]["fAUX2"] = fAUX2 / 100
     ttMeasure[uiCpt]["sAUX2"] = ( "%.2f" % ttMeasure[uiCpt]["fAUX2"] )
    if( uiAUX2_DP == 3 ):
     ttMeasure[uiCpt]["fAUX2"] = -9999
     ttMeasure[uiCpt]["sAUX2"] = "----"
    # Assign
    ttMeasure[uiCpt]["uiAUX2_Assign"] = uiAux2ASSign
    ttMeasure[uiCpt]["sAUX2_Assign"]  = self.sFGetChannelNameWithID( uiAux2ASSign )

   #-- AUX3
   if( ttConfig["PRODUCT"]["uiAUXNumber"] > 2 ):
    # DP nombre de décimal
    uiAUX3_DP = ( ( uiAux3HSB & 0x30 ) >> 4 )
    fAUX3 = ( -1 if( uiAux3HSB & 0x8 ) else 1 ) * ( ( ( uiAux3HSB & 0x7 ) << 16 ) + ( uiAux3MSB << 8 ) + uiAux3LSB )
    print( "%.3f" % fAUX3 )
    if( uiAUX3_DP == 0 ):
     ttMeasure[uiCpt]["fAUX3"] = fAUX3
     ttMeasure[uiCpt]["sAUX3"] = ( "%.0f" % ttMeasure[uiCpt]["fAUX3"] )
    if( uiAUX3_DP == 1 ):
     ttMeasure[uiCpt]["fAUX3"] = fAUX3 / 10
     ttMeasure[uiCpt]["sAUX3"] = ( "%.1f" % ttMeasure[uiCpt]["fAUX3"] )
    if( uiAUX3_DP == 2 ):
     ttMeasure[uiCpt]["fAUX3"] = fAUX3 / 100
     ttMeasure[uiCpt]["sAUX3"] = ( "%.2f" % ttMeasure[uiCpt]["fAUX3"] )
    if( uiAUX3_DP == 3 ):
     ttMeasure[uiCpt]["fAUX3"] = -9999
     ttMeasure[uiCpt]["sAUX3"] = "----"
    # Assign
    ttMeasure[uiCpt]["uiAUX3_Assign"] = uiAux3ASSign
    ttMeasure[uiCpt]["sAUX3_Assign"]  = self.sFGetChannelNameWithID( uiAux3ASSign )

   #-- AUX4
   if( ttConfig["PRODUCT"]["uiAUXNumber"] > 3 ):
    # DP nombre de décimal
    uiAUX4_DP = ( ( uiAux4HSB & 0x30 ) >> 4 )
    fAUX4 = ( -1 if( uiAux4HSB & 0x8 ) else 1 ) * ( ( ( uiAux4HSB & 0x7 ) << 16 ) + ( uiAux4MSB << 8 ) + uiAux4LSB )
    if( uiAUX4_DP == 0 ):
     ttMeasure[uiCpt]["fAUX4"] = fAUX4
     ttMeasure[uiCpt]["sAUX4"] = ( "%.0f" % ttMeasure[uiCpt]["fAUX4"] )
    if( uiAUX4_DP == 1 ):
     ttMeasure[uiCpt]["fAUX4"] = fAUX4 / 10
     ttMeasure[uiCpt]["sAUX4"] = ( "%.1f" % ttMeasure[uiCpt]["fAUX4"] )
    if( uiAUX4_DP == 2 ):
     ttMeasure[uiCpt]["fAUX4"] = fAUX4 / 100
     ttMeasure[uiCpt]["sAUX4"] = ( "%.2f" % ttMeasure[uiCpt]["fAUX4"] )
    if( uiAUX4_DP == 3 ):
     ttMeasure[uiCpt]["fAUX4"] = -9999
     ttMeasure[uiCpt]["sAUX4"] = "----"
    # Assign
    ttMeasure[uiCpt]["uiAUX4_Assign"] = uiAux4ASSign
    ttMeasure[uiCpt]["sAUX4_Assign"]  = self.sFGetChannelNameWithID( uiAux4ASSign )

   #-- AUX5
   if( ttConfig["PRODUCT"]["uiAUXNumber"] > 4 ):
    # DP nombre de décimal
    uiAUX5_DP = ( ( uiAux5HSB & 0x30 ) >> 4 )
    fAUX5 = ( -1 if( uiAux5HSB & 0x8 ) else 1 ) * ( ( ( uiAux5HSB & 0x7 ) << 16 ) + ( uiAux5MSB << 8 ) + uiAux5LSB )
    if( uiAUX5_DP == 0 ):
     ttMeasure[uiCpt]["fAUX5"] = fAUX5
     ttMeasure[uiCpt]["sAUX5"] = ( "%.0f" % ttMeasure[uiCpt]["fAUX5"] )
    if( uiAUX5_DP == 1 ):
     ttMeasure[uiCpt]["fAUX5"] = fAUX5 / 10
     ttMeasure[uiCpt]["sAUX5"] = ( "%.1f" % ttMeasure[uiCpt]["fAUX5"] )
    if( uiAUX5_DP == 2 ):
     ttMeasure[uiCpt]["fAUX5"] = fAUX5 / 100
     ttMeasure[uiCpt]["sAUX5"] = ( "%.2f" % ttMeasure[uiCpt]["fAUX5"] )
    if( uiAUX5_DP == 3 ):
     ttMeasure[uiCpt]["fAUX5"] = -9999
     ttMeasure[uiCpt]["sAUX5"] = "----"
    # Assign
    ttMeasure[uiCpt]["uiAUX5_Assign"] = uiAux5ASSign
    ttMeasure[uiCpt]["sAUX5_Assign"]  = self.sFGetChannelNameWithID( uiAux5ASSign )

   #-- AUX6
   if( ttConfig["PRODUCT"]["uiAUXNumber"] > 5 ):
    # DP nombre de décimal
    uiAUX6_DP = ( ( uiAux6HSB & 0x30 ) >> 4 )
    fAUX6 = ( -1 if( uiAux6HSB & 0x8 ) else 1 ) * ( ( ( uiAux6HSB & 0x7 ) << 16 ) + ( uiAux6MSB << 8 ) + uiAux6LSB )
    if( uiAUX6_DP == 0 ):
     ttMeasure[uiCpt]["fAUX6"] = fAUX6
     ttMeasure[uiCpt]["sAUX6"] = ( "%.0f" % ttMeasure[uiCpt]["fAUX6"] )
    if( uiAUX6_DP == 1 ):
     ttMeasure[uiCpt]["fAUX6"] = fAUX6 / 10
     ttMeasure[uiCpt]["sAUX6"] = ( "%.1f" % ttMeasure[uiCpt]["fAUX6"] )
    if( uiAUX6_DP == 2 ):
     ttMeasure[uiCpt]["fAUX6"] = fAUX6 / 100
     ttMeasure[uiCpt]["sAUX6"] = ( "%.2f" % ttMeasure[uiCpt]["fAUX6"] )
    if( uiAUX6_DP == 3 ):
     ttMeasure[uiCpt]["fAUX6"] = -9999
     ttMeasure[uiCpt]["sAUX6"] = "----"
    # Assign
    ttMeasure[uiCpt]["uiAUX6_Assign"] = uiAux6ASSign
    ttMeasure[uiCpt]["sAUX6_Assign"]  = self.sFGetChannelNameWithID( uiAux6ASSign )

   #-- AUX7
   # Assign
   if( ttConfig["CALCULATED"]["AMMONIA"]["bActivated"] ):
    # DP nombre de décimal
    uiAUX7_DP = ( ( uiAux7HSB & 0x30 ) >> 4 )
    fAUX7 = ( -1 if( uiAux7HSB & 0x8 ) else 1 ) * ( ( ( uiAux7HSB & 0x7 ) << 16 ) + ( uiAux7MSB << 8 ) + uiAux7LSB )
    if( uiAUX7_DP == 0 ):
     ttMeasure[uiCpt]["fAUX7"] = fAUX7
     ttMeasure[uiCpt]["sAUX7"] = ( "%.0f" % ttMeasure[uiCpt]["fAUX7"] )
    if( uiAUX7_DP == 1 ):
     ttMeasure[uiCpt]["fAUX7"] = fAUX7 / 10
     ttMeasure[uiCpt]["sAUX7"] = ( "%.1f" % ttMeasure[uiCpt]["fAUX7"] )
    if( uiAUX7_DP == 2 ):
     ttMeasure[uiCpt]["fAUX7"] = fAUX7 / 100
     ttMeasure[uiCpt]["sAUX7"] = ( "%.2f" % ttMeasure[uiCpt]["fAUX7"] )
    if( uiAUX7_DP == 3 ):
     ttMeasure[uiCpt]["fAUX7"] = -9999
     ttMeasure[uiCpt]["sAUX7"] = "----"
    # Assign
    ttMeasure[uiCpt]["uiAUX7_Assign"] = 254
    ttMeasure[uiCpt]["sAUX7_Assign"]  = "Ammonia"


   # Cleaning flag
   ttMeasure[uiCpt]["uiCleaningFlag"] = uiCleanFlag
   ttMeasure[uiCpt]["sCleaningFlag"]  = "YES" if( uiCleanFlag == 1 ) else "NO"
   # Battery level
   ttMeasure[uiCpt]["fBatteryLevel"] = ( ( ( uiBattLevelMSB & 0x7F ) << 8 ) + uiBattLevelLSB ) / 102.3
   ttMeasure[uiCpt]["sBatteryLevel"]  = ("%.2f" % ttMeasure[uiCpt]["fBatteryLevel"])

   #print("sTempC = "+ttMeasure[uiCpt]["sTempC"])
   #print("sTempF = "+ttMeasure[uiCpt]["sTempF"])
   #print("spH    = "+ttMeasure[uiCpt]["spH"])

  # Retourne buffer
  return( ttMeasure )

 #--------------------------
 # Calcul des voies calculées
 #--------------------------
 def ttFCalculatedDataCalculation( self, ttConfig, ttMeasure ):
  print("-- TConfigParser > ttFCalculatedDataCalculation --")

  fTDSFactor = ttConfig["CALCULATED"]["TDS"]["fFactor"]

  # Nombre de paquet de donnée
  uiMemRecords = ttConfig["PRODUCT"]["uiMemRecords"]
  # Unpack de chaque packet de données
  for uiCpt in range(uiMemRecords):

   fEC = ttMeasure[uiCpt]["fEC"]
   fTemperature = ttMeasure[uiCpt]["fTempC"]

   # Salinity
   fSal_K0 = 0.012
   fSal_K1 = -0.2174
   fSal_K2 = 25.3283
   fSal_K3 = 13.7714
   fSal_K4 = -6.4788
   fSal_K5 = 2.5842
   fSal_Sea_EC25 = 53087

   r = ttMeasure[uiCpt]["fEC_25"] / fSal_Sea_EC25
   fSalinity = fSal_K0 + fSal_K1 * r ** 0.5 + fSal_K2 * r + fSal_K3 * r ** 1.5 + fSal_K4 * r ** 2 + fSal_K5 * r ** 2.5

   if( fEC == 0 ): fSalinity = 0
   ttMeasure[uiCpt]["fSalinity"] = fSalinity
   ttMeasure[uiCpt]["sSalinity"] = ( "%.2f" % fSalinity )

   # SSG
   fDen_R0  = 3.9863
   fDen_R1  = 288.9414
   fDen_R2  = 68.12963
   fDen_R3  = 508.9292
   fDen_K00 = 0.824493
   fDen_K01 = -0.0040899
   fDen_K02 = 0.000076438
   fDen_K03 = -0.00000082467
   fDen_K04 = 0.0000000053675
   fDen_K10 = -0.005724
   fDen_K11 = 0.00010227
   fDen_K12 = -0.0000016546
   fDen_K20 = 0.00048314
   fDensity = 1000.0 - (fTemperature - fDen_R0) ** 2 * (fTemperature + fDen_R1) / (fTemperature + fDen_R2) / fDen_R3
   fA0      = fDen_K00 + fDen_K01 * fTemperature + fDen_K02 * fTemperature ** 2 + fDen_K03 * fTemperature ** 3 + fDen_K04 * fTemperature ** 4
   fA1      = fDen_K10 + fDen_K11 * fTemperature + fDen_K12 * fTemperature ** 2
   fDensity = fDensity + fA0 * fSalinity + fA1 * fSalinity ** 1.5 + fDen_K20 * fSalinity ** 2
   fSSG     = fDensity - 1000
   if( fEC == 0 ): fSSG = 0

   ttMeasure[uiCpt]["fSSG"] = fSSG
   ttMeasure[uiCpt]["sSSG"] = ( "%.2f" % fSSG )

   # TDS
   fTDS = ttMeasure[uiCpt]["fEC"] * fTDSFactor
   ttMeasure[uiCpt]["fTDS"] = fTDS
   ttMeasure[uiCpt]["sTDS"] = ( "%.2f" % fTDS ) if( fTDS < 10000 ) else ( "%.1f" % fTDS )


 #===========================================================================================
 # Fonctions outils
 #===========================================================================================

 #-------------------------------------
 # Nom de la voie selon l'ID
 #-------------------------------------
 def sFGetChannelNameWithID( self, uiAUXAssign ):
  sAUX1_A = "EMPTY"
  if( uiAUXAssign == 0 ):  sAUX1_A = "EMPTY"
  if( uiAUXAssign == 1 ):  sAUX1_A = "Ammonium"
  if( uiAUXAssign == 2 ):  sAUX1_A = "Chloride"
  if( uiAUXAssign == 3 ):  sAUX1_A = "Fluoride"
  if( uiAUXAssign == 4 ):  sAUX1_A = "Nitrate"
  if( uiAUXAssign == 5 ):  sAUX1_A = "Calcium"
  if( uiAUXAssign == 16 ): sAUX1_A = "Turbidity"
  if( uiAUXAssign == 17 ): sAUX1_A = "Chlorophyll"
  if( uiAUXAssign == 18 ): sAUX1_A = "BGA-PC"
  if( uiAUXAssign == 19 ): sAUX1_A = "BGA-PE"
  if( uiAUXAssign == 20 ): sAUX1_A = "Rhodamine"
  if( uiAUXAssign == 21 ): sAUX1_A = "Fluorescein"
  if( uiAUXAssign == 22 ): sAUX1_A = "Refined Oil"
  if( uiAUXAssign == 23 ): sAUX1_A = "CDOM"
  if( uiAUXAssign == 24 ): sAUX1_A = "Crude Oil"
  if( uiAUXAssign == 25 ): sAUX1_A = "Tryptophan"
  if( uiAUXAssign == 254 ): sAUX1_A = "Amonnia"
  return( sAUX1_A )

 #-------------------------------------
 # Unité de la voie selon l'ID
 #-------------------------------------
 def sFGetChannelUnitWithID( self, uiAUXAssign ):
  sAUX1_A = "--"
  if( uiAUXAssign == 0 ):   sAUX1_A = "--"
  if( uiAUXAssign == 1 ):   sAUX1_A = "ppm"      # Ammonium
  if( uiAUXAssign == 2 ):   sAUX1_A = "ppm"      # Chloride
  if( uiAUXAssign == 3 ):   sAUX1_A = "ppm"      # Fluoride
  if( uiAUXAssign == 4 ):   sAUX1_A = "ppm"      # Nitrate
  if( uiAUXAssign == 5 ):   sAUX1_A = "ppm"      # Calcium
  if( uiAUXAssign == 16 ):  sAUX1_A = "NTU"      # Turbidity
  if( uiAUXAssign == 17 ):  sAUX1_A = "ug/L"     # Chlorophyll
  if( uiAUXAssign == 18 ):  sAUX1_A = "cells/mL" # BGA-PC
  if( uiAUXAssign == 19 ):  sAUX1_A = "cells/mL" # BGA-PE
  if( uiAUXAssign == 20 ):  sAUX1_A = "ug/L"     # Rhodamine
  if( uiAUXAssign == 21 ):  sAUX1_A = "ug/L"     # Fluorescein
  if( uiAUXAssign == 22 ):  sAUX1_A = "ug/L"     # Refined Oil
  if( uiAUXAssign == 23 ):  sAUX1_A = "ug/L"     # CDOM
  if( uiAUXAssign == 24 ):  sAUX1_A = "ug/L"     # Crude Oil
  if( uiAUXAssign == 25 ):  sAUX1_A = "ug/L"     # Tryptophan
  if( uiAUXAssign == 254 ): sAUX1_A = "ppm"      # Ammonia
  return( sAUX1_A )

 #-------------------------------------
 # ID selon le Nom de la voie
 #-------------------------------------
 def uiFGetIDWithChannelNameWith( self, sChannelName ):
  uiAUXAssign = 0
  if( sChannelName == "Baro"        ): uiAUXAssign = -9
  if( sChannelName == "Pressure"    ): uiAUXAssign = -8
  if( sChannelName == "ORP"         ): uiAUXAssign = -7
  if( sChannelName == "pH"          ): uiAUXAssign = -6
  if( sChannelName == "pH"          ): uiAUXAssign = -5
  if( sChannelName == "DO"          ): uiAUXAssign = -4
  if( sChannelName == "DO"          ): uiAUXAssign = -3
  if( sChannelName == "EC"          ): uiAUXAssign = -2
  if( sChannelName == "Temperature" ): uiAUXAssign = -1
  if( sChannelName == "EMPTY"       ): uiAUXAssign = 0
  if( sChannelName == "Ammonium"    ): uiAUXAssign = 1
  if( sChannelName == "Chloride"    ): uiAUXAssign = 2
  if( sChannelName == "Fluoride"    ): uiAUXAssign = 3
  if( sChannelName == "Nitrate"     ): uiAUXAssign = 4
  if( sChannelName == "Calcium"     ): uiAUXAssign = 5
  if( sChannelName == "Turbidity"   ): uiAUXAssign = 16
  if( sChannelName == "Chlorophyll" ): uiAUXAssign = 17
  if( sChannelName == "BGA-PC"      ): uiAUXAssign = 18
  if( sChannelName == "BGA-PE"      ): uiAUXAssign = 19
  if( sChannelName == "Rhodamine"   ): uiAUXAssign = 20
  if( sChannelName == "Fluorescein" ): uiAUXAssign = 21
  if( sChannelName == "Refined Oil" ): uiAUXAssign = 22
  if( sChannelName == "CDOM"        ): uiAUXAssign = 23
  if( sChannelName == "Crude Oil"   ): uiAUXAssign = 24
  if( sChannelName == "Tryptophan"  ): uiAUXAssign = 25
  if( sChannelName == "Amonnia"     ): uiAUXAssign = 254
  return( int(uiAUXAssign) )

 #-------------------------------------
 # Type de sonde selon l'ID
 #-------------------------------------
 def sFGetProductNameWithID( self, uiProductID ):
  sProductName = "EMPTY"
  if( uiProductID == 53 ):  sProductName = "AquaPlus"
  if( uiProductID == 30 ):  sProductName = "AP-Lite"
  if( uiProductID == 40 ):  sProductName = "AP-700"
  if( uiProductID == 50 ):  sProductName = "AP-800"
  if( uiProductID == 60 ):  sProductName = "AP-700-D"
  if( uiProductID == 70 ):  sProductName = "AP-800-D"
  if( uiProductID == 10 ):  sProductName = "AS-2000"
  if( uiProductID == 20 ):  sProductName = "AS-2000"
  if( uiProductID == 59 ):  sProductName = "AS-5000"
  if( uiProductID == 29 ):  sProductName = "AS-6K/7K/Pro"
  return( sProductName )

 #-------------------------------------
 # ID avec type de la sonde
 #-------------------------------------
 def uiFGetIDWithProductName( self, sProductName ):
  uiProductID = 0
  if( sProductName == "EMPTY"        ):  uiProductID = 0
  if( sProductName == "AquaPlus"     ):  uiProductID = 53
  if( sProductName == "AP-Lite"      ):  uiProductID = 30
  if( sProductName == "AP-700"       ):  uiProductID = 40
  if( sProductName == "AP-800"       ):  uiProductID = 50
  if( sProductName == "AP-700-D"     ):  uiProductID = 60
  if( sProductName == "AP-800-D"     ):  uiProductID = 70
  #if( sProductName == "AS-2000"      ):  uiProductID = 10
  if( sProductName == "AS-2000"      ):  uiProductID = 20
  if( sProductName == "AS-5000"      ):  uiProductID = 59
  if( sProductName == "AS-6K/7K/Pro" ):  uiProductID = 29
  return( int( uiProductID ) )

 #-------------------------------------
 # Nombre d'AUX selon l'ID
 #-------------------------------------
 def sFGetAUXNumberWithID( self, uiProductID ):
  sProductName = "EMPTY"
  if( uiProductID == 10 ): uiAUXNumber = 2 # AS-2000
  if( uiProductID == 20 ): uiAUXNumber = 2 # AS-2000-D
  if( uiProductID == 59 ): uiAUXNumber = 4 # AS-5000
  if( uiProductID == 29 ): uiAUXNumber = 6 # AS-6K/7K/Pro
  return( uiAUXNumber )

 #-------------------------------------
 # Nom de la voie le log sensor
 #-------------------------------------
 def sFGetLogSensorNameWithIndex( self, uiLogSensor ):
  sName = "EMPTY"
  if( uiLogSensor == 0 ):  sName = "Temperature"
  if( uiLogSensor == 2 ):  sName = "Depth"
  if( uiLogSensor == 4 ):  sName = "pH"
  if( uiLogSensor == 5 ):  sName = "ORP"
  if( uiLogSensor == 6 ):  sName = "DO"
  if( uiLogSensor == 7 ):  sName = "EC"
  if( uiLogSensor == 8 ):  sName = "AUX1"
  if( uiLogSensor == 9 ):  sName = "AUX2"
  if( uiLogSensor == 10 ): sName = "AUX3"
  if( uiLogSensor == 11 ): sName = "AUX4"
  if( uiLogSensor == 12 ): sName = "AUX5"
  if( uiLogSensor == 13 ): sName = "AUX6"
  if( uiLogSensor == 14 ): sName = "AUX7"
  return( sName )

 #-------------------------------------
 # Nom de la voie le log sensor
 #-------------------------------------
 def uiFGetIndexWithLogSensorName( self, sName ):
  uiLogSensor = 0
  if( sName == "Temperature" ): uiLogSensor = 0
  if( sName == "Depth"       ): uiLogSensor = 2
  if( sName == "pH"          ): uiLogSensor = 4
  if( sName == "ORP"         ): uiLogSensor = 5
  if( sName == "DO"          ): uiLogSensor = 6
  if( sName == "EC"          ): uiLogSensor = 7
  if( sName == "AUX1"        ): uiLogSensor = 8
  if( sName == "AUX2"        ): uiLogSensor = 9
  if( sName == "AUX3"        ): uiLogSensor = 10
  if( sName == "AUX4"        ): uiLogSensor = 11
  if( sName == "AUX5"        ): uiLogSensor = 12
  if( sName == "AUX6"        ): uiLogSensor = 13
  if( sName == "AUX7"        ): uiLogSensor = 14
  return( uiLogSensor )

 #-------------------------------------
 # Calcul de l'estimatif d'autonomie
 #-------------------------------------
 def uiFLifetimeCalculation( self, ttConfig ):
  # Récupération des paramètres de la configuration
  sModel       = ttConfig["PRODUCT"]["sModel"]
  uiAux1Assign = ttConfig["SENSOR"]["AUX1"]["uiIndex"]
  uiAux2Assign = ttConfig["SENSOR"]["AUX2"]["uiIndex"]
  uiAux3Assign = ttConfig["SENSOR"]["AUX3"]["uiIndex"]
  uiAux4Assign = ttConfig["SENSOR"]["AUX4"]["uiIndex"]
  uiAux5Assign = ttConfig["SENSOR"]["AUX5"]["uiIndex"]
  uiAux6Assign = ttConfig["SENSOR"]["AUX6"]["uiIndex"]
  uiBattPC     = ttConfig["PRODUCT"]["uiBATT_PC"]
  uiLogSec     = ttConfig["PRODUCT"]["uiLOG_SEC"]
  uiLogMin     = ttConfig["PRODUCT"]["uiLOG_MIN"]
  uiLogHour    = ttConfig["PRODUCT"]["uiLOG_HOUR"]
  uiEventHour  = ttConfig["PRODUCT"]["uiEVENT_HOUR"]
  uiEventMin   = ttConfig["PRODUCT"]["uiEVENT_MIN"]
  uiCleanHour  = ttConfig["PRODUCT"]["uiCLEAN_HR"]
  uiLogEvent   = ttConfig["PRODUCT"]["uiLOG_EVENT"]

  # Si AS-2000 ou AS-2000-D
  if( ( sModel == "AS-2000" ) or ( sModel == "AS-2000-D" ) ):
   uiBattmAh = 5500
  else:
   uiBattmAh = 12500
  # Calcul capacité batterie restante
  uiBattmAhRemaining = uiBattmAh * (uiBattPC / 100)
  # Durée acquisition en sec
  uiLogDataInterval  = ( ( uiLogHour * 60 + uiLogMin ) * 60 ) + uiLogSec
  print("uiLogDataInterval = %d"%uiLogDataInterval)

  # Si Event log activé
  if( uiLogEvent == 1 ):
   uiLogEventSec = ( ( uiEventHour * 60 ) + uiEventMin * 60 )
   if( uiLogEventSec == 0 ): uiLogEventSec = 60
   print("uiLogEventSec = %d"%uiLogEventSec)
   # Si cadence event est supérieure à la cadence d'acquisition normal
   if( uiLogEventSec < uiLogDataInterval ): uiLogDataInterval = uiLogEventSec

  uiLogDataDuration = 20
  if( uiAux1Assign > 16 ): uiLogDataDuration = 40
  if( uiAux2Assign > 16 ): uiLogDataDuration = 40
  if( uiAux3Assign > 16 ): uiLogDataDuration = 40
  if( uiAux4Assign > 16 ): uiLogDataDuration = 40
  if( uiAux5Assign > 16 ): uiLogDataDuration = 40
  if( uiAux6Assign > 16 ): uiLogDataDuration = 40

  # Durée balayage
  uiCleanInterval  = uiCleanHour * 3600
  uiCleanDuration  = 3

  if( sModel == "AS-2000" ):      uiLogDataCurrent = 40
  if( sModel == "AS-5000" ):      uiLogDataCurrent = 54
  if( sModel == "AS-6K/7K/Pro" ): uiLogDataCurrent = 54
  else:                           uiLogDataCurrent = 29

  if( uiAux1Assign > 15 ): uiLogDataCurrent = uiLogDataCurrent + 2
  if( uiAux2Assign > 15 ): uiLogDataCurrent = uiLogDataCurrent + 2
  if( uiAux3Assign > 15 ): uiLogDataCurrent = uiLogDataCurrent + 2
  if( uiAux4Assign > 15 ): uiLogDataCurrent = uiLogDataCurrent + 2
  if( uiAux5Assign > 15 ): uiLogDataCurrent = uiLogDataCurrent + 2
  if( uiAux6Assign > 15 ): uiLogDataCurrent = uiLogDataCurrent + 2

  if( uiAux1Assign == 22 or uiAux1Assign == 25 ): uiLogDataCurrent = uiLogDataCurrent + 15
  if( uiAux2Assign == 22 or uiAux2Assign == 25 ): uiLogDataCurrent = uiLogDataCurrent + 15
  if( uiAux3Assign == 22 or uiAux3Assign == 25 ): uiLogDataCurrent = uiLogDataCurrent + 15
  if( uiAux4Assign == 22 or uiAux4Assign == 25 ): uiLogDataCurrent = uiLogDataCurrent + 15
  if( uiAux5Assign == 22 or uiAux5Assign == 25 ): uiLogDataCurrent = uiLogDataCurrent + 15
  if( uiAux6Assign == 22 or uiAux6Assign == 25 ): uiLogDataCurrent = uiLogDataCurrent + 15

  # Calcul du ratio conso en mode acquisition
  fLogDataConsumption = (uiLogDataDuration / uiLogDataInterval) * uiLogDataCurrent
  fCleanConsumption = 0
  #
  if( sModel == "AS-6K/7K/Pro" ):
   # 300mA cleaning current
   fCleanConsumption = ( uiCleanDuration / uiCleanInterval ) * 300
  # 0.35mA sleep current
  fSleepConsumption = ( 1 - ( uiCleanDuration / 300 ) - (uiLogDataDuration / uiLogDataInterval) ) * 0.35
  #fSleepConsumption = ( 1 - (uiLogDataDuration / uiLogDataInterval) - ( uiCleanDuration / 300 ) ) * 0.35
  fAvgConsumption = fSleepConsumption + fCleanConsumption + fLogDataConsumption
  # Si à la seconde : la sonde ne passe pas en veille => tout le temps conso mesure + conso balai
  if( uiLogSec != 0 ): fAvgConsumption = uiLogDataCurrent + fCleanConsumption
  # Calcul de la durée de vie en jours
  uiBattDayLife = ( uiBattmAhRemaining / fAvgConsumption ) / 24
  # Retour du nombre de jour sous forme entière
  return( int(uiBattDayLife) )





