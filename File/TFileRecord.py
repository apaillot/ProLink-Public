# This Python file uses the following encoding: utf-8

#============================================================================#
# Librairies système
#============================================================================#
import sys
import csv
from datetime import datetime

#============================================================================#
# Librairies Qt
#============================================================================#
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QMetaObject)
from PySide6.QtCore import Slot

#============================================================================#
# Librairies Utilisateur
#============================================================================#

#============================================================================#
# Variable
#============================================================================#

#------------------------------------------------------------------------
# Controleur de main Windows
#------------------------------------------------------------------------
class TFileRecord:
 #----------------------------------------------
 # Init : création de l'objet
 #----------------------------------------------
 def __init__(self):
  # Nom du fichier courrant
  self.sFileName = ""
  # Separateur par défaut
  self.cSeparator = "\t"
  self.sFileExtension = ".csv"

 #----------------------------------------------
 # Création d'un nouveau fichier
 #----------------------------------------------
 def vFCreateNewFileTSV( self, sFileName, ttConfig, ttMeasure ):
  print("-- vFCreateNewFileTSV --")
  self.cSeparator = "\t"
  self.sFileExtension = ".tab"
  self.sFileName = sFileName
  # Appel de la fonction de création de fichier
  self.vFCreateNewFile( ttConfig, ttMeasure )

 #----------------------------------------------
 # Création d'un nouveau fichier
 #----------------------------------------------
 def vFCreateNewFileCSV( self, sFileName, ttConfig, ttMeasure ):
  print("-- vFCreateNewFileCSV --")
  self.cSeparator = ","
  self.sFileExtension = ".csv"
  self.sFileName = sFileName
  # Appel de la fonction de création de fichier
  self.vFCreateNewFile( ttConfig, ttMeasure )

 #----------------------------------------------
 # Création d'un nouveau fichier
 #----------------------------------------------
 def vFCreateNewFile( self, ttConfig, ttMeasure ):
  print("-- TCSVRecorded > vFCreateNewFile --")
  print(ttMeasure)
  print("-- id(ttMeasure) 2 --")
  print(id(ttMeasure))

  tFirstLine = []
  tFirstLine.append(ttConfig["PRODUCT"]["sModel"])
  tFirstLine.append("S/N:"+ttConfig["PRODUCT"]["sPSN1"])
  tFirstLine.append("Site:"+ttConfig["PRODUCT"]["sSiteID"])
  tFirstLine.append("Site Lat:"+ttConfig["PRODUCT"]["sSiteLat"])
  tFirstLine.append("Site Lon:"+ttConfig["PRODUCT"]["sSiteLong"])
  # Fichier à écrire
  #for ucChannel in range(tConfig["sensor"]["channelNumber"]) :
  # tFirstLine.append( "CH"+str(ucChannel)+":"+str(tConfig["channel"][ucChannel]["name"])+"("+str(tConfig["channel"][ucChannel]["unit"])+")" )

  tSecondLine = []
  ucChannel = 0
  tSecondLine.append("Tag")
  tSecondLine.append("Date & Time")
  if( ttMeasure[0]["bBatt"] ):         tSecondLine.append("Battery Voltage")
  tSecondLine.append("Cleaned")
  if( ttMeasure[0]["bTemperature"] ):
   if( ttConfig["CALCULATED"]["TEMP"]["bC"] ):
    tSecondLine.append("Temp(C)")
   if( ttConfig["CALCULATED"]["TEMP"]["bF"] ):
    tSecondLine.append("Temp(F)")
  if( ttMeasure[0]["bDepth"] ):
   if( ttConfig["CALCULATED"]["DEPTH"]["bM"] ):
    tSecondLine.append("Depth(m)")
   if( ttConfig["CALCULATED"]["DEPTH"]["bF"] ):
    tSecondLine.append("Depth(f)")
  if( ttMeasure[0]["bBaro"] ):         tSecondLine.append("Baro (mB)")
  if( ttMeasure[0]["bpH"] ):           tSecondLine.append("pH")
  if( ttMeasure[0]["bpHmv"] ):         tSecondLine.append("pH mV (mV)")
  if( ttMeasure[0]["bORP"] ):          tSecondLine.append("ORP (mV)")
  if( ttMeasure[0]["bDO_PC"] ):        tSecondLine.append("DO (%sat)")
  if( ttMeasure[0]["bDO"] ):           tSecondLine.append("DO (mg/l)")
  if( ttMeasure[0]["bEC"] ):           tSecondLine.append("EC (uS/cm)")
  #if( ttMeasure[0]["bAmmonia"] ):      tSecondLine.append("Ammonia (mg/L)")
  if( ttMeasure[0]["bSalinity"] ):     tSecondLine.append("Sal (PSU)")
  if( ttMeasure[0]["bSSG"] ):          tSecondLine.append("SSG (dt)")
  if( ttMeasure[0]["bTDS"] ):          tSecondLine.append("TDS (mg/L)")
  # Selection des labels
  if(    ( ttConfig["PRODUCT"]["uiAUXNumber"] > 0 )
     and ( ttConfig["SENSOR"]["AUX1"]["sIndex"] != "EMPTY" ) ):
   if( ttMeasure[0]["bAUX1"] ):
    tSecondLine.append(ttConfig["SENSOR"]["AUX1"]["sIndex"]+" ("+str(ttConfig["SENSOR"]["AUX1"]["sUnit"])+")")
  # Selection des labels
  if(    ( ttConfig["PRODUCT"]["uiAUXNumber"] > 1 )
     and ( ttConfig["SENSOR"]["AUX2"]["sIndex"] != "EMPTY" ) ):
   if( ttMeasure[0]["bAUX2"] ):
    tSecondLine.append(ttConfig["SENSOR"]["AUX2"]["sIndex"]+" ("+str(ttConfig["SENSOR"]["AUX2"]["sUnit"])+")")
  # Selection des labels
  if(    ( ttConfig["PRODUCT"]["uiAUXNumber"] > 2 )
     and ( ttConfig["SENSOR"]["AUX3"]["sIndex"] != "EMPTY" ) ):
   if( ttMeasure[0]["bAUX3"] ):
    tSecondLine.append(ttConfig["SENSOR"]["AUX3"]["sIndex"]+" ("+str(ttConfig["SENSOR"]["AUX3"]["sUnit"])+")")
  # Selection des labels
  if(    ( ttConfig["PRODUCT"]["uiAUXNumber"] > 3 )
     and ( ttConfig["SENSOR"]["AUX4"]["sIndex"] != "EMPTY" ) ):
   if( ttMeasure[0]["bAUX4"] ):
    tSecondLine.append(ttConfig["SENSOR"]["AUX4"]["sIndex"]+" ("+str(ttConfig["SENSOR"]["AUX4"]["sUnit"])+")")
  # Selection des labels
  if(    ( ttConfig["PRODUCT"]["uiAUXNumber"] > 4 )
     and ( ttConfig["SENSOR"]["AUX5"]["sIndex"] != "EMPTY" ) ):
   if( ttMeasure[0]["bAUX5"] ):
    tSecondLine.append(ttConfig["SENSOR"]["AUX5"]["sIndex"]+" ("+str(ttConfig["SENSOR"]["AUX5"]["sUnit"])+")")
  # Selection des labels
  if(    ( ttConfig["PRODUCT"]["uiAUXNumber"] > 5 )
     and ( ttConfig["SENSOR"]["AUX6"]["sIndex"] != "EMPTY" ) ):
   if( ttMeasure[0]["bAUX6"] ):
    tSecondLine.append(ttConfig["SENSOR"]["AUX6"]["sIndex"]+" ("+str(ttConfig["SENSOR"]["AUX6"]["sUnit"])+")")
  # Ammonia
  if( ttConfig["CALCULATED"]["AMMONIA"]["bActivated"] ):
   tSecondLine.append("Ammonia (mg/L)")

  # Nom du fichier
  tUtc = datetime.now()
  sDatetimeInfo  = tUtc.strftime( '%y%m%d_%H%M%S' )

  # Ecriture dans le fichier
  with open(self.sFileName, 'w', newline='') as tCsvFileHandler:
   writer = csv.writer(tCsvFileHandler, delimiter=self.cSeparator)
   writer.writerows([tFirstLine])
   writer.writerows([tSecondLine])

   print("-- ttMeasure --")
   print(len(ttMeasure))
   # Parcourt de la donnée
   for uiCpt in range(0, len(ttMeasure)):
    # Tag
    tLine = []
    tLine.append(uiCpt+1)
    tLine.append(ttMeasure[uiCpt]["sDateTime"])
    if( ttMeasure[0]["bBatt"] ):         tLine.append(ttMeasure[uiCpt]["sBatteryLevel"])
    tLine.append(ttMeasure[uiCpt]["sCleaningFlag"])
    if( ttMeasure[0]["bTemperature"] ):
     if( ttConfig["CALCULATED"]["TEMP"]["bC"] ):
      tLine.append(ttMeasure[uiCpt]["sTempC"])
     if( ttConfig["CALCULATED"]["TEMP"]["bF"] ):
      tLine.append(ttMeasure[uiCpt]["sTempF"])
    if( ttMeasure[0]["bDepth"] ):
     if( ttConfig["CALCULATED"]["DEPTH"]["bM"] ):
      tLine.append(ttMeasure[uiCpt]["sDepthM"])
     if( ttConfig["CALCULATED"]["DEPTH"]["bF"] ):
      tLine.append(ttMeasure[uiCpt]["sDepthF"])
    if( ttMeasure[0]["bBaro"] ):         tLine.append(ttMeasure[uiCpt]["sBaro"])
    if( ttMeasure[0]["bpH"] ):           tLine.append(ttMeasure[uiCpt]["spH"])
    if( ttMeasure[0]["bpHmv"] ):         tLine.append(ttMeasure[uiCpt]["spHmV"])
    if( ttMeasure[0]["bORP"] ):          tLine.append(ttMeasure[uiCpt]["sORP"])
    if( ttMeasure[0]["bDO_PC"] ):        tLine.append(ttMeasure[uiCpt]["sDO_PC"])
    if( ttMeasure[0]["bDO"] ):           tLine.append(ttMeasure[uiCpt]["sDO"])
    if( ttMeasure[0]["bEC"] ):
     if( ttConfig["CALCULATED"]["EC"]["sTSelect"] == "25 C" ):
      tLine.append(ttMeasure[uiCpt]["sEC_25"])
     elif( ttConfig["CALCULATED"]["EC"]["sTSelect"] == "20 C" ):
      tLine.append(ttMeasure[uiCpt]["sEC_20"])
     else:
      tLine.append(ttMeasure[uiCpt]["sEC"])

    if( ttMeasure[0]["bSalinity"] ):     tLine.append(ttMeasure[uiCpt]["sSalinity"])
    if( ttMeasure[0]["bSSG"] ):          tLine.append(ttMeasure[uiCpt]["sSSG"])
    if( ttMeasure[0]["bTDS"] ):          tLine.append(ttMeasure[uiCpt]["sTDS"])

    if(   ( ttConfig["PRODUCT"]["uiAUXNumber"] > 0 )
      and ( ttConfig["SENSOR"]["AUX1"]["sIndex"] != "EMPTY" ) ):
     if( ttMeasure[0]["bAUX1"] ):
      tLine.append(ttMeasure[uiCpt]["sAUX1"])
    if(   ( ttConfig["PRODUCT"]["uiAUXNumber"] > 1 )
      and ( ttConfig["SENSOR"]["AUX2"]["sIndex"] != "EMPTY" ) ):
     if( ttMeasure[0]["bAUX2"] ):
      tLine.append(ttMeasure[uiCpt]["sAUX2"])
    if(   ( ttConfig["PRODUCT"]["uiAUXNumber"] > 2 )
      and ( ttConfig["SENSOR"]["AUX3"]["sIndex"] != "EMPTY" ) ):
     if( ttMeasure[0]["bAUX3"] ):
      tLine.append(ttMeasure[uiCpt]["sAUX3"])
    if(   ( ttConfig["PRODUCT"]["uiAUXNumber"] > 3 )
      and ( ttConfig["SENSOR"]["AUX4"]["sIndex"] != "EMPTY" ) ):
     if( ttMeasure[0]["bAUX4"] ):
      tLine.append(ttMeasure[uiCpt]["sAUX4"])
    if(   ( ttConfig["PRODUCT"]["uiAUXNumber"] > 4 )
      and ( ttConfig["SENSOR"]["AUX5"]["sIndex"] != "EMPTY" ) ):
     if( ttMeasure[0]["bAUX5"] ):
      tLine.append(ttMeasure[uiCpt]["sAUX5"])
    if(   ( ttConfig["PRODUCT"]["uiAUXNumber"] > 5 )
      and ( ttConfig["SENSOR"]["AUX6"]["sIndex"] != "EMPTY" ) ):
     if( ttMeasure[0]["bAUX6"] ):
      tLine.append(ttMeasure[uiCpt]["sAUX6"])
    # Ammonia
    if( ttConfig["CALCULATED"]["AMMONIA"]["bActivated"] ):
     tLine.append(ttMeasure[uiCpt]["sAUX7"])
    # Ecriture d'une nouvelle ligne
    writer.writerows([tLine])





