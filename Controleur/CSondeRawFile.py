# This Python file uses the following encoding: utf-8

#============================================================================#
# Librairies système
#============================================================================#
import sys
from datetime import datetime

#============================================================================#
# Librairies Qt
#============================================================================#
from PySide6.QtCore    import (QDate, QDateTime)
from PySide6.QtCore    import Slot
from PySide6.QtWidgets import QDialog, QFileDialog

#============================================================================#
# Librairies Utilisateur
#============================================================================#
from File.TSondeRawFile   import TSondeRawFile
from File.TFileRecord     import TFileRecord

#============================================================================#
# Variable
#============================================================================#

#============================================================================#
# Classe
#============================================================================#

#------------------------------------------------------------------------
# Controleur de main Windows
#------------------------------------------------------------------------
class CSondeRawFile:
 #----------------------------------------------
 # Init
 #----------------------------------------------
 def __init__( self, view, model, tINIConfig ):
  # Conservation des entrées
  self._model = model
  self._view  = view

  #self.ttConfig     = {}
  #self.ttMeasureRaw = []

  # Création pour rapport de calibration
  self.tSondeRawFile = TSondeRawFile()
  # Création objet écriture CSV
  self.tFileRecord = TFileRecord()

  # Init de la configuration avec ini-file
  # Temperature unit
  self.tSondeRawFile.ttConfig["CALCULATED"]["TEMP"]["bF"] = ( tINIConfig.tConfig["MEASURE"]["temperature_unit"] == "F" )
  self.tSondeRawFile.ttConfig["CALCULATED"]["TEMP"]["bC"] = not self.tSondeRawFile.ttConfig["CALCULATED"]["TEMP"]["bF"]
  # Depth unit
  self.tSondeRawFile.ttConfig["CALCULATED"]["DEPTH"]["bM"] = ( tINIConfig.tConfig["MEASURE"]["depth_unit"] == "m" )
  self.tSondeRawFile.ttConfig["CALCULATED"]["DEPTH"]["bF"] = not self.tSondeRawFile.ttConfig["CALCULATED"]["DEPTH"]["bM"]
  # TDS Factor
  self.tSondeRawFile.ttConfig["CALCULATED"]["TDS"]["fFactor"] = float(tINIConfig.tConfig["MEASURE"]["tds_factor"])
  # EC Temperature ref
  self.tSondeRawFile.ttConfig["CALCULATED"]["EC"]["sTSelect"] = tINIConfig.tConfig["MEASURE"]["ec_ref_temp"]

 #----------------------------------------------
 # Data - Ouverture d'une fenêtre pour enregistrement fichier
 #----------------------------------------------
 def vFRawOpenFile(self):
  print("-- vFRawOpenFile --")

  tFileName = QFileDialog.getOpenFileName(self._view, "Open file", "", "ASF File (*.asf)")
  print(tFileName)
  if( tFileName[0] != "" ):
   print(tFileName[0])
   #
   #self.tSondeRawFile.vFOpenRaw(tFileName[0], self.ttConfig, self.ttMeasureRaw)
   self.tSondeRawFile.vFOpenRaw(tFileName[0])
   # Affichage dans la vue du fichier
   self._view.tVSondeRawFile.vFDisplayProductNav()
   self._view.tVSondeRawFile.vFDisplayGeneralConfiguration( self.tSondeRawFile.ttConfig )

   #self.tFileRecord.vFCreateNewFileCSV(tFileName[0], self._model.tMSonde.tProduct.ttConfig, self._model.tMSonde.tProduct.ttMeasure)

   self._view.tVSondeRawFile.vFDATADisplayRecordedData(self.tSondeRawFile.ttConfig, self.tSondeRawFile.ttMeasure)
   # Connexion signaux
   self.connectSignalsPostInit()

 #----------------------------------------------
 # Data - Ouverture d'une fenêtre pour enregistrement fichier
 #----------------------------------------------
 def vFDataOpenFileDialogCSV(self):
  print("-- vFDataOpenFileDialogCSV --")
  tCurrentDateTime = datetime.now()
  print("%02u/%02u/%02u"%(tCurrentDateTime.day,
                          tCurrentDateTime.month,
                          tCurrentDateTime.year-2000))

  sFileNameDefault  = "%02u%02u%02u" % ( tCurrentDateTime.year, tCurrentDateTime.month, tCurrentDateTime.day )
  sFileNameDefault += "_%02u%02u%02u" % ( tCurrentDateTime.hour, tCurrentDateTime.minute, tCurrentDateTime.second )
  sFileNameDefault += "_" + self.tSondeRawFile.ttConfig["PRODUCT"]["sSiteID"]

  tFileName = QFileDialog.getSaveFileName(self._view, "Recording path", sFileNameDefault, "CSV File (*.csv)")
  print(tFileName)
  print(tFileName[0])
  if( tFileName[0] != "" ):
   self.tFileRecord.vFCreateNewFileCSV(tFileName[0], self.tSondeRawFile.ttConfig, self.tSondeRawFile.ttMeasure)

 #----------------------------------------------
 # Data - Ouverture d'une fenêtre pour enregistrement fichier
 #----------------------------------------------
 def vFDataOpenFileDialogTSV( self ):
  print("-- vFDataOpenFileDialogTSV --")
  tCurrentDateTime = datetime.now()
  print("%02u/%02u/%02u"%(tCurrentDateTime.day,
                    tCurrentDateTime.month,
                    tCurrentDateTime.year-2000))

  sFileNameDefault  = "%02u%02u%02u" % ( tCurrentDateTime.year, tCurrentDateTime.month, tCurrentDateTime.day )
  sFileNameDefault += "_%02u%02u%02u" % ( tCurrentDateTime.hour, tCurrentDateTime.minute, tCurrentDateTime.second )
  sFileNameDefault += "_" + self.tSondeRawFile.ttConfig["PRODUCT"]["sSiteID"]

  tFileName = QFileDialog.getSaveFileName(self._view, "Recording path", sFileNameDefault, "TAB File (*.tab)")
  print(tFileName)
  print(tFileName[0])
  if( tFileName[0] != "" ):
   self.tFileRecord.vFCreateNewFileTSV(tFileName[0], self.tSondeRawFile.ttConfig, self.tSondeRawFile.ttMeasure)

 #----------------------------------------------
 # PCConf - Modification EC Ref temperature
 #----------------------------------------------
 def vFPCConfECRefTempChange( self, sValue ):
  print("-- vFPCConfECRefTempChange --")

  print("sValue = "+sValue)
  # Mise à jour de la variable EC Temperature ref
  self.tSondeRawFile.ttConfig["CALCULATED"]["EC"]["sTSelect"] = sValue
  #
  self._view.vFPCONFChangeECRefTemperature(sValue)

  try:
   # Recalcul des voies calculées
   self.tSondeRawFile._vFProductUpdateCalculatedParameters()
   # Mise à jour des valeurs affichées
   self._view.tVSondeRawFile.vFDATAUpdateRecordedData(self.tSondeRawFile.ttConfig, self.tSondeRawFile.ttMeasure)
   # Update affichage des voies
   #self._view.tVSondeRawFile.vDataTreeviewHideColumn(self.tSondeRawFile.ttConfig, self.tSondeRawFile.ttMeasure)
  except Exception as err:
   print(err)

 #----------------------------------------------
 # PCConf - Modification unité T°/F°
 #----------------------------------------------
 def vFPCConfTempUnitChange( self, sValue ):
  print("-- vFPCConfTempUnitChange --")
  # Fahrenheit
  if( sValue == "F" ):
   self.tSondeRawFile.ttConfig["CALCULATED"]["TEMP"]["bF"] = True
   self.tSondeRawFile.ttConfig["CALCULATED"]["TEMP"]["bC"] = False
  else:
   self.tSondeRawFile.ttConfig["CALCULATED"]["TEMP"]["bF"] = False
   self.tSondeRawFile.ttConfig["CALCULATED"]["TEMP"]["bC"] = True
  # Modification temperature unit
  self._view.vFPCONFChangeTemperatureUnit( sValue )
  try:
   # Update affichage des voies
   self._view.tVSondeRawFile.vDataTreeviewHideColumn(self.tSondeRawFile.ttConfig, self.tSondeRawFile.ttMeasure)
  except Exception as err:
   print(err)

 #----------------------------------------------
 # PCConf - Modification unité m/f
 #----------------------------------------------
 def vFPCConfDepthUnitChange( self, sValue ):
  print("-- vFPCConfDepthUnitChange --")
  # Foot
  if( sValue == "f" ):
   self.tSondeRawFile.ttConfig["CALCULATED"]["DEPTH"]["bF"] = True
   self.tSondeRawFile.ttConfig["CALCULATED"]["DEPTH"]["bM"] = False
  else:
   self.tSondeRawFile.ttConfig["CALCULATED"]["DEPTH"]["bF"] = False
   self.tSondeRawFile.ttConfig["CALCULATED"]["DEPTH"]["bM"] = True
  # Modification temperature unit
  self._view.vFPCONFChangeDepthUnit( sValue )
  try:
   # Update affichage des voies
   self._view.tVSondeRawFile.vDataTreeviewHideColumn(self.tSondeRawFile.ttConfig, self.tSondeRawFile.ttMeasure)
  except Exception as err:
   print(err)

 #----------------------------------------------
 # PCConf - Modification TDS Factor
 #----------------------------------------------
 def vFPCConfTDSFactorChange( self, fValue ):
  print("-- vFPCConfTDSFactorChange --")
  # Mise à jour de la variable TDS Factor
  self.tSondeRawFile.ttConfig["CALCULATED"]["TDS"]["fFactor"] = fValue
  # Modification temperature unit
  self._view.vFPCONFChangeTDSFactor( fValue )
  try:
   # Recalcul des voies calculées
   self.tSondeRawFile._vFProductUpdateCalculatedParameters()
   # Mise à jour des valeurs affichées
   self._view.tVSondeRawFile.vFDATAUpdateRecordedData(self.tSondeRawFile.ttConfig, self.tSondeRawFile.ttMeasure)
   # Update affichage des voies
   #self._view.tVSondeRawFile.vDataTreeviewHideColumn(self.tSondeRawFile.ttConfig, self.tSondeRawFile.ttMeasure)
  except Exception as err:
   print(err)

 #----------------------------------------------
 # Connexion des signaux pour une sonde
 #----------------------------------------------
 def connectSignals( self ):
  print("-- CSondeRawFile > connectSignals --")
  #---------------
  # Detect/Connect
  #---------------
  # Détection produit sonde
  self._view.ui.pushButton_openRawFile.clicked.connect(self.vFRawOpenFile)
  self._view.ui.pushButton_openRawFile.clicked.connect( self._view.tVSondeRawFile.vFVSondeRawFileInitMode )

 #----------------------------------------------
 # Connexion des signaux pour une sonde
 #----------------------------------------------
 def connectSignalsPostInit( self ):
  print("-- connectSignalsPostInit --")

  #----------------
  # Data
  #----------------
  # Sélection/Déselection de toutes les voies
  self._view.ui.pushButton_dataSelectAll.clicked.connect(lambda:self._view.tVSondeRawFile.vDataSelectAllChannel(self.tSondeRawFile.ttConfig, self.tSondeRawFile.ttMeasure))
  self._view.ui.pushButton_dataDeselectAll.clicked.connect(lambda:self._view.tVSondeRawFile.vDataDeselectAllChannel(self.tSondeRawFile.ttConfig, self.tSondeRawFile.ttMeasure))
  # Export en CSV
  self._view.ui.exportToCSV_btn.clicked.connect(self.vFDataOpenFileDialogCSV)
  self._view.ui.exportToTAB_btn.clicked.connect(self.vFDataOpenFileDialogTSV)

  #----------------
  # PC Config
  #----------------
  # Validation
  self._view.tUIECRefTemp.siWriteData.connect( self.vFPCConfECRefTempChange )
  self._view.tUITempUnit.siWriteData.connect( self.vFPCConfTempUnitChange )
  self._view.tUIDepthUnit.siWriteData.connect( self.vFPCConfDepthUnitChange )
  self._view.tUITDSFactor.siWriteData.connect( self.vFPCConfTDSFactorChange )

 #----------------------------------------------
 # Déconnexion des signaux pour une sonde
 #----------------------------------------------
 def disconnectSignalsPostInit( self ):
  print("-- disconnectSignalsPostInit --")

  #----------------
  # Data
  #----------------
  # Sélection/Déselection de toutes les voies
  self._view.ui.pushButton_dataSelectAll.clicked.disconnect(lambda:self._view.tVSondeRawFile.vDataSelectAllChannel(self.tSondeRawFile.ttConfig, self.tSondeRawFile.ttMeasure))
  self._view.ui.pushButton_dataDeselectAll.clicked.disconnect(lambda:self._view.tVSondeRawFile.vDataDeselectAllChannel(self.tSondeRawFile.ttConfig, self.tSondeRawFile.ttMeasure))

  #----------------
  # PC Config
  #----------------
  # Validation
  self._view.tUIECRefTemp.siWriteData.disconnect( self.vFPCConfECRefTempChange )
  self._view.tUITempUnit.siWriteData.disconnect( self.vFPCConfTempUnitChange )
  self._view.tUIDepthUnit.siWriteData.disconnect( self.vFPCConfDepthUnitChange )
  self._view.tUITDSFactor.siWriteData.disconnect( self.vFPCConfTDSFactorChange )
