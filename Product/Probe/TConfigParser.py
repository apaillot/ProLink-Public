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
  ttConfig["SENSOR"]["DO Sat"] = {}
  ttConfig["SENSOR"]["PH"]     = {}
  ttConfig["SENSOR"]["PHmv"]   = {}
  ttConfig["SENSOR"]["ORP"]    = {}
  ttConfig["SENSOR"]["Depth"]  = {}
  ttConfig["SENSOR"]["Baro"]   = {}
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
  ttConfig["CALCULATED"]["AMMONIA"]  = {}
  ttConfig["CALCULATED"]["EC"]       = {}
  ttConfig["CALCULATED"]["TEMP"]     = {}
  ttConfig["CALCULATED"]["DEPTH"]    = {}
  ttConfig["CALCULATED"]["Salinity"] = {}
  ttConfig["CALCULATED"]["SSG"]      = {}
  ttConfig["CALCULATED"]["TDS"]      = {}
  # Choix unité
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
  ttConfig["SENSOR"]["AUX1"  ]["uiIndex"] = 0
  ttConfig["SENSOR"]["AUX2"  ]["uiIndex"] = 0
  ttConfig["SENSOR"]["AUX3"  ]["uiIndex"] = 0
  ttConfig["SENSOR"]["AUX4"  ]["uiIndex"] = 0
  ttConfig["SENSOR"]["AUX5"  ]["uiIndex"] = 0
  ttConfig["SENSOR"]["AUX6"  ]["uiIndex"] = 0
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
  # Résultat de mesure
  ttConfig["SENSOR"]["TEMP"]["fResult"]   = 0
  ttConfig["SENSOR"]["EC"]["fResult"]     = 0
  ttConfig["SENSOR"]["DO"]["fResult"]     = 0
  ttConfig["SENSOR"]["DO Sat"]["fResult"] = 0
  ttConfig["SENSOR"]["PH"]["fResult"]     = 0
  ttConfig["SENSOR"]["PHmv"]["fResult"]   = 0
  ttConfig["SENSOR"]["ORP"]["fResult"]    = 0
  ttConfig["SENSOR"]["Depth"]["fResult"]  = 0
  ttConfig["SENSOR"]["AUX1"]["fResult"]   = 0
  ttConfig["SENSOR"]["AUX2"]["fResult"]   = 0
  ttConfig["SENSOR"]["AUX3"]["fResult"]   = 0
  ttConfig["SENSOR"]["AUX4"]["fResult"]   = 0
  ttConfig["SENSOR"]["AUX5"]["fResult"]   = 0
  ttConfig["SENSOR"]["AUX6"]["fResult"]   = 0
  ttConfig["SENSOR"]["AUX7"]["fResult"]   = 0
  # Evolution
  ttConfig["SENSOR"]["AUX1"]["iTrend"] = 0
  ttConfig["SENSOR"]["AUX2"]["iTrend"] = 0
  ttConfig["SENSOR"]["AUX3"]["iTrend"] = 0
  ttConfig["SENSOR"]["AUX4"]["iTrend"] = 0
  ttConfig["SENSOR"]["AUX5"]["iTrend"] = 0
  ttConfig["SENSOR"]["AUX6"]["iTrend"] = 0
  ttConfig["SENSOR"]["AUX7"]["iTrend"] = 0
  # Etat d'activation
  ttConfig["SENSOR"]["TEMP"  ]["bActivated"] = False
  ttConfig["SENSOR"]["EC"    ]["bActivated"] = False
  ttConfig["SENSOR"]["DO"    ]["bActivated"] = False
  ttConfig["SENSOR"]["DO Sat"]["bActivated"] = False
  ttConfig["SENSOR"]["PH"    ]["bActivated"] = False
  ttConfig["SENSOR"]["PHmv"  ]["bActivated"] = False
  ttConfig["SENSOR"]["ORP"   ]["bActivated"] = False
  ttConfig["SENSOR"]["Depth" ]["bActivated"] = False
  ttConfig["SENSOR"]["Baro"  ]["bActivated"] = False
  ttConfig["SENSOR"]["AUX1"  ]["bActivated"] = False
  ttConfig["SENSOR"]["AUX2"  ]["bActivated"] = False
  ttConfig["SENSOR"]["AUX3"  ]["bActivated"] = False
  ttConfig["SENSOR"]["AUX4"  ]["bActivated"] = False
  ttConfig["SENSOR"]["AUX5"  ]["bActivated"] = False
  ttConfig["SENSOR"]["AUX6"  ]["bActivated"] = False
  ttConfig["SENSOR"]["AUX7"  ]["bActivated"] = False
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
  # Valeur par défaut
  ttConfig["SENSOR"]["Baro"]["fResult"]  = 1013
  ttConfig["SENSOR"]["EC"]["bSC35_flag"] = False

 #--------------------------
 # Extraction des champs Setup Data
 #--------------------------
 def ttFParseSerialNumber( self, sDataRead, ttConfig ):
  print("-- ttFParseSerialNumber --")
  print("len(sDataRead) = %d"%len(sDataRead))
  #
  txUnpacked = struct.unpack( '>9B3B1B', sDataRead )
  print(txUnpacked)
  uiCpt = 0

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
  uiCRC       = txUnpacked[uiCpt]; uiCpt+=1

  sPSN1 = str(uiPSN1)+str(uiPSN2)+str(uiPSN3)+str(uiPSN4)+str(uiPSN5)+str(uiPSN6)+str(uiPSN7)+str(uiPSN8)+str(uiPSN9)
  uiModel = int( str(uiPSN8) + "" + str(uiPSN9) )
  print("Model: %u"% uiModel )
  ttConfig["PRODUCT"]["sPSN1"]   = sPSN1
  ttConfig["PRODUCT"]["uiModel"] = uiModel
  sModel = self.sFGetProductNameWithID(uiModel)
  ttConfig["PRODUCT"]["sModel"]      = sModel
  ttConfig["PRODUCT"]["uiAUXNumber"] = self.sFGetAUXNumberWithID(uiModel)

  """
  uiFWR1       = txUnpacked[uiCpt]; uiCpt+=1
  uiFWR2       = txUnpacked[uiCpt]; uiCpt+=1
  uiFWR3       = txUnpacked[uiCpt]; uiCpt+=1
  """
  #sPSW1        = str(uiPSW1)+"."+str(uiPSW2)+str(uiPSW3)+"."+str(uiFWR1)+"."+str(uiFWR2)+str(uiFWR3)
  sPSW1 = str(uiPSW1)+"."+str(uiPSW2)+str(uiPSW3)
  uiPSW = int(str(uiPSW1)+str(uiPSW2)+str(uiPSW3))
  ttConfig["PRODUCT"]["uiPSW1"] = uiPSW1
  ttConfig["PRODUCT"]["uiPSW2"] = uiPSW2
  ttConfig["PRODUCT"]["uiPSW3"] = uiPSW3
  ttConfig["PRODUCT"]["uiPSW"]  = uiPSW
  ttConfig["PRODUCT"]["sPSW1"]  = sPSW1

  ttConfig["PRODUCT"]["ProBE_SW"] = 0
  # Envoi 0xD0 0x01
  if(  (  ( ( uiPSW1 == 3 ) and ( uiPSW2 >= 5 ) )
       or ( ( uiPSW1 == 4 ) and ( uiPSW2 == 0 ) and ( uiPSW3 < 7 ) ) ) ):
   ttConfig["PRODUCT"]["ProBE_SW"] = 1
  # Envoi 0xD0 0x02
  if( ( uiPSW1 == 4 ) and ( uiPSW2 >= 1 ) ):
   ttConfig["PRODUCT"]["ProBE_SW"] = 2
  # Envoi 0xD0 0x03
  if(  (  ( ( uiPSW1 == 4 ) and ( uiPSW2 == 0 ) and ( uiPSW3 > 6 ) )
       or ( ( uiPSW1 >= 5 ) ) ) ):
   ttConfig["PRODUCT"]["ProBE_SW"] = 3

  # Probe type
  ttConfig["PRODUCT"]["uiProbeType"] = self.uiFGetProbeTypeWithID( ttConfig["PRODUCT"]["uiModel"] )

  # Retourne la configuration
  return( ttConfig )

 #------------------------------------------------------------------------------
 # Extraction des champs Calibration Data AquaPlus
 #------------------------------------------------------------------------------
 def ttFParseCalibrationDataAquaPlus( self, sDataRead, ttConfig ):
  print("-- ttFParseCalibrationDataAquaPlus --")
  print(sDataRead)
  # Decryptage de la donnée binaire => "<" LSB first
  # B : unsigned char (1 Byte)
  # H : unsigned short (2 Byte)
  txUnpacked = struct.unpack( "<28B", sDataRead )
  print(txUnpacked)
  uiCpt = 12 # 13
  # Extraction des champs
  uiEC_Flag    = txUnpacked[uiCpt]; uiCpt+=1
  uiCpt = 18
  uiDO100_Day   = txUnpacked[uiCpt]; uiCpt+=1
  uiDO100_Month = txUnpacked[uiCpt]; uiCpt+=1
  uiDO100_Year  = txUnpacked[uiCpt]; uiCpt+=1
  uiDO0_Day     = txUnpacked[uiCpt]; uiCpt+=1
  uiDO0_Month   = txUnpacked[uiCpt]; uiCpt+=1
  uiDO0_Year    = txUnpacked[uiCpt]; uiCpt+=1
  uiEC_Day      = txUnpacked[uiCpt]; uiCpt+=1
  uiEC_Month    = txUnpacked[uiCpt]; uiCpt+=1
  uiEC_Year     = txUnpacked[uiCpt]; uiCpt+=1

  print("uiEC_Flag = %d"%uiEC_Flag)

  # EC calibration standard
  if( ( uiEC_Flag & 0x0F ) == 0 ): sECCalValue = "RapidCal"
  # EC_STD_BOX
  if( ttConfig["PRODUCT"]["ProBE_SW"] < 3 ):
   if( ( uiEC_Flag & 0x0F ) == 1 ): sECCalValue = "RapidCal"
   if( ( uiEC_Flag & 0x0F ) == 2 ): sECCalValue = "1413 uS"
   if( ( uiEC_Flag & 0x0F ) == 4 ): sECCalValue = "12,880 uS"
   if( ( uiEC_Flag & 0x0F ) >  4 ): sECCalValue = "SC-35"
   if( ( uiEC_Flag & 0x0F ) >  4 ): bEC_SC35_flag = True
   else:                            bEC_SC35_flag = False
  # EC_STD_BOX_V5
  if( ttConfig["PRODUCT"]["ProBE_SW"] == 3 ):
   if( ( uiEC_Flag & 0x0F ) == 1 ): sECCalValue = "RapidCal"
   if( ( uiEC_Flag & 0x0F ) == 2 ): sECCalValue = "User"
   if( ( uiEC_Flag & 0x0F ) >  4 ): sECCalValue = "SC-35"
   if( ( uiEC_Flag & 0x0F ) >  4 ): bEC_SC35_flag = True
   else:                            bEC_SC35_flag = False
  # AQUAPLUS_EC_BOX
  if(   ( ttConfig["PRODUCT"]["uiModel"] == 53 )
    and ( ttConfig["PRODUCT"]["uiPSW1"]  ==  3 )
    and ( ttConfig["PRODUCT"]["uiPSW2"]  >=  1 ) ):
   if( ( uiEC_Flag & 0x0F ) == 1 ): sECCalValue = "RapidCal"
   if( ( uiEC_Flag & 0x0F ) == 2 ): sECCalValue = "1413 uS"
   if( ( uiEC_Flag & 0x0F ) >= 4 ): sECCalValue = "SC-35"
   if( ( uiEC_Flag & 0x0F ) >= 4 ): bEC_SC35_flag = True
   else:                            bEC_SC35_flag = False

  # DO
  ttConfig["SENSOR"]["DO"]["ucPoint"] = 2
  ttConfig["SENSOR"]["DO"]["Point"][0]["sName"]          = tCalibChannelInfo["DO"]["Point"][0]["sName"]
  ttConfig["SENSOR"]["DO"]["Point"][0]["sCalReportUnit"] = tCalibChannelInfo["DO"]["Point"][0]["sCalReportUnit"]
  ttConfig["SENSOR"]["DO"]["Point"][0]["uiDay"]          = uiDO0_Day
  ttConfig["SENSOR"]["DO"]["Point"][0]["uiMonth"]        = uiDO0_Month
  ttConfig["SENSOR"]["DO"]["Point"][0]["uiYear"]         = uiDO0_Year
  ttConfig["SENSOR"]["DO"]["Point"][1]["sName"]          = tCalibChannelInfo["DO"]["Point"][1]["sName"]
  ttConfig["SENSOR"]["DO"]["Point"][1]["sCalReportUnit"] = tCalibChannelInfo["DO"]["Point"][1]["sCalReportUnit"]
  ttConfig["SENSOR"]["DO"]["Point"][1]["uiDay"]          = uiDO100_Day
  ttConfig["SENSOR"]["DO"]["Point"][1]["uiMonth"]        = uiDO100_Month
  ttConfig["SENSOR"]["DO"]["Point"][1]["uiYear"]         = uiDO100_Year

  # EC
  ttConfig["SENSOR"]["EC"]["ucPoint"] = 1
  ttConfig["SENSOR"]["EC"]["sCalValue"]      = sECCalValue
  #ttConfig["SENSOR"]["EC"]["uiUserCalValue"] = uiEC_UserCalValue
  ttConfig["SENSOR"]["EC"]["bSC35_flag"]     = bEC_SC35_flag
  #ttConfig["SENSOR"]["EC"]["uiUserCalValue"] = uiEC_UserCalValue
  ttConfig["SENSOR"]["EC"]["Point"][0]["sName"]          = tCalibChannelInfo["EC"]["Point"][0]["sName"]
  ttConfig["SENSOR"]["EC"]["Point"][0]["sCalReportUnit"] = tCalibChannelInfo["EC"]["Point"][0]["sCalReportUnit"]
  ttConfig["SENSOR"]["EC"]["Point"][0]["uiDay"]          = uiEC_Day
  ttConfig["SENSOR"]["EC"]["Point"][0]["uiMonth"]        = uiEC_Month
  ttConfig["SENSOR"]["EC"]["Point"][0]["uiYear"]         = uiEC_Year
  #ttConfig["SENSOR"]["EC"]["Point"][0]["uiCalValueRef"]  = 229 if( ( uiORP_Month & 0x80 ) == 0x80 ) else 250

  # Etat d'activation
  ttConfig["SENSOR"]["TEMP"  ]["bActivated"] = True
  ttConfig["SENSOR"]["EC"    ]["bActivated"] = True
  ttConfig["SENSOR"]["DO"    ]["bActivated"] = True
  ttConfig["SENSOR"]["DO Sat"]["bActivated"] = True
  ttConfig["SENSOR"]["PH"    ]["bActivated"] = False
  ttConfig["SENSOR"]["PHmv"  ]["bActivated"] = False
  ttConfig["SENSOR"]["ORP"   ]["bActivated"] = False
  ttConfig["SENSOR"]["Depth" ]["bActivated"] = False
  ttConfig["SENSOR"]["Baro"  ]["bActivated"] = True
  ttConfig["SENSOR"]["AUX1"  ]["bActivated"] = False
  ttConfig["SENSOR"]["AUX2"  ]["bActivated"] = False
  ttConfig["SENSOR"]["AUX3"  ]["bActivated"] = False
  ttConfig["SENSOR"]["AUX4"  ]["bActivated"] = False
  ttConfig["SENSOR"]["AUX5"  ]["bActivated"] = False
  ttConfig["SENSOR"]["AUX6"  ]["bActivated"] = False
  ttConfig["SENSOR"]["AUX7"  ]["bActivated"] = False
  ttConfig["SENSOR"]["AUX1"]["sIndex"]   = "EMPTY"
  ttConfig["SENSOR"]["AUX2"]["sIndex"]   = "EMPTY"
  ttConfig["SENSOR"]["AUX3"]["sIndex"]   = "EMPTY"
  ttConfig["SENSOR"]["AUX4"]["sIndex"]   = "EMPTY"
  ttConfig["SENSOR"]["AUX5"]["sIndex"]   = "EMPTY"
  ttConfig["SENSOR"]["AUX6"]["sIndex"]   = "EMPTY"
  ttConfig["SENSOR"]["AUX7"]["sIndex"]   = "EMPTY"

  # Retour de la config
  return( ttConfig )

 #------------------------------------------------------------------------------
 # Extraction des champs Calibration Data
 #------------------------------------------------------------------------------
 def ttFParseCalibrationDataAPLite( self, sDataRead, ttConfig ):
  print("-- ttFParseCalibrationDataAPLite --")
  print(sDataRead)
  # Decryptage de la donnée binaire => "<" LSB first
  # B : unsigned char (1 Byte)
  # H : unsigned short (2 Byte)
  txUnpacked = struct.unpack( "<73B 6B 6H 9B B", sDataRead )
  print(txUnpacked)
  uiCpt = 19
  # Extraction des champs
  uiAUX1_P1_Day    = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX1_P1_Month  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX1_P1_Year   = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX1_P2_Day    = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX1_P2_Month  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX1_P2_Year   = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX1_P3_Day    = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX1_P3_Month  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX1_P3_Year   = txUnpacked[uiCpt]; uiCpt+=1
  uiCpt = 73
  # Assignement
  uiAUX1_Assign  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX2_Assign  = 0; uiCpt+=1
  uiAUX3_Assign  = 0; uiCpt+=1
  uiAUX4_Assign  = 0; uiCpt+=1
  uiAUX5_Assign  = 0; uiCpt+=1
  uiAUX6_Assign  = 0; uiCpt+=1
  sAUX1_Assign   = self.sFGetChannelNameWithID(uiAUX1_Assign)
  sAUX2_Assign   = self.sFGetChannelNameWithID(uiAUX2_Assign)
  sAUX3_Assign   = self.sFGetChannelNameWithID(uiAUX3_Assign)
  sAUX4_Assign   = self.sFGetChannelNameWithID(uiAUX4_Assign)
  sAUX5_Assign   = self.sFGetChannelNameWithID(uiAUX5_Assign)
  sAUX6_Assign   = self.sFGetChannelNameWithID(uiAUX6_Assign)
  # Grab sample factor
  uiAUX1_GS  = txUnpacked[uiCpt]; uiCpt+=1
  uiAUX2_GS  = 0; uiCpt+=1
  uiAUX3_GS  = 0; uiCpt+=1
  uiAUX4_GS  = 0; uiCpt+=1
  uiAUX5_GS  = 0; uiCpt+=1
  uiAUX6_GS  = 0; uiCpt+=1

  ttConfig["SENSOR"]["AUX1"]["uiIndex"]  = uiAUX1_Assign
  ttConfig["SENSOR"]["AUX2"]["uiIndex"]  = uiAUX2_Assign
  ttConfig["SENSOR"]["AUX3"]["uiIndex"]  = uiAUX3_Assign
  ttConfig["SENSOR"]["AUX4"]["uiIndex"]  = uiAUX4_Assign
  ttConfig["SENSOR"]["AUX5"]["uiIndex"]  = uiAUX5_Assign
  ttConfig["SENSOR"]["AUX6"]["uiIndex"]  = uiAUX6_Assign
  ttConfig["SENSOR"]["AUX7"]["uiIndex"]  = 254
  ttConfig["SENSOR"]["AUX1"]["sIndex"]   = self.sFGetChannelNameWithID(uiAUX1_Assign)
  ttConfig["SENSOR"]["AUX2"]["sIndex"]   = self.sFGetChannelNameWithID(uiAUX2_Assign)
  ttConfig["SENSOR"]["AUX3"]["sIndex"]   = self.sFGetChannelNameWithID(uiAUX3_Assign)
  ttConfig["SENSOR"]["AUX4"]["sIndex"]   = self.sFGetChannelNameWithID(uiAUX4_Assign)
  ttConfig["SENSOR"]["AUX5"]["sIndex"]   = self.sFGetChannelNameWithID(uiAUX5_Assign)
  ttConfig["SENSOR"]["AUX6"]["sIndex"]   = self.sFGetChannelNameWithID(uiAUX6_Assign)
  ttConfig["SENSOR"]["AUX7"]["sIndex"]   = self.sFGetChannelNameWithID(254)
  # Unité
  ttConfig["SENSOR"]["AUX1"]["sUnit"]   = self.sFGetChannelUnitWithID(uiAUX1_Assign)
  ttConfig["SENSOR"]["AUX2"]["sUnit"]   = self.sFGetChannelUnitWithID(uiAUX2_Assign)
  ttConfig["SENSOR"]["AUX3"]["sUnit"]   = self.sFGetChannelUnitWithID(uiAUX3_Assign)
  ttConfig["SENSOR"]["AUX4"]["sUnit"]   = self.sFGetChannelUnitWithID(uiAUX4_Assign)
  ttConfig["SENSOR"]["AUX5"]["sUnit"]   = self.sFGetChannelUnitWithID(uiAUX5_Assign)
  ttConfig["SENSOR"]["AUX6"]["sUnit"]   = self.sFGetChannelUnitWithID(uiAUX6_Assign)
  ttConfig["SENSOR"]["AUX7"]["sUnit"]   = self.sFGetChannelUnitWithID(254)

  print("sAUX1_Assign = "+sAUX1_Assign)
  print("uiAUX1_P1_Day = %u"%uiAUX1_P1_Day)

  # AUX1
  if( sAUX1_Assign != "EMPTY" ):
   ttConfig["SENSOR"]["AUX1"]["ucPoint"] = tCalibChannelInfo[sAUX1_Assign]["ucPoint"]
   ttConfig["SENSOR"]["AUX1"]["Point"][0]["sName"]          = tCalibChannelInfo[sAUX1_Assign]["Point"][0]["sName"]
   ttConfig["SENSOR"]["AUX1"]["Point"][0]["sCalReportUnit"] = tCalibChannelInfo[sAUX1_Assign]["Point"][0]["sCalReportUnit"]
   ttConfig["SENSOR"]["AUX1"]["Point"][0]["uiDay"]          = uiAUX1_P1_Day
   ttConfig["SENSOR"]["AUX1"]["Point"][0]["uiMonth"]        = uiAUX1_P1_Month
   ttConfig["SENSOR"]["AUX1"]["Point"][0]["uiYear"]         = uiAUX1_P1_Year
   ##ttConfig["SENSOR"]["AUX1"]["Point"][0]["uiCalReport"]    = ( ( uiAUX1_P1_CalReport & 0x7FFF ) * -1 ) if(uiAUX1_P1_CalReport & 0x8000) else uiAUX1_P1_CalReport
   if( tCalibChannelInfo[sAUX1_Assign]["ucPoint"] > 1 ):
    ttConfig["SENSOR"]["AUX1"]["Point"][1]["sName"]          = tCalibChannelInfo[sAUX1_Assign]["Point"][1]["sName"]
    ttConfig["SENSOR"]["AUX1"]["Point"][1]["sCalReportUnit"] = tCalibChannelInfo[sAUX1_Assign]["Point"][1]["sCalReportUnit"]
    ttConfig["SENSOR"]["AUX1"]["Point"][1]["uiDay"]          = uiAUX1_P2_Day
    ttConfig["SENSOR"]["AUX1"]["Point"][1]["uiMonth"]        = uiAUX1_P2_Month
    ttConfig["SENSOR"]["AUX1"]["Point"][1]["uiYear"]         = uiAUX1_P2_Year
    ##ttConfig["SENSOR"]["AUX1"]["Point"][1]["uiCalReport"]    = ( ( uiAUX1_P2_CalReport & 0x7FFF ) * -1 ) if(uiAUX1_P2_CalReport & 0x8000) else uiAUX1_P2_CalReport
   if( tCalibChannelInfo[sAUX1_Assign]["ucPoint"] > 2 ):
    ttConfig["SENSOR"]["AUX1"]["Point"][2]["sName"]          = tCalibChannelInfo[sAUX1_Assign]["Point"][2]["sName"]
    ttConfig["SENSOR"]["AUX1"]["Point"][2]["sCalReportUnit"] = tCalibChannelInfo[sAUX1_Assign]["Point"][2]["sCalReportUnit"]
    ttConfig["SENSOR"]["AUX1"]["Point"][2]["uiDay"]          = uiAUX1_P3_Day
    ttConfig["SENSOR"]["AUX1"]["Point"][2]["uiMonth"]        = uiAUX1_P3_Month
    ttConfig["SENSOR"]["AUX1"]["Point"][2]["uiYear"]         = uiAUX1_P3_Year
    ##ttConfig["SENSOR"]["AUX1"]["Point"][2]["uiCalReport"]    = ( ( uiAUX1_P3_CalReport & 0x7FFF ) * -1 ) if(uiAUX1_P3_CalReport & 0x8000) else uiAUX1_P3_CalReport
  # GS
  ttConfig["SENSOR"]["AUX1"]["fGS"]        = uiAUX1_GS / 100

  # Test si voie calculée ammonia
  if(  ( uiAUX1_Assign == 0x01 )
    or ( uiAUX2_Assign == 0x01 )
    or ( uiAUX3_Assign == 0x01 )
    or ( uiAUX4_Assign == 0x01 )
    or ( uiAUX5_Assign == 0x01 )
    or ( uiAUX6_Assign == 0x01 ) ):
   # Ammonia
   ttConfig["CALCULATED"]["AMMONIA"]["bActivated"] = True
  # Pas de voie Ammonia
  else:
   ttConfig["CALCULATED"]["AMMONIA"]["bActivated"] = False

  # Etat d'activation
  ttConfig["SENSOR"]["TEMP"  ]["bActivated"] = True
  ttConfig["SENSOR"]["EC"    ]["bActivated"] = False
  ttConfig["SENSOR"]["DO"    ]["bActivated"] = False
  ttConfig["SENSOR"]["DO Sat"]["bActivated"] = False
  ttConfig["SENSOR"]["PH"    ]["bActivated"] = False
  ttConfig["SENSOR"]["PHmv"  ]["bActivated"] = False
  ttConfig["SENSOR"]["ORP"   ]["bActivated"] = False
  ttConfig["SENSOR"]["Depth" ]["bActivated"] = False
  ttConfig["SENSOR"]["Baro"  ]["bActivated"] = True
  ttConfig["SENSOR"]["AUX1"  ]["bActivated"] = True
  ttConfig["SENSOR"]["AUX2"  ]["bActivated"] = False
  ttConfig["SENSOR"]["AUX3"  ]["bActivated"] = False
  ttConfig["SENSOR"]["AUX4"  ]["bActivated"] = False
  ttConfig["SENSOR"]["AUX5"  ]["bActivated"] = False
  ttConfig["SENSOR"]["AUX6"  ]["bActivated"] = False
  ttConfig["SENSOR"]["AUX7"  ]["bActivated"] = False

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
  uiPH4_10_Day     = txUnpacked[uiCpt]; uiCpt+=1
  uiPH4_10_Month   = txUnpacked[uiCpt]; uiCpt+=1
  uiPH4_10_Year    = txUnpacked[uiCpt]; uiCpt+=1
  uiPH7_Day        = txUnpacked[uiCpt]; uiCpt+=1
  uiPH7_Month      = txUnpacked[uiCpt]; uiCpt+=1
  uiPH7_Year       = txUnpacked[uiCpt]; uiCpt+=1
  uiORP_Day        = txUnpacked[uiCpt]; uiCpt+=1
  uiORP_Month      = txUnpacked[uiCpt]; uiCpt+=1
  uiORP_Year       = txUnpacked[uiCpt]; uiCpt+=1
  uiCal_Param_10   = txUnpacked[uiCpt]; uiCpt+=1 # Plusieurs paramètres
  uiDO100_Day      = txUnpacked[uiCpt]; uiCpt+=1
  uiDO100_Month    = txUnpacked[uiCpt]; uiCpt+=1
  uiDO100_Year     = txUnpacked[uiCpt]; uiCpt+=1
  uiDO0_Day        = txUnpacked[uiCpt]; uiCpt+=1
  uiDO0_Month      = txUnpacked[uiCpt]; uiCpt+=1
  uiDO0_Year       = txUnpacked[uiCpt]; uiCpt+=1
  uiEC_Day         = txUnpacked[uiCpt]; uiCpt+=1
  uiEC_Month       = txUnpacked[uiCpt]; uiCpt+=1
  uiEC_Year        = txUnpacked[uiCpt]; uiCpt+=1
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

  # Activation des voies
  ttConfig["SENSOR"]["TEMP"  ]["bActivated"] = True
  ttConfig["SENSOR"]["EC"    ]["bActivated"] = True
  ttConfig["SENSOR"]["DO"    ]["bActivated"] = True
  ttConfig["SENSOR"]["DO Sat"]["bActivated"] = True
  ttConfig["SENSOR"]["PH"    ]["bActivated"] = True
  ttConfig["SENSOR"]["PHmv"  ]["bActivated"] = True
  ttConfig["SENSOR"]["ORP"   ]["bActivated"] = True
  # Si AP-700-D / AP-800-D / AP-2000-D / AP-5000 / AP-6K/7K/Pro
  if(  ( ttConfig["PRODUCT"]["uiModel"] == 60 )    # AP-700-D
    or ( ttConfig["PRODUCT"]["uiModel"] == 70 )    # AP-800-D
    or ( ttConfig["PRODUCT"]["uiModel"] == 20 )    # AP-2000-D
    or ( ttConfig["PRODUCT"]["uiModel"] == 59 )    # AP-5000
    or ( ttConfig["PRODUCT"]["uiModel"] == 29 ) ): # AP-6K/7K/Pro
   ttConfig["SENSOR"]["Depth" ]["bActivated"] = True
  else:
   ttConfig["SENSOR"]["Depth" ]["bActivated"] = False
  ttConfig["SENSOR"]["Baro"  ]["bActivated"] = True
  ttConfig["SENSOR"]["AUX1"  ]["bActivated"] = False
  ttConfig["SENSOR"]["AUX2"  ]["bActivated"] = False
  ttConfig["SENSOR"]["AUX3"  ]["bActivated"] = False
  ttConfig["SENSOR"]["AUX4"  ]["bActivated"] = False
  ttConfig["SENSOR"]["AUX5"  ]["bActivated"] = False
  ttConfig["SENSOR"]["AUX6"  ]["bActivated"] = False

  ttConfig["SENSOR"]["AUX1"]["uiIndex"]  = uiAUX1_Assign
  ttConfig["SENSOR"]["AUX2"]["uiIndex"]  = uiAUX2_Assign
  ttConfig["SENSOR"]["AUX3"]["uiIndex"]  = uiAUX3_Assign
  ttConfig["SENSOR"]["AUX4"]["uiIndex"]  = uiAUX4_Assign
  ttConfig["SENSOR"]["AUX5"]["uiIndex"]  = uiAUX5_Assign
  ttConfig["SENSOR"]["AUX6"]["uiIndex"]  = uiAUX6_Assign
  ttConfig["SENSOR"]["AUX7"]["uiIndex"]  = 254
  ttConfig["SENSOR"]["AUX1"]["sIndex"]   = self.sFGetChannelNameWithID(uiAUX1_Assign)
  ttConfig["SENSOR"]["AUX2"]["sIndex"]   = self.sFGetChannelNameWithID(uiAUX2_Assign)
  ttConfig["SENSOR"]["AUX3"]["sIndex"]   = self.sFGetChannelNameWithID(uiAUX3_Assign)
  ttConfig["SENSOR"]["AUX4"]["sIndex"]   = self.sFGetChannelNameWithID(uiAUX4_Assign)
  ttConfig["SENSOR"]["AUX5"]["sIndex"]   = self.sFGetChannelNameWithID(uiAUX5_Assign)
  ttConfig["SENSOR"]["AUX6"]["sIndex"]   = self.sFGetChannelNameWithID(uiAUX6_Assign)
  ttConfig["SENSOR"]["AUX7"]["sIndex"]   = self.sFGetChannelNameWithID(254)
  # Unité
  ttConfig["SENSOR"]["AUX1"]["sUnit"]   = self.sFGetChannelUnitWithID(uiAUX1_Assign)
  ttConfig["SENSOR"]["AUX2"]["sUnit"]   = self.sFGetChannelUnitWithID(uiAUX2_Assign)
  ttConfig["SENSOR"]["AUX3"]["sUnit"]   = self.sFGetChannelUnitWithID(uiAUX3_Assign)
  ttConfig["SENSOR"]["AUX4"]["sUnit"]   = self.sFGetChannelUnitWithID(uiAUX4_Assign)
  ttConfig["SENSOR"]["AUX5"]["sUnit"]   = self.sFGetChannelUnitWithID(uiAUX5_Assign)
  ttConfig["SENSOR"]["AUX6"]["sUnit"]   = self.sFGetChannelUnitWithID(uiAUX6_Assign)
  ttConfig["SENSOR"]["AUX7"]["sUnit"]   = self.sFGetChannelUnitWithID(254)

  # AUX1
  if( sAUX1_Assign != "EMPTY" ):
   ttConfig["SENSOR"]["AUX1"]["bActivated"] = True
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
   ttConfig["SENSOR"]["AUX2"]["bActivated"] = True
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
   ttConfig["SENSOR"]["AUX3"]["bActivated"] = True
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
   ttConfig["SENSOR"]["AUX4"]["bActivated"] = True
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
   ttConfig["SENSOR"]["AUX5"]["bActivated"] = True
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
   ttConfig["SENSOR"]["AUX6"]["bActivated"] = True
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
  # Optical averaging constant
  ttConfig["PRODUCT"]["uiOpticalAvg"] = uiOpticalAvg

  # Test si voie calculée ammonia
  if(  ( uiAUX1_Assign == 0x01 )
    or ( uiAUX2_Assign == 0x01 )
    or ( uiAUX3_Assign == 0x01 )
    or ( uiAUX4_Assign == 0x01 )
    or ( uiAUX5_Assign == 0x01 )
    or ( uiAUX6_Assign == 0x01 ) ):
   # Ammonia
   ttConfig["CALCULATED"]["AMMONIA"]["bActivated"] = True
   ttConfig["SENSOR"]["AUX7"  ]["bActivated"] = True
  # Pas de voie Ammonia
  else:
   ttConfig["CALCULATED"]["AMMONIA"]["bActivated"] = False
   ttConfig["SENSOR"]["AUX7"  ]["bActivated"] = False

  # Retour de la config
  return( ttConfig )

 #--------------------------
 # Extraction des champs Measurement data
 #--------------------------
 def ttFParseCalibrationResult( self, sDataRead, ttConfig, uiCode ):
  print("-- ttFParseCalibrationResult --")
  print(sDataRead)
  print(uiCode)
  # Decryptage de la donnée binaire
  txUnpacked = struct.unpack( '>2B', sDataRead )
  print(txUnpacked)
  uiCpt = 0
  # Extraction des champs
  uiLSB = txUnpacked[uiCpt]; uiCpt+=1 #  0 -
  uiMSB = txUnpacked[uiCpt]; uiCpt+=1 #  1 -
  #
  print("uiMSB")
  print(uiMSB)
  print( "uiMSB = %d %s" % (uiMSB,hex(uiMSB)) )
  print( "uiLSB = %d %s" % (uiLSB,hex(uiLSB)) )
  uiNumber = uiLSB + ( uiMSB << 8 )
  print("uiNumber = %d"%uiNumber)
  #uiNumber = uiNumber / 1000

  # pH - Point 0 - 7.00
  if( uiCode == 221 ):  ttConfig["SENSOR"]["PH"]["Point"][0]["uiCalReport"] = uiNumber if( ( uiMSB >> 7 ) == 0 ) else -uiNumber
  # pH - Point 1 - 4.01
  if( uiCode == 220 ): ttConfig["SENSOR"]["PH"]["Point"][1]["uiCalReport"] = uiNumber
  # pH - Point 2 - 10.0
  if( uiCode == 219 ): ttConfig["SENSOR"]["PH"]["Point"][2]["uiCalReport"] = uiNumber
  # ORP - 250mV / ORP - 229 mV
  if(  ( uiCode == 217 )
    or ( uiCode == 216 ) ): ttConfig["SENSOR"]["ORP"]["Point"][0]["uiCalReport"] = uiNumber if( ( uiMSB >> 7 ) == 0 ) else -uiNumber
  # DO - Point 0 - Zéro
  if( uiCode == 222 ): ttConfig["SENSOR"]["DO"]["Point"][0]["uiCalReport"] = uiNumber / 1000
  # DO - Point 1 - 100%
  if( uiCode == 223 ): ttConfig["SENSOR"]["DO"]["Point"][1]["uiCalReport"] = uiNumber / 1000
  # EC
  if(  ( uiCode == 231 )
    or ( uiCode == 229 )
    or ( uiCode == 210 )
    or ( uiCode == 224 ) ): ttConfig["SENSOR"]["EC"]["Point"][0]["uiCalReport"] = uiNumber / 100

  # Si Tbd sur AP-800 : code différent
  if(  ( ttConfig["PRODUCT"]["uiModel"] == 50 )
    or ( ttConfig["PRODUCT"]["uiModel"] == 70 ) ):
   # AUX1 - P1 - AP-800 Tbd
   if( uiCode == 216 ): ttConfig["SENSOR"]["AUX1"]["Point"][0]["uiCalReport"] = uiNumber if( ( uiMSB >> 7 ) == 0 ) else -uiNumber
  else:
   # AUX1
   if( uiCode == 237 ): ttConfig["SENSOR"]["AUX1"]["Point"][0]["uiCalReport"] = uiNumber if( ( uiMSB >> 7 ) == 0 ) else -uiNumber
  if( uiCode == 238 ): ttConfig["SENSOR"]["AUX1"]["Point"][1]["uiCalReport"] = uiNumber if( ( uiMSB >> 7 ) == 0 ) else -uiNumber
  if( uiCode == 239 ): ttConfig["SENSOR"]["AUX1"]["Point"][2]["uiCalReport"] = uiNumber if( ( uiMSB >> 7 ) == 0 ) else -uiNumber
  # AUX2
  if( uiCode == 240 ): ttConfig["SENSOR"]["AUX2"]["Point"][0]["uiCalReport"] = uiNumber if( ( uiMSB >> 7 ) == 0 ) else -uiNumber
  if( uiCode == 241 ): ttConfig["SENSOR"]["AUX2"]["Point"][1]["uiCalReport"] = uiNumber if( ( uiMSB >> 7 ) == 0 ) else -uiNumber
  if( uiCode == 242 ): ttConfig["SENSOR"]["AUX2"]["Point"][2]["uiCalReport"] = uiNumber if( ( uiMSB >> 7 ) == 0 ) else -uiNumber
  # AUX3
  if( uiCode == 243 ): ttConfig["SENSOR"]["AUX3"]["Point"][0]["uiCalReport"] = uiNumber if( ( uiMSB >> 7 ) == 0 ) else -uiNumber
  if( uiCode == 244 ): ttConfig["SENSOR"]["AUX3"]["Point"][1]["uiCalReport"] = uiNumber if( ( uiMSB >> 7 ) == 0 ) else -uiNumber
  if( uiCode == 245 ): ttConfig["SENSOR"]["AUX3"]["Point"][2]["uiCalReport"] = uiNumber if( ( uiMSB >> 7 ) == 0 ) else -uiNumber
  # AUX4
  if( uiCode == 246 ): ttConfig["SENSOR"]["AUX4"]["Point"][0]["uiCalReport"] = uiNumber if( ( uiMSB >> 7 ) == 0 ) else -uiNumber
  if( uiCode == 247 ): ttConfig["SENSOR"]["AUX4"]["Point"][1]["uiCalReport"] = uiNumber if( ( uiMSB >> 7 ) == 0 ) else -uiNumber
  if( uiCode == 248 ): ttConfig["SENSOR"]["AUX4"]["Point"][2]["uiCalReport"] = uiNumber if( ( uiMSB >> 7 ) == 0 ) else -uiNumber
  # AUX5
  if( uiCode == 249 ): ttConfig["SENSOR"]["AUX5"]["Point"][0]["uiCalReport"] = uiNumber if( ( uiMSB >> 7 ) == 0 ) else -uiNumber
  if( uiCode == 250 ): ttConfig["SENSOR"]["AUX5"]["Point"][1]["uiCalReport"] = uiNumber if( ( uiMSB >> 7 ) == 0 ) else -uiNumber
  if( uiCode == 251 ): ttConfig["SENSOR"]["AUX5"]["Point"][2]["uiCalReport"] = uiNumber if( ( uiMSB >> 7 ) == 0 ) else -uiNumber
  # AUX6
  if( uiCode == 252 ): ttConfig["SENSOR"]["AUX6"]["Point"][0]["uiCalReport"] = uiNumber if( ( uiMSB >> 7 ) == 0 ) else -uiNumber
  if( uiCode == 253 ): ttConfig["SENSOR"]["AUX6"]["Point"][1]["uiCalReport"] = uiNumber if( ( uiMSB >> 7 ) == 0 ) else -uiNumber
  if( uiCode == 254 ): ttConfig["SENSOR"]["AUX6"]["Point"][2]["uiCalReport"] = uiNumber if( ( uiMSB >> 7 ) == 0 ) else -uiNumber

 #--------------------------
 # Extraction des champs Measurement data
 #--------------------------
 def ttFParseCalibrationResultReinit( self, ttConfig, uiCode ):
  print("-- ttFParseCalibrationResultReinit --")
  print(uiCode)
  print(id(ttConfig))

  print("----------------")
  print(ttConfig["SENSOR"]["DO"])
  print("----------------")
  print(ttConfig["SENSOR"]["DO"]["Point"][1])

  print("----------------")
  # pH - ORP
  if( uiCode == 211 ):
   if( "uiCalReport" in ttConfig["SENSOR"]["PH"]["Point"][0] ): ttConfig["SENSOR"]["PH"]["Point"][0].pop("uiCalReport")
   if( "uiCalReport" in ttConfig["SENSOR"]["PH"]["Point"][1] ): ttConfig["SENSOR"]["PH"]["Point"][1].pop("uiCalReport")
   if( "uiCalReport" in ttConfig["SENSOR"]["PH"]["Point"][2] ): ttConfig["SENSOR"]["PH"]["Point"][2].pop("uiCalReport")
   if( "uiCalReport" in ttConfig["SENSOR"]["ORP"]["Point"][0] ): ttConfig["SENSOR"]["ORP"]["Point"][0].pop("uiCalReport")
   if( "fTemp" in ttConfig["SENSOR"]["PH"]["Point"][0] ): ttConfig["SENSOR"]["PH"]["Point"][0].pop("fTemp")
   if( "fTemp" in ttConfig["SENSOR"]["PH"]["Point"][1] ): ttConfig["SENSOR"]["PH"]["Point"][1].pop("fTemp")
   if( "fTemp" in ttConfig["SENSOR"]["PH"]["Point"][2] ): ttConfig["SENSOR"]["PH"]["Point"][2].pop("fTemp")
   if( "fTemp" in ttConfig["SENSOR"]["ORP"]["Point"][0] ): ttConfig["SENSOR"]["ORP"]["Point"][0].pop("fTemp")
  # DO - EC
  if( uiCode == 213 ):
   if( "uiCalReport" in ttConfig["SENSOR"]["DO"]["Point"][0] ): ttConfig["SENSOR"]["DO"]["Point"][0].pop("uiCalReport")
   if( "uiCalReport" in ttConfig["SENSOR"]["DO"]["Point"][1] ): ttConfig["SENSOR"]["DO"]["Point"][1].pop("uiCalReport")
   if( "uiCalReport" in ttConfig["SENSOR"]["EC"]["Point"][0] ): ttConfig["SENSOR"]["EC"]["Point"][0].pop("uiCalReport")
   if( "fTemp" in ttConfig["SENSOR"]["DO"]["Point"][0] ): ttConfig["SENSOR"]["DO"]["Point"][0].pop("fTemp")
   if( "fTemp" in ttConfig["SENSOR"]["DO"]["Point"][1] ): ttConfig["SENSOR"]["DO"]["Point"][1].pop("fTemp")
   if( "fTemp" in ttConfig["SENSOR"]["EC"]["Point"][0] ): ttConfig["SENSOR"]["EC"]["Point"][0].pop("fTemp")
  # AUX1 - Point
  if( uiCode == 227 ):
   if( "uiCalReport" in ttConfig["SENSOR"]["AUX1"]["Point"][0] ): ttConfig["SENSOR"]["AUX1"]["Point"][0].pop("uiCalReport")
   if( "uiCalReport" in ttConfig["SENSOR"]["AUX1"]["Point"][1] ): ttConfig["SENSOR"]["AUX1"]["Point"][1].pop("uiCalReport")
   if( "uiCalReport" in ttConfig["SENSOR"]["AUX1"]["Point"][2] ): ttConfig["SENSOR"]["AUX1"]["Point"][2].pop("uiCalReport")
   if( "fTemp" in ttConfig["SENSOR"]["AUX1"]["Point"][0] ): ttConfig["SENSOR"]["AUX1"]["Point"][0].pop("fTemp")
   if( "fTemp" in ttConfig["SENSOR"]["AUX1"]["Point"][1] ): ttConfig["SENSOR"]["AUX1"]["Point"][1].pop("fTemp")
   if( "fTemp" in ttConfig["SENSOR"]["AUX1"]["Point"][2] ): ttConfig["SENSOR"]["AUX1"]["Point"][2].pop("fTemp")
  # AUX2 - Point0
  if( uiCode == 228 ):
   if( "uiCalReport" in ttConfig["SENSOR"]["AUX2"]["Point"][0] ): ttConfig["SENSOR"]["AUX2"]["Point"][0].pop("uiCalReport")
   if( "uiCalReport" in ttConfig["SENSOR"]["AUX2"]["Point"][1] ): ttConfig["SENSOR"]["AUX2"]["Point"][1].pop("uiCalReport")
   if( "uiCalReport" in ttConfig["SENSOR"]["AUX2"]["Point"][2] ): ttConfig["SENSOR"]["AUX2"]["Point"][2].pop("uiCalReport")
   if( "fTemp" in ttConfig["SENSOR"]["AUX2"]["Point"][0] ): ttConfig["SENSOR"]["AUX2"]["Point"][0].pop("fTemp")
   if( "fTemp" in ttConfig["SENSOR"]["AUX2"]["Point"][1] ): ttConfig["SENSOR"]["AUX2"]["Point"][1].pop("fTemp")
   if( "fTemp" in ttConfig["SENSOR"]["AUX2"]["Point"][2] ): ttConfig["SENSOR"]["AUX2"]["Point"][2].pop("fTemp")
  # AUX3 - Point
  if( uiCode == 232 ):
   if( "uiCalReport" in ttConfig["SENSOR"]["AUX3"]["Point"][0] ): ttConfig["SENSOR"]["AUX3"]["Point"][0].pop("uiCalReport")
   if( "uiCalReport" in ttConfig["SENSOR"]["AUX3"]["Point"][1] ): ttConfig["SENSOR"]["AUX3"]["Point"][1].pop("uiCalReport")
   if( "uiCalReport" in ttConfig["SENSOR"]["AUX3"]["Point"][2] ): ttConfig["SENSOR"]["AUX3"]["Point"][2].pop("uiCalReport")
   if( "fTemp" in ttConfig["SENSOR"]["AUX3"]["Point"][0] ): ttConfig["SENSOR"]["AUX3"]["Point"][0].pop("fTemp")
   if( "fTemp" in ttConfig["SENSOR"]["AUX3"]["Point"][1] ): ttConfig["SENSOR"]["AUX3"]["Point"][1].pop("fTemp")
   if( "fTemp" in ttConfig["SENSOR"]["AUX3"]["Point"][2] ): ttConfig["SENSOR"]["AUX3"]["Point"][2].pop("fTemp")
  # AUX4 - Point
  if( uiCode == 234 ):
   if( "uiCalReport" in ttConfig["SENSOR"]["AUX4"]["Point"][0] ): ttConfig["SENSOR"]["AUX4"]["Point"][0].pop("uiCalReport")
   if( "uiCalReport" in ttConfig["SENSOR"]["AUX4"]["Point"][1] ): ttConfig["SENSOR"]["AUX4"]["Point"][1].pop("uiCalReport")
   if( "uiCalReport" in ttConfig["SENSOR"]["AUX4"]["Point"][2] ): ttConfig["SENSOR"]["AUX4"]["Point"][2].pop("uiCalReport")
   if( "fTemp" in ttConfig["SENSOR"]["AUX4"]["Point"][0] ): ttConfig["SENSOR"]["AUX4"]["Point"][0].pop("fTemp")
   if( "fTemp" in ttConfig["SENSOR"]["AUX4"]["Point"][1] ): ttConfig["SENSOR"]["AUX4"]["Point"][1].pop("fTemp")
   if( "fTemp" in ttConfig["SENSOR"]["AUX4"]["Point"][2] ): ttConfig["SENSOR"]["AUX4"]["Point"][2].pop("fTemp")
  # AUX5 - Point
  if( uiCode == 235 ):
   if( "uiCalReport" in ttConfig["SENSOR"]["AUX5"]["Point"][0] ): ttConfig["SENSOR"]["AUX5"]["Point"][0].pop("uiCalReport")
   if( "uiCalReport" in ttConfig["SENSOR"]["AUX5"]["Point"][1] ): ttConfig["SENSOR"]["AUX5"]["Point"][1].pop("uiCalReport")
   if( "uiCalReport" in ttConfig["SENSOR"]["AUX5"]["Point"][2] ): ttConfig["SENSOR"]["AUX5"]["Point"][2].pop("uiCalReport")
   if( "fTemp" in ttConfig["SENSOR"]["AUX5"]["Point"][0] ): ttConfig["SENSOR"]["AUX5"]["Point"][0].pop("fTemp")
   if( "fTemp" in ttConfig["SENSOR"]["AUX5"]["Point"][1] ): ttConfig["SENSOR"]["AUX5"]["Point"][1].pop("fTemp")
   if( "fTemp" in ttConfig["SENSOR"]["AUX5"]["Point"][2] ): ttConfig["SENSOR"]["AUX5"]["Point"][2].pop("fTemp")
  # AUX6 - Point
  if( uiCode == 236 ):
   if( "uiCalReport" in ttConfig["SENSOR"]["AUX6"]["Point"][0] ): ttConfig["SENSOR"]["AUX6"]["Point"][0].pop("uiCalReport")
   if( "uiCalReport" in ttConfig["SENSOR"]["AUX6"]["Point"][1] ): ttConfig["SENSOR"]["AUX6"]["Point"][1].pop("uiCalReport")
   if( "uiCalReport" in ttConfig["SENSOR"]["AUX6"]["Point"][2] ): ttConfig["SENSOR"]["AUX6"]["Point"][2].pop("uiCalReport")
   if( "fTemp" in ttConfig["SENSOR"]["AUX6"]["Point"][0] ): ttConfig["SENSOR"]["AUX6"]["Point"][0].pop("fTemp")
   if( "fTemp" in ttConfig["SENSOR"]["AUX6"]["Point"][1] ): ttConfig["SENSOR"]["AUX6"]["Point"][1].pop("fTemp")
   if( "fTemp" in ttConfig["SENSOR"]["AUX6"]["Point"][2] ): ttConfig["SENSOR"]["AUX6"]["Point"][2].pop("fTemp")

  #print(ttConfig)
  print(ttConfig["SENSOR"]["DO"]["Point"][1])

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

  if( ttConfig["PRODUCT"]["ProBE_SW"] == 0 ):
   uiTEMP  = ( ( uiTEMP_MSB  & 0x03 ) << 8  ) + uiTEMP_LSB
  elif( ttConfig["PRODUCT"]["uiProbeType"] > 7 ):
   uiTEMP  = ( ( uiTEMP_MSB  & 0x0F ) << 8  ) + uiTEMP_LSB
  else:
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

  if( ttConfig["PRODUCT"]["ProBE_SW"] == 0 ):
   uiTEMP = ( -uiTEMP ) if( uiTEMP_MSB & 0x04 ) else uiTEMP
  elif( ttConfig["PRODUCT"]["uiProbeType"] > 7 ):
   uiTEMP = ( -uiTEMP ) if( uiTEMP_MSB & 0x80 ) else uiTEMP
  else:
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

  ttConfig["SENSOR"]["Baro"]["fDepthRaw"] = fDepth
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
 # Extraction des champs Measurement data
 #--------------------------
 def ttFParseMeasurementDataAquaPlus( self, sDataRead, ttConfig  ):
  # Decryptage de la donnée binaire
  txUnpacked = struct.unpack( '>20B', sDataRead )
  print(txUnpacked)
  uiCpt = 0
  # Extraction des champs
  uiEC_HSB    = txUnpacked[uiCpt]; uiCpt+=1 #  0 - EC_HSB - Flag bit 7
  uiTEMP_LSB  = txUnpacked[uiCpt]; uiCpt+=1 #  1 - TEMP_LSB
  uiEC_MSB    = txUnpacked[uiCpt]; uiCpt+=1 #  2 - EC_MSB
  uiCpt+=1                                  #  3 - SPARE
  uiCpt+=1                                  #  4 - SPARE
  uiCpt+=1                                  #  5 - SPARE
  uiDO_LSB    = txUnpacked[uiCpt]; uiCpt+=1 #  6 - DO_LSB
  uiTEMP_MSB  = txUnpacked[uiCpt]; uiCpt+=1 #  7 - TEMP_MSB - Flag bit 7
  uiEC_LSB    = txUnpacked[uiCpt]; uiCpt+=1 #  8 - EC_LSB
  uiCpt+=1                                  #  9 - SPARE
  uiDO_MSB    = txUnpacked[uiCpt]; uiCpt+=1 # 10 - DO_MSB - Flag bit 7
  uiCpt+=1                                  # 11 - SPARE
  uiCpt+=1                                  # 12 - SPARE
  uiDOsat_LSB = txUnpacked[uiCpt]; uiCpt+=1 # 13 - DO_PC_LSB
  uiDOsat_MSB = txUnpacked[uiCpt]; uiCpt+=1 # 14 - DO_PC_MSB
  uiCpt+=1                                  # 15 - SPARE
  uiCpt+=1                                  # 16 - SPARE
  uiCRC       = txUnpacked[uiCpt]; uiCpt+=1 # 17 - CRC


  print("uiTEMP_LSB      = %d"%( (uiTEMP_LSB )))
  print("uiTEMP_MSB      = %d"%( (uiTEMP_MSB )))

  uiEC_HSB   = ( uiEC_HSB   >> 4 ) + ( ( uiEC_HSB   << 4 ) & 0xF0 )
  uiEC_MSB   = ( uiEC_MSB   >> 4 ) + ( ( uiEC_MSB   << 4 ) & 0xF0 )
  uiTEMP_MSB = ( uiTEMP_MSB >> 4 ) + ( ( uiTEMP_MSB << 4 ) & 0xF0 )
  uiDO_MSB   = ( uiDO_MSB   >> 4 ) + ( ( uiDO_MSB   << 4 ) & 0xF0 )
  #uiDO_MSB   = ( uiDO_MSB   >> 4 ) or ( ( uiDO_MSB   << 4 ) & 0xF0 )

  if( ttConfig["PRODUCT"]["ProBE_SW"] == 0 ):
   uiTEMP  = ( ( uiTEMP_MSB  & 0x03 ) << 8  ) + uiTEMP_LSB
  elif( ttConfig["PRODUCT"]["uiProbeType"] > 7 ):
   uiTEMP  = ( ( uiTEMP_MSB  & 0x0F ) << 8  ) + uiTEMP_LSB
  else:
   uiTEMP  = ( ( uiTEMP_MSB  & 0x7F ) << 8  ) + uiTEMP_LSB
  uiEC    = ( ( uiEC_HSB    & 0x7F ) << 16 ) + ( uiEC_MSB << 8 ) + uiEC_LSB
  uiDO    = ( ( uiDO_MSB    & 0x7F ) << 8  ) + uiDO_LSB
  uiDOsat = ( ( uiDOsat_MSB & 0x7F ) << 8  ) + uiDOsat_LSB

  print("uiTEMP  = %d" % uiTEMP)
  print("uiEC    = %d" % uiEC)
  print("uiDO    = %d" % uiDO)
  print("uiDOsat = %d" % uiDOsat)

  if( ttConfig["PRODUCT"]["ProBE_SW"] == 0 ):
   uiTEMP = ( -uiTEMP ) if( uiTEMP_MSB & 0x04 ) else uiTEMP
  else:
   uiTEMP = ( -uiTEMP ) if( uiTEMP_MSB & 0x80 ) else uiTEMP
  fTEMP  = float( uiTEMP  ) / 10
  fEC    = float( uiEC    )
  fDO    = float( uiDO    ) / 100
  fDOsat = float( uiDOsat ) / 10

  Den_R0   = 3.9863
  Den_R1   = 288.9414
  Den_R2   = 68.12963
  Den_R3   = 508.9292
  fDensity = 1000.0 - (fTEMP - Den_R0) ** 2 * (fTEMP + Den_R1) / (fTEMP + Den_R2) / Den_R3

  print("fTEMP  = %f" % fTEMP)
  print("fEC    = %f" % fEC)
  print("fDO    = %f" % fDO)
  print("fDOsat = %f" % fDOsat)

  ttConfig["SENSOR"]["TEMP"]["fResult"]   = fTEMP
  ttConfig["SENSOR"]["EC"]["fResult"]     = fEC
  ttConfig["SENSOR"]["DO"]["fResult"]     = fDO
  ttConfig["SENSOR"]["DO Sat"]["fResult"] = fDOsat

  ttConfig["CALCULATED"]["EC"]["fEC_20"]    = fEC / ( ( ( fTEMP - 20 ) * 0.0191 ) + 1 )
  if( ttConfig["SENSOR"]["EC"]["bSC35_flag"] ):
   ttConfig["CALCULATED"]["EC"]["fEC_25"]     = fEC / ( ( ( fTEMP - 25 ) * 0.0181 ) + 1 )
  else:
   ttConfig["CALCULATED"]["EC"]["fEC_25"]     = fEC / ( ( ( fTEMP - 25 ) * 0.0191 ) + 1 )
  ttConfig["CALCULATED"]["TEMP"]["fTempF"]     = fTEMP * 1.8 + 32

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

  # Retour de la donnée
  return( ttConfig["SENSOR"] )

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
  """
  print('ttConfig["SENSOR"]["AUX1"]["fGS"] = %d'%ttConfig["SENSOR"]["AUX1"]["fGS"])
  print('ttConfig["SENSOR"]["AUX2"]["fGS"] = %d'%ttConfig["SENSOR"]["AUX2"]["fGS"])
  print('ttConfig["SENSOR"]["AUX3"]["fGS"] = %d'%ttConfig["SENSOR"]["AUX3"]["fGS"])
  print('ttConfig["SENSOR"]["AUX4"]["fGS"] = %d'%ttConfig["SENSOR"]["AUX4"]["fGS"])
  print('ttConfig["SENSOR"]["AUX5"]["fGS"] = %d'%ttConfig["SENSOR"]["AUX5"]["fGS"])
  print('ttConfig["SENSOR"]["AUX6"]["fGS"] = %d'%ttConfig["SENSOR"]["AUX6"]["fGS"])
  """
  if( "fGS" in ttConfig["SENSOR"]["AUX1"] ): fAUX1GS = ttConfig["SENSOR"]["AUX1"]["fGS"]
  if( "fGS" in ttConfig["SENSOR"]["AUX2"] ): fAUX2GS = ttConfig["SENSOR"]["AUX2"]["fGS"]
  if( "fGS" in ttConfig["SENSOR"]["AUX3"] ): fAUX3GS = ttConfig["SENSOR"]["AUX3"]["fGS"]
  if( "fGS" in ttConfig["SENSOR"]["AUX4"] ): fAUX4GS = ttConfig["SENSOR"]["AUX4"]["fGS"]
  if( "fGS" in ttConfig["SENSOR"]["AUX5"] ): fAUX5GS = ttConfig["SENSOR"]["AUX5"]["fGS"]
  if( "fGS" in ttConfig["SENSOR"]["AUX6"] ): fAUX6GS = ttConfig["SENSOR"]["AUX6"]["fGS"]

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

  # Si version sup à 5.11
  if( ttConfig["PRODUCT"]["uiPSW"] >= 511 ):
   # Ajout de l'optical avg au mois
   uiMonth = tCurrentDateTime.month + ttConfig["PRODUCT"]["uiOpticalAvg"]
  else:
   uiMonth = tCurrentDateTime.month

  #-- AP-Lite
  if( ttConfig["PRODUCT"]["uiModel"] == 30 ):
   # Formattage à partir du prototype
   txDataByte = struct.pack( ">4B",
                             225, # 0xE1
                             tCurrentDateTime.day,
                             uiMonth,
                             tCurrentDateTime.year-2000 )
   # Retourne buffer
   return( txDataByte )

  # Selon le numéro de version
  sPSW1 = ttConfig["PRODUCT"]["sPSW1"].replace(".", "")
  #    ( ( int(sPSW1[0]) == 4 ) and ( int(sPSW1[1]) == 0 ) and ( int(sPSW1[2]) > 6 ) )
  # or ( int(sPSW1[0]) >= 5 )
  #-- Si pas AP-Lite et ProbeSW != 3
  if(   ( ttConfig["PRODUCT"]["ProBE_SW"] !=  3 )
    and ( ttConfig["PRODUCT"]["uiModel"]  != 30 ) ):
   # Formattage à partir du prototype
   txDataByte = struct.pack( ">3B",
                             tCurrentDateTime.day,
                             uiMonth,
                             tCurrentDateTime.year-2000,
                             )
   # Retourne buffer
   return( txDataByte )

  # Dernier choix par défaut

  # Selon le numéro de version
  #sPSW1 = ttConfig["PRODUCT"]["sPSW1"].replace(".")
  #-- ProbeSW == 3
  #if(  ( ( int(sPSW1[0]) == 4 ) and ( int(sPSW1[1]) == 0 ) and ( int(sPSW1[2]) > 6 ) )
  #  or ( int(sPSW1[0]) >= 5 ) ):
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

  # Si AP-Lite
  if( ttConfig["PRODUCT"]["uiModel"] == 30 ):
   # Formattage à partir du prototype
   txDataByte = struct.pack( ">7B",
                             0xDA,
                             uiAux1Assign,
                             uiAux2Assign,
                             uiAux3Assign,
                             uiAux4Assign,
                             uiAux5Assign,
                             uiAux6Assign
                             )
  else:
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
 def uiFGetProbeTypeWithID( self, uiProductID ):
  # Init par défaut AP-2000
  uiProbeType = 4
  # AquaPlus
  if( uiProductID == 53 ): uiProbeType = 7
  # AP-Lite
  if( uiProductID == 30 ): uiProbeType = 1
  # AP-700
  if( uiProductID == 40 ): uiProbeType = 2
  # AP-700 - Old
  if( uiProductID == 17 ): uiProbeType = 8
  # AP-800
  if( uiProductID == 50 ): uiProbeType = 3
  # AP-800 - Old
  if( uiProductID ==  8 ): uiProbeType = 9
  # AP-700-D
  if( uiProductID == 60 ): uiProbeType = 2
  # AP-700-D - Old
  if( uiProductID == 27 ): uiProbeType = 8
  # AP-800-D
  if( uiProductID == 70 ): uiProbeType = 3
  # AP-800-D
  if( uiProductID == 28 ): uiProbeType = 9
  # AP-2000
  if( uiProductID == 10 ): uiProbeType = 4
  # AP-2000-D
  if( uiProductID == 20 ): uiProbeType = 4
  # AP-5000
  if( uiProductID == 59 ): uiProbeType = 5
  # AP-6K/7K/Pro
  if( uiProductID == 29 ): uiProbeType = 6
  # Retourne le résultat
  return( uiProbeType )

 #-------------------------------------
 # Type de sonde selon l'ID
 #-------------------------------------
 def sFGetProductNameWithID( self, uiProductID ):
  sProductName = "EMPTY"
  if( uiProductID == 53 ):  sProductName = "AquaPlus"
  if( uiProductID == 30 ):  sProductName = "AP-Lite"
  if( ( uiProductID == 40 ) or ( uiProductID == 17 ) ):  sProductName = "AP-700"
  if( ( uiProductID == 50 ) or ( uiProductID ==  8 ) ):  sProductName = "AP-800"
  if( ( uiProductID == 60 ) or ( uiProductID == 27 ) ):  sProductName = "AP-700-D"
  if( ( uiProductID == 70 ) or ( uiProductID == 28 ) ):  sProductName = "AP-800-D"
  if( uiProductID == 10 ):  sProductName = "AP-2000"
  if( uiProductID == 20 ):  sProductName = "AP-2000-D"
  if( uiProductID == 59 ):  sProductName = "AP-5000"
  if( uiProductID == 29 ):  sProductName = "AP-6K/7K/Pro"
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
  if( sProductName == "AP-2000"      ):  uiProductID = 10
  if( sProductName == "AP-2000-D"    ):  uiProductID = 20
  if( sProductName == "AP-5000"      ):  uiProductID = 59
  if( sProductName == "AP-6K/7K/Pro" ):  uiProductID = 29
  return( int( uiProductID ) )

 #-------------------------------------
 # Nombre d'AUX selon l'ID
 #-------------------------------------
 def sFGetAUXNumberWithID( self, uiProductID ):
  sProductName = "EMPTY"
  if( uiProductID == 53 ): uiAUXNumber = 0 # AquaPlus
  if( uiProductID == 30 ): uiAUXNumber = 1 # AP-Lite
  if( uiProductID == 40 ): uiAUXNumber = 0 # AP-700
  if( uiProductID == 50 ): uiAUXNumber = 1 # AP-800
  if( uiProductID == 60 ): uiAUXNumber = 0 # AP-700-D
  if( uiProductID == 70 ): uiAUXNumber = 1 # AP-800-D
  if( uiProductID == 10 ): uiAUXNumber = 2 # AP-2000
  if( uiProductID == 20 ): uiAUXNumber = 2 # AP-2000-D
  if( uiProductID == 59 ): uiAUXNumber = 4 # AP-5000
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
  if( ( sModel == "AP-2000" ) or ( sModel == "AP-2000-D" ) ):
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





