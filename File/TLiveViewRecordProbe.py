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
  #-- AquaPlus
  if( ttConfig["PRODUCT"]["uiModel"] == 53 ):
   # Appel de la fonction de création de fichier
   self.vFCreateNewFileAquaPlus( ttConfig )
  #-- AP-Lite
  elif( ttConfig["PRODUCT"]["uiModel"] == 30 ):
   # Appel de la fonction de création de fichier
   self.vFCreateNewFileAPLite( ttConfig )
  #-- Autres probes
  else:
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
  #-- AquaPlus
  if( ttConfig["PRODUCT"]["uiModel"] == 53 ):
   # Appel de la fonction de création de fichier
   self.vFCreateNewFileAquaPlus( ttConfig )
  #-- AP-Lite
  elif( ttConfig["PRODUCT"]["uiModel"] == 30 ):
   # Appel de la fonction de création de fichier
   self.vFCreateNewFileAPLite( ttConfig )
  #-- Autres probes
  else:
   # Appel de la fonction de création de fichier
   self.vFCreateNewFile( ttConfig )

 #----------------------------------------------
 # Création d'un nouveau fichier
 #----------------------------------------------
 def vFCreateNewFileAquaPlus( self, ttConfig ):
  print("-- TCSVRecorded > vFCreateNewFileAquaPlus --")
  # Tag
  self.uiCpt = 0
  # Init en-tête
  tFirstLine = []
  tFirstLine.append("TAB delimited data file. Format the Date & Time column as dd/mm/yyyy hh:mm:ss to see the seconds values")
  tDummyLine = []
  tDummyLine.append("")
  tSecondLine = []
  ucChannel = 0
  tSecondLine.append("Date & Time")
  if( ttConfig["CALCULATED"]["TEMP"]["bC"] ):
   tSecondLine.append("Temp(C)")
  if( ttConfig["CALCULATED"]["TEMP"]["bF"] ):
   tSecondLine.append("Temp(F)")
  tSecondLine.append("Baro(mB)")
  tSecondLine.append("DO(mg/l)")
  tSecondLine.append("DO(%sat)")
  tSecondLine.append("EC(uS/cm)")
  #tSecondLine.append("Sal(PSU)")
  # Ecriture dans le fichier
  with open(self.sFileName, 'w', newline='') as tCsvFileHandler:
   writer = csv.writer(tCsvFileHandler, delimiter=self.cSeparator)
   writer.writerows([tFirstLine])
   writer.writerows([tDummyLine])
   writer.writerows([tSecondLine])

 #----------------------------------------------
 # Création d'un nouveau fichier AP-Lite
 #----------------------------------------------
 def vFCreateNewFileAPLite( self, ttConfig ):
  print("-- TCSVRecorded > vFCreateNewFileAPLite --")
  # Tag
  self.uiCpt = 0
  # Init en-tête
  tFirstLine = []
  tFirstLine.append("TAB delimited data file. Format the Date & Time column as dd/mm/yyyy hh:mm:ss to see the seconds values")
  tDummyLine = []
  tDummyLine.append("")
  tSecondLine = []
  ucChannel = 0
  tSecondLine.append("Date & Time")
  if( ttConfig["CALCULATED"]["TEMP"]["bC"] ):
   tSecondLine.append("Temp(C)")
  if( ttConfig["CALCULATED"]["TEMP"]["bF"] ):
   tSecondLine.append("Temp(F)")
  #tSecondLine.append("Baro(mB)")
  #tSecondLine.append("SSG(dt)")
  #tSecondLine.append("TDS(mg/L)")
  # Selection des labels
  if(    ( ttConfig["PRODUCT"]["uiAUXNumber"] > 0 )
     and ( ttConfig["SENSOR"]["AUX1"]["sIndex"] != "EMPTY" ) ):
   tSecondLine.append(ttConfig["SENSOR"]["AUX1"]["sIndex"]+"("+str(ttConfig["SENSOR"]["AUX1"]["sUnit"])+")")
  # Ecriture dans le fichier
  with open(self.sFileName, 'w', newline='') as tCsvFileHandler:
   writer = csv.writer(tCsvFileHandler, delimiter=self.cSeparator)
   writer.writerows([tFirstLine])
   writer.writerows([tDummyLine])
   writer.writerows([tSecondLine])

 #----------------------------------------------
 # Création d'un nouveau fichier
 #----------------------------------------------
 def vFCreateNewFile( self, ttConfig ):
  print("-- TCSVRecorded > vFCreateNewFile --")
  # Tag
  self.uiCpt = 0
  # Init en-tête
  tFirstLine = []
  tFirstLine.append("TAB delimited data file. Format the Date & Time column as dd/mm/yyyy hh:mm:ss to see the seconds values")

  tDummyLine = []
  tDummyLine.append("")

  tSecondLine = []
  ucChannel = 0
  tSecondLine.append("Date & Time")
  if( ttConfig["CALCULATED"]["TEMP"]["bC"] ):
   tSecondLine.append("Temp(C)")
  if( ttConfig["CALCULATED"]["TEMP"]["bF"] ):
   tSecondLine.append("Temp(F)")
  # Si AP-700-D / AP-800-D / AP-2000-D / AP-5000 / AP-6K/7K/Pro
  if(  ( ttConfig["PRODUCT"]["uiModel"] == 60 )    # AP-700-D
    or ( ttConfig["PRODUCT"]["uiModel"] == 70 )    # AP-800-D
    or ( ttConfig["PRODUCT"]["uiModel"] == 20 )    # AP-2000-D
    or ( ttConfig["PRODUCT"]["uiModel"] == 59 )    # AP-5000
    or ( ttConfig["PRODUCT"]["uiModel"] == 29 ) ): # AP-6K/7K/Pro
   if( ttConfig["CALCULATED"]["DEPTH"]["bM"] ):
    tSecondLine.append("Depth(m)")
   if( ttConfig["CALCULATED"]["DEPTH"]["bF"] ):
    tSecondLine.append("Depth(f)")
  tSecondLine.append("Baro(mB)")
  tSecondLine.append("pH")
  tSecondLine.append("pH mV(mV)")
  tSecondLine.append("ORP(mV)")
  tSecondLine.append("DO(mg/l)")
  tSecondLine.append("DO(%sat)")
  tSecondLine.append("EC(uS/cm)")
  #tSecondLine.append("Ammonia (mg/L)")
  tSecondLine.append("Sal(PSU)")
  tSecondLine.append("SSG(dt)")
  tSecondLine.append("TDS(mg/L)")
  # Selection des labels
  if(    ( ttConfig["PRODUCT"]["uiAUXNumber"] > 0 )
     and ( ttConfig["SENSOR"]["AUX1"]["sIndex"] != "EMPTY" ) ):
   tSecondLine.append(ttConfig["SENSOR"]["AUX1"]["sIndex"]+"("+str(ttConfig["SENSOR"]["AUX1"]["sUnit"])+")")
  # Selection des labels
  if(    ( ttConfig["PRODUCT"]["uiAUXNumber"] > 1 )
     and ( ttConfig["SENSOR"]["AUX2"]["sIndex"] != "EMPTY" ) ):
   tSecondLine.append(ttConfig["SENSOR"]["AUX2"]["sIndex"]+"("+str(ttConfig["SENSOR"]["AUX2"]["sUnit"])+")")
  # Selection des labels
  if(    ( ttConfig["PRODUCT"]["uiAUXNumber"] > 2 )
     and ( ttConfig["SENSOR"]["AUX3"]["sIndex"] != "EMPTY" ) ):
   tSecondLine.append(ttConfig["SENSOR"]["AUX3"]["sIndex"]+"("+str(ttConfig["SENSOR"]["AUX3"]["sUnit"])+")")
  # Selection des labels
  if(    ( ttConfig["PRODUCT"]["uiAUXNumber"] > 3 )
     and ( ttConfig["SENSOR"]["AUX4"]["sIndex"] != "EMPTY" ) ):
   tSecondLine.append(ttConfig["SENSOR"]["AUX4"]["sIndex"]+"("+str(ttConfig["SENSOR"]["AUX4"]["sUnit"])+")")
  # Selection des labels
  if(    ( ttConfig["PRODUCT"]["uiAUXNumber"] > 4 )
     and ( ttConfig["SENSOR"]["AUX5"]["sIndex"] != "EMPTY" ) ):
   tSecondLine.append(ttConfig["SENSOR"]["AUX5"]["sIndex"]+"("+str(ttConfig["SENSOR"]["AUX5"]["sUnit"])+")")
  # Selection des labels
  if(    ( ttConfig["PRODUCT"]["uiAUXNumber"] > 5 )
     and ( ttConfig["SENSOR"]["AUX6"]["sIndex"] != "EMPTY" ) ):
   tSecondLine.append(ttConfig["SENSOR"]["AUX6"]["sIndex"]+"("+str(ttConfig["SENSOR"]["AUX6"]["sUnit"])+")")

  # Ecriture dans le fichier
  with open(self.sFileName, 'w', newline='') as tCsvFileHandler:
   writer = csv.writer(tCsvFileHandler, delimiter=self.cSeparator)
   writer.writerows([tFirstLine])
   writer.writerows([tDummyLine])
   writer.writerows([tSecondLine])

 #----------------------------------------------
 # Création d'un nouveau fichier
 #----------------------------------------------
 def vFAddSample( self, ttConfig ):
  #-- AquaPlus
  if( ttConfig["PRODUCT"]["uiModel"] == 53 ):
   # Appel de la fonction de création de fichier
   self.vFAddSampleAquaPlus( ttConfig )
  #-- AP-Lite
  elif( ttConfig["PRODUCT"]["uiModel"] == 30 ):
   # Appel de la fonction de création de fichier
   self.vFAddSampleAPLite( ttConfig )
  #-- Autres probes
  else:
   # Appel de la fonction de création de fichier
   self.vFAddSampleProbe( ttConfig )

 #----------------------------------------------
 # Création d'un nouveau fichier
 #----------------------------------------------
 def vFAddSampleAquaPlus( self, ttConfig ):
  print("-- TCSVRecorded > vFAddSampleAquaPlus --")
  print('ttConfig["PRODUCT"]["uiModel"] = %d'%ttConfig["PRODUCT"]["uiModel"])

  tUtc = datetime.now()
  sDatetimeInfo  = tUtc.strftime( '%y/%m/%d %H:%M:%S' )
  # Tag
  self.uiCpt += 1
  # Ecriture dans le fichier
  with open(self.sFileName, 'a', newline='') as tCsvFileHandler:
   writer = csv.writer(tCsvFileHandler, delimiter=self.cSeparator)
   # Tag
   tLine = []
   tLine.append(sDatetimeInfo)
   if( ttConfig["CALCULATED"]["TEMP"]["bC"] ):
    tLine.append( "%.2f" % ttConfig["SENSOR"]["TEMP"]["fResult"] )
   if( ttConfig["CALCULATED"]["TEMP"]["bF"] ):
    tLine.append( "%.2f" % ttConfig["CALCULATED"]["TEMP"]["fTempF"] )
   tLine.append( ttConfig["SENSOR"]["Baro"]["fResult"] )
   tLine.append( "%.2f" % ttConfig["SENSOR"]["DO"]["fResult"] )     # DO
   tLine.append( "%.1f" % ttConfig["SENSOR"]["DO Sat"]["fResult"] ) # DO_PC
   if( ttConfig["CALCULATED"]["EC"]["sTSelect"] == "25 C" ):
    tLine.append( "%.0f" % ttConfig["CALCULATED"]["EC"]["fEC_25"] )
   elif( ttConfig["CALCULATED"]["EC"]["sTSelect"] == "20 C" ):
    tLine.append( "%.0f" % ttConfig["CALCULATED"]["EC"]["fEC_20"] )
   else:
    tLine.append( "%.0f" % ttConfig["SENSOR"]["EC"]["fResult"] )
   #tLine.append( "%.2f" % ttConfig["CALCULATED"]["Salinity"]["fResult"] )
   # Ecriture d'une nouvelle ligne
   writer.writerows([tLine])

 #----------------------------------------------
 # Création d'un nouveau fichier
 #----------------------------------------------
 def vFAddSampleAPLite( self, ttConfig ):
  print("-- TCSVRecorded > vFAddSampleAPLite --")
  print('ttConfig["PRODUCT"]["uiModel"] = %d'%ttConfig["PRODUCT"]["uiModel"])

  tUtc = datetime.now()
  sDatetimeInfo  = tUtc.strftime( '%y/%m/%d %H:%M:%S' )
  # Tag
  self.uiCpt += 1
  # Ecriture dans le fichier
  with open(self.sFileName, 'a', newline='') as tCsvFileHandler:
   writer = csv.writer(tCsvFileHandler, delimiter=self.cSeparator)
   # Tag
   tLine = []
   tLine.append(sDatetimeInfo)
   if( ttConfig["CALCULATED"]["TEMP"]["bC"] ):
    tLine.append( "%.2f" % ttConfig["SENSOR"]["TEMP"]["fResult"] )
   if( ttConfig["CALCULATED"]["TEMP"]["bF"] ):
    tLine.append( "%.2f" % ttConfig["CALCULATED"]["TEMP"]["fTempF"] )
   #tLine.append( ttConfig["SENSOR"]["Baro"]["fResult"] )
   #tLine.append( "%.2f" % ttConfig["CALCULATED"]["SSG"]["fResult"] )
   #tLine.append( "%.2f" % ttConfig["CALCULATED"]["TDS"]["fResult"] )
   if(   ( ttConfig["PRODUCT"]["uiAUXNumber"] > 0 )
     and ( ttConfig["SENSOR"]["AUX1"]["sIndex"] != "EMPTY" ) ):
    tLine.append( "%.2f" % ttConfig["SENSOR"]["AUX1"]["fResult"] )
   # Ecriture d'une nouvelle ligne
   writer.writerows([tLine])

 #----------------------------------------------
 # Création d'un nouveau fichier
 #----------------------------------------------
 def vFAddSampleProbe( self, ttConfig ):
  print("-- TCSVRecorded > vFAddSample --")
  print('ttConfig["PRODUCT"]["uiModel"] = %d'%ttConfig["PRODUCT"]["uiModel"])

  tUtc = datetime.now()
  sDatetimeInfo  = tUtc.strftime( '%y/%m/%d %H:%M:%S' )
  # Tag
  self.uiCpt += 1

  # Ecriture dans le fichier
  with open(self.sFileName, 'a', newline='') as tCsvFileHandler:
   writer = csv.writer(tCsvFileHandler, delimiter=self.cSeparator)
   # Tag
   tLine = []
   tLine.append(sDatetimeInfo)

   if( ttConfig["CALCULATED"]["TEMP"]["bC"] ):
    tLine.append( "%.2f" % ttConfig["SENSOR"]["TEMP"]["fResult"] )
   if( ttConfig["CALCULATED"]["TEMP"]["bF"] ):
    tLine.append( "%.2f" % ttConfig["CALCULATED"]["TEMP"]["fTempF"] )

   # Si AP-700-D / AP-800-D / AP-2000-D / AP-5000 / AP-6K/7K/Pro
   if(  ( ttConfig["PRODUCT"]["uiModel"] == 60 )    # AP-700-D
     or ( ttConfig["PRODUCT"]["uiModel"] == 70 )    # AP-800-D
     or ( ttConfig["PRODUCT"]["uiModel"] == 20 )    # AP-2000-D
     or ( ttConfig["PRODUCT"]["uiModel"] == 59 )    # AP-5000
     or ( ttConfig["PRODUCT"]["uiModel"] == 29 ) ): # AP-6K/7K/Pro
    if( ttConfig["CALCULATED"]["DEPTH"]["bM"] ):
     tLine.append( "%.3f" % ttConfig["SENSOR"]["Depth"]["fResult"] )
    if( ttConfig["CALCULATED"]["DEPTH"]["bF"] ):
     tLine.append( "%.3f" % ttConfig["CALCULATED"]["DEPTH"]["fDepthF"] )
   tLine.append( ttConfig["SENSOR"]["Baro"]["fResult"] )
   tLine.append( "%.2f" % ttConfig["SENSOR"]["PH"]["fResult"] )     # pH
   tLine.append( "%.1f" % ttConfig["SENSOR"]["PHmv"]["fResult"] )   # pHmv
   tLine.append( "%.1f" % ttConfig["SENSOR"]["ORP"]["fResult"] )    # ORP
   tLine.append( "%.2f" % ttConfig["SENSOR"]["DO"]["fResult"] )     # DO
   tLine.append( "%.1f" % ttConfig["SENSOR"]["DO Sat"]["fResult"] ) # DO_PC

   if( ttConfig["CALCULATED"]["EC"]["sTSelect"] == "25 C" ):
    tLine.append( "%.0f" % ttConfig["CALCULATED"]["EC"]["fEC_25"] )
   elif( ttConfig["CALCULATED"]["EC"]["sTSelect"] == "20 C" ):
    tLine.append( "%.0f" % ttConfig["CALCULATED"]["EC"]["fEC_20"] )
   else:
    tLine.append( "%.0f" % ttConfig["SENSOR"]["EC"]["fResult"] )

   tLine.append( "%.2f" % ttConfig["CALCULATED"]["Salinity"]["fResult"] )
   tLine.append( "%.2f" % ttConfig["CALCULATED"]["SSG"]["fResult"] )
   tLine.append( "%.2f" % ttConfig["CALCULATED"]["TDS"]["fResult"] )

   if(   ( ttConfig["PRODUCT"]["uiAUXNumber"] > 0 )
     and ( ttConfig["SENSOR"]["AUX1"]["sIndex"] != "EMPTY" ) ):
    tLine.append( "%.2f" % ttConfig["SENSOR"]["AUX1"]["fResult"] )
   if(   ( ttConfig["PRODUCT"]["uiAUXNumber"] > 1 )
     and ( ttConfig["SENSOR"]["AUX2"]["sIndex"] != "EMPTY" ) ):
    tLine.append( "%.2f" % ttConfig["SENSOR"]["AUX2"]["fResult"] )
   if(   ( ttConfig["PRODUCT"]["uiAUXNumber"] > 2 )
     and ( ttConfig["SENSOR"]["AUX3"]["sIndex"] != "EMPTY" ) ):
    tLine.append( "%.2f" % ttConfig["SENSOR"]["AUX3"]["fResult"] )
   if(   ( ttConfig["PRODUCT"]["uiAUXNumber"] > 3 )
     and ( ttConfig["SENSOR"]["AUX4"]["sIndex"] != "EMPTY" ) ):
    tLine.append( "%.2f" % ttConfig["SENSOR"]["AUX4"]["fResult"] )
   if(   ( ttConfig["PRODUCT"]["uiAUXNumber"] > 4 )
     and ( ttConfig["SENSOR"]["AUX5"]["sIndex"] != "EMPTY" ) ):
    tLine.append( "%.2f" % ttConfig["SENSOR"]["AUX5"]["fResult"] )
   if(   ( ttConfig["PRODUCT"]["uiAUXNumber"] > 5 )
     and ( ttConfig["SENSOR"]["AUX6"]["sIndex"] != "EMPTY" ) ):
    tLine.append( "%.2f" % ttConfig["SENSOR"]["AUX6"]["fResult"] )
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




