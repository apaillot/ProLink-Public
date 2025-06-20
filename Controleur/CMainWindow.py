# This Python file uses the following encoding: utf-8

#============================================================================#
# Librairies système
#============================================================================#
import sys
import configparser
from datetime import datetime

#============================================================================#
# Librairies Qt
#============================================================================#
from PySide6.QtCore import (QDate, QDateTime, QLocale, QMetaObject)
from PySide6.QtCore import Slot, QTimer

#============================================================================#
# Librairies Utilisateur
#============================================================================#
from Update.HTTPUpdate         import HTTPUpdate
from Vue.VLib                  import *
from Vue.VMainWindowLib        import TECalibSensorNavIndex, TECalibPointNavIndex
from File.TFileRecord          import TFileRecord
from File.TLiveViewRecord      import TLiveViewRecord
from Controleur.CSonde         import CSonde
from Controleur.CProbe         import CProbe
from Controleur.CSondeRawFile  import CSondeRawFile
from Controleur.CLeveLine      import CLeveLine

#============================================================================#
# Variable
#============================================================================#

#============================================================================#
# Classe
#============================================================================#

#------------------------------------------------------------------------
# Controleur de main Windows
#------------------------------------------------------------------------
class CMainWindow:
 #----------------------------------------------
 # Init
 #----------------------------------------------
 def __init__( self, view, model, sSoftwareVersion, tINIConfig ):
  # Conservation des entrées
  self._model = model
  self._view  = view
  self.tINIConfig  = tINIConfig
  self.tHTTPUpdate = HTTPUpdate(self.tINIConfig)
  # Création des signaux
  self.connectionSignaux()
  # Conservation du numéro de version
  self.sSoftwareVersion = sSoftwareVersion
  print(os.getcwd())
  # Si la mise à jour est activée
  if( tINIConfig.tConfig['UPDATE']['activate'] == "1" ):
   print("Mise à jour activée - Lancement timer")
   #%%AP - On décale la détection par rapport au splashscreen
   # Recherche de mise à jour
   #self.tHTTPUpdate.startUpdateCheck(self.sSoftwareVersion)
   QTimer.singleShot(2000, lambda:self.tHTTPUpdate.startUpdateCheck(self.sSoftwareVersion))
  else:
   print("Mise à jour non activée")

  #-- Controleur produit --
  # Sonde
  self.tCSonde    = CSonde(view, model, tINIConfig)
  # Probe
  self.tCProbe    = CProbe(view, model, tINIConfig)
  # LeveLine
  self.tCLeveLine = CLeveLine(view, model, tINIConfig)
  # Temporaire pour maintenir en fonctionnement
  self.tCSonde.connectSignals()
  self.tCProbe.connectSignals()
  self.tCLeveLine.connectSignals()
  # Sonde - Lecture fichier RAW
  self.CSondeRawFile = CSondeRawFile(view, model, tINIConfig)
  # Temporaire pour maintenir en fonctionnement
  self.CSondeRawFile.connectSignals()

  #-------------------------------------------
  # PC Configuration
  #-------------------------------------------
  self._view.vFPCConfDisplayConf( tINIConfig.tConfig )


 #----------------------------------------------
 # Click bouton product COM
 #----------------------------------------------
 @Slot()
 def slotDashboardTestButtonClicked( self ):
  print("-- slotDashboardTestButtonClicked --")
  # Création fichier CSV
  self.tCSVMeasure.vFCreateNewFile(self._model.tProduct.ttConfig)

 #----------------------------------------------
 # Création des signaux de la fenêtre principale
 #----------------------------------------------
 def connectionSignaux( self ):
  print("-- connectionSignaux --")
  #----------------
  # Sur ouverture fenêtre
  #----------------
  self._view.tUILoadingScreen.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tUIBatteryRemaining.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tUIEstimatedMemory.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  self._view.tUIEstimatedBattery.siOpen.connect(lambda:self._view.tUIBackground.vFOpen( self._view.size() ))
  #----------------
  # Sur fermeture fenêtre
  #----------------
  self._view.tUILoadingScreen.siClose.connect( self._view.tUIBackground.close )
  self._view.tUIBatteryRemaining.siClose.connect(self._view.tUIBackground.close)
  self._view.tUIEstimatedMemory.siClose.connect(self._view.tUIBackground.close)
  self._view.tUIEstimatedBattery.siClose.connect(self._view.tUIBackground.close)

  #---------------
  # Update
  #---------------
  self.tHTTPUpdate.siUpdateDetected.connect(self._view.UIUpdateDetected.vFOpen)
  self.tHTTPUpdate.siUpdateDetected.connect(lambda event:self._view.tUIBackground.vFOpen( self._view.size() ) )
  self._view.UIUpdateDetected.siAcceptUpdate.connect(self.tHTTPUpdate.startUpdate)
  self._view.UIUpdateDetected.siAcceptUpdate.connect(self._view.UIUpdateProgress.vFOpen)
  self._view.UIUpdateDetected.siClose.connect(self._view.tUIBackground.close)
  self._view.UIUpdateDetected.siAcceptUpdate.connect(lambda event:self._view.tUIBackground.vFOpen( self._view.size() ) )
  self.tHTTPUpdate.siUpdateEndSuccess.connect(self._view.UIUpdateProgress.vFClose)
  self._view.UIUpdateProgress.siClose.connect(self._view.tUIBackground.close)
  self.tHTTPUpdate.siTotalProgress.connect(self._view.UIUpdateProgress.vFTotalProgress)
  self.tHTTPUpdate.siCurrentProgress.connect(self._view.UIUpdateProgress.vFProgress)
  self.tHTTPUpdate.siUpdateError.connect( lambda sMsg:vFAlert( self._view, "Update",  sMsg) )
  self.tHTTPUpdate.siUpdateError.connect( self._view.UIUpdateProgress.vFClose )

  #---------------
  # Général
  #---------------
  # Message d'erreur
  self._model.siErrorMsg.connect(lambda sTitle, sMsg:vFAlert( self._view, sTitle, sMsg))
  # Mise à jour check (sur click numéro de version)
  self._view.ui.version_label.mouseReleaseEvent = lambda event:self.tHTTPUpdate.startUpdateCheck(self.sSoftwareVersion)
  #---------------
  # Detect/Connect
  #---------------
  # Détection sonde
  self._view.ui.pushButton_detectProduct.clicked.connect(lambda:self._view.vFDeleteDetectBtn( self._view.ui.pushButton_detectProduct ))
  self._view.ui.pushButton_detectProbe.clicked.connect(lambda:self._view.vFDeleteDetectBtn( self._view.ui.pushButton_detectProbe ))
  self._view.ui.pushButton_detectLeveLine.clicked.connect(lambda:self._view.vFDeleteDetectBtn( self._view.ui.pushButton_detectLeveLine ))
  self._view.ui.pushButton_openRawFile.clicked.connect(lambda:self._view.vFDeleteDetectBtn( self._view.ui.pushButton_openRawFile ))
  ## RAW File open
  #self._view.ui.pushButton_openRawFile.connect()

  #----------------
  # Dashboard
  #----------------
  # Bouton de test (temporaire)
  self._view.ui.pushButton_TestDashboard.clicked.connect( self.slotDashboardTestButtonClicked )
  # Dashboard - Timeout
  self._model.tMSonde.tProduct.siRequestTimeout.connect(self._view.tUILoadingScreen.vFClose)
  self._model.tMSonde.tProduct.siRequestTimeout.connect(lambda:self._view.tUIInfo.vFOpen("Detection", "Request timeout"))
  self._view.ui.widget_BatteryRemaining.mouseReleaseEvent  = lambda event:self._view.tUIBatteryRemaining.vFOpen()
  self._view.ui.widget_UntilMemFull.mouseReleaseEvent      = lambda event:self._view.tUIEstimatedMemory.vFOpen()
  self._view.ui.widget_UntilBattFull.mouseReleaseEvent     = lambda event:self._view.tUIEstimatedBattery.vFOpen()

  #----------------
  # Data
  #----------------
  # Navigation entre mode tableau ou graphique
  self._view.ui.pushButton_DataTabView.clicked.connect(lambda:self._view.tVSonde.vFDATAChangeDataViewMode(0))
  self._view.ui.pushButton_DataGraphView.clicked.connect(lambda:self._view.tVSonde.vFDATAChangeDataViewMode(1))

  #----------------
  # PC Conf
  #----------------
  # - Ouverture fenêtre - Modification paramètre
  self._view.ui.widget_ECRefTemp.mouseReleaseEvent      = lambda event:self._view.tUIECRefTemp.vFOpen(self._view.ui.label_Config_ECRefTemp.text())
  self._view.ui.widget_TempUnit.mouseReleaseEvent       = lambda event:self._view.tUITempUnit.vFOpen(self._view.ui.label_Config_TempUnit.text())
  self._view.ui.widget_DepthUnit.mouseReleaseEvent      = lambda event:self._view.tUIDepthUnit.vFOpen(self._view.ui.label_Config_DepthUnit.text())
  self._view.ui.widget_TDSFactor.mouseReleaseEvent      = lambda event:self._view.tUITDSFactor.vFOpen(float(self._view.ui.label_Config_TDSFactor.text()))
  self._view.ui.widget_GraphicalDepth.mouseReleaseEvent = self._view.vFPCConfGraphicalDepthOpen
  self._view.ui.widget_Config_DisplayCalculated.mouseReleaseEvent = lambda event:self._view.tUIDisplayCalculated.vFOpen(self._view.ui.label_Config_DisplayCalculated.text())
  # Sur ouverture fenêtre
  self._view.tUIECRefTemp.siOpen.connect( lambda:self._view.tUIBackground.vFOpen( self._view.size() ) )
  self._view.tUITempUnit.siOpen.connect( lambda:self._view.tUIBackground.vFOpen( self._view.size() ) )
  self._view.tUIDepthUnit.siOpen.connect( lambda:self._view.tUIBackground.vFOpen( self._view.size() ) )
  self._view.tUITDSFactor.siOpen.connect( lambda:self._view.tUIBackground.vFOpen( self._view.size() ) )
  self._view.tUIGraphicalDepth.siOpen.connect( lambda:self._view.tUIBackground.vFOpen( self._view.size() ) )
  self._view.tUIDisplayCalculated.siOpen.connect( lambda:self._view.tUIBackground.vFOpen( self._view.size() ) )
  # Sur fermeture fenêtre
  self._view.tUIECRefTemp.siClose.connect( self._view.tUIBackground.close )
  self._view.tUITempUnit.siClose.connect( self._view.tUIBackground.close )
  self._view.tUIDepthUnit.siClose.connect( self._view.tUIBackground.close )
  self._view.tUITDSFactor.siClose.connect( self._view.tUIBackground.close )
  self._view.tUIGraphicalDepth.siClose.connect( self._view.tUIBackground.close )
  self._view.tUIDisplayCalculated.siClose.connect( self._view.tUIBackground.close )
  # Sur validation
  self._view.tUIECRefTemp.siWriteData.connect( self.tINIConfig.vFWriteECRefTemp )
  self._view.tUITempUnit.siWriteData.connect( self.tINIConfig.vFWriteTemperatureUnit )
  self._view.tUIDepthUnit.siWriteData.connect( self.tINIConfig.vFWriteDepthUnit )
  self._view.tUITDSFactor.siWriteData.connect( self.tINIConfig.vFWriteTDSFactor )
  self._view.tUIGraphicalDepth.siWriteData.connect( self.tINIConfig.vFWriteGraphicalDepth )
  self._view.tUIDisplayCalculated.siWriteData.connect( self.tINIConfig.vFWriteDisplayCalculated )

  #----------------
  # Instruction de fin
  QMetaObject.connectSlotsByName(self._view)

 #----------------------------------------------
 # Clique sur
 #----------------------------------------------
 def connectionSignaux2( self ):
  print("-- connectionSignaux2 --")

