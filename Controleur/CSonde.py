# This Python file uses the following encoding: utf-8

#============================================================================#
# Librairies système
#============================================================================#
import sys
from datetime import datetime

#============================================================================#
# Librairies Qt
#============================================================================#
from PySide6.QtCore import (QDate, QDateTime)
from PySide6.QtCore import Slot

#============================================================================#
# Librairies Utilisateur
#============================================================================#
from Vue.VLib             import *
from Vue.VMainWindowLib   import TECalibSensorNavIndex, TECalibPointNavIndex
from File.TFileRecord     import TFileRecord
from File.TLiveViewRecord import TLiveViewRecord
from File.TCalibReport    import TCalibReport
from File.TSondeRawFile   import TSondeRawFile

#============================================================================#
# Variable
#============================================================================#

#============================================================================#
# Classe
#============================================================================#

#------------------------------------------------------------------------
# Controleur de main Windows
#------------------------------------------------------------------------
class CSonde:
 #----------------------------------------------
 # Init
 #----------------------------------------------
 def __init__( self, view, model, tINIConfig ):
  # Conservation des entrées
  self._model = model
  self._view  = view

  # Création objet écriture CSV
  self.tFileRecord = TFileRecord()
  # Création objet écriture CSV
  self.tLiveViewRecord = TLiveViewRecord()
  # Création pour rapport de calibration
  self.tCalibReport = TCalibReport()
  # Création pour rapport de calibration
  self.tSondeRawFile = TSondeRawFile()
  # Enregistrement
  self.bStartRecording = False

  # Init de la configuration avec ini-file
  # Temperature unit
  self._model.tMSonde.tProduct.ttConfig["CALCULATED"]["TEMP"]["bF"] = ( tINIConfig.tConfig["MEASURE"]["temperature_unit"] == "F" )
  self._model.tMSonde.tProduct.ttConfig["CALCULATED"]["TEMP"]["bC"] = not self._model.tMSonde.tProduct.ttConfig["CALCULATED"]["TEMP"]["bF"]
  # Depth unit
  self._model.tMSonde.tProduct.ttConfig["CALCULATED"]["DEPTH"]["bM"] = ( tINIConfig.tConfig["MEASURE"]["depth_unit"] == "m" )
  self._model.tMSonde.tProduct.ttConfig["CALCULATED"]["DEPTH"]["bF"] = not self._model.tMSonde.tProduct.ttConfig["CALCULATED"]["DEPTH"]["bM"]
  # TDS Factor
  self._model.tMSonde.tProduct.ttConfig["CALCULATED"]["TDS"]["fFactor"] = float(tINIConfig.tConfig["MEASURE"]["tds_factor"])
  # EC Temperature ref
  self._model.tMSonde.tProduct.ttConfig["CALCULATED"]["EC"]["sTSelect"] = tINIConfig.tConfig["MEASURE"]["ec_ref_temp"]

 #----------------------------------------------
 # Click bouton connect product
 #----------------------------------------------
 @Slot()
 def slotConnexionProductConnectClicked( self, sCom ):
  print("-- slotConnexionProductConnectClicked --")
  # Réinit du mode Sonde
  self._view.tVSonde.vFVSondeInitMode()
  # Requête de la configuration du produit
  self._model.tMSonde.tProduct.vFProductGetConfiguration( sCom )
  # Affichage de la fenêtre loading
  self._view.tUILoadingScreen.vFShow("Connection to sonde\nReading configuration")

 #----------------------------------------------
 # Click bouton product COM
 #----------------------------------------------
 @Slot()
 def slotProductConnectClicked( self ):
  print("-- slotProductConnectClicked --")
  # Récupération du port COM de la sonde en cours
  sCOM = self._view.ui.label_InterfaceCom.text()
  # Lancement
  self._view.tUILoadingScreen.vFShow("Reading config")
  self._view.tUIBackground.vFOpen( self._view.size() )
  # Requête de la configuration du produit
  self._model.tMSonde.tProduct.vFProductGetConfiguration( sCOM )
  print("-- slotProductConnectClicked End--")

 #----------------------------------------------
 # Dashboard - Création des signaux dashboard - Channel select
 #----------------------------------------------
 @Slot()
 def dashboardChannelSelectConnect( self, ucChannel, tChannel, tWidget ):
  print("-- dashboardChannelSelectConnect --")
  print("ucChannel = %d"%ucChannel)
  # Event ouverture de la fenêtre
  tWidget.mouseReleaseEvent     = lambda event:self._view.tVSonde.vFDashboardChannelSelectOpen(ucChannel, tChannel, tWidget)

 #----------------------------------------------
 # Liveview - Ouverture d'une fenêtre pour enregistrement fichier
 #----------------------------------------------
 def vFLiveviewOpenFileDialog( self ):
  print("-- vFLiveviewOpenFileDialog --")
  tCurrentDateTime = datetime.now()
  print("%02u/%02u/%02u"%(tCurrentDateTime.day,
                          tCurrentDateTime.month,
                          tCurrentDateTime.year-2000))

  sFileNameDefault  = "%02u%02u%02u" % ( tCurrentDateTime.year, tCurrentDateTime.month, tCurrentDateTime.day )
  sFileNameDefault += "_%02u%02u%02u" % ( tCurrentDateTime.hour, tCurrentDateTime.minute, tCurrentDateTime.second )
  sFileNameDefault += "_" + self._model.tMSonde.tProduct.ttConfig["PRODUCT"]["sSiteID"]

  tFileName = QFileDialog.getSaveFileName(self._view, "Recording path", sFileNameDefault, "TAB File (*.tab)")
  print(tFileName)
  print(tFileName[0])
  if( tFileName[0] != "" ):
   # Démarrage de l'enregistrement
   self.bStartRecording = True
   # Modification de la vue
   self._view.tVSonde.vFLiveviewStartRecording()
   self._view.tVSonde.vFCALIBRATIONStartRecording()
   # Création du fichier
   self.tLiveViewRecord.vFCreateNewFileTSV(tFileName[0], self._model.tMSonde.tProduct.ttConfig)
 #----------------------------------------------
 def vFLiveviewRecordingNewSample( self, ttConfig ):
  print("-- vFLiveviewRecordingNewSample --")
  if( self.bStartRecording ):
   self.tLiveViewRecord.vFAddSample( ttConfig )
 #----------------------------------------------
 def vFLiveviewStopRecording( self ):
  print("-- vFLiveviewStopRecording --")
  # Démarrage de l'enregistrement
  self.bStartRecording = False
  # Modification de la vue
  self._view.tVSonde.vFLiveviewStopRecording()
  self._view.tVSonde.vFCALIBRATIONStopRecording()

 #----------------------------------------------
 # Création des signaux calibration - Sensor select
 #----------------------------------------------
 @Slot()
 def calibrationSensorSelectConnect( self, sConfigName, ucChannel, tChannel, tWidget, ttConfig ):
  print("-- calibrationSensorSelectConnect --")
  print("ucChannel = %d"%ucChannel)
  # Event ouverture de la fenêtre
  tWidget.mouseReleaseEvent     = lambda event:self._view.tVSonde.vFCALIBRATIONSensorNavSelectionDynamic(sConfigName, ucChannel, tChannel, tWidget, ttConfig)

 #----------------------------------------------
 # Signal Calibration - Point select - Passage du menu point calibration à la calibration du point
 #----------------------------------------------
 @Slot()
 def calibrationPointSelectConnect( self, sConfigName, ucChannel, tChannel, tWidget, uiPoint ):
  print("-- calibrationPointSelectConnect --")
  print("ucChannel = %d"%ucChannel)
  print("uiPoint   = %d"%uiPoint)
  # Event ouverture de la fenêtre
  #tWidget.mouseReleaseEvent = lambda event:self._view.tVSonde.vFCALIBRATIONPointNavSelectionDynamic(sConfigName, ucChannel, tChannel, tWidget, uiPoint)
  tWidget.mouseReleaseEvent = lambda event:self.calibrationPointStartCalibrationPage(sConfigName, ucChannel, tChannel, tWidget, uiPoint)
 #----------------------------------------------
 def calibrationPointStartCalibrationPage( self, sConfigName, ucChannel, tChannel, tWidget, uiPoint ):
  print("-- calibrationPointStartCalibrationPage --")
  print("sConfigName = "+sConfigName)
  print("ucChannel = %d"%ucChannel)
  print("uiPoint = %d"%uiPoint)
  # Test si calibration autorisé pour point demandé
  if( not self._model.tMSonde.bFCalibrationIsCalibrationAllowed( sConfigName, ucChannel, tChannel, uiPoint ) ):
   # On quitte
   return
  # Passage en calibration du point sur la vue
  self._view.tVSonde.vFCALIBRATIONPointNavSelectionDynamic(sConfigName, ucChannel, tChannel, tWidget, uiPoint)

 #----------------------------------------------
 # Restauration point de calibration
 #----------------------------------------------
 @Slot()
 def calibrationPointRestore( self, sConfigName ):
  print("-- calibrationPointRestore --")
  print("sConfigName = "+sConfigName)
  # Event ouverture de la fenêtre
  self._view.ui.pushButton_RestoreDefaultCalibration.mouseReleaseEvent = lambda event:self._view.tVSonde.tUICalibRestore.vFOpen(sConfigName)

 #----------------------------------------------
 # Validation point de calibration
 #----------------------------------------------
 def vFCMWDataEC_TValueUpdate( self, sValue ):
  print("-- vFCMWDataEC_TValueUpdate --")
  #fTDSValue = self._view.ui.doubleSpinBox_TDSValue.value()
  # Mise à jour de la variable TDS Factor
  self._model.tMSonde.tProduct.ttConfig["CALCULATED"]["EC"]["sTSelect"] = sValue
  # Recalcul des voies calculées
  self._view.tVSonde.vFDATAUpdateRecordedData(self._model.tMSonde.tProduct.ttConfig, self._model.tMSonde.tProduct.ttMeasure)

 #----------------------------------------------
 # Ecriture AUX GS Factor
 #----------------------------------------------
 def vFCMWWriteGSFactor( self, fValue ):
  print("-- vFCMWWriteGSFactor --")
  print("fValue = %f"%fValue)
  # Sauvegarde de l'onglet sélectionné
  sConfigName = self._view.tVSonde.tCalibrationCurrentSensor["sConfigName"]
  ucChannel   = self._view.tVSonde.tCalibrationCurrentSensor["ucChannel"]
  tChannel    = self._view.tVSonde.tCalibrationCurrentSensor["tChannel"]
  print("sConfigName = "+sConfigName)
  print("ucChannel = %d"%ucChannel)
  self._model.tMSonde.slotWriteGSFactor( sConfigName, ucChannel, fValue )

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
  sFileNameDefault += "_" + self._model.tMSonde.tProduct.ttConfig["PRODUCT"]["sSiteID"]

  tFileName = QFileDialog.getSaveFileName(self._view, "Recording path", sFileNameDefault, "CSV File (*.csv)")
  print(tFileName)
  print(tFileName[0])
  if( tFileName[0] != "" ):
   self.tFileRecord.vFCreateNewFileCSV(tFileName[0], self._model.tMSonde.tProduct.ttConfig, self._model.tMSonde.tProduct.ttMeasure)

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
  sFileNameDefault += "_" + self._model.tMSonde.tProduct.ttConfig["PRODUCT"]["sSiteID"]

  tFileName = QFileDialog.getSaveFileName(self._view, "Recording path", sFileNameDefault, "TAB File (*.tab)")
  print(tFileName)
  print(tFileName[0])
  if( tFileName[0] != "" ):
   self.tFileRecord.vFCreateNewFileTSV(tFileName[0], self._model.tMSonde.tProduct.ttConfig, self._model.tMSonde.tProduct.ttMeasure)

 #----------------------------------------------
 # Data - Ouverture d'une fenêtre pour enregistrement fichier
 #----------------------------------------------
 def vFDataOpenFileDialogRAW( self ):
  print("-- vFDataOpenFileDialogRAW --")
  tCurrentDateTime = datetime.now()
  print("%02u/%02u/%02u"%(tCurrentDateTime.day,
                    tCurrentDateTime.month,
                    tCurrentDateTime.year-2000))

  sFileNameDefault  = "%02u%02u%02u" % ( tCurrentDateTime.year, tCurrentDateTime.month, tCurrentDateTime.day )
  sFileNameDefault += "_%02u%02u%02u" % ( tCurrentDateTime.hour, tCurrentDateTime.minute, tCurrentDateTime.second )
  sFileNameDefault += "_" + self._model.tMSonde.tProduct.ttConfig["PRODUCT"]["sSiteID"]

  tFileName = QFileDialog.getSaveFileName(self._view, "Recording path", sFileNameDefault, "ASF File (*.asf)")
  print(tFileName)
  print(tFileName[0])
  if( tFileName[0] != "" ):
   self.tSondeRawFile.vFCreateNewFileRaw(tFileName[0], self._model.tMSonde.tProduct.ttConfig, self._model.tMSonde.tProduct.ttMeasureRaw)

 #----------------------------------------------
 # Validation point de calibration
 #----------------------------------------------
 def vFCMWCalibrationValidatePoint( self ):
  print("-- vFCMWCalibrationValidatePoint --")
  sCalibPointName    = self._view.ui.label_calibPointName.text()
  sHiddenChannelName = self._view.ui.label_hiddenChannelName.text()
  sHiddenPointNumber = self._view.ui.label_hiddenPointNumber.text()
  tsCalibPointName   = sCalibPointName.split(" - ")
  print("sCalibPointName     = "+sCalibPointName)
  print("sHiddenChannelName  = "+sHiddenChannelName)
  print("tsCalibPointName[1] = "+tsCalibPointName[1])
  print("sHiddenPointNumber  = "+sHiddenPointNumber)

  # Ouverture fenêtre d'attente
  self._view.tUILoadingScreen.vFShow("Writing to sonde...")

  tCalibConfigObj = {}
  if( sHiddenChannelName == "ORP" ):
   sORPCalValue = self._view.ui.comboBox_ORPCalValue_Point.currentText()
   tCalibConfigObj["sORPCalValue"] = sORPCalValue
  if( sHiddenChannelName == "EC" ):
   sECCalValue      = self._view.ui.comboBox_ECCalValue_Point.currentText()
   uiECCalUserValue = int(self._view.ui.spinBox_ECCalValue_2_Point.text())
   tCalibConfigObj["sECCalValue"]      = sECCalValue
   tCalibConfigObj["uiECCalUserValue"] = uiECCalUserValue
   print('tCalibConfigObj["sECCalValue"]='+tCalibConfigObj["sECCalValue"])
   print('tCalibConfigObj["sECCalValue"]='+tCalibConfigObj["sECCalValue"])

  #  Appel de la fonction normal
  self._model.tMSonde.slotWriteCalibrationPoint( sHiddenChannelName, int(sHiddenPointNumber), tCalibConfigObj )

 #----------------------------------------------
 # PCConf - Modification EC Ref temperature
 #----------------------------------------------
 def vFPCConfECRefTempChange( self, sValue ):
  print("-- vFPCConfECRefTempChange --")

  print("sValue = "+sValue)
  # Mise à jour de la variable EC Temperature ref
  self._model.tMSonde.tProduct.ttConfig["CALCULATED"]["EC"]["sTSelect"] = sValue
  #
  self._view.vFPCONFChangeECRefTemperature(sValue)

  try:
   # Recalcul des voies calculées
   self._model.tMSonde.tProduct._vFProductUpdateCalculatedParameters()
   # Mise à jour des valeurs affichées
   self._view.tVSonde.vFDATAUpdateRecordedData(self._model.tMSonde.tProduct.ttConfig, self._model.tMSonde.tProduct.ttMeasure)
   # Update affichage des voies
   #self._view.tVSonde.vDataTreeviewHideColumn(self._model.tMSonde.tProduct.ttConfig, self._model.tMSonde.tProduct.ttMeasure)
  except Exception as err:
   print(err)

 #----------------------------------------------
 # PCConf - Modification unité T°/F°
 #----------------------------------------------
 def vFPCConfTempUnitChange( self, sValue ):
  print("-- vFPCConfTempUnitChange --")
  # Fahrenheit
  if( sValue == "F" ):
   self._model.tMSonde.tProduct.ttConfig["CALCULATED"]["TEMP"]["bF"] = True
   self._model.tMSonde.tProduct.ttConfig["CALCULATED"]["TEMP"]["bC"] = False
  else:
   self._model.tMSonde.tProduct.ttConfig["CALCULATED"]["TEMP"]["bF"] = False
   self._model.tMSonde.tProduct.ttConfig["CALCULATED"]["TEMP"]["bC"] = True
  # Modification temperature unit
  self._view.vFPCONFChangeTemperatureUnit( sValue )
  try:
   # Update affichage des voies
   self._view.tVSonde.vDataTreeviewHideColumn(self._model.tMSonde.tProduct.ttConfig, self._model.tMSonde.tProduct.ttMeasure)
  except Exception as err:
   print(err)
  #%%AP - Ajout - Relecture de la configuration produit
  self.slotProductConnectClicked()

 #----------------------------------------------
 # PCConf - Modification unité m/f
 #----------------------------------------------
 def vFPCConfDepthUnitChange( self, sValue ):
  print("-- vFPCConfDepthUnitChange --")
  # Foot
  if( sValue == "f" ):
   self._model.tMSonde.tProduct.ttConfig["CALCULATED"]["DEPTH"]["bF"] = True
   self._model.tMSonde.tProduct.ttConfig["CALCULATED"]["DEPTH"]["bM"] = False
  else:
   self._model.tMSonde.tProduct.ttConfig["CALCULATED"]["DEPTH"]["bF"] = False
   self._model.tMSonde.tProduct.ttConfig["CALCULATED"]["DEPTH"]["bM"] = True
  # Modification temperature unit
  self._view.vFPCONFChangeDepthUnit( sValue )
  try:
   # Update affichage des voies
   self._view.tVSonde.vDataTreeviewHideColumn(self._model.tMSonde.tProduct.ttConfig, self._model.tMSonde.tProduct.ttMeasure)
  except Exception as err:
   print(err)
  #%%AP - Ajout - Relecture de la configuration produit
  self.slotProductConnectClicked()

 #----------------------------------------------
 # PCConf - Modification TDS Factor
 #----------------------------------------------
 def vFPCConfTDSFactorChange( self, fValue ):
  print("-- vFPCConfTDSFactorChange --")
  # Mise à jour de la variable TDS Factor
  self._model.tMSonde.tProduct.ttConfig["CALCULATED"]["TDS"]["fFactor"] = fValue
  # Modification temperature unit
  self._view.vFPCONFChangeTDSFactor( fValue )
  try:
   # Recalcul des voies calculées
   self._model.tMSonde.tProduct._vFProductUpdateCalculatedParameters()
   # Mise à jour des valeurs affichées
   self._view.tVSonde.vFDATAUpdateRecordedData(self._model.tMSonde.tProduct.ttConfig, self._model.tMSonde.tProduct.ttMeasure)
   # Update affichage des voies
   #self._view.tVSonde.vDataTreeviewHideColumn(self._model.tMSonde.tProduct.ttConfig, self._model.tMSonde.tProduct.ttMeasure)
  except Exception as err:
   print(err)

 #----------------------------------------------
 # Liveview - Ouverture d'une fenêtre pour enregistrement fichier
 #----------------------------------------------
 def vFCALIBReportSaveDialog( self ):
  print("-- vFCALIBReportSaveDialog --")
  tCurrentDateTime = datetime.now()
  print("%02u/%02u/%02u"%(tCurrentDateTime.day,
                          tCurrentDateTime.month,
                          tCurrentDateTime.year-2000))

  sFileNameDefault  = "%02u%02u%02u" % ( tCurrentDateTime.year, tCurrentDateTime.month, tCurrentDateTime.day )
  sFileNameDefault += "_%02u%02u%02u" % ( tCurrentDateTime.hour, tCurrentDateTime.minute, tCurrentDateTime.second )
  sFileNameDefault += "_" + self._model.tMSonde.tProduct.ttConfig["PRODUCT"]["sSiteID"]+"_report"

  tFileName = QFileDialog.getSaveFileName(self._view, "Recording path", sFileNameDefault, "TXT File (*.txt)")
  print(tFileName)
  print(tFileName[0])
  if( tFileName[0] != "" ):
   self.tCalibReport.vFCreateNewFile(self._model.tMSonde.tProduct.ttConfig, tFileName[0])

 #----------------------------------------------
 # Connexion des signaux pour une sonde
 #----------------------------------------------
 def connectSignals( self ):
  print("-- CSonde > connectSignals --")

  #---------------
  # Detect/Connect
  #---------------
  # Détection produit sonde
  self._view.ui.pushButton_detectProduct.clicked.connect(lambda:self._view.tUILoadingScreen.vFShow("Products detection"))
  self._view.ui.pushButton_detectProduct.clicked.connect(self._model.tMSonde.tProduct.vFSondeList)
  # Fin détection produit sonde
  self._model.tMSonde.tProduct.siDetectProductEnd.connect(self._view.vFDisplaySondeDetected)
  self._model.tMSonde.tProduct.siDetectProductEnd.connect(self._view.tUILoadingScreen.vFClose)

  # Connexion - Signal connexion sonde
  self._view.xConnectionSondeSelectConnectSignal.connect(self.connectionSondeSelectConnect)

  self._model.tMSonde.tProduct.siConfigurationReadEnd.connect(self.connectSignalsPostInit)
  self._model.tMSonde.tProduct.siConfigurationReadEnd.connect(self._view.tVSonde.vFDisplayGeneralConfiguration)
  self._model.tMSonde.tProduct.siConfigurationReadEnd.connect(self._view.tVSonde.vFDisplayProductNav)
  self._model.tMSonde.tProduct.siConfigurationReadEnd.connect(self._view.tUILoadingScreen.vFClose)
  #----------------
  # Connect
  #----------------
  self._view.ui.pushButton_detectProduct.clicked.connect( self._view.tVSonde.vFVSondeInitMode )
  self._view.ui.pushButton_detectProduct.clicked.connect( self._view.tVSonde.vFDisplayProductNavInit )


 #----------------------------------------------
 # Connexion des signaux pour une sonde
 #----------------------------------------------
 def connectSignalsPostInit( self ):
  print("-- CSonde > connectSignalsPostInit --")

  # Suppression du signal
  self._model.tMSonde.tProduct.siConfigurationReadEnd.disconnect(self.connectSignalsPostInit)
  #---------------
  # Général
  #---------------
  # Gestion du menu nav AS
  self._view.ui.connexion_btn.clicked.connect(lambda:self._view.tVSonde.vFNavASBtnClicked(0))
  self._view.ui.dashboard_btn.clicked.connect(lambda:self._view.tVSonde.vFNavASBtnClicked(1))
  self._view.ui.liveview_btn.clicked.connect(lambda:self._view.tVSonde.vFNavASBtnClicked(2))
  self._view.ui.data_btn.clicked.connect(lambda:self._view.tVSonde.vFNavASBtnClicked(3))
  self._view.ui.calibration_btn.clicked.connect(lambda:self._view.tVSonde.vFNavASBtnClicked(4))
  self._view.ui.about_btn.clicked.connect(lambda:self._view.tVSonde.vFNavASBtnClicked(5))
  self._view.ui.pcConfig_btn.clicked.connect(lambda:self._view.tVSonde.vFNavASBtnClicked(6))
  # Erreur général
  self._model.tMSonde.tProduct.siError.connect(self._view.tUILoadingScreen.vFClose)
  self._model.tMSonde.tProduct.siError.connect(lambda sError:vFAlert(self._view, "Error", sError))
  self._model.tMSonde.siErrorMsg.connect(self._view.tUILoadingScreen.vFClose)
  self._model.tMSonde.siErrorMsg.connect(lambda sTitle, sMsg:vFAlert(self._view, sTitle, sMsg))

  #----------------
  # Sur ouverture fenêtre
  #----------------
  self._view.tUIInfo.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tUIStab.siOpen.connect( lambda:self._view.tUIBackground.vFOpen( self._view.size() ) )
  self._view.tUIGSFactor.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tUIDataGetWait.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVSonde.tUIClearSondeMemory.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVSonde.tUINewBatteriesFitted.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVSonde.tUIUpdateClockWithPC.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVSonde.tUISondeDate.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVSonde.tUISondeTime.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVSonde.tUISiteID.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVSonde.tUISiteLatitude.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVSonde.tUISiteLongitude.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVSonde.tUIChannelSelect.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVSonde.tUILogDataEvery.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVSonde.tUICleanEvery.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVSonde.tUISetupLoggingState.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVSonde.tUISetupLoggingCheck.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVSonde.tUISetupLoggingEvery.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVSonde.tUISetupLoggingThreshold.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVSonde.tUIOpticalAvg.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVSonde.tUICalibRestore.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))

  #----------------
  # Sur fermeture fenêtre
  #----------------
  self._view.tUIInfo.siClose.connect( self._view.tUIBackground.close )
  self._view.tUIStab.siClose.connect(self._view.tUIBackground.close)
  self._view.tUIGSFactor.siClose.connect(self._view.tUIBackground.close)
  self._view.tUIDataGetWait.siClose.connect(self._view.tUIBackground.close)
  self._view.tVSonde.tUIClearSondeMemory.siClose.connect(self._view.tUIBackground.close)
  self._view.tVSonde.tUINewBatteriesFitted.siClose.connect(self._view.tUIBackground.close)
  self._view.tVSonde.tUIUpdateClockWithPC.siClose.connect(self._view.tUIBackground.close)
  self._view.tVSonde.tUISondeDate.siClose.connect(self._view.tUIBackground.close)
  self._view.tVSonde.tUISondeTime.siClose.connect(self._view.tUIBackground.close)
  self._view.tVSonde.tUISiteID.siClose.connect(self._view.tUIBackground.close)
  self._view.tVSonde.tUISiteLatitude.siClose.connect(self._view.tUIBackground.close)
  self._view.tVSonde.tUISiteLongitude.siClose.connect(self._view.tUIBackground.close)
  self._view.tVSonde.tUIChannelSelect.siClose.connect(self._view.tUIBackground.close)
  self._view.tVSonde.tUILogDataEvery.siClose.connect(self._view.tUIBackground.close)
  self._view.tVSonde.tUICleanEvery.siClose.connect(self._view.tUIBackground.close)
  self._view.tVSonde.tUISetupLoggingState.siClose.connect(self._view.tUIBackground.close)
  self._view.tVSonde.tUISetupLoggingCheck.siClose.connect(self._view.tUIBackground.close)
  self._view.tVSonde.tUISetupLoggingEvery.siClose.connect(self._view.tUIBackground.close)
  self._view.tVSonde.tUISetupLoggingThreshold.siClose.connect(self._view.tUIBackground.close)
  self._view.tVSonde.tUIOpticalAvg.siClose.connect(self._view.tUIBackground.close)
  self._view.tVSonde.tUICalibRestore.siClose.connect(self._view.tUIBackground.close)

  #----------------
  # Dashboard
  #----------------
  # - Ouverture fenêtre - Modification paramètre
  self._view.ui.clearSondeMem_btn.clicked.connect( self._view.tVSonde.tUIClearSondeMemory.vFOpen )
  self._view.ui.newBatteryFitted_btn.clicked.connect( self._view.tVSonde.tUINewBatteriesFitted.vFOpen )
  self._view.ui.resyncClockWithPC_btn.clicked.connect( self._view.tVSonde.tUIUpdateClockWithPC.vFOpen )
  self._view.ui.widget_SondeDate.mouseReleaseEvent          = self._view.tVSonde.vFDashboardSondeDateOpen
  self._view.ui.widget_SondeTime.mouseReleaseEvent          = self._view.tVSonde.vFDashboardSondeTimeOpen
  self._view.ui.widget_SiteID.mouseReleaseEvent             = self._view.tVSonde.vFDashboardSiteIDOpen
  self._view.ui.widget_SiteLatitude.mouseReleaseEvent       = self._view.tVSonde.vFDashboardSiteLatitudeOpen
  self._view.ui.widget_SiteLongitude.mouseReleaseEvent      = self._view.tVSonde.vFDashboardSiteLongitudeOpen
  self._view.ui.widget_LogDataEvery.mouseReleaseEvent       = self._view.tVSonde.vFDashboardLogDataEveryOpen
  self._view.ui.widget_CleanEvery.mouseReleaseEvent         = self._view.tVSonde.vFDashboardCleanEveryOpen
  self._view.ui.widget_EventLogState.mouseReleaseEvent      = self._view.tVSonde.vFDashboardSetupLoggingStateOpen
  self._view.ui.widget_EventLogCheck.mouseReleaseEvent      = self._view.tVSonde.vFDashboardSetupLoggingCheckOpen
  self._view.ui.widget_EventLogEvery.mouseReleaseEvent      = self._view.tVSonde.vFDashboardSetupLoggingEveryOpen
  self._view.ui.widget_EventLogThreshold.mouseReleaseEvent  = self._view.tVSonde.vFDashboardSetupLoggingThresholdOpen
  self._view.ui.widget_OpticalAveraging.mouseReleaseEvent   = self._view.tVSonde.vFDashboardOpticalAveragingOpen

  # Dynamique channel display/selection
  self._view.tVSonde.xDashboardChannelSelectConnectSignal.connect(self.dashboardChannelSelectConnect)

  #----------------
  # Dasboard - Validation écriture de donnée
  #----------------
  self._view.tVSonde.tUISondeDate.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVSonde.tUISondeTime.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVSonde.tUISiteID.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVSonde.tUISiteLatitude.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVSonde.tUISiteLongitude.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVSonde.tUILogDataEvery.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVSonde.tUICleanEvery.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVSonde.tUISetupLoggingState.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVSonde.tUISetupLoggingCheck.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVSonde.tUISetupLoggingEvery.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVSonde.tUISetupLoggingThreshold.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVSonde.tUIOpticalAvg.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  # Fenêtre écriture Aux assignement
  self._view.tVSonde.tUIChannelSelect.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  # Calibration
  self._view.tVSonde.tUICalibRestore.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))

  #------------------------
  # -- Dashboard Windows --
  #------------------------
  # Clear memory
  self._view.tVSonde.tUIClearSondeMemory.siAccept.connect(self._model.tMSonde.vFModelClearMemoryCMD)
  self._view.tVSonde.tUIClearSondeMemory.siAccept.connect(lambda:self._view.tUILoadingScreen.vFShow("Clearing memory..."))
   # New batteries fitted
  self._view.tVSonde.tUINewBatteriesFitted.siAccept.connect(self._model.tMSonde.siNewBatteriesFittedStart)
  self._view.tVSonde.tUINewBatteriesFitted.siAccept.connect(lambda:self._view.tUILoadingScreen.vFShow("New batteries fitted \ntaking into account"))
  # Update clock with PC
  self._view.tVSonde.tUIUpdateClockWithPC.siAccept.connect(self._model.tMSonde.slotWriteSondeDateTimePC)
  self._view.tVSonde.tUIUpdateClockWithPC.siAccept.connect(lambda:self._view.tUILoadingScreen.vFShow("Updating clock..."))
  # Modification paramètre - Validation écriture
  self._view.tVSonde.tUISondeDate.siWriteData.connect(self._model.tMSonde.slotWriteSondeDate)
  self._view.tVSonde.tUISondeTime.siWriteData.connect(self._model.tMSonde.slotWriteSondeTime)
  self._view.tVSonde.tUISiteID.siWriteData.connect(self._model.tMSonde.slotWriteSiteID)
  self._view.tVSonde.tUISiteLatitude.siWriteData.connect(self._model.tMSonde.slotWriteSiteLatitude)
  self._view.tVSonde.tUISiteLongitude.siWriteData.connect(self._model.tMSonde.slotWriteSiteLongitude)
  self._view.tVSonde.tUILogDataEvery.siWriteData.connect(self._model.tMSonde.slotWriteLogDataEvery)
  self._view.tVSonde.tUICleanEvery.siWriteData.connect(self._model.tMSonde.slotWriteCleanEvery)
  self._view.tVSonde.tUISetupLoggingState.siWriteData.connect(self._model.tMSonde.slotWriteLogEventState)
  self._view.tVSonde.tUISetupLoggingCheck.siWriteData.connect(self._model.tMSonde.slotWriteLogEventSensor)
  self._view.tVSonde.tUISetupLoggingEvery.siWriteData.connect(self._model.tMSonde.slotWriteLogEventEvery)
  self._view.tVSonde.tUISetupLoggingThreshold.siWriteData.connect(self._model.tMSonde.slotWriteLogEventThreshold)
  self._view.tVSonde.tUIOpticalAvg.siWriteData.connect(self._model.tMSonde.slotWriteOpticalAverage)
  # Fenêtre écriture Aux assignement
  self._view.tVSonde.tUIChannelSelect.siWriteData.connect(self._model.tMSonde.slotWriteAUXChannelSelect)
  # Fin d'écriture
  self._model.tMSonde.siClearMemoryEndSuccess.connect(self.slotProductConnectClicked)
  self._model.tMSonde.siNewBatteriesFittedEndSuccess.connect(self.slotProductConnectClicked)

  self._model.tMSonde.tProduct.siConfigSiteWriteEnd.connect(self.slotProductConnectClicked)
  self._model.tMSonde.tProduct.siUserSettingsWriteEnd.connect(self.slotProductConnectClicked)
  self._model.tMSonde.tProduct.siDateTimeSondeWriteEnd.connect(self.slotProductConnectClicked)
  self._model.tMSonde.tProduct.siAUXAssignementWriteEnd.connect(self.slotProductConnectClicked)


  #----------------
  # Liveview
  #----------------
  # Démarrage mesure
  self._view.ui.startMeasure_btn.clicked.connect(self._model.tMSonde.vFMeasureDataReadStart)
  self._view.ui.startMeasure_btn.clicked.connect(self._view.tVSonde.vFStartMeasureData)
  # Stop mesure
  self._view.ui.stopMeasure_btn.clicked.connect(self._model.tMSonde.vFMeasureDataReadStop)
  self._view.ui.stopMeasure_btn.clicked.connect(self._view.tVSonde.vFStopMeasureData)
  # Effacement graph
  self._view.ui.clearMeasure_btn.clicked.connect(self._view.tVSonde.vFClearMeasureData)
  # Affichage résultat
  self._model.tMSonde.siMeasureDataReadEnd.connect(self._view.tVSonde.vFDisplayMeasureData)
  self._model.tMSonde.siMeasureDataReadEnd.connect(self.vFLiveviewRecordingNewSample)
  # Liveview - Sur click box mesure
  self._view.tVSonde.siLiveviewClickBox.connect( self.vFCMainWindowBoxClickConnect )
  # Liveview - Enregistrement Liveview
  self._view.ui.pushButton_LiveViewRecord.clicked.connect( self.vFLiveviewOpenFileDialog )
  self._view.ui.pushButton_LiveViewRecordStop.clicked.connect( self.vFLiveviewStopRecording )

  #----------------
  # Calibration
  #----------------
  # Balai
  self._view.ui.cleanSonde_btn.clicked.connect(self._model.tMSonde.tProduct.bFProductGetDirectAccessModeWiperStart)
  self._view.ui.cleanSonde_btn.clicked.connect(lambda:self._view.tUILoadingScreen.vFShow("Cleaning..."))
  self._model.tMSonde.tProduct.siWiperStartEnd.connect(self._view.tUILoadingScreen.vFClose)
  self._model.tMSonde.tProduct.siWiperStartEnd.connect(lambda:self._view.tUIInfo.vFOpen("Wiper", "Cleaning success"))
  # Texte calibration report Export
  self._view.ui.exportToTxt_btn.clicked.connect(self.vFCALIBReportSaveDialog)
  # Dynamique capteur nav
  self._view.tVSonde.xCalibrationSensorSelectConnectSignal.connect(self.calibrationSensorSelectConnect)

  # Dynamique passage au menu point de calibration
  self._view.tVSonde.siCalibrationPointSelectConnectSignal.connect(self.calibrationPointSelectConnect)
  # Annulation point de calibration
  self._view.ui.pushButton_calibrateCancel.clicked.connect(lambda:self._view.tVSonde.vFCALIBRATIONPointNavSelection(TECalibPointNavIndex.MAIN))
  # Démarrage mesure
  self._view.tVSonde.xCalibrationPointPageDisplayedSignal.connect(self._model.tMSonde.vFMeasureDataReadStart)
  # Stop mesure
  self._view.ui.pushButton_calibrateCancel.clicked.connect(self._model.tMSonde.vFMeasureDataReadStop)
  # GS factor
  self._view.ui.widget_AuxGSFactor.mouseReleaseEvent = lambda event:self._view.tUIGSFactor.vFOpen( float(self._view.ui.label_AuxGSFactor.text()) )
  self._view.tUIGSFactor.siWriteData.connect( lambda:self._view.tUILoadingScreen.vFShow("Configuration writing...") )
  self._view.tUIGSFactor.siWriteData.connect( self.vFCMWWriteGSFactor )
  # Liveview - Enregistrement Liveview
  self._view.tVSonde.xCalibrationPointPageDisplayedSignal.connect( self._view.tVSonde.vFCALIBRATIONMesureStart )
  self._view.ui.pushButton_calibrateCancel.clicked.connect( self.vFLiveviewStopRecording )
  self._view.ui.pushButton_CalibRecord.clicked.connect( self.vFLiveviewOpenFileDialog )
  self._view.ui.pushButton_CalibRecordStop.clicked.connect( self.vFLiveviewStopRecording )
  self._model.tMSonde.tProduct.siCalibrationCMDPointEnd.connect(self.vFLiveviewStopRecording)
  self._model.tMSonde.siCalibrationCMDPointError.connect(self.vFLiveviewStopRecording)

  # Validation calibration
  self._view.ui.pushButton_calibrateAndExit.clicked.connect(self.vFCMWCalibrationValidatePoint)
  # Validation rapidCal btn
  self._view.ui.rapidCal_btn.clicked.connect(self._model.tMSonde.slotWriteCalibrationPointRapidCal)
  # Calibration - Fin de validation point
  self._model.tMSonde.tProduct.siCalibrationCMDPointEnd.connect(lambda:self._view.tVSonde.vFCALIBRATIONPointNavSelection(TECalibPointNavIndex.MAIN))
  self._model.tMSonde.tProduct.siCalibrationCMDPointEnd.connect(self.slotProductConnectClicked)
  self._model.tMSonde.tProduct.siCalibrationCMDPointEnd.connect(lambda:self._view.tUILoadingScreen.vFShow("Connection to sonde\nReading configuration"))
  self._model.tMSonde.tProduct.siCalibrationCMDPointEnd.connect(self._view.tVSonde.vFCALIBRATIONMesureStop)
  self._model.tMSonde.tProduct.siCalibrationCMDPointEnd.connect(self._model.tMSonde.vFCALIBSaveTemperatureCalibEnd)

  # Calibration - Erreur calibration
  self._model.tMSonde.siCalibrationCMDPointError.connect(lambda:self._view.tVSonde.vFCALIBRATIONPointNavSelection(TECalibPointNavIndex.MAIN))
  self._model.tMSonde.siCalibrationCMDPointError.connect(self._view.tUIStab.vFClose)
  self._model.tMSonde.siCalibrationCMDPointError.connect(self._view.tUILoadingScreen.vFClose)
  self._model.tMSonde.siCalibrationCMDPointError.connect(lambda sError:self._view.tUIInfo.vFOpen("Calibration error", sError))

  # Stabilisation
  self._model.tMSonde.siCalibrationStabStart.connect(self._view.tUILoadingScreen.vFClose)
  self._model.tMSonde.siCalibrationStabStart.connect(self._view.tUIStab.vFOpen)
  self._model.tMSonde.siCalibrationStabProgress.connect( self._view.tUIStab.vFUpdate )
  self._model.tMSonde.siCalibrationStabStop.connect( self._view.tUIStab.vFClose )
  self._model.tMSonde.siCalibrationStabStop.connect( lambda:self._view.tUILoadingScreen.vFShow("Calibration in progress...") )

  # Point - Sélection EC Cal value
  self._view.ui.comboBox_ECCalValue_Point.currentTextChanged.connect(self._view.tVSonde.vFCALIBRATION_ECCalValueChange)

  # Calibration restauration
  self._view.tVSonde.siCalibrationPointRestore.connect(self.calibrationPointRestore)
  self._view.tVSonde.tUICalibRestore.siWriteData.connect(self._model.tMSonde.slotWriteCalibrationPointRestoreDefault)

  # Erreur général
  self._model.tMSonde.siCalibrationStabilizeError.connect(lambda sTitle, sError:self._view.tUIStab.vFClose())
  self._model.tMSonde.siCalibrationStabilizeError.connect(lambda sTitle, sError:vFAlert(self._view, sTitle, sError))
  self._model.tMSonde.tProduct.siCalibrationStabilizeError.connect(lambda sTitle, sError:self._view.tUIStab.vFClose())
  self._model.tMSonde.tProduct.siCalibrationStabilizeError.connect(lambda sTitle, sError:vFAlert(self._view, sTitle, sError))

  # Calibration - Clear graph
  self._view.ui.clearGraphCal_btn.clicked.connect(self._view.tVSonde.vFCalibrationClearGraphData)

  #----------------
  # Data
  #----------------
  self._view.ui.getMeasureData_btn.clicked.connect(self._model.tMSonde.vFRecordedDataReadStart)
  # Export en CSV
  self._view.ui.exportToCSV_btn.clicked.connect(self.vFDataOpenFileDialogCSV)
  self._view.ui.exportToTAB_btn.clicked.connect(self.vFDataOpenFileDialogTSV)
  self._view.ui.exportToRAW_btn.clicked.connect(self.vFDataOpenFileDialogRAW)
  # Sélection/Déselection de toutes les voies
  self._view.ui.pushButton_dataSelectAll.clicked.connect(lambda:self._view.tVSonde.vDataSelectAllChannel(self._model.tMSonde.tProduct.ttConfig, self._model.tMSonde.tProduct.ttMeasure))
  self._view.ui.pushButton_dataDeselectAll.clicked.connect(lambda:self._view.tVSonde.vDataDeselectAllChannel(self._model.tMSonde.tProduct.ttConfig, self._model.tMSonde.tProduct.ttMeasure))
  # Avancement de la récupération de donnée
  self._model.tMSonde.tProduct.siRecordedDataReadStart.connect(self._view.tUIDataGetWait.vFOpen)
  self._model.tMSonde.tProduct.siRecordedDataReadProgress.connect(self._view.tUIDataGetWait.vFUpdate)
  self._model.tMSonde.siRecordedDataReadEnd.connect(self._view.tUIDataGetWait.vFClose)
  self._model.tMSonde.siRecordedDataReadEnd.connect(lambda:self._view.tVSonde.vFDATADisplayRecordedData(self._model.tMSonde.tProduct.ttConfig, self._model.tMSonde.tProduct.ttMeasure))
  # Relecture de la configuration après lecture recorded data
  # Permet d'éviter le bug sonde mauvaise température
  self._model.tMSonde.siRecordedDataReadEnd.connect(self.slotProductConnectClicked)

  # Erreur général
  self._model.tMSonde.tProduct.siRecordedDataReadError.connect(self._view.tUIDataGetWait.vFClose)
  self._model.tMSonde.tProduct.siRecordedDataReadError.connect(lambda sError:vFAlert(self._view, "Error", sError))

  #----------------
  # PC Config
  #----------------
  # Validation
  self._view.tUIECRefTemp.siWriteData.connect( self.vFPCConfECRefTempChange )
  self._view.tUITempUnit.siWriteData.connect( self.vFPCConfTempUnitChange )
  self._view.tUIDepthUnit.siWriteData.connect( self.vFPCConfDepthUnitChange )
  self._view.tUITDSFactor.siWriteData.connect( self.vFPCConfTDSFactorChange )
  self._view.tUIGraphicalDepth.siWriteData.connect( self._view.tVSonde.vFPCONFChangeGraphicalDepth )
  self._view.tUIDisplayCalculated.siWriteData.connect( self._view.tVSonde.vFPCONFDisplayCalculated )


 #----------------------------------------------
 # Création des signaux connexion - Connexion sonde
 #----------------------------------------------
 @Slot()
 def connectionSondeSelectConnect( self, sCom, tWidget ):
  print("-- connectionSondeSelectConnect --")
  print("sCom = "+sCom)
  # Event
  tWidget.mouseReleaseEvent = lambda event:self.slotConnexionProductConnectClicked(sCom)

 #----------------------------------------------
 # Liveview - Signaux affichage graph
 #----------------------------------------------
 @Slot()
 def vFCMainWindowBoxClickConnect( self, sLabel, tWidget, tWidgetChannelName, uiChannelIndex ):
  print("-- vFCMainWindowBoxClickConnect --")
  print("sLabel = "+sLabel)
  # Event
  tWidget.mouseReleaseEvent = lambda event:self._view.tVSonde.vFMainWindowLiveviewBoxMeasureClick(sLabel, tWidget, tWidgetChannelName, uiChannelIndex)





