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
from Vue.VLib                  import *
from Vue.VMainWindowLib        import TECalibSensorNavIndex, TECalibPointNavIndex
from File.TLiveViewRecordProbe import TLiveViewRecord
from File.TCalibReport         import TCalibReport

#============================================================================#
# Variable
#============================================================================#

#============================================================================#
# Classe
#============================================================================#

#------------------------------------------------------------------------
# Controleur de main Windows
#------------------------------------------------------------------------
class CProbe:
 #----------------------------------------------
 # Init
 #----------------------------------------------
 def __init__( self, view, model, tINIConfig ):
  # Conservation des entrées
  self._model = model
  self._view  = view

  # Création objet écriture CSV
  self.tLiveViewRecord = TLiveViewRecord()
  # Création pour rapport de calibration
  self.tCalibReport = TCalibReport()
  # Enregistrement
  self.bStartRecording = False

  # Init de la configuration avec ini-file
  # Temperature unit
  self._model.tMProbe.tProduct.ttINIConfig["CALCULATED"]["TEMP"]["bF"] = ( tINIConfig.tConfig["MEASURE"]["temperature_unit"] == "F" )
  self._model.tMProbe.tProduct.ttINIConfig["CALCULATED"]["TEMP"]["bC"] = not self._model.tMProbe.tProduct.ttINIConfig["CALCULATED"]["TEMP"]["bF"]
  # Depth unit
  self._model.tMProbe.tProduct.ttINIConfig["CALCULATED"]["DEPTH"]["bM"] = ( tINIConfig.tConfig["MEASURE"]["depth_unit"] == "m" )
  self._model.tMProbe.tProduct.ttINIConfig["CALCULATED"]["DEPTH"]["bF"] = not self._model.tMProbe.tProduct.ttINIConfig["CALCULATED"]["DEPTH"]["bM"]
  # TDS Factor
  self._model.tMProbe.tProduct.ttINIConfig["CALCULATED"]["TDS"]["fFactor"] = float(tINIConfig.tConfig["MEASURE"]["tds_factor"])
  # EC Temperature ref
  self._model.tMProbe.tProduct.ttINIConfig["CALCULATED"]["EC"]["sTSelect"] = tINIConfig.tConfig["MEASURE"]["ec_ref_temp"]

 #----------------------------------------------
 # Click bouton connect product
 #----------------------------------------------
 @Slot()
 def slotConnexionProductConnectClicked( self, sCom ):
  print("-- slotConnexionProductConnectClicked --")
  # Réinit du mode probe
  self._view.tVProbe.vFVProbeInitMode()
  # Réinit configuration
  self._model.tMProbe.tProduct.vFConfigurationInit()
  # Affichage de la fenêtre loading
  self._view.tUILoadingScreen.vFShow("Connection to sonde\nReading configuration")
  # Requête de la configuration du produit
  self._model.tMProbe.tProduct.vFProductGetConfiguration( sCom )

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
  self._model.tMProbe.tProduct.vFProductGetConfiguration( sCOM )
  print("-- slotProductConnectClicked End--")

 #----------------------------------------------
 # Dashboard - Création des signaux dashboard - Channel select
 #----------------------------------------------
 @Slot()
 def dashboardChannelSelectConnect( self, ucChannel, tChannel, tWidget ):
  print("-- dashboardChannelSelectConnect --")
  print("ucChannel = %d"%ucChannel)
  # Event ouverture de la fenêtre
  tWidget.mouseReleaseEvent     = lambda event:self._view.tVProbe.vFDashboardChannelSelectOpen(ucChannel, tChannel, tWidget)

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
  sFileNameDefault += "_" + self._model.tMProbe.tProduct.ttConfig["PRODUCT"]["sModel"].replace("/","")
  sFileNameDefault += "_" + self._model.tMProbe.tProduct.ttConfig["PRODUCT"]["sPSN1"]

  tFileName = QFileDialog.getSaveFileName(self._view, "Recording path", sFileNameDefault, "TAB File (*.tab)")
  print(tFileName)
  print(tFileName[0])
  if( tFileName[0] != "" ):
   # Démarrage de l'enregistrement
   self.bStartRecording = True
   # Modification de la vue
   self._view.tVProbe.vFLiveviewStartRecording()
   self._view.tVProbe.vFCALIBRATIONStartRecording()
   # Création du fichier
   self.tLiveViewRecord.vFCreateNewFileTSV(tFileName[0], self._model.tMProbe.tProduct.ttConfig)
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
  self._view.tVProbe.vFLiveviewStopRecording()
  self._view.tVProbe.vFCALIBRATIONStopRecording()

 #----------------------------------------------
 # Création des signaux calibration - Sensor select
 #----------------------------------------------
 @Slot()
 def calibrationSensorSelectConnect( self, sConfigName, ucChannel, tChannel, tWidget, ttConfig ):
  print("-- calibrationSensorSelectConnect --")
  print("ucChannel = %d"%ucChannel)
  # Event ouverture de la fenêtre
  tWidget.mouseReleaseEvent     = lambda event:self._view.tVProbe.vFCALIBRATIONSensorNavSelectionDynamic(sConfigName, ucChannel, tChannel, tWidget, ttConfig)

 #----------------------------------------------
 # Signal Calibration - Point select - Passage du menu point calibration à la calibration du point
 #----------------------------------------------
 @Slot()
 def calibrationPointSelectConnect( self, sConfigName, ucChannel, tChannel, tWidget, uiPoint, ttConfig ):
  print("-- calibrationPointSelectConnect --")
  print("ucChannel = %d"%ucChannel)
  print("uiPoint   = %d"%uiPoint)
  # Event ouverture de la fenêtre
  tWidget.mouseReleaseEvent = lambda event:self.calibrationPointStartCalibrationPage(sConfigName, ucChannel, tChannel, tWidget, uiPoint, ttConfig)
 #----------------------------------------------
 def calibrationPointStartCalibrationPage( self, sConfigName, ucChannel, tChannel, tWidget, uiPoint, ttConfig ):
  print("-- calibrationPointStartCalibrationPage --")
  print("sConfigName = "+sConfigName)
  print("ucChannel = %d"%ucChannel)
  print("uiPoint = %d"%uiPoint)
  # Test si calibration autorisé pour point demandé
  if( not self._model.tMProbe.bFCalibrationIsCalibrationAllowed( sConfigName, ucChannel, tChannel, uiPoint ) ):
   # On quitte
   return
  # Passage en calibration du point sur la vue
  self._view.tVProbe.vFCALIBRATIONPointNavSelectionDynamic(sConfigName, ucChannel, tChannel, tWidget, uiPoint, ttConfig )

 #----------------------------------------------
 # Restauration point de calibration
 #----------------------------------------------
 @Slot()
 def calibrationPointRestore( self, sConfigName ):
  print("-- calibrationPointRestore --")
  print("sConfigName = "+sConfigName)
  # Event ouverture de la fenêtre
  self._view.ui.pushButton_RestoreDefaultCalibration.mouseReleaseEvent = lambda event:self._view.tVProbe.tUICalibRestore.vFOpen(sConfigName)

 #----------------------------------------------
 # Validation point de calibration
 #----------------------------------------------
 def vFCMWDataEC_TValueUpdate( self, sValue ):
  print("-- vFCMWDataEC_TValueUpdate --")
  #fTDSValue = self._view.ui.doubleSpinBox_TDSValue.value()
  # Mise à jour de la variable TDS Factor
  self._model.tMProbe.tProduct.ttConfig["CALCULATED"]["EC"]["sTSelect"] = sValue
  # Recalcul des voies calculées
  self._view.tVProbe.vFDATAUpdateRecordedData(self._model.tMProbe.tProduct.ttConfig, self._model.tMProbe.tProduct.ttMeasure)

 #----------------------------------------------
 # Ecriture AUX GS Factor
 #----------------------------------------------
 def vFCMWWriteGSFactor( self, fValue ):
  print("-- vFCMWWriteGSFactor --")
  print("fValue = %f"%fValue)
  # Sauvegarde de l'onglet sélectionné
  sConfigName = self._view.tVProbe.tCalibrationCurrentSensor["sConfigName"]
  ucChannel   = self._view.tVProbe.tCalibrationCurrentSensor["ucChannel"]
  tChannel    = self._view.tVProbe.tCalibrationCurrentSensor["tChannel"]
  print("sConfigName = "+sConfigName)
  print("ucChannel = %d"%ucChannel)
  self._model.tMProbe.slotWriteGSFactor( sConfigName, ucChannel, fValue )

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
  # AP-Lite - AUX1 P2
  if(   ( sHiddenChannelName == "AUX1" )
    and ( int(self._model.tMProbe.tProduct.ttConfig["PRODUCT"]["uiModel"]) == 30 ) ):
   # Si Tbd : force la valeur
   if( self._model.tMProbe.tProduct.ttConfig["SENSOR"]["AUX1"]["uiIndex"] == 16 ):
    tCalibConfigObj["uiAUX1P2CalibValue"] = 2570
   # Capteur optique autre que Tbd
   else:
    # AUX
    tCalibConfigObj["uiAUX1P2CalibValue"] = int(self._view.ui.spinBox_ProbeAUXCalValueP2.value())

  #  Appel de la fonction normal
  self._model.tMProbe.slotWriteCalibrationPoint( sHiddenChannelName, int(sHiddenPointNumber), tCalibConfigObj )

 #----------------------------------------------
 # PCConf - Modification EC Ref temperature
 #----------------------------------------------
 def vFPCConfECRefTempChange( self, sValue ):
  print("-- vFPCConfECRefTempChange --")

  print("sValue = "+sValue)
  # Mise à jour de la variable EC Temperature ref
  self._model.tMProbe.tProduct.ttConfig["CALCULATED"]["EC"]["sTSelect"] = sValue
  #
  self._view.vFPCONFChangeECRefTemperature(sValue)

  try:
   # Recalcul des voies calculées
   self._model.tMProbe.tProduct._vFProductUpdateCalculatedParameters()
   # Mise à jour des valeurs affichées
   self._view.tVProbe.vFDATAUpdateRecordedData(self._model.tMProbe.tProduct.ttConfig, self._model.tMProbe.tProduct.ttMeasure)
   # Update affichage des voies
   #self._view.tVProbe.vDataTreeviewHideColumn(self._model.tMProbe.tProduct.ttConfig, self._model.tMProbe.tProduct.ttMeasure)
  except Exception as err:
   print(err)

 #----------------------------------------------
 # PCConf - Modification unité T°/F°
 #----------------------------------------------
 def vFPCConfTempUnitChange( self, sValue ):
  print("-- vFPCConfTempUnitChange --")
  # Fahrenheit
  if( sValue == "F" ):
   self._model.tMProbe.tProduct.ttConfig["CALCULATED"]["TEMP"]["bF"] = True
   self._model.tMProbe.tProduct.ttConfig["CALCULATED"]["TEMP"]["bC"] = False
  else:
   self._model.tMProbe.tProduct.ttConfig["CALCULATED"]["TEMP"]["bF"] = False
   self._model.tMProbe.tProduct.ttConfig["CALCULATED"]["TEMP"]["bC"] = True
  # Modification temperature unit
  self._view.vFPCONFChangeTemperatureUnit( sValue )
  try:
   # Update affichage des voies
   self._view.tVProbe.vDataTreeviewHideColumn(self._model.tMProbe.tProduct.ttConfig, self._model.tMProbe.tProduct.ttMeasure)
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
   self._model.tMProbe.tProduct.ttConfig["CALCULATED"]["DEPTH"]["bF"] = True
   self._model.tMProbe.tProduct.ttConfig["CALCULATED"]["DEPTH"]["bM"] = False
  else:
   self._model.tMProbe.tProduct.ttConfig["CALCULATED"]["DEPTH"]["bF"] = False
   self._model.tMProbe.tProduct.ttConfig["CALCULATED"]["DEPTH"]["bM"] = True
  # Modification temperature unit
  self._view.vFPCONFChangeDepthUnit( sValue )
  try:
   # Update affichage des voies
   self._view.tVProbe.vDataTreeviewHideColumn(self._model.tMProbe.tProduct.ttConfig, self._model.tMProbe.tProduct.ttMeasure)
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
  self._model.tMProbe.tProduct.ttConfig["CALCULATED"]["TDS"]["fFactor"] = fValue
  # Modification temperature unit
  self._view.vFPCONFChangeTDSFactor( fValue )
  try:
   # Recalcul des voies calculées
   self._model.tMProbe.tProduct._vFProductUpdateCalculatedParameters()
   # Mise à jour des valeurs affichées
   self._view.tVProbe.vFDATAUpdateRecordedData(self._model.tMProbe.tProduct.ttConfig, self._model.tMProbe.tProduct.ttMeasure)
   # Update affichage des voies
   #self._view.tVProbe.vDataTreeviewHideColumn(self._model.tMProbe.tProduct.ttConfig, self._model.tMProbe.tProduct.ttMeasure)
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
  sFileNameDefault += "_" + self._model.tMProbe.tProduct.ttConfig["PRODUCT"]["sModel"].replace("/","")
  sFileNameDefault += "_" + self._model.tMProbe.tProduct.ttConfig["PRODUCT"]["sPSN1"]+"_Calibration_Certificate"

  tFileName = QFileDialog.getSaveFileName(self._view, "Recording path", sFileNameDefault, "TXT File (*.txt)")
  print(tFileName)
  print(tFileName[0])
  if( tFileName[0] != "" ):
   self.tCalibReport.vFCreateNewFile(self._model.tMProbe.tProduct.ttConfig, tFileName[0])

 #----------------------------------------------
 # Connexion des signaux pour une sonde
 #----------------------------------------------
 def connectSignals( self ):
  print("-- CProbe > connectSignals --")

  #---------------
  # Detect/Connect
  #---------------
  # Détection produit probe
  self._view.ui.pushButton_detectProbe.clicked.connect(lambda:self._view.tUILoadingScreen.vFShow("Products detection"))
  self._view.ui.pushButton_detectProbe.clicked.connect(self._model.tMProbe.tProduct.vFSondeList)
  # Fin détection produit probe
  self._model.tMProbe.tProduct.siDetectProductEnd.connect(self._view.vFDisplayProbeDetected)
  self._model.tMProbe.tProduct.siDetectProductEnd.connect(self._view.tUILoadingScreen.vFClose)

  # Connexion - Signal connexion probe
  self._view.xConnectionProbeSelectConnectSignal.connect(self.connectionSondeSelectConnect)

  self._model.tMProbe.tProduct.siConfigurationReadEnd.connect(self.connectSignalsPostInit)
  self._model.tMProbe.tProduct.siConfigurationReadEnd.connect(self._view.tVProbe.vFDisplayGeneralConfiguration)
  self._model.tMProbe.tProduct.siConfigurationReadEnd.connect(self._view.tVProbe.vFDisplayProductNav)
  self._model.tMProbe.tProduct.siConfigurationReadEnd.connect(self._view.tUILoadingScreen.vFClose)
  #----------------
  # Connect
  #----------------
  self._view.ui.pushButton_detectProbe.clicked.connect( self._view.tVProbe.vFVProbeInitMode )
  self._view.ui.pushButton_detectProbe.clicked.connect( self._view.tVProbe.vFDisplayProductNavInit )
  # Erreur général
  self._model.tMProbe.tProduct.siError.connect(self._view.tUILoadingScreen.vFClose)
  self._model.tMProbe.tProduct.siError.connect(lambda sError:vFAlert(self._view, "Error", sError))
  self._model.tMProbe.siErrorMsg.connect(self._view.tUILoadingScreen.vFClose)
  self._model.tMProbe.siErrorMsg.connect(lambda sTitle, sMsg:vFAlert(self._view, sTitle, sMsg))


 #----------------------------------------------
 # Connexion des signaux pour une sonde
 #----------------------------------------------
 def connectSignalsPostInit( self ):
  print("-- CSonde > connectSignalsPostInit --")

  # Suppression du signal
  self._model.tMProbe.tProduct.siConfigurationReadEnd.disconnect(self.connectSignalsPostInit)
  #---------------
  # Général
  #---------------
  # Gestion du menu nav AS
  self._view.ui.connexion_btn.clicked.connect(lambda:self._view.tVProbe.vFNavASBtnClicked(0))
  self._view.ui.dashboard_btn.clicked.connect(lambda:self._view.tVProbe.vFNavASBtnClicked(1))
  self._view.ui.liveview_btn.clicked.connect(lambda:self._view.tVProbe.vFNavASBtnClicked(2))
  self._view.ui.data_btn.clicked.connect(lambda:self._view.tVProbe.vFNavASBtnClicked(3))
  self._view.ui.calibration_btn.clicked.connect(lambda:self._view.tVProbe.vFNavASBtnClicked(4))
  self._view.ui.about_btn.clicked.connect(lambda:self._view.tVProbe.vFNavASBtnClicked(5))
  self._view.ui.pcConfig_btn.clicked.connect(lambda:self._view.tVProbe.vFNavASBtnClicked(6))

  #----------------
  # Sur ouverture fenêtre
  #----------------
  self._view.tUIInfo.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tUIStab.siOpen.connect( lambda:self._view.tUIBackground.vFOpen( self._view.size() ) )
  self._view.tUIGSFactor.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tUIDataGetWait.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVProbe.tUIClearSondeMemory.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVProbe.tUINewBatteriesFitted.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVProbe.tUIUpdateClockWithPC.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVProbe.tUISondeDate.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVProbe.tUISondeTime.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVProbe.tUISiteID.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVProbe.tUISiteLatitude.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVProbe.tUISiteLongitude.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVProbe.tUIChannelSelect.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVProbe.tUILogDataEvery.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVProbe.tUICleanEvery.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVProbe.tUISetupLoggingState.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVProbe.tUISetupLoggingCheck.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVProbe.tUISetupLoggingEvery.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVProbe.tUISetupLoggingThreshold.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVProbe.tUIOpticalAvg.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVProbe.tUIProbeSetBaro.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVProbe.tUICalibRestore.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))

  #----------------
  # Sur fermeture fenêtre
  #----------------
  self._view.tUIInfo.siClose.connect( self._view.tUIBackground.close )
  self._view.tUIStab.siClose.connect(self._view.tUIBackground.close)
  self._view.tUIGSFactor.siClose.connect(self._view.tUIBackground.close)
  self._view.tUIDataGetWait.siClose.connect(self._view.tUIBackground.close)
  self._view.tVProbe.tUIClearSondeMemory.siClose.connect(self._view.tUIBackground.close)
  self._view.tVProbe.tUINewBatteriesFitted.siClose.connect(self._view.tUIBackground.close)
  self._view.tVProbe.tUIUpdateClockWithPC.siClose.connect(self._view.tUIBackground.close)
  self._view.tVProbe.tUISondeDate.siClose.connect(self._view.tUIBackground.close)
  self._view.tVProbe.tUISondeTime.siClose.connect(self._view.tUIBackground.close)
  self._view.tVProbe.tUISiteID.siClose.connect(self._view.tUIBackground.close)
  self._view.tVProbe.tUISiteLatitude.siClose.connect(self._view.tUIBackground.close)
  self._view.tVProbe.tUISiteLongitude.siClose.connect(self._view.tUIBackground.close)
  self._view.tVProbe.tUIChannelSelect.siClose.connect(self._view.tUIBackground.close)
  self._view.tVProbe.tUILogDataEvery.siClose.connect(self._view.tUIBackground.close)
  self._view.tVProbe.tUICleanEvery.siClose.connect(self._view.tUIBackground.close)
  self._view.tVProbe.tUISetupLoggingState.siClose.connect(self._view.tUIBackground.close)
  self._view.tVProbe.tUISetupLoggingCheck.siClose.connect(self._view.tUIBackground.close)
  self._view.tVProbe.tUISetupLoggingEvery.siClose.connect(self._view.tUIBackground.close)
  self._view.tVProbe.tUISetupLoggingThreshold.siClose.connect(self._view.tUIBackground.close)
  self._view.tVProbe.tUIOpticalAvg.siClose.connect(self._view.tUIBackground.close)
  self._view.tVProbe.tUIProbeSetBaro.siClose.connect(self._view.tUIBackground.close)
  self._view.tVProbe.tUICalibRestore.siClose.connect(self._view.tUIBackground.close)

  #----------------
  # Dashboard
  #----------------
  # - Ouverture fenêtre - Modification paramètre
  self._view.ui.clearSondeMem_btn.clicked.connect( self._view.tVProbe.tUIClearSondeMemory.vFOpen )
  self._view.ui.newBatteryFitted_btn.clicked.connect( self._view.tVProbe.tUINewBatteriesFitted.vFOpen )
  self._view.ui.resyncClockWithPC_btn.clicked.connect( self._view.tVProbe.tUIUpdateClockWithPC.vFOpen )
  self._view.ui.widget_SondeDate.mouseReleaseEvent          = self._view.tVProbe.vFDashboardSondeDateOpen
  self._view.ui.widget_SondeTime.mouseReleaseEvent          = self._view.tVProbe.vFDashboardSondeTimeOpen
  self._view.ui.widget_SiteID.mouseReleaseEvent             = self._view.tVProbe.vFDashboardSiteIDOpen
  self._view.ui.widget_SiteLatitude.mouseReleaseEvent       = self._view.tVProbe.vFDashboardSiteLatitudeOpen
  self._view.ui.widget_SiteLongitude.mouseReleaseEvent      = self._view.tVProbe.vFDashboardSiteLongitudeOpen
  self._view.ui.widget_LogDataEvery.mouseReleaseEvent       = self._view.tVProbe.vFDashboardLogDataEveryOpen
  self._view.ui.widget_CleanEvery.mouseReleaseEvent         = self._view.tVProbe.vFDashboardCleanEveryOpen
  self._view.ui.widget_EventLogState.mouseReleaseEvent      = self._view.tVProbe.vFDashboardSetupLoggingStateOpen
  self._view.ui.widget_EventLogCheck.mouseReleaseEvent      = self._view.tVProbe.vFDashboardSetupLoggingCheckOpen
  self._view.ui.widget_EventLogEvery.mouseReleaseEvent      = self._view.tVProbe.vFDashboardSetupLoggingEveryOpen
  self._view.ui.widget_EventLogThreshold.mouseReleaseEvent  = self._view.tVProbe.vFDashboardSetupLoggingThresholdOpen
  self._view.ui.widget_OpticalAveraging.mouseReleaseEvent   = self._view.tVProbe.vFDashboardOpticalAveragingOpen

  # Dynamique channel display/selection
  self._view.tVProbe.xDashboardChannelSelectConnectSignal.connect(self.dashboardChannelSelectConnect)

  #----------------
  # Dasboard - Validation écriture de donnée
  #----------------
  self._view.tVProbe.tUISondeDate.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVProbe.tUISondeTime.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVProbe.tUISiteID.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVProbe.tUISiteLatitude.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVProbe.tUISiteLongitude.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVProbe.tUILogDataEvery.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVProbe.tUICleanEvery.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVProbe.tUISetupLoggingState.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVProbe.tUISetupLoggingCheck.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVProbe.tUISetupLoggingEvery.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVProbe.tUISetupLoggingThreshold.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVProbe.tUIOpticalAvg.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  ##self._view.tVProbe.tUIProbeSetBaro.siWriteData.siWriteData(self._model.tMProbe.slotWriteBaroValue)
  # Fenêtre écriture Aux assignement
  self._view.tVProbe.tUIChannelSelect.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  # Calibration
  self._view.tVProbe.tUICalibRestore.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))

  #------------------------
  # -- Dashboard Windows --
  #------------------------
  # Clear memory
  self._view.tVProbe.tUIClearSondeMemory.siAccept.connect(self._model.tMProbe.vFModelClearMemoryCMD)
  self._view.tVProbe.tUIClearSondeMemory.siAccept.connect(lambda:self._view.tUILoadingScreen.vFShow("Clearing memory..."))
   # New batteries fitted
  self._view.tVProbe.tUINewBatteriesFitted.siAccept.connect(self._model.tMProbe.siNewBatteriesFittedStart)
  self._view.tVProbe.tUINewBatteriesFitted.siAccept.connect(lambda:self._view.tUILoadingScreen.vFShow("New batteries fitted \ntaking into account"))
  # Modification paramètre - Validation écriture
  self._view.tVProbe.tUIOpticalAvg.siWriteData.connect(self._model.tMProbe.slotWriteOpticalAverage)
  self._view.tVProbe.tUIProbeSetBaro.siWriteData.connect(self._model.tMProbe.slotWriteBaroValue)
  # Fenêtre écriture Aux assignement
  self._view.tVProbe.tUIChannelSelect.siWriteData.connect(self._model.tMProbe.slotWriteAUXChannelSelect)
  # Fin d'écriture
  self._model.tMProbe.tProduct.siConfigSiteWriteEnd.connect(self.slotProductConnectClicked)
  self._model.tMProbe.tProduct.siUserSettingsWriteEnd.connect(self.slotProductConnectClicked)
  self._model.tMProbe.tProduct.siDateTimeSondeWriteEnd.connect(self.slotProductConnectClicked)
  self._model.tMProbe.tProduct.siAUXAssignementWriteEnd.connect(self.slotProductConnectClicked)

  #----------------
  # Liveview
  #----------------
  # Démarrage mesure
  self._view.ui.startMeasure_btn.clicked.connect(self._model.tMProbe.vFMeasureDataReadStart)
  self._view.ui.startMeasure_btn.clicked.connect(self._view.tVProbe.vFStartMeasureData)
  # Stop mesure
  self._view.ui.stopMeasure_btn.clicked.connect(self._model.tMProbe.vFMeasureDataReadStop)
  self._view.ui.stopMeasure_btn.clicked.connect(self._view.tVProbe.vFStopMeasureData)
  # Effacement graph
  self._view.ui.clearMeasure_btn.clicked.connect(self._view.tVProbe.vFClearMeasureData)
  # Affichage résultat
  self._model.tMProbe.siMeasureDataReadEnd.connect(self._view.tVProbe.vFDisplayMeasureData)
  self._model.tMProbe.siMeasureDataReadEnd.connect(self.vFLiveviewRecordingNewSample)
  # Liveview - Sur click box mesure
  self._view.tVProbe.siLiveviewClickBox.connect( self.vFCMainWindowBoxClickConnect )
  # Liveview - Enregistrement Liveview
  self._view.ui.pushButton_LiveViewRecord.clicked.connect( self.vFLiveviewOpenFileDialog )
  self._view.ui.pushButton_LiveViewRecordStop.clicked.connect( self.vFLiveviewStopRecording )
  # Liveview - Ouverture de la fenêtre de modification du baro
  self._view.ui.pushButton_LiveviewSetBaro.clicked.connect( lambda:self._view.tVProbe.tUIProbeSetBaro.vFOpen( int(self._model.tMProbe.tProduct.ttConfig["SENSOR"]["Baro"]["fResult"]) ) )

  #----------------
  # Calibration
  #----------------
  # Balai
  self._view.ui.cleanSonde_btn.clicked.connect(self._model.tMProbe.tProduct._vFProductWiperStart)
  self._view.ui.cleanSonde_btn.clicked.connect(lambda:self._view.tUILoadingScreen.vFShow("Cleaning..."))
  self._model.tMProbe.tProduct.siWiperStartEnd.connect(self._view.tUILoadingScreen.vFClose)
  self._model.tMProbe.tProduct.siWiperStartEnd.connect(lambda:self._view.tUIInfo.vFOpen("Wiper", "Cleaning success"))
  # Texte calibration report Export
  self._view.ui.exportToTxt_btn.clicked.connect(self.vFCALIBReportSaveDialog)
  # Dynamique capteur nav
  self._view.tVProbe.xCalibrationSensorSelectConnectSignal.connect(self.calibrationSensorSelectConnect)

  # Dynamique passage au menu point de calibration
  self._view.tVProbe.siCalibrationPointSelectConnectSignal.connect(self.calibrationPointSelectConnect)
  # Annulation point de calibration
  self._view.ui.pushButton_calibrateCancel.clicked.connect(lambda:self._view.tVProbe.vFCALIBRATIONPointNavSelection(TECalibPointNavIndex.MAIN))
  # Démarrage mesure
  self._view.tVProbe.xCalibrationPointPageDisplayedSignal.connect(self._model.tMProbe.vFMeasureDataReadStart)
  # Stop mesure
  self._view.ui.pushButton_calibrateCancel.clicked.connect(self._model.tMProbe.vFMeasureDataReadStop)
  # GS factor
  self._view.ui.widget_AuxGSFactor.mouseReleaseEvent = lambda event:self._view.tUIGSFactor.vFOpen( float(self._view.ui.label_AuxGSFactor.text()) )
  self._view.tUIGSFactor.siWriteData.connect( lambda:self._view.tUILoadingScreen.vFShow("Configuration writing...") )
  self._view.tUIGSFactor.siWriteData.connect( self.vFCMWWriteGSFactor )
  # Liveview - Enregistrement Liveview
  self._view.tVProbe.xCalibrationPointPageDisplayedSignal.connect( self._view.tVProbe.vFCALIBRATIONMesureStart )
  self._view.ui.pushButton_calibrateCancel.clicked.connect( self.vFLiveviewStopRecording )
  self._view.ui.pushButton_CalibRecord.clicked.connect( self.vFLiveviewOpenFileDialog )
  self._view.ui.pushButton_CalibRecordStop.clicked.connect( self.vFLiveviewStopRecording )
  self._model.tMProbe.tProduct.siCalibrationCMDPointEnd.connect(self.vFLiveviewStopRecording)
  self._model.tMProbe.siCalibrationCMDPointError.connect(self.vFLiveviewStopRecording)

  # Validation calibration
  self._view.ui.pushButton_calibrateAndExit.clicked.connect(self.vFCMWCalibrationValidatePoint)
  # Validation rapidCal btn
  self._view.ui.rapidCal_btn.clicked.connect(self._model.tMProbe.slotWriteCalibrationPointRapidCal)
  # Calibration - Fin de validation point
  self._model.tMProbe.tProduct.siCalibrationCMDPointEnd.connect(lambda:self._view.tVProbe.vFCALIBRATIONPointNavSelection(TECalibPointNavIndex.MAIN))
  self._model.tMProbe.tProduct.siCalibrationCMDPointEnd.connect(self.slotProductConnectClicked)
  self._model.tMProbe.tProduct.siCalibrationCMDPointEnd.connect(lambda:self._view.tUILoadingScreen.vFShow("Connection to sonde\nReading configuration"))
  self._model.tMProbe.tProduct.siCalibrationCMDPointEnd.connect(self._view.tVProbe.vFCALIBRATIONMesureStop)
  self._model.tMProbe.tProduct.siCalibrationCMDPointEnd.connect(self._model.tMProbe.vFCALIBSaveTemperatureCalibEnd)
  # Calibration - Fin de restauration de point
  self._model.tMProbe.tProduct.siCalibrationCMDRestorePointEnd.connect(self.slotProductConnectClicked)
  self._model.tMProbe.tProduct.siCalibrationCMDRestorePointEnd.connect(lambda:self._view.tUILoadingScreen.vFShow("Connection to sonde\nReading configuration"))

  # Calibration - Erreur calibration
  self._model.tMProbe.siCalibrationCMDPointError.connect(lambda:self._view.tVProbe.vFCALIBRATIONPointNavSelection(TECalibPointNavIndex.MAIN))
  self._model.tMProbe.siCalibrationCMDPointError.connect(self._view.tUIStab.vFClose)
  self._model.tMProbe.siCalibrationCMDPointError.connect(self._view.tUILoadingScreen.vFClose)
  self._model.tMProbe.siCalibrationCMDPointError.connect(lambda sError:self._view.tUIInfo.vFOpen("Calibration error", sError))

  # Stabilisation
  self._model.tMProbe.siCalibrationStabStart.connect(self._view.tUILoadingScreen.vFClose)
  self._model.tMProbe.siCalibrationStabStart.connect(self._view.tUIStab.vFOpen)
  self._model.tMProbe.siCalibrationStabProgress.connect( self._view.tUIStab.vFUpdate )
  self._model.tMProbe.siCalibrationStabStop.connect( self._view.tUIStab.vFClose )
  self._model.tMProbe.siCalibrationStabStop.connect( lambda:self._view.tUILoadingScreen.vFShow("Calibration in progress...") )

  # Point - Sélection EC Cal value
  self._view.ui.comboBox_ECCalValue_Point.currentTextChanged.connect(self._view.tVProbe.vFCALIBRATION_ECCalValueChange)

  # Calibration restauration
  self._view.tVProbe.siCalibrationPointRestore.connect(self.calibrationPointRestore)
  self._view.tVProbe.tUICalibRestore.siWriteData.connect(self._model.tMProbe.slotWriteCalibrationPointRestoreDefault)

  # Erreur général
  self._model.tMProbe.siCalibrationStabilizeError.connect(lambda sTitle, sError:self._view.tUIStab.vFClose())
  self._model.tMProbe.siCalibrationStabilizeError.connect(lambda sTitle, sError:vFAlert(self._view, sTitle, sError))
  self._model.tMProbe.tProduct.siCalibrationStabilizeError.connect(lambda sTitle, sError:self._view.tUIStab.vFClose())
  self._model.tMProbe.tProduct.siCalibrationStabilizeError.connect(lambda sTitle, sError:vFAlert(self._view, sTitle, sError))

  # Calibration - Ouverture de la fenêtre de modification du baro
  self._view.ui.setBaroCal_btn.clicked.connect( lambda:self._view.tVProbe.tUIProbeSetBaro.vFOpen(int(self._model.tMProbe.tProduct.ttConfig["SENSOR"]["Baro"]["fResult"])) )

  # Calibration - Clear graph
  self._view.ui.clearGraphCal_btn.clicked.connect(self._view.tVProbe.vFCalibrationClearGraphData)

  #----------------
  # PC Config
  #----------------
  # Validation
  self._view.tUIECRefTemp.siWriteData.connect( self.vFPCConfECRefTempChange )
  self._view.tUITempUnit.siWriteData.connect( self.vFPCConfTempUnitChange )
  self._view.tUIDepthUnit.siWriteData.connect( self.vFPCConfDepthUnitChange )
  self._view.tUITDSFactor.siWriteData.connect( self.vFPCConfTDSFactorChange )
  self._view.tUIGraphicalDepth.siWriteData.connect( self._view.tVProbe.vFPCONFChangeGraphicalDepth )
  self._view.tUIDisplayCalculated.siWriteData.connect( self._view.tVProbe.vFPCONFDisplayCalculated )

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
  tWidget.mouseReleaseEvent = lambda event:self._view.tVProbe.vFMainWindowLiveviewBoxMeasureClick(sLabel, tWidget, tWidgetChannelName, uiChannelIndex)





