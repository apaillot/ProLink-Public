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
class TLiveViewRecord:
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
 def vFCreateNewFileTSV( self, sFileName, ttConfig ):
  print("-- vFCreateNewFileTSV --")
  self.cSeparator = "\t"
  self.sFileExtension = ".tab"
  self.sFileName = sFileName
  # Appel de la fonction de création de fichier
  self.vFCreateNewFile( ttConfig )

 #----------------------------------------------
 # Création d'un nouveau fichier
 #----------------------------------------------
 def vFCreateNewFileCSV( self, sFileName, ttConfig ):
  print("-- vFCreateNewFileCSV --")
  self.cSeparator = ","
  self.sFileExtension = ".csv"
  self.sFileName = sFileName
  # Appel de la fonction de création de fichier
  self.vFCreateNewFile( ttConfig )

 #----------------------------------------------
 # Création d'un nouveau fichier
 #----------------------------------------------
 def vFCreateNewFile( self, ttConfig ):
  print("-- TCSVRecorded > vFCreateNewFile --")
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
  tSecondLine.append(ttConfig["PRODUCT"]["sSiteID"])
  tSecondLine.append(ttConfig["PRODUCT"]["sSerialNumber"])

  if( ttConfig["PRODUCT"]["sLatitudeRef"] != "" ):
   sLatitudeRef = ttConfig["PRODUCT"]["sLatitudeRef"]
   iLatitudeDeg = ttConfig["PRODUCT"]["iLatitudeDeg"]
   iLatitudeMin = ttConfig["PRODUCT"]["iLatitudeMin"]
   iLatitudeSec = ttConfig["PRODUCT"]["iLatitudeSec"]
   sLatitude = "%s %02d %02d.%04u"%(sLatitudeRef, iLatitudeDeg, iLatitudeMin, iLatitudeSec)
  else:
   sLatitude = ""

  if( ttConfig["PRODUCT"]["sLongitudeRef"] != "" ):
   sLongitudeRef = ttConfig["PRODUCT"]["sLongitudeRef"]
   iLongitudeDeg = ttConfig["PRODUCT"]["iLongitudeDeg"]
   iLongitudeMin = ttConfig["PRODUCT"]["iLongitudeMin"]
   iLongitudeSec = ttConfig["PRODUCT"]["iLongitudeSec"]
   sLongitude = "%s %03d %02d.%04u"%(sLongitudeRef, iLongitudeDeg, iLongitudeMin, iLongitudeSec)
  else:
   sLongitude = ""

  sAltitude = "%d"%ttConfig["PRODUCT"]["iAltitude"]+" m"

  tSecondLine.append(sLatitude)
  tSecondLine.append(sLongitude)
  tSecondLine.append(sAltitude)




  # Fichier à écrire
  #for ucChannel in range(tConfig["sensor"]["channelNumber"]) :
  # tFirstLine.append( "CH"+str(ucChannel)+":"+str(tConfig["channel"][ucChannel]["name"])+"("+str(tConfig["channel"][ucChannel]["unit"])+")" )

  tThirdLine = []
  ucChannel = 0
  #tThirdLine.append("Tag")
  tThirdLine.append("Date & Time")
  #tThirdLine.append("Battery Voltage")
  #tThirdLine.append("Cleaned")
  if( ttConfig["CALCULATED"]["DEPTH"]["bM"] ):
   tThirdLine.append("Pressure (cmH2O)")
  if( ttConfig["CALCULATED"]["DEPTH"]["bF"] ):
   tThirdLine.append("Pressure (f)")
  if( ttConfig["CALCULATED"]["TEMP"]["bC"] ):
   tThirdLine.append("Temp (C)")
  if( ttConfig["CALCULATED"]["TEMP"]["bF"] ):
   tThirdLine.append("Temp (F)")
  # EC
  if( ttConfig["PRODUCT"]["bECSensor"] ):
   tThirdLine.append("Sal (PSU)")
   tThirdLine.append("EC (uS 25C)")

  # Ecriture dans le fichier
  with open(self.sFileName, 'w', newline='') as tCsvFileHandler:
   writer = csv.writer(tCsvFileHandler, delimiter=self.cSeparator)
   writer.writerows([tFirstLine])
   writer.writerows([tSecondLine])
   writer.writerows([""])
   writer.writerows([tThirdLine])

 #----------------------------------------------
 # Création d'un nouveau fichier
 #----------------------------------------------
 def vFAddSample( self, ttConfig ):
  print("-- TCSVRecorded > vFAddSample --")

  tUtc = datetime.now()
  sDatetimeInfo  = tUtc.strftime( '%y/%m/%d %H:%M:%S' )
  # Tag
  self.uiCpt += 1

  # Ecriture dans le fichier
  with open(self.sFileName, 'a', newline='') as tCsvFileHandler:
   writer = csv.writer(tCsvFileHandler, delimiter=self.cSeparator)

   #print("-- ttMeasure --")
   #print(len(ttMeasure))
   # Tag
   tLine = []
   #tLine.append(uiCpt+1)
   tLine.append(sDatetimeInfo)
   #tLine.append(ttMeasure[uiCpt]["sBatteryLevel"])
   #tLine.append(ttMeasure[uiCpt]["sCleaningFlag"])

   if( ttConfig["CALCULATED"]["DEPTH"]["bM"] ):
    tLine.append( "%.3f" % ttConfig["SENSOR"]["DEPTH"]["fResult"] )
   if( ttConfig["CALCULATED"]["DEPTH"]["bF"] ):
    tLine.append( "%.3f" % ttConfig["CALCULATED"]["DEPTH"]["fDepthF"] )
   if( ttConfig["CALCULATED"]["TEMP"]["bC"] ):
    tLine.append( "%.2f" % ttConfig["SENSOR"]["TEMP"]["fResult"] )
   if( ttConfig["CALCULATED"]["TEMP"]["bF"] ):
    tLine.append( "%.2f" % ttConfig["CALCULATED"]["TEMP"]["fTempF"] )


   # EC
   if( ttConfig["PRODUCT"]["bECSensor"] ):
    tLine.append( "%.2f" % ttConfig["CALCULATED"]["Salinity"]["fResult"] )
    if( ttConfig["CALCULATED"]["EC"]["sTSelect"] == "25 C" ):
     tLine.append( "%.0f" % ttConfig["CALCULATED"]["EC"]["fEC_25"] )
    elif( ttConfig["CALCULATED"]["EC"]["sTSelect"] == "20 C" ):
     tLine.append( "%.0f" % ttConfig["CALCULATED"]["EC"]["fEC_20"] )
    else:
     tLine.append( "%.0f" % ttConfig["SENSOR"]["EC"]["fResult"] )


   # Ecriture d'une nouvelle ligne
   writer.writerows([tLine])

 #----------------------------------------------
 # Création d'un nouveau raw
 #----------------------------------------------
 def vFCreateNewFileRaw( self, ttConfig, ttMeasureRaw ):
  print("-- vFCreateNewFileRaw --")
  #self.cSeparator = "\t"
  self.sFileExtension = ".asf"
  self.sFileName = "measure"+self.sFileExtension
  # Création du fichier binaire
  with open(self.sFileName, "wb") as file:
   # Ecriture de la data
   file.write(ttMeasureRaw)




