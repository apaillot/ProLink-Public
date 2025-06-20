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
from Vue.VLib                     import *
from Vue.VMainWindowLib           import TECalibSensorNavIndex, TECalibPointNavIndex
from File.TFileRecord             import TFileRecord
from File.TLiveViewRecordLeveLine import TLiveViewRecord
from File.TCalibReport            import TCalibReport
from File.TSondeRawFile           import TSondeRawFile

#============================================================================#
# Variable
#============================================================================#

#============================================================================#
# Classe
#============================================================================#

#------------------------------------------------------------------------
# Controleur de main Windows
#------------------------------------------------------------------------
class CLeveLine:
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
  # Init variable
  self.bStartRecording = False


  # Init de la configuration avec ini-file
  # Temperature unit
  self._model.tMLeveLine.tProduct.ttConfig["CALCULATED"]["TEMP"]["bF"] = ( tINIConfig.tConfig["MEASURE"]["temperature_unit"] == "F" )
  self._model.tMLeveLine.tProduct.ttConfig["CALCULATED"]["TEMP"]["bC"] = not self._model.tMLeveLine.tProduct.ttConfig["CALCULATED"]["TEMP"]["bF"]
  # Depth unit
  self._model.tMLeveLine.tProduct.ttConfig["CALCULATED"]["DEPTH"]["bM"] = ( tINIConfig.tConfig["MEASURE"]["depth_unit"] == "m" )
  self._model.tMLeveLine.tProduct.ttConfig["CALCULATED"]["DEPTH"]["bF"] = not self._model.tMLeveLine.tProduct.ttConfig["CALCULATED"]["DEPTH"]["bM"]
  # TDS Factor
  #self._model.tMLeveLine.tProduct.ttConfig["CALCULATED"]["TDS"]["fFactor"] = float(tINIConfig.tConfig["MEASURE"]["tds_factor"])
  # EC Temperature ref
  self._model.tMLeveLine.tProduct.ttConfig["CALCULATED"]["EC"]["sTSelect"] = tINIConfig.tConfig["MEASURE"]["ec_ref_temp"]

 #----------------------------------------------
 # Click bouton connect product
 #----------------------------------------------
 @Slot()
 def slotConnexionProductConnectClicked( self, sCom ):
  print("-- slotConnexionProductConnectClicked --")
  # Réinit du mode Sonde
  self._view.tVLeveLine.vFLeveLineInitMode()
  # Requête de la configuration du produit
  self._model.tMLeveLine.tProduct.vFProductGetConfiguration( sCom )
  # Affichage de la fenêtre loading
  self._view.tUILoadingScreen.vFShow("Connection to LeveLine\nReading configuration")

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
  sFileNameDefault += "_" + self._model.tMLeveLine.tProduct.ttConfig["PRODUCT"]["sSiteID"]

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
   self.tLiveViewRecord.vFCreateNewFileTSV(tFileName[0], self._model.tMLeveLine.tProduct.ttConfig)
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
 # Click bouton connect product
 #----------------------------------------------
 '''
 @Slot()
 def slotProductConnectClicked( self ):
  print("-- slotConnexionProductConnectClicked --")
  # Réinit du mode Sonde
  self._view.tVLeveLine.vFLeveLineInitMode()
  # Requête de la configuration du produit
  self._model.tMLeveLine.tProduct.vFProductGetConfiguration( sCom )
  # Affichage de la fenêtre loading
  self._view.tUILoadingScreen.vFShow("Connection to LeveLine\nReading configuration")
 '''

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
  #print("tsCalibPointName[1] = "+tsCalibPointName[1])
  print("sHiddenPointNumber  = "+sHiddenPointNumber)

  # Ouverture fenêtre d'attente
  self._view.tUILoadingScreen.vFShow("Writing to sonde...")

  tCalibConfigObj = {}
  if( sHiddenChannelName == "EC" ):
   sECCalValue      = self._view.ui.comboBox_ECCalValue_Point.currentText()
   uiECCalUserValue = int(self._view.ui.spinBox_ECCalValue_2_Point.text())
   tCalibConfigObj["sECCalValue"]      = sECCalValue
   tCalibConfigObj["uiECCalUserValue"] = uiECCalUserValue
   print('tCalibConfigObj["sECCalValue"]='+tCalibConfigObj["sECCalValue"])
   print('tCalibConfigObj["sECCalValue"]='+tCalibConfigObj["sECCalValue"])

  #  Appel de la fonction normal
  self._model.tMLeveLine.tProduct.bFProductCalibrateECEnd()

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


 #----------------------------------------------
 # Connexion des signaux pour une sonde
 #----------------------------------------------
 def connectSignals( self ):
  print("-- CLeveLine > connectSignals --")

  #---------------
  # Detect/Connect
  #---------------
  # Détection produit sonde
  self._view.ui.pushButton_detectLeveLine.clicked.connect(lambda:self._view.tUILoadingScreen.vFShow("Products detection"))
  self._view.ui.pushButton_detectLeveLine.clicked.connect(self._model.tMLeveLine.tProduct.vFSondeList)
  # Fin détection produit sonde
  self._model.tMLeveLine.tProduct.siDetectProductEnd.connect(self._view.vFDisplayLeveLineDetected)
  self._model.tMLeveLine.tProduct.siDetectProductEnd.connect(self._view.tUILoadingScreen.vFClose)
  # Détection produit LeveLine
  #self._view.ui.pushButton_detectLeveLine.clicked.connect( self.vFSondeList )
  # Fin de détection produit LeveLine
  #self._model. connect( self._view.vFDisplayLeveLineDetected )

  # Connexion - Signal connexion sonde
  self._view.xConnectionLeveLineSelectConnectSignal.connect(self.connectionLeveLineSelectConnect)

  self._model.tMLeveLine.tProduct.siConfigurationReadEnd.connect(self.connectSignalsPostInit)
  self._model.tMLeveLine.tProduct.siConfigurationReadEnd.connect(self._view.tVLeveLine.vFDisplayGeneralConfiguration)
  self._model.tMLeveLine.tProduct.siConfigurationReadEnd.connect(lambda:self._view.tVLeveLine.vFDisplayProductNav(self._model.tMLeveLine.tProduct.ttConfig))
  self._model.tMLeveLine.tProduct.siConfigurationReadEnd.connect(self._view.tUILoadingScreen.vFClose)

  # Erreur
  self._model.tMLeveLine.tProduct.siError.connect(self._view.tUILoadingScreen.vFClose)
  self._model.tMLeveLine.tProduct.siError.connect(lambda sMsg:self._view.tUIInfo.vFOpen("Error", sMsg))

 #----------------------------------------------
 # Connexion des signaux pour une sonde
 #----------------------------------------------
 def connectSignalsPostInit( self ):
  print("-- CSonde > connectSignalsPostInit --")

  # Suppression du signal
  self._model.tMLeveLine.tProduct.siConfigurationReadEnd.disconnect(self.connectSignalsPostInit)

  #---------------
  # Général
  #---------------
  # Gestion du menu nav AS
  self._view.ui.connexion_btn.clicked.connect(lambda:self._view.tVLeveLine.vFNavASBtnClicked(0))
  self._view.ui.dashboard_btn.clicked.connect(lambda:self._view.tVLeveLine.vFNavASBtnClicked(7))
  self._view.ui.liveview_btn.clicked.connect(lambda:self._view.tVLeveLine.vFNavASBtnClicked(2))
  self._view.ui.data_btn.clicked.connect(lambda:self._view.tVLeveLine.vFNavASBtnClicked(3))
  self._view.ui.calibration_btn.clicked.connect(lambda:self._view.tVLeveLine.vFNavASBtnClicked(4))
  self._view.ui.about_btn.clicked.connect(lambda:self._view.tVLeveLine.vFNavASBtnClicked(5))
  self._view.ui.pcConfig_btn.clicked.connect(lambda:self._view.tVLeveLine.vFNavASBtnClicked(6))

  #----------------
  # Sur ouverture fenêtre
  #----------------
  self._view.tVLeveLine.tUIClearSondeMemory.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVLeveLine.tUIResetLeveLine.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVLeveLine.tUIUpdateClockWithPC.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVLeveLine.tUISondeDate.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVLeveLine.tUISondeTime.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVLeveLine.tUISiteID.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVLeveLine.tUISiteLatitude.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVLeveLine.tUISiteLongitude.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVLeveLine.tUISiteAltitude.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVLeveLine.tUIStartProduct.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVLeveLine.tUILogDataEvery.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVLeveLine.tUILogDataFor.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVLeveLine.tUISetupLoggingState.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVLeveLine.tUISetupLoggingEvery.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVLeveLine.tUIEventLoggingLevel.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVLeveLine.tUIEventLoggingTemperature.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tVLeveLine.tUIEventLoggingSalinity.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))

  #----------------
  # Sur fermeture fenêtre
  #----------------
  self._view.tVLeveLine.tUIClearSondeMemory.siClose.connect(self._view.tUIBackground.close)
  self._view.tVLeveLine.tUIResetLeveLine.siClose.connect(self._view.tUIBackground.close)
  self._view.tVLeveLine.tUIUpdateClockWithPC.siClose.connect(self._view.tUIBackground.close)
  self._view.tVLeveLine.tUISondeDate.siClose.connect(self._view.tUIBackground.close)
  self._view.tVLeveLine.tUISondeTime.siClose.connect(self._view.tUIBackground.close)
  self._view.tVLeveLine.tUISiteID.siClose.connect(self._view.tUIBackground.close)
  self._view.tVLeveLine.tUISiteLatitude.siClose.connect(self._view.tUIBackground.close)
  self._view.tVLeveLine.tUISiteLongitude.siClose.connect(self._view.tUIBackground.close)
  self._view.tVLeveLine.tUISiteAltitude.siClose.connect(self._view.tUIBackground.close)
  self._view.tVLeveLine.tUIStartProduct.siClose.connect(self._view.tUIBackground.close)
  self._view.tVLeveLine.tUILogDataEvery.siClose.connect(self._view.tUIBackground.close)
  self._view.tVLeveLine.tUILogDataFor.siClose.connect(self._view.tUIBackground.close)
  self._view.tVLeveLine.tUISetupLoggingState.siClose.connect(self._view.tUIBackground.close)
  self._view.tVLeveLine.tUISetupLoggingEvery.siClose.connect(self._view.tUIBackground.close)
  self._view.tVLeveLine.tUIEventLoggingLevel.siClose.connect(self._view.tUIBackground.close)
  self._view.tVLeveLine.tUIEventLoggingTemperature.siClose.connect(self._view.tUIBackground.close)
  self._view.tVLeveLine.tUIEventLoggingSalinity.siClose.connect(self._view.tUIBackground.close)

  #----------------
  # Dashboard
  #----------------
  self._view.ui.clearSondeMem_btn_2.clicked.connect( self._view.tVLeveLine.tUIClearSondeMemory.vFOpen )
  self._view.ui.resetLeveLine_btn_2.clicked.connect( self._view.tVLeveLine.tUIResetLeveLine.vFOpen )
  self._view.ui.resyncClockWithPC_btn_2.clicked.connect( self._view.tVLeveLine.tUIUpdateClockWithPC.vFOpen )

  self._view.ui.startProductLeveLine_btn.clicked.connect(self._view.tVLeveLine.vFDashboardStartProductOpen)
  self._view.ui.widget_BatteryRemaining_2.mouseReleaseEvent = lambda event:self._view.tUIBatteryRemaining.vFOpen()
  # - Ouverture fenêtre - Modification paramètre
  self._view.ui.widget_SondeDate_5.mouseReleaseEvent      = self._view.tVLeveLine.vFDashboardSondeDateOpen
  self._view.ui.widget_SondeTime_2.mouseReleaseEvent      = self._view.tVLeveLine.vFDashboardSondeTimeOpen
  self._view.ui.widget_SiteID_2.mouseReleaseEvent         = self._view.tVLeveLine.vFDashboardSiteIDOpen
  self._view.ui.widget_SiteLatitude_2.mouseReleaseEvent   = self._view.tVLeveLine.vFDashboardSiteLatitudeOpen
  self._view.ui.widget_SiteLongitude_2.mouseReleaseEvent  = self._view.tVLeveLine.vFDashboardSiteLongitudeOpen
  self._view.ui.widget_SiteAltitude.mouseReleaseEvent     = self._view.tVLeveLine.vFDashboardSiteAltitudeOpen
  # self._view.ui.widget_LogStartMode.mouseReleaseEvent     = self._view.tVLeveLine.vFDashboardStartProductOpen
  self._view.ui.widget_LogDataEvery_2.mouseReleaseEvent   = self._view.tVLeveLine.vFDashboardLogDataEveryOpen
  self._view.ui.widget_LogDataFor.mouseReleaseEvent       = self._view.tVLeveLine.vFDashboardLogDataForOpen
  self._view.ui.widget_EventLogState_2.mouseReleaseEvent          = self._view.tVLeveLine.vFDashboardSetupLoggingStateOpen
  self._view.ui.widget_EventLogEvery_2.mouseReleaseEvent          = self._view.tVLeveLine.vFDashboardSetupLoggingEveryOpen
  self._view.ui.widget_EventLogLevelValue.mouseReleaseEvent       = self._view.tVLeveLine.vFDashboardEventLoggingLevelOpen
  self._view.ui.widget_EventLogTemperatureValue.mouseReleaseEvent = self._view.tVLeveLine.vFDashboardSetupLoggingTemperatureOpen
  self._view.ui.widget_EventLogSalinityValue.mouseReleaseEvent    = self._view.tVLeveLine.vFDashboardSetupLoggingSalinityOpen

  #----------------
  # Dasboard - Validation écriture de donnée
  #----------------
  self._view.tVLeveLine.tUISondeDate.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVLeveLine.tUISondeTime.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVLeveLine.tUISiteID.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVLeveLine.tUISiteLatitude.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVLeveLine.tUISiteLongitude.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVLeveLine.tUISiteAltitude.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVLeveLine.tUILogDataEvery.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  #self._view.tVLeveLine.tUICleanEvery.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVLeveLine.tUISetupLoggingState.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  #self._view.tVLeveLine.tUISetupLoggingCheck.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  self._view.tVLeveLine.tUISetupLoggingEvery.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  ##self._view.tVLeveLine.tUISetupLoggingThreshold.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  # Fenêtre écriture Aux assignement
  #self._view.tVLeveLine.tUIChannelSelect.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))
  # Calibration
  #self._view.tVLeveLine.tUICalibRestore.siWriteData.connect(lambda:self._view.tUILoadingScreen.vFShow("Writing configuration..."))

  #------------------------
  # -- Dashboard Windows --
  #------------------------
  # Clear memory
  self._view.tVLeveLine.tUIClearSondeMemory.siAccept.connect(self._model.tMLeveLine.tProduct.bFProductClearMemory)
  self._view.tVLeveLine.tUIClearSondeMemory.siAccept.connect(lambda:self._view.tUILoadingScreen.vFShow("Clearing memory..."))
   # New batteries fitted
  self._view.tVLeveLine.tUIResetLeveLine.siAccept.connect(self._model.tMLeveLine.tProduct.bFProductResetLeveLine)
  self._view.tVLeveLine.tUIResetLeveLine.siAccept.connect(lambda:self._view.tUILoadingScreen.vFShow("Resetting LeveLine..."))
  # Update clock with PC
  self._view.tVLeveLine.tUIUpdateClockWithPC.siAccept.connect(self._model.tMLeveLine.slotWriteSondeDateTimePC)
  self._view.tVLeveLine.tUIUpdateClockWithPC.siAccept.connect(lambda:self._view.tUILoadingScreen.vFShow("Updating clock..."))
  # Modification paramètre - Validation écriture
  self._view.tVLeveLine.tUISondeDate.siWriteData.connect(self._model.tMLeveLine.slotWriteSondeDate)
  self._view.tVLeveLine.tUISondeTime.siWriteData.connect(self._model.tMLeveLine.slotWriteSondeTime)
  self._view.tVLeveLine.tUISiteID.siWriteData.connect(self._model.tMLeveLine.slotWriteSiteID)
  self._view.tVLeveLine.tUISiteLatitude.siWriteData.connect(self._model.tMLeveLine.slotWriteSiteLatitude)
  self._view.tVLeveLine.tUISiteLongitude.siWriteData.connect(self._model.tMLeveLine.slotWriteSiteLongitude)
  self._view.tVLeveLine.tUISiteAltitude.siWriteData.connect(self._model.tMLeveLine.slotWriteSiteAltitude)
  self._view.tVLeveLine.tUILogDataEvery.siWriteData.connect(self._model.tMLeveLine.slotWriteLogDataEvery)

  self._view.tVLeveLine.tUILogDataFor.siWriteData.connect(self._model.tMLeveLine.slotWriteLogDataFor)

  self._view.tVLeveLine.tUISetupLoggingState.siWriteData.connect(self._model.tMLeveLine.slotWriteEventLogCheckState)
  self._view.tVLeveLine.tUISetupLoggingEvery.siWriteData.connect(self._model.tMLeveLine.slotWriteEventLogCheckPeriod)

  self._view.tVLeveLine.tUIEventLoggingLevel.siWriteData.connect(self._model.tMLeveLine.slotWriteEventLogPressure)
  self._view.tVLeveLine.tUIEventLoggingTemperature.siWriteData.connect(self._model.tMLeveLine.slotWriteEventLogTemperature)
  self._view.tVLeveLine.tUIEventLoggingSalinity.siWriteData.connect(self._model.tMLeveLine.slotWriteEventLogSalinity)

  self._view.tVLeveLine.tUIStartProduct.siWriteData.connect(self._model.tMLeveLine.slotWriteProductStartDate)

  ##self._view.tVLeveLine.tUISetupLoggingThreshold.siWriteData.connect(self._model.tMLeveLine.slotWriteLogEventThreshold)
  # Fenêtre écriture Aux assignement
  ##self._view.tVLeveLine.tUIChannelSelect.siWriteData.connect(self._model.tMLeveLine.slotWriteAUXChannelSelect)
  # Fin d'écriture
  """
  self._model.tMLeveLine.siClearMemoryEndSuccess.connect(self.slotProductConnectClicked)
  self._model.tMLeveLine.siNewBatteriesFittedEndSuccess.connect(self.slotProductConnectClicked)
  self._model.tMLeveLine.siConfigSiteWriteEnd.connect(self.slotProductConnectClicked)
  self._model.tMLeveLine.siAUXAssignementWriteEnd.connect(self.slotProductConnectClicked)
  """
  self._model.tMLeveLine.tProduct.siClearMemoryEnd.connect(lambda:self.slotConnexionProductConnectClicked(self._view.ui.label_InterfaceCom_2.text()))
  self._model.tMLeveLine.tProduct.siResetLeveLineEnd.connect(lambda:self.slotConnexionProductConnectClicked(self._view.ui.label_InterfaceCom_2.text()))
  self._model.tMLeveLine.tProduct.siDateTimeSondeWriteEnd.connect(lambda:self.slotConnexionProductConnectClicked(self._view.ui.label_InterfaceCom_2.text()))
  self._model.tMLeveLine.tProduct.siSiteIDWriteEnd.connect(lambda:self.slotConnexionProductConnectClicked(self._view.ui.label_InterfaceCom_2.text()))
  self._model.tMLeveLine.tProduct.siPositionWriteEnd.connect(lambda:self.slotConnexionProductConnectClicked(self._view.ui.label_InterfaceCom_2.text()))
  self._model.tMLeveLine.tProduct.siLogIntervalWriteEnd.connect(lambda:self.slotConnexionProductConnectClicked(self._view.ui.label_InterfaceCom_2.text()))
  self._model.tMLeveLine.tProduct.siLogDataForWriteEnd.connect(lambda:self.slotConnexionProductConnectClicked(self._view.ui.label_InterfaceCom_2.text()))
  self._model.tMLeveLine.tProduct.siEventLogCheckPeriodWriteEnd.connect(lambda:self.slotConnexionProductConnectClicked(self._view.ui.label_InterfaceCom_2.text()))
  self._model.tMLeveLine.tProduct.siEventLogCheckLimitWriteEnd.connect(lambda:self.slotConnexionProductConnectClicked(self._view.ui.label_InterfaceCom_2.text()))

  #----------------
  # Liveview
  #----------------
  # Démarrage mesure
  self._view.ui.startMeasure_btn.clicked.connect(self._model.tMLeveLine.vFMeasureDataReadStart)
  self._view.ui.startMeasure_btn.clicked.connect(self._view.tVLeveLine.vFStartMeasureData)
  # Stop mesure
  self._view.ui.stopMeasure_btn.clicked.connect(self._model.tMLeveLine.vFMeasureDataReadStop)
  self._view.ui.stopMeasure_btn.clicked.connect(self._view.tVLeveLine.vFStopMeasureData)
  # Effacement graph
  self._view.ui.clearMeasure_btn.clicked.connect(self._view.tVLeveLine.vFClearMeasureData)
  # Affichage résultat
  self._model.tMLeveLine.siMeasureDataReadEnd.connect(self._view.tVLeveLine.vFDisplayMeasureData)
  self._model.tMLeveLine.siMeasureDataReadEnd.connect(self.vFLiveviewRecordingNewSample)
  # Liveview - Sur click box mesure
  self._view.tVLeveLine.siLiveviewClickBox.connect( self.vFCMainWindowBoxClickConnect )
  # Liveview - Enregistrement Liveview
  self._view.ui.pushButton_LiveViewRecord.clicked.connect( self.vFLiveviewOpenFileDialog )
  self._view.ui.pushButton_LiveViewRecordStop.clicked.connect( self.vFLiveviewStopRecording )

  #----------------
  # Calibration
  #----------------
  # Dynamique passage au menu point de calibration
  self._view.tVLeveLine.siCalibrationPointSelectConnectSignal.connect(self.calibrationPointSelectConnect)
  # Annulation point de calibration
  self._view.ui.pushButton_calibrateCancel.clicked.connect(lambda:self._view.tVLeveLine.vFCALIBRATIONPointNavSelection(TECalibPointNavIndex.MAIN))
  # Démarrage mesure
  self._view.tVLeveLine.xCalibrationPointPageDisplayedSignal.connect(self._model.tMLeveLine.vFMeasureDataReadStart)
  # Stop mesure
  self._view.ui.pushButton_calibrateCancel.clicked.connect(self._model.tMLeveLine.vFMeasureDataReadStop)
  # Liveview - Enregistrement Liveview
  self._view.tVLeveLine.xCalibrationPointPageDisplayedSignal.connect( self._view.tVLeveLine.vFCALIBRATIONMesureStart )
  self._view.ui.pushButton_calibrateCancel.clicked.connect( self.vFLiveviewStopRecording )
  self._view.ui.pushButton_CalibRecord.clicked.connect( self.vFLiveviewOpenFileDialog )
  self._view.ui.pushButton_CalibRecordStop.clicked.connect( self.vFLiveviewStopRecording )
  self._model.tMLeveLine.tProduct.siCalibrationCMDPointEnd.connect(self.vFLiveviewStopRecording)
  self._model.tMLeveLine.siCalibrationCMDPointError.connect(self.vFLiveviewStopRecording)

  # Validation calibration
  self._view.ui.pushButton_calibrateAndExit.clicked.connect(self.vFCMWCalibrationValidatePoint)
  # Calibration - Fin de validation point
  self._model.tMLeveLine.tProduct.siCalibrationCMDPointEnd.connect(lambda:self._view.tVLeveLine.vFCALIBRATIONPointNavSelection(TECalibPointNavIndex.MAIN))
  ##self._model.tMLeveLine.tProduct.siCalibrationCMDPointEnd.connect(self.slotProductConnectClicked)
  self._model.tMLeveLine.tProduct.siCalibrationCMDPointEnd.connect(lambda:self.slotConnexionProductConnectClicked(self._view.ui.label_InterfaceCom_2.text()))
  self._model.tMLeveLine.tProduct.siCalibrationCMDPointEnd.connect(lambda:self._view.tUILoadingScreen.vFShow("Connection to sonde\nReading configuration"))
  self._model.tMLeveLine.tProduct.siCalibrationCMDPointEnd.connect(self._view.tVLeveLine.vFCALIBRATIONMesureStop)
  self._model.tMLeveLine.tProduct.siCalibrationCMDPointEnd.connect(self._model.tMLeveLine.vFCALIBSaveTemperatureCalibEnd)

  # Calibration - Erreur calibration
  self._model.tMLeveLine.siCalibrationCMDPointError.connect(lambda:self._view.tVLeveLine.vFCALIBRATIONPointNavSelection(TECalibPointNavIndex.MAIN))
  self._model.tMLeveLine.siCalibrationCMDPointError.connect(self._view.tUIStab.vFClose)
  self._model.tMLeveLine.siCalibrationCMDPointError.connect(self._view.tUILoadingScreen.vFClose)
  self._model.tMLeveLine.siCalibrationCMDPointError.connect(lambda sError:self._view.tUIInfo.vFOpen("Calibration error", sError))

  # Stabilisation
  ##self._model.tMLeveLine.siCalibrationStabStart.connect(self._view.tUILoadingScreen.vFClose)
  ##self._model.tMLeveLine.siCalibrationStabStart.connect(self._view.tUIStab.vFOpen)
  ##self._model.tMLeveLine.siCalibrationStabProgress.connect( self._view.tUIStab.vFUpdate )
  ##self._model.tMLeveLine.siCalibrationStabStop.connect( self._view.tUIStab.vFClose )
  ##self._model.tMLeveLine.siCalibrationStabStop.connect( lambda:self._view.tUILoadingScreen.vFShow("Calibration in progress...") )

  # Point - Sélection EC Cal value
  self._view.ui.comboBox_ECCalValue_Point.currentTextChanged.connect(self._view.tVLeveLine.vFCALIBRATION_ECCalValueChange)

  # Calibration restauration
  #self._view.tVLeveLine.siCalibrationPointRestore.connect(self.calibrationPointRestore)
  #self._view.tVLeveLine.tUICalibRestore.siWriteData.connect(self._model.tMLeveLine.slotWriteCalibrationPointRestoreDefault)

  # Erreur général
  ##self._model.tMLeveLine.siCalibrationStabilizeError.connect(lambda sTitle, sError:self._view.tUIStab.vFClose())
  ##self._model.tMLeveLine.siCalibrationStabilizeError.connect(lambda sTitle, sError:vFAlert(self._view, sTitle, sError))
  ##self._model.tMLeveLine.tProduct.siCalibrationStabilizeError.connect(lambda sTitle, sError:self._view.tUIStab.vFClose())
  ##self._model.tMLeveLine.tProduct.siCalibrationStabilizeError.connect(lambda sTitle, sError:vFAlert(self._view, sTitle, sError))

 #----------------------------------------------
 # Création des signaux connexion - Connexion sonde
 #----------------------------------------------
 @Slot()
 def connectionLeveLineSelectConnect( self, sCom, tWidget ):
  print("-- connectionLeveLineSelectConnect --")
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
  tWidget.mouseReleaseEvent = lambda event:self._view.tVLeveLine.vFMainWindowLiveviewBoxMeasureClick(sLabel, tWidget, tWidgetChannelName, uiChannelIndex)

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
  # Passage en calibration du point sur la vue
  self._view.tVLeveLine.vFCALIBRATIONPointNavSelectionDynamic(sConfigName, ucChannel, tChannel, tWidget, uiPoint)
