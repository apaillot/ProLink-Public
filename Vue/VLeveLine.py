# This Python file uses the following encoding: utf-8

#============================================================================#
# Librairies système
#============================================================================#
import sys, datetime

#============================================================================#
# Librairies Qt
#============================================================================#
from PySide6.QtCore import QUrl, Signal, Slot, Qt, QTimer, QObject, QDateTime
from PySide6.QtWidgets import ( QListWidgetItem, QWidget, QLabel, QTreeWidgetItem,
                                QHBoxLayout, QVBoxLayout, QGraphicsDropShadowEffect,
                                QHeaderView, QAbstractItemView )
from PySide6.QtWidgets import *
from PySide6.QtGui     import QPixmap, QColor, QPainter, QPen
from PySide6.QtCharts  import QChart, QChartView, QLineSeries

#============================================================================#
# Librairies Utilisateur
#============================================================================#
from Vue.VChart         import VChart, tSensorColor
from Vue.VMainWindowLib import *
from Vue.py_toggle      import PyToggle
# Sonde
from Vue.Windows.Dashboard.UIClearSondeMemory      import UIClearSondeMemory
from Vue.Windows.Dashboard.UIResetLeveLine         import UIResetLeveLine
from Vue.Windows.Dashboard.UIUpdateClockWithPC     import UIUpdateClockWithPC
from Vue.Windows.Dashboard.UISondeDate             import UISondeDate
from Vue.Windows.Dashboard.UISondeTime             import UISondeTime
from Vue.Windows.Dashboard.UISiteID                import UISiteID
from Vue.Windows.Dashboard.UISiteLatitude          import UISiteLatitude
from Vue.Windows.Dashboard.UISiteLongitude         import UISiteLongitude
from Vue.Windows.Dashboard.UISiteAltitude          import UISiteAltitude
from Vue.Windows.Dashboard.UIStartProduct          import UIStartProduct
from Vue.Windows.Dashboard.UILogDataEveryLeveLine      import UILogDataEvery
from Vue.Windows.Dashboard.UILogDataFor                import UILogDataFor
from Vue.Windows.Dashboard.UISetupLoggingState         import UISetupLoggingState
from Vue.Windows.Dashboard.UISetupLoggingEveryLeveLine import UISetupLoggingEvery
from Vue.Windows.Dashboard.UIEventLoggingLevel         import UIEventLoggingLevel
from Vue.Windows.Dashboard.UIEventLoggingTemperature   import UIEventLoggingTemperature
from Vue.Windows.Dashboard.UIEventLoggingSalinity      import UIEventLoggingSalinity

#============================================================================#
# Constante
#============================================================================#

#============================================================================#
# Variable
#============================================================================#

#============================================================================#
# Classe
#============================================================================#

#------------------------------------------------------------------------
# Main Windows
#------------------------------------------------------------------------
class VLeveLine(QObject):
 #-- Liveview - Click sur bouton mesure
 siLiveviewClickBox = Signal(str, QWidget, QWidget, int)
 #-- Calibration
 # Signal de fin d'init de la vignette
 xCalibrationSensorSelectConnectSignal = Signal( str, int, dict, QWidget )
 # Signal pour sélection point calibration
 siCalibrationPointSelectConnectSignal  = Signal( str, int, dict, QWidget, int )
 # Signal fin d'affichage page point calibration
 xCalibrationPointPageDisplayedSignal  = Signal()
 # Signal restauration point de calibration
 siCalibrationPointRestore             = Signal( str )

 #----------------------------------------------
 # Init
 #----------------------------------------------
 def __init__(self, tParent, tINIFile, tUI):
  super().__init__(tParent)
  #super().__init__(self)
  print("VLeveLine init")
  # Conservation INIFile
  self.tINIConfig = tINIFile.tConfig
  self.tINIFile   = tINIFile
  #
  self.ui = tUI
  # Fenêtre parent
  self.tParent = tParent

  #-- Calibration
  # Calibration - Variable de l'onglet capteur courant
  self.tCalibrationCurrentSensor = {}

  # -- Création fenêtre --
  # - Dashboard -
  self.tUIClearSondeMemory        = UIClearSondeMemory( tParent )
  self.tUIResetLeveLine           = UIResetLeveLine( tParent )
  self.tUIUpdateClockWithPC       = UIUpdateClockWithPC( tParent )
  self.tUISondeDate               = UISondeDate( tParent )
  self.tUISondeTime               = UISondeTime( tParent )
  self.tUISiteID                  = UISiteID( tParent )
  self.tUISiteLatitude            = UISiteLatitude( tParent )
  self.tUISiteLongitude           = UISiteLongitude( tParent )
  self.tUISiteAltitude            = UISiteAltitude( tParent )
  self.tUIStartProduct            = UIStartProduct( tParent )
  self.tUILogDataEvery            = UILogDataEvery( tParent )
  self.tUILogDataFor              = UILogDataFor( tParent )
  self.tUISetupLoggingState       = UISetupLoggingState( tParent )
  self.tUISetupLoggingEvery       = UISetupLoggingEvery( tParent )
  self.tUIEventLoggingLevel       = UIEventLoggingLevel( tParent )
  self.tUIEventLoggingTemperature = UIEventLoggingTemperature( tParent )
  self.tUIEventLoggingSalinity    = UIEventLoggingSalinity( tParent )

  # Timer pour bouton clignotte enregistrement liveview
  self.timerLVRecording  = QTimer(self)
  self.timerLVRecording.timeout.connect( self.vFLiveviewRecordingOccuringTimeout )
  self.timerCALRecording = QTimer(self)
  self.timerCALRecording.timeout.connect( self.vFCALIBRATIONRecordingOccuringTimeout )

 #----------------------------------------------
 # Affichage des onglets
 #----------------------------------------------
 def vFDisplayProductNav( self, ttConfig ):
  #self.ui.connexion_btn.setVisible(False)
  self.ui.dashboard_btn.setVisible(True)
  self.ui.liveview_btn.setVisible(True)
  self.ui.data_btn.setVisible(True)
  # Si EC
  if( ttConfig["PRODUCT"]["bECSensor"] ): self.ui.calibration_btn.setVisible(True)
  else                                  : self.ui.calibration_btn.setVisible(False)
  self.ui.pcConfig_btn.setVisible(True)

 #----------------------------------------------
 # NAV - Gestion menu bouton nav
 #----------------------------------------------
 def vFNavASBtnClicked( self, uiIndex ):
  print("-- VLeveLine > vFNavASBtnClicked --")
  tBtnNav = [
   self.ui.connexion_btn,
   None,
   self.ui.liveview_btn,
   self.ui.data_btn,
   self.ui.calibration_btn,
   self.ui.about_btn,
   self.ui.pcConfig_btn,
   self.ui.dashboard_btn
  ]
  # Modification page affichée
  self.ui.stackedWidget.setCurrentIndex(uiIndex)
  self.ui.stackedWidget_Nav2.setCurrentIndex(uiIndex)
  # Gestion de la ligne blanche gauche du bouton nav active
  for uiCpt in range(len(tBtnNav)):
   if( tBtnNav[uiCpt] == None ): continue
   print("uiCpt   = %d"%uiCpt)
   print("uiIndex = %d"%uiIndex)
   if( uiCpt == uiIndex ):
    tBtnNav[uiCpt].setStyleSheet("background-color: #3E4072;border-left: 3px solid rgb(255,255,255);");
   else:
    tBtnNav[uiCpt].setStyleSheet("");
  # Conservation de l'onglet actif
  self.uiNavActivePage = uiIndex

 #----------------------------------------------
 # Init du mode lecture sonde
 #----------------------------------------------
 def vFLeveLineInitMode( self ):
  # Cache
  self.ui.widget_SondeInfoInterface_2.setVisible(False)
  self.ui.groupBox_DashboardSensors_2.setVisible(False)
  self.ui.widget_LogStartMode.setVisible(False)
  self.ui.rapidCal_btn.setVisible(False)
  self.ui.cleanSonde_btn.setVisible(False)
  # Affichage spécifique sonde
  #self.ui.widget_SondeInfoInterface.setVisible(True)
  #self.ui.groupBox_EstimatedLogLife.setVisible(True)
  #self.ui.groupBox_SondeClock.setVisible(True)
  #self.ui.groupBox_Averaging.setVisible(True)
  #self.ui.widget_DashboardNavBtn.setVisible(True)
  #self.ui.getMeasureData_btn.setVisible(True)
  # Data
  self.ui.exportToRAW_btn.setVisible(True)
  # Conf box
  self.ui.groupBox_PCConf_AppSettings.setVisible(True)
  self.ui.groupBox_PCConf_Measure.setVisible(True)
  # Dashboard - Couleur au survol des lignes modifiables
  self.ui.widget_BatteryRemaining_2.setStyleSheet("#widget_BatteryRemaining_2:hover{background-color: #efefef;}")
  self.ui.groupBox_SondeClock_2.setStyleSheet("#groupBox_SondeClock_2 > QWidget:hover{background-color: #efefef;}")
  self.ui.groupBox_SiteIDLocation_2.setStyleSheet("#groupBox_SiteIDLocation_2 > QWidget:hover{background-color: #efefef;}")
  self.ui.widget_LogStartMode.setStyleSheet("#widget_LogStartMode:hover{background-color: #efefef;}")
  self.ui.groupBox_SetupLogRate_2.setStyleSheet("#groupBox_SetupLogRate_2 > QWidget:hover{background-color: #efefef;}")

  self.ui.widget_EventLogState_2.setStyleSheet("#widget_EventLogState_2:hover{background-color: #efefef;}")
  self.ui.widget_EventLogEvery_2.setStyleSheet("#widget_EventLogEvery_2:hover{background-color: #efefef;}")
  self.ui.widget_EventLogLevelValue.setStyleSheet("#widget_EventLogLevelValue:hover{background-color: #efefef;}")
  self.ui.widget_EventLogTemperatureValue.setStyleSheet("#widget_EventLogTemperatureValue:hover{background-color: #efefef;}")
  self.ui.widget_EventLogSalinityValue.setStyleSheet("#widget_EventLogSalinityValue:hover{background-color: #efefef;}")
  # Dashboard - Modification du logo modification
  #self.ui.label_setSiteID.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version.svg") )
  #self.ui.label_setSiteLatitude.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version.svg") )
  #self.ui.label_setSiteLong.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version.svg") )
  #self.ui.label_setLogDataEvery.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version.svg") )
  #self.ui.label_setCleanEvery.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version.svg") )
  #self.ui.label_setEventLogState.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version.svg") )
  # Data - Clear du treeview
  self.ui.treeWidget.clear()
  self.vFTreeviewRemoveItem( self.ui.treeWidget )
  # Data - Clear du graphique
  self.vFClearLayout( self.ui.widget_DataChart.layout() )

 #----------------------------------------------
 # Affichage configuration
 #----------------------------------------------
 def vFDisplayGeneralConfiguration( self, ttConfig, sCom ):
  print("-- vFSONDEDisplayGeneralConfiguration --")

  #-----------------
  # Dashboard
  #-----------------
  # Sonde info
  self.ui.label_Model_2.setText( str(ttConfig["PRODUCT"]["bFGetProductName"](ttConfig)) + "\n("+ttConfig["PRODUCT"]["sSensorTypeFormat"]+")" )
  self.ui.label_SerialNo_2.setText( str(ttConfig["PRODUCT"]["sSerialNumber"]) )
  self.ui.label_InterfaceCom_2.setText( str(sCom) )
  self.ui.label_SWRev_2.setText( str(ttConfig["PRODUCT"]["sFirmwareVersion"]) )
  self.ui.label_DepthRating.setText( str( ttConfig["PRODUCT"]["sDepthRating"] ) )
  self.ui.label_RecordsStored_2.setText( str(ttConfig["PRODUCT"]["uiLogCount"]) )
  self.ui.label_MemoryRemaining_2.setText( str(ttConfig["PRODUCT"]["uiLogFree"]) )
  self.ui.label_BatteryRemaining_2.setText( ("%.1f"%ttConfig["PRODUCT"]["fBatteryLife"])+" %" )
  #self.ui.label_BatteryVoltage_2.setText( str("%.2f"%ttConfig["PRODUCT"]["fBATT"])+" V" )
  #-- Sonde clock
  self.ui.label_sondeClockDate_2.setText( str(ttConfig["PRODUCT"]["sRTCDate"]) )
  self.ui.label_sondeClockTime_2.setText( str(ttConfig["PRODUCT"]["sRTCTime"]) )
  #-- Site ID and location
  self.ui.label_SiteID_2.setText( str(ttConfig["PRODUCT"]["sSiteID"]) )
  self.ui.label_SiteLat_2.setText( str(ttConfig["PRODUCT"]["sLatitude"]) )
  self.ui.label_SiteLong_2.setText( str(ttConfig["PRODUCT"]["sLongitude"]) )
  self.ui.label_SiteAltitude.setText( str(ttConfig["PRODUCT"]["iAltitude"])+" m" )

  #-- Measurement status
  if( ttConfig["PRODUCT"]["bLogging"] ):
   self.ui.label_MeasStatusState.setText( "Logging" )
  else:
   if( ttConfig["PRODUCT"]["bScheduled"] ):
    self.ui.label_MeasStatusState.setText("Scheduled")
   else:
    self.ui.label_MeasStatusState.setText("Stopped")

  #-- Setup logging rate
  sLogDataRate = ("%u"%ttConfig["PRODUCT"]["uiLogIntervalHour"]) + "h" + ("%u"%ttConfig["PRODUCT"]["uiLogIntervalMin"]) + "m" + ("%.1f"%ttConfig["PRODUCT"]["fLogIntervalSec"])
  self.ui.label_LogDataEvery_2.setText(sLogDataRate)

  #-- Log data for
  # Log data activé
  if( ttConfig["PRODUCT"]["uiLogDuration"] != 0 ):
   self.ui.label_LogDataFor.setText( str( ttConfig["PRODUCT"]["uiLogDuration"] )+" h" )
   self.ui.widget_LogEndDateTime.setVisible(True)
  # Log data désactivé
  else:
   self.ui.label_LogDataFor.setText( "0 h (not limited)" )
   self.ui.widget_LogEndDateTime.setVisible(False)

  if( ttConfig["PRODUCT"]["bScheduled"] ):
   self.ui.label_LogStartMode.setText("Scheduled Start")
  else:
   self.ui.label_LogStartMode.setText("Manual deployement")
  self.ui.widget_LogDataStartAt.setVisible(ttConfig["PRODUCT"]["bScheduled"])
  self.ui.label_LogStartAt.setText(ttConfig["PRODUCT"]["sLogStartDate"])

  # Calcul de la date d'arrêt de mesure
  if(   ( ttConfig["PRODUCT"]["uiLogDuration"] != 0 )
    and ttConfig["PRODUCT"]["bScheduled"] ):
   uiLogDuration = ttConfig["PRODUCT"]["uiLogDuration"]
   tLogStartDate = ttConfig["PRODUCT"]["tLogStartDate"]
   # Calcul de la date de fin
   tLogStartDateEnd = tLogStartDate + datetime.timedelta(seconds=uiLogDuration*3600)
   # Affichage de la date de fin de mesure
   self.ui.label_LogEndDateTime.setText(tLogStartDateEnd.strftime("%d/%m/%Y %H:%M:%S"))
   self.ui.widget_LogEndDateTime.setVisible(True)
  else:
   self.ui.widget_LogEndDateTime.setVisible(False)

  #self.label_LogDataFor.setText()

  #-- Event log
  if( ttConfig["PRODUCT"]["uiEventInterval"] != 0 ):
   self.ui.label_EventLogState_2.setText( "Enable" )
   self.ui.label_logoEventLogEvery_2.setPixmap( QPixmap(":/Logo/Dashboard/7-Event-logging/3-Every.svg") )
   self.ui.label_txtEventLogEvery_2.setStyleSheet("color: #000000;")
   self.ui.label_EventLogEvery_2.setStyleSheet("color: rgb(84,84,84);")
   self.ui.label_setEventLogEvery_2.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version.svg") )
   #self.ui.label_logoEventLogThreshold_2.setPixmap( QPixmap(":/Logo/Dashboard/7-Event-logging/4-Log-data-if.svg") )
   #self.ui.label_txtEventLogThreshold_2.setStyleSheet("color: #000000;")
   #self.ui.label_EventLogThreshold_2.setStyleSheet("color: rgb(84,84,84);")
   #self.ui.label_setEventLogThreshold_2.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version.svg") )
  else:
   self.ui.label_EventLogState_2.setText( "Disable" )
   self.ui.label_logoEventLogEvery_2.setPixmap( QPixmap(":/Logo/Dashboard/7-Event-logging/3-Every-grey.svg") )
   self.ui.label_txtEventLogEvery_2.setStyleSheet("color: #888888;")
   self.ui.label_EventLogEvery_2.setStyleSheet("color: #888888;")
   self.ui.label_setEventLogEvery_2.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version-grey.svg") )
   #self.ui.label_logoEventLogThreshold_2.setPixmap( QPixmap(":/Logo/Dashboard/7-Event-logging/4-Log-data-if-grey.svg") )
   #self.ui.label_txtEventLogThreshold_2.setStyleSheet("color: #888888;")
   #self.ui.label_EventLogThreshold_2.setStyleSheet("color: #888888;")
   #self.ui.label_setEventLogThreshold_2.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version-grey.svg") )
  # Log
  #self.ui.label_EventLogCheck.setText( str(ttConfig["PRODUCT"]["sLOG_SENSOR"]) )


  self.ui.label_EventLogEvery_2.setText( str(ttConfig["PRODUCT"]["uiEventHour"])+"h"+str(ttConfig["PRODUCT"]["uiEventMin"])+"m"+("%.1f"%ttConfig["PRODUCT"]["fEventSec"])+"s" )
  #self.ui.label_EventLogThreshold_2.setText( str(ttConfig["PRODUCT"]["uiEVENT_CHANGE"])+" %" )

  # Event log value
  #self.ui.label_EventLogLevelValue.setText()
  #self.ui.label_EventLogTemperatureValue.setText()
  #self.ui.label_EventLogSalinityValue.setText()

  # Si Event log actif
  if( ttConfig["PRODUCT"]["bEventLog"] ):
   self.ui.widget_EventLogLimitTxt.setVisible(True)
   self.ui.widget_EventLogLevelValue.setVisible(True)
   self.ui.widget_EventLogEvery_2.setVisible(True)
   # Event pression niveau
   if( ttConfig["PRODUCT"]["uiPressureLimit"] != 0 ):
    self.ui.label_EventLogLevelValue.setText( ("%.3f"%ttConfig["PRODUCT"]["fPressureLimit"] )+" m" )
   else:
    self.ui.label_EventLogLevelValue.setText( "Disable" )
   # Si capteur CTD
   if( ttConfig["PRODUCT"]["bECSensor"] ):
    # Event log sur salinité
    self.ui.widget_EventLogTemperatureValue.setVisible(False)
    self.ui.widget_EventLogSalinityValue.setVisible(True)
    # Event pression niveau
    if( ttConfig["PRODUCT"]["uiSalinityLimit"] != 0 ):
     self.ui.label_EventLogSalinityValue.setText( (("%.1f"%ttConfig["PRODUCT"]["fSalinityLimit"] )+" PSU" ) )
    else:
     self.ui.label_EventLogSalinityValue.setText( "Disable" )
   # Sinon Event log sur temperature
   else:
    # Event log sur temperature
    self.ui.widget_EventLogTemperatureValue.setVisible(True)
    self.ui.widget_EventLogSalinityValue.setVisible(False)
    # Event pression niveau
    if( ttConfig["PRODUCT"]["uiTempLimit"] != 0 ):
     self.ui.label_EventLogTemperatureValue.setText( (("%.1f"%ttConfig["PRODUCT"]["fTempLimit"] )+" °C" ) )
    else:
     self.ui.label_EventLogTemperatureValue.setText( "Disable" )
  # Event log inactif
  else:
   self.ui.widget_EventLogEvery_2.setVisible(False)
   self.ui.widget_EventLogLimitTxt.setVisible(False)
   self.ui.widget_EventLogLevelValue.setVisible(False)
   self.ui.widget_EventLogTemperatureValue.setVisible(False)
   self.ui.widget_EventLogSalinityValue.setVisible(False)

  # Clear du layout dashboard sensor list
  for i in reversed(range(self.ui.groupBox_DashboardSensors_2.layout().count())):
   self.ui.groupBox_DashboardSensors_2.layout().itemAt(i).widget().deleteLater()
  # Pression
  self.vFDashboardAddPressureLine()
  # Temperature
  self.vFDashboardAddTemperatureLine()
  # Si capteur CTD
  if( ttConfig["PRODUCT"]["bECSensor"] ):
   # Conductivity
   self.vFDashboardAddConductivityLine()

  #-----------------
  # Liveview
  #-----------------
  # Liste des capteurs
  if( ttConfig["PRODUCT"]["bECSensor"] ):
   tListSensor = ["TEMP", "DEPTH", "EC"]
  else:
   tListSensor = ["TEMP", "DEPTH"]
  self.tListSensor = tListSensor
  # Nettoyage zone vignette valeur physique
  for i in reversed(range(self.ui.widget_11.layout().count())):
   self.ui.widget_11.layout().itemAt(i).widget().deleteLater()
  # On compte le nombre d'item
  ucItemNb = 0
  for ucCpt in range( len( tListSensor ) ):
   sIndex = tListSensor[ucCpt]
   print("sIndex = "+sIndex)
   if( ttConfig["SENSOR"][sIndex]["sIndex"] == "EMPTY" ): continue
   ucItemNb = ucItemNb + 1
  # Création des items
  ucCptItem = 0
  # Réinit de l'objet
  self.tMeasureBox = []
  # On boucle
  for ucCpt in range( len( tListSensor ) ):
   print(tListSensor[ucCpt])
   sIndex = tListSensor[ucCpt]
   if( ttConfig["SENSOR"][sIndex]["sIndex"] == "EMPTY" ): continue
   """
   self.vFLiveviewDisplayBloc( ttConfig["SENSOR"][sIndex],
                               ( ucCptItem % int( int( ucItemNb / 2 ) + 1 ) ),
                               ( ucCptItem / int( int( ucItemNb / 2 ) + 1 ) ),
                               ucCptItem )
   """
   self.vFLiveviewDisplayBloc( ttConfig["SENSOR"][sIndex],
                               ucCptItem,
                               0,
                               ucCptItem )
   ucCptItem = ucCptItem + 1
  # Correction unité
  # Liveview - Modification unité Temp bloc
  if( ttConfig["CALCULATED"]["TEMP"]["bF"] ):
   self.tMeasureBox[0]["tLabelUnit"].setText("(degF)")
  else:
   self.tMeasureBox[0]["tLabelUnit"].setText("(degC)")
  # Liveview - Modification unité Depth bloc
  if( ttConfig["CALCULATED"]["DEPTH"]["bF"]  ):
   self.tMeasureBox[1]["tLabelUnit"].setText("(f)")
  else:
   self.tMeasureBox[1]["tLabelUnit"].setText("(m)")

  #-------------------------------------------
  # Liveview - Chart multigraph
  #-------------------------------------------
  # Chart
  print(list(ttConfig["SENSOR"]))
  print(len(list(ttConfig["SENSOR"])))

  # Nombre de voie
  ucChannelNb = 0
  for ucChannelCpt in range( len(tListSensor) ):
   sIndex = tListSensor[ucChannelCpt]
   if(ttConfig["SENSOR"][sIndex]["sIndex"] == "EMPTY"): continue
   ucChannelNb = ucChannelNb + 1
  # Init du graphique
  self.chart = VChart(ucChannelNb)
  self.chart.setContentsMargins(-10, -30, -10, -10)
  self.chart.vFSetSampleDepth(int(self.tINIConfig["SOFTWARE"]["graphical_depth"]))
  # Parcourt des voies d'acquisition
  print("OBSERVATION //////////////////")
  ucChannelCreated = 0

  tPen = QPen()
  tPen.setMiterLimit(0)
  tPen.setWidth(1);
  #--
  for ucChannelCpt in range( len(tListSensor) ):
   print(ucChannelCpt)
   print(tListSensor[ucChannelCpt])
   sIndex = tListSensor[ucChannelCpt]
   if(ttConfig["SENSOR"][sIndex]["sIndex"] == "EMPTY"): continue
   print(ttConfig["SENSOR"][sIndex]["sIndex"])

   #sName = ttConfig["SENSOR"][sIndex]["sIndex"]+" ("+ttConfig["SENSOR"][sIndex]["sUnit"]+")"
   sName = ttConfig["SENSOR"][sIndex]["sIndex"]
   sUnit = ttConfig["SENSOR"][sIndex]["sUnit"]
   self.chart._series[ucChannelCreated].setName(sName)
   self.chart.tPenTemplate.setBrush( QColor(self.sFGetSensorColorWithID(ttConfig["SENSOR"][sIndex]["uiIndex"])) )
   self.chart._series[ucChannelCreated].setPen( self.chart.tPenTemplate )
   ###
   #self.chart._axisY[ucChannelCreated].setTitleText(sUnit)
   self.chart._axisY[ucChannelCreated].setLabelsColor( self.sFGetSensorColorWithID(ttConfig["SENSOR"][sIndex]["uiIndex"]) )
   tPen.setBrush( QColor(self.sFGetSensorColorWithID(ttConfig["SENSOR"][sIndex]["uiIndex"])) )
   self.chart._axisY[ucChannelCreated].setLinePen( tPen )
   ###
   ucChannelCreated = ucChannelCreated + 1
  #--
  # Init du chartview
  self.chart_view = QChartView( self.chart )
  self.chart_view.setRenderHint( QPainter.Antialiasing )
  self.chart_view.setRubberBand(QChartView.HorizontalRubberBand)
  # Clear vieux graphique
  vbox = QVBoxLayout()
  self.ui.widget_18.setLayout(vbox)
  for i in reversed(range(self.ui.widget_18.layout().count())):
   self.ui.widget_18.layout().itemAt(i).widget().deleteLater()
  self.ui.widget_18.layout().addWidget(self.chart_view)

  #-------------------------------------------
  # CALIBRATION
  #-------------------------------------------
  # Seulement quand en connexion : non ! sinon pas de refresh des datas en live
  for i in reversed(range(self.ui.widget_CalibNav.layout().count())):
   self.ui.widget_CalibNav.layout().itemAt(i).widget().deleteLater()
  # Seulement quand en connexion : non ! sinon pas de refresh des datas en live
  if( self.ui.stackedWidget.currentIndex() == 0 ):
   # Ouverture de l'onglet dashboard
   self.vFNavASBtnClicked(7)
  # Seulement si EC
  if( ttConfig["PRODUCT"]["bECSensor"] ):
   self.tCalibNavSensorWidget = {}
   #
   self.tCalibNavSensorWidget[ "EC" ]  = self.vFCALIBRATIONAddCalibNavElt( "EC",  uiFGetIDWithChannelNameWith("EC"),  ttConfig["SENSOR"]["EC"] )
   # On cache l'inutile
   self.ui.groupBox_CalibrationParameters.setVisible(False)
   self.ui.widget_AuxPt1Date.setVisible(False)
   self.ui.label_txtSN_13.setText("Click to calibrate")
   self.ui.label_AuxPt1Value.setText("EC")

   # Seulement quand en connexion : non ! sinon pas de refresh des datas en live
   #if( self.ui.stackedWidget.currentIndex() == 0 ):
   self.vFCALIBRATIONSensorNavSelectionDynamic("EC",
                                               uiFGetIDWithChannelNameWith("EC"),
                                               ttConfig["SENSOR"]["EC"],
                                               self.tCalibNavSensorWidget["EC"] )
   ##TODO - Prévoir une resélection de l'onglet courant si pas sur connexion
   #else:
   # self.vFCALIBRATIONSensorNavSelectionDynamic( self.tCalibrationCurrentSensor["sConfigName"],
   #                                              self.tCalibrationCurrentSensor["ucChannel"],
   #                                              ttConfig["SENSOR"][self.tCalibrationCurrentSensor["sConfigName"]],
   #                                            self.tCalibNavSensorWidget[self.tCalibrationCurrentSensor["sConfigName"]] )


 #--------------------------------------------------------------------------
 # Suppression element du treeview
 #--------------------------------------------------------------------------
 def vFTreeviewRemoveItem(self, tTreeview):
  uiTopLevelItemCount = tTreeview.topLevelItemCount()
  for uiCpt in range(0,uiTopLevelItemCount):
   tWidget = tTreeview.takeTopLevelItem( 0)
   tTreeview.removeItemWidget(tWidget,0)

 #----------------------------------------------
 # General - Display calculated
 #----------------------------------------------
 def vFClearLayout( self, layout ):
  print("-- vFClearLayout --")
  try:
   for i in reversed(range(layout.count())):
    layout.itemAt(i).widget().setParent(None)
  except Exception as err:
   print(err)

 #----------------------------------------------
 # Dashboard - Création voie depth
 #----------------------------------------------
 def vFDashboardAddPressureLine( self ):
  #
  sTitle = "Pressure"
  sLogo = ":/Logo/Sensor/SVG/F08_Pressure.svg"
  # Appel
  self.vFDashboardSensorLine(sTitle, sLogo)
 #----------------------------------------------
 def vFDashboardAddTemperatureLine( self ):
  #
  sTitle = "Temperature"
  sLogo = ":/Logo/Sensor/SVG/F01_Temperature.svg"
  # Appel
  self.vFDashboardSensorLine(sTitle, sLogo)
 #----------------------------------------------
 def vFDashboardAddConductivityLine( self ):
  #
  sTitle = "Conductivity"
  sLogo = ":/Logo/Sensor/SVG/F02_Conductivity.svg"
  # Appel
  self.vFDashboardSensorLine(sTitle, sLogo)

 #----------------------------------------------
 # Dashboard - Création ligne capteur
 #----------------------------------------------
 def vFDashboardSensorLine( self, sTitle, sLogo ):
  #
  tWidget = QWidget()
  tWidget.setContentsMargins(0,0,0,0)
  # Create a boxlayout (horizontal here)
  tBox = QHBoxLayout()
  tBox.setContentsMargins(9,5,9,5)
  # Set the layout for your tab
  tWidget.setLayout(tBox)
  # Logo
  tLogoLabel = QLabel()
  pixmap = QPixmap( sLogo )
  tLogoLabel.setPixmap(pixmap)
  tLogoLabel.setScaledContents(True)
  tLogoLabel.setMaximumSize(20, 20)
  tWidget.layout().addWidget(tLogoLabel)
  # Numero de la voie
  tLabel = QLabel()
  tLabel.setText("FIXED:")
  tWidget.layout().addWidget(tLabel)
  # Nom de la voie
  tLabel = QLabel()
  tLabel.setText( sTitle )
  tLabel.setStyleSheet("color: rgb(84,84,84);")
  tWidget.layout().addWidget(tLabel)
  # Logo
  tLogoLabel = QLabel()
  pixmap = QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version.svg - W")
  tLogoLabel.setPixmap(pixmap)
  tLogoLabel.setScaledContents(True)
  tLogoLabel.setMaximumSize(20, 20)
  tWidget.layout().addWidget(tLogoLabel)
  # Ajout d'un widget dans un widget en utilisant son layout interne
  self.ui.groupBox_DashboardSensors_2.layout().addWidget(tWidget)

 #----------------------------------------------
 # Dashboard - Affichage windows Sonde date
 #----------------------------------------------
 def vFDashboardSondeDateOpen( self, event ):
  print("-- vFDashboardSondeDateOpen --")
  # Récupération de la valeur du champs
  sSondeDate = self.ui.label_sondeClockDate_2.text()
  # Parse de la donnée
  uiSondeDay   = int( sSondeDate.split("/")[0] )
  uiSondeMonth = int( sSondeDate.split("/")[1] )
  uiSondeYear  = int( sSondeDate.split("/")[2][2]+sSondeDate.split("/")[2][3] )
  # Ouverture de la fenêtre
  self.tUISondeDate.vFOpen( uiSondeDay, uiSondeMonth, uiSondeYear )

 #----------------------------------------------
 # Dashboard - Affichage windows Sonde time
 #----------------------------------------------
 def vFDashboardSondeTimeOpen( self, event ):
  print("-- vFDashboardSondeTimeOpen --")
  # Récupération de la valeur du champs
  sSondeTime = self.ui.label_sondeClockTime_2.text()
  # Parse de la donnée
  uiSondeHour = int( sSondeTime.split(":")[0] )
  uiSondeMin  = int( sSondeTime.split(":")[1] )
  uiSondeSec  = int( sSondeTime.split(":")[2] )
  # Ouverture de la fenêtre
  self.tUISondeTime.vFOpen( uiSondeHour, uiSondeMin, uiSondeSec )

 #----------------------------------------------
 # Dashboard - Affichage windows site ID
 #----------------------------------------------
 def vFDashboardSiteIDOpen( self, event ):
  print("-- vFDashboardCleanEveryOpen --")
  # Récupération du label actuel
  sSiteID = self.ui.label_SiteID_2.text()
  # Ouverture de la fenêtre
  self.tUISiteID.vFOpen( sSiteID )

 #----------------------------------------------
 # Dashboard - Affichage windows site Latitude
 #----------------------------------------------
 def vFDashboardSiteLatitudeOpen( self, event ):
  print("-- vFDashboardSiteIDLatitude --")
  #
  sSiteLatitude = self.ui.label_SiteLat_2.text()
  # Extraction
  sRef  = str( sSiteLatitude.split(" ")[0] )
  if( sRef != "-" ):
   sTxt2 = sSiteLatitude.split(" ")[1]
   uiDeg = int(sTxt2.split("°")[0])
   fMin  = float((sTxt2.split("°")[1]).split("'")[0])
   # Ouverture de la fenêtre
   self.tUISiteLatitude.vFOpenLeveLine( sRef, uiDeg, fMin )
  else:
   # Ouverture de la fenêtre
   self.tUISiteLatitude.vFOpenLeveLine( "N", 0, 0.0 )

 #----------------------------------------------
 # Dashboard - Affichage windows site Longitude
 #----------------------------------------------
 def vFDashboardSiteLongitudeOpen( self, event ):
  print("-- vFDashboardSiteIDLongitude --")
  #
  sSiteLongitude = self.ui.label_SiteLong_2.text()
  # Extraction du champs
  sRef  = str( sSiteLongitude.split(" ")[0] )
  if( sRef != "-" ):
   sTxt2 = sSiteLongitude.split(" ")[1]
   uiDeg = int(sTxt2.split("°")[0])
   fMin  = float((sTxt2.split("°")[1]).split("'")[0])
   # Ouverture de la fenêtre
   self.tUISiteLongitude.vFOpenLeveLine( sRef, uiDeg, fMin )
  else:
   # Ouverture de la fenêtre
   self.tUISiteLongitude.vFOpenLeveLine( "E", 0, 0.0 )

 #----------------------------------------------
 # Dashboard - Affichage windows site altitude
 #----------------------------------------------
 def vFDashboardSiteAltitudeOpen( self, event ):
  print("-- vFDashboardSiteAltitudeOpen --")
  #
  sSiteAltitude = self.ui.label_SiteAltitude.text()
  # Extraction
  uiAltitude = int(sSiteAltitude.split(" m")[0])
  # Ouverture de la fenêtre
  self.tUISiteAltitude.vFOpen( uiAltitude )

 #----------------------------------------------
 # Dashboard - Affichage windows site altitude
 #----------------------------------------------
 def vFDashboardStartProductOpen( self, event ):
  print("-- vFDashboardStartProductOpen --")
  #
  sStartModeType = self.ui.label_LogStartMode.text()
  sStartModeDate = self.ui.label_LogStartAt.text()
  # Current datetime
  #sSondeDate = self.ui.label_sondeClockDate_2.text()
  #sSondeTime = self.ui.label_sondeClockTime_2.text()

  # Extraction
  #uiAltitude = int(sSiteAltitude.split(" m")[0])
  # Ouverture de la fenêtre
  self.tUIStartProduct.vFOpen( sStartModeType, sStartModeDate )

 #----------------------------------------------
 # Dashboard - Affichage configuration
 #----------------------------------------------
 def vFDashboardLogDataEveryOpen( self, event ):
  print("-- vFDashboardLogDataEveryOpen --")
  # Récupération valeur
  sLogDataPeriod = self.ui.label_LogDataEvery_2.text()
  uiLogDataHour = int( sLogDataPeriod.split("h")[0] )
  uiLogDataMin  = int( sLogDataPeriod.split("h")[1].split("m")[0] )
  fLogDataSec   = float( sLogDataPeriod.split("h")[1].split("m")[1] )
  self.tUILogDataEvery.vFOpen( uiLogDataHour, uiLogDataMin, fLogDataSec )

 #----------------------------------------------
 # Dashboard - Affichage windows site altitude
 #----------------------------------------------
 def vFDashboardLogDataForOpen( self, event ):
  print("-- vFDashboardLogDataForOpen --")
  # Log data for
  sLogDataFor = self.ui.label_LogDataFor.text()
  # Extraction
  uiLogDataFor = int(sLogDataFor.split(" h")[0])
  # Ouverture de la fenêtre
  self.tUILogDataFor.vFOpen( uiLogDataFor )

 #----------------------------------------------
 # Dashboard - Affichage windows setup logging state
 #----------------------------------------------
 def vFDashboardSetupLoggingStateOpen( self, event ):
  print("-- vFDashboardSetupLoggingState --")
  # Récupération valeur
  sActivation = self.ui.label_EventLogState_2.text()
  self.tUISetupLoggingState.vFOpen( sActivation )

 #----------------------------------------------
 #Dashboard -  Affichage windows setup logging every
 #----------------------------------------------
 def vFDashboardSetupLoggingEveryOpen( self, event ):
  print("-- vFDashboardSetupLoggingEvery --")
  # Récupération valeur
  sParameter = self.ui.label_EventLogEvery_2.text()
  uiHours    = int(sParameter.split("h")[0])
  sMinutes   = sParameter.split("h")[1]
  uiMinutes  = int(sMinutes.split("m")[0])
  sSec       = sParameter.split("m")[1].split("s")[0]
  fSec       = float(sSec)
  # Open
  self.tUISetupLoggingEvery.vFOpen( uiHours, uiMinutes, fSec )

 #----------------------------------------------
 # Dashboard - Affichage windows event logging level
 #----------------------------------------------
 def vFDashboardEventLoggingLevelOpen( self, event ):
  print("-- vFDashboardEventLoggingLevelOpen --")
  # Récupération valeur
  sParameter = self.ui.label_EventLogLevelValue.text()
  if( sParameter == "Disable" ):
   self.tUIEventLoggingLevel.vFOpen( "Disable", 0.0 )
  else:
   fValue = float(sParameter.split(" m")[0])
   self.tUIEventLoggingLevel.vFOpen( "Enable", fValue )

 #----------------------------------------------
 # Dashboard - Affichage windows event logging temperature
 #----------------------------------------------
 def vFDashboardSetupLoggingTemperatureOpen( self, event ):
  print("-- vFDashboardSetupLoggingTemperatureOpen --")
  # Récupération valeur
  sParameter = self.ui.label_EventLogTemperatureValue.text()
  if( sParameter == "Disable" ):
   self.tUIEventLoggingTemperature.vFOpen( "Disable", 0.0 )
  else:
   fValue = float(sParameter.split(" °C")[0])
   self.tUIEventLoggingTemperature.vFOpen( "Enable", fValue )

 #----------------------------------------------
 # Dashboard - Affichage windows event logging salinity
 #----------------------------------------------
 def vFDashboardSetupLoggingSalinityOpen( self, event ):
  print("-- vFDashboardSetupLoggingSalinityOpen --")
  # Récupération valeur
  sParameter = self.ui.label_EventLogSalinityValue.text()
  if( sParameter == "Disable" ):
   self.tUIEventLoggingSalinity.vFOpen( "Disable", 0 )
  else:
   fValue = float(sParameter.split(" PSU")[0])
   self.tUIEventLoggingSalinity.vFOpen( "Enable", fValue )


 #=========================================================================
 # LIVEVIEW
 #=========================================================================
 #----------------------------------------------
 # Liveview - Affichage configuration
 #----------------------------------------------
 #def vFLiveviewDisplayBloc( self, ucChannel, tChannel ):
 def vFLiveviewDisplayBloc( self, tChannel, uiColumn, uiRow, uiChannelIndex ):
  #print("-- vFLiveviewDisplayBloc --")
  #print("uiRow    = %d" % uiRow)
  #print("uiColumn = %d" % uiColumn)
  tWidget = QWidget()
  tWidget.setContentsMargins(0,0,0,0)
  # Create a boxlayout (vertical here)
  tBox = QVBoxLayout()
  tBox.setContentsMargins(0,0,0,0)
  # Set the layout for your tab
  tWidget.setLayout(tBox);

  tWidget.setMaximumSize(120, 110)
  tWidget.setMinimumSize(120, 110)

  # Nom de la voie + logo
  tWidgetChannelName = QWidget()
  tWidgetChannelName.setContentsMargins(0,0,0,0)
  tWidgetChannelName.setMaximumSize(120, 30)
  tWidgetChannelName.setMinimumSize(120, 30)
  # Set the layout for your tab
  tBoxChannelName = QHBoxLayout()
  tBoxChannelName.setContentsMargins(9,0,9,0)
  tWidgetChannelName.setLayout(tBoxChannelName);
  # Style
  tWidgetChannelName.setStyleSheet("background-color: "+self.sFGetSensorColorWithID(tChannel["uiIndex"])+";"+
  "border: none;"+
  "color: white;"+
  "border-radius: 0;"+
  "border-top-left-radius: 8px;"+
  "border-top-right-radius: 8px;"
  )
  # Logo
  tLogoLabel = QLabel()
  print(tChannel)
  print(tChannel["uiIndex"])
  pixmap = QPixmap( self.sFGetSensorLogoWithID( tChannel["uiIndex"], "white" ) )
  tLogoLabel.setPixmap(pixmap)
  tLogoLabel.setScaledContents(True)
  tLogoLabel.setMaximumSize(20, 20)
  tLogoLabel.setMinimumSize(20, 20)
  # Label
  tChannelLabel = QLabel()
  tChannelLabel.setText(tChannel["sIndex"])

  tBoxChannelName.layout().addWidget(tLogoLabel)
  tBoxChannelName.layout().addWidget(tChannelLabel)
  tWidget.layout().addWidget(tWidgetChannelName)

  self.tMeasureBox.append({})
  self.tMeasureBox[len(self.tMeasureBox)-1]   = {}
  self.tMeasureBox[len(self.tMeasureBox)-1]["tLabelMeasure"] = QLabel()
  self.tMeasureBox[len(self.tMeasureBox)-1]["tLabelMeasure"].setText("--")
  self.tMeasureBox[len(self.tMeasureBox)-1]["tLabelMeasure"].setAlignment(Qt.AlignCenter)
  self.tMeasureBox[len(self.tMeasureBox)-1]["tLabelMeasure"].setStyleSheet("*{font-size: 15pt;font-weight:800;}")
  tWidget.layout().addWidget(self.tMeasureBox[len(self.tMeasureBox)-1]["tLabelMeasure"])
  """ Avant PC Conf
  tLabelUnit = QLabel()
  tLabelUnit.setText("("+tChannel["sUnit"]+")")
  tLabelUnit.setAlignment(Qt.AlignCenter)
  tLabelUnit.setStyleSheet("*{font-size: 10pt;}")
  tWidget.layout().addWidget(tLabelUnit)
  """
  self.tMeasureBox[len(self.tMeasureBox)-1]["tLabelUnit"] = QLabel()
  self.tMeasureBox[len(self.tMeasureBox)-1]["tLabelUnit"].setText("("+tChannel["sUnit"]+")")
  self.tMeasureBox[len(self.tMeasureBox)-1]["tLabelUnit"].setAlignment(Qt.AlignCenter)
  self.tMeasureBox[len(self.tMeasureBox)-1]["tLabelUnit"].setStyleSheet("*{font-size: 10pt;}")
  tWidget.layout().addWidget(self.tMeasureBox[len(self.tMeasureBox)-1]["tLabelUnit"])

  # Sauvegarde de l'emplacement texte de la donnée
  self.tMeasureBox[len(self.tMeasureBox)-1]["sName"]         = tChannel["sIndex"]
  #self.tMeasureBox[len(self.tMeasureBox)-1]["tLabelMeasure"] = tLabelMeasure
  #self.tMeasureBox[len(self.tMeasureBox)-1]["tLabelUnit"]    = tLabelUnit
  self.tMeasureBox[len(self.tMeasureBox)-1]["bState"]        = True
  self.tMeasureBox[len(self.tMeasureBox)-1]["sColor"]        = self.sFGetSensorColorWithID(tChannel["uiIndex"])

  # Ajout d'un widget dans un widget en utilisant son layout interne
  self.ui.widget_11.layout().addWidget(tWidget, uiRow, uiColumn )
  # Signal - Sur clique
  self.siLiveviewClickBox.emit(tChannel["sIndex"], tWidget, tWidgetChannelName, uiChannelIndex)


 #-------------------------------------
 # Nom de la voie selon l'ID
 #-------------------------------------
 def sFGetSensorLogoWithID( self, uiAUXAssign, sColor ):
  print("== sFGetSensorLogoWithID ==")

  if( sColor == "white" ): sSVG = "SVG_blanc"
  else:                    sSVG = "SVG"
  # Par défaut
  sSvgPath = ":/Logo/Sensor/"+sSVG+"/EC DO.svg"
  # Selon le type de capteur
  if( uiAUXAssign == 0 ):  sSvgPath = "EMPTY"
  # FIXED
  if( uiAUXAssign == -1 ):  sSvgPath = "://Logo/Sensor/"+sSVG+"/F01_Temperature.svg"
  if( uiAUXAssign == -2 ):  sSvgPath = "://Logo/Sensor/"+sSVG+"/F02_Conductivity.svg"
  if( uiAUXAssign == -8 ):  sSvgPath = "://Logo/Sensor/"+sSVG+"/F08_Pressure.svg"
  if( uiAUXAssign == -9 ):  sSvgPath = "://Logo/Sensor/"+sSVG+"/F09_Baro.svg"
  print(sSvgPath)
  return( sSvgPath )

 #-------------------------------------
 # Couleur de la voie selon l'ID
 #-------------------------------------
 def sFGetSensorColorWithID( self, uiAUXAssign ):
  #print("== sFGetSensorColorWithID ==")

  if( uiAUXAssign == 0 ):  sColor = "#555555"
  # FIXED
  if( uiAUXAssign == -1 ):  sColor = "#F34333" # Temperature
  if( uiAUXAssign == -2 ):  sColor = "#1E847A" # EC
  if( uiAUXAssign == -8 ):  sColor = "#AFC0E1" # Depth
  if( uiAUXAssign == -9 ):  sColor = "#03A9F2" # Baro
  # Retour de la couleur
  return( sColor )

 #-------------------------------------
 # Couleur de la voie selon l'ID
 #-------------------------------------
 def sFGetSensorColorWithGraphLabel( self, sLabel ):
  # FIXED
  if( sLabel == "Batt"      ): sColor = "#555555" # VBatt
  if( sLabel == "Temp C"    ): sColor = "#F34333" # Temperature
  if( sLabel == "Temp F"    ): sColor = "#F34333" # Temperature
  if( sLabel == "Depth m"   ): sColor = "#AFC0E1" # Depth m
  if( sLabel == "Depth f"   ): sColor = "#AFC0E1" # Depth f
  if( sLabel == "Baro"      ): sColor = "#03A9F2" # Baro
  if( sLabel == "EC"        ): sColor = "#1E847A" # EC
  # AUX
  if( sLabel == "Salinity"    ): sColor = "#B2BEB5" # Salinity
  # Retour de la couleur
  return( sColor )


 #----------------------------------------------
 # Affichage measurement data
 #----------------------------------------------
 def vFDisplayMeasureData( self, ttConfig ):
  print("-- VIEW - vFDisplayMeasureData --")

  ttMeasure = ttConfig["SENSOR"]
  tfResult = [0]*len(self.tMeasureBox)

  #-- Onglet liveview --
  if( self.uiNavActivePage == 2 ):
   print("############################################")
   # Parcourt des résultats de mesure
   for sElt in ttMeasure:
    if( sElt == "EMPTY" ): continue
    sIndex = ttMeasure[sElt]["sIndex"]
    # Recherche du paramètre
    for uiCpt in range(len(self.tMeasureBox)):
     # Si empty on skip
     if( ttMeasure[sElt]["sIndex"] == "EMPTY" ): continue
     # Si on trouve le paramètre
     if( self.tMeasureBox[uiCpt]["sName"] == sIndex ):
      print("sElt = "+sElt)
      # -- TEMP --
      if( sElt == "TEMP" ):
       print('self.ui.label_Config_TempUnit.text() = '+self.ui.label_Config_TempUnit.text())
       # DegF
       if( self.ui.label_Config_TempUnit.text() == "F" ):
        fResult = ttConfig["CALCULATED"]["TEMP"]["fTempF"]
        print("fResult = %.2f"%fResult)
       # DegC
       else:
        fResult = ttConfig["SENSOR"]["TEMP"]["fResult"]
      # -- DEPTH --
      elif( sElt == "DEPTH" ):
       print('self.ui.label_Config_DepthUnit.text() = '+self.ui.label_Config_DepthUnit.text())
       # Foot
       if( self.ui.label_Config_DepthUnit.text() == "f" ):
        fResult = ttConfig["CALCULATED"]["DEPTH"]["fDepthF"]
        print("fResult = %.2f"%fResult)
       # Meter
       else:
        fResult = ttConfig["SENSOR"]["DEPTH"]["fResult"]
      # -- EC --
      elif( ( sElt == "EC" ) and ( ttConfig["PRODUCT"]["bECSensor"] ) ):
       """
       # 25C
       if( self.ui.label_Config_ECRefTemp.text() == "25 C" ):
        fResult = ttConfig["CALCULATED"]["EC"]["fEC_25"]
       elif( self.ui.label_Config_ECRefTemp.text() == "20 C" ):
        fResult = ttConfig["CALCULATED"]["EC"]["fEC_20"]
       else:
        fResult = ttConfig["SENSOR"]["EC"]["fResult"]
       """
       fResult = ttConfig["SENSOR"]["EC"]["fResult"]
      # -- AUTRES --
      else:
       continue
       #fResult = ttMeasure[sElt]["fResult"]

      uiIndex = uiCpt
      self.tMeasureBox[uiIndex]["tLabelMeasure"].setText( "%.2f"%fResult )
      # Affichage résultat texte
      tfResult[uiIndex] = fResult
      break

   # Voie calculée
   #self.ui.label_LV_salinity.setText( "%.2f"%ttConfig["CALCULATED"]["Salinity"]["fResult"] )
   #self.ui.label_LV_SSG.setText( "%.2f"%ttConfig["CALCULATED"]["SSG"]["fResult"] )
   #self.ui.label_LV_TDS.setText( "%.2f"%ttConfig["CALCULATED"]["TDS"]["fResult"] )
   #self.ui.label_LV_Ammonia.setText( "%.2f"%ttConfig["SENSOR"]["AUX7"]["fResult"] )

   # Affichage du lot d'échantillon dans le graph
   self.chart.vFAddSample( tfResult )
   self.chart_view.repaint()
   self.chart_view.update()
   self.chart.layout().invalidate()
   self.chart.layout().activate()

  #-- Onglet calibration --
  if(   ( self.uiNavActivePage == 4 )
    and ( self.ui.stackedWidget_calibrationMain.currentIndex() == 1 ) ):
   # Récupération du point
   slabel_calibPointName = self.ui.label_calibPointName.text()
   scalibPointName       = slabel_calibPointName.split(" - ")[0]
   # Si DO
   if( scalibPointName == "DO" ):
    print("**********************")
    print("DOOOOOOOOO")
    print("**********************")
    scalibPointName = "DO Sat"

   print(ttMeasure)

   # Parcourt des résultats de mesure
   for ucCpt in range( len( list(ttMeasure) ) ):
    sIndexTab = list(ttMeasure)[ucCpt]
    # Pour la calibration
    if( sIndexTab == "TEMP" ):
     sIndexTemperature = sIndexTab
     # Si unité en degC
     if( self.ui.label_Config_TempUnit.text() == "F" ):
      # Remplissage valeur numérique
      self.ui.label_calibRT_tempValue.setText( "%.2f"%ttConfig["CALCULATED"]["TEMP"]["fTempF"] + "°F" )
     else:
      self.ui.label_calibRT_tempValue.setText( "%.2f"%ttConfig["SENSOR"]["TEMP"]["fResult"] + "°C" )
     continue
    if( ttMeasure[sIndexTab]["sIndex"] == "Baro" ):
     sIndexBaro = sIndexTab
     self.ui.label_calibRT_baroValue.setText( "%.2f"%ttMeasure[sIndexBaro]["fResult"] + "mB" )
     continue
    if( ttMeasure[sIndexTab]["sIndex"] == "pH mV" ):
     sIndexPHmv = sIndexTab
     self.ui.label_calibRT_pHmvValue.setText( "%.2f"%ttMeasure[sIndexPHmv]["fResult"] + "mV" )
     continue
    # Si la voie que l'on calibre
    if( ttMeasure[sIndexTab]["sIndex"].replace(" ","").lower() != scalibPointName.replace(" ","").lower() ): continue
    # Conservation de la voie
    sIndex = ttMeasure[sIndexTab]["sIndex"]
    sIndexTabKeep = sIndexTab
    #break
   # Si voie EC
   if( sIndex == "EC" ):
    if( self.ui.label_Config_ECRefTemp.text() == "25 C" ):
     fResult = ttConfig["CALCULATED"]["EC"]["fEC_25"]
    elif( self.ui.label_Config_ECRefTemp.text() == "20 C" ):
     fResult = ttConfig["CALCULATED"]["EC"]["fEC_20"]
    else:
     fResult = ttConfig["SENSOR"]["EC"]["fResult"]
   # Toutes autres voies de mesure
   else:
    fResult = ttMeasure[sIndexTabKeep]["fResult"]

   # Ajout de l'échantillon sur le graph
   self.chartCalib.vFAddSample( [fResult] )
   # Refresh
   self.chart_view.repaint()
   self.chart_view.update()
   self.chart.layout().invalidate()
   self.chart.layout().activate()
   # Remplissage valeur numérique
   self.ui.label_calibRTValue.setText( "%.2f"%fResult )

 #----------------------------------------------
 # Liveview - Clique box mesure
 #----------------------------------------------
 def vFMainWindowLiveviewBoxMeasureClick( self, sLabel, tWidget, tWidgetChannelName, uiChannelIndex ):
  print("-- LIVEVIEW - vFMainWindowLiveviewBoxMeasureClick --")
  print("sLabel = "+sLabel)
  # Si bloc actif
  if( self.tMeasureBox[uiChannelIndex]["bState"] ):
   tWidgetChannelName.setStyleSheet("background-color: #cccccc;"+
   "border: none;"+
   "color: white;"+
   "border-radius: 0;"+
   "border-top-left-radius: 8px;"+
   "border-top-right-radius: 8px;"
   )
   self.tMeasureBox[uiChannelIndex]["tLabelMeasure"].setStyleSheet("*{font-size: 15pt;font-weight:800;color: #cccccc;}")
   self.tMeasureBox[uiChannelIndex]["tLabelUnit"].setStyleSheet("*{font-size: 10pt;color: #cccccc;}")
   #
   self.chart.vFRemoveSeries(uiChannelIndex)
   #
   self.tMeasureBox[uiChannelIndex]["bState"] = False
  # Bloc inactif
  else:
   tWidgetChannelName.setStyleSheet("background-color: "+self.tMeasureBox[uiChannelIndex]["sColor"]+";"+
   "border: none;"+
   "color: white;"+
   "border-radius: 0;"+
   "border-top-left-radius: 8px;"+
   "border-top-right-radius: 8px;"
   )
   self.tMeasureBox[uiChannelIndex]["tLabelMeasure"].setStyleSheet("*{font-size: 15pt;font-weight:800;}")
   self.tMeasureBox[uiChannelIndex]["tLabelUnit"].setStyleSheet("*{font-size: 10pt;}")
   #
   self.chart.vFAddSeries(uiChannelIndex)
   # Activation du bloc
   self.tMeasureBox[uiChannelIndex]["bState"] = True

 #----------------------------------------------
 # Liveview - Start measurement data
 #----------------------------------------------
 def vFStartMeasureData( self ):
  # Activation bouton enregistrement
  self.ui.pushButton_LiveViewRecord.setEnabled(True)
  # Gestion état bouton on-off
  self.ui.startMeasure_btn.setVisible(False)
  self.ui.stopMeasure_btn.setVisible(True)

 #----------------------------------------------
 # Liveview - Stop measurement data
 #----------------------------------------------
 def vFStopMeasureData( self ):
  # Désactivation bouton enregistrement
  self.ui.pushButton_LiveViewRecord.setEnabled(False)
  # Gestion état bouton on-off
  self.ui.startMeasure_btn.setVisible(True)
  self.ui.stopMeasure_btn.setVisible(False)

 #----------------------------------------------
 # Liveview - Clear measurement data
 #----------------------------------------------
 def vFClearMeasureData( self ):
  # Effacement de la data dans les blocs
  for ucCpt in range(len(self.tMeasureBox)):
   #print("ucCpt = %d"%ucCpt)
   self.tMeasureBox[ucCpt]["tLabelMeasure"].setText("--")
  # Clear graph
  self.chart.vFClear()

 #----------------------------------------------
 # Liveview - Start recording
 #----------------------------------------------
 def vFLiveviewStartRecording( self ):
  print("-- vFLiveviewStartRecording --")
  self.ui.pushButton_LiveViewRecordStop.setVisible(True)
  self.ui.pushButton_LiveViewRecord.setVisible(False)
  # Variable pour le changement de couleur du bouton
  self.bLiveviewRecordBtnColored = False
  self.timerLVRecording.start(1000)
 #----------------------------------------------
 def vFLiveviewRecordingOccuringTimeout( self ):
  print("vFLiveviewRecordingOccuringTimeout")
  if( self.bLiveviewRecordBtnColored ):
   self.bLiveviewRecordBtnColored = False
   self.ui.pushButton_LiveViewRecordStop.setStyleSheet("")
   self.ui.pushButton_CalibRecordStop.setStyleSheet("")
  else:
   self.bLiveviewRecordBtnColored = True
   self.ui.pushButton_LiveViewRecordStop.setStyleSheet("background-color: #f94c57;")
   self.ui.pushButton_CalibRecordStop.setStyleSheet("background-color: #f94c57;")
 #----------------------------------------------
 def vFLiveviewStopRecording( self ):
  print("-- vFLiveviewStopRecording --")
  self.bLiveviewRecordBtnColored = False
  self.ui.pushButton_LiveViewRecordStop.setStyleSheet("")
  self.ui.pushButton_LiveViewRecordStop.setVisible(False)
  self.ui.pushButton_LiveViewRecord.setVisible(True)
  # Arrêt du timer
  self.timerLVRecording.stop()


 #=========================================================================
 # CALIBRATION
 #=========================================================================
  #----------------------------------------------
 # Calibration - Affichage de la donnée
 #----------------------------------------------
 def vFCALIBRATIONAddCalibNavElt( self, sChannelName, ucChannel, tChannel ):
  print("-- vFCALIBRATIONAddCalibNavElt --")

  tWidget = QWidget()
  tWidget.setContentsMargins(0,0,0,0)
  # Create a boxlayout (horizontal here)
  tLayout = QVBoxLayout()
  tLayout.setSpacing(0)
  tWidget.setStyleSheet("background-color: "+self.sFGetSensorColorWithID(tChannel["uiIndex"])+";")
  print("#widget_CalibNav > Qwidget{background-color: "+self.sFGetSensorColorWithID(tChannel["uiIndex"])+"};")
  # Set the layout for your tab
  tWidget.setLayout(tLayout)
  # Logo
  tLogoLabel = QLabel()
  pixmap = QPixmap( self.sFGetSensorLogoWithID( tChannel["uiIndex"], "white" ) )
  tLogoLabel.setPixmap(pixmap)
  tLogoLabel.setScaledContents(True)
  tLogoLabel.setFixedWidth(40)
  tLogoLabel.setFixedHeight(40)
  tLogoLabel.setAlignment(Qt.AlignCenter)
  tWidget.layout().addWidget(tLogoLabel, Qt.AlignCenter)
  # Nom de la voie
  tLabel = QLabel()
  tLabel.setAlignment(Qt.AlignCenter)
  if( ucChannel < 0 ):
   tLabel.setText(tChannel["sIndex"])
   tWidget.layout().addWidget(tLabel)
  else:
   tLabel.setText("AUX"+str(int(ucChannel)+1)+":")
   tWidget.layout().addWidget(tLabel)
   tLabel = QLabel()
   tLabel.setAlignment(Qt.AlignCenter)
   tLabel.setText(tChannel["sIndex"])
   tWidget.layout().addWidget(tLabel)

  tWidget.layout().setAlignment(Qt.AlignHCenter)
  tWidget.setFixedWidth(90)
  tWidget.setFixedHeight(90)
  tWidget.layout().setStretch(0, 5)
  tWidget.layout().setStretch(1, 1)
  tWidget.layout().setStretch(2, 1)
  tWidget.layout().addStretch()

  # Ajout d'un widget dans un widget en utilisant son layout interne
  self.ui.widget_CalibNav.layout().addWidget(tWidget)
  # Ajout de l'event sur ligne
  ##self.xCalibrationSensorSelectConnectSignal.emit( sChannelName, ucChannel, tChannel, tWidget )
  # Appui sur la première ligne
  self.siCalibrationPointSelectConnectSignal.emit( sChannelName, ucChannel, tChannel, self.ui.widget_AuxPt1Value, 0 )

  return tWidget


 #----------------------------------------------
 # Calibration - Changement de menu capteur
 #----------------------------------------------
 def vFCALIBRATIONSensorNavSelectionDynamic( self, sConfigName, ucChannel, tChannel, tWidget ):
  print("-- vFCALIBRATIONSensorNavSelectionDynamic --")
  print("ucChannel = %d"%ucChannel)

  # Sauvegarde de l'onglet sélectionné
  self.tCalibrationCurrentSensor["sConfigName"] = sConfigName
  self.tCalibrationCurrentSensor["ucChannel"]   = ucChannel
  self.tCalibrationCurrentSensor["tChannel"]    = tChannel

  # Remise par défaut
  for i in reversed(range(self.ui.widget_CalibNav.layout().count())):
   self.ui.widget_CalibNav.layout().itemAt(i).widget().setObjectName("")
   self.ui.widget_CalibNav.layout().itemAt(i).widget().setStyleSheet( self.ui.widget_CalibNav.layout().itemAt(i).widget().styleSheet() )

  tWidget.setObjectName("objectNameTest")
  tWidget.setStyleSheet( tWidget.styleSheet() )
  self.ui.widget_CalibNav.style().unpolish(self.ui.widget_CalibNav)
  self.ui.widget_CalibNav.style().polish(self.ui.widget_CalibNav)
  #tWidget.setStyleSheet("QWidget#objectNameTest{ border: 5px solid rgb(255,255,255);background-color:transparent;}");
  #tWidget.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)
  #tWidget.setLineWidth(1)
  #widget_CalibNav

  # Affichage menu
  sIndex = tChannel["sIndex"]
  # Point 1
  self.ui.groupBox_AUX_PT1.setTitle(tCalibChannelInfo[sIndex]["Point"][0]["sName"])
  self.siCalibrationPointSelectConnectSignal.emit( sConfigName, ucChannel, tChannel, self.ui.widget_AuxPt1Value, 0 )
  # Point 2
  self.ui.groupBox_AUX_PT2.setVisible(False)
  # Point 3
  self.ui.groupBox_AUX_PT3.setVisible(False)

  # Restauration point de calibration
  print("--------------------")
  print(sConfigName)
  print("--------------------")
  self.siCalibrationPointRestore.emit( sConfigName )

  # Réinit sensor
  self.ui.groupBox_CalibrationParameters.setVisible(False)
  #self.ui.widget_ECCalValue.setVisible(False)
  #self.ui.widget_ECRefTemperature.setVisible(False)
  self.ui.widget_ORPCalValue.setVisible(False)
  self.ui.widget_AuxGSFactor.setVisible(False)
  # Reinit point
  self.ui.groupBox_CalibrationParameters_Point.setVisible(False)
  self.ui.widget_ECCalValue_Point.setVisible(False)
  self.ui.widget_ECCalValue_Point_2.setVisible(False)
  self.ui.widget_ORPCalValue_Point.setVisible(False)
  self.ui.widget_CalSensor_ECCalValue.setVisible(False)
  self.ui.widget_CalSensor_ECUserValue.setVisible(False)
  self.ui.widget_ECCalValue_Point_2.setVisible(False)
  self.ui.widget_ECCalValue_Point_3.setVisible(False)
  #	Cache date de dernière calibration et valeur
  self.ui.widget_31.setVisible(False)
  self.ui.widget_32.setVisible(False)

  #---------------
  # Si EC
  if( sIndex == "EC" ):
   print('sIndex == "EC"')
   self.ui.groupBox_CalibrationParameters.setVisible(False)
   #self.ui.widget_CalSensor_ECUserValue.setVisible(True)
   self.ui.pushButton_RestoreDefaultCalibration.setVisible(False)
   ##self.ui.widget_CalSensor_ECCalValue.setVisible(True)
   ##self.ui.label_CalSensor_ECCalValue.setText( tChannel["sCalValue"] )

   self.ui.groupBox_CalibrationParameters_Point.setVisible(True)
   self.ui.widget_ECCalValue_Point.setVisible(True)

   if(  ( self.ui.label_CalSensor_ECCalValue.text() == "User" ) ):
    self.ui.widget_CalSensor_ECUserValue.setVisible(True)
    self.ui.label_CalSensor_ECUserValue.setText( str( tChannel["uiUserCalValue"] )+ " uS/cm" )
   elif ( self.ui.label_CalSensor_ECCalValue.text() == "RapidCal" ):
    self.ui.widget_CalSensor_ECUserValue.setVisible(True)
    self.ui.label_CalSensor_ECUserValue.setText( str( 2570 )+ " uS/cm" )
   else:
    self.ui.widget_CalSensor_ECUserValue.setVisible(False)

   ##self.ui.comboBox_ECCalValue_Point.setCurrentText(tChannel["sCalValue"])

   # User
   #self.ui.spinBox_ECCalValue_2_Point.setValue(tChannel["uiUserCalValue"])
   if( self.ui.comboBox_ECCalValue_Point.currentText() == "User" ):
    self.ui.widget_ECCalValue_Point_2.setVisible(True)
   # RapidCal
   if( self.ui.comboBox_ECCalValue_Point.currentText() == "RapidCal" ):
    self.ui.spinBox_ECCalValue_2_Point_2.setValue(2570)
    self.ui.widget_ECCalValue_Point_3.setVisible(True)
   # SC-35
   if( self.ui.comboBox_ECCalValue_Point.currentText() == "SC-35" ):
    self.ui.spinBox_ECCalValue_2_Point_2.setValue(53065)
    self.ui.widget_ECCalValue_Point_3.setVisible(True)

  # Descriptif
  sNetwork = tCalibChannelInfo[sIndex]["sNetwork"]
  self.ui.textBrowser_6.setText(sNetwork)

  # Changement pour l'onglet template
  #self.ui.stackedWidget_calibSensorPoint.setCurrentIndex(3)

 #----------------------------------------------
 # Calibration - Changement du menu point de calibration
 #----------------------------------------------
 def vFCALIBRATIONPointNavSelection( self, uiIndex ):
  print("-- vFCALIBRATIONPointNavSelection --")
  self.ui.stackedWidget_calibrationMain.setCurrentIndex(int(uiIndex))


 #----------------------------------------------
 # Calibration - Chargement/Affichage du menu point de calibration
 #----------------------------------------------
 def vFCALIBRATIONPointNavSelectionDynamic( self, sConfigName, ucChannel, tChannel, tWidget, uiPoint ):
  # Changement d'onglet
  self.ui.stackedWidget_calibrationMain.setCurrentIndex(1)
  # Nom du point
  #self.ui.label_calibPointName.setText( sConfigName+":"+tChannel["sIndex"] + " - " + tChannel["Point"][uiPoint]["sName"] )
  ##self.ui.label_calibPointName.setText( tChannel["sIndex"] + " - " + tChannel["Point"][uiPoint]["sName"] )
  self.ui.label_calibPointName.setText( tChannel["sIndex"]  )
  # Unité de la voie mesurée
  self.ui.label_calibRTUnit.setText( "("+tChannel["sUnit"]+")" )
  # Last calibration date
  ##self.ui.label_calibPointLastCalibDate.setText( ("%02u"%tChannel["Point"][uiPoint]["uiDay"])+("/%02u"%tChannel["Point"][uiPoint]["uiMonth"])+("/20%02u"%tChannel["Point"][uiPoint]["uiYear"]) )
  # Last calibration value
  ##self.ui.label_calibPointLastCalibValue.setText( str(tChannel["Point"][uiPoint]["uiCalReport"])+" "+tChannel["Point"][uiPoint]["sCalReportUnit"] )
  # Pas de pH
  self.ui.widget_calibRTpHmV.setVisible(False)
  # Nom de la voie dans la configuration (masqué dans la page)
  self.ui.label_hiddenChannelName.setText(sConfigName)
  # Numéro du point de calibration
  self.ui.label_hiddenPointNumber.setText(str(uiPoint))
  # Network
  self.ui.textBrowser_calPoint.setText( tCalibChannelInfo[tChannel["sIndex"]]["Point"][uiPoint]["sNetwork"] )

  # Création du graphique
  self.chartCalib = VChart(1)
  self.chartCalib.vFSetSampleDepth(int(self.tINIConfig["SOFTWARE"]["graphical_depth"]))
  self.chartCalib._series[0].setName(tChannel["sIndex"])
  self.chartCalib.tPenTemplate.setBrush( QColor(self.sFGetSensorColorWithID(tChannel["uiIndex"])) )
  self.chartCalib._series[0].setPen( self.chart.tPenTemplate )
  self.chartCalib.legend().hide()
  self.chartCalib.setContentsMargins(-15, -15, -15, -15)

  self.chartCalib_view = QChartView( self.chartCalib )
  self.chartCalib_view.setRenderHint( QPainter.Antialiasing )
  self.chartCalib_view.setRubberBand(QChartView.HorizontalRubberBand)
  # Clear vieux graphique
  vbox = QVBoxLayout()
  vbox.setContentsMargins(0, 0, 0, 0)
  self.ui.widget_calibGraph.setLayout(vbox);
  for i in reversed(range(self.ui.widget_calibGraph.layout().count())):
   self.ui.widget_calibGraph.layout().itemAt(i).widget().deleteLater()
  self.ui.widget_calibGraph.layout().addWidget(self.chartCalib_view)
  # On émet le signal de fin d'affichage de la page (démarrage mesure)
  self.xCalibrationPointPageDisplayedSignal.emit()

  # Signal de fin de point de calibration


 #----------------------------------------------
 # Calibration - Lancement mesure
 #----------------------------------------------
 def vFCALIBRATIONMesureStart( self ):
  self.ui.pushButton_CalibRecord.setEnabled(True)
 #----------------------------------------------
 def vFCALIBRATIONMesureStop( self ):
  self.ui.pushButton_CalibRecord.setEnabled(False)
 #----------------------------------------------
 def vFCALIBRATIONStartRecording( self ):
  self.ui.pushButton_CalibRecord.setVisible(False)
  self.ui.pushButton_CalibRecordStop.setVisible(True)
  # Variable pour le changement de couleur du bouton
  self.bCalibrationRecordBtnColored = False
  self.timerCALRecording.start(1000)

 #----------------------------------------------
 def vFCALIBRATIONRecordingOccuringTimeout( self ):
  print("vFCALIBRATIONRecordingOccuringTimeout")
  if( self.bCalibrationRecordBtnColored ):
   self.bCalibrationRecordBtnColored = False
   self.ui.pushButton_CalibRecordStop.setStyleSheet("")
  else:
   self.bCalibrationRecordBtnColored = True
   self.ui.pushButton_CalibRecordStop.setStyleSheet("background-color: #f94c57;")

 #----------------------------------------------
 def vFCALIBRATIONStopRecording( self ):
  print("-- vFCALIBRATIONStopRecording --")
  self.bLiveviewRecordBtnColored = False
  self.ui.pushButton_CalibRecordStop.setStyleSheet("")
  self.ui.pushButton_CalibRecordStop.setVisible(False)
  self.ui.pushButton_CalibRecord.setVisible(True)
  # Arrêt du timer
  self.timerCALRecording.stop()

 #----------------------------------------------
 def vFCALIBRATION_ECCalValueChange( self ):
  print("-- vFCALIBRATION_ECCalValueChange --")
  # Si en mode User
  if( self.ui.comboBox_ECCalValue_Point.currentText() == "User"     ):
   self.ui.widget_ECCalValue_Point_2.setVisible(True)
   self.ui.widget_ECCalValue_Point_3.setVisible(False)
  # RapidCal
  elif( self.ui.comboBox_ECCalValue_Point.currentText() == "RapidCal" ):
   self.ui.widget_ECCalValue_Point_2.setVisible(False)
   self.ui.widget_ECCalValue_Point_3.setVisible(True)
   self.ui.spinBox_ECCalValue_2_Point_2.setValue(2570)
  # SC-35
  else:
   # Modification Calibration cal value
   self.ui.widget_ECCalValue_Point_2.setVisible(False)
   self.ui.widget_ECCalValue_Point_3.setVisible(True)
   self.ui.spinBox_ECCalValue_2_Point_2.setValue(53065)

