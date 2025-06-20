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
from Product.Sonde.TConfigParser import TConfigParser

#============================================================================#
# Variable
#============================================================================#

#------------------------------------------------------------------------
# Controleur de main Windows
#------------------------------------------------------------------------
class TSondeRawFile:
 #----------------------------------------------
 # Init : création de l'objet
 #----------------------------------------------
 def __init__(self):
  # Nom du fichier courrant
  self.sFileName = ""
  # Separateur par défaut
  self.cSeparator = "\t"
  self.sFileExtension = ".asf"
  # Parser de config
  self.tConfigParser = TConfigParser()
  # Init
  self.ttConfig  = {}
  # Init de la configuration
  self.tConfigParser.vFInitConfigObj(self.ttConfig)
  # Init recorded data
  self.ttMeasure = []

 #----------------------------------------------
 # Création d'un nouveau raw
 #----------------------------------------------
 def vFCreateNewFileRaw( self, sFileName, ttConfig, ttMeasureRaw ):
  print("-- vFCreateNewFileRaw --")
  #self.cSeparator = "\t"
  #self.sFileExtension = ".asf"
  self.sFileName = sFileName

  tRaw = []
  if( ttConfig["PRODUCT"]["uiLOG_SEC"] != 0 ):
   uiLogSec = 1
   uiLogMin = ttConfig["PRODUCT"]["uiLOG_SEC"]
  else:
   uiLogMin = ttConfig["PRODUCT"]["uiLOG_HOUR"] * 60 + ttConfig["PRODUCT"]["uiLOG_MIN"]
  tRaw.append( ( uiLogMin                              & 0xFF00 ) >> 8 )
  tRaw.append( ( uiLogMin                              & 0x00FF )      )
  tRaw.append( ( uiLogSec                              & 0x00FF )      )
  tRaw.append( ( ttConfig["PRODUCT"]["uiLOG_EVENT"]    & 0x00FF )      )
  tRaw.append( ( ttConfig["PRODUCT"]["uiLOG_SENSOR"]   & 0x00FF )      )
  uiEventMin = ttConfig["PRODUCT"]["uiEVENT_HOUR"] * 60 + ttConfig["PRODUCT"]["uiEVENT_MIN"]
  tRaw.append( ( uiEventMin                            & 0xFF00 ) >> 8 )
  tRaw.append( ( uiEventMin                            & 0x00FF )      )

  tRaw.append( ( ttConfig["PRODUCT"]["uiCLEAN_HR"]     & 0x00FF )      )
  tRaw.append( ( ttConfig["PRODUCT"]["uiEVENT_CHANGE"] & 0x00FF )      )
  tRaw.append( ( ttConfig["PRODUCT"]["uiBatt"]         & 0xFF00 ) >> 8 )
  tRaw.append( ( ttConfig["PRODUCT"]["uiBatt"]         & 0x00FF )      )
  tRaw.append( ( ttConfig["PRODUCT"]["uiBATT_PC"]      & 0x00FF )      )

  tRaw.append( ( int(ttConfig["PRODUCT"]["sPSN1"][0])  & 0x00FF )      )
  tRaw.append( ( int(ttConfig["PRODUCT"]["sPSN1"][1])  & 0x00FF )      )
  tRaw.append( ( int(ttConfig["PRODUCT"]["sPSN1"][2])  & 0x00FF )      )
  tRaw.append( ( int(ttConfig["PRODUCT"]["sPSN1"][3])  & 0x00FF )      )
  tRaw.append( ( int(ttConfig["PRODUCT"]["sPSN1"][4])  & 0x00FF )      )
  tRaw.append( ( int(ttConfig["PRODUCT"]["sPSN1"][5])  & 0x00FF )      )
  tRaw.append( ( int(ttConfig["PRODUCT"]["sPSN1"][6])  & 0x00FF )      )
  tRaw.append( ( int(ttConfig["PRODUCT"]["sPSN1"][7])  & 0x00FF )      )
  tRaw.append( ( int(ttConfig["PRODUCT"]["sPSN1"][8])  & 0x00FF )      )

  tRaw.append( ( int(ttConfig["PRODUCT"]["sPSW1"][0])  & 0x00FF )      )
  tRaw.append( ( int(ttConfig["PRODUCT"]["sPSW1"][2])  & 0x00FF )      )
  tRaw.append( ( int(ttConfig["PRODUCT"]["sPSW1"][3])  & 0x00FF )      )

  tRaw.append( ( int(ttConfig["SENSOR"]["AUX1"]["uiIndex"]) & 0x00FF )      )
  tRaw.append( ( int(ttConfig["SENSOR"]["AUX2"]["uiIndex"]) & 0x00FF )      )
  tRaw.append( ( int(ttConfig["SENSOR"]["AUX3"]["uiIndex"]) & 0x00FF )      )
  tRaw.append( ( int(ttConfig["SENSOR"]["AUX4"]["uiIndex"]) & 0x00FF )      )
  tRaw.append( ( int(ttConfig["SENSOR"]["AUX5"]["uiIndex"]) & 0x00FF )      )
  tRaw.append( ( int(ttConfig["SENSOR"]["AUX6"]["uiIndex"]) & 0x00FF )      )

  tRaw.append( ( int(ttConfig["PRODUCT"]["sPSW1"][5])  & 0x00FF )      )
  tRaw.append( ( int(ttConfig["PRODUCT"]["sPSW1"][7])  & 0x00FF )      )
  tRaw.append( ( int(ttConfig["PRODUCT"]["sPSW1"][8])  & 0x00FF )      )

  uiMemRecords = ttConfig["PRODUCT"]["uiMemRecords"] * 55
  tRaw.append( ( uiMemRecords & 0xFF0000 ) >> 16 )
  tRaw.append( ( uiMemRecords & 0x00FF00 ) >> 8  )
  tRaw.append( ( uiMemRecords & 0x0000FF )       )

  for ucElt in range(0, len(ttConfig["PRODUCT"]["tucSiteID"])):
   tRaw.append( ord(ttConfig["PRODUCT"]["tucSiteID"][ucElt]) )
  for ucElt in range(len(ttConfig["PRODUCT"]["tucSiteID"]), 16):
   tRaw.append( ord(" ") )

  for ucElt in range(0, len(ttConfig["PRODUCT"]["tucSiteLat"])):
   try:
    tRaw.append( ord(ttConfig["PRODUCT"]["tucSiteLat"][ucElt]) )
   except Exception as err:
    tRaw.append( ttConfig["PRODUCT"]["tucSiteLat"][ucElt] )
  for ucElt in range(len(ttConfig["PRODUCT"]["tucSiteLat"]), 7):
   tRaw.append( ord(" ") )

  for ucElt in range(0, len(ttConfig["PRODUCT"]["tucSiteLong"])):
   try:
    tRaw.append( ord(ttConfig["PRODUCT"]["tucSiteLong"][ucElt]) )
   except Exception as err:
    tRaw.append( ttConfig["PRODUCT"]["tucSiteLong"][ucElt] )
  for ucElt in range(len(ttConfig["PRODUCT"]["tucSiteLong"]), 8):
   tRaw.append( ord(" ") )
  """
  # Formattage du prototype de donnée
  sProto = '>2B'
  for uiCpt in range(uiMemRecords):
   #print("Loop %d"%uiCpt)
   sProto = sProto + str(uiPacketSize) + "s"
  # Ajout des CRC
  sProto = sProto + "2B"
  """
  # Conversion de la donnée en tableau de int
  for ucElt in range(2, len(ttMeasureRaw)-2):
   # Ajout
   tRaw.append( int.from_bytes( ttMeasureRaw[ucElt] ) )

  sLine = "$,$,"
  # Ajout à notre chaine d'écriture
  for ucElt in range(0, len(tRaw)):
   # Ajout
   sLine += str(tRaw[ucElt]) +","

  sLine += "$,$"

  # Création du fichier binaire
  with open(self.sFileName, "w") as file:
   # Ecriture de la data
   file.write(sLine)


 #----------------------------------------------
 # Création d'un nouveau raw
 #----------------------------------------------
 def vFOpenRaw( self, sFileName ):
  print("-- vFOpenRaw --")
  #self.cSeparator = "\t"
  #self.sFileExtension = ".asf"
  self.sFileName = sFileName
  #
  ttConfig  = self.ttConfig
  ttMeasure = self.ttMeasure

  # Création du fichier binaire
  with open(self.sFileName, "r") as file:
   # Ecriture de la data
   #file.write(sLine)
   # Lecture du fichier
   sRaw = file.read()

  # Séparation de la donnée
  tRaw = sRaw.split(",")

  uiCpt = 2
  uiLogMin      = int(tRaw[uiCpt]) * 256 + int(tRaw[uiCpt+1]); uiCpt+=2
  uiLogSec      = int(tRaw[uiCpt]); uiCpt+=1
  uiLogEvent    = int(tRaw[uiCpt]); uiCpt+=1
  uiLogSensor   = int(tRaw[uiCpt]); uiCpt+=1
  uiEventMin    = int(tRaw[uiCpt]) * 256 + int(tRaw[uiCpt+1]); uiCpt+=2
  uiCleanHR     = int(tRaw[uiCpt]); uiCpt+=1
  uiEventChange = int(tRaw[uiCpt]); uiCpt+=1
  uiBatt        = int(tRaw[uiCpt]) * 256 + int(tRaw[uiCpt+1]); uiCpt+=2
  fBatt         = float(uiBatt) / 102.3
  uiBattPC      = int(tRaw[uiCpt]); uiCpt+=1

  # Si flag seconde
  if( uiLogSec == 1 ):
   uiLogSec = uiLogMin
   uiLogMin = 0
  ttConfig["PRODUCT"]["uiLOG_HOUR"]    = int( uiLogMin / 60 )
  ttConfig["PRODUCT"]["uiLOG_MIN"]     = int( uiLogMin % 60 )
  ttConfig["PRODUCT"]["uiLOG_SEC"]     = uiLogSec
  ttConfig["PRODUCT"]["uiLOG_EVENT"]   = uiLogEvent
  ttConfig["PRODUCT"]["uiLOG_SENSOR"]  = uiLogSensor
  ttConfig["PRODUCT"]["sLOG_SENSOR"]   = self.tConfigParser.sFGetLogSensorNameWithIndex(uiLogSensor)
  ttConfig["PRODUCT"]["uiEVENT_HOUR"]  = int( uiEventMin / 60 )
  ttConfig["PRODUCT"]["uiEVENT_MIN"]   = int( uiEventMin % 60 )
  ttConfig["PRODUCT"]["uiCLEAN_HR"]    = int( uiEventMin )
  ttConfig["PRODUCT"]["uiEVENT_CHANGE"] = uiEventChange
  ttConfig["PRODUCT"]["uiBatt"]         = uiBatt
  ttConfig["PRODUCT"]["fBATT"]          = fBatt
  ttConfig["PRODUCT"]["uiBATT_PC"]      = uiBattPC

  print('ttConfig["PRODUCT"]["uiLOG_HOUR"]     = %u'%ttConfig["PRODUCT"]["uiLOG_HOUR"])
  print('ttConfig["PRODUCT"]["uiLOG_MIN"]      = %u'%ttConfig["PRODUCT"]["uiLOG_MIN"])
  print('ttConfig["PRODUCT"]["uiLOG_SEC"]      = %u'%ttConfig["PRODUCT"]["uiLOG_SEC"])
  print('ttConfig["PRODUCT"]["uiLOG_EVENT"]    = %u'%ttConfig["PRODUCT"]["uiLOG_EVENT"])
  print('ttConfig["PRODUCT"]["uiLOG_SENSOR"]   = %u'%ttConfig["PRODUCT"]["uiLOG_SENSOR"])
  print('ttConfig["PRODUCT"]["uiEVENT_HOUR"]   = %u'%ttConfig["PRODUCT"]["uiEVENT_HOUR"])
  print('ttConfig["PRODUCT"]["uiEVENT_MIN"]    = %u'%ttConfig["PRODUCT"]["uiEVENT_MIN"])
  print('ttConfig["PRODUCT"]["uiCLEAN_HR"]     = %u'%ttConfig["PRODUCT"]["uiCLEAN_HR"])
  print('ttConfig["PRODUCT"]["uiEVENT_CHANGE"] = %u'%ttConfig["PRODUCT"]["uiEVENT_CHANGE"])
  print('ttConfig["PRODUCT"]["uiBatt"]         = %u'%ttConfig["PRODUCT"]["uiBatt"])
  print('ttConfig["PRODUCT"]["fBATT"]          = %.02f'%ttConfig["PRODUCT"]["fBATT"])
  print('ttConfig["PRODUCT"]["uiBATT_PC"]      = %u'%ttConfig["PRODUCT"]["uiBATT_PC"])

  uiPSN1      = int(tRaw[uiCpt]); uiCpt+=1
  uiPSN2      = int(tRaw[uiCpt]); uiCpt+=1
  uiPSN3      = int(tRaw[uiCpt]); uiCpt+=1
  uiPSN4      = int(tRaw[uiCpt]); uiCpt+=1
  uiPSN5      = int(tRaw[uiCpt]); uiCpt+=1
  uiPSN6      = int(tRaw[uiCpt]); uiCpt+=1
  uiPSN7      = int(tRaw[uiCpt]); uiCpt+=1
  uiPSN8      = int(tRaw[uiCpt]); uiCpt+=1
  uiPSN9      = int(tRaw[uiCpt]); uiCpt+=1
  uiPSW1      = int(tRaw[uiCpt]); uiCpt+=1
  uiPSW2      = int(tRaw[uiCpt]); uiCpt+=1
  uiPSW3      = int(tRaw[uiCpt]); uiCpt+=1

  sPSN1 = str(uiPSN1)+str(uiPSN2)+str(uiPSN3)+str(uiPSN4)+str(uiPSN5)+str(uiPSN6)+str(uiPSN7)+str(uiPSN8)+str(uiPSN9)
  uiModel = int( str(uiPSN8) + "" + str(uiPSN9) )
  ttConfig["PRODUCT"]["sPSN1"]   = sPSN1
  ttConfig["PRODUCT"]["uiModel"] = uiModel
  sModel = self.tConfigParser.sFGetProductNameWithID(uiModel)
  ttConfig["PRODUCT"]["sModel"]      = sModel
  ttConfig["PRODUCT"]["uiAUXNumber"] = self.tConfigParser.sFGetAUXNumberWithID(uiModel)

  print('ttConfig["PRODUCT"]["sPSN1"]          = ' + ttConfig["PRODUCT"]["sPSN1"])
  print('ttConfig["PRODUCT"]["uiModel"]        = %u'%ttConfig["PRODUCT"]["uiModel"])
  print('ttConfig["PRODUCT"]["sModel"]         = ' + ttConfig["PRODUCT"]["sModel"])
  print('ttConfig["PRODUCT"]["uiAUXNumber"]    = %u'%ttConfig["PRODUCT"]["uiAUXNumber"])

  uiAux1Assign = int(tRaw[uiCpt]); uiCpt+=1
  uiAux2Assign = int(tRaw[uiCpt]); uiCpt+=1
  uiAux3Assign = int(tRaw[uiCpt]); uiCpt+=1
  uiAux4Assign = int(tRaw[uiCpt]); uiCpt+=1
  uiAux5Assign = int(tRaw[uiCpt]); uiCpt+=1
  uiAux6Assign = int(tRaw[uiCpt]); uiCpt+=1

  ttConfig["SENSOR"]["AUX1"]["uiIndex"]  = uiAux1Assign
  ttConfig["SENSOR"]["AUX2"]["uiIndex"]  = uiAux2Assign
  ttConfig["SENSOR"]["AUX3"]["uiIndex"]  = uiAux3Assign
  ttConfig["SENSOR"]["AUX4"]["uiIndex"]  = uiAux4Assign
  ttConfig["SENSOR"]["AUX5"]["uiIndex"]  = uiAux5Assign
  ttConfig["SENSOR"]["AUX6"]["uiIndex"]  = uiAux6Assign
  ttConfig["SENSOR"]["AUX7"]["uiIndex"]  = 254
  ttConfig["SENSOR"]["AUX1"]["sIndex"]   = self.tConfigParser.sFGetChannelNameWithID(uiAux1Assign)
  ttConfig["SENSOR"]["AUX2"]["sIndex"]   = self.tConfigParser.sFGetChannelNameWithID(uiAux2Assign)
  ttConfig["SENSOR"]["AUX3"]["sIndex"]   = self.tConfigParser.sFGetChannelNameWithID(uiAux3Assign)
  ttConfig["SENSOR"]["AUX4"]["sIndex"]   = self.tConfigParser.sFGetChannelNameWithID(uiAux4Assign)
  ttConfig["SENSOR"]["AUX5"]["sIndex"]   = self.tConfigParser.sFGetChannelNameWithID(uiAux5Assign)
  ttConfig["SENSOR"]["AUX6"]["sIndex"]   = self.tConfigParser.sFGetChannelNameWithID(uiAux6Assign)
  ttConfig["SENSOR"]["AUX7"]["sIndex"]   = self.tConfigParser.sFGetChannelNameWithID(254)
  # Unité
  ttConfig["SENSOR"]["AUX1"]["sUnit"]   = self.tConfigParser.sFGetChannelUnitWithID(uiAux1Assign)
  ttConfig["SENSOR"]["AUX2"]["sUnit"]   = self.tConfigParser.sFGetChannelUnitWithID(uiAux2Assign)
  ttConfig["SENSOR"]["AUX3"]["sUnit"]   = self.tConfigParser.sFGetChannelUnitWithID(uiAux3Assign)
  ttConfig["SENSOR"]["AUX4"]["sUnit"]   = self.tConfigParser.sFGetChannelUnitWithID(uiAux4Assign)
  ttConfig["SENSOR"]["AUX5"]["sUnit"]   = self.tConfigParser.sFGetChannelUnitWithID(uiAux5Assign)
  ttConfig["SENSOR"]["AUX6"]["sUnit"]   = self.tConfigParser.sFGetChannelUnitWithID(uiAux6Assign)
  ttConfig["SENSOR"]["AUX7"]["sUnit"]   = self.tConfigParser.sFGetChannelUnitWithID(254)

  print('ttConfig["SENSOR"]["AUX1"]["sIndex"] = ' + ttConfig["SENSOR"]["AUX1"]["sIndex"])
  print('ttConfig["SENSOR"]["AUX2"]["sIndex"] = ' + ttConfig["SENSOR"]["AUX2"]["sIndex"])
  print('ttConfig["SENSOR"]["AUX3"]["sIndex"] = ' + ttConfig["SENSOR"]["AUX3"]["sIndex"])
  print('ttConfig["SENSOR"]["AUX4"]["sIndex"] = ' + ttConfig["SENSOR"]["AUX4"]["sIndex"])
  print('ttConfig["SENSOR"]["AUX5"]["sIndex"] = ' + ttConfig["SENSOR"]["AUX5"]["sIndex"])
  print('ttConfig["SENSOR"]["AUX6"]["sIndex"] = ' + ttConfig["SENSOR"]["AUX6"]["sIndex"])

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

  uiFWR1       = int(tRaw[uiCpt]); uiCpt+=1
  uiFWR2       = int(tRaw[uiCpt]); uiCpt+=1
  uiFWR3       = int(tRaw[uiCpt]); uiCpt+=1
  uiMemHSB     = int(tRaw[uiCpt]); uiCpt+=1
  uiMemMSB     = int(tRaw[uiCpt]); uiCpt+=1
  uiMemLSB     = int(tRaw[uiCpt]); uiCpt+=1

  sPSW1        = str(uiPSW1)+"."+str(uiPSW2)+str(uiPSW3)+"."+str(uiFWR1)+"."+str(uiFWR2)+str(uiFWR3)
  uiMemRecords = ( ( uiMemHSB * 65536 ) + ( uiMemMSB * 256 ) + uiMemLSB ) / 55


  ttConfig["PRODUCT"]["sPSW1"]          = sPSW1
  ttConfig["PRODUCT"]["uiMemRecords"]   = int(uiMemRecords)
  uiMemRemaining = ( 150000 - uiMemRecords )
  ttConfig["PRODUCT"]["uiMemRemaining"]   = int(uiMemRemaining)
  ttConfig["PRODUCT"]["uiMemRemainingPC"] = int( uiMemRemaining * 100 / 150000 )

  print('ttConfig["PRODUCT"]["sPSW1"]             = ' + ttConfig["PRODUCT"]["sPSW1"])
  print('ttConfig["PRODUCT"]["uiMemRecords"]      = %u'%ttConfig["PRODUCT"]["uiMemRecords"])
  print('ttConfig["PRODUCT"]["uiMemRemainingPC"]  = %u'%ttConfig["PRODUCT"]["uiMemRemainingPC"])

  tucSiteID = []
  for ucElt in range(uiCpt, uiCpt+16):
   tucSiteID.append( chr(int(tRaw[ucElt])) )
  uiCpt+=16

  sSiteLat  = ""+chr(int(tRaw[uiCpt]))+" "+str(int(tRaw[uiCpt+1]))+str(int(tRaw[uiCpt+2]))+"°"+str(int(tRaw[uiCpt+3]))+str(int(tRaw[uiCpt+4]))+"."+str(int(tRaw[uiCpt+5]))+str(int(tRaw[uiCpt+6]))+"'"
  uiCpt+=7
  sSiteLong = ""+chr(int(tRaw[uiCpt]))+" "+str(int(tRaw[uiCpt+1]))+str(int(tRaw[uiCpt+2]))+str(int(tRaw[uiCpt+3]))+"°"+str(int(tRaw[uiCpt+4]))+str(int(tRaw[uiCpt+5]))+"."+str(int(tRaw[uiCpt+6]))+str(int(tRaw[uiCpt+7]))+"'"
  uiCpt+=8

  ttConfig["PRODUCT"]["sSiteID"]        = ''.join(tucSiteID).strip()
  ttConfig["PRODUCT"]["sSiteLat"]       = sSiteLat
  ttConfig["PRODUCT"]["sSiteLong"]      = sSiteLong
  ttConfig["PRODUCT"]["tucSiteID"]      = tucSiteID
  #ttConfig["PRODUCT"]["tucSiteLat"]     = tucSiteLat
  #ttConfig["PRODUCT"]["tucSiteLong"]    = tucSiteLong

  print('ttConfig["PRODUCT"]["sSiteID"]   = ' + ttConfig["PRODUCT"]["sSiteID"])
  print('ttConfig["PRODUCT"]["sSiteLat"]  = ' + ttConfig["PRODUCT"]["sSiteLat"])
  print('ttConfig["PRODUCT"]["sSiteLong"] = ' + ttConfig["PRODUCT"]["sSiteLong"])

  # - Estimatif Mémoire -
  # Durée acquisition
  uiLogIntBatt = ( uiLogMin * 60 ) + uiLogSec
  # Autonomie mémoire
  ttConfig["PRODUCT"]["uiMemFullDay"] = int( uiMemRemaining / ( 86400 / uiLogIntBatt ) )
  print('ttConfig["PRODUCT"]["uiMemFullDay"] = %u'%ttConfig["PRODUCT"]["uiMemFullDay"])
  # -------------------
  # - Estimatif conso -
  # -------------------
  uiBattDayLife = self.tConfigParser.uiFLifetimeCalculation(ttConfig)
  # Nombre de jours avant fin batterie
  ttConfig["PRODUCT"]["uiBattDeadDay"]  = uiBattDayLife
  print('ttConfig["PRODUCT"]["uiBattDeadDay"] = %u'%ttConfig["PRODUCT"]["uiBattDeadDay"])

  # Donnée de mesure
  #sData = ""
  # Dummy byte
  sData = ( (ord('$')).to_bytes(1) )
  sData += ( (ord('M')).to_bytes(1) )
  for uiElt in range(uiCpt, len(tRaw)-2) :
   sData += ( int(tRaw[uiElt]).to_bytes(1) )
  sData += ( (ord('$')).to_bytes(1) )
  sData += ( (ord('$')).to_bytes(1) )

  print( sData )
  self.ttMeasure =  self.tConfigParser.ttFParseRecordedData( ttConfig, sData )

  self.tConfigParser.ttFCalculatedDataCalculation( ttConfig, self.ttMeasure )

 #----------------------------------------------
 # Calcul des voies calculées (MAJ)
 #----------------------------------------------
 def _vFProductUpdateCalculatedParameters( self ):
  print("-- _vFProductUpdateCalculatedParameters --")
  # Calcul des voies calculées
  self.tConfigParser.ttFCalculatedDataCalculation( self.ttConfig, self.ttMeasure )


