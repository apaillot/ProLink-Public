# This Python file uses the following encoding: utf-8

#============================================================================#
# Librairies système
#============================================================================#
import sys

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
from Vue.VLib           import *
from Vue.py_toggle      import PyToggle
# Sonde
from Vue.Windows.Dashboard.UIClearSondeMemory      import UIClearSondeMemory
from Vue.Windows.Dashboard.UINewBatteriesFitted    import UINewBatteriesFitted
from Vue.Windows.Dashboard.UIUpdateClockWithPC     import UIUpdateClockWithPC
from Vue.Windows.Dashboard.UISondeDate             import UISondeDate
from Vue.Windows.Dashboard.UISondeTime             import UISondeTime
from Vue.Windows.Dashboard.UISiteLatitude          import UISiteLatitude
from Vue.Windows.Dashboard.UISiteLongitude         import UISiteLongitude
from Vue.Windows.Dashboard.UIChannelSelect         import UIChannelSelect
from Vue.Windows.Dashboard.UILogDataEvery          import UILogDataEvery
from Vue.Windows.Dashboard.UICleanEvery            import UICleanEvery
from Vue.Windows.Dashboard.UISiteID                import UISiteID
from Vue.Windows.Dashboard.UISetupLoggingState     import UISetupLoggingState
from Vue.Windows.Dashboard.UISetupLoggingCheck     import UISetupLoggingCheck
from Vue.Windows.Dashboard.UISetupLoggingEvery     import UISetupLoggingEvery
from Vue.Windows.Dashboard.UISetupLoggingThreshold import UISetupLoggingThreshold
from Vue.Windows.Dashboard.UIOpticalAvg            import UIOpticalAvg
from Vue.Windows.Calibration.UICalibRestore        import UICalibRestore

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
class VSonde(QObject):
 #-- Dashboard
 # Signal de fin d'init de la vue
 xDashboardChannelSelectConnectSignal  = Signal( int, dict, QWidget )
 #-- Liveview
 # Liveview - Click sur box mesure
 siLiveviewClickBox = Signal(str, QWidget, QWidget, int)
 #-- Calibration
 # Signal de fin d'init de la vignette
 xCalibrationSensorSelectConnectSignal = Signal( str, int, dict, QWidget, dict )
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
  print("VSonde init")
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
  self.tUIClearSondeMemory      = UIClearSondeMemory( tParent )
  self.tUINewBatteriesFitted    = UINewBatteriesFitted( tParent )
  self.tUIUpdateClockWithPC     = UIUpdateClockWithPC( tParent )
  self.tUISondeDate             = UISondeDate( tParent )
  self.tUISondeTime             = UISondeTime( tParent )
  self.tUISiteID                = UISiteID( tParent )
  self.tUISiteLatitude          = UISiteLatitude( tParent )
  self.tUISiteLongitude         = UISiteLongitude( tParent )
  self.tUIChannelSelect         = UIChannelSelect( tParent )
  self.tUILogDataEvery          = UILogDataEvery( tParent )
  self.tUICleanEvery            = UICleanEvery( tParent )
  self.tUISetupLoggingState     = UISetupLoggingState( tParent )
  self.tUISetupLoggingCheck     = UISetupLoggingCheck( tParent )
  self.tUISetupLoggingEvery     = UISetupLoggingEvery( tParent )
  self.tUISetupLoggingThreshold = UISetupLoggingThreshold( tParent )
  self.tUIOpticalAvg            = UIOpticalAvg( tParent )
  # Calibration
  self.tUICalibRestore          = UICalibRestore( tParent )
  # Timer pour bouton clignotte enregistrement liveview
  self.timerLVRecording  = QTimer(self)
  self.timerLVRecording.timeout.connect( self.vFLiveviewRecordingOccuringTimeout )
  self.timerCALRecording = QTimer(self)
  self.timerCALRecording.timeout.connect( self.vFCALIBRATIONRecordingOccuringTimeout )

 #----------------------------------------------
 # Affichage des onglets
 #----------------------------------------------
 def vFDisplayProductNavInit( self ):
  #self.ui.connexion_btn.setVisible(False)
  self.ui.dashboard_btn.setVisible(False)
  self.ui.liveview_btn.setVisible(False)
  self.ui.data_btn.setVisible(False)
  self.ui.calibration_btn.setVisible(False)
  self.ui.pcConfig_btn.setVisible(False)

 #----------------------------------------------
 # Affichage des onglets
 #----------------------------------------------
 def vFDisplayProductNav( self ):
  #self.ui.connexion_btn.setVisible(False)
  self.ui.dashboard_btn.setVisible(True)
  self.ui.liveview_btn.setVisible(True)
  self.ui.data_btn.setVisible(True)
  self.ui.calibration_btn.setVisible(True)
  self.ui.pcConfig_btn.setVisible(True)

 #----------------------------------------------
 # NAV - Gestion menu bouton nav
 #----------------------------------------------
 def vFNavASBtnClicked( self, uiIndex ):
  print("-- VSonde > vFNavASBtnClicked --")
  tBtnNav = [
   self.ui.connexion_btn,
   self.ui.dashboard_btn,
   self.ui.liveview_btn,
   self.ui.data_btn,
   self.ui.calibration_btn,
   self.ui.about_btn,
   self.ui.pcConfig_btn
  ]
  # Si on est en mode liveview activé
  if(   ( self.ui.stackedWidget.currentIndex() == 2 )
    and ( self.ui.stopMeasure_btn.isVisible() ) ):
   print("bloque")
   vFAlert(self.tParent, "Warning", "Please stop liveview to change tab")
   # On quitte pour bloquer
   return

  # Si on est en mode calibration en cours
  if( self.ui.stackedWidget_calibrationMain.currentIndex() == 1 ):
   print("bloque")
   vFAlert(self.tParent, "Warning", "Please stop current calibration to change tab")
   # On quitte pour bloquer
   return

  # Modification page affichée
  self.ui.stackedWidget.setCurrentIndex(uiIndex)
  self.ui.stackedWidget_Nav2.setCurrentIndex(uiIndex)
  # Gestion de la ligne blanche gauche du bouton nav active
  for uiCpt in range(len(tBtnNav)):
   if( tBtnNav[uiCpt] == None ): continue
   if( uiCpt == uiIndex ):
    tBtnNav[uiCpt].setStyleSheet("background-color: #3E4072;border-left: 3px solid rgb(255,255,255);");
   else:
    tBtnNav[uiCpt].setStyleSheet("");
  # Conservation de l'onglet actif
  self.uiNavActivePage = uiIndex

 #----------------------------------------------
 # Init du mode lecture sonde
 #----------------------------------------------
 def vFVSondeInitMode( self ):
  # Affichage spécifique sonde
  self.ui.widget_SondeInfoInterface.setVisible(True)
  self.ui.groupBox_EstimatedLogLife.setVisible(True)
  self.ui.groupBox_SondeClock.setVisible(True)
  self.ui.groupBox_Averaging.setVisible(True)
  self.ui.widget_DashboardNavBtn.setVisible(True)
  self.ui.getMeasureData_btn.setVisible(True)
  # Data
  self.ui.exportToRAW_btn.setVisible(True)
  # Conf box
  self.ui.groupBox_PCConf_AppSettings.setVisible(True)
  self.ui.groupBox_PCConf_Measure.setVisible(True)
  # Dashboard - Couleur au survol des lignes modifiables
  self.ui.groupBox_SondeClock.setStyleSheet("#groupBox_SondeClock > QWidget:hover{background-color: #efefef;}")
  self.ui.groupBox_SiteIDLocation.setStyleSheet("#groupBox_SiteIDLocation > QWidget:hover{background-color: #efefef;}")
  self.ui.groupBox_SetupLogRate.setStyleSheet("#groupBox_SetupLogRate > QWidget:hover{background-color: #efefef;}")
  self.ui.groupBox_EventLogging.setStyleSheet("#groupBox_EventLogging > QWidget:hover{background-color: #efefef;}")
  self.ui.widget_OpticalAveraging.setStyleSheet("#widget_OpticalAveraging:hover{background-color: #efefef;}")
  # Dashboard - Modification du logo modification
  self.ui.label_setSiteID.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version.svg") )
  self.ui.label_setSiteLatitude.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version.svg") )
  self.ui.label_setSiteLong.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version.svg") )
  self.ui.label_setLogDataEvery.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version.svg") )
  self.ui.label_setCleanEvery.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version.svg") )
  self.ui.label_setEventLogState.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version.svg") )
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
  # Suppression inutile
  #-----------------
  # Si AS-6K/7K/Pro
  #if( uiProductID == 29 ):
  if( ttConfig["PRODUCT"]["uiModel"] == 29 ):
   # Balayage
   self.ui.widget_CleanEvery.setVisible(True)
   self.ui.cleanSonde_btn.setVisible(True)
  # Si sonde AS-2000 ou AS-5000
  else:
   # Pas de balayage
   self.ui.widget_CleanEvery.setVisible(False)
   self.ui.cleanSonde_btn.setVisible(False)

  #-----------------
  # Dashboard
  #-----------------
  # Sonde info
  self.ui.label_Model.setText( str(ttConfig["PRODUCT"]["sModel"]) )
  self.ui.label_SerialNo.setText( str(ttConfig["PRODUCT"]["sPSN1"]) )
  self.ui.label_InterfaceCom.setText( str(sCom) )
  self.ui.label_SWRev.setText( str(ttConfig["PRODUCT"]["sPSW1"]) )
  self.ui.label_RecordsStored.setText( str(ttConfig["PRODUCT"]["uiMemRecords"]) )
  self.ui.label_MemoryRemaining.setText( str(ttConfig["PRODUCT"]["uiMemRemaining"]) )
  self.ui.label_BatteryRemaining.setText( str(ttConfig["PRODUCT"]["uiBATT_PC"])+" %" )
  self.ui.label_BatteryVoltage.setText( str("%.2f"%ttConfig["PRODUCT"]["fBATT"])+" V" )
  # Sonde clock
  self.ui.label_sondeClockDate.setText( str(ttConfig["PRODUCT"]["sRTCDate"]) )
  self.ui.label_sondeClockTime.setText( str(ttConfig["PRODUCT"]["sRTCTime"]) )
  # Site ID and location
  self.ui.label_SiteID.setText( str(ttConfig["PRODUCT"]["sSiteID"]) )
  self.ui.label_SiteLat.setText( str(ttConfig["PRODUCT"]["sSiteLat"]) )
  self.ui.label_SiteLong.setText( str(ttConfig["PRODUCT"]["sSiteLong"]) )
  # Setup logging rate
  sLogDataRate = ("%u"%ttConfig["PRODUCT"]["uiLOG_HOUR"]) + "h" + ("%u"%ttConfig["PRODUCT"]["uiLOG_MIN"]) + "m" + ("%u"%ttConfig["PRODUCT"]["uiLOG_SEC"])
  self.ui.label_LogDataEvery.setText(sLogDataRate)
  self.ui.label_CleanEvery.setText( str(ttConfig["PRODUCT"]["uiCLEAN_HR"])+" hours" )
  # Estimated log life
  self.ui.label_UntilMemFull.setText( str(ttConfig["PRODUCT"]["uiMemFullDay"])+" days" )
  self.ui.label_UntilBattDead.setText( str(ttConfig["PRODUCT"]["uiBattDeadDay"])+" days" )
  # Event logging
  if( ttConfig["PRODUCT"]["uiLOG_EVENT"] == 1 ):
   self.ui.label_EventLogState.setText( "Enable" )
   self.ui.label_logoEventLogCheck.setPixmap( QPixmap(":/Logo/Dashboard/7-Event-logging/2-Check.svg") )
   self.ui.label_txtEventLogCheck.setStyleSheet("color: #000000;")
   self.ui.label_EventLogCheck.setStyleSheet("color: rgb(84,84,84);")
   self.ui.label_setEventLogCheck.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version.svg") )
   self.ui.label_logoEventLogEvery.setPixmap( QPixmap(":/Logo/Dashboard/7-Event-logging/3-Every.svg") )
   self.ui.label_txtEventLogEvery.setStyleSheet("color: #000000;")
   self.ui.label_EventLogEvery.setStyleSheet("color: rgb(84,84,84);")
   self.ui.label_setEventLogEvery.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version.svg") )
   self.ui.label_logoEventLogThreshold.setPixmap( QPixmap(":/Logo/Dashboard/7-Event-logging/4-Log-data-if.svg") )
   self.ui.label_txtEventLogThreshold.setStyleSheet("color: #000000;")
   self.ui.label_EventLogThreshold.setStyleSheet("color: rgb(84,84,84);")
   self.ui.label_setEventLogThreshold.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version.svg") )
  else:
   self.ui.label_EventLogState.setText( "Disable" )
   self.ui.label_logoEventLogCheck.setPixmap( QPixmap(":/Logo/Dashboard/7-Event-logging/2-Check-grey.svg") )
   self.ui.label_txtEventLogCheck.setStyleSheet("color: #888888;")
   self.ui.label_EventLogCheck.setStyleSheet("color: #888888;")
   self.ui.label_setEventLogCheck.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version-grey.svg") )
   self.ui.label_logoEventLogEvery.setPixmap( QPixmap(":/Logo/Dashboard/7-Event-logging/3-Every-grey.svg") )
   self.ui.label_txtEventLogEvery.setStyleSheet("color: #888888;")
   self.ui.label_EventLogEvery.setStyleSheet("color: #888888;")
   self.ui.label_setEventLogEvery.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version-grey.svg") )
   self.ui.label_logoEventLogThreshold.setPixmap( QPixmap(":/Logo/Dashboard/7-Event-logging/4-Log-data-if-grey.svg") )
   self.ui.label_txtEventLogThreshold.setStyleSheet("color: #888888;")
   self.ui.label_EventLogThreshold.setStyleSheet("color: #888888;")
   self.ui.label_setEventLogThreshold.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version-grey.svg") )
  self.ui.label_EventLogCheck.setText( str(ttConfig["PRODUCT"]["sLOG_SENSOR"]) )
  self.ui.label_EventLogEvery.setText( str(ttConfig["PRODUCT"]["uiEVENT_HOUR"])+"h "+str(ttConfig["PRODUCT"]["uiEVENT_MIN"])+"min" )
  self.ui.label_EventLogThreshold.setText( str(ttConfig["PRODUCT"]["uiEVENT_CHANGE"])+" %" )
  # Si version >= 5.11
  if( ttConfig["PRODUCT"]["uiPSW"] >= 511 ):
   # Optical sensor averaging
   self.ui.label_AveragingValue.setText( str(ttConfig["PRODUCT"]["uiOpticalAvg"]) )
   self.ui.groupBox_Averaging.setVisible(True)
  else:
   # Optical sensor averaging
   self.ui.groupBox_Averaging.setVisible(False)
  # Clear du layout dashboard sensor list
  for i in reversed(range(self.ui.groupBox_DashboardSensors.layout().count())):
   self.ui.groupBox_DashboardSensors.layout().itemAt(i).widget().deleteLater()
  # pH / ORP
  self.vFDashboardAddpHORPLine()
  # DO / EC
  self.vFDashboardAddDoEcLine()
  # Test fonction ajout de capteur
  print('ttConfig["PRODUCT"]["uiAUXNumber"] = %d' % ttConfig["PRODUCT"]["uiAUXNumber"])
  # Selon le type de sonde
  if( ttConfig["PRODUCT"]["uiAUXNumber"] >= 1 ):
   self.vFDashboardAddSensorsLine( 0, ttConfig["SENSOR"]["AUX1"] )
  if( ttConfig["PRODUCT"]["uiAUXNumber"] >= 2 ):
   self.vFDashboardAddSensorsLine( 1, ttConfig["SENSOR"]["AUX2"] )
  if( ttConfig["PRODUCT"]["uiAUXNumber"] >= 3 ):
   self.vFDashboardAddSensorsLine( 2, ttConfig["SENSOR"]["AUX3"] )
  if( ttConfig["PRODUCT"]["uiAUXNumber"] >= 4 ):
   self.vFDashboardAddSensorsLine( 3, ttConfig["SENSOR"]["AUX4"] )
  if( ttConfig["PRODUCT"]["uiAUXNumber"] >= 5 ):
   self.vFDashboardAddSensorsLine( 4, ttConfig["SENSOR"]["AUX5"] )
  if( ttConfig["PRODUCT"]["uiAUXNumber"] >= 6 ):
   self.vFDashboardAddSensorsLine( 5, ttConfig["SENSOR"]["AUX6"] )

  #-----------------
  # Liveview
  #-----------------
   # Liste des capteurs
  tListSensor = ["TEMP", "Depth", "Baro", "PH",
  "PHmv", "ORP",  "DO Sat", "DO",   "EC",
  "AUX1", "AUX2", "AUX3", "AUX4", "AUX5", "AUX6"]
  self.tListSensor = tListSensor
  # Nettoyage zone vignette valeur physique
  for i in reversed(range(self.ui.widget_11.layout().count())):
   self.ui.widget_11.layout().itemAt(i).widget().deleteLater()
  # On compte le nombre d'item
  ucItemNb = 0
  for ucCpt in range( len( tListSensor ) ):
   sIndex = tListSensor[ucCpt]
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
   self.vFLiveviewDisplayBloc( ttConfig["SENSOR"][sIndex],
                               ( ucCptItem % int( int( ucItemNb / 2 ) + 1 ) ),
                               ( ucCptItem / int( int( ucItemNb / 2 ) + 1 ) ),
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

  # Ammonia affichage ou pas
  if( ttConfig["CALCULATED"]["AMMONIA"]["bActivated"] ):
   # Affichage
   self.ui.widget_LVCalculatedAmmonia.setVisible(True)
  else:
   self.ui.widget_LVCalculatedAmmonia.setVisible(False)

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

  self.tCalibNavSensorWidget = {}
  #
  self.tCalibNavSensorWidget[ "PH" ]  = self.vFCALIBRATIONAddCalibNavElt( "PH",  uiFGetIDWithChannelNameWith("pH"),  ttConfig["SENSOR"]["PH"], ttConfig )
  self.tCalibNavSensorWidget[ "ORP" ] = self.vFCALIBRATIONAddCalibNavElt( "ORP", uiFGetIDWithChannelNameWith("ORP"), ttConfig["SENSOR"]["ORP"], ttConfig )
  self.tCalibNavSensorWidget[ "DO" ]  = self.vFCALIBRATIONAddCalibNavElt( "DO",  uiFGetIDWithChannelNameWith("DO"),  ttConfig["SENSOR"]["DO"], ttConfig )
  self.tCalibNavSensorWidget[ "EC" ]  = self.vFCALIBRATIONAddCalibNavElt( "EC",  uiFGetIDWithChannelNameWith("EC"),  ttConfig["SENSOR"]["EC"], ttConfig )

  # Selon le type de sonde
  if( ttConfig["PRODUCT"]["uiAUXNumber"] >= 1 ):
   self.tCalibNavSensorWidget[ "AUX1" ] = self.vFCALIBRATIONAddCalibNavElt( "AUX1", 0, ttConfig["SENSOR"]["AUX1"], ttConfig )
  if( ttConfig["PRODUCT"]["uiAUXNumber"] >= 2 ):
   self.tCalibNavSensorWidget[ "AUX2" ] = self.vFCALIBRATIONAddCalibNavElt( "AUX2", 1, ttConfig["SENSOR"]["AUX2"], ttConfig )
  if( ttConfig["PRODUCT"]["uiAUXNumber"] >= 3 ):
   self.tCalibNavSensorWidget[ "AUX3" ] = self.vFCALIBRATIONAddCalibNavElt( "AUX3", 2, ttConfig["SENSOR"]["AUX3"], ttConfig )
  if( ttConfig["PRODUCT"]["uiAUXNumber"] >= 4 ):
   self.tCalibNavSensorWidget[ "AUX4" ] = self.vFCALIBRATIONAddCalibNavElt( "AUX4", 3, ttConfig["SENSOR"]["AUX4"], ttConfig )
  if( ttConfig["PRODUCT"]["uiAUXNumber"] >= 5 ):
   self.tCalibNavSensorWidget[ "AUX5" ] = self.vFCALIBRATIONAddCalibNavElt( "AUX5", 4, ttConfig["SENSOR"]["AUX5"], ttConfig )
  if( ttConfig["PRODUCT"]["uiAUXNumber"] >= 6 ):
   self.tCalibNavSensorWidget[ "AUX6" ] = self.vFCALIBRATIONAddCalibNavElt( "AUX6", 5, ttConfig["SENSOR"]["AUX6"], ttConfig )

  # Seulement quand en connexion : non ! sinon pas de refresh des datas en live
  if( self.ui.stackedWidget.currentIndex() == 0 ):
   self.vFCALIBRATIONSensorNavSelectionDynamic("PH",
                                               uiFGetIDWithChannelNameWith("pH"),
                                               ttConfig["SENSOR"]["PH"],
                                               self.tCalibNavSensorWidget["PH"],
                                               ttConfig )
   # Ouverture de l'onglet dashboard
   self.vFNavASBtnClicked(1)
  ##TODO - Prévoir une resélection de l'onglet courant si pas sur connexion
  else:
   self.vFCALIBRATIONSensorNavSelectionDynamic( self.tCalibrationCurrentSensor["sConfigName"],
                                                self.tCalibrationCurrentSensor["ucChannel"],
                                                ttConfig["SENSOR"][self.tCalibrationCurrentSensor["sConfigName"]],
                                                self.tCalibNavSensorWidget[self.tCalibrationCurrentSensor["sConfigName"]],
                                                ttConfig )

  #-------------------------------------------
  # Data
  #-------------------------------------------
  #-------------------------------------------
  # PC Configuration
  #-------------------------------------------


 #----------------------------------------------
 # Dashboard - Création voie pH / ORP
 #----------------------------------------------
 def vFDashboardAddpHORPLine( self ):
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
  pixmap = QPixmap( "://Logo/Sensor/SVG/pH ORP - Copie.svg" )
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
  tLabel.setText( "pH / ORP" )
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
  self.ui.groupBox_DashboardSensors.layout().addWidget(tWidget)

 #----------------------------------------------
 # Dashboard - Création voie DO / EC
 #----------------------------------------------
 def vFDashboardAddDoEcLine( self ):
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
  pixmap = QPixmap( "://Logo/Sensor/SVG/EC DO - Copie.svg" )
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
  tLabel.setText( "DO / EC" )
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
  self.ui.groupBox_DashboardSensors.layout().addWidget(tWidget)

 #----------------------------------------------
 # Dashboard - Affichage dashboard voie sensor
 #----------------------------------------------
 def vFDashboardAddSensorsLine( self, ucChannel, tChannel ):
  #
  #self.ui.groupBox_DashboardSensors
  tWidget = QWidget()
  tWidget.setContentsMargins(0,0,0,0)
  tWidget.setStyleSheet("*:hover{background-color: #efefef;}")
  # Create a boxlayout (horizontal here)
  tBox = QHBoxLayout()
  tBox.setContentsMargins(9,5,9,5)
  # Set the layout for your tab
  tWidget.setLayout(tBox)
  # Logo
  tLogoLabel = QLabel()
  pixmap = QPixmap( self.sFGetSensorLogoWithID( tChannel["uiIndex"], "" ) )
  tLogoLabel.setPixmap(pixmap)
  tLogoLabel.setScaledContents(True)
  tLogoLabel.setMaximumSize(20, 20)
  tWidget.layout().addWidget(tLogoLabel)
  # Numero de la voie
  tLabel = QLabel()
  # Si voie fixed
  if( ucChannel < 0 ): tLabel.setText("FIXED:")
  else:                tLabel.setText("AUX"+str(int(ucChannel)+1)+":")
  if( tChannel["sIndex"] == "EMPTY" ): tLabel.setStyleSheet("color: #888888")
  else:                                tLabel.setStyleSheet("color: rgb(84,84,84);")
  tWidget.layout().addWidget(tLabel)
  # Nom de la voie
  tLabel = QLabel()
  tLabel.setText( tChannel["sIndex"] )
  if( tChannel["sIndex"] == "EMPTY" ): tLabel.setStyleSheet("color: #888888")
  else:                                tLabel.setStyleSheet("color: rgb(84,84,84);")
  tWidget.layout().addWidget(tLabel)
  # Logo
  tLogoLabel = QLabel()
  if( ucChannel < 0 ): pixmap = QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version.svg - W")
  else:
   if( tChannel["sIndex"] == "EMPTY" ): pixmap = QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version-grey.svg")
   else:                                pixmap = QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version.svg")

  tLogoLabel.setPixmap(pixmap)
  tLogoLabel.setScaledContents(True)
  tLogoLabel.setMaximumSize(20, 20)
  tWidget.layout().addWidget(tLogoLabel)
  # Ajout d'un widget dans un widget en utilisant son layout interne
  self.ui.groupBox_DashboardSensors.layout().addWidget(tWidget)
  # Ajout de l'event sur ligne
  self.xDashboardChannelSelectConnectSignal.emit( ucChannel, tChannel, tWidget )

 #-------------------------------------
 # Nom de la voie selon l'ID
 #-------------------------------------
 def sFGetSensorLogoWithID( self, uiAUXAssign, sColor ):
  print("== sFGetSensorLogoWithID ==")

  if( sColor == "white" ): sSVG = "SVG_blanc"
  else:                    sSVG = "SVG"

  sSvgPath = ":/Logo/Sensor/"+sSVG+"/EC DO.svg"

  if( uiAUXAssign == 0 ):  sSvgPath = "EMPTY"
  # FIXED
  if( uiAUXAssign == -1 ):  sSvgPath = "://Logo/Sensor/"+sSVG+"/F01_Temperature.svg"
  if( uiAUXAssign == -2 ):  sSvgPath = "://Logo/Sensor/"+sSVG+"/F02_Conductivity.svg"
  if( uiAUXAssign == -3 ):  sSvgPath = "://Logo/Sensor/"+sSVG+"/F03_DO.svg"
  if( uiAUXAssign == -4 ):  sSvgPath = "://Logo/Sensor/"+sSVG+"/F04_DO.svg"
  if( uiAUXAssign == -5 ):  sSvgPath = "://Logo/Sensor/"+sSVG+"/F05_pH.svg"
  if( uiAUXAssign == -6 ):  sSvgPath = "://Logo/Sensor/"+sSVG+"/F06_pH.svg"
  if( uiAUXAssign == -7 ):  sSvgPath = "://Logo/Sensor/"+sSVG+"/F07_ORP.svg"
  if( uiAUXAssign == -8 ):  sSvgPath = "://Logo/Sensor/"+sSVG+"/F08_Pressure.svg"
  if( uiAUXAssign == -9 ):  sSvgPath = "://Logo/Sensor/"+sSVG+"/F09_Baro.svg"
  # AUX
  if( uiAUXAssign == 1 ):  sSvgPath = "://Logo/Sensor/"+sSVG+"/A01_Ammonium_NH4.svg"
  if( uiAUXAssign == 2 ):  sSvgPath = "://Logo/Sensor/"+sSVG+"/A02_Chloride_Cl-.svg"
  if( uiAUXAssign == 3 ):  sSvgPath = "://Logo/Sensor/"+sSVG+"/A03_Fluoride_F.svg"
  if( uiAUXAssign == 4 ):  sSvgPath = "://Logo/Sensor/"+sSVG+"/A04_Nitrate_NO-.svg"
  if( uiAUXAssign == 5 ):  sSvgPath = "://Logo/Sensor/"+sSVG+"/A05_Calcium_Ca2.svg"
  if( uiAUXAssign == 16 ): sSvgPath = "://Logo/Sensor/"+sSVG+"/A16_Turbidity.svg"
  if( uiAUXAssign == 17 ): sSvgPath = "://Logo/Sensor/"+sSVG+"/A17_Chl-a.svg"
  if( uiAUXAssign == 18 ): sSvgPath = "://Logo/Sensor/"+sSVG+"/A18_PC.svg"
  if( uiAUXAssign == 19 ): sSvgPath = "://Logo/Sensor/"+sSVG+"/A19_PE.svg"
  if( uiAUXAssign == 20 ): sSvgPath = "://Logo/Sensor/"+sSVG+"/A20_RHODd.svg"
  if( uiAUXAssign == 21 ): sSvgPath = "://Logo/Sensor/"+sSVG+"/A21_FSCEIN.svg"
  if( uiAUXAssign == 22 ): sSvgPath = "://Logo/Sensor/"+sSVG+"/A22_Ref_Oil.svg"
  if( uiAUXAssign == 23 ): sSvgPath = "://Logo/Sensor/"+sSVG+"/A23_CDOM.svg"
  if( uiAUXAssign == 24 ): sSvgPath = "://Logo/Sensor/"+sSVG+"/A24_Crude_oil.svg"
  if( uiAUXAssign == 25 ): sSvgPath = "://Logo/Sensor/"+sSVG+"/A25_Trypto.svg"
  if( uiAUXAssign == 254 ): sSvgPath = "://Logo/Sensor/"+sSVG+"/A01_Ammonium_NH4.svg"
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
  if( uiAUXAssign == -3 ):  sColor = "#193D8B" # DO
  if( uiAUXAssign == -4 ):  sColor = "#193D8B" # DO sat
  if( uiAUXAssign == -5 ):  sColor = "#FFB200" # PH
  if( uiAUXAssign == -6 ):  sColor = "#FFB200" # PH mv
  if( uiAUXAssign == -7 ):  sColor = "#8EA9DB" # ORP
  if( uiAUXAssign == -8 ):  sColor = "#AFC0E1" # Depth
  if( uiAUXAssign == -9 ):  sColor = "#03A9F2" # Baro
  # AUX
  if( uiAUXAssign == 1 ):  sColor = "#1A4973" # Ammonium
  if( uiAUXAssign == 2 ):  sColor = "#BABABA" # Chloride
  if( uiAUXAssign == 3 ):  sColor = "#F5FF2F" # Fluoride
  if( uiAUXAssign == 4 ):  sColor = "#70AD47" # Nitrate
  if( uiAUXAssign == 5 ):  sColor = "#E20020" # Calcium
  if( uiAUXAssign == 16 ): sColor = "#038B99" # Turbidity
  if( uiAUXAssign == 17 ): sColor = "#8BC24A" # Chlorophyle
  if( uiAUXAssign == 18 ): sColor = "#285C8D" # BGA-PC
  if( uiAUXAssign == 19 ): sColor = "#9D0015" # BGA-PE
  if( uiAUXAssign == 20 ): sColor = "#AD3EC0" # Rhodamine
  if( uiAUXAssign == 21 ): sColor = "#FFD966" # Fluorescein
  if( uiAUXAssign == 22 ): sColor = "#806000" # Refined Oil
  if( uiAUXAssign == 23 ): sColor = "#a2cf61" # CDOM
  if( uiAUXAssign == 24 ): sColor = "#3A2B00" # Crude Oil
  if( uiAUXAssign == 25 ): sColor = "#40591B" # Tryptophan
  if( uiAUXAssign == 254 ): sColor = "#40591B" # Ammonia
  # Retour de la couleur
  return( sColor )

 #-------------------------------------
 # Couleur de la voie selon l'ID
 #-------------------------------------
 def sFGetSensorColorWithGraphLabel( self, sLabel ):
  #print("== sFGetSensorColorWithGraphLabel ==")
  #print(sLabel)
  #sColor = "#555555"

  # FIXED
  if( sLabel == "Batt"      ): sColor = "#555555" # VBatt
  if( sLabel == "Temp C"    ): sColor = "#F34333" # Temperature
  if( sLabel == "Temp F"    ): sColor = "#F34333" # Temperature
  if( sLabel == "Depth m"   ): sColor = "#AFC0E1" # Depth m
  if( sLabel == "Depth f"   ): sColor = "#AFC0E1" # Depth f
  if( sLabel == "Baro"      ): sColor = "#03A9F2" # Baro
  if( sLabel == "pH"        ): sColor = "#FFB200" # PH
  if( sLabel == "pH (mV)"   ): sColor = "#FFB200" # PH mv
  if( sLabel == "ORP"       ): sColor = "#8EA9DB" # ORP
  if( sLabel == "DO (%sat)" ): sColor = "#193D8B" # DO sat
  if( sLabel == "DO"        ): sColor = "#193D8B" # DO
  if( sLabel == "EC"        ): sColor = "#1E847A" # EC
  # AUX
  if( sLabel == "EMPTY"       ): sColor = "#555555" # EMPTY
  if( sLabel == "Ammonium"    ): sColor = "#1A4973" # Ammonium
  if( sLabel == "Chloride"    ): sColor = "#BABABA" # Chloride
  if( sLabel == "Fluoride"    ): sColor = "#F5FF2F" # Fluoride
  if( sLabel == "Nitrate"     ): sColor = "#70AD47" # Nitrate
  if( sLabel == "Calcium"     ): sColor = "#E20020" # Calcium
  if( sLabel == "Turbidity"   ): sColor = "#038B99" # Turbidity
  if( sLabel == "Chlorophyll" ): sColor = "#8BC24A" # Chlorophyle
  if( sLabel == "BGA-PC"      ): sColor = "#285C8D" # BGA-PC
  if( sLabel == "BGA-PE"      ): sColor = "#9D0015" # BGA-PE
  if( sLabel == "Rhodamine"   ): sColor = "#AD3EC0" # Rhodamine
  if( sLabel == "Fluorescein" ): sColor = "#FFD966" # Fluorescein
  if( sLabel == "Refined Oil" ): sColor = "#806000" # Refined Oil
  if( sLabel == "CDOM"        ): sColor = "#a2cf61" # CDOM
  if( sLabel == "Crude Oil"   ): sColor = "#3A2B00" # Crude Oil
  if( sLabel == "Tryptophan"  ): sColor = "#40591B" # Tryptophan
  if( sLabel == "Salinity"    ): sColor = "#B2BEB5" # Salinity
  if( sLabel == "TDS"         ): sColor = "#7393B3" # TDS
  if( sLabel == "SSG"         ): sColor = "#36454F" # SSG
  if( sLabel == "Ammonia"     ): sColor = "#36454F" # Ammonia
  # Retour de la couleur
  return( sColor )

 #----------------------------------------------
 # Dashboard - Affichage windows Sonde date
 #----------------------------------------------
 def vFDashboardSondeDateOpen( self, event ):
  print("-- vFDashboardSondeDateOpen --")
  # Récupération de la valeur du champs
  sSondeDate = self.ui.label_sondeClockDate.text()
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
  sSondeTime = self.ui.label_sondeClockTime.text()
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
  sSiteID = self.ui.label_SiteID.text()
  # Ouverture de la fenêtre
  self.tUISiteID.vFOpen( sSiteID )

 #----------------------------------------------
 # Dashboard - Affichage windows site Latitude
 #----------------------------------------------
 def vFDashboardSiteLatitudeOpen( self, event ):
  print("-- vFDashboardSiteIDLatitude --")
  #
  sSiteLatitude = self.ui.label_SiteLat.text()
  # Extraction
  sRef  = str( sSiteLatitude.split(" ")[0] )
  sTxt2 = sSiteLatitude.split(" ")[1]
  uiDeg = int(sTxt2.split("°")[0])
  fMin  = float((sTxt2.split("°")[1]).split("'")[0])
  # Ouverture de la fenêtre
  self.tUISiteLatitude.vFOpen( sRef, uiDeg, fMin )

 #----------------------------------------------
 # Dashboard - Affichage windows site Longitude
 #----------------------------------------------
 def vFDashboardSiteLongitudeOpen( self, event ):
  print("-- vFDashboardSiteIDLongitude --")
  #
  sSiteLongitude = self.ui.label_SiteLong.text()
  # Extraction
  sRef  = str( sSiteLongitude.split(" ")[0] )
  sTxt2 = sSiteLongitude.split(" ")[1]
  uiDeg = int(sTxt2.split("°")[0])
  fMin  = float((sTxt2.split("°")[1]).split("'")[0])
  # Ouverture de la fenêtre
  self.tUISiteLongitude.vFOpen( sRef, uiDeg, fMin )

 #----------------------------------------------
 # Dashboard - Affichage windows channel select
 #----------------------------------------------
 def vFDashboardChannelSelectOpen( self, ucChannel, tChannel, tWidget ):
  print("-- vFDashboardChannelSelectOpen --")
  print("ucChannel = %d"%ucChannel)
  # Ouverture de la fenêtre
  self.tUIChannelSelect.vFOpen( ucChannel, tChannel, tWidget )

 #----------------------------------------------
 # Dashboard - Affichage configuration
 #----------------------------------------------
 def vFDashboardLogDataEveryOpen( self, event ):
  print("-- vFDashboardLogDataEveryOpen --")
  # Récupération valeur
  sLogDataPeriod = self.ui.label_LogDataEvery.text()
  uiLogDataHour = int( sLogDataPeriod.split("h")[0] )
  uiLogDataMin  = int( sLogDataPeriod.split("h")[1].split("m")[0] )
  uiLogDataSec  = int( sLogDataPeriod.split("h")[1].split("m")[1] )
  self.tUILogDataEvery.vFOpen( uiLogDataHour, uiLogDataMin, uiLogDataSec )

 #----------------------------------------------
 # Dashboard - Affichage windows clean every
 #----------------------------------------------
 def vFDashboardCleanEveryOpen( self, event ):
  print("-- vFDashboardCleanEveryOpen --")
  # Récupération valeur
  sLogDataPeriod = self.ui.label_CleanEvery.text()
  # Extraction
  uiLogDataHour = int( sLogDataPeriod.split(" ")[0] )
  self.tUICleanEvery.vFOpen( uiLogDataHour )

 #----------------------------------------------
 # Dashboard - Affichage windows setup logging state
 #----------------------------------------------
 def vFDashboardSetupLoggingStateOpen( self, event ):
  print("-- vFDashboardSetupLoggingState --")
  # Récupération valeur
  sActivation = self.ui.label_EventLogState.text()
  self.tUISetupLoggingState.vFOpen( sActivation )

 #----------------------------------------------
 # Dashboard - Affichage windows setup logging check
 #----------------------------------------------
 def vFDashboardSetupLoggingCheckOpen( self, event ):
  print("-- vFDashboardSetupLoggingCheck --")
  # Récupération valeur
  sParameter = self.ui.label_EventLogCheck.text()
  self.tUISetupLoggingCheck.vFOpen( sParameter )

 #----------------------------------------------
 #Dashboard -  Affichage windows setup logging every
 #----------------------------------------------
 def vFDashboardSetupLoggingEveryOpen( self, event ):
  print("-- vFDashboardSetupLoggingEvery --")
  # Récupération valeur
  sParameter = self.ui.label_EventLogEvery.text()
  uiHours    = int(sParameter.split("h")[0])
  sMinutes   = sParameter.split("h ")[1]
  uiMinutes  = int(sMinutes.split("min")[0])
  # Open
  self.tUISetupLoggingEvery.vFOpen( uiHours, uiMinutes )

 #----------------------------------------------
 # Dashboard - Affichage windows setup logging threshold
 #----------------------------------------------
 def vFDashboardSetupLoggingThresholdOpen( self, event ):
  print("-- vFDashboardSetupLoggingThreshold --")
  # Récupération valeur
  sParameter = self.ui.label_EventLogThreshold.text()
  uiPourcent = int(sParameter.split(" %")[0])
  self.tUISetupLoggingThreshold.vFOpen( uiPourcent )

 #----------------------------------------------
 # Dashboard - Affichage windows optical averaging
 #----------------------------------------------
 def vFDashboardOpticalAveragingOpen( self, event ):
  print("-- vFDashboardSetupLoggingThreshold --")
  # Récupération valeur
  sParameter = self.ui.label_AveragingValue.text()
  uiPourcent = int(sParameter)
  self.tUIOpticalAvg.vFOpen( uiPourcent )


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
      elif( sElt == "Depth" ):
       print('self.ui.label_Config_DepthUnit.text() = '+self.ui.label_Config_DepthUnit.text())
       # Foot
       if( self.ui.label_Config_DepthUnit.text() == "f" ):
        fResult = ttConfig["CALCULATED"]["DEPTH"]["fDepthF"]
        print("fResult = %.2f"%fResult)
       # Meter
       else:
        fResult = ttConfig["SENSOR"]["Depth"]["fResult"]
      # -- EC --
      elif( sElt == "EC" ):
       # 25C
       if( self.ui.label_Config_ECRefTemp.text() == "25 C" ):
        fResult = ttConfig["CALCULATED"]["EC"]["fEC_25"]
       elif( self.ui.label_Config_ECRefTemp.text() == "20 C" ):
        fResult = ttConfig["CALCULATED"]["EC"]["fEC_20"]
       else:
        fResult = ttConfig["SENSOR"]["EC"]["fResult"]
      # -- AUTRES --
      else:
       fResult = ttMeasure[sElt]["fResult"]

      uiIndex = uiCpt
      self.tMeasureBox[uiIndex]["tLabelMeasure"].setText( "%.2f"%fResult )
      # Affichage résultat texte
      tfResult[uiIndex] = fResult
      break

   # Voie calculée
   self.ui.label_LV_salinity.setText( "%.2f"%ttConfig["CALCULATED"]["Salinity"]["fResult"] )
   self.ui.label_LV_SSG.setText( "%.2f"%ttConfig["CALCULATED"]["SSG"]["fResult"] )
   self.ui.label_LV_TDS.setText( "%.2f"%ttConfig["CALCULATED"]["TDS"]["fResult"] )
   self.ui.label_LV_Ammonia.setText( "%.2f"%ttConfig["SENSOR"]["AUX7"]["fResult"] )

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
 def vFCALIBRATIONAddCalibNavElt( self, sChannelName, ucChannel, tChannel, ttConfig ):
  print("-- vFCALIBRATIONAddCalibNavElt --")

  # Si voie vide
  if( tChannel["sIndex"] == "EMPTY" ): return

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
  self.xCalibrationSensorSelectConnectSignal.emit( sChannelName, ucChannel, tChannel, tWidget, ttConfig )
  return tWidget

 #----------------------------------------------
 # Calibration - Changement de menu capteur
 #----------------------------------------------
 def vFCALIBRATIONSensorNavSelectionDynamic( self, sConfigName, ucChannel, tChannel, tWidget, ttConfig ):
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
  if( tCalibChannelInfo[sIndex]["ucPoint"] > 1 ):
   self.ui.groupBox_AUX_PT2.setVisible(True)
   self.ui.groupBox_AUX_PT2.setTitle(tCalibChannelInfo[sIndex]["Point"][1]["sName"])
   self.siCalibrationPointSelectConnectSignal.emit( sConfigName, ucChannel, tChannel, self.ui.widget_AuxPt2Value, 1 )
  else:
   self.ui.groupBox_AUX_PT2.setVisible(False)
  # Point 3
  if( tCalibChannelInfo[sIndex]["ucPoint"] > 2 ):
   self.ui.groupBox_AUX_PT3.setVisible(True)
   self.ui.groupBox_AUX_PT3.setTitle(tCalibChannelInfo[sIndex]["Point"][2]["sName"])
   self.siCalibrationPointSelectConnectSignal.emit( sConfigName, ucChannel, tChannel, self.ui.widget_AuxPt3Value, 2 )
  else:
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

  # Si ORP
  if( sIndex == "ORP" ):
   print('sIndex == "ORP"')
   self.ui.groupBox_CalibrationParameters.setVisible(True)
   self.ui.groupBox_CalibrationParameters_Point.setVisible(True)
   self.ui.widget_ORPCalValue.setVisible(True)
   self.ui.widget_ORPCalValue_Point.setVisible(True)
   self.ui.label_ORPCalValueType.setText( str( tChannel["Point"][0]["uiCalValueRef"] )+ " mV" )
   # ORP select
   #self.ui.label_ORPCalValueType.setText( str( tChannel["Point"][0]["uiCalValueRef"] )+ " mV" )
   #self.ui.spinBox_ECCalValue_2_Point.setValue()
   # Page point
   self.ui.comboBox_ORPCalValue_Point.setCurrentText( str( tChannel["Point"][0]["uiCalValueRef"] )+ " mV")

  #---------------
  # Si EC
  if( sIndex == "EC" ):
   print('sIndex == "EC"')
   self.ui.groupBox_CalibrationParameters.setVisible(True)
   self.ui.widget_CalSensor_ECCalValue.setVisible(True)
   self.ui.widget_CalSensor_ECUserValue.setVisible(True)
   self.ui.label_CalSensor_ECCalValue.setText( tChannel["sCalValue"] )

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

   self.ui.comboBox_ECCalValue_Point.setCurrentText(tChannel["sCalValue"])

   # User
   self.ui.spinBox_ECCalValue_2_Point.setValue(tChannel["uiUserCalValue"])
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

  #---------------
  print("sConfigName = "+sConfigName)
  print("ttConfig[PRODUCT][uiModel] = %u"%ttConfig["PRODUCT"]["uiModel"])
  # Si AS/AP-Pro - AUX
  if(   ( "AUX" in sConfigName )
    and ( ttConfig["PRODUCT"]["uiModel"] == 29 ) ):
   self.ui.label_ASAPpro_calibRestore.setVisible(True)
  else:
   self.ui.label_ASAPpro_calibRestore.setVisible(False)

  #---------------
  # Si capteur optique
  if( uiFGetIDWithChannelNameWith(sIndex) > 16 ):
   print('sIndex == "OPTICAL"')
   print("sConfigName = "+sConfigName)
   print(tChannel)
   self.ui.groupBox_CalibrationParameters.setVisible(True)
   self.ui.widget_AuxGSFactor.setVisible(True)
   self.ui.label_AuxGSFactor.setText( str( tChannel["fGS"] ) )

  #-- Complète date calibration
  # Point 1
  if(   ( tChannel["Point"][0]["uiDay"]   == 0 )
    and ( tChannel["Point"][0]["uiMonth"] == 0 )
    and ( tChannel["Point"][0]["uiYear"]  == 0 ) ):
   self.ui.label_AuxPt1Date.setText( "--/--/--" )
  else:
   self.ui.label_AuxPt1Date.setText( ("%02u"%tChannel["Point"][0]["uiDay"])+("/%02u"%tChannel["Point"][0]["uiMonth"])+("/20%02u"%tChannel["Point"][0]["uiYear"]) )
  self.ui.label_AuxPt1Value.setText( str(tChannel["Point"][0]["uiCalReport"])+" "+tChannel["Point"][0]["sCalReportUnit"]  )
  # Point 2
  if( tChannel["ucPoint"] > 1 ):
   if(   ( tChannel["Point"][1]["uiDay"]   == 0 )
     and ( tChannel["Point"][1]["uiMonth"] == 0 )
     and ( tChannel["Point"][1]["uiYear"]  == 0 ) ):
    self.ui.label_AuxPt2Date.setText( "--/--/--" )
   else:
    self.ui.label_AuxPt2Date.setText( ("%02u"%tChannel["Point"][1]["uiDay"])+("/%02u"%tChannel["Point"][1]["uiMonth"])+("/20%02u"%tChannel["Point"][1]["uiYear"]) )
   self.ui.label_AuxPt2Value.setText( str(tChannel["Point"][1]["uiCalReport"])+" "+tChannel["Point"][1]["sCalReportUnit"]  )
  # Point 3
  if( tChannel["ucPoint"] > 2 ):
   if(   ( tChannel["Point"][2]["uiDay"]   == 0 )
     and ( tChannel["Point"][2]["uiMonth"] == 0 )
     and ( tChannel["Point"][2]["uiYear"]  == 0 ) ):
    self.ui.label_AuxPt3Date.setText( "--/--/--" )
   else:
    self.ui.label_AuxPt3Date.setText( ("%02u"%tChannel["Point"][2]["uiDay"])+("/%02u"%tChannel["Point"][2]["uiMonth"])+("/20%02u"%tChannel["Point"][2]["uiYear"]) )
   self.ui.label_AuxPt3Value.setText( str(tChannel["Point"][2]["uiCalReport"])+" "+tChannel["Point"][2]["sCalReportUnit"] )

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
  # Si main calibration : changement nav
  if( uiIndex == TECalibPointNavIndex.MAIN ):self.ui.stackedWidget_Nav2.setCurrentIndex(4)

 #----------------------------------------------
 # Calibration - Chargement/Affichage du menu point de calibration
 #----------------------------------------------
 def vFCALIBRATIONPointNavSelectionDynamic( self, sConfigName, ucChannel, tChannel, tWidget, uiPoint ):
  # Changement d'onglet
  self.ui.stackedWidget_calibrationMain.setCurrentIndex(1)
  # Nom du point
  #self.ui.label_calibPointName.setText( sConfigName+":"+tChannel["sIndex"] + " - " + tChannel["Point"][uiPoint]["sName"] )
  self.ui.label_calibPointName.setText( tChannel["sIndex"] + " - " + tChannel["Point"][uiPoint]["sName"] )
  # Exception DO
  if( tChannel["sIndex"] == "DO" ):
   # Unité de la voie mesurée
   self.ui.label_calibRTUnit.setText( "(%)" )
  else:
   # Unité de la voie mesurée
   self.ui.label_calibRTUnit.setText( "("+tChannel["sUnit"]+")" )
  # Last calibration date
  self.ui.label_calibPointLastCalibDate.setText( ("%02u"%tChannel["Point"][uiPoint]["uiDay"])+("/%02u"%tChannel["Point"][uiPoint]["uiMonth"])+("/20%02u"%tChannel["Point"][uiPoint]["uiYear"]) )
  # Last calibration value
  self.ui.label_calibPointLastCalibValue.setText( str(tChannel["Point"][uiPoint]["uiCalReport"])+" "+tChannel["Point"][uiPoint]["sCalReportUnit"] )
  # Si pH : Affichage pHmv
  if( tChannel["sIndex"] == "pH" ):
   self.ui.widget_calibRTpHmV.setVisible(True)
  else:
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

  # Changement onglet
  # Effacement de la commande balai en mode calibration
  self.ui.stackedWidget_Nav2.setCurrentIndex(8)

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

 #----------------------------------------------
 # Calibration -
 #----------------------------------------------
 def vFCalibrationClearGraphData( self ):
  # Clear graph
  self.chartCalib.vFClear()

 #=========================================================================
 # DATA
 #=========================================================================
 #--------------------------------------------------------------------------
 # Data - Affichage de la donnée
 #--------------------------------------------------------------------------
 def vFDATADisplayRecordedData( self, ttConfig, ttMeasure ):
  print("-- vFDATADisplayRecordedData --")

  # Data - Bouton export to CSV visible
  self.ui.exportToCSV_btn.setVisible(True)
  self.ui.exportToTAB_btn.setVisible(True)
  ##TODO - Pour le moment pas d'export en RAW
  self.ui.exportToRAW_btn.setVisible(True)

  #------- Ajout d'un checkbox
  def vFAddCheckbox( sTxt, uiRow, uicolumn, ttConfig, ttMeasure, sChannelIndex, tParentWidget ):
   # Variable
   sChannelBoolIndex     = "b"+sChannelIndex
   sChannelCheckBoxIndex = "t"+sChannelIndex+"Checkbox"

   tWidgetCheckBox = QWidget()
   tWidgetCheckBox.setContentsMargins(0,0,0,0)
   tBox = QHBoxLayout()
   tWidgetCheckBox.setLayout(tBox)
   tBox.setContentsMargins(0,0,0,0)

   tCheckBox = PyToggle()
   if( ttMeasure[0][sChannelBoolIndex] ):
    tCheckBox.setCheckState( Qt.Checked )
   else:
    tCheckBox.setCheckState( Qt.Unchecked )
   tLabel = QLabel()
   tLabel.setText( sTxt )
   # Sauvegarde de la checkbox
   ttMeasure[0][sChannelCheckBoxIndex] = tCheckBox

   tWidgetCheckBox.layout().addWidget(tCheckBox)
   tWidgetCheckBox.layout().addWidget(tLabel)
   #tLabel.setText( sTxt )
   #self.ui.widget_9.layout().addWidget( tLabel, uiRow, uicolumn)
   #self.ui.widget_dataChanneCheckbox.layout().addWidget(tCheckBox)
   tCheckBox.checkStateChanged.connect(lambda event:self.vFDATACheckboxClicked( event, ttConfig, ttMeasure, sChannelBoolIndex ) )
   #self.ui.widget_dataChanneCheckbox.layout().addWidget(tWidgetCheckBox, uiRow, uicolumn)
   tParentWidget.layout().addWidget(tWidgetCheckBox)
  #--------

  # Suppression des marges
  self.ui.widget_dataChanneCheckbox.setContentsMargins(0,0,0,0)
  # Sauvegarde de la donnée
  self.ttMeasure = ttMeasure

  # Etat de l'affichage
  ttMeasure[0]["bBatt"]         = True
  ttMeasure[0]["bTemperature"]  = True
  ttMeasure[0]["bDepth"]        = True
  ttMeasure[0]["bBaro"]         = True
  ttMeasure[0]["bpH"]           = True
  ttMeasure[0]["bpHmv"]         = True
  ttMeasure[0]["bORP"]          = True
  ttMeasure[0]["bDO"]           = True
  ttMeasure[0]["bDO_PC"]        = True
  ttMeasure[0]["bEC"]           = True
  ttMeasure[0]["bAmmonia"]      = True
  ttMeasure[0]["bSalinity"]     = True
  ttMeasure[0]["bSSG"]          = True
  ttMeasure[0]["bTDS"]          = True
  if( ttConfig["PRODUCT"]["uiAUXNumber"] > 0 ): ttMeasure[0]["bAUX1"] = True
  else:                                         ttMeasure[0]["bAUX1"] = False
  if( ttConfig["PRODUCT"]["uiAUXNumber"] > 1 ): ttMeasure[0]["bAUX2"] = True
  else:                                         ttMeasure[0]["bAUX2"] = False
  if( ttConfig["PRODUCT"]["uiAUXNumber"] > 2 ): ttMeasure[0]["bAUX3"] = True
  else:                                         ttMeasure[0]["bAUX3"] = False
  if( ttConfig["PRODUCT"]["uiAUXNumber"] > 3 ): ttMeasure[0]["bAUX4"] = True
  else:                                         ttMeasure[0]["bAUX4"] = False
  if( ttConfig["PRODUCT"]["uiAUXNumber"] > 4 ): ttMeasure[0]["bAUX5"] = True
  else:                                         ttMeasure[0]["bAUX5"] = False
  if( ttConfig["PRODUCT"]["uiAUXNumber"] > 5 ): ttMeasure[0]["bAUX6"] = True
  else:                                         ttMeasure[0]["bAUX6"] = False
  if( ttConfig["CALCULATED"]["AMMONIA"]["bActivated"] ): ttMeasure[0]["bAmmonia"] = True
  else:                                                  ttMeasure[0]["bAmmonia"] = False

  # Entête du tableau
  self.tLabels = []
  self.tLabels.append("Tag")
  self.tLabels.append("DateTime")
  self.tLabels.append("Cleaned")
  self.tLabels.append("Batt (V)")
  self.tLabels.append("Temp (C)")
  self.tLabels.append("Temp (F)")
  self.tLabels.append("Depth (m)")
  self.tLabels.append("Depth (f)")
  self.tLabels.append("Baro (mB)")
  self.tLabels.append("pH")
  self.tLabels.append("pH (mV)")
  self.tLabels.append("ORP (mV)")
  self.tLabels.append("DO (%sat)")
  self.tLabels.append("DO (mg/l)")
  self.tLabels.append("EC (uS/cm)")
  #tLabels.append("Ammonia (mg/L)")
  self.tLabels.append("Sal (PSU)")
  self.tLabels.append("SSG (dt)")
  self.tLabels.append("TDS")
  # Selection des labels
  if( ( ttConfig["PRODUCT"]["uiAUXNumber"] > 0 ) and ( ttMeasure[0]["sAUX1_Assign"] != "EMPTY" ) ):
   self.tLabels.append("AUX1 name")
   self.tLabels.append("AUX1")
  # Selection des labels
  if( ( ttConfig["PRODUCT"]["uiAUXNumber"] > 1 ) and ( ttMeasure[0]["sAUX2_Assign"] != "EMPTY" ) ):
   self.tLabels.append("AUX2 name")
   self.tLabels.append("AUX2")
  # Selection des labels
  if( ( ttConfig["PRODUCT"]["uiAUXNumber"] > 2 ) and ( ttMeasure[0]["sAUX3_Assign"] != "EMPTY" ) ):
   self.tLabels.append("AUX3 name")
   self.tLabels.append("AUX3")
  # Selection des labels
  if( ( ttConfig["PRODUCT"]["uiAUXNumber"] > 3 ) and ( ttMeasure[0]["sAUX4_Assign"] != "EMPTY" ) ):
   self.tLabels.append("AUX4 name")
   self.tLabels.append("AUX4")
  # Selection des labels
  if( ( ttConfig["PRODUCT"]["uiAUXNumber"] > 4 ) and ( ttMeasure[0]["sAUX6_Assign"] != "EMPTY" ) ):
   self.tLabels.append("AUX5 name")
   self.tLabels.append("AUX5")
  # Selection des labels
  if( ( ttConfig["PRODUCT"]["uiAUXNumber"] > 5 ) and ( ttMeasure[0]["sAUX6_Assign"] != "EMPTY" ) ):
   self.tLabels.append("AUX6 name")
   self.tLabels.append("AUX6")
  # Selection des labels
  if( ttConfig["CALCULATED"]["AMMONIA"]["bActivated"] ):
   self.tLabels.append("Ammonia (mg/L)")

  # Création des Layouts
  vbox = QVBoxLayout(); self.ui.groupBox_Environment.setLayout(vbox)
  vbox = QVBoxLayout(); self.ui.groupBox_pHORPDOEC.setLayout(vbox)
  vbox = QVBoxLayout(); self.ui.groupBox_calculated.setLayout(vbox)
  vbox = QVBoxLayout(); self.ui.groupBox_Aux.setLayout(vbox)

  # Effacement checkbox - Nettoyage
  for i in reversed(range(self.ui.groupBox_Environment.layout().count())):
   self.ui.groupBox_Environment.layout().itemAt(i).widget().deleteLater()
  for i in reversed(range(self.ui.groupBox_pHORPDOEC.layout().count())):
   self.ui.groupBox_pHORPDOEC.layout().itemAt(i).widget().deleteLater()
  for i in reversed(range(self.ui.groupBox_calculated.layout().count())):
   self.ui.groupBox_calculated.layout().itemAt(i).widget().deleteLater()
  for i in reversed(range(self.ui.groupBox_Aux.layout().count())):
   self.ui.groupBox_Aux.layout().itemAt(i).widget().deleteLater()

  tGraphLabel = []
  tGraphLabel.append("Batt")
  tGraphLabel.append("Temp C")
  tGraphLabel.append("Temp F")
  tGraphLabel.append("Depth m")
  tGraphLabel.append("Depth f")
  tGraphLabel.append("Baro")
  tGraphLabel.append("pH")
  tGraphLabel.append("pH (mV)")
  tGraphLabel.append("ORP")
  tGraphLabel.append("DO (%sat)")
  tGraphLabel.append("DO")
  tGraphLabel.append("EC")
  tGraphLabel.append("Salinity")
  tGraphLabel.append("SSG")
  tGraphLabel.append("TDS")
  if( ttMeasure[0]["sAUX1_Assign"] != "EMPTY" ):
   tGraphLabel.append(ttMeasure[0]["sAUX1_Assign"])
  if( ttMeasure[0]["sAUX2_Assign"] != "EMPTY" ):
   tGraphLabel.append(ttMeasure[0]["sAUX2_Assign"])
  if( ttMeasure[0]["sAUX3_Assign"] != "EMPTY" ):
   tGraphLabel.append(ttMeasure[0]["sAUX3_Assign"])
  if( ttMeasure[0]["sAUX4_Assign"] != "EMPTY" ):
   tGraphLabel.append(ttMeasure[0]["sAUX4_Assign"])
  if( ttMeasure[0]["sAUX5_Assign"] != "EMPTY" ):
   tGraphLabel.append(ttMeasure[0]["sAUX5_Assign"])
  if( ttMeasure[0]["sAUX6_Assign"] != "EMPTY" ):
   tGraphLabel.append(ttMeasure[0]["sAUX6_Assign"])
  if( ttConfig["CALCULATED"]["AMMONIA"]["bActivated"] ):
   tGraphLabel.append("Ammonia")

  # Création des bouton de désactivation
  vFAddCheckbox("Batt",       5, 0, ttConfig, ttMeasure, "Batt",         self.ui.groupBox_Environment )
  vFAddCheckbox("Temp",       0, 0, ttConfig, ttMeasure, "Temperature",  self.ui.groupBox_Environment )
  vFAddCheckbox("Depth",      2, 0, ttConfig, ttMeasure, "Depth",        self.ui.groupBox_Environment )
  vFAddCheckbox("Baro",       4, 0, ttConfig, ttMeasure, "Baro",         self.ui.groupBox_Environment )
  vFAddCheckbox("pH",         0, 1, ttConfig, ttMeasure, "pH",           self.ui.groupBox_pHORPDOEC )
  vFAddCheckbox("pH (mV)",    1, 1, ttConfig, ttMeasure, "pHmv",         self.ui.groupBox_pHORPDOEC )
  vFAddCheckbox("ORP",        2, 1, ttConfig, ttMeasure, "ORP",          self.ui.groupBox_pHORPDOEC )
  vFAddCheckbox("DO (%sat)",  3, 1, ttConfig, ttMeasure, "DO_PC",        self.ui.groupBox_pHORPDOEC )
  vFAddCheckbox("DO",         4, 1, ttConfig, ttMeasure, "DO",           self.ui.groupBox_pHORPDOEC )
  vFAddCheckbox("EC",         5, 1, ttConfig, ttMeasure, "EC",           self.ui.groupBox_pHORPDOEC )
  #vFAddCheckbox("Ammonia",    0, 2, ttConfig, ttMeasure, "bAmmonia" )
  vFAddCheckbox("Salinity",   1, 2, ttConfig, ttMeasure, "Salinity",     self.ui.groupBox_calculated )
  vFAddCheckbox("SSG",        2, 2, ttConfig, ttMeasure, "SSG",          self.ui.groupBox_calculated )
  vFAddCheckbox("TDS",        3, 2, ttConfig, ttMeasure, "TDS",          self.ui.groupBox_calculated )
  if( ( ttConfig["PRODUCT"]["uiAUXNumber"] > 0 ) and ( ttMeasure[0]["sAUX1_Assign"] != "EMPTY" ) ): vFAddCheckbox("AUX1", 0, 3, ttConfig, ttMeasure, "AUX1", self.ui.groupBox_Aux )
  if( ( ttConfig["PRODUCT"]["uiAUXNumber"] > 1 ) and ( ttMeasure[0]["sAUX2_Assign"] != "EMPTY" ) ): vFAddCheckbox("AUX2", 1, 3, ttConfig, ttMeasure, "AUX2", self.ui.groupBox_Aux )
  if( ( ttConfig["PRODUCT"]["uiAUXNumber"] > 2 ) and ( ttMeasure[0]["sAUX3_Assign"] != "EMPTY" ) ): vFAddCheckbox("AUX3", 2, 3, ttConfig, ttMeasure, "AUX3", self.ui.groupBox_Aux )
  if( ( ttConfig["PRODUCT"]["uiAUXNumber"] > 3 ) and ( ttMeasure[0]["sAUX4_Assign"] != "EMPTY" ) ): vFAddCheckbox("AUX4", 3, 3, ttConfig, ttMeasure, "AUX4", self.ui.groupBox_Aux )
  if( ( ttConfig["PRODUCT"]["uiAUXNumber"] > 4 ) and ( ttMeasure[0]["sAUX5_Assign"] != "EMPTY" ) ): vFAddCheckbox("AUX5", 4, 3, ttConfig, ttMeasure, "AUX5", self.ui.groupBox_Aux )
  if( ( ttConfig["PRODUCT"]["uiAUXNumber"] > 5 ) and ( ttMeasure[0]["sAUX6_Assign"] != "EMPTY" ) ): vFAddCheckbox("AUX6", 5, 3, ttConfig, ttMeasure, "AUX6", self.ui.groupBox_Aux )
  if( ttConfig["CALCULATED"]["AMMONIA"]["bActivated"] ): vFAddCheckbox("Ammonia", 4, 2, ttConfig, ttMeasure, "Ammonia", self.ui.groupBox_calculated )

  self.ui.groupBox_Environment.layout().setAlignment(Qt.AlignTop)
  self.ui.groupBox_pHORPDOEC.layout().setAlignment(Qt.AlignTop)
  self.ui.groupBox_calculated.layout().setAlignment(Qt.AlignTop)
  self.ui.groupBox_Aux.layout().setAlignment(Qt.AlignTop)

  # 2024/08/29 14:59:01
  tDateTimeStart = QDateTime.fromString(ttMeasure[0]["sDateTime"], "yyyy/MM/dd HH:mm:ss")
  tDateTimeEnd   = QDateTime.fromString(ttMeasure[len(ttMeasure)-1]["sDateTime"], "yyyy/MM/dd HH:mm:ss")
  print(tDateTimeStart)
  ttMeasure[0]["sStartMeasure"] = ttMeasure[0]["sDateTime"]
  ttMeasure[0]["sEndMeasure"]   = ttMeasure[len(ttMeasure)-1]["sDateTime"]

  self.ui.dateTimeEdit_dataStart.setDateTime(tDateTimeStart)
  self.ui.dateTimeEdit_dataEnd.setDateTime(tDateTimeEnd)

  self.ui.dateTimeEdit_dataStart.setMinimumDateTime(tDateTimeStart)
  self.ui.dateTimeEdit_dataStart.setMaximumDateTime(tDateTimeEnd)
  self.ui.dateTimeEdit_dataEnd.setMinimumDateTime(tDateTimeStart)
  self.ui.dateTimeEdit_dataEnd.setMaximumDateTime(tDateTimeEnd)

  self.ui.dateTimeEdit_dataStart.dateTimeChanged.connect(lambda tDateTime:self.vDataTreeviewDatetimeChanged(tDateTime, ttConfig, ttMeasure))
  self.ui.dateTimeEdit_dataEnd.dateTimeChanged.connect(lambda tDateTime:self.vDataTreeviewDatetimeChanged(tDateTime, ttConfig, ttMeasure))

  #---------
  # Nombre maximum de graphique
  self.uiChartDataChannelMax = 10
  # Création du graphique data
  #if( len(tLabels) > self.uiChartDataChannelMax ): self.chartData = VChart(self.uiChartDataChannelMax)
  #else:
  # Création du graphique avec nombre de série
  self.chartData = VChart(len(tGraphLabel))
  self.chartData.vFSetSampleDepth(int(self.tINIConfig["SOFTWARE"]["graphical_depth"]))
  self.chartData.uiSampleDepth = 0
  # Pour axes Y
  tPen = QPen()
  tPen.setMiterLimit(0)
  tPen.setWidth(1);

  print("###### Création graphique #######")
  print("len(tGraphLabel) = %u"%len(tGraphLabel))
  print(tGraphLabel)
  # Parcourt des voies
  for uiCpt in range(len(tGraphLabel)):
   #tGraphLabel
   self.chartData._series[uiCpt].setName(tGraphLabel[uiCpt])
   self.chartData.tPenTemplate.setBrush( QColor(self.sFGetSensorColorWithGraphLabel(tGraphLabel[uiCpt]) ) )
   self.chartData._series[uiCpt].setPen( self.chartData.tPenTemplate )
   # Axis Y
   self.chartData._axisY[uiCpt].setLabelsColor( self.sFGetSensorColorWithGraphLabel(tGraphLabel[uiCpt]) )
   tPen.setBrush( QColor(self.sFGetSensorColorWithGraphLabel(tGraphLabel[uiCpt])) )
   self.chartData._axisY[uiCpt].setLinePen( tPen )
   """
   if( uiCpt < 3 ): continue
   #if( len(self.chartData._series) >= self.uiChartDataChannelMax ): break
   self.chartData._series[uiCpt-3].setName(self.tLabels[uiCpt])
   print(self.tLabels[uiCpt])
   #uiIndex = ttConfig["SENSOR"][self.tLabels[uiCpt]]["uiIndex"]
   #self.chartData.tPenTemplate.setBrush( QColor(self.sFGetSensorColorWithID(uiIndex) ) )
   self.chartData._series[0].setPen( self.chart.tPenTemplate )
   """

  #self.chartData.legend().hide()
  self.chartData.setContentsMargins(-15, -15, -15, -15)
  # Création chartview
  self.chartData_view = QChartView( self.chartData )
  self.chartData_view.setRenderHint( QPainter.Antialiasing )
  self.chartData_view.setRubberBand(QChartView.HorizontalRubberBand)
  # Clear vieux graphique
  vbox = QVBoxLayout()
  vbox.setContentsMargins(0, 0, 0, 0)
  self.ui.widget_DataChart.setLayout(vbox)
  for i in reversed(range(self.ui.widget_DataChart.layout().count())):
   self.ui.widget_DataChart.layout().itemAt(i).widget().deleteLater()
  self.ui.widget_DataChart.layout().addWidget(self.chartData_view)
  #---------

  # QCheckBox
  self.vFDATAUpdateRecordedData(ttConfig, ttMeasure)

 #--------------------------------------------------------------------------
 def vFDATACheckboxClicked( self, bState, ttConfig, ttMeasure, sChannelBoolIndex ):
  print("-- vFDATACheckboxClicked --")
  ttMeasure[0][sChannelBoolIndex] = not ttMeasure[0][sChannelBoolIndex]
  #self.vFDATAUpdateRecordedData( ttConfig, ttMeasure )
  self.vDataTreeviewHideColumn( ttConfig, ttMeasure )

 #--------------------------------------------------------------------------
 def vFDATAUpdateRecordedData( self, ttConfig, ttMeasure ):
  print("-- VMainWindow > vFDATAUpdateRecordedData --")
  # Ajout d'un échantillon
  def vFAddElt( sTxt, uiRow, uicolumn ):
   tLabel = QLabel()
   tLabel.setText( sTxt )
   self.ui.widget_9.layout().addWidget( tLabel, uiRow, uicolumn)

  # Clear du treeview
  self.ui.treeWidget.clear()
  self.vFTreeviewRemoveItem( self.ui.treeWidget )

  # Ajout des en-têtes de colonne
  self.ui.treeWidget.setHeaderLabels(self.tLabels)

  # Ajout des entêtes
  tHeader = self.ui.treeWidget.header()

  tTreeviewCalib = []
  tTreeData = []
  tGraphData = []
  # Parcourt des lignes
  for ucPoint in range(len(ttMeasure)):
   tTreeData.append([])
   # Tag
   tTreeData[ucPoint].append( str(ucPoint+1) )
   tTreeData[ucPoint].append( ttMeasure[ucPoint]["sDateTime"]      )
   tTreeData[ucPoint].append( ttMeasure[ucPoint]["sCleaningFlag"]  )
   tTreeData[ucPoint].append( ttMeasure[ucPoint]["sBatteryLevel"]  )
   tTreeData[ucPoint].append( ttMeasure[ucPoint]["sTempC"]         )
   tTreeData[ucPoint].append( ttMeasure[ucPoint]["sTempF"]         )
   tTreeData[ucPoint].append( ttMeasure[ucPoint]["sDepthM"]        )
   tTreeData[ucPoint].append( ttMeasure[ucPoint]["sDepthF"]        )
   tTreeData[ucPoint].append( ttMeasure[ucPoint]["sBaro"]          )
   tTreeData[ucPoint].append( ttMeasure[ucPoint]["spH"]            )
   tTreeData[ucPoint].append( ttMeasure[ucPoint]["spHmV"]          )
   tTreeData[ucPoint].append( ttMeasure[ucPoint]["sORP"]           )
   tTreeData[ucPoint].append( ttMeasure[ucPoint]["sDO_PC"]         )
   tTreeData[ucPoint].append( ttMeasure[ucPoint]["sDO"]            )
   # Choix EC
   if( ttConfig["CALCULATED"]["EC"]["sTSelect"] == "25 C" ):
    tTreeData[ucPoint].append( ttMeasure[ucPoint]["sEC_25"] )
   elif( ttConfig["CALCULATED"]["EC"]["sTSelect"] == "20 C" ):
    tTreeData[ucPoint].append( ttMeasure[ucPoint]["sEC_20"] )
   else:
    tTreeData[ucPoint].append( ttMeasure[ucPoint]["sEC"] )

   tTreeData[ucPoint].append( ttMeasure[ucPoint]["sSalinity"]      )
   tTreeData[ucPoint].append( ttMeasure[ucPoint]["sSSG"]           )
   tTreeData[ucPoint].append( ttMeasure[ucPoint]["sTDS"]           )
   if( ttMeasure[ucPoint]["sAUX1_Assign"] != "EMPTY" ):
    tTreeData[ucPoint].append( ttMeasure[ucPoint]["sAUX1_Assign"]   )
    tTreeData[ucPoint].append( ttMeasure[ucPoint]["sAUX1"]          )

   if( ttMeasure[ucPoint]["sAUX2_Assign"] != "EMPTY" ):
    tTreeData[ucPoint].append( ttMeasure[ucPoint]["sAUX2_Assign"]   )
    tTreeData[ucPoint].append( ttMeasure[ucPoint]["sAUX2"]          )

   if( ttMeasure[ucPoint]["sAUX3_Assign"] != "EMPTY" ):
    tTreeData[ucPoint].append( ttMeasure[ucPoint]["sAUX3_Assign"]   )
    tTreeData[ucPoint].append( ttMeasure[ucPoint]["sAUX3"]          )

   if( ttMeasure[ucPoint]["sAUX4_Assign"] != "EMPTY" ):
    tTreeData[ucPoint].append( ttMeasure[ucPoint]["sAUX4_Assign"]   )
    tTreeData[ucPoint].append( ttMeasure[ucPoint]["sAUX4"]          )

   if( ttMeasure[ucPoint]["sAUX5_Assign"] != "EMPTY" ):
    tTreeData[ucPoint].append( ttMeasure[ucPoint]["sAUX5_Assign"]   )
    tTreeData[ucPoint].append( ttMeasure[ucPoint]["sAUX5"]          )

   if( ttMeasure[ucPoint]["sAUX6_Assign"] != "EMPTY" ):
    tTreeData[ucPoint].append( ttMeasure[ucPoint]["sAUX6_Assign"]   )
    tTreeData[ucPoint].append( ttMeasure[ucPoint]["sAUX6"]          )

   if( ttConfig["CALCULATED"]["AMMONIA"]["bActivated"] ):
    tTreeData[ucPoint].append( ttMeasure[ucPoint]["sAUX7"] )

   # Ajout
   tTreeviewCalib.append(QTreeWidgetItem(tTreeData[ucPoint]))

   # Graphique
   tGraphData.append([])
   # Tag
   #tGraphData[ucPoint].append( str(ucPoint+1) )
   #tGraphData[ucPoint].append( ttMeasure[ucPoint]["sDateTime"]      )
   #tGraphData[ucPoint].append( ttMeasure[ucPoint]["sCleaningFlag"]  )
   tGraphData[ucPoint].append( ttMeasure[ucPoint]["fBatteryLevel"]  )
   tGraphData[ucPoint].append( ttMeasure[ucPoint]["fTempC"]         )
   tGraphData[ucPoint].append( ttMeasure[ucPoint]["fTempF"]         )
   tGraphData[ucPoint].append( ttMeasure[ucPoint]["fDepthM"]        )
   tGraphData[ucPoint].append( ttMeasure[ucPoint]["fDepthF"]        )
   tGraphData[ucPoint].append( ttMeasure[ucPoint]["fBaro"]          )
   tGraphData[ucPoint].append( ttMeasure[ucPoint]["fpH"]            )
   tGraphData[ucPoint].append( ttMeasure[ucPoint]["fpHmV"]          )
   tGraphData[ucPoint].append( ttMeasure[ucPoint]["fORP"]           )
   tGraphData[ucPoint].append( ttMeasure[ucPoint]["fDO_PC"]         )
   tGraphData[ucPoint].append( ttMeasure[ucPoint]["fDO"]            )
   # Choix EC
   if( ttConfig["CALCULATED"]["EC"]["sTSelect"] == "25 C" ):
    tGraphData[ucPoint].append( ttMeasure[ucPoint]["fEC_25"] )
   elif( ttConfig["CALCULATED"]["EC"]["sTSelect"] == "20 C" ):
    tGraphData[ucPoint].append( ttMeasure[ucPoint]["fEC_20"] )
   else:
    tGraphData[ucPoint].append( ttMeasure[ucPoint]["fEC"] )

   tGraphData[ucPoint].append( ttMeasure[ucPoint]["fSalinity"]      )
   tGraphData[ucPoint].append( ttMeasure[ucPoint]["fSSG"]           )
   tGraphData[ucPoint].append( ttMeasure[ucPoint]["fTDS"]           )

   if( ttMeasure[0]["sAUX1_Assign"] != "EMPTY" ):
    if( ttMeasure[ucPoint]["sAUX1_Assign"] != "EMPTY" ):
     tGraphData[ucPoint].append( ttMeasure[ucPoint]["fAUX1"]          )
    else:
     tGraphData[ucPoint].append(0)
   if( ttMeasure[0]["sAUX2_Assign"] != "EMPTY" ):
    if( ttMeasure[ucPoint]["sAUX2_Assign"] != "EMPTY" ):
     tGraphData[ucPoint].append( ttMeasure[ucPoint]["fAUX2"]          )
    else:
     tGraphData[ucPoint].append(0)
   if( ttMeasure[0]["sAUX3_Assign"] != "EMPTY" ):
    if( ttMeasure[ucPoint]["sAUX3_Assign"] != "EMPTY" ):
     tGraphData[ucPoint].append( ttMeasure[ucPoint]["fAUX3"]          )
    else:
     tGraphData[ucPoint].append(0)
   if( ttMeasure[0]["sAUX4_Assign"] != "EMPTY" ):
    if( ttMeasure[ucPoint]["sAUX4_Assign"] != "EMPTY" ):
     tGraphData[ucPoint].append( ttMeasure[ucPoint]["fAUX4"]          )
    else:
     tGraphData[ucPoint].append(0)
   if( ttMeasure[0]["sAUX5_Assign"] != "EMPTY" ):
    if( ttMeasure[ucPoint]["sAUX5_Assign"] != "EMPTY" ):
     tGraphData[ucPoint].append( ttMeasure[ucPoint]["fAUX5"]          )
    else:
     tGraphData[ucPoint].append(0)
   if( ttMeasure[0]["sAUX6_Assign"] != "EMPTY" ):
    if( ttMeasure[ucPoint]["sAUX6_Assign"] != "EMPTY" ):
     tGraphData[ucPoint].append( ttMeasure[ucPoint]["fAUX6"]          )
    else:
     tGraphData[ucPoint].append(0)
   if( ttConfig["CALCULATED"]["AMMONIA"]["bActivated"] ):
    tGraphData[ucPoint].append( ttMeasure[ucPoint]["fAUX7"] )

   # Ajout
   self.chartData.vFAddSample(tGraphData[ucPoint])

  self.vFTreeviewRemoveItem(self.ui.treeWidget)
  self.ui.treeWidget.insertTopLevelItems( 0, tTreeviewCalib )
  self.ui.treeWidget.sortItems( 1, Qt.AscendingOrder )

  header = self.ui.treeWidget.header()
  header.setSectionResizeMode(QHeaderView.ResizeToContents)
  header.setStretchLastSection(False)
  header.setSectionResizeMode(len(self.tLabels), QHeaderView.Stretch)

  # Redéfinit le mode de sélection
  self.ui.treeWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
  self.ui.treeWidget.setSelectionMode(QAbstractItemView.MultiSelection)
  # Lance le filtrage une première fois
  self.vDataTreeviewHideColumn( ttConfig, ttMeasure )

 #--------------------------------------------------------------------------
 # Suppression element du treeview
 #--------------------------------------------------------------------------
 def vFTreeviewRemoveItem(self, tTreeview):
  uiTopLevelItemCount = tTreeview.topLevelItemCount()
  for uiCpt in range(0,uiTopLevelItemCount):
   tWidget = tTreeview.takeTopLevelItem( 0)
   tTreeview.removeItemWidget(tWidget,0)

 #--------------------------------------------------------------------------
 # Affichage ou non des columns du tableau
 #--------------------------------------------------------------------------
 def vDataTreeviewHideColumn( self, ttConfig, ttMeasure ):
  print("-- vDataTreeviewHideColumn --")

  uiCpt = 3
  uiCptChart = 0
  if( ttMeasure[0]["bBatt"] ):
   self.ui.treeWidget.showColumn(uiCpt)
   self.chartData.vFAddSeries(uiCptChart)
   uiCpt+=1; uiCptChart+=1
  else:
   self.ui.treeWidget.hideColumn(uiCpt)
   self.chartData.vFRemoveSeries(uiCptChart)
   uiCpt+=1; uiCptChart+=1
  if( ttMeasure[0]["bTemperature"] ):
   if( ttConfig["CALCULATED"]["TEMP"]["bC"] ):
    self.ui.treeWidget.showColumn(uiCpt)
    self.chartData.vFAddSeries(uiCptChart)
    uiCpt+=1; uiCptChart+=1
    self.ui.treeWidget.hideColumn(uiCpt)
    self.chartData.vFRemoveSeries(uiCptChart)
    uiCpt+=1; uiCptChart+=1
   if( ttConfig["CALCULATED"]["TEMP"]["bF"] ):
    self.ui.treeWidget.hideColumn(uiCpt)
    self.chartData.vFRemoveSeries(uiCptChart)
    uiCpt+=1; uiCptChart+=1
    self.ui.treeWidget.showColumn(uiCpt)
    self.chartData.vFAddSeries(uiCptChart)
    uiCpt+=1; uiCptChart+=1
  else:
   # Cache les deux colonnes C et F
   self.ui.treeWidget.hideColumn(uiCpt)
   self.chartData.vFRemoveSeries(uiCptChart)
   uiCpt+=1; uiCptChart+=1
   self.ui.treeWidget.hideColumn(uiCpt)
   self.chartData.vFRemoveSeries(uiCptChart)
   uiCpt+=1; uiCptChart+=1

  if( ttMeasure[0]["bDepth"] ):
   if( ttConfig["CALCULATED"]["DEPTH"]["bM"] ):
    self.ui.treeWidget.showColumn(uiCpt)
    self.chartData.vFAddSeries(uiCptChart)
    uiCpt+=1; uiCptChart+=1
    self.ui.treeWidget.hideColumn(uiCpt)
    self.chartData.vFRemoveSeries(uiCptChart)
    uiCpt+=1; uiCptChart+=1
   if( ttConfig["CALCULATED"]["DEPTH"]["bF"] ):
    self.ui.treeWidget.hideColumn(uiCpt)
    self.chartData.vFRemoveSeries(uiCptChart)
    uiCpt+=1; uiCptChart+=1
    self.ui.treeWidget.showColumn(uiCpt)
    self.chartData.vFAddSeries(uiCptChart)
    uiCpt+=1; uiCptChart+=1
  else:
   self.ui.treeWidget.hideColumn(uiCpt)
   self.chartData.vFRemoveSeries(uiCptChart)
   uiCpt+=1; uiCptChart+=1
   self.ui.treeWidget.hideColumn(uiCpt)
   self.chartData.vFRemoveSeries(uiCptChart)
   uiCpt+=1; uiCptChart+=1
  if( ttMeasure[0]["bBaro"] ):
   self.ui.treeWidget.showColumn(uiCpt);
   self.chartData.vFAddSeries(uiCptChart)
   uiCpt+=1; uiCptChart+=1
  else:
   self.ui.treeWidget.hideColumn(uiCpt);
   self.chartData.vFRemoveSeries(uiCptChart)
   uiCpt+=1; uiCptChart+=1
  if( ttMeasure[0]["bpH"] ):
   self.ui.treeWidget.showColumn(uiCpt)
   self.chartData.vFAddSeries(uiCptChart)
   uiCpt+=1; uiCptChart+=1
  else:
   self.ui.treeWidget.hideColumn(uiCpt)
   self.chartData.vFRemoveSeries(uiCptChart)
   uiCpt+=1; uiCptChart+=1
  if( ttMeasure[0]["bpHmv"] ):
   self.ui.treeWidget.showColumn(uiCpt)
   self.chartData.vFAddSeries(uiCptChart)
   uiCpt+=1; uiCptChart+=1
  else:
   self.ui.treeWidget.hideColumn(uiCpt)
   self.chartData.vFRemoveSeries(uiCptChart)
   uiCpt+=1; uiCptChart+=1
  if( ttMeasure[0]["bORP"] ):
   self.ui.treeWidget.showColumn(uiCpt)
   self.chartData.vFAddSeries(uiCptChart)
   uiCpt+=1; uiCptChart+=1
  else:
   self.ui.treeWidget.hideColumn(uiCpt)
   self.chartData.vFRemoveSeries(uiCptChart)
   uiCpt+=1; uiCptChart+=1
  if( ttMeasure[0]["bDO_PC"] ):
   self.ui.treeWidget.showColumn(uiCpt)
   self.chartData.vFAddSeries(uiCptChart)
   uiCpt+=1; uiCptChart+=1
  else:
   self.ui.treeWidget.hideColumn(uiCpt)
   self.chartData.vFRemoveSeries(uiCptChart)
   uiCpt+=1; uiCptChart+=1
  if( ttMeasure[0]["bDO"] ):
   self.ui.treeWidget.showColumn(uiCpt)
   self.chartData.vFAddSeries(uiCptChart)
   uiCpt+=1; uiCptChart+=1
  else:
   self.ui.treeWidget.hideColumn(uiCpt)
   self.chartData.vFRemoveSeries(uiCptChart)
   uiCpt+=1; uiCptChart+=1
  if( ttMeasure[0]["bEC"] ):
   self.ui.treeWidget.showColumn(uiCpt)
   self.chartData.vFAddSeries(uiCptChart)
   uiCpt+=1; uiCptChart+=1
  else:
   self.ui.treeWidget.hideColumn(uiCpt)
   self.chartData.vFRemoveSeries(uiCptChart)
   uiCpt+=1; uiCptChart+=1
  #
  if( ttMeasure[0]["bSalinity"] ):
   self.ui.treeWidget.showColumn(uiCpt)
   self.chartData.vFAddSeries(uiCptChart)
   uiCpt+=1; uiCptChart+=1
  else:
   self.ui.treeWidget.hideColumn(uiCpt)
   self.chartData.vFRemoveSeries(uiCptChart)
   uiCpt+=1; uiCptChart+=1
  if( ttMeasure[0]["bSSG"] ):
   self.ui.treeWidget.showColumn(uiCpt)
   self.chartData.vFAddSeries(uiCptChart)
   uiCpt+=1; uiCptChart+=1
  else:
   self.ui.treeWidget.hideColumn(uiCpt)
   self.chartData.vFRemoveSeries(uiCptChart)
   uiCpt+=1; uiCptChart+=1
  if( ttMeasure[0]["bTDS"] ):
   self.ui.treeWidget.showColumn(uiCpt)
   self.chartData.vFAddSeries(uiCptChart)
   uiCpt+=1; uiCptChart+=1
  else:
   self.ui.treeWidget.hideColumn(uiCpt)
   self.chartData.vFRemoveSeries(uiCptChart)
   uiCpt+=1; uiCptChart+=1

  # Selection des labels
  if( ( ttConfig["PRODUCT"]["uiAUXNumber"] > 0 ) and ( ttMeasure[0]["sAUX1_Assign"] != "EMPTY" ) ):
   if( ttMeasure[0]["bAUX1"] ):
    self.ui.treeWidget.showColumn(uiCpt)
    self.chartData.vFAddSeries(uiCptChart)
    uiCpt+=1; uiCptChart+=1
    self.ui.treeWidget.showColumn(uiCpt)
    uiCpt+=1;
   else:
    self.ui.treeWidget.hideColumn(uiCpt)
    self.chartData.vFRemoveSeries(uiCptChart)
    uiCpt+=1; uiCptChart+=1
    self.ui.treeWidget.hideColumn(uiCpt)
    uiCpt+=1
  # Selection des labels
  if( ( ttConfig["PRODUCT"]["uiAUXNumber"] > 1 ) and ( ttMeasure[0]["sAUX2_Assign"] != "EMPTY" )  ):
   if( ttMeasure[0]["bAUX2"] ):
    self.ui.treeWidget.showColumn(uiCpt)
    self.chartData.vFAddSeries(uiCptChart)
    uiCpt+=1; uiCptChart+=1
    self.ui.treeWidget.showColumn(uiCpt)
    uiCpt+=1
   else:
    self.ui.treeWidget.hideColumn(uiCpt)
    self.chartData.vFRemoveSeries(uiCptChart)
    uiCpt+=1; uiCptChart+=1
    self.ui.treeWidget.hideColumn(uiCpt)
    uiCpt+=1
  # Selection des labels
  if( ( ttConfig["PRODUCT"]["uiAUXNumber"] > 2 ) and ( ttMeasure[0]["sAUX3_Assign"] != "EMPTY" ) ):
   if( ttMeasure[0]["bAUX3"] ):
    self.ui.treeWidget.showColumn(uiCpt)
    self.chartData.vFAddSeries(uiCptChart)
    uiCpt+=1; uiCptChart+=1
    self.ui.treeWidget.showColumn(uiCpt)
    uiCpt+=1
   else:
    self.ui.treeWidget.hideColumn(uiCpt)
    self.chartData.vFRemoveSeries(uiCptChart)
    uiCpt+=1; uiCptChart+=1
    self.ui.treeWidget.hideColumn(uiCpt)
    uiCpt+=1
  # Selection des labels
  if( ( ttConfig["PRODUCT"]["uiAUXNumber"] > 3 ) and ( ttMeasure[0]["sAUX4_Assign"] != "EMPTY" ) ):
   if( ttMeasure[0]["bAUX4"] ):
    self.ui.treeWidget.showColumn(uiCpt)
    self.chartData.vFAddSeries(uiCptChart)
    uiCpt+=1; uiCptChart+=1
    self.ui.treeWidget.showColumn(uiCpt)
    uiCpt+=1
   else:
    self.ui.treeWidget.hideColumn(uiCpt)
    self.chartData.vFRemoveSeries(uiCptChart)
    uiCpt+=1; uiCptChart+=1
    self.ui.treeWidget.hideColumn(uiCpt)
    uiCpt+=1
  # Selection des labels
  if( ( ttConfig["PRODUCT"]["uiAUXNumber"] > 4 ) and ( ttMeasure[0]["sAUX5_Assign"] != "EMPTY" )  ):
   if( ttMeasure[0]["bAUX5"] ):
    self.ui.treeWidget.showColumn(uiCpt)
    self.chartData.vFAddSeries(uiCptChart)
    uiCpt+=1; uiCptChart+=1
    self.ui.treeWidget.showColumn(uiCpt)
    uiCpt+=1
   else:
    self.ui.treeWidget.hideColumn(uiCpt)
    self.chartData.vFRemoveSeries(uiCptChart)
    uiCpt+=1; uiCptChart+=1
    self.ui.treeWidget.hideColumn(uiCpt)
    uiCpt+=1
  # Selection des labels
  if( ( ttConfig["PRODUCT"]["uiAUXNumber"] > 5 ) and ( ttMeasure[0]["sAUX6_Assign"] != "EMPTY" )  ):
   if( ttMeasure[0]["bAUX6"] ):
    self.ui.treeWidget.showColumn(uiCpt)
    self.chartData.vFAddSeries(uiCptChart)
    uiCpt+=1; uiCptChart+=1
    self.ui.treeWidget.showColumn(uiCpt)
    uiCpt+=1
   else:
    self.ui.treeWidget.hideColumn(uiCpt)
    self.chartData.vFRemoveSeries(uiCptChart)
    uiCpt+=1; uiCptChart+=1
    self.ui.treeWidget.hideColumn(uiCpt)
    uiCpt+=1
  # Ammonia affichage ou pas
  if( ttConfig["CALCULATED"]["AMMONIA"]["bActivated"] ):
   if( ttMeasure[0]["bAmmonia"] ):
    self.ui.treeWidget.showColumn(uiCpt)
    self.chartData.vFAddSeries(uiCptChart)
    uiCpt+=1; uiCptChart+=1
   else:
    self.ui.treeWidget.hideColumn(uiCpt)
    self.chartData.vFRemoveSeries(uiCptChart)
    uiCpt+=1; uiCptChart+=1

  # Redéfinit le mode de sélection
  self.ui.treeWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
  self.ui.treeWidget.setSelectionMode(QAbstractItemView.MultiSelection)

 #--------------------------------------------------------------------------
 # Désélection de toutes les voies
 #--------------------------------------------------------------------------
 def vDataDeselectAllChannel( self, ttConfig, ttMeasure ):
  print("-- vDataDeselectAllChannel --")

  ttMeasure[0]["tBattCheckbox"].setCheckState( Qt.Unchecked )
  ttMeasure[0]["tTemperatureCheckbox"].setCheckState( Qt.Unchecked )
  ttMeasure[0]["tDepthCheckbox"].setCheckState( Qt.Unchecked )
  ttMeasure[0]["tBaroCheckbox"].setCheckState( Qt.Unchecked )
  ttMeasure[0]["tpHCheckbox"].setCheckState( Qt.Unchecked )
  ttMeasure[0]["tpHmvCheckbox"].setCheckState( Qt.Unchecked )
  ttMeasure[0]["tORPCheckbox"].setCheckState( Qt.Unchecked )
  ttMeasure[0]["tDOCheckbox"].setCheckState( Qt.Unchecked )
  ttMeasure[0]["tDO_PCCheckbox"].setCheckState( Qt.Unchecked )
  ttMeasure[0]["tECCheckbox"].setCheckState( Qt.Unchecked )
  ttMeasure[0]["tSalinityCheckbox"].setCheckState( Qt.Unchecked )
  ttMeasure[0]["tSSGCheckbox"].setCheckState( Qt.Unchecked )
  ttMeasure[0]["tTDSCheckbox"].setCheckState( Qt.Unchecked )
  if( ttMeasure[0]["sAUX1_Assign"] != "EMPTY" ): ttMeasure[0]["tAUX1Checkbox"].setCheckState( Qt.Unchecked )
  if( ttMeasure[0]["sAUX2_Assign"] != "EMPTY" ): ttMeasure[0]["tAUX2Checkbox"].setCheckState( Qt.Unchecked )
  if( ttMeasure[0]["sAUX3_Assign"] != "EMPTY" ): ttMeasure[0]["tAUX3Checkbox"].setCheckState( Qt.Unchecked )
  if( ttMeasure[0]["sAUX4_Assign"] != "EMPTY" ): ttMeasure[0]["tAUX4Checkbox"].setCheckState( Qt.Unchecked )
  if( ttMeasure[0]["sAUX5_Assign"] != "EMPTY" ): ttMeasure[0]["tAUX5Checkbox"].setCheckState( Qt.Unchecked )
  if( ttMeasure[0]["sAUX6_Assign"] != "EMPTY" ): ttMeasure[0]["tAUX6Checkbox"].setCheckState( Qt.Unchecked )
  if( ttConfig["CALCULATED"]["AMMONIA"]["bActivated"] ): ttMeasure[0]["tAmmoniaCheckbox"].setCheckState( Qt.Unchecked )
  #
  ttMeasure[0]["bBatt"]         = False
  ttMeasure[0]["bTemperature"]  = False
  ttMeasure[0]["bDepth"]        = False
  ttMeasure[0]["bBaro"]         = False
  ttMeasure[0]["bpH"]           = False
  ttMeasure[0]["bpHmv"]         = False
  ttMeasure[0]["bORP"]          = False
  ttMeasure[0]["bDO"]           = False
  ttMeasure[0]["bDO_PC"]        = False
  ttMeasure[0]["bEC"]           = False
  ttMeasure[0]["bAmmonia"]      = False
  ttMeasure[0]["bSalinity"]     = False
  ttMeasure[0]["bSSG"]          = False
  ttMeasure[0]["bTDS"]          = False
  ttMeasure[0]["bAUX1"]         = False
  ttMeasure[0]["bAUX2"]         = False
  ttMeasure[0]["bAUX3"]         = False
  ttMeasure[0]["bAUX4"]         = False
  ttMeasure[0]["bAUX4"]         = False
  ttMeasure[0]["bAUX5"]         = False
  ttMeasure[0]["bAUX6"]         = False
  ttMeasure[0]["bAmmonia"]      = False
  # Application de la nouvelle sélection
  self.vDataTreeviewHideColumn( ttConfig, ttMeasure )

 #--------------------------------------------------------------------------
 # Sélection de toutes les voies
 #--------------------------------------------------------------------------
 def vDataSelectAllChannel( self, ttConfig, ttMeasure ):
  print("-- vDataSelectAllChannel --")
  # Modification état checkbox
  ttMeasure[0]["tBattCheckbox"].setCheckState( Qt.Checked )
  ttMeasure[0]["tTemperatureCheckbox"].setCheckState( Qt.Checked )
  ttMeasure[0]["tDepthCheckbox"].setCheckState( Qt.Checked )
  ttMeasure[0]["tBaroCheckbox"].setCheckState( Qt.Checked )
  ttMeasure[0]["tpHCheckbox"].setCheckState( Qt.Checked )
  ttMeasure[0]["tpHmvCheckbox"].setCheckState( Qt.Checked )
  ttMeasure[0]["tORPCheckbox"].setCheckState( Qt.Checked )
  ttMeasure[0]["tDOCheckbox"].setCheckState( Qt.Checked )
  ttMeasure[0]["tDO_PCCheckbox"].setCheckState( Qt.Checked )
  ttMeasure[0]["tECCheckbox"].setCheckState( Qt.Checked )
  ttMeasure[0]["tSalinityCheckbox"].setCheckState( Qt.Checked )
  ttMeasure[0]["tSSGCheckbox"].setCheckState( Qt.Checked )
  ttMeasure[0]["tTDSCheckbox"].setCheckState( Qt.Checked )
  if( ttMeasure[0]["sAUX1_Assign"] != "EMPTY" ): ttMeasure[0]["tAUX1Checkbox"].setCheckState( Qt.Checked )
  if( ttMeasure[0]["sAUX2_Assign"] != "EMPTY" ): ttMeasure[0]["tAUX2Checkbox"].setCheckState( Qt.Checked )
  if( ttMeasure[0]["sAUX3_Assign"] != "EMPTY" ): ttMeasure[0]["tAUX3Checkbox"].setCheckState( Qt.Checked )
  if( ttMeasure[0]["sAUX4_Assign"] != "EMPTY" ): ttMeasure[0]["tAUX4Checkbox"].setCheckState( Qt.Checked )
  if( ttMeasure[0]["sAUX5_Assign"] != "EMPTY" ): ttMeasure[0]["tAUX5Checkbox"].setCheckState( Qt.Checked )
  if( ttMeasure[0]["sAUX6_Assign"] != "EMPTY" ): ttMeasure[0]["tAUX6Checkbox"].setCheckState( Qt.Checked )
  if( ttConfig["CALCULATED"]["AMMONIA"]["bActivated"] ): ttMeasure[0]["tAmmoniaCheckbox"].setCheckState( Qt.Checked )
  #
  # Etat de l'affichage
  ttMeasure[0]["bBatt"]         = True
  ttMeasure[0]["bTemperature"]  = True
  ttMeasure[0]["bDepth"]        = True
  ttMeasure[0]["bBaro"]         = True
  ttMeasure[0]["bpH"]           = True
  ttMeasure[0]["bpHmv"]         = True
  ttMeasure[0]["bORP"]          = True
  ttMeasure[0]["bDO"]           = True
  ttMeasure[0]["bDO_PC"]        = True
  ttMeasure[0]["bEC"]           = True
  ttMeasure[0]["bAmmonia"]      = True
  ttMeasure[0]["bSalinity"]     = True
  ttMeasure[0]["bSSG"]          = True
  ttMeasure[0]["bTDS"]          = True
  if( ttConfig["PRODUCT"]["uiAUXNumber"] > 0 ): ttMeasure[0]["bAUX1"] = True
  else:                                         ttMeasure[0]["bAUX1"] = False
  if( ttConfig["PRODUCT"]["uiAUXNumber"] > 1 ): ttMeasure[0]["bAUX2"] = True
  else:                                         ttMeasure[0]["bAUX2"] = False
  if( ttConfig["PRODUCT"]["uiAUXNumber"] > 2 ): ttMeasure[0]["bAUX3"] = True
  else:                                         ttMeasure[0]["bAUX3"] = False
  if( ttConfig["PRODUCT"]["uiAUXNumber"] > 3 ): ttMeasure[0]["bAUX4"] = True
  else:                                         ttMeasure[0]["bAUX4"] = False
  if( ttConfig["PRODUCT"]["uiAUXNumber"] > 4 ): ttMeasure[0]["bAUX5"] = True
  else:                                         ttMeasure[0]["bAUX5"] = False
  if( ttConfig["PRODUCT"]["uiAUXNumber"] > 5 ): ttMeasure[0]["bAUX6"] = True
  else:                                         ttMeasure[0]["bAUX6"] = False
  if( ttConfig["CALCULATED"]["AMMONIA"]["bActivated"] ): ttMeasure[0]["bAmmonia"] = True
  else:                                                  ttMeasure[0]["bAmmonia"] = False
  # Application de la nouvelle sélection
  self.vDataTreeviewHideColumn( ttConfig, ttMeasure )

 #--------------------------------------------------------------------------
 # Affichage ou non des lignes du tableau
 #--------------------------------------------------------------------------
 def vDataTreeviewDatetimeChanged( self, tDateTime, ttConfig, ttMeasure ):
  print("-- vDataTreeviewDatetimeChanged --")

  # Récupération des dates de début et de fin
  tDateTimeStart = self.ui.dateTimeEdit_dataStart.dateTime()
  tDateTimeEnd   = self.ui.dateTimeEdit_dataEnd.dateTime()

  # Si supérieur on force au max
  #if( tDateTimeStart > tDateTimeEnd ): tDateTimeStart = tDateTimeEnd
  # La date de fin minimum est égal ou supérieur à la date de début
  self.ui.dateTimeEdit_dataEnd.setMinimumDateTime(tDateTimeStart)
  # La date de start minimum est égal ou supérieur à la date de fin
  self.ui.dateTimeEdit_dataStart.setMaximumDateTime(tDateTimeEnd)

  # Masquage de tout ce qui sort des bornes

  # Parcourt de l'ensemble des points
  for ucPoint in range(len(ttMeasure)):
   # Datetime du point
   tDateTime = QDateTime.fromString(ttMeasure[ucPoint]["sDateTime"], "yyyy/MM/dd HH:mm:ss")
   # Test si date sample est inférieur à date start
   if(  ( tDateTime < tDateTimeStart )
     or ( tDateTime > tDateTimeEnd ) ):
    # Hide l'échantillon
    tInvisibleRootItem = self.ui.treeWidget.invisibleRootItem()
    # QModelIndex QTreeWidget::indexFromItem(const QTreeWidgetItem *item, int column = 0) const
    tModelIndex = self.ui.treeWidget.indexFromItem(tInvisibleRootItem)
    # PySide6.QtWidgets.QTreeView.setRowHidden(int, Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex], bool)
    self.ui.treeWidget.setRowHidden(ucPoint, tModelIndex, True)
   else:
    # Hide l'échantillon
    tInvisibleRootItem = self.ui.treeWidget.invisibleRootItem()
    # QModelIndex QTreeWidget::indexFromItem(const QTreeWidgetItem *item, int column = 0) const
    tModelIndex = self.ui.treeWidget.indexFromItem(tInvisibleRootItem)
    # PySide6.QtWidgets.QTreeView.setRowHidden(int, Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex], bool)
    self.ui.treeWidget.setRowHidden(ucPoint, tModelIndex, False)

 #----------------------------------------------
 # Data - Changement de mode tableau de donnée ou graphique
 #----------------------------------------------
 def vFDATAChangeDataViewMode( self, uiIndex ):
  print("-- vFDATAChangeDataViewMode --")
  self.ui.stackedWidget_DataTabChart.setCurrentIndex(int(uiIndex))

 #----------------------------------------------
 # PC Conf - Graphical Depth change
 #----------------------------------------------
 def vFPCONFChangeGraphicalDepth( self, sValue ):
  print("-- vFPCONFChangeGraphicalDepth --")
  # Mise à jour du label
  self.ui.label_Config_GraphDepth.setText(sValue)
  # Mise à jour des graphiques
  self.chart.vFClear()
  self.chart.vFSetSampleDepth(int(self.tINIConfig["SOFTWARE"]["graphical_depth"]))
  try:
   self.chartCalib.vFClear()
   self.chartCalib.vFSetSampleDepth(int(self.tINIConfig["SOFTWARE"]["graphical_depth"]))
  except Exception as err:
   print(err)
  try:
   self.chartData.vFClear()
   self.chartData.vFSetSampleDepth(int(self.tINIConfig["SOFTWARE"]["graphical_depth"]))
  except Exception as err:
   print(err)

 #----------------------------------------------
 # PC Conf - Display calculated
 #----------------------------------------------
 def vFPCONFDisplayCalculated( self, sValue ):
  print("-- vFPCONFDisplayCalculated --")
  # Mise à jour du label
  self.ui.label_Config_DisplayCalculated.setText(sValue)
  # Display calculated
  if( sValue == "Enable" ):
   self.ui.widget_CalculatedResult.setVisible(True)
  else:
   self.ui.widget_CalculatedResult.setVisible(False)

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

