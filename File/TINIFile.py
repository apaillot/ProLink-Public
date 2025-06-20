# This Python file uses the following encoding: utf-8

#============================================================================#
# Librairies système
#============================================================================#
import sys
import configparser
import traceback
import os

#============================================================================#
# Librairies Qt
#============================================================================#
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QMetaObject)
from PySide6.QtCore import Slot

#============================================================================#
# Librairies Utilisateur
#============================================================================#
from TVersion import *

#============================================================================#
# Variable
#============================================================================#

#============================================================================#
# Classe
#============================================================================#

#------------------------------------------------------------------------
# Controleur de main Windows
#------------------------------------------------------------------------
class TINIFile:
 #----------------------------------------------
 # Init
 #----------------------------------------------
 def __init__( self ):
  print("-- TINIFile > init --")
  self.sINIFilename = 'config.ini'
  # Init de la configuratio
  self.tConfig = {}

 #----------------------------------------------
 # Lecture configuration local
 #----------------------------------------------
 def vFReadConfig( self ):
  print("-- TINIFile > vFReadConfig --")
  # Si réécriture
  bRewrite = False
  # Par sécurité
  try:
   self.tConfig = configparser.ConfigParser()
   self.tConfig.read( self.sINIFilename )
   print(os.getcwd())
   # Vérification que les paramètres sont présents
   # Global - Debug
   uiDebug = int(self.tConfig["GLOBAL"]["debug"])
   if( ( uiDebug != 0 ) and ( uiDebug != 0 ) ):
    self.tConfig["GLOBAL"]["debug"] = 0
    bRewrite = True
   # Global - Log error
   uiLogError = int(self.tConfig["GLOBAL"]["error"])
   if( ( uiLogError != 0 ) and ( uiLogError != 0 ) ):
    self.tConfig["GLOBAL"]["error"] = 0
    bRewrite = True
   # Global - Location
   self.tConfig["GLOBAL"].get("location", "")
   # Update - Activate
   uiUpdateActivate = int(self.tConfig["UPDATE"]["activate"])
   print("uiUpdateActivate = %d"%uiUpdateActivate)
   if( ( uiUpdateActivate != 0 ) and ( uiUpdateActivate != 1 ) ):
    self.tConfig["UPDATE"]["activate"] = "1"
    bRewrite = True
   # Update - HttpPath
   sUpdatePath = self.tConfig["UPDATE"]["httppath"]
   if( ( sUpdatePath == "" ) or ( sUpdatePath == None ) ):
    self.tConfig["UPDATE"]["httppath"] = "https://support.nke-instrumentation.com/Update/Aquaread/ProLink/Mainline/"
    bRewrite = True
   # Measure - EC_ref_temp
   sECRefTemp = self.tConfig["MEASURE"]["ec_ref_temp"]
   if(   ( sECRefTemp != "25"  )
     and ( sECRefTemp != "20"  )
     and ( sECRefTemp != "ABS" ) ):
    self.tConfig["MEASURE"]["ec_ref_temp"] = "25"
    bRewrite = True
   # Measure - Temperature unit
   sTemperatureUnit = self.tConfig["MEASURE"]["temperature_unit"]
   if(   ( sTemperatureUnit != "C" )
     and ( sTemperatureUnit != "F" ) ):
    self.tConfig["MEASURE"]["temperature_unit"] = "C"
    bRewrite = True
   # Measure - Depth unit
   sDepthUnit = self.tConfig["MEASURE"]["depth_unit"]
   if(   ( sDepthUnit != "m" )
     and ( sDepthUnit != "f" ) ):
    self.tConfig["MEASURE"]["depth_unit"] = "m"
    bRewrite = True
   # Measure - Depth unit
   fTDSFactor = float(self.tConfig["MEASURE"]["tds_factor"])
   if(  ( fTDSFactor < 0.01 )
     or ( fTDSFactor > 2.00 ) ):
    self.tConfig["MEASURE"]["tds_factor"] = "0.65"
    bRewrite = True
   # Software - Depth unit
   uiGraphicalDepth = int(self.tConfig["SOFTWARE"]["graphical_depth"])
   if(  ( uiGraphicalDepth < 0 )
     or ( uiGraphicalDepth > 8192 ) ):
    self.tConfig["SOFTWARE"]["graphical_depth"] = "128"
    bRewrite = True
   # Software - Display calculated measure
   sDisplayCalculated = self.tConfig["SOFTWARE"]["display_calculated"]
   if(   ( sDisplayCalculated != "0" )
     and ( sDisplayCalculated != "1" ) ):
    self.tConfig["SOFTWARE"]["display_calculated"] = "0"
    bRewrite = True
   # Software - Version
   sSoftwareVersion = self.tConfig["SOFTWARE"]["version"]
   if( sSoftwareVersion != sGlobalSoftwareVersion ):
    self.tConfig["SOFTWARE"]["version"] = sGlobalSoftwareVersion
    bRewrite = True

   # Si réécriture
   if( bRewrite ):
    self.vFWriteConfig()

  except Exception as err:
   print(err)
   print(traceback.format_exc())
   # On recréé l'objet
   #self.tConfig = {}
   self.tConfig["GLOBAL"]   = {}
   self.tConfig["UPDATE"]   = {}
   self.tConfig["MEASURE"]  = {}
   self.tConfig["SOFTWARE"] = {}
   # Réécriture du fichier INI
   self.tConfig["GLOBAL"]["recordmeasurelocation"] = "./Measure"
   self.tConfig["GLOBAL"]["debug"]                 = "0"
   self.tConfig["GLOBAL"]["error"]                 = "0"
   self.tConfig["GLOBAL"]["location"]              = ""
   self.tConfig["UPDATE"]["activate"]              = "1"
   self.tConfig["UPDATE"]["httppath"]              = "https://support.nke-instrumentation.com/Update/Aquaread/ProLink/Mainline/"
   self.tConfig["MEASURE"]["ec_ref_temp"]          = "25"
   self.tConfig["MEASURE"]["temperature_unit"]     = "C"
   self.tConfig["MEASURE"]["depth_unit"]           = "m"
   self.tConfig["MEASURE"]["tds_factor"]           = "0.65"
   self.tConfig["SOFTWARE"]["graphical_depth"]     = "128"
   self.tConfig["SOFTWARE"]["display_calculated"]  = "0"
   self.tConfig["SOFTWARE"]["version"]             = sGlobalSoftwareVersion
   # Tentative d'écriture
   try:
    # Ecriture
    self.vFWriteConfig()
   except Exception as err2:
    print(err2)
    print(traceback.format_exc())

 #----------------------------------------------
 # Ecriture configuration local
 #----------------------------------------------
 def vFWriteConfig( self ):
  print("-- TINIFile > vFWriteConfig --")
  # Ecriture fichier
  with open( self.sINIFilename, 'w' ) as tFileHandler:
   self.tConfig.write(tFileHandler)

 #----------------------------------------------
 # Ecriture EC Ref temp
 #----------------------------------------------
 def vFWriteECRefTemp( self, sText ):
  print("-- vFWriteECRefTemp --")
  sText.split(" ")[0]
  # Mise à jour de la valeur
  if( sText == "25 C" ):
   self.tConfig["MEASURE"]["ec_ref_temp"] = "25"
  elif( sText == "20 C" ):
   self.tConfig["MEASURE"]["ec_ref_temp"] = "20"
  else: #( sText == "ABS EC" ):
   self.tConfig["MEASURE"]["ec_ref_temp"] = "ABS"
  # Ecriture dans le .ini
  self.vFWriteConfig()

 #----------------------------------------------
 # Ecriture temperature unit
 #----------------------------------------------
 def vFWriteTemperatureUnit( self, sText ):
  print("-- vFWriteTemperatureUnit --")
  # Mise à jour de la valeur
  self.tConfig["MEASURE"]["temperature_unit"] = sText
  # Ecriture dans le .ini
  self.vFWriteConfig()

 #----------------------------------------------
 # Ecriture temperature unit
 #----------------------------------------------
 def vFWriteDepthUnit( self, sText ):
  print("-- vFWriteDepthUnit --")
  # Mise à jour de la valeur
  self.tConfig["MEASURE"]["depth_unit"] = sText
  # Ecriture dans le .ini
  self.vFWriteConfig()

 #----------------------------------------------
 # Ecriture tds factor
 #----------------------------------------------
 def vFWriteTDSFactor( self, fText ):
  print("-- vFWriteTDSFactor --")
  print("fText = %f"%fText)
  # Mise à jour de la valeur
  self.tConfig["MEASURE"]["tds_factor"] = ("%.2f"%fText)
  # Ecriture dans le .ini
  self.vFWriteConfig()

 #----------------------------------------------
 # Ecriture graphical depth
 #----------------------------------------------
 def vFWriteGraphicalDepth( self, sText ):
  print("-- vFWriteGraphicalDepth --")
  # Mise à jour de la valeur
  if( sText == "Unlimited" ):
   self.tConfig["SOFTWARE"]["graphical_depth"] = "0"
  else:
   self.tConfig["SOFTWARE"]["graphical_depth"] = sText
  # Ecriture dans le .ini
  self.vFWriteConfig()

 #----------------------------------------------
 # Ecriture display calculated measure
 #----------------------------------------------
 def vFWriteDisplayCalculated( self, sText ):
  print("-- vFWriteDisplayCalculated --")
  # Mise à jour de la valeur
  if( sText == "Enable" ):
   self.tConfig["SOFTWARE"]["display_calculated"] = "1"
  else:
   self.tConfig["SOFTWARE"]["display_calculated"] = "0"
  # Ecriture dans le .ini
  self.vFWriteConfig()



