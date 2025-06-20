# This Python file uses the following encoding: utf-8

#============================================================================#
# Librairies système
#============================================================================#
import sys
import csv
from datetime import datetime, date, time

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
class TCalibReport:
 #----------------------------------------------
 # Init : création de l'objet
 #----------------------------------------------
 def __init__( self ):
  print("TCalibReport init")

 #----------------------------------------------
 # Add new temperature last point
 #----------------------------------------------
 #def vFCreateNewFile( self, ttConfig ):

 #----------------------------------------------
 # Création d'un nouveau fichier
 #----------------------------------------------
 def vFCreateNewFile( self, ttConfig, sFileName ):
  #-- AquaPlus
  if( ttConfig["PRODUCT"]["uiModel"] == 53 ):
   self.vFCreateNewFileAquaPlus( ttConfig, sFileName )
  #-- AP-Lite
  elif( ttConfig["PRODUCT"]["uiModel"] == 30 ):
   self.vFCreateNewFileProbeAPLite( ttConfig, sFileName )
  #-- Autres probes
  else:
   self.vFCreateNewFileProbe( ttConfig, sFileName )

 #----------------------------------------------
 # Création d'un nouveau fichier
 #----------------------------------------------
 def vFCreateNewFileProbeAPLite( self, ttConfig, sFileName ):
  print("-- vFCreateNewFileProbeAPLite --")

  f = open(sFileName, "w")

  tLines = []
  tLines.append("TAB delimited raw text file. Use the TAB key to align the columns in your word processor software.\n")
  tLines.append("\n")
  tLines.append("\n")
  tLines.append("AquaSonde Calibration Certificate\n")
  tLines.append("\n")
  tLines.append("Date: "+ datetime.now().strftime("%d/%m/%Y")+"\n")
  tLines.append("Time: "+datetime.now().strftime("%H:%M:%S")+"\n")
  tLines.append("Sonde Type: "+ttConfig["PRODUCT"]["sModel"]+"\n")
  tLines.append("Sonde S/N: "+ttConfig["PRODUCT"]["sPSN1"]+"\n")
  tLines.append("Sonde S/W Rev: "+ttConfig["PRODUCT"]["sPSW1"]+"\n")
  tLines.append("\n")
  tLines.append("Calibration Record\n")
  tLines.append("\n")
  tLines.append("Function\tValue\tTemp\tBaro\n\n")
  #sLine = "Sonde type:"
  #sLine += "Sonde type: "+self.ttConfig["PRODUCT"]["sModel"]

  #------
  # AUX1
  if( ttConfig["SENSOR"]["AUX1"]["sIndex"] != "EMPTY" ):
   #---
   # AUX1 - P1
   sLine  = ttConfig["SENSOR"]["AUX1"]["sIndex"]+" Point 1\t"
   if( "fTemp" in ttConfig["SENSOR"]["AUX1"]["Point"][0] ):
    sLine += "%.0fmV\t"%( ttConfig["SENSOR"]["AUX1"]["Point"][0]["uiCalReport"] )
    sLine += "%.2fC\t"%ttConfig["SENSOR"]["AUX1"]["Point"][0]["fTemp"]
    if( "fPressure" in ttConfig["SENSOR"]["AUX1"]["Point"][0] ):
     sLine += "%.0fmB\t\n"%( ttConfig["SENSOR"]["AUX1"]["Point"][0]["fPressure"] )
    else:
     sLine += "N/A\t\n"
   else:
    sLine += "N/A\tN/A\tN/A\n"
   tLines.append(sLine)
   #---
   # AUX1 - P2
   sLine  = ttConfig["SENSOR"]["AUX1"]["sIndex"]+" Point 2\t"
   if( "fTemp" in ttConfig["SENSOR"]["AUX1"]["Point"][1] ):
    sLine += "%.0fmV\t"%( ttConfig["SENSOR"]["AUX1"]["Point"][1]["uiCalReport"] )
    sLine += "%.2fC\t"%ttConfig["SENSOR"]["AUX1"]["Point"][1]["fTemp"]
    if( "fPressure" in ttConfig["SENSOR"]["AUX1"]["Point"][1] ):
     sLine += "%.0fmB\t\n"%( ttConfig["SENSOR"]["AUX1"]["Point"][1]["fPressure"] )
    else:
     sLine += "N/A\t\n"
   else:
    sLine += "N/A\tN/A\tN/A\n"
   tLines.append(sLine)
   #---
   # AUX1 - P3
   if( ttConfig["SENSOR"]["AUX1"]["ucPoint"] > 2 ):
    sLine  = ttConfig["SENSOR"]["AUX1"]["sIndex"]+" Point 3\t"
    if( "fTemp" in ttConfig["SENSOR"]["AUX1"]["Point"][2] ):
     sLine += "%.0fmV\t"%( ttConfig["SENSOR"]["AUX1"]["Point"][2]["uiCalReport"] )
     sLine += "%.2fC\t"%ttConfig["SENSOR"]["AUX1"]["Point"][2]["fTemp"]
     if( "fPressure" in ttConfig["SENSOR"]["AUX1"]["Point"][2] ):
      sLine += "%.0fmB\t\n"%( ttConfig["SENSOR"]["AUX1"]["Point"][2]["fPressure"] )
     else:
      sLine += "N/A\t\n"
    else:
     sLine += "N/A\tN/A\tN/A\n"
    tLines.append(sLine)
  else:
   tLines.append("EMPTY Point 1\tN/A\tN/A\tN/A\n")
   tLines.append("EMPTY Point 2\tN/A\tN/A\tN/A\n")
   tLines.append("EMPTY Point 3\tN/A\tN/A\tN/A\n")

  f.writelines(tLines)
  f.close()

 #----------------------------------------------
 # Création d'un nouveau fichier
 #----------------------------------------------
 def vFCreateNewFileAquaPlus( self, ttConfig, sFileName ):
  print("-- vFCreateNewFileAquaPlus --")
  print(id(ttConfig))

  f = open(sFileName, "w")

  tLines = []
  tLines.append("TAB delimited raw text file. Use the TAB key to align the columns in your word processor software.\n")
  tLines.append("\n")
  tLines.append("\n")
  tLines.append("AquaSonde Calibration Certificate\n")
  tLines.append("\n")
  tLines.append("Date: "+ datetime.now().strftime("%d/%m/%Y")+"\n")
  tLines.append("Time: "+datetime.now().strftime("%H:%M:%S")+"\n")
  tLines.append("Sonde Type: "+ttConfig["PRODUCT"]["sModel"]+"\n")
  tLines.append("Sonde S/N: "+ttConfig["PRODUCT"]["sPSN1"]+"\n")
  tLines.append("Sonde S/W Rev: "+ttConfig["PRODUCT"]["sPSW1"]+"\n")
  tLines.append("\n")
  tLines.append("Calibration Record\n")
  tLines.append("\n")
  tLines.append("Function\tValue\tTemp\tBaro\n\n")
  #sLine = "Sonde type:"
  #sLine += "Sonde type: "+self.ttConfig["PRODUCT"]["sModel"]
  #---
  # DO - 0%
  sLine  = "DO Zero Output\t"
  if( "fTemp" in ttConfig["SENSOR"]["DO"]["Point"][0] ):
   sLine += "%.1fmV\t"%( ttConfig["SENSOR"]["DO"]["Point"][0]["uiCalReport"]*1000 )
   sLine += "%.2f\t"%ttConfig["SENSOR"]["DO"]["Point"][0]["fTemp"]
   if( "fPressure" in ttConfig["SENSOR"]["DO"]["Point"][0] ):
    sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["DO"]["Point"][0]["fPressure"] )
   else:
    sLine += "N/A\t\n"
  else:
   sLine += "N/A\tN/A\tN/A\n"
  tLines.append(sLine)
  #---
  # DO - 100%
  print(ttConfig["SENSOR"]["DO"]["Point"])
  sLine  = "DO 100% Output\t"
  if( "fTemp" in ttConfig["SENSOR"]["DO"]["Point"][1] ):
   sLine += "%.1fmV\t"%( ttConfig["SENSOR"]["DO"]["Point"][1]["uiCalReport"]*1000 )
   sLine += "%.2fC\t"%ttConfig["SENSOR"]["DO"]["Point"][1]["fTemp"]
   if( "fPressure" in ttConfig["SENSOR"]["DO"]["Point"][1] ):
    sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["DO"]["Point"][1]["fPressure"] )
   else:
    sLine += "N/A\t\n"
  else:
   sLine += "N/A\tN/A\tN/A\n"
  tLines.append(sLine)
  #---
  # EC Cell Constant
  sLine  = "EC Cell Constant\t"
  if( "fTemp" in ttConfig["SENSOR"]["EC"]["Point"][0] ):
   sLine += "%.2f\t"%( ttConfig["SENSOR"]["EC"]["Point"][0]["uiCalReport"] )
   sLine += "%.2fC\t"%ttConfig["SENSOR"]["EC"]["Point"][0]["fTemp"]
   if( "fPressure" in ttConfig["SENSOR"]["EC"]["Point"][0] ):
    sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["EC"]["Point"][0]["fPressure"] )
   else:
    sLine += "N/A\t\n"
  else:
   sLine += "N/A\tN/A\tN/A\n"
  tLines.append(sLine)
  f.writelines(tLines)
  f.close()

 #----------------------------------------------
 # Création d'un nouveau fichier
 #----------------------------------------------
 def vFCreateNewFileProbe( self, ttConfig, sFileName ):
  print("-- vFCreateNewFile --")

  f = open(sFileName, "w")

  tLines = []
  tLines.append("TAB delimited raw text file. Use the TAB key to align the columns in your word processor software.\n")
  tLines.append("\n")
  tLines.append("\n")
  tLines.append("AquaSonde Calibration Certificate\n")
  tLines.append("\n")
  tLines.append("Date: "+ datetime.now().strftime("%d/%m/%Y")+"\n")
  tLines.append("Time: "+datetime.now().strftime("%H:%M:%S")+"\n")
  tLines.append("Sonde Type: "+ttConfig["PRODUCT"]["sModel"]+"\n")
  tLines.append("Sonde S/N: "+ttConfig["PRODUCT"]["sPSN1"]+"\n")
  tLines.append("Sonde S/W Rev: "+ttConfig["PRODUCT"]["sPSW1"]+"\n")
  tLines.append("\n")
  tLines.append("Calibration Record\n")
  tLines.append("\n")
  tLines.append("Function\tValue\tTemp\tBaro\n\n")
  #sLine = "Sonde type:"
  #sLine += "Sonde type: "+self.ttConfig["PRODUCT"]["sModel"]
  #---
  # DO - 0%
  sLine  = "DO Zero Output\t"
  if( "fTemp" in ttConfig["SENSOR"]["DO"]["Point"][0] ):
   sLine += "%.1fmV\t"%( ttConfig["SENSOR"]["DO"]["Point"][0]["uiCalReport"] * 1000 )
   sLine += "%.2fC\t"%ttConfig["SENSOR"]["DO"]["Point"][0]["fTemp"]
   if( "fPressure" in ttConfig["SENSOR"]["DO"]["Point"][0] ):
    sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["DO"]["Point"][0]["fPressure"] )
   else:
    sLine += "N/A\t\n"
  else:
   sLine += "N/A\tN/A\tN/A\n"
  tLines.append(sLine)
  #---
  # DO - 100%
  sLine  = "DO 100% Output\t"
  if( "fTemp" in ttConfig["SENSOR"]["DO"]["Point"][1] ):
   sLine += "%.1fmV\t"%( ttConfig["SENSOR"]["DO"]["Point"][1]["uiCalReport"] * 1000 )
   sLine += "%.2fC\t"%ttConfig["SENSOR"]["DO"]["Point"][1]["fTemp"]
   if( "fPressure" in ttConfig["SENSOR"]["DO"]["Point"][1] ):
    sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["DO"]["Point"][1]["fPressure"] )
   else:
    sLine += "N/A\t\n"
  else:
   sLine += "N/A\tN/A\tN/A\n"
  tLines.append(sLine)
  #---
  # EC Cell Constant
  sLine  = "EC Cell Constant\t"
  if( "fTemp" in ttConfig["SENSOR"]["EC"]["Point"][0] ):
   sLine += "%.2f\t"%( ttConfig["SENSOR"]["EC"]["Point"][0]["uiCalReport"] )
   sLine += "%.2fC\t"%ttConfig["SENSOR"]["EC"]["Point"][0]["fTemp"]
   if( "fPressure" in ttConfig["SENSOR"]["EC"]["Point"][0] ):
    sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["EC"]["Point"][0]["fPressure"] )
   else:
    sLine += "N/A\t\n"
  else:
   sLine += "N/A\tN/A\tN/A\n"
  tLines.append(sLine)
  #---
  # pH 7.00 Offset
  sLine  = "pH 7.00 Offset\t"
  if( "fTemp" in ttConfig["SENSOR"]["PH"]["Point"][0] ):
   sLine += "%.1fmV\t"%( ttConfig["SENSOR"]["PH"]["Point"][0]["uiCalReport"] )
   sLine += "%.2fC\t"%ttConfig["SENSOR"]["PH"]["Point"][0]["fTemp"]
   if( "fPressure" in ttConfig["SENSOR"]["PH"]["Point"][0] ):
    sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["PH"]["Point"][0]["fPressure"] )
   else:
    sLine += "N/A\t\n"
  else:
   sLine += "N/A\tN/A\tN/A\n"
  tLines.append(sLine)
  #---
  # pH 4.01 Swing
  sLine  = "pH 4.01 Swing\t"
  if( "fTemp" in ttConfig["SENSOR"]["PH"]["Point"][1] ):
   sLine += "%.1fmV/pH\t"%( ttConfig["SENSOR"]["PH"]["Point"][1]["uiCalReport"] )
   sLine += "%.2fC\t"%ttConfig["SENSOR"]["PH"]["Point"][1]["fTemp"]
   if( "fPressure" in ttConfig["SENSOR"]["PH"]["Point"][1] ):
    sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["PH"]["Point"][1]["fPressure"] )
   else:
    sLine += "N/A\t\n"
  else:
   sLine += "N/A\tN/A\tN/A\n"
  tLines.append(sLine)
  #---
  # pH 10.00 Swing
  sLine  = "pH 10.00 Swing\t"
  if( "fTemp" in ttConfig["SENSOR"]["PH"]["Point"][2] ):
   sLine += "%.1fmV/pH\t"%( ttConfig["SENSOR"]["PH"]["Point"][2]["uiCalReport"] )
   sLine += "%.2fC\t"%ttConfig["SENSOR"]["PH"]["Point"][2]["fTemp"]
   if( "fPressure" in ttConfig["SENSOR"]["PH"]["Point"][2] ):
    sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["PH"]["Point"][2]["fPressure"] )
   else:
    sLine += "N/A\t\n"
  else:
   sLine += "N/A\tN/A\tN/A\n"
  tLines.append(sLine)
  #---
  # ORP Offset
  sLine  = "ORP Offset\t"
  if( "fTemp" in ttConfig["SENSOR"]["ORP"]["Point"][0] ):
   sLine += "%.1fmV\t"%( ttConfig["SENSOR"]["ORP"]["Point"][0]["uiCalReport"] )
   sLine += "%.2fC\t"%ttConfig["SENSOR"]["ORP"]["Point"][0]["fTemp"]
   if( "fPressure" in ttConfig["SENSOR"]["ORP"]["Point"][0] ):
    sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["ORP"]["Point"][0]["fPressure"] )
   else:
    sLine += "N/A\t\n"
  else:
   sLine += "N/A\tN/A\tN/A\n"
  tLines.append(sLine)

  #------
  # AUX1
  print("uiAUXNumber = %d"%ttConfig["PRODUCT"]["uiAUXNumber"])
  if( ttConfig["PRODUCT"]["uiAUXNumber"] >= 1 ):
   if( ttConfig["SENSOR"]["AUX1"]["sIndex"] != "EMPTY" ):
    #---
    # AUX1 - P1
    sLine  = ttConfig["SENSOR"]["AUX1"]["sIndex"]+" Point 1\t"
    if( "fTemp" in ttConfig["SENSOR"]["AUX1"]["Point"][0] ):
     sLine += "%.1fmV\t"%( ttConfig["SENSOR"]["AUX1"]["Point"][0]["uiCalReport"] )
     sLine += "%.2fC\t"%ttConfig["SENSOR"]["AUX1"]["Point"][0]["fTemp"]
     if( "fPressure" in ttConfig["SENSOR"]["AUX1"]["Point"][0] ):
      sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["AUX1"]["Point"][0]["fPressure"] )
     else:
      sLine += "N/A\t\n"
    else:
     sLine += "N/A\tN/A\tN/A\n"
    tLines.append(sLine)
    #---
    # AUX1 - P2
    sLine  = ttConfig["SENSOR"]["AUX1"]["sIndex"]+" Point 2\t"
    if( "fTemp" in ttConfig["SENSOR"]["AUX1"]["Point"][1] ):
     sLine += "%.1fmV\t"%( ttConfig["SENSOR"]["AUX1"]["Point"][1]["uiCalReport"] )
     sLine += "%.2fC\t"%ttConfig["SENSOR"]["AUX1"]["Point"][1]["fTemp"]
     if( "fPressure" in ttConfig["SENSOR"]["AUX1"]["Point"][1] ):
      sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["AUX1"]["Point"][1]["fPressure"] )
     else:
      sLine += "N/A\t\n"
    else:
     sLine += "N/A\tN/A\tN/A\n"
    tLines.append(sLine)
    #---
    # AUX1 - P3
    if( ttConfig["SENSOR"]["AUX1"]["ucPoint"] > 2 ):
     sLine  = ttConfig["SENSOR"]["AUX1"]["sIndex"]+" Point 3\t"
     if( "fTemp" in ttConfig["SENSOR"]["AUX1"]["Point"][2] ):
      sLine += "%.1fmV\t"%( ttConfig["SENSOR"]["AUX1"]["Point"][2]["uiCalReport"] )
      sLine += "%.2fC\t"%ttConfig["SENSOR"]["AUX1"]["Point"][2]["fTemp"]
      if( "fPressure" in ttConfig["SENSOR"]["AUX1"]["Point"][2] ):
       sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["AUX1"]["Point"][2]["fPressure"] )
      else:
       sLine += "N/A\t\n"
     else:
      sLine += "N/A\tN/A\tN/A\n"
     tLines.append(sLine)
   else:
    tLines.append("EMPTY Point 1\tN/A\tN/A\tN/A\n")
    tLines.append("EMPTY Point 2\tN/A\tN/A\tN/A\n")
    tLines.append("EMPTY Point 3\tN/A\tN/A\tN/A\n")

  #------
  # AUX2
  if( ttConfig["PRODUCT"]["uiAUXNumber"] >= 2 ):
   tLines.append("\n")
   if( ttConfig["SENSOR"]["AUX2"]["sIndex"] != "EMPTY" ):
    #---
    # AUX2 - P1
    sLine  = ttConfig["SENSOR"]["AUX2"]["sIndex"]+" Point 1\t"
    if( "fTemp" in ttConfig["SENSOR"]["AUX2"]["Point"][0] ):
     sLine += "%.1fmV\t"%( ttConfig["SENSOR"]["AUX2"]["Point"][0]["uiCalReport"] )
     sLine += "%.2fC\t"%ttConfig["SENSOR"]["AUX2"]["Point"][0]["fTemp"]
     if( "fPressure" in ttConfig["SENSOR"]["AUX2"]["Point"][0] ):
      sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["AUX2"]["Point"][0]["fPressure"] )
     else:
      sLine += "N/A\t\n"
    else:
     sLine += "N/A\tN/A\tN/A\n"
    tLines.append(sLine)
    #---
    # AUX2 - P2
    sLine  = ttConfig["SENSOR"]["AUX2"]["sIndex"]+" Point 2\t"
    if( "fTemp" in ttConfig["SENSOR"]["AUX2"]["Point"][1] ):
     sLine += "%.1fmV\t"%( ttConfig["SENSOR"]["AUX2"]["Point"][1]["uiCalReport"] )
     sLine += "%.2fC\t"%ttConfig["SENSOR"]["AUX2"]["Point"][1]["fTemp"]
     if( "fPressure" in ttConfig["SENSOR"]["AUX2"]["Point"][1] ):
      sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["AUX2"]["Point"][1]["fPressure"] )
     else:
      sLine += "N/A\t\n"
    else:
     sLine += "N/A\tN/A\tN/A\n"
    tLines.append(sLine)
    #---
    # AUX2 - P3
    if( ttConfig["SENSOR"]["AUX2"]["ucPoint"] > 2 ):
     sLine  = ttConfig["SENSOR"]["AUX2"]["sIndex"]+" Point 3\t"
     if( "fTemp" in ttConfig["SENSOR"]["AUX2"]["Point"][2] ):
      sLine += "%.1fmV\t"%( ttConfig["SENSOR"]["AUX2"]["Point"][2]["uiCalReport"] )
      sLine += "%.2fC\t"%ttConfig["SENSOR"]["AUX2"]["Point"][2]["fTemp"]
      if( "fPressure" in ttConfig["SENSOR"]["AUX2"]["Point"][2] ):
       sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["AUX2"]["Point"][2]["fPressure"] )
      else:
       sLine += "N/A\t\n"
     else:
      sLine += "N/A\tN/A\tN/A\n"
     tLines.append(sLine)
   else:
    tLines.append("EMPTY Point 1\tN/A\tN/A\tN/A\n")
    tLines.append("EMPTY Point 2\tN/A\tN/A\tN/A\n")
    tLines.append("EMPTY Point 3\tN/A\tN/A\tN/A\n")

  #------
  # AUX3
  if( ttConfig["PRODUCT"]["uiAUXNumber"] >= 3 ):
   tLines.append("\n")
   if( ttConfig["SENSOR"]["AUX3"]["sIndex"] != "EMPTY" ):
    #---
    # AUX3 - P1
    sLine  = ttConfig["SENSOR"]["AUX3"]["sIndex"]+" Point 1\t"
    if( "fTemp" in ttConfig["SENSOR"]["AUX3"]["Point"][0] ):
     sLine += "%.1fmV\t"%( ttConfig["SENSOR"]["AUX3"]["Point"][0]["uiCalReport"] )
     sLine += "%.2fC\t"%ttConfig["SENSOR"]["AUX3"]["Point"][0]["fTemp"]
     if( "fPressure" in ttConfig["SENSOR"]["AUX3"]["Point"][0] ):
      sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["AUX3"]["Point"][0]["fPressure"] )
     else:
      sLine += "N/A\t\n"
    else:
     sLine += "N/A\tN/A\tN/A\n"
    tLines.append(sLine)
    #---
    # AUX3 - P2
    sLine  = ttConfig["SENSOR"]["AUX3"]["sIndex"]+" Point 2\t"
    if( "fTemp" in ttConfig["SENSOR"]["AUX3"]["Point"][1] ):
     sLine += "%.1fmV\t"%( ttConfig["SENSOR"]["AUX3"]["Point"][1]["uiCalReport"] )
     sLine += "%.2fC\t"%ttConfig["SENSOR"]["AUX3"]["Point"][1]["fTemp"]
     if( "fPressure" in ttConfig["SENSOR"]["AUX3"]["Point"][1] ):
      sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["AUX3"]["Point"][1]["fPressure"] )
     else:
      sLine += "N/A\t\n"
    else:
     sLine += "N/A\tN/A\tN/A\n"
    tLines.append(sLine)
    #---
    # AUX3 - P3
    if( ttConfig["SENSOR"]["AUX3"]["ucPoint"] > 2 ):
     sLine  = ttConfig["SENSOR"]["AUX3"]["sIndex"]+" Point 3\t"
     if( "fTemp" in ttConfig["SENSOR"]["AUX3"]["Point"][2] ):
      sLine += "%.1fmV\t"%( ttConfig["SENSOR"]["AUX3"]["Point"][2]["uiCalReport"] )
      sLine += "%.2fC\t"%ttConfig["SENSOR"]["AUX3"]["Point"][2]["fTemp"]
      if( "fPressure" in ttConfig["SENSOR"]["AUX3"]["Point"][2] ):
       sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["AUX3"]["Point"][2]["fPressure"] )
      else:
       sLine += "N/A\t\n"
     else:
      sLine += "N/A\tN/A\tN/A\n"
     tLines.append(sLine)
   else:
    tLines.append("EMPTY Point 1\tN/A\tN/A\tN/A\n")
    tLines.append("EMPTY Point 2\tN/A\tN/A\tN/A\n")
    tLines.append("EMPTY Point 3\tN/A\tN/A\tN/A\n")

  #------
  # AUX4
  if( ttConfig["PRODUCT"]["uiAUXNumber"] >= 4 ):
   tLines.append("\n")
   if( ttConfig["SENSOR"]["AUX4"]["sIndex"] != "EMPTY" ):
    #---
    # AUX4 - P1
    sLine  = ttConfig["SENSOR"]["AUX4"]["sIndex"]+" Point 1\t"
    if( "fTemp" in ttConfig["SENSOR"]["AUX4"]["Point"][0] ):
     sLine += "%.1fmV\t"%( ttConfig["SENSOR"]["AUX4"]["Point"][0]["uiCalReport"] )
     sLine += "%.2fC\t"%ttConfig["SENSOR"]["AUX4"]["Point"][0]["fTemp"]
     if( "fPressure" in ttConfig["SENSOR"]["AUX4"]["Point"][0] ):
      sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["AUX4"]["Point"][0]["fPressure"] )
     else:
      sLine += "N/A\t\n"
    else:
     sLine += "N/A\tN/A\tN/A\n"
    tLines.append(sLine)
    #---
    # AUX4 - P2
    sLine  = ttConfig["SENSOR"]["AUX4"]["sIndex"]+" Point 2\t"
    if( "fTemp" in ttConfig["SENSOR"]["AUX4"]["Point"][1] ):
     sLine += "%.1fmV\t"%( ttConfig["SENSOR"]["AUX4"]["Point"][1]["uiCalReport"] )
     sLine += "%.2fC\t"%ttConfig["SENSOR"]["AUX4"]["Point"][1]["fTemp"]
     if( "fPressure" in ttConfig["SENSOR"]["AUX4"]["Point"][1] ):
      sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["AUX4"]["Point"][1]["fPressure"] )
     else:
      sLine += "N/A\t\n"
    else:
     sLine += "N/A\tN/A\tN/A\n"
    tLines.append(sLine)
    #---
    # AUX4 - P3
    if( ttConfig["SENSOR"]["AUX4"]["ucPoint"] > 2 ):
     sLine  = ttConfig["SENSOR"]["AUX4"]["sIndex"]+" Point 3\t"
     if( "fTemp" in ttConfig["SENSOR"]["AUX4"]["Point"][2] ):
      sLine += "%.1fmV\t"%( ttConfig["SENSOR"]["AUX4"]["Point"][2]["uiCalReport"] )
      sLine += "%.2fC\t"%ttConfig["SENSOR"]["AUX4"]["Point"][2]["fTemp"]
      if( "fPressure" in ttConfig["SENSOR"]["AUX4"]["Point"][2] ):
       sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["AUX4"]["Point"][2]["fPressure"] )
      else:
       sLine += "N/A\t\n"
     else:
      sLine += "N/A\tN/A\tN/A\n"
     tLines.append(sLine)
   else:
    tLines.append("EMPTY Point 1\tN/A\tN/A\tN/A\n")
    tLines.append("EMPTY Point 2\tN/A\tN/A\tN/A\n")
    tLines.append("EMPTY Point 3\tN/A\tN/A\tN/A\n")

  #------
  # AUX5
  if( ttConfig["PRODUCT"]["uiAUXNumber"] >= 5 ):
   tLines.append("\n")
   if( ttConfig["SENSOR"]["AUX5"]["sIndex"] != "EMPTY" ):
    #---
    # AUX5 - P1
    sLine  = ttConfig["SENSOR"]["AUX5"]["sIndex"]+" Point 1\t"
    if( "fTemp" in ttConfig["SENSOR"]["AUX5"]["Point"][0] ):
     sLine += "%.1fmV\t"%( ttConfig["SENSOR"]["AUX5"]["Point"][0]["uiCalReport"] )
     sLine += "%.2fC\t"%ttConfig["SENSOR"]["AUX5"]["Point"][0]["fTemp"]
     if( "fPressure" in ttConfig["SENSOR"]["AUX5"]["Point"][0] ):
      sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["AUX5"]["Point"][0]["fPressure"] )
     else:
      sLine += "N/A\t\n"
    else:
     sLine += "N/A\tN/A\tN/A\n"
    tLines.append(sLine)
    #---
    # AUX5 - P2
    sLine  = ttConfig["SENSOR"]["AUX5"]["sIndex"]+" Point 2\t"
    if( "fTemp" in ttConfig["SENSOR"]["AUX5"]["Point"][1] ):
     sLine += "%.1fmV\t"%( ttConfig["SENSOR"]["AUX5"]["Point"][1]["uiCalReport"] )
     sLine += "%.2fC\t"%ttConfig["SENSOR"]["AUX5"]["Point"][1]["fTemp"]
     if( "fPressure" in ttConfig["SENSOR"]["AUX5"]["Point"][1] ):
      sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["AUX5"]["Point"][1]["fPressure"] )
     else:
      sLine += "N/A\t\n"
    else:
     sLine += "N/A\tN/A\tN/A\n"
    tLines.append(sLine)
    #---
    # AUX5 - P3
    if( ttConfig["SENSOR"]["AUX5"]["ucPoint"] > 2 ):
     sLine  = ttConfig["SENSOR"]["AUX5"]["sIndex"]+" Point 3\t"
     if( "fTemp" in ttConfig["SENSOR"]["AUX5"]["Point"][2] ):
      sLine += "%.1fmV\t"%( ttConfig["SENSOR"]["AUX5"]["Point"][2]["uiCalReport"] )
      sLine += "%.2fC\t"%ttConfig["SENSOR"]["AUX5"]["Point"][2]["fTemp"]
      if( "fPressure" in ttConfig["SENSOR"]["AUX5"]["Point"][2] ):
       sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["AUX5"]["Point"][2]["fPressure"] )
      else:
       sLine += "N/A\t\n"
     else:
      sLine += "N/A\tN/A\tN/A\n"
     tLines.append(sLine)
   else:
    tLines.append("EMPTY Point 1\tN/A\tN/A\tN/A\n")
    tLines.append("EMPTY Point 2\tN/A\tN/A\tN/A\n")
    tLines.append("EMPTY Point 3\tN/A\tN/A\tN/A\n")

  #------
  # AUX6
  if( ttConfig["PRODUCT"]["uiAUXNumber"] >= 6 ):
   tLines.append("\n")
   if( ttConfig["SENSOR"]["AUX6"]["sIndex"] != "EMPTY" ):
    #---
    # AUX6 - P1
    sLine  = ttConfig["SENSOR"]["AUX6"]["sIndex"]+" Point 1\t"
    if( "fTemp" in ttConfig["SENSOR"]["AUX6"]["Point"][0] ):
     sLine += "%.1fmV\t"%( ttConfig["SENSOR"]["AUX6"]["Point"][0]["uiCalReport"] )
     sLine += "%.2fC\t"%ttConfig["SENSOR"]["AUX6"]["Point"][0]["fTemp"]
     if( "fPressure" in ttConfig["SENSOR"]["AUX6"]["Point"][0] ):
      sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["AUX6"]["Point"][0]["fPressure"] )
     else:
      sLine += "N/A\t\n"
    else:
     sLine += "N/A\tN/A\tN/A\n"
    tLines.append(sLine)
    #---
    # AUX6 - P2
    sLine  = ttConfig["SENSOR"]["AUX6"]["sIndex"]+" Point 2\t"
    if( "fTemp" in ttConfig["SENSOR"]["AUX6"]["Point"][1] ):
     sLine += "%.1fmV\t"%( ttConfig["SENSOR"]["AUX6"]["Point"][1]["uiCalReport"] )
     sLine += "%.2fC\t"%ttConfig["SENSOR"]["AUX6"]["Point"][1]["fTemp"]
     if( "fPressure" in ttConfig["SENSOR"]["AUX6"]["Point"][1] ):
      sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["AUX6"]["Point"][1]["fPressure"] )
     else:
      sLine += "N/A\t\n"
    else:
     sLine += "N/A\tN/A\tN/A\n"
    tLines.append(sLine)
    #---
    # AUX6 - P3
    if( ttConfig["SENSOR"]["AUX6"]["ucPoint"] > 2 ):
     sLine  = ttConfig["SENSOR"]["AUX6"]["sIndex"]+" Point 3\t"
     if( "fTemp" in ttConfig["SENSOR"]["AUX6"]["Point"][2] ):
      sLine += "%.1fmV\t"%( ttConfig["SENSOR"]["AUX6"]["Point"][2]["uiCalReport"] )
      sLine += "%.2fC\t"%ttConfig["SENSOR"]["AUX6"]["Point"][2]["fTemp"]
      if( "fPressure" in ttConfig["SENSOR"]["AUX6"]["Point"][2] ):
       sLine += "%.1fmB\t\n"%( ttConfig["SENSOR"]["AUX6"]["Point"][2]["fPressure"] )
      else:
       sLine += "N/A\t\n"
     else:
      sLine += "N/A\tN/A\tN/A\n"
     tLines.append(sLine)
   else:
    tLines.append("EMPTY Point 1\tN/A\tN/A\tN/A\n")
    tLines.append("EMPTY Point 2\tN/A\tN/A\tN/A\n")
    tLines.append("EMPTY Point 3\tN/A\tN/A\tN/A\n")

  f.writelines(tLines)
  f.close()


