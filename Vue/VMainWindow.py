# This Python file uses the following encoding: utf-8

#============================================================================#
# Librairies système
#============================================================================#
import sys
import io, csv
import time
#from maps import MapCreator
from enum import Enum, IntEnum
# Création carte
#import folium

#============================================================================#
# Librairies Qt
#============================================================================#
from PySide6.QtCore import QUrl, Signal, Slot, Qt, QTimer
from PySide6.QtWidgets import ( QApplication, QMainWindow, QListWidgetItem, QWidget, QLabel,
                                QHBoxLayout, QVBoxLayout, QSplashScreen, QGraphicsDropShadowEffect )
from PySide6.QtGui     import QPixmap, QColor, QPainter
from PySide6.QtWidgets import *
from PySide6.QtCharts  import QChart, QChartView, QLineSeries

#============================================================================#
# Librairies Utilisateur
#============================================================================#
from ui_form    import Ui_MainWindow
from Controleur import CMainWindow
import ressource_rc
from Vue.VChart import VChart, tSensorColor
from Vue.Windows.UIBackground                 import UIBackground
from Vue.Windows.UILoadingScreen              import LoadingScreen
from Vue.Windows.UIInfo                       import UIInfo
from Vue.Windows.Update.UIUpdateDetected      import UIUpdateDetected
from Vue.Windows.Update.UIUpdateProgress      import UIUpdateProgress
from Vue.Windows.Dashboard.UIBatteryRemaining import UIBatteryRemaining
from Vue.Windows.Dashboard.UIEstimatedMemory  import UIEstimatedMemory
from Vue.Windows.Dashboard.UIEstimatedBattery import UIEstimatedBattery
from Vue.Windows.Calibration.UIStab           import UIStab
from Vue.Windows.Calibration.UIGSFactor       import UIGSFactor
from Vue.Windows.Data.UIDataGetWait           import UIDataGetWait
from Vue.Windows.PCConf.UIDepthUnit           import UIDepthUnit
from Vue.Windows.PCConf.UIECRefTemp           import UIECRefTemp
from Vue.Windows.PCConf.UIGraphicalDepth      import UIGraphicalDepth
from Vue.Windows.PCConf.UITDSFactor           import UITDSFactor
from Vue.Windows.PCConf.UITempUnit            import UITempUnit
from Vue.Windows.PCConf.UIDisplayCalculated   import UIDisplayCalculated
from TVersion           import *
from Vue.VMainWindowLib import *
from Vue.VLib           import *
from Vue.VSonde         import VSonde
from Vue.VProbe         import VProbe
from Vue.VSondeRawFile  import VSondeRawFile
from Vue.VLeveLine      import VLeveLine

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
class VMainWindow(QMainWindow):
 # Signal de fin d'init de la vue
 xEndInitSignal = Signal()
 # Signal connection sonde
 xConnectionSondeSelectConnectSignal = Signal( str, QWidget )
 # Signal connection probe
 xConnectionProbeSelectConnectSignal = Signal( str, QWidget )
 # Signal connection sonde
 xConnectionLeveLineSelectConnectSignal = Signal( str, QWidget )

 # Sonde
 #-- Calibration
 # Signal pour valider la calibration
 xCalibrationPointCalibrateSignal      = Signal( str, int, dict, QWidget, int )

 #----------------------------------------------
 # Init
 #----------------------------------------------
 def __init__(self, tINIFile, parent=None):
  print("VMainWindow init")
  #super(VSonde, self).__init__(parent)
  super().__init__(parent)
  #QMainWindow.__init__(self, parent, tINIFile)
  #VSonde.__init__(self, tINIFile)
  #VSonde.__init__(self, tINIFile)
  #QMainWindow.__init__(self)

  # Initialisation GUI
  self.ui = Ui_MainWindow()
  self.ui.setupUi(self)
  ##-----------------
  ## DEBUG
  # Pour version spécifique livraison
  #self.ui.pushButton_detectProbe.setVisible(False)
  self.ui.pushButton_detectLeveLine.setVisible(False)
  # Cache
  self.ui.widget_ProbeAUXCalValue_Point.setVisible(False)
  ##-----------------

  #---------
  # Déclaration objet
  #---------
  self.tVSonde        = VSonde(self, tINIFile, self.ui)
  self.tVProbe        = VProbe(self, tINIFile, self.ui)
  self.tVSondeRawFile = VSondeRawFile(self, tINIFile, self.ui)
  self.tVLeveLine     = VLeveLine(self, tINIFile, self.ui)
  # APPLY JSON STYLESHEET
  #loadJsonStyle(self, self.ui)
  # Map
  #file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "my_map.html"))
  #local_url = QUrl.fromLocalFile(file_path)
  # Affichage carte
  #self.vFDisplayMap()

  # Conservation INIFile
  self.tINIConfig = tINIFile.tConfig
  # -- Création fenêtre --
  # - Général -
  self.tUIBackground    = UIBackground(self)
  self.UIUpdateDetected = UIUpdateDetected(self)
  self.UIUpdateProgress = UIUpdateProgress(self)
  self.tUILoadingScreen = LoadingScreen(self)
  self.tUIInfo          = UIInfo(self)
  # - Dashboard -
  self.tUIBatteryRemaining = UIBatteryRemaining( self )
  self.tUIEstimatedMemory  = UIEstimatedMemory( self )
  self.tUIEstimatedBattery = UIEstimatedBattery( self )
  # - Calibration -
  self.tUIStab          = UIStab(self)
  self.tUIGSFactor      = UIGSFactor(self)
  # - Data -
  self.tUIDataGetWait   = UIDataGetWait(self)
  # - PC Conf -
  self.tUIDepthUnit         = UIDepthUnit(self)
  self.tUIECRefTemp         = UIECRefTemp(self)
  self.tUIGraphicalDepth    = UIGraphicalDepth(self)
  self.tUITDSFactor         = UITDSFactor(self)
  self.tUITempUnit          = UITempUnit(self)
  self.tUIDisplayCalculated = UIDisplayCalculated(self)

  # Création variable emplacement mesure
  self.tMeasureBox      = []

  # Nav - Nav invisible
  self.ui.connexion_btn.setVisible(True)
  self.ui.dashboard_btn.setVisible(False)
  self.ui.liveview_btn.setVisible(False)
  self.ui.data_btn.setVisible(False)
  self.ui.calibration_btn.setVisible(False)
  self.ui.pcConfig_btn.setVisible(False) # A voir si utile

  # Connexion - Cache
  self.ui.widget_onlineHelp.setVisible(False)
  #self.ui.pushButton_detectLeveLine.setVisible(False)

  # Dashboard - Cache le bouton de test
  self.ui.pushButton_TestDashboard.setVisible(False)

  # Liveview - Bouton stop invisible par défaut
  self.ui.stopMeasure_btn.setVisible(False)
  # Liveview - Cache calculated result
  #self.ui.groupBox_CalculatedResult.setVisible(False)
  # Liveview - Cache bouton Stop logging
  self.ui.pushButton_LiveViewRecordStop.setVisible(False)
  # Liveview - De base set probe Baro invisible
  self.ui.pushButton_LiveviewSetBaro.setVisible(False)
  # Calib - De base set probe Baro invisible
  self.ui.setBaroCal_btn.setVisible(False)

  # Data - Clear du tableau de donnée
  self.ui.treeWidget.clear()
  self.ui.treeWidget.setColumnCount(0)
  # Data - Cache bouton export RAW
  self.ui.exportToRAW_btn.setVisible(False)

  # Calibration - Init valeur
  self.ui.stackedWidget_calibrationMain.setCurrentIndex(0)
  # Calibration - Bouton Export to pdf non visible pour le moment
  self.ui.exportToPdf_btn.setVisible(False)
  # Calibration - Cache bouton Stop logging
  self.ui.pushButton_CalibRecordStop.setVisible(False)

  # Data - Bouton export to CSV non visible pour le moment
  self.ui.exportToCSV_btn.setVisible(False)
  self.ui.exportToTAB_btn.setVisible(False)
  self.ui.exportToRAW_btn.setVisible(False)

  # Changement d'onglet vers connexion
  self.ui.stackedWidget.setCurrentIndex(0)
  self.ui.stackedWidget_Nav2.setCurrentIndex(0)

  # Modification version logiciel
  print("PC Software Version = "+sGlobalSoftwareVersion)
  self.ui.version_label.setText(sGlobalSoftwareVersion)
  # Si pas en debug
  if( int(self.tINIConfig["GLOBAL"]["debug"]) == 0 ):
   # SplashScreen
   self.tSplash = QSplashScreen();
   self.tSplash.setPixmap(QPixmap(":/Logo/Splashscreen/Splash_Screen_-_Aquaread.png"));
   self.tSplash.show();
   # Maintient 2 secondes du splash screen
   self.tSplashTimer = QTimer(self)
   self.tSplashTimer.timeout.connect(self.vFCloseSplashOpenMainWindow)
   self.tSplashTimer.start(2000)

  # Connexion - Création layout
  self.ui.widget_ConnectSondeList.setLayout(QVBoxLayout())

  # Signal de fin d'init
  self.xEndInitSignal.emit()

 #-----------------------------
 # General - Fermeture splashscreen/ouverture main window
 #-----------------------------
 def vFCloseSplashOpenMainWindow(self):
  self.tSplash.close()
  self.show()

 #----------------------------------------------
 # NAV - Gestion menu bouton nav
 #----------------------------------------------
 """
 def vFNavASBtnClicked( self, uiIndex ):
  print("-- VMainWindow > vFNavASBtnClicked --")
  tBtnNav = [
   self.ui.connexion_btn,   # 0
   self.ui.dashboard_btn,   # 1
   self.ui.liveview_btn,    # 2
   self.ui.data_btn,        # 3
   self.ui.calibration_btn, # 4
   self.ui.about_btn,       # 5
   self.ui.pcConfig_btn     # 6
  ]
  # Si on est en mode liveview activé
  if(   ( self.ui.stackedWidget.currentIndex() == 2 )
    and ( self.ui.stopMeasure_btn.isVisible() ) ):
   print("bloque")
   vFAlert(self, "Warning", "Please stop liveview to change tab")
   # On quitte pour bloquer
   return

  # Si on est en mode calibration en cours
  if( self.ui.stackedWidget_calibrationMain.currentIndex() == 1 ):
   print("bloque")
   vFAlert(self, "Warning", "Please stop current calibration to change tab")
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
 """

 #----------------------------------------------
 # Affichage de la carte avec les points de mesure
 #----------------------------------------------
 def vFDisplayMap( self ):
  print("-- vFDisplayMap --")
  '''
  ##TODO - Externaliser la variable
  latlon = [ (47.794753, -3.276730, "DO=12.123<br>Chla=50.5"),
             (47.794097, -3.280239, 12.456),
             (47.793319, -3.288736, 12.523),
             (47.790991, -3.292888, 13.546) ]
  #mapit = folium.Map( location=[47.794753, -3.276730], zoom_start=6 )
  mapit = folium.Map( location=[47.794753, -3.276730] )
  for coord in latlon:
   folium.Marker( location=[ coord[0], coord[1] ], popup=coord[2], fill_color='#43d9de', radius=8 ).add_to( mapit )
  #Set the zoom to the maximum possible
  mapit.fit_bounds(mapit.get_bounds())

  self.ui.webEngineView.setHtml(mapit.get_root().render())
  '''

 #----------------------------------------------
 # Connexion - Suppression des boutons des autres types de produits
 #----------------------------------------------
 def vFDeleteDetectBtn( self, tCurrentBtn ):
  print("-- vFDeleteDetectBtn --")
  tBtnNav = [
   self.ui.pushButton_detectProduct,
   self.ui.pushButton_detectProbe,
   self.ui.pushButton_detectLeveLine,
   self.ui.pushButton_openRawFile
  ]
  # Désaffiche les boutons des autres type de produits
  for uiCpt in range(len(tBtnNav)):
   if( tBtnNav[uiCpt] == None ): continue
   if( tBtnNav[uiCpt] != tCurrentBtn ):
    tBtnNav[uiCpt].setVisible(False)
  # Suppression des photos
  self.ui.label_photoSonde.setVisible(False)
  self.ui.label_photoProbe.setVisible(False)
  self.ui.label_photoLeveLine.setVisible(False)

 #----------------------------------------------
 # Connexion - Affichage produit présent/détecté
 #----------------------------------------------
 def vFDisplaySondeDetected( self, tsProductList ):
  print("-- VMainWindow > vFDisplaySondeDetected --")
  print(range(self.ui.widget_ConnectSondeList.layout().count()))
  # Effacement des vieux produits - Clear du layout
  if( self.ui.widget_ConnectSondeList.layout().count() != 0 ):
   for i in reversed(range(self.ui.widget_ConnectSondeList.layout().count())):
    self.ui.widget_ConnectSondeList.layout().itemAt(i).widget().deleteLater()

  # Si produit détecté
  if( len(tsProductList) ):
   # Parcourt des sondes détectées
   for tElt in tsProductList:
    # Ajout au layout
    self.vFConnectionAddSondeLine(tElt, tsProductList[tElt])
   print("Fin d'ajout des lignes")
   # Alignement produit détecté
   self.ui.widget_ConnectSondeList.layout().setAlignment(Qt.AlignTop)
  # Pas de produit détecté
  else:
   #self.tUIBackground.close()
   #vFAlert( self, "Product detection",  "No product detected" )
   self.tUIInfo.vFOpen( "Product detection",  "No product detected" )

 #----------------------------------------------
 # Connexion - Affichage produit présent/détecté
 #----------------------------------------------
 def vFDisplayProbeDetected( self, tsProductList ):
  print("-- VMainWindow > vFDisplayProbeDetected --")
  print(range(self.ui.widget_ConnectSondeList.layout().count()))
  # Effacement des vieux produits - Clear du layout
  if( self.ui.widget_ConnectSondeList.layout().count() != 0 ):
   for i in reversed(range(self.ui.widget_ConnectSondeList.layout().count())):
    self.ui.widget_ConnectSondeList.layout().itemAt(i).widget().deleteLater()

  # Si produit détecté
  if( len(tsProductList) ):
   # Parcourt des sondes détectées
   for tElt in tsProductList:
    # Ajout au layout
    self.vFConnectionAddProbeLine(tElt, tsProductList[tElt])
   print("Fin d'ajout des lignes")
   # Alignement produit détecté
   self.ui.widget_ConnectSondeList.layout().setAlignment(Qt.AlignTop)
  # Pas de produit détecté
  else:
   #self.tUIBackground.close()
   #vFAlert( self, "Product detection",  "No product detected" )
   self.tUIInfo.vFOpen( "Product detection",  "No product detected" )

 """
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
 """

 #----------------------------------------------
 # Connection - Ajout d'une sonde
 #----------------------------------------------
 def vFConnectionAddSondeLine( self, sCOM, ttConfig ):

  # Container principal de la ligne
  tWidgetLine = QWidget()
  tWidgetLine.setContentsMargins(0,0,0,0)
  tWidgetLine.setMaximumSize(8000, 200)

  tEffect = QGraphicsDropShadowEffect(self)
  tEffect.setBlurRadius(20)
  tEffect.setXOffset(0)
  tEffect.setYOffset(0)
  #tEffect.setColor(Qt.black)
  tEffect.setColor(QColor(60, 60, 60, 60))
  tWidgetLine.setGraphicsEffect(tEffect)

  # Create a boxlayout (horizontal here)
  tBox = QHBoxLayout()
  tBox.setContentsMargins(10,10,10,10)
  tBox.setSpacing(15)
  # Set the layout for your tab
  tWidgetLine.setLayout(tBox)
  #--
  # Photo produit
  tProductPhoto = QLabel(self)
  tProductPhoto.setContentsMargins(0,0,0,0)
  tPixmap = QPixmap( self.sFDashboardGetSondeImageByID( ttConfig["PRODUCT"]["uiModel"] ) )
  tProductPhoto.setPixmap(tPixmap)
  tProductPhoto.setScaledContents(True)
  tProductPhoto.setMaximumSize(200, 200)
  tWidgetLine.layout().addWidget(tProductPhoto)
  #--
  # Info product
  tWidgetProductInfo = QWidget()
  tWidgetProductInfo.setMaximumSize(300, 200)
  tWidgetProductInfo.setContentsMargins(0,0,0,0)
  # Layout
  tVbox = QVBoxLayout();
  tVbox.setContentsMargins(0,0,0,0)
  tWidgetProductInfo.setLayout(tVbox);
  # Nom de la voie
  tLabel = QLabel()
  tLabel.setText( ttConfig["PRODUCT"]["sModel"] ) #"AP-6000 - COM4"
  tLabel.setMinimumSize(0, 50)
  tLabel.setStyleSheet("QLabel{font-size: 18pt;font-weight:600;color:#3e4072;}")
  tWidgetProductInfo.layout().addWidget(tLabel)
  # Numéro de série
  tLabel = QLabel()
  tLabel.setText( "SN: "+ttConfig["PRODUCT"]["sPSN1"] )
  tLabel.setStyleSheet("QLabel{color:#666;}")
  tWidgetProductInfo.layout().addWidget(tLabel)
  # Pourcentage mémoire
  tLabelMemory = QLabel()
  tLabelMemory.setText( "Memory: "+str(ttConfig["PRODUCT"]["uiMemRemainingPC"])+"%" + " - " +"Battery: "+str(ttConfig["PRODUCT"]["uiBATT_PC"])+"%")
  tLabelMemory.setStyleSheet("QLabel{color:#666;}")
  tLabelMemory.setMinimumSize(0, 20)
  tWidgetProductInfo.layout().addWidget(tLabelMemory)
  '''
  # Pourcentage batterie
  tLabelBattery = QLabel()
  tLabelBattery.setText( "Battery: "+str(ttConfig["PRODUCT"]["uiBATT_PC"])+"%" )
  tLabelBattery.setStyleSheet("QLabel{color:#666;}")
  tLabelBattery.setMinimumSize(0, 20)
  tWidgetProductInfo.layout().addWidget(tLabelBattery)
  '''
  # COM
  tLabelMemory = QLabel()
  tLabelMemory.setText( "Interface: "+sCOM )
  tLabelMemory.setStyleSheet("QLabel{color:#666;}")
  tLabelMemory.setMinimumSize(0, 20)
  tWidgetProductInfo.layout().addWidget(tLabelMemory)

  verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
  tWidgetProductInfo.layout().addItem(verticalSpacer)
  tProductConnectBtn = QPushButton()
  tProductConnectBtn.setText( "Connect" )
  tWidgetProductInfo.layout().addWidget(tProductConnectBtn)
  # Alignement des élements
  tWidgetProductInfo.layout().setAlignment(Qt.AlignTop)
  tWidgetLine.layout().addWidget(tWidgetProductInfo)
  #--
  # Carte
  '''
  tWidgetMap = QWidget()
  tWidgetMap.setMaximumSize(300, 200)
  tWidgetMap.setContentsMargins(0,0,0,0)
  tCoordinate = (46.7873953, -2.2952942)
  tFoliumMapProduct = folium.Map(
   title = "nke",
   location=tCoordinate
  )
  folium.Marker(location = tCoordinate).add_to(tFoliumMapProduct)
  # Save map  data to data object
  tIOData = io.BytesIO()
  tFoliumMapProduct.save(tIOData, close_file=False)
  # Webview
  tWebViewProduct = QWebEngineView()
  tWebViewProduct.setHtml(tIOData.getvalue().decode())
  # Layout
  tVbox = QVBoxLayout();
  tVbox.setContentsMargins(0,0,0,0)
  tWidgetMap.setLayout(tVbox);
  tWidgetMap.layout().addWidget(tWebViewProduct)
  # Ajout de la carte
  tWidgetLine.layout().addWidget(tWidgetMap)
  '''
  # Ajout de la nouvelle ligne au layout
  self.ui.widget_ConnectSondeList.layout().addWidget(tWidgetLine)
  # Ajout signal sur bouton connect
  self.xConnectionSondeSelectConnectSignal.emit( sCOM, tProductConnectBtn )

 #----------------------------------------------
 # Connection - Ajout d'une sonde
 #----------------------------------------------
 def vFConnectionAddProbeLine( self, sCOM, ttConfig ):

  # Container principal de la ligne
  tWidgetLine = QWidget()
  tWidgetLine.setContentsMargins(0,0,0,0)
  tWidgetLine.setMaximumSize(8000, 200)

  tEffect = QGraphicsDropShadowEffect(self)
  tEffect.setBlurRadius(20)
  tEffect.setXOffset(0)
  tEffect.setYOffset(0)
  #tEffect.setColor(Qt.black)
  tEffect.setColor(QColor(60, 60, 60, 60))
  tWidgetLine.setGraphicsEffect(tEffect)

  # Create a boxlayout (horizontal here)
  tBox = QHBoxLayout()
  tBox.setContentsMargins(10,10,10,10)
  tBox.setSpacing(15)
  # Set the layout for your tab
  tWidgetLine.setLayout(tBox)
  #--
  # Photo produit
  tProductPhoto = QLabel(self)
  tProductPhoto.setContentsMargins(0,0,0,0)
  tPixmap = QPixmap( self.sFDashboardGetProbeImageByID( ttConfig["PRODUCT"]["uiModel"] ) )
  tProductPhoto.setPixmap(tPixmap)
  tProductPhoto.setScaledContents(True)
  tProductPhoto.setMaximumSize(200, 200)
  tWidgetLine.layout().addWidget(tProductPhoto)
  #--
  # Info product
  tWidgetProductInfo = QWidget()
  tWidgetProductInfo.setMaximumSize(300, 200)
  tWidgetProductInfo.setContentsMargins(0,0,0,0)
  # Layout
  tVbox = QVBoxLayout();
  tVbox.setContentsMargins(0,0,0,0)
  tWidgetProductInfo.setLayout(tVbox);
  # Nom de la voie
  tLabel = QLabel()
  tLabel.setText( ttConfig["PRODUCT"]["sModel"] ) #"AP-6000 - COM4"
  tLabel.setMinimumSize(0, 50)
  tLabel.setStyleSheet("QLabel{font-size: 18pt;font-weight:600;color:#3e4072;}")
  tWidgetProductInfo.layout().addWidget(tLabel)
  # Numéro de série
  tLabel = QLabel()
  tLabel.setText( "SN: "+ttConfig["PRODUCT"]["sPSN1"] )
  tLabel.setStyleSheet("QLabel{color:#666;}")
  tWidgetProductInfo.layout().addWidget(tLabel)
  # Pourcentage mémoire
  """
  tLabelMemory = QLabel()
  tLabelMemory.setText( "Memory: "+str(ttConfig["PRODUCT"]["uiMemRemainingPC"])+"%" + " - " +"Battery: "+str(ttConfig["PRODUCT"]["uiBATT_PC"])+"%")
  tLabelMemory.setStyleSheet("QLabel{color:#666;}")
  tLabelMemory.setMinimumSize(0, 20)
  tWidgetProductInfo.layout().addWidget(tLabelMemory)
  """
  '''
  # Pourcentage batterie
  tLabelBattery = QLabel()
  tLabelBattery.setText( "Battery: "+str(ttConfig["PRODUCT"]["uiBATT_PC"])+"%" )
  tLabelBattery.setStyleSheet("QLabel{color:#666;}")
  tLabelBattery.setMinimumSize(0, 20)
  tWidgetProductInfo.layout().addWidget(tLabelBattery)
  '''
  # COM
  tLabelMemory = QLabel()
  tLabelMemory.setText( "Interface: "+sCOM )
  tLabelMemory.setStyleSheet("QLabel{color:#666;}")
  tLabelMemory.setMinimumSize(0, 20)
  tWidgetProductInfo.layout().addWidget(tLabelMemory)

  verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
  tWidgetProductInfo.layout().addItem(verticalSpacer)
  tProductConnectBtn = QPushButton()
  tProductConnectBtn.setText( "Connect" )
  tWidgetProductInfo.layout().addWidget(tProductConnectBtn)
  # Alignement des élements
  tWidgetProductInfo.layout().setAlignment(Qt.AlignTop)
  tWidgetLine.layout().addWidget(tWidgetProductInfo)
  #--
  # Carte
  '''
  tWidgetMap = QWidget()
  tWidgetMap.setMaximumSize(300, 200)
  tWidgetMap.setContentsMargins(0,0,0,0)
  tCoordinate = (46.7873953, -2.2952942)
  tFoliumMapProduct = folium.Map(
   title = "nke",
   location=tCoordinate
  )
  folium.Marker(location = tCoordinate).add_to(tFoliumMapProduct)
  # Save map  data to data object
  tIOData = io.BytesIO()
  tFoliumMapProduct.save(tIOData, close_file=False)
  # Webview
  tWebViewProduct = QWebEngineView()
  tWebViewProduct.setHtml(tIOData.getvalue().decode())
  # Layout
  tVbox = QVBoxLayout();
  tVbox.setContentsMargins(0,0,0,0)
  tWidgetMap.setLayout(tVbox);
  tWidgetMap.layout().addWidget(tWebViewProduct)
  # Ajout de la carte
  tWidgetLine.layout().addWidget(tWidgetMap)
  '''
  # Ajout de la nouvelle ligne au layout
  self.ui.widget_ConnectSondeList.layout().addWidget(tWidgetLine)
  # Ajout signal sur bouton connect
  self.xConnectionProbeSelectConnectSignal.emit( sCOM, tProductConnectBtn )

 #----------------------------------------------
 # Dashboard - Choix de la photo sonde
 #----------------------------------------------
 def sFDashboardGetSondeImageByID( self, uiProductID ):
  sPhoto = ":/Photo/XX-Unknow-product.jpg"
  if( uiProductID == 10 ): sPhoto = ":/Photo/20-AS-2000.jpg"  # AS-2000
  if( uiProductID == 20 ): sPhoto = ":/Photo/20-AS-2000.jpg"  # AS-2000-D
  if( uiProductID == 59 ): sPhoto = ":/Photo/59-AS-5000.jpg"  # AS-5000
  if( uiProductID == 29 ): sPhoto = ":/Photo/29-AS-6000.jpg"  # AS-6K/7K/Pro
  return( sPhoto )

 #----------------------------------------------
 # Dashboard - Choix de la photo probe
 #----------------------------------------------
 def sFDashboardGetProbeImageByID( self, uiProductID ):
  sPhoto = ":/Photo/XX-Unknow-product.jpg"
  if( uiProductID == 53 ): sPhoto = ":/Photo/53-AquaPlus.jpg" # AquaPlus
  if( uiProductID == 30 ): sPhoto = ":/Photo/30-AP-Lite.jpg"  # AP-Lite
  if( uiProductID == 40 ): sPhoto = ":/Photo/40-AP-700.jpg"   # AP-700
  if( uiProductID == 60 ): sPhoto = ":/Photo/40-AP-700.jpg"   # AP-700-D
  if( uiProductID == 50 ): sPhoto = ":/Photo/50-AP-800.jpg"   # AP-800
  if( uiProductID == 70 ): sPhoto = ":/Photo/50-AP-800.jpg"   # AP-800-D
  if( uiProductID == 10 ): sPhoto = ":/Photo/20-AP-2000.jpg"  # AP-2000
  if( uiProductID == 20 ): sPhoto = ":/Photo/20-AP-2000.jpg"  # AP-2000-D
  if( uiProductID == 59 ): sPhoto = ":/Photo/59-AP-5000.jpg"  # AP-5000
  if( uiProductID == 29 ): sPhoto = ":/Photo/29-AP-6000.jpg"  # AP-6K/7K/Pro
  return( sPhoto )

 #----------------------------------------------
 # PCConf - Open Graphical depth Windows
 #----------------------------------------------
 def vFPCConfDisplayConf( self, tINIConfig ):
  print("-- vFPCConfGraphicalDepthOpen --")
  if( tINIConfig["MEASURE"]["ec_ref_temp"] == "25" ):
   self.ui.label_Config_ECRefTemp.setText("25 C")
  elif( tINIConfig["MEASURE"]["ec_ref_temp"] == "20" ):
   self.ui.label_Config_ECRefTemp.setText("20 C")
  else:
   self.ui.label_Config_ECRefTemp.setText("ABS EC")
  self.ui.label_Config_TempUnit.setText(tINIConfig["MEASURE"]["temperature_unit"])
  self.ui.label_Config_DepthUnit.setText(tINIConfig["MEASURE"]["depth_unit"])
  self.ui.label_Config_TDSFactor.setText(tINIConfig["MEASURE"]["tds_factor"])
  self.ui.label_Config_GraphDepth.setText(tINIConfig["SOFTWARE"]["graphical_depth"]+" samples")
  if( tINIConfig["SOFTWARE"]["display_calculated"] == "1" ):
   self.ui.label_Config_DisplayCalculated.setText("Enable")
   self.ui.widget_CalculatedResult.setVisible(True)
  else:
   self.ui.label_Config_DisplayCalculated.setText("Disable")
   self.ui.widget_CalculatedResult.setVisible(False)

 #----------------------------------------------
 # PCConf - Open Graphical depth Windows
 #----------------------------------------------
 def vFPCConfGraphicalDepthOpen( self, event ):
  print("-- vFPCConfGraphicalDepthOpen --")
  sLabel = self.ui.label_Config_GraphDepth.text()
  sLabel = str(sLabel.split(" ")[0])
  if( sLabel == "0" ): sLabel = "Unlimited"
  self.tUIGraphicalDepth.vFOpen(sLabel)


 #----------------------------------------------
 # PC Conf - EC Ref Temperature
 #----------------------------------------------
 def vFPCONFChangeECRefTemperature( self, sValue ):
  print("-- vFPCONFChangeECRefTemperature --")
  # Mise à jour du label dans App Config
  self.ui.label_Config_ECRefTemp.setText(sValue)

 #----------------------------------------------
 # PC Conf - Temperature Unit
 #----------------------------------------------
 def vFPCONFChangeTemperatureUnit( self, sValue ):
  print("-- vFPCONFChangeTemperatureUnit --")
  # Mise à jour du label PCConf
  self.ui.label_Config_TempUnit.setText(sValue)
  try:
   # Liveview - Temp
   if( sValue == "F" ):
    self.tMeasureBox[0]["tLabelUnit"].setText("(degF)")
   else:
    self.tMeasureBox[0]["tLabelUnit"].setText("(degC)")
  except Exception as err:
   print(err)

 #----------------------------------------------
 # PC Conf - Depth unit
 #----------------------------------------------
 def vFPCONFChangeDepthUnit( self, sValue ):
  print("-- vFPCONFChangeDepthUnit --")
  # Mise à jour du label
  self.ui.label_Config_DepthUnit.setText(sValue)
  try:
   # Liveview - Temp
   if( sValue == "f" ):
    self.tMeasureBox[1]["tLabelUnit"].setText("(f)")
   else:
    self.tMeasureBox[1]["tLabelUnit"].setText("(m)")
  except Exception as err:
   print(err)

 #----------------------------------------------
 # PC Conf - TDS Factor
 #----------------------------------------------
 def vFPCONFChangeTDSFactor( self, fText ):
  print("-- vFPCONFChangeTDSFactor --")
  # Mise à jour du label
  self.ui.label_Config_TDSFactor.setText(("%.2f"%fText))



 #----------------------------------------------
 # Connexion - Affichage produit présent/détecté
 #----------------------------------------------
 def vFDisplayLeveLineDetected( self, tsProductList ):
  print("-- VMainWindow > vFDisplaySondeDetected --")
  print(range(self.ui.widget_ConnectSondeList.layout().count()))
  # Effacement des vieux produits - Clear du layout
  if( self.ui.widget_ConnectSondeList.layout().count() != 0 ):
   for i in reversed(range(self.ui.widget_ConnectSondeList.layout().count())):
    self.ui.widget_ConnectSondeList.layout().itemAt(i).widget().deleteLater()

  # Si produit détecté
  if( len(tsProductList) ):
   # Parcourt des sondes détectées
   for tElt in tsProductList:
    # Ajout au layout
    self.vFConnectionAddLeveLineLine(tElt, tsProductList[tElt])
   print("Fin d'ajout des lignes")
   # Alignement produit détecté
   self.ui.widget_ConnectSondeList.layout().setAlignment(Qt.AlignTop)
  # Pas de produit détecté
  else:
   # Ouverture fenêtre information
   self.tUIInfo.vFOpen( "Product detection", "No product detected" )

 #----------------------------------------------
 # Connection - Ajout d'une sonde
 #----------------------------------------------
 def vFConnectionAddLeveLineLine( self, sCOM, ttConfig ):

  # Container principal de la ligne
  tWidgetLine = QWidget()
  tWidgetLine.setContentsMargins(0,0,0,0)
  tWidgetLine.setMaximumSize(8000, 200)

  tEffect = QGraphicsDropShadowEffect(self)
  tEffect.setBlurRadius(20)
  tEffect.setXOffset(0)
  tEffect.setYOffset(0)
  tEffect.setColor(QColor(60, 60, 60, 60))
  tWidgetLine.setGraphicsEffect(tEffect)

  # Create a boxlayout (horizontal here)
  tBox = QHBoxLayout()
  tBox.setContentsMargins(10,10,10,10)
  tBox.setSpacing(15)
  # Set the layout for your tab
  tWidgetLine.setLayout(tBox)
  #--
  # Photo produit
  """"""
  tProductPhoto = QLabel(self)
  tProductPhoto.setContentsMargins(0,0,0,0)
  tPixmap = QPixmap( ttConfig["PRODUCT"]["bFGetProductPhoto"]( ttConfig ) )
  tProductPhoto.setPixmap(tPixmap)
  tProductPhoto.setScaledContents(True)
  tProductPhoto.setMaximumSize(200, 200)
  tWidgetLine.layout().addWidget(tProductPhoto)
  """"""
  #--
  # Info product
  tWidgetProductInfo = QWidget()
  tWidgetProductInfo.setMaximumSize(300, 200)
  tWidgetProductInfo.setContentsMargins(0,0,0,0)
  # Layout
  tVbox = QVBoxLayout();
  tVbox.setContentsMargins(0,0,0,0)
  tWidgetProductInfo.setLayout(tVbox);
  # Nom de la voie
  """"""
  tLabel = QLabel()
  print(ttConfig)
  bFGetProductName = ttConfig["PRODUCT"]["bFGetProductName"]
  tLabel.setText( bFGetProductName(ttConfig) ) #"LeveLine - 10m"
  #tLabel.setMinimumSize(0, 50)
  tLabel.setStyleSheet("QLabel{font-size: 18pt;font-weight:600;color:#3e4072;}")
  tWidgetProductInfo.layout().addWidget(tLabel)
  # Nom de la voie
  """"""
  tLabel = QLabel()
  print(ttConfig)
  bFGetProductName = ttConfig["PRODUCT"]["bFGetProductName"]
  tLabel.setText( ttConfig["PRODUCT"]["sSensorTypeFormat"] ) #"LeveLine - 10m"
  #tLabel.setMinimumSize(0, 50)
  tLabel.setStyleSheet("QLabel{font-size: 13pt;font-weight:600;color:#3e4072;}")
  tWidgetProductInfo.layout().addWidget(tLabel)
  """"""
  # Depth rating
  tLabel = QLabel()
  tLabel.setText( "Depth rating: "+ttConfig["PRODUCT"]["sDepthRating"] )
  tLabel.setStyleSheet("QLabel{color:#666;}")
  tWidgetProductInfo.layout().addWidget(tLabel)
  # Numéro de série
  tLabel = QLabel()
  tLabel.setText( "SN: "+ttConfig["PRODUCT"]["sSerialNumber"] )
  tLabel.setStyleSheet("QLabel{color:#666;}")
  tWidgetProductInfo.layout().addWidget(tLabel)
  # COM
  tLabelMemory = QLabel()
  tLabelMemory.setText( "Interface: "+sCOM )
  tLabelMemory.setStyleSheet("QLabel{color:#666;}")
  tLabelMemory.setMinimumSize(0, 20)
  tWidgetProductInfo.layout().addWidget(tLabelMemory)

  verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
  tWidgetProductInfo.layout().addItem(verticalSpacer)
  tProductConnectBtn = QPushButton()
  tProductConnectBtn.setText( "Connect" )
  tWidgetProductInfo.layout().addWidget(tProductConnectBtn)
  # Alignement des élements
  tWidgetProductInfo.layout().setAlignment(Qt.AlignTop)
  tWidgetLine.layout().addWidget(tWidgetProductInfo)
  #--
  # Carte
  '''
  tWidgetMap = QWidget()
  tWidgetMap.setMaximumSize(300, 200)
  tWidgetMap.setContentsMargins(0,0,0,0)
  tCoordinate = (46.7873953, -2.2952942)
  tFoliumMapProduct = folium.Map(
   title = "nke",
   location=tCoordinate
  )
  folium.Marker(location = tCoordinate).add_to(tFoliumMapProduct)
  # Save map  data to data object
  tIOData = io.BytesIO()
  tFoliumMapProduct.save(tIOData, close_file=False)
  # Webview
  tWebViewProduct = QWebEngineView()
  tWebViewProduct.setHtml(tIOData.getvalue().decode())
  # Layout
  tVbox = QVBoxLayout();
  tVbox.setContentsMargins(0,0,0,0)
  tWidgetMap.setLayout(tVbox);
  tWidgetMap.layout().addWidget(tWebViewProduct)
  # Ajout de la carte
  tWidgetLine.layout().addWidget(tWidgetMap)
  '''
  # Ajout de la nouvelle ligne au layout
  self.ui.widget_ConnectSondeList.layout().addWidget(tWidgetLine)
  # Ajout signal sur bouton connect
  self.xConnectionLeveLineSelectConnectSignal.emit( sCOM, tProductConnectBtn )

 #----------------------------------------------
 # Dashboard - Choix de la photo LeveLine
 #----------------------------------------------
 def sFDashboardGetLeveLineImageByProductType( self, uiProductID ):
  sPhoto = ":/Photo/XX-Unknow-product.jpg"
  if( uiProductID == 53 ): sPhoto = ":/Photo/53-AquaPlus.jpg" # AquaPlus
  if( uiProductID == 30 ): sPhoto = ":/Photo/30-AP-Lite.jpg"  # AP-Lite
  if( uiProductID == 40 ): sPhoto = ":/Photo/40-AP-700.jpg"   # AP-700
  if( uiProductID == 60 ): sPhoto = ":/Photo/40-AP-700.jpg"   # AP-700-D
  if( uiProductID == 50 ): sPhoto = ":/Photo/50-AP-800.jpg"   # AP-800
  if( uiProductID == 70 ): sPhoto = ":/Photo/50-AP-800.jpg"   # AP-800-D
  if( uiProductID == 10 ): sPhoto = ":/Photo/20-AS-2000.jpg"  # AS-2000
  if( uiProductID == 20 ): sPhoto = ":/Photo/20-AS-2000.jpg"  # AS-2000-D
  if( uiProductID == 59 ): sPhoto = ":/Photo/59-AS-5000.jpg"  # AS-5000
  if( uiProductID == 29 ): sPhoto = ":/Photo/29-AS-6000.jpg"  # AS-6K/7K/Pro
  return( sPhoto )
