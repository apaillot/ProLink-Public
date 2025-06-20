# This Python file uses the following encoding: utf-8

#============================================================================#
# Librairies système
#============================================================================#
import sys
from datetime import datetime
import json
import csv

#============================================================================#
# Librairies Qt
#============================================================================#
from PySide6.QtCore import (QDate, QDateTime)
from PySide6.QtCore import Slot

#============================================================================#
# Librairies Utilisateur
#============================================================================#
from Vue.VLib                     import *

#============================================================================#
# Variable
#============================================================================#

#============================================================================#
# Classe
#============================================================================#

#------------------------------------------------------------------------
# Gestion du projet donnée LeveLine
#------------------------------------------------------------------------
class TLeveLineDataProject:
 #----------------------------------------------
 # Init
 #----------------------------------------------
 def __init__( self ):
  # Init variable
  self.sProjectPathName = ""
  # Objet general
  self.tPrj = {}

 #----------------------------------------------
 # Création du projet :
 #---------------------------------------------
 # - Création du fichier dans le repertoire
 # - Initialisation de la structure de base
 #----------------------------------------------
 def bFCreateProject( self, sProjectPathName ):
  # Sauvegarde du nom du projet/chemin
  self.sProjectPathName = sProjectPathName
  #
  self.tPrj = {}
  sProjectName = sProjectPathName.split("/")[len(sProjectPathName.split("/"))-1]
  #sProjectName = sProjectName.split(".")[0]
  self.tPrj["sProjectName"]   = sProjectName
  self.tPrj["sProjectFolder"] = sProjectPathName[:len(sProjectPathName.split("/")[len(sProjectPathName.split("/"))-1])]
  self.tPrj["tSensor"] = {}
  # Création du fichier
  with open(self.sProjectPathName, 'w', newline='') as tFileHandler:
   # Ecriture
   json.dump(self.tPrj, tFileHandler, indent = 1)

 #----------------------------------------------
 # Ouverture du projet :
 #---------------------------------------------
 # - Ouverture du fichier contenant le projet
 # - Initialisation de la structure de base
 #----------------------------------------------
 def openProject( self, sProjectPathName ):
  print("-- TLvlDataPrj > openProject --")
  # Sauvegarde du nom du projet/chemin
  self.sProjectPathName = sProjectPathName
  # Ouverture en lecture
  with open(self.sProjectPathName, "r") as tFileHandler:
   self.tPrj = json.load(tFileHandler)

  # Vérification
  for sSerialNumber in self.tPrj["tSensor"]:
   for sSerieName in self.tPrj["tSensor"][sSerialNumber]["serie"]:
    # Vérification baro correction
    if( not "sBaroCorrection" in self.tPrj["tSensor"][sSerialNumber]["serie"][sSerieName] ):
     self.tPrj["tSensor"][sSerialNumber]["serie"][sSerieName]["sBaroCorrection"]      = "None"
     self.tPrj["tSensor"][sSerialNumber]["serie"][sSerieName]["xBaroCorrectionValue"] = ""
    # Vérification density correction
    if( not "sDensityCorrection" in self.tPrj["tSensor"][sSerialNumber]["serie"][sSerieName] ):
     self.tPrj["tSensor"][sSerialNumber]["serie"][sSerieName]["sDensityCorrection"]      = "Temp only"
     self.tPrj["tSensor"][sSerialNumber]["serie"][sSerieName]["fDensityCorrectionValue"] = ""
    # Vérification offset correction
    if( not "uiOffsetCorrection" in self.tPrj["tSensor"][sSerialNumber]["serie"][sSerieName] ):
     self.tPrj["tSensor"][sSerialNumber]["serie"][sSerieName]["uiOffsetCorrection"]     = 0
     self.tPrj["tSensor"][sSerialNumber]["serie"][sSerieName]["fOffsetCorrectionValue"] = 0
    # Vérification averaging
    if( not "uiAveraging" in self.tPrj["tSensor"][sSerialNumber]["serie"][sSerieName] ):
     self.tPrj["tSensor"][sSerialNumber]["serie"][sSerieName]["uiAveraging"]      = 0
     self.tPrj["tSensor"][sSerialNumber]["serie"][sSerieName]["uiAveragingValue"] = 0

   # Sauvegarde
   self.saveProject

 #----------------------------------------------
 # Sauvegarde du projet :
 #---------------------------------------------
 # - Sauvegarde du projet dans son fichier initial
 #----------------------------------------------
 def saveProject( self ):
  print("-- TLvlDataPrj > saveProject --")
  # Création du fichier
  with open(self.sProjectPathName, 'w', newline='') as tFileHandler:
   # Ecriture
   json.dump(self.tPrj, tFileHandler, indent = 1)

 #----------------------------------------------
 # Ajout de donnée capteur :
 #---------------------------------------------
 # - Création si besoin du capteur dans l'objet
 # - Ajout de la série de donnée
 #----------------------------------------------
 def addSensorData( self, ttConfig, ttMeasure ):
  print("-- TLvlDataPrj > addSensorData --")

  sSerialNumber = ttConfig["PRODUCT"]["sSerialNumber"]
  # Si capteur existe
  if( not sSerialNumber in self.tPrj["tSensor"] ):
   self.tPrj["tSensor"][sSerialNumber] = {}
   self.tPrj["tSensor"][sSerialNumber]["sSN"]           = ttConfig["PRODUCT"]["sSerialNumber"]
   self.tPrj["tSensor"][sSerialNumber]["sProductName"]  = ttConfig["PRODUCT"]["bFGetProductName"](ttConfig)
   self.tPrj["tSensor"][sSerialNumber]["sSiteID"]       = ttConfig["PRODUCT"]["sSiteID"]
   self.tPrj["tSensor"][sSerialNumber]["sLatitude"]     = ttConfig["PRODUCT"]["sLatitude"]
   self.tPrj["tSensor"][sSerialNumber]["sLongitude"]    = ttConfig["PRODUCT"]["sLongitude"]
   self.tPrj["tSensor"][sSerialNumber]["sAltitude"]     = ttConfig["PRODUCT"]["sAltitude"]
   self.tPrj["tSensor"][sSerialNumber]["bBaro"]         = ttConfig["PRODUCT"]["bBaro"]
   self.tPrj["tSensor"][sSerialNumber]["bECSensor"]     = ttConfig["PRODUCT"]["bECSensor"]
   self.tPrj["tSensor"][sSerialNumber]["sProductPhoto"] = ttConfig["PRODUCT"]["bFGetProductPhoto"](ttConfig)

  # Premier échantillon
  uiYear  = ttMeasure[0]["uiYear"]
  uiMonth = ttMeasure[0]["uiMonth"]
  uiDays  = ttMeasure[0]["uiDays"]
  uiHour  = ttMeasure[0]["uiHour"]
  uiMin   = ttMeasure[0]["uiMin"]
  uiSec   = ttMeasure[0]["uiSec"]
  sSerieName = "%02u%02u%02u%02u%02u%02u"%(uiYear,uiMonth,uiDays,uiHour,uiMin,uiSec)

  # Si série existe
  if( not "serie" in self.tPrj["tSensor"][sSerialNumber] ):
   self.tPrj["tSensor"][sSerialNumber]["serie"] = {}
  if( not sSerieName in self.tPrj["tSensor"][sSerialNumber]["serie"] ):
   self.tPrj["tSensor"][sSerialNumber]["serie"][sSerieName] = {}
   self.tPrj["tSensor"][sSerialNumber]["serie"][sSerieName]["data"] = []
   # Correction
   self.tPrj["tSensor"][sSerialNumber]["serie"][sSerieName]["sBaroCorrection"]         = "None"
   self.tPrj["tSensor"][sSerialNumber]["serie"][sSerieName]["xBaroCorrectionValue"]    = ""
   self.tPrj["tSensor"][sSerialNumber]["serie"][sSerieName]["sDensityCorrection"]      = "Temp only"
   self.tPrj["tSensor"][sSerialNumber]["serie"][sSerieName]["fDensityCorrectionValue"] = ""
   self.tPrj["tSensor"][sSerialNumber]["serie"][sSerieName]["uiOffsetCorrection"]      = 1
   self.tPrj["tSensor"][sSerialNumber]["serie"][sSerieName]["sOffsetCorrectionValue"]  = ""

  # Taille de la série de donnée
  uiSerieSize = len(self.tPrj["tSensor"][sSerialNumber]["serie"][sSerieName]["data"])

  # Si la série n'existait pas ou que pas la même taille
  if( len(ttMeasure) != uiSerieSize ):
   self.tPrj["tSensor"][sSerialNumber]["serie"][sSerieName]["data"] = []
   # Parcourt de la mesure
   for tSample in ttMeasure:
    print(tSample)
    uiYear  = tSample["uiYear"]
    uiMonth = tSample["uiMonth"]
    uiDays  = tSample["uiDays"]
    uiHour  = tSample["uiHour"]
    uiMin   = tSample["uiMin"]
    uiSec   = tSample["uiSec"]
    uiMSec  = tSample["uiMSec"]
    #sDateTime = ""%( uiYear,  )

    fTemperature = tSample["fTemperature"]
    fPressure    = tSample["fPressure"]
    if( ttConfig["PRODUCT"]["bECSensor"] ):
     fEC = tSample["fEC"]
     tLine = {"uiYear":  uiYear,
              "uiMonth": uiMonth,
              "uiDays":  uiDays,
              "uiHour":  uiHour,
              "uiMin":   uiMin,
              "uiSec":   uiSec,
              "uiMSec":  uiMSec,
              "fTemperature":fTemperature,
              "fPressure":fPressure,
              "fEC":fEC}
    else:
     tLine = {"uiYear":  uiYear,
              "uiMonth": uiMonth,
              "uiDays":  uiDays,
              "uiHour":  uiHour,
              "uiMin":   uiMin,
              "uiSec":   uiSec,
              "uiMSec":  uiMSec,
              "fTemperature":fTemperature,
              "fPressure":fPressure}

    self.tPrj["tSensor"][sSerialNumber]["serie"][sSerieName]["data"].append(tLine)


  print(self.tPrj)
  # Sauvegarde
  self.saveProject()

 #----------------------------------------------
 # Export des données en CSV
 #----------------------------------------------
 def exportAllDataFromSensorToCSV( self, sFileName, sSN ):
  print("-- TLvlDataPrj > exportAllDataFromSensorToCSV --")

  # Parcourt de la liste des séries
  for sSerie in self.tPrj["tSensor"][sSN]["serie"]:
   # Export de la série de donnée
   self.exportDataToCSV( sFileName, sSN, sSerie )

 #----------------------------------------------
 # Export des données en CSV
 #----------------------------------------------
 def exportDataToCSV( self, sFileName, sSN, sSerie ):
  print("-- TLvlDataPrj > exportDataToCSV --")

  self.cSeparator = ','

  # Test si le fichier existe
  if( not os.path.exists(sFileName) ):
   # Tag
   self.uiCpt = 0
   # Init en-tête
   tFirstLine = []
   tFirstLine.append("Site Indent")
   tFirstLine.append("Serial number")
   tFirstLine.append("Latitude")
   tFirstLine.append("Longitude")
   tFirstLine.append("Altitude")
   tSecondLine = []
   tSecondLine.append(self.tPrj["tSensor"][sSN]["sSiteID"])
   tSecondLine.append(self.tPrj["tSensor"][sSN]["sSN"])
   tSecondLine.append(self.tPrj["tSensor"][sSN]["sLatitude"])
   tSecondLine.append(self.tPrj["tSensor"][sSN]["sLongitude"])
   tSecondLine.append(self.tPrj["tSensor"][sSN]["sAltitude"])

   # Fichier à écrire
   #for ucChannel in range(tConfig["sensor"]["channelNumber"]) :
   # tFirstLine.append( "CH"+str(ucChannel)+":"+str(tConfig["channel"][ucChannel]["name"])+"("+str(tConfig["channel"][ucChannel]["unit"])+")" )

   tThirdLine = []
   ucChannel = 0
   #tThirdLine.append("Tag")
   tThirdLine.append("Date & Time")
   #tThirdLine.append("Battery Voltage")
   #tThirdLine.append("Cleaned")
   #if( ttConfig["CALCULATED"]["DEPTH"]["bM"] ):
   tThirdLine.append("Pressure (cmH2O)")
   #if( ttConfig["CALCULATED"]["DEPTH"]["bF"] ):
   # tThirdLine.append("Pressure (f)")
   #if( ttConfig["CALCULATED"]["TEMP"]["bC"] ):
   tThirdLine.append("Temp (C)")
   #if( ttConfig["CALCULATED"]["TEMP"]["bF"] ):
   # tThirdLine.append("Temp (F)")
   # EC
   if( self.tPrj["tSensor"][sSN]["bECSensor"] ):
    tThirdLine.append("Sal (PSU)")
    tThirdLine.append("EC (uS 25C)")

   # Ecriture dans le fichier
   with open(sFileName, 'w', newline='') as tCsvFileHandler:
    writer = csv.writer(tCsvFileHandler, delimiter=self.cSeparator)
    writer.writerows([tFirstLine])
    writer.writerows([tSecondLine])
    writer.writerows([""])
    writer.writerows([tThirdLine])
    #writer.writerows(ttLine)

  # Initialisation du tableau de ligne
  ttLine = []
  # Parcourt des échantillons
  for uiCpt in range( len(self.tPrj["tSensor"][sSN]["serie"][sSerie]["data"]) ) :
   # Init d'une nouvelle ligne
   ttLine.append([])
   # Formattage de la date
   uiYear  = self.tPrj["tSensor"][sSN]["serie"][sSerie]["data"][uiCpt]["uiYear"]
   uiMonth = self.tPrj["tSensor"][sSN]["serie"][sSerie]["data"][uiCpt]["uiMonth"]
   uiDays  = self.tPrj["tSensor"][sSN]["serie"][sSerie]["data"][uiCpt]["uiDays"]
   uiHour  = self.tPrj["tSensor"][sSN]["serie"][sSerie]["data"][uiCpt]["uiHour"]
   uiMin   = self.tPrj["tSensor"][sSN]["serie"][sSerie]["data"][uiCpt]["uiMin"]
   uiSec   = self.tPrj["tSensor"][sSN]["serie"][sSerie]["data"][uiCpt]["uiSec"]
   uiMSec  = self.tPrj["tSensor"][sSN]["serie"][sSerie]["data"][uiCpt]["uiMSec"]
   #tUtc = datetime.now()
   sDatetime = ( "%02u/%02u/%02u %02u:%02u:%02u.%02u" ) % ( uiYear, uiMonth, uiDays, uiHour, uiMin, uiSec, uiMSec )
   ttLine[uiCpt].append(sDatetime)

   # Pression
   ttLine[uiCpt].append( self.tPrj["tSensor"][sSN]["serie"][sSerie]["data"][uiCpt]["fPressure"] )
   # Temperature
   ttLine[uiCpt].append( self.tPrj["tSensor"][sSN]["serie"][sSerie]["data"][uiCpt]["fTemperature"] )
   # EC
   if( self.tPrj["tSensor"][sSN]["bECSensor"] ):
    # EC
    ttLine[uiCpt].append( self.tPrj["tSensor"][sSN]["serie"][sSerie]["data"][uiCpt]["fEC"] )

  # Ecriture dans le fichier
  with open(sFileName, 'a', newline='') as tCsvFileHandler:
   writer = csv.writer(tCsvFileHandler, delimiter=self.cSeparator)
   writer.writerows(ttLine)

 #----------------------------------------------
 # Liste des Baro
 #----------------------------------------------
 def tsFGetBaroListBySN( self ):
  print("-- getBaroListBySN --")
  # Init de l'objet
  self.tsBaroList = []
  # Parcourt des capteurs
  for sSerialNumber in self.tPrj["tSensor"]:
   # Si capteur Baro
   if( self.tPrj["tSensor"][sSerialNumber]["bBaro"] ):
    # Ajout
    self.tsBaroList.append(sSerialNumber)
  # Retourne la liste
  return( self.tsBaroList )

 #----------------------------------------------
 # Baro correction change
 #----------------------------------------------
 def bFSetCorrectionChange( self, sSN, sSerie, sCorrectionType, sBaroSN, fFixedValue ):
  print("-- vFSetCorrectionChange --")
  bResult = False

  #-- Baro --
  if( sCorrectionType == "Baro" ):
   # Baro List
   tBaroList = self.tsFGetBaroListBySN()
   # Vérification que le BaroSN existe
   for sBaroIndex in tBaroList:
    # Si Baro existe
    if( sBaroIndex == sBaroSN ):
     # Sauvegarde OK
     self.tPrj["tSensor"][sSN]["serie"][sSerie]["sBaroCorrection"] = sCorrectionType
     self.tPrj["tSensor"][sSN]["serie"][sSerie]["xBaroCorrectionValue"] = sBaroSN
     # Sauvegarde dans le fichier
     self.saveProject()
     # OK
     bResult = True

  #-- Fixed --
  if( sCorrectionType == "Fixed" ):
   # Sauvegarde OK
   self.tPrj["tSensor"][sSN]["serie"][sSerie]["sBaroCorrection"] = sCorrectionType
   self.tPrj["tSensor"][sSN]["serie"][sSerie]["xBaroCorrectionValue"] = "%.3f"%fFixedValue
   # OK
   bResult = True

  #-- None --
  if( sCorrectionType == "None" ):
   # Sauvegarde OK
   self.tPrj["tSensor"][sSN]["serie"][sSerie]["sBaroCorrection"] = sCorrectionType
   # OK
   bResult = True

  #-- Logged Zeros --
  if( sCorrectionType == "Logged Zeros" ):
   # Sauvegarde OK
   self.tPrj["tSensor"][sSN]["serie"][sSerie]["sBaroCorrection"] = sCorrectionType
   # OK
   bResult = True

  # Sauvegarde dans le fichier
  self.saveProject()
  # OK
  return( True )

