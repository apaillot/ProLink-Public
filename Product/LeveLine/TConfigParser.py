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
#from datetime import datetime

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
 # Init de la configuration
 #--------------------------
 def vFInitConfigObj( self, ttConfig ):
  print("-- vFInitConfigObj --")

  ttConfig["PRODUCT"]                = {}
  ttConfig["SENSOR"]                 = {}
  ttConfig["CALCULATED"]             = {}
  ttConfig["SENSOR"]["TEMP"]         = {}
  ttConfig["SENSOR"]["DEPTH"]        = {}
  ttConfig["SENSOR"]["BARO"]         = {}
  ttConfig["CALCULATED"]["TEMP"]     = {}
  ttConfig["CALCULATED"]["DEPTH"]    = {}
  ttConfig["CALCULATED"]["EC"]       = {}
  # Génération du nom de produit
  ttConfig["PRODUCT"]["bFGetProductName"]  = self.bFGetProductName
  # Chemin vers la photo produit
  ttConfig["PRODUCT"]["bFGetProductPhoto"] = self.bFGetProductPhoto
  # Voies fixes (index manuel négatif)
  ttConfig["SENSOR"]["TEMP"  ]["uiIndex"] = -1
  ttConfig["SENSOR"]["DEPTH" ]["uiIndex"] = -8
  ttConfig["SENSOR"]["BARO"  ]["uiIndex"] = -9
  # Nom de voie : fixed
  ttConfig["SENSOR"]["TEMP"  ]["sIndex"] = "Temperature"
  ttConfig["SENSOR"]["DEPTH" ]["sIndex"] = "Depth"
  ttConfig["SENSOR"]["BARO"  ]["sIndex"] = "Baro"
  # Unité
  ttConfig["SENSOR"]["TEMP"  ]["sUnit"] = "degC"
  ttConfig["SENSOR"]["DEPTH" ]["sUnit"] = "m"
  ttConfig["SENSOR"]["BARO"  ]["sUnit"] = "mB"
  # Nom de voie : fixed
  ttConfig["SENSOR"]["TEMP"  ]["sIndexCSV"] = "Temp"
  ttConfig["SENSOR"]["DEPTH" ]["sIndexCSV"] = "Depth"
  ttConfig["SENSOR"]["BARO"  ]["sIndexCSV"] = "Baro"
  # Unité
  ttConfig["SENSOR"]["TEMP"  ]["sUnitCSV"] = "C"
  ttConfig["SENSOR"]["DEPTH" ]["sUnitCSV"] = "m"
  ttConfig["SENSOR"]["BARO"  ]["sUnitCSV"] = "mB"
  # Résultat
  ttConfig["SENSOR"]["TEMP"  ]["fResult"] = 0
  ttConfig["SENSOR"]["DEPTH" ]["fResult"] = 0
  ttConfig["SENSOR"]["BARO"  ]["fResult"] = 0

 #------------------------------------------------------------------------------
 # Extraction des champs serial number
 #------------------------------------------------------------------------------
 def bFParseSerialNumber( self, sDataRead, ttConfig ):
  print("-- bFParseSerialNumber --")
  print(sDataRead)
  # Si invalide
  if(  ( len(sDataRead) < 17 )
    or ( sDataRead[1].decode() != "R" ) ): return( False )

  sDataRead = sDataRead[:18]
  print(sDataRead)
  print(len(sDataRead))
  # Decryptage de la donnée binaire
  txUnpacked = struct.unpack( '>2B8s1s3s4B', sDataRead )
  print(txUnpacked)
  uiCpt = 0
  # Extraction des champs
  uiDummy          = txUnpacked[uiCpt]; uiCpt+=1
  uiCMD            = txUnpacked[uiCpt]; uiCpt+=1
  sSerialNumber    = txUnpacked[uiCpt].decode(); uiCpt+=1
  sProbMeterInd    = txUnpacked[uiCpt].decode(); uiCpt+=1
  sFirmwareVersion = txUnpacked[uiCpt].decode(); uiCpt+=1
  print("sSerialNumber    = " + sSerialNumber)
  print("sProbMeterInd    = " + sProbMeterInd)
  print("sFirmwareVersion = " + sFirmwareVersion)

  bMeterDetected = (sProbMeterInd != "0")
  bECSensor  = (sSerialNumber[7]!="0") and ( (sSerialNumber[4]>="7") or (sSerialNumber[0]>"1") )
  bEcoSensor = (sSerialNumber[7]!="0") and (sSerialNumber[4]<"7") and (sSerialNumber[0]=="1")

  # Placement dans l'objet de configuration
  ttConfig["PRODUCT"]["sSerialNumber"]    = sSerialNumber
  ttConfig["PRODUCT"]["uiProbMeterInd"]   = int(sProbMeterInd)
  ttConfig["PRODUCT"]["sFirmwareVersion"] = sFirmwareVersion[0]+"."+sFirmwareVersion[1:]
  ttConfig["PRODUCT"]["bMeterDetected"]   = bMeterDetected
  ttConfig["PRODUCT"]["bECSensor"]        = bECSensor
  ttConfig["PRODUCT"]["bEcoSensor"]       = bEcoSensor
  print('ttConfig["PRODUCT"]["sSerialNumber"]    = ' + ttConfig["PRODUCT"]["sSerialNumber"])
  print('ttConfig["PRODUCT"]["uiProbMeterInd"]   = %d' % ttConfig["PRODUCT"]["uiProbMeterInd"])
  print('ttConfig["PRODUCT"]["sFirmwareVersion"] = ' + ttConfig["PRODUCT"]["sFirmwareVersion"])
  print('ttConfig["PRODUCT"]["bMeterDetected"]   = %d' % ttConfig["PRODUCT"]["bMeterDetected"])
  print('ttConfig["PRODUCT"]["bECSensor"]        = %d' % ttConfig["PRODUCT"]["bECSensor"])
  print('ttConfig["PRODUCT"]["bEcoSensor"]       = %d' % ttConfig["PRODUCT"]["bEcoSensor"])

  # Si EC
  if( bECSensor ):
   # Ajout de l'EC
   ttConfig["SENSOR"]["EC"] = {}
   ttConfig["CALCULATED"]["Salinity"] = {}
   ttConfig["SENSOR"]["EC"    ]["uiIndex"] = -2
   ttConfig["SENSOR"]["EC"    ]["sIndex"] = "EC"
   ttConfig["SENSOR"]["EC"    ]["sUnit"] = "uS/cm"
   ttConfig["SENSOR"]["EC"    ]["sIndexCSV"] = "EC"
   ttConfig["SENSOR"]["EC"    ]["sUnitCSV"] = "uS/cm"
   ttConfig["SENSOR"]["EC"    ]["fResult"] = 0

  # Valide
  return( True )

 #------------------------------------------------------------------------------
 # Extraction sensor type
 #------------------------------------------------------------------------------
 def bFParseSensorType( self, sDataRead, ttConfig ):
  print("-- bFParseSensorType --")
  print(sDataRead)
  # Si invalide
  if(  ( len(sDataRead) < 9 )
    or ( sDataRead[1].decode() != "T" ) ): return( False )

  sDataRead = sDataRead[:10]
  # Decryptage de la donnée binaire
  txUnpacked = struct.unpack( '>2B4s4B', sDataRead )
  print(txUnpacked)
  uiCpt = 0
  # Extraction des champs
  uiDummy          = txUnpacked[uiCpt]; uiCpt+=1
  uiCMD            = txUnpacked[uiCpt]; uiCpt+=1
  sSensorType      = txUnpacked[uiCpt].decode(); uiCpt+=1
  print("sSensorType    = " + sSensorType)

  bGauge = (sSensorType[0] == "G")
  bBaro  = (sSensorType    == "A001")

  # Format the depth rating & sensor type strings.
  # Supprime toutes les occurrences des caractères spécifiés dans la chaine
  #SensorType = senType.TrimStart("A"c, "G"c, "0"c)
  sSensorTypeStrip = sSensorType.lstrip("AG0")
  if( len(sSensorTypeStrip) == 0 ):
   sDepthRating   = "Unknown"
   sSensorTypeRep = "Unknown"
  else:
   #Dim rating As Integer = Convert.ToInt32(SensorType)
   uiRating = int(sSensorTypeStrip)
   if( bBaro ):
    sDepthRating = "0 m"
   elif( not bGauge and ( uiRating < 5 ) ):
    sDepthRating = str(uiRating - 1) + "0 m"
   else:
    sDepthRating = sSensorTypeStrip + "0 m"
   sSensorTypeRep = sSensorTypeStrip + " bar " + ("absolute" if(sSensorType[0] == "A") else "gauge")

  # Placement dans l'objet de configuration
  ttConfig["PRODUCT"]["sSensorType"] = sSensorType
  ttConfig["PRODUCT"]["bGauge"]      = bGauge
  ttConfig["PRODUCT"]["bBaro"]       = bBaro
  ttConfig["PRODUCT"]["sDepthRating"]      = sDepthRating
  ttConfig["PRODUCT"]["sSensorType"]       = sSensorType
  ttConfig["PRODUCT"]["sSensorTypeFormat"] = sSensorTypeRep
  print('ttConfig["PRODUCT"]["sSensorType"] = '   + ttConfig["PRODUCT"]["sSensorType"])
  print('ttConfig["PRODUCT"]["bGauge"]      = %d' % ttConfig["PRODUCT"]["bGauge"])
  print('ttConfig["PRODUCT"]["bBaro"]       = %d' % ttConfig["PRODUCT"]["bBaro"])
  print("sDepthRating = "+sDepthRating)
  print("sSensorType  = "+sSensorType)
  print("sSensorTypeRep = "+sSensorTypeRep)
  # Valide
  return( True )

 #------------------------------------------------------------------------------
 # Génération du nom de produit
 #------------------------------------------------------------------------------
 def bFGetProductName( self, ttConfig ):
  print("-- bFGetProductName --")
  #print(sDataRead)
  sName = ""
  # Selon le type de produit
  if( ttConfig["PRODUCT"]["bGauge"] ):         sName = "LeveLine Gauge"
  else:                                        sName = "LeveLine Absolute"
  if( ttConfig["PRODUCT"]["bBaro"]  ):         sName = "LeveLine Baro"
  if( ttConfig["PRODUCT"]["bMeterDetected"] ): sName = "GPS LeveLine Meter"
  if( ttConfig["PRODUCT"]["bECSensor"]  ):     sName = "LeveLine CTD"
  # Retour du nom du produit
  return( sName )

 #------------------------------------------------------------------------------
 # Extraction sensor type
 #------------------------------------------------------------------------------
 def bFGetProductPhoto( self, ttConfig ):
  print("-- bFGetProductName --")
  # Par défaut
  sPhoto = ":/Photo/LeveLine-TD.jpg"
  # Selon le type de produit
  #if( ttConfig["PRODUCT"]["bGauge"] ):         sName = "LeveLine Gauge"
  #else:                                        sName = "LeveLine Absolute"
  if( ttConfig["PRODUCT"]["bBaro"]  ):         sPhoto = ":/Photo/LeveLine-Baro.jpg"
  if( ttConfig["PRODUCT"]["bMeterDetected"] ): sPhoto = ":/Photo/LeveLine-meter.jpg"
  if( ttConfig["PRODUCT"]["bECSensor"]  ):     sPhoto = ":/Photo/LeveLine-CTD.jpg"
  # Retour du nom du produit
  return( sPhoto )

 #------------------------------------------------------------------------------
 # Extraction des champs cal date
 #------------------------------------------------------------------------------
 def bFParseCalDate( self, sDataRead, ttConfig ):
  print("-- bFParseCalDate --")
  print(sDataRead)
  # Si invalide
  if(  ( len(sDataRead) < 17 )
    or ( sDataRead[1].decode() != "O" ) ): return( False )

  sDataRead = sDataRead[:18]
  # Decryptage de la donnée binaire
  txUnpacked = struct.unpack( '>2B2s2s2s2s2s2s4B', sDataRead )
  print(txUnpacked)
  uiCpt = 0
  # Extraction des champs
  uiDummy            = txUnpacked[uiCpt]; uiCpt+=1
  uiCMD              = txUnpacked[uiCpt]; uiCpt+=1
  uiPressureCalDay   = int(txUnpacked[uiCpt]); uiCpt+=1
  uiPressureCalMonth = int(txUnpacked[uiCpt]); uiCpt+=1
  uiPressureCalYear  = int(txUnpacked[uiCpt]); uiCpt+=1
  uiTempCalDay       = int(txUnpacked[uiCpt]); uiCpt+=1
  uiTempCalMonth     = int(txUnpacked[uiCpt]); uiCpt+=1
  uiTempCalYear      = int(txUnpacked[uiCpt]); uiCpt+=1

  # Placement dans l'objet de configuration
  ttConfig["PRODUCT"]["uiPressureCalDay"]   = uiPressureCalDay
  ttConfig["PRODUCT"]["uiPressureCalMonth"] = uiPressureCalMonth
  ttConfig["PRODUCT"]["uiPressureCalYear"]  = uiPressureCalYear
  ttConfig["PRODUCT"]["uiTempCalDay"]       = uiTempCalDay
  ttConfig["PRODUCT"]["uiTempCalMonth"]     = uiTempCalMonth
  ttConfig["PRODUCT"]["uiTempCalYear"]      = uiTempCalYear
  # Formatage des dates
  sPressureCalDate = ("%02u"%uiPressureCalDay)+"/"+("%02u"%uiPressureCalMonth)+"/20"+("%02u"%uiPressureCalYear)
  sTempCalDate     = ("%02u"%uiTempCalDay)+"/"+("%02u"%uiTempCalMonth)+"/20"+("%02u"%uiTempCalYear)
  # Objet conf
  ttConfig["PRODUCT"]["sPressureCalDate"] = sPressureCalDate
  ttConfig["PRODUCT"]["sTempCalDate"]     = sTempCalDate
  print('ttConfig["PRODUCT"]["sPressureCalDate"] = '+ttConfig["PRODUCT"]["sPressureCalDate"])
  print('ttConfig["PRODUCT"]["sTempCalDate"]     = '+ttConfig["PRODUCT"]["sTempCalDate"])
  # Valide
  return( True )

 #------------------------------------------------------------------------------
 # Extraction des champs indent et position
 #------------------------------------------------------------------------------
 def bFParseIdentAndPosition( self, sDataRead, ttConfig ):
  print("-- bFParseCalDate --")
  print(sDataRead)
  # Si invalide
  if(  ( len(sDataRead) < 46 )
    or ( sDataRead[1].decode() != "W" ) ): return( False )

  sDataRead = sDataRead[:47]
  # Decryptage de la donnée binaire
  txUnpacked = struct.unpack( '>2B16s9s10s6s4B', sDataRead )
  print(txUnpacked)
  uiCpt = 0
  # Extraction des champs
  uiDummy    = txUnpacked[uiCpt]; uiCpt+=1
  uiCMD      = txUnpacked[uiCpt]; uiCpt+=1
  sSiteID    = txUnpacked[uiCpt].decode(); uiCpt+=1
  sLatitude  = txUnpacked[uiCpt].decode(); uiCpt+=1
  sLongitude = txUnpacked[uiCpt].decode(); uiCpt+=1
  sAltitude  = txUnpacked[uiCpt].decode(); uiCpt+=1
  print("sSiteID    = " + sSiteID)
  print("sLatitude  = " + sLatitude)
  print("sLongitude = " + sLongitude)
  print("sAltitude  = " + sAltitude)

  # Site ID
  sSiteID    = sSiteID.strip()
  ttConfig["PRODUCT"]["sSiteID"]    = sSiteID

  # Latitude
  ttConfig["PRODUCT"]["sLatitudeRaw"]  = sLatitude
  # Si non-initialisé
  if( sLatitude != "---------" ):
   ttConfig["PRODUCT"]["sLatitudeRef"] = str( sLatitude[0] )
   ttConfig["PRODUCT"]["iLatitudeDeg"] = int( sLatitude[1]+sLatitude[2] )
   ttConfig["PRODUCT"]["iLatitudeMin"] = int( sLatitude[3]+sLatitude[4] )
   ttConfig["PRODUCT"]["iLatitudeSec"] = int( sLatitude[5]+sLatitude[6]+sLatitude[7]+sLatitude[8] )
   ttConfig["PRODUCT"]["sLatitude"]    = sLatitude[0]+" "+sLatitude[1]+sLatitude[2]+"°"+sLatitude[3]+sLatitude[4]+"."+sLatitude[5]+sLatitude[6]+sLatitude[7]+sLatitude[8]+"'"
  else:
   ttConfig["PRODUCT"]["sLatitudeRef"] = ""
   ttConfig["PRODUCT"]["iLatitudeDeg"] = 0
   ttConfig["PRODUCT"]["iLatitudeMin"] = 0
   ttConfig["PRODUCT"]["iLatitudeSec"] = 0
   ttConfig["PRODUCT"]["sLatitude"]    = "- --°--.----'"

  # Longitude
  ttConfig["PRODUCT"]["sLongitudeRaw"] = sLongitude
  # Si non-initialisé
  if( sLongitude != "----------" ):
   ttConfig["PRODUCT"]["sLongitudeRef"] = str( sLongitude[0] )
   ttConfig["PRODUCT"]["iLongitudeDeg"] = int( sLongitude[1]+sLongitude[2]+sLongitude[3] )
   ttConfig["PRODUCT"]["iLongitudeMin"] = int( sLongitude[4]+sLongitude[5] )
   ttConfig["PRODUCT"]["iLongitudeSec"] = int( sLongitude[6]+sLongitude[7]+sLongitude[8]+sLongitude[9] )
   ttConfig["PRODUCT"]["sLongitude"]    = sLongitude[0]+" "+sLongitude[1]+sLongitude[2]+sLongitude[3]+"°"+sLongitude[4]+sLongitude[5]+"."+sLongitude[6]+sLongitude[7]+sLongitude[8]+sLongitude[9]+"'"
  else:
   ttConfig["PRODUCT"]["sLongitudeRef"] = ""
   ttConfig["PRODUCT"]["iLongitudeDeg"] = 0
   ttConfig["PRODUCT"]["iLongitudeMin"] = 0
   ttConfig["PRODUCT"]["iLongitudeSec"] = 0
   ttConfig["PRODUCT"]["sLongitude"]    = "- ---°--.----'"

  # Altitude
  ttConfig["PRODUCT"]["sAltitudeRaw"]  = sAltitude
  if( sAltitude != "------" ):
   ttConfig["PRODUCT"]["iAltitude"]  = int(sAltitude)
   ttConfig["PRODUCT"]["sAltitude"]   = str( int(sAltitude) )
  else:
   ttConfig["PRODUCT"]["iAltitude"]  = 0
   ttConfig["PRODUCT"]["sAltitude"]  = sAltitude

  print('ttConfig["PRODUCT"]["sSiteID"]    = '+ttConfig["PRODUCT"]["sSiteID"])
  print('ttConfig["PRODUCT"]["sLatitude"]  = '+ttConfig["PRODUCT"]["sLatitude"])
  print('ttConfig["PRODUCT"]["sLongitude"] = '+ttConfig["PRODUCT"]["sLongitude"])
  print('ttConfig["PRODUCT"]["sAltitude"]  = '+ttConfig["PRODUCT"]["sAltitude"])

  if (ttConfig["PRODUCT"]["sLatitudeRef"] != ""):
   print( "iLatitude  = %s %d %d %d"%(ttConfig["PRODUCT"]["sLongitudeRef"],
                                      ttConfig["PRODUCT"]["iLatitudeDeg"],
                                      ttConfig["PRODUCT"]["iLatitudeMin"],
                                      ttConfig["PRODUCT"]["iLatitudeSec"]) )
  if( ttConfig["PRODUCT"]["sLongitudeRef"] != "" ):
   print( "iLongitude = %s %d %d %d"%(ttConfig["PRODUCT"]["sLongitudeRef"],
                                      ttConfig["PRODUCT"]["iLongitudeDeg"],
                                      ttConfig["PRODUCT"]["iLongitudeMin"],
                                      ttConfig["PRODUCT"]["iLongitudeSec"]) )

  # Valide
  return( True )

 #------------------------------------------------------------------------------
 # Extraction des champs log interval
 #------------------------------------------------------------------------------
 def bFParseLogInterval( self, sDataRead, ttConfig ):
  print("-- bFParseLogInterval --")
  print(sDataRead)
  # Si invalide
  if(  ( len(sDataRead) < 12 )
    or ( sDataRead[1].decode() != "B" ) ): return( False )

  sDataRead = sDataRead[:13]
  # Decryptage de la donnée binaire
  txUnpacked = struct.unpack( '>2B7s4B', sDataRead )
  print(txUnpacked)
  uiCpt = 0
  # Extraction des champs
  uiDummy      = txUnpacked[uiCpt]; uiCpt+=1
  uiCMD        = txUnpacked[uiCpt]; uiCpt+=1
  xLogInterval = txUnpacked[uiCpt]; uiCpt+=1

  uiLogInterval = int(xLogInterval)
  print("uiLogInterval = %d"%uiLogInterval)
  uiLogIntervalHour = int(uiLogInterval / 36000)
  uiLogIntervalMin  = int( ( uiLogInterval % 36000 ) / 600 )
  fLogIntervalSec   = float( int(uiLogInterval % 600) ) / 10

  ttConfig["PRODUCT"]["uiLogInterval"]     = uiLogInterval
  ttConfig["PRODUCT"]["uiLogIntervalHour"] = uiLogIntervalHour
  ttConfig["PRODUCT"]["uiLogIntervalMin"]  = uiLogIntervalMin
  ttConfig["PRODUCT"]["fLogIntervalSec"]   = fLogIntervalSec

  print("uiLogInterval     = %d"%uiLogInterval)
  print("uiLogIntervalHour = %d"%uiLogIntervalHour)
  print("uiLogIntervalMin  = %d"%uiLogIntervalMin)
  print("fLogIntervalSec   = %.1f"%fLogIntervalSec)
  # Valide
  return( True )

 #------------------------------------------------------------------------------
 # Extraction des champs log start datetime
 #------------------------------------------------------------------------------
 def bFParseLogStartDatetime( self, sDataRead, ttConfig ):
  print("-- bFParseLogStartDatetime --")
  print(sDataRead)
  # Si invalide
  if(  ( len(sDataRead) < 17 )
    or ( sDataRead[1].decode() != "J" ) ): return( False )

  sDataRead = sDataRead[:18]
  # Decryptage de la donnée binaire
  txUnpacked = struct.unpack( '>2B12s4B', sDataRead )
  print(txUnpacked)
  uiCpt = 0
  # Extraction des champs
  uiDummy = txUnpacked[uiCpt]; uiCpt+=1
  uiCMD   = txUnpacked[uiCpt]; uiCpt+=1
  sDatetimeRaw = txUnpacked[uiCpt].decode(); uiCpt+=1

  # Si activé ou non
  if( sDatetimeRaw == "000000000000" ):
   ttConfig["PRODUCT"]["bScheduled"]  = False
  else:
   ttConfig["PRODUCT"]["bScheduled"]  = True
  uiHour  = int(sDatetimeRaw[0:2])
  uiMin   = int(sDatetimeRaw[2:4])
  uiSec   = int(sDatetimeRaw[4:6])
  uiDay   = int(sDatetimeRaw[6:8])
  uiMonth = int(sDatetimeRaw[8:10])
  uiYear  = int(sDatetimeRaw[10:12])
  # Affichage
  print("uiHour  = %d"%uiHour)
  print("uiMin   = %d"%uiMin)
  print("uiSec   = %d"%uiSec)
  print("uiDay   = %d"%uiDay)
  print("uiMonth = %d"%uiMonth)
  print("uiYear  = %d"%uiYear)
  # Date de démarrage mesure
  sDate = ("%02u/%02u/%02u %02u:%02u:%02u"%(uiDay, uiMonth, 2000+uiYear, uiHour, uiMin, uiSec))

  #ttConfig["PRODUCT"]["uiLogDate"]     = uiLogInterval
  ttConfig["PRODUCT"]["uiLogStartYear"]  = uiYear
  ttConfig["PRODUCT"]["uiLogStartMonth"] = uiMonth
  ttConfig["PRODUCT"]["uiLogStartDay"]   = uiDay
  ttConfig["PRODUCT"]["uiLogStartHour"]  = uiHour
  ttConfig["PRODUCT"]["uiLogStartMin"]   = uiMin
  ttConfig["PRODUCT"]["uiLogStartSec"]   = uiSec
  ttConfig["PRODUCT"]["sLogStartDate"]   = sDate

  if( sDatetimeRaw != "000000000000" ):
   tDateTime = datetime.datetime(2000+uiYear, uiMonth, uiDay, uiHour, uiMin, uiSec)
   ttConfig["PRODUCT"]["tLogStartDate"]   = tDateTime
  # Valide
  return( True )

 #------------------------------------------------------------------------------
 # Extraction des champs log duration
 #------------------------------------------------------------------------------
 def bFParseLogDuration( self, sDataRead, ttConfig ):
  print("-- bFParseLogDuration --")
  print(sDataRead)
  # Si invalide
  if(  ( len(sDataRead) < 10 )
    or ( sDataRead[1].decode() != "L" ) ): return( False )

  sDataRead = sDataRead[:11]
  # Decryptage de la donnée binaire
  txUnpacked = struct.unpack( '>2B5s4B', sDataRead )
  print(txUnpacked)
  uiCpt = 0
  # Extraction des champs
  uiDummy      = txUnpacked[uiCpt]; uiCpt+=1
  uiCMD        = txUnpacked[uiCpt]; uiCpt+=1
  xLogDuration = txUnpacked[uiCpt]; uiCpt+=1

  uiLogDuration = int(xLogDuration)
  print("uiLogDuration = %d"%uiLogDuration)

  ttConfig["PRODUCT"]["uiLogDuration"]     = uiLogDuration

  # Valide
  return( True )

 #------------------------------------------------------------------------------
 # Extraction des champs event interval
 #------------------------------------------------------------------------------
 def bFParseEventInterval( self, sDataRead, ttConfig ):
  print("-- bFParseEventInterval --")
  print(sDataRead)
  # Si invalide
  if(  ( len(sDataRead) < 12 )
    or ( sDataRead[1].decode() != "D" ) ): return( False )

  sDataRead = sDataRead[:13]
  # Decryptage de la donnée binaire
  txUnpacked = struct.unpack( '>2B7s4B', sDataRead )
  print(txUnpacked)
  uiCpt = 0
  # Extraction des champs
  uiDummy        = txUnpacked[uiCpt]; uiCpt+=1
  uiCMD          = txUnpacked[uiCpt]; uiCpt+=1
  sEventInterval = txUnpacked[uiCpt]; uiCpt+=1

  uiEventInterval = int(sEventInterval)
  print("uiEventInterval = %d"%uiEventInterval)
  ttConfig["PRODUCT"]["bEventLog"]       = ( uiEventInterval != 0 )
  ttConfig["PRODUCT"]["uiEventInterval"] = uiEventInterval
  ttConfig["PRODUCT"]["uiEventHour"]     = int( uiEventInterval / 36000 )
  ttConfig["PRODUCT"]["uiEventMin"]      = int( ( uiEventInterval % 36000 ) / 600 )
  ttConfig["PRODUCT"]["fEventSec"]       = float( ( uiEventInterval % 600 ) / 10 )
  # Valide
  return( True )

 #------------------------------------------------------------------------------
 # Extraction des champs event limits
 #------------------------------------------------------------------------------
 def bFParseEventLimits( self, sDataRead, ttConfig ):
  print("-- bFParseEventLimits --")
  print(sDataRead)
  # Si invalide
  if(  ( len(sDataRead) < 14 )
    or ( sDataRead[1].decode() != "F" ) ): return( False )

  sDataRead = sDataRead[:15]
  # Decryptage de la donnée binaire
  txUnpacked = struct.unpack( '>2B9s4B', sDataRead )
  print(txUnpacked)
  uiCpt = 0
  # Extraction des champs
  uiDummy      = txUnpacked[uiCpt]; uiCpt+=1
  uiCMD        = txUnpacked[uiCpt]; uiCpt+=1
  sEventLimits = txUnpacked[uiCpt]; uiCpt+=1

  uiPressureLimit = int(sEventLimits[0:6])
  uiTempLimit     = int(sEventLimits[6:10])
  '''
  # Test si CTD
  if():
   uiTempLimit     = int(sEventLimits[6:9])
  # TD classique
  else:
   uiTempLimit     = int(sEventLimits[6:9])
  '''
  print("uiPressureLimit = %d"%uiPressureLimit)
  print("uiTempLimit     = %d"%uiTempLimit)
  ttConfig["PRODUCT"]["uiPressureLimit"] = uiPressureLimit
  ttConfig["PRODUCT"]["fPressureLimit"]  = float(uiPressureLimit) / 1000

  if( ttConfig["PRODUCT"]["bECSensor"] ):
   ttConfig["PRODUCT"]["uiSalinityLimit"] = float(uiTempLimit)
   ttConfig["PRODUCT"]["fSalinityLimit"]  = float(uiTempLimit) / 10
  else:
   ttConfig["PRODUCT"]["uiTempLimit"]     = float(uiTempLimit)
   ttConfig["PRODUCT"]["fTempLimit"]      = float(uiTempLimit) / 10
  # Valide
  return( True )

 #------------------------------------------------------------------------------
 # Extraction des champs datetime
 #------------------------------------------------------------------------------
 def bFParseDatetime( self, sDataRead, ttConfig ):
  print("-- bFParseDatetime --")
  print(sDataRead)
  # Si invalide
  if(  ( len(sDataRead) < 17 )
    or ( sDataRead[1].decode() != "H" ) ): return( False )

  sDataRead = sDataRead[:18]
  # Decryptage de la donnée binaire
  txUnpacked = struct.unpack( '>2B12s4B', sDataRead )
  print(txUnpacked)
  uiCpt = 0
  # Extraction des champs
  uiDummy      = txUnpacked[uiCpt]; uiCpt+=1
  uiCMD        = txUnpacked[uiCpt]; uiCpt+=1
  sDatetimeRaw = txUnpacked[uiCpt].decode(); uiCpt+=1

  uiHour  = int(sDatetimeRaw[0:2])
  uiMin   = int(sDatetimeRaw[2:4])
  uiSec   = int(sDatetimeRaw[4:6])
  uiDay   = int(sDatetimeRaw[6:8])
  uiMonth = int(sDatetimeRaw[8:10])
  uiYear  = int(sDatetimeRaw[10:12])

  print("uiHour  = %d"%uiHour)
  print("uiMin   = %d"%uiMin)
  print("uiSec   = %d"%uiSec)
  print("uiDay   = %d"%uiDay)
  print("uiMonth = %d"%uiMonth)
  print("uiYear  = %d"%uiYear)

  #ttConfig["PRODUCT"]["uiLogDate"]     = uiLogInterval
  ttConfig["PRODUCT"]["uiYear"]  = uiYear
  ttConfig["PRODUCT"]["uiMonth"] = uiMonth
  ttConfig["PRODUCT"]["uiDay"]   = uiDay
  ttConfig["PRODUCT"]["uiHour"]  = uiHour
  ttConfig["PRODUCT"]["uiMin"]   = uiMin
  ttConfig["PRODUCT"]["uiSec"]   = uiSec
  # Formatage des dates
  sRTCDate = ("%02u"%uiDay)+"/"+("%02u"%uiMonth)+"/20"+("%02u"%uiYear)
  sRTCTime = ("%02u"%uiHour)+":"+("%02u"%uiMin)+":"+("%02u"%uiSec)
  # Objet conf
  ttConfig["PRODUCT"]["sRTCDate"]   = sRTCDate
  ttConfig["PRODUCT"]["sRTCTime"]   = sRTCTime
  # Valide
  return( True )

 #------------------------------------------------------------------------------
 # Extraction des champs datetime
 #------------------------------------------------------------------------------
 def bFParseLiveData( self, sDataRead, ttConfig ):
  print("-- bFParseLiveData --")
  print(sDataRead)

  # Si invalide
  if(  ( len(sDataRead) < 18 )
    or ( sDataRead[1].decode() != "b" ) ): return( False )

  print("Valide")
  #----------
  # Si EC
  #----------
  if( len( sDataRead ) > 20 ):
   sDataRead = sDataRead[:27]
   # Decryptage de la donnée binaire
   txUnpacked = struct.unpack( '>2B8s6s7s4B', sDataRead )
   print(txUnpacked)
   uiCpt = 0
   # Extraction des champs
   uiDummy    = txUnpacked[uiCpt]; uiCpt+=1
   uiCMD      = txUnpacked[uiCpt]; uiCpt+=1
   uiPressure    = int(txUnpacked[uiCpt]); uiCpt+=1
   uiTemperature = int(txUnpacked[uiCpt]); uiCpt+=1
   uiEC          = int(txUnpacked[uiCpt]); uiCpt+=1
   # Calcul de la valeur
   fDepth    = float(uiPressure) / 10
   fTEMP     = float(uiTemperature) / 100
   fEC       = float(uiEC)

   # Résultat de mesure
   ttConfig["SENSOR"]["DEPTH"]["fResult"] = fDepth
   ttConfig["SENSOR"]["TEMP"]["fResult"]  = fTEMP
   ttConfig["SENSOR"]["EC"]["fResult"]    = fEC
   # Voies calculées
   ttConfig["CALCULATED"]["TEMP"]["fTempF"]   = fTEMP * 1.8 + 32
   ttConfig["CALCULATED"]["DEPTH"]["fDepthF"] = fDepth * 3.28083
   ttConfig["CALCULATED"]["EC"]["fEC_20"]     = fEC / ( ( ( fTEMP - 20 ) * 0.0191 ) + 1 )
   ttConfig["CALCULATED"]["EC"]["fEC_25"]     = fEC / ( ( ( fTEMP - 25 ) * 0.0191 ) + 1 )
   # Calcul salinité
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

   print("fDepth    = %.1f"%ttConfig["SENSOR"]["DEPTH"]["fResult"])
   print("fTEMP     = %.2f"%ttConfig["SENSOR"]["TEMP"]["fResult"])
   print("fEC       = %.0f"%ttConfig["SENSOR"]["EC"]["fResult"])
   print("fTempF    = %.2f"%ttConfig["CALCULATED"]["TEMP"]["fTempF"])
   print("fEC_20    = %.0f"%ttConfig["CALCULATED"]["EC"]["fEC_20"])
   print("fEC_25    = %.0f"%ttConfig["CALCULATED"]["EC"]["fEC_25"])
   print("fSalinity = %.2f"%ttConfig["CALCULATED"]["Salinity"]["fResult"])

  #----------
  # TD ou baro
  #----------
  else:
   sDataRead = sDataRead[:21]
   # Decryptage de la donnée binaire
   txUnpacked = struct.unpack( '>2B8s6s4B', sDataRead )
   print(txUnpacked)
   uiCpt = 0
   # Extraction des champs
   uiDummy       = txUnpacked[uiCpt]; uiCpt+=1
   uiCMD         = txUnpacked[uiCpt]; uiCpt+=1
   uiDepth       = int(txUnpacked[uiCpt]); uiCpt+=1
   uiTemperature = int(txUnpacked[uiCpt]); uiCpt+=1
   # Calcul de la valeur
   fDepth  = float(uiDepth) / 10
   fTEMP   = float(uiTemperature) / 100

   # Résultat de mesure
   ttConfig["SENSOR"]["DEPTH"]["fResult"]  = fDepth
   ttConfig["SENSOR"]["TEMP"]["fResult"]   = fTEMP
   # Voies calculées
   ttConfig["CALCULATED"]["TEMP"]["fTempF"]   = fTEMP * 1.8 + 32
   ttConfig["CALCULATED"]["DEPTH"]["fDepthF"] = fDepth * 3.28083

   print("fDepth    = %.1f"%ttConfig["SENSOR"]["DEPTH"]["fResult"])
   print("fTEMP     = %.2f"%ttConfig["SENSOR"]["TEMP"]["fResult"])
   print("fTempF    = %.2f"%ttConfig["CALCULATED"]["TEMP"]["fTempF"])

  # Valide
  return( True )

 #------------------------------------------------------------------------------
 # Extraction du status
 #------------------------------------------------------------------------------
 def bFParseStatus( self, sDataRead, ttConfig ):
  print("-- bFParseStatus --")
  print(sDataRead)
  # Si invalide
  if(  ( len(sDataRead) < 16 )
    or ( sDataRead[1].decode() != "P" ) ): return( False )

  sDataRead = sDataRead[:16]
  # Decryptage de la donnée binaire
  txUnpacked = struct.unpack( '>2B6s3s1s4B', sDataRead )
  print(txUnpacked)
  uiCpt = 0
  # Extraction des champs
  uiDummy      = txUnpacked[uiCpt]; uiCpt+=1
  uiCMD        = txUnpacked[uiCpt]; uiCpt+=1
  sLogCount    = txUnpacked[uiCpt]; uiCpt+=1
  sBatteryLife = txUnpacked[uiCpt]; uiCpt+=1
  sLogging     = txUnpacked[uiCpt]; uiCpt+=1

  uiLogCount   = int(sLogCount)
  fBatteryLife = float(sBatteryLife) / 10
  bLogging     = bool(int(sLogging))
  print("uiLogCount   = %d"%uiLogCount)
  print("fBatteryLife = %.1f"%fBatteryLife)
  print("bLogging     = %d"% bLogging)
  ttConfig["PRODUCT"]["uiLogCount"]   = uiLogCount
  ttConfig["PRODUCT"]["fBatteryLife"] = fBatteryLife
  ttConfig["PRODUCT"]["bLogging"]     = bLogging

  # Calcul du nombre d'échantillon restant
  if(  ttConfig["PRODUCT"]["bEcoSensor"]
    or ttConfig["PRODUCT"]["bBaro"] ):
   ttConfig["PRODUCT"]["uiLogFree"] = 150000 - uiLogCount
  else:
   ttConfig["PRODUCT"]["uiLogFree"] = 500000 - uiLogCount




  # Valide
  return( True )
