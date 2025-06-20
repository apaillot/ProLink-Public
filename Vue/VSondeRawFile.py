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
from Vue.py_toggle      import PyToggle

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
class VSondeRawFile(QObject):

 #----------------------------------------------
 # Init
 #----------------------------------------------
 def __init__(self, tParent, tINIFile, tUI):
  super().__init__(tParent)
  print("VSondeRawFile init")
  # Conservation INIFile
  self.tINIConfig = tINIFile.tConfig
  self.tINIFile   = tINIFile
  #
  self.ui = tUI
  # Fenêtre parent
  self.tParent = tParent

 #----------------------------------------------
 # Affichage des onglets
 #----------------------------------------------
 def vFDisplayProductNav( self ):
  #self.ui.connexion_btn.setVisible(False)
  self.ui.dashboard_btn.setVisible(True)
  self.ui.liveview_btn.setVisible(False)
  self.ui.calibration_btn.setVisible(False)
  self.ui.data_btn.setVisible(True)
  self.ui.pcConfig_btn.setVisible(True)

 #----------------------------------------------
 # Init du mode Fichier raw lecture
 #----------------------------------------------
 def vFVSondeRawFileInitMode( self ):
   #-- Cache l'inutile --
  self.ui.widget_SondeInfoInterface.setVisible(False)
  #self.ui.groupBox_EstimatedLogLife.setVisible(False)
  self.ui.groupBox_SondeClock.setVisible(False)
  self.ui.groupBox_Averaging.setVisible(False)
  self.ui.widget_DashboardNavBtn.setVisible(False)
  self.ui.getMeasureData_btn.setVisible(False)
  # Data
  self.ui.exportToRAW_btn.setVisible(False)
  # Conf box
  self.ui.groupBox_PCConf_AppSettings.setVisible(False)
  self.ui.groupBox_PCConf_Measure.setVisible(True)

  # Pas de modification possible en mode lecture
  #self.ui.widget_BatteryRemaining.setStyleSheet("")
  self.ui.groupBox_SondeClock.setStyleSheet("")
  self.ui.groupBox_SiteIDLocation.setStyleSheet("")
  self.ui.groupBox_SetupLogRate.setStyleSheet("")
  #self.ui.groupBox_EstimatedLogLife.setStyleSheet("")
  self.ui.groupBox_EventLogging.setStyleSheet("")
  self.ui.widget_OpticalAveraging.setStyleSheet("")

  self.ui.label_setSiteID.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version - W.svg") )
  self.ui.label_setSiteLatitude.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version - W.svg") )
  self.ui.label_setSiteLong.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version - W.svg") )
  self.ui.label_setLogDataEvery.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version - W.svg") )
  self.ui.label_setCleanEvery.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version - W.svg") )
  self.ui.label_setEventLogState.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version - W.svg") )
  self.ui.label_setEventLogCheck.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version - W.svg") )
  self.ui.label_setEventLogEvery.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version - W.svg") )
  self.ui.label_setEventLogThreshold.setPixmap( QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version - W.svg") )


 #----------------------------------------------
 # Affichage configuration
 #----------------------------------------------
 def vFDisplayGeneralConfiguration( self, ttConfig, sCom="" ):
  print("-- vFDisplayGeneralConfiguration --")
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
   self.ui.label_logoEventLogEvery.setPixmap( QPixmap(":/Logo/Dashboard/7-Event-logging/3-Every.svg") )
   self.ui.label_txtEventLogEvery.setStyleSheet("color: #000000;")
   self.ui.label_EventLogEvery.setStyleSheet("color: rgb(84,84,84);")
   self.ui.label_logoEventLogThreshold.setPixmap( QPixmap(":/Logo/Dashboard/7-Event-logging/4-Log-data-if.svg") )
   self.ui.label_txtEventLogThreshold.setStyleSheet("color: #000000;")
   self.ui.label_EventLogThreshold.setStyleSheet("color: rgb(84,84,84);")
  else:
   self.ui.label_EventLogState.setText( "Disable" )
   self.ui.label_logoEventLogCheck.setPixmap( QPixmap(":/Logo/Dashboard/7-Event-logging/2-Check-grey.svg") )
   self.ui.label_txtEventLogCheck.setStyleSheet("color: #888888;")
   self.ui.label_EventLogCheck.setStyleSheet("color: #888888;")
   self.ui.label_logoEventLogEvery.setPixmap( QPixmap(":/Logo/Dashboard/7-Event-logging/3-Every-grey.svg") )
   self.ui.label_txtEventLogEvery.setStyleSheet("color: #888888;")
   self.ui.label_EventLogEvery.setStyleSheet("color: #888888;")
   self.ui.label_logoEventLogThreshold.setPixmap( QPixmap(":/Logo/Dashboard/7-Event-logging/4-Log-data-if-grey.svg") )
   self.ui.label_txtEventLogThreshold.setStyleSheet("color: #888888;")
   self.ui.label_EventLogThreshold.setStyleSheet("color: #888888;")
  self.ui.label_EventLogCheck.setText( str(ttConfig["PRODUCT"]["sLOG_SENSOR"]) )
  self.ui.label_EventLogEvery.setText( str(ttConfig["PRODUCT"]["uiEVENT_HOUR"])+"h "+str(ttConfig["PRODUCT"]["uiEVENT_MIN"])+"min" )
  self.ui.label_EventLogThreshold.setText( str(ttConfig["PRODUCT"]["uiEVENT_CHANGE"])+" %" )
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

  #-------------------------------------------
  # PC Configuration
  #-------------------------------------------

  # Ouverture OK, Affichage OK
  # Seulement quand en connexion
  if( self.ui.stackedWidget.currentIndex() == 0 ):
   # Ouverture de l'onglet dashboard
   self.vFNavASBtnClicked(1)

 #----------------------------------------------
 # NAV - Gestion menu bouton nav
 #----------------------------------------------
 def vFNavASBtnClicked( self, uiIndex ):
  tBtnNav = [
   self.ui.connexion_btn,
   self.ui.dashboard_btn,
   self.ui.liveview_btn,
   self.ui.data_btn,
   self.ui.calibration_btn,
   self.ui.about_btn,
   self.ui.pcConfig_btn
  ]
  # Modification page affichée
  self.ui.stackedWidget.setCurrentIndex(uiIndex)
  self.ui.stackedWidget_Nav2.setCurrentIndex(uiIndex)
  # Gestion de la ligne blanche gauche du bouton nav active
  for uiCpt in range(len(tBtnNav)):
   if( tBtnNav[uiCpt] == None ): continue
   if( uiCpt == uiIndex ) :
    tBtnNav[uiCpt].setStyleSheet("background-color: #3E4072;border-left: 3px solid rgb(255,255,255);");
   else:
    tBtnNav[uiCpt].setStyleSheet("");
  # Conservation de l'onglet actif
  self.uiNavActivePage = uiIndex

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
  #tWidget.setStyleSheet("*:hover{background-color: #efefef;}")
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
  pixmap = QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version - W.svg")
  '''
  if( ucChannel < 0 ): pixmap = QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version.svg - W")
  else:
   if( tChannel["sIndex"] == "EMPTY" ): pixmap = QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version-grey.svg")
   else:                                pixmap = QPixmap(":/Logo/Dashboard/Sonde info/3-Software-version.svg")
  '''
  tLogoLabel.setPixmap(pixmap)
  tLogoLabel.setScaledContents(True)
  tLogoLabel.setMaximumSize(20, 20)
  tWidget.layout().addWidget(tLogoLabel)
  # Ajout d'un widget dans un widget en utilisant son layout interne
  self.ui.groupBox_DashboardSensors.layout().addWidget(tWidget)
  # Ajout de l'event sur ligne
  #self.xDashboardChannelSelectConnectSignal.emit( ucChannel, tChannel, tWidget )

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

  #------- Ajout d'un checkbox
  #def vFAddCheckbox( sTxt, uiRow, uicolumn, ttConfig, ttMeasure, sChannelBoolIndex ):
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

  ##TODO ---------------------
  # Effacement checkbox

  # Création des
  vbox = QVBoxLayout(); self.ui.groupBox_Environment.setLayout(vbox)
  vbox = QVBoxLayout(); self.ui.groupBox_pHORPDOEC.setLayout(vbox)
  vbox = QVBoxLayout(); self.ui.groupBox_calculated.setLayout(vbox)
  vbox = QVBoxLayout(); self.ui.groupBox_Aux.setLayout(vbox)

  # Nettoyage
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
  #self.ui.treeWidget.setColumnCount(0)

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
 # PC Conf - EC Ref Temperature
 #----------------------------------------------
 def vFPCONFChangeECRefTemperature( self, sValue ):
  print("-- vFPCONFChangeECRefTemperature --")
  # Mise à jour du label
  self.ui.label_Config_ECRefTemp.setText(sValue)

 #----------------------------------------------
 # PC Conf - Temperature Unit
 #----------------------------------------------
 def vFPCONFChangeTemperatureUnit( self, sValue ):
  print("-- vFPCONFChangeTemperatureUnit --")
  # Mise à jour du label PCConf
  self.ui.label_Config_TempUnit.setText(sValue)
  # Liveview - Temp
  if( sValue == "F" ):
   self.tMeasureBox[0]["tLabelUnit"].setText("(degF)")
  else:
   self.tMeasureBox[0]["tLabelUnit"].setText("(degC)")

 #----------------------------------------------
 # PC Conf - Depth unit
 #----------------------------------------------
 def vFPCONFChangeDepthUnit( self, sValue ):
  print("-- vFPCONFChangeDepthUnit --")
  # Mise à jour du label
  self.ui.label_Config_DepthUnit.setText(sValue)
  # Liveview - Temp
  if( sValue == "f" ):
   self.tMeasureBox[1]["tLabelUnit"].setText("(f)")
  else:
   self.tMeasureBox[1]["tLabelUnit"].setText("(m)")

 #----------------------------------------------
 # PC Conf - TDS Factor
 #----------------------------------------------
 def vFPCONFChangeTDSFactor( self, fText ):
  print("-- vFPCONFChangeTDSFactor --")
  # Mise à jour du label
  self.ui.label_Config_TDSFactor.setText(("%.2f"%fText))

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
