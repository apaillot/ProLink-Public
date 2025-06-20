# This Python file uses the following encoding: utf-8

#============================================================================#
# Librairies système
#============================================================================#
import sys
import io, csv
import serial
import serial.tools.list_ports as port_list
import time
import struct
import random
import logging
from datetime import datetime
import copy

#============================================================================#
# Librairies Qt
#============================================================================#
from PySide6.QtCore import QObject, QThread, Signal, Slot, QTimer, QDateTime

#============================================================================#
# Librairies Utilisateur
#============================================================================#
from Product.LeveLine.TProduct import TProduct
#from Model.MSonde           import MSonde

#============================================================================#
# Variable
#============================================================================#

#============================================================================#
# Classe
#============================================================================#

#------------------------------------------------------------------------
# Main Windows
#------------------------------------------------------------------------
class MLeveLine(QObject):
 #----------------------------------------------
 # Signaux
 #----------------------------------------------
 #-- Liveview
 siMeasureDataReadEnd           = Signal(dict)
 siMeasureDataReadStop          = Signal()
 siCalibrationCMDPointError     = Signal(str)

 #----------------------------------------------
 # Init
 #----------------------------------------------
 def __init__(self, parent=None):
  # Init QObject
  super(MLeveLine, self).__init__(parent=parent)
  # Initialisation avec objet generique
  self.tProduct = TProduct()

  # Déclaration des signaux fixes
  self.tProduct.siMeasureDataReadEnd.connect(self.tsFMeasureDataReadEnd)

  # Timer measure
  self.tTimerMeasure = QTimer()
  self.tTimerMeasure.timeout.connect(self.tsFMeasureDataRead)
  self.uiMeasureInterval = 2000

 #----------------------------------------------
 # Requête mesure data
 #----------------------------------------------
 def vFMeasureDataReadStart(self):
  print("== vFMeasureDataReadStart ==")
  # Démarrage d'un timer de mesure
  self.tTimerMeasure.setInterval(self.uiMeasureInterval)
  self.tTimerMeasure.start()
  # Première requête
  #self.tProduct.bFProductGetDirectAccessMode()
 #----------------------------------------------
 # Appelé périodiquement
 def tsFMeasureDataRead(self):
  print("== tsFMeasureDataRead == "+QDateTime.currentDateTime().toString("yyyy-MM-ddTHH:mm:ss.zzz"))
  if( not self.tProduct.bFProductGetLiveData() ):
   # Stop du timer
   self.tTimerMeasure.stop()

 #----------------------------------------------
 def tsFMeasureDataReadEnd(self):
  print("== tsFMeasureDataReadEnd ==")
  # Fin une détection automatique
  self.siMeasureDataReadEnd.emit( self.tProduct.ttConfig )
 #----------------------------------------------
 # Requête mesure data
 #----------------------------------------------
 def vFMeasureDataReadStop(self):
  print("---------------------------")
  print("-- vFMeasureDataReadStop --")
  print("---------------------------")
  # Stop du timer
  self.tTimerMeasure.stop()
  # Signal fin de mesure
  self.siMeasureDataReadStop.emit()

 #==================================================================
 # Ecriture paramètrage
 #==================================================================
  #----------------------------------------------
 # DASHBOARD - Ecriture RTC sonde date
 #----------------------------------------------
 @Slot(int, int, int)
 def slotWriteSondeDate(self, uiDay, uiMonth, uiYear):
  print("== slotWriteSondeDate ==")
  print("Date = %0u/%0u/%u" % (uiYear, uiMonth, uiDay) )
  ##TODO - Test d'intégrité
  self.tProduct.ttConfig["PRODUCT"]["uiDay"]   = uiDay
  self.tProduct.ttConfig["PRODUCT"]["uiMonth"] = uiMonth
  self.tProduct.ttConfig["PRODUCT"]["uiYear"]  = uiYear-2000
  print('self.tProduct.ttConfig["PRODUCT"]["uiYear"]  = %d'%self.tProduct.ttConfig["PRODUCT"]["uiYear"])
  print('self.tProduct.ttConfig["PRODUCT"]["uiMonth"] = %d'%self.tProduct.ttConfig["PRODUCT"]["uiMonth"])
  print('self.tProduct.ttConfig["PRODUCT"]["uiDay"]   = %d'%self.tProduct.ttConfig["PRODUCT"]["uiDay"])
  print('self.tProduct.ttConfig["PRODUCT"]["uiHour"]  = %d'%self.tProduct.ttConfig["PRODUCT"]["uiHour"])
  print('self.tProduct.ttConfig["PRODUCT"]["uiMin"]   = %d'%self.tProduct.ttConfig["PRODUCT"]["uiMin"])
  print('self.tProduct.ttConfig["PRODUCT"]["uiSec"]   = %d'%self.tProduct.ttConfig["PRODUCT"]["uiSec"])
  # Sonde datetime écriture
  self.tProduct.bFProductDateTimeWrite()

 #----------------------------------------------
 # DASHBOARD - Ecriture RTC sonde time
 #----------------------------------------------
 @Slot(int, int, int)
 def slotWriteSondeTime(self, uiHour, uiMin, uiSec):
  print("== slotWriteSondeTime ==")
  print("Time = %0u:%0u:%0u" % (uiHour, uiMin, uiSec) )
  ##TODO - Test d'intégrité
  # Ecriture dans la configuration
  self.tProduct.ttConfig["PRODUCT"]["uiHour"] = uiHour
  self.tProduct.ttConfig["PRODUCT"]["uiMin"]  = uiMin
  self.tProduct.ttConfig["PRODUCT"]["uiSec"]  = uiSec
  print('self.tProduct.ttConfig["PRODUCT"]["uiYear"]  = %d'%self.tProduct.ttConfig["PRODUCT"]["uiYear"])
  print('self.tProduct.ttConfig["PRODUCT"]["uiMonth"] = %d'%self.tProduct.ttConfig["PRODUCT"]["uiMonth"])
  print('self.tProduct.ttConfig["PRODUCT"]["uiDay"]   = %d'%self.tProduct.ttConfig["PRODUCT"]["uiDay"])
  print('self.tProduct.ttConfig["PRODUCT"]["uiHour"]  = %d'%self.tProduct.ttConfig["PRODUCT"]["uiHour"])
  print('self.tProduct.ttConfig["PRODUCT"]["uiMin"]   = %d'%self.tProduct.ttConfig["PRODUCT"]["uiMin"])
  print('self.tProduct.ttConfig["PRODUCT"]["uiSec"]   = %d'%self.tProduct.ttConfig["PRODUCT"]["uiSec"])
  # Sonde datetime écriture
  self.tProduct.bFProductDateTimeWrite()

 #----------------------------------------------
 # DASHBOARD - Ecriture RTC sonde date time PC
 #----------------------------------------------
 @Slot(int, int, int)
 def slotWriteSondeDateTimePC(self):
  print("== slotWriteSondeDateTimePC ==")
  tDateTime = datetime.now()

  print("tDateTime = %0u/%0u/%0u %0u:%0u:%0u" % (tDateTime.year, tDateTime.month, tDateTime.day,
                                                 tDateTime.hour, tDateTime.minute, tDateTime.second) )
  ##TODO - Test d'intégrité
  # Ecriture dans la configuration
  self.tProduct.ttConfig["PRODUCT"]["uiYear"]  = tDateTime.year-2000
  self.tProduct.ttConfig["PRODUCT"]["uiMonth"] = tDateTime.month
  self.tProduct.ttConfig["PRODUCT"]["uiDay"]   = tDateTime.day
  self.tProduct.ttConfig["PRODUCT"]["uiHour"]  = tDateTime.hour
  self.tProduct.ttConfig["PRODUCT"]["uiMin"]   = tDateTime.minute
  self.tProduct.ttConfig["PRODUCT"]["uiSec"]   = tDateTime.second
  print('self.tProduct.ttConfig["PRODUCT"]["uiYear"]  = %d'%self.tProduct.ttConfig["PRODUCT"]["uiYear"])
  print('self.tProduct.ttConfig["PRODUCT"]["uiMonth"] = %d'%self.tProduct.ttConfig["PRODUCT"]["uiMonth"])
  print('self.tProduct.ttConfig["PRODUCT"]["uiDay"]   = %d'%self.tProduct.ttConfig["PRODUCT"]["uiDay"])
  print('self.tProduct.ttConfig["PRODUCT"]["uiHour"]  = %d'%self.tProduct.ttConfig["PRODUCT"]["uiHour"])
  print('self.tProduct.ttConfig["PRODUCT"]["uiMin"]   = %d'%self.tProduct.ttConfig["PRODUCT"]["uiMin"])
  print('self.tProduct.ttConfig["PRODUCT"]["uiSec"]   = %d'%self.tProduct.ttConfig["PRODUCT"]["uiSec"])
  # Sonde datetime écriture
  self.tProduct.bFProductDateTimeWrite()

 #----------------------------------------------
 # DASHBOARD - Ecriture Site ID
 #----------------------------------------------
 @Slot(str)
 def slotWriteSiteID(self, sTxt):
  print("== slotWriteSiteID ==")
  print("sTxt = %s" % sTxt )
  # Ecriture dans la configuration
  self.tProduct.ttConfig["PRODUCT"]["sSiteID"] = sTxt
  # Lancement écriture vers sonde
  self.tProduct.bFProductSiteIDWrite()

 #----------------------------------------------
 # DASHBOARD - Ecriture Site Latitude
 #----------------------------------------------
 @Slot(str, int, float)
 def slotWriteSiteLatitude(self, sRef, uiDeg, fMin):
  print("== slotWriteSiteLatitude ==")
  print("sRef, uiDeg, fMin = %s %u %.5f" % (sRef, uiDeg, fMin) )
  # Degré
  sDeg = "%02d"%uiDeg
  # Minutes
  uiMin  = int(fMin)
  sMin = "%02d"%uiMin
  print("sMin = "+sMin)
  # Seconds
  uiSec = int(fMin*10000) - int(uiMin*10000)
  sSec = "%04d"%uiSec
  print("sSec = "+sSec)
  # Concatenation
  sSiteLat = sRef+sDeg+sMin+sSec
  # Ecriture dans la configuration
  self.tProduct.ttConfig["PRODUCT"]["sLatitudeRaw"] = sSiteLat
  print(sSiteLat)
  # Lancement écriture vers sonde
  self.tProduct.bFProductPositionWrite()

 #----------------------------------------------
 # DASHBOARD - Ecriture Site longitude
 #----------------------------------------------
 @Slot(str, int, float)
 def slotWriteSiteLongitude(self, sRef, uiDeg, fMin):
  print("== slotWriteSiteLongitude ==")
  print("sRef, uiDeg, fMin = %s %u %.5f" % (sRef, uiDeg, fMin) )
  #####################
  ##TODO test intégrité
  #####################
  # Degré
  sDeg = "%03d"%uiDeg
  # Minutes
  uiMin  = int(fMin)
  sMin = "%02d"%uiMin
  print("sMin = "+sMin)
  # Seconds
  uiSec = int(fMin*10000) - int(uiMin*10000)
  sSec = "%04d"%uiSec
  print("sSec = "+sSec)
  # Concatène
  sSiteLong = sRef+sDeg+sMin+sSec
  # Ecriture dans la configuration
  self.tProduct.ttConfig["PRODUCT"]["sLongitudeRaw"]   = sSiteLong
  print(sSiteLong)
  # Lancement écriture vers sonde
  self.tProduct.bFProductPositionWrite()

 #----------------------------------------------
 # DASHBOARD - Ecriture Site altitude
 #----------------------------------------------
 def slotWriteSiteAltitude(self, iAltitude):
  print("== slotWriteSiteAltitude ==")
  print("fAltitude = %05d" % iAltitude )
  #####################
  ##TODO test intégrité
  #####################
  # Si positif ou négatif
  if( iAltitude >= 0 ):
   sAltitude = "+"
   sAltitude += "%05d"%iAltitude
  else:
   sAltitude = "" #"-"
   sAltitude += "%06d"%iAltitude

  # Ecriture dans la configuration
  self.tProduct.ttConfig["PRODUCT"]["sAltitudeRaw"]   = sAltitude
  print(sAltitude)
  # Lancement écriture vers sonde
  self.tProduct.bFProductPositionWrite()



 #----------------------------------------------
 # DASHBOARD - Ecriture Log data every
 #----------------------------------------------
 @Slot(int, int, int)
 def slotWriteLogDataEvery(self, uiHour, uiMin, fSec):
  print("== slotWriteLogDataEvery ==")
  print("Hour %d, Min %d, Sec %.1f" % (uiHour, uiMin, fSec) )

  """
  # Si inférieur à la minute
  if(   ( uiHour == 0 )
    and ( uiMin  == 0 )
    and ( fSec   != 0 ) ):
   # Vérification que event logging désactivé
   if( self.tProduct.ttConfig["PRODUCT"]["uiLOG_EVENT"] == 1 ):
    # Erreur
    print("Error")
    self.siErrorMsg.emit("Log event state error", "Log data can not be under 1 minute with log event activated")
    return
  """

  # Calcul de la cadence total en secondes
  uiLogSec = int( ( uiHour * 3600 + uiMin * 60 + fSec ) * 10 )

  # Ecriture configuration
  self.tProduct.ttConfig["PRODUCT"]["uiLogIntervalHour"] = uiHour
  self.tProduct.ttConfig["PRODUCT"]["uiLogIntervalMin"]  = uiMin
  self.tProduct.ttConfig["PRODUCT"]["fLogIntervalSec"]   = fSec
  self.tProduct.ttConfig["PRODUCT"]["uiLogInterval"]     = uiLogSec

  # Lancement écriture vers sonde
  self.tProduct.bFProductLogIntervalWrite()

 #----------------------------------------------
 # DASHBOARD - Ecriture Log data for
 #----------------------------------------------
 def slotWriteLogDataFor(self, uiHour):
  print("== slotWriteLogDataFor ==")
  print("Hour %d" % (uiHour) )

  # Calcul de la cadence total en secondes
  self.tProduct.ttConfig["PRODUCT"]["uiLogDuration"] = uiHour
  # Lancement écriture vers sonde
  self.tProduct.bFProductLogDataForWrite()

 #----------------------------------------------
 # DASHBOARD - Ecriture Log event state
 #----------------------------------------------
 @Slot(int)
 def slotWriteEventLogCheckState(self, sState):
  print("== slotWriteEventLogCheckState ==")
  print("sState %s" % sState )
  # Si demande d'activation
  if( sState == "Enable" ):
   self.tProduct.ttConfig["PRODUCT"]["bEventLog"] = True
   uiEventInterval = 600
  else:
   self.tProduct.ttConfig["PRODUCT"]["bEventLog"] = False
   uiEventInterval = 0
  # Remplit les champs
  self.tProduct.ttConfig["PRODUCT"]["uiEventInterval"] = uiEventInterval
  self.tProduct.ttConfig["PRODUCT"]["uiEventHour"]     = int( uiEventInterval / 36000 )
  self.tProduct.ttConfig["PRODUCT"]["uiEventMin"]      = int( ( uiEventInterval % 36000 ) / 600 )
  self.tProduct.ttConfig["PRODUCT"]["fEventSec"]       = float( ( uiEventInterval % 600 ) / 10 )

  # Lancement écriture vers sonde
  self.tProduct.bFProductEventLogCheckPeriodWrite()

 #----------------------------------------------
 # DASHBOARD - Ecriture Log event every
 #----------------------------------------------
 @Slot(int)
 def slotWriteEventLogCheckPeriod(self, uiHours, uiMinutes, fSec):
  print("== slotWriteEventLogCheckPeriod ==")
  print("Hour %d" % uiHours )
  print("uiMinutes %d" % uiMinutes )
  print("fSec %.1f" % fSec )
  # Vérification pas à 0
  if( ( uiHours == 0 ) and ( uiMinutes == 0 ) and ( fSec == 0 ) ):
   print("Error")
   self.siErrorMsg.emit("Log event state error", "Log event period can not be 0 second")
   return
  # Calcul de l'event interval en 10ieme de sec
  uiEventInterval = int( ( ( uiHours * 60 + uiMinutes ) * 60 + fSec ) * 10 )
  # Assigne les valeurs dans notre structu
  self.tProduct.ttConfig["PRODUCT"]["uiEventInterval"] = uiEventInterval
  self.tProduct.ttConfig["PRODUCT"]["uiEventHour"]     = uiHours
  self.tProduct.ttConfig["PRODUCT"]["uiEventMin"]      = uiMinutes
  self.tProduct.ttConfig["PRODUCT"]["fEventSec"]       = fSec
  # Lancement écriture vers sonde
  self.tProduct.bFProductEventLogCheckPeriodWrite()

 #----------------------------------------------
 # DASHBOARD - Ecriture event Log pressure
 #----------------------------------------------
 @Slot(int)
 def slotWriteEventLogPressure(self, fPressureLimit):
  print("== slotWriteEventLogPressure ==")
  print("fPressureLimit %.3f" % fPressureLimit )
  self.tProduct.ttConfig["PRODUCT"]["fPressureLimit"]  = fPressureLimit
  self.tProduct.ttConfig["PRODUCT"]["uiPressureLimit"] = int(fPressureLimit * 1000)
  # Lancement écriture vers sonde
  self.tProduct.bFProductEventLogLimitWrite()

 #----------------------------------------------
 # DASHBOARD - Ecriture event Log temperature
 #----------------------------------------------
 @Slot(int)
 def slotWriteEventLogTemperature(self, fTempLimit):
  print("== slotWriteEventLogTemperature ==")
  print("fTempLimit %.1f" % fTempLimit )

  self.tProduct.ttConfig["PRODUCT"]["fTempLimit"]  = fTempLimit
  self.tProduct.ttConfig["PRODUCT"]["uiTempLimit"] = int(fTempLimit * 10)
  # Lancement écriture vers sonde
  self.tProduct.bFProductEventLogLimitWrite()

 #----------------------------------------------
 # DASHBOARD - Ecriture event Log salinity
 #----------------------------------------------
 def slotWriteEventLogSalinity(self, fSalinityLimit):
  print("== slotWriteEventLogSalinity ==")
  print("fSalinityLimit %.1f" % fSalinityLimit )
  self.tProduct.ttConfig["PRODUCT"]["fSalinityLimit"]  = fSalinityLimit
  self.tProduct.ttConfig["PRODUCT"]["uiSalinityLimit"] = int(fSalinityLimit * 10)
  # Lancement écriture vers sonde
  self.tProduct.bFProductEventLogLimitWrite()

 #----------------------------------------------
 # DASHBOARD - Start/Stop product - Start date write
 #----------------------------------------------
 def slotWriteProductStartDate(self, tDatetime):
  print("== slotWriteProductStartDate ==")

  if( tDatetime != None ):
   uiYear  = tDatetime.date().year()-2000
   uiMonth = tDatetime.date().month()
   uiDay   = tDatetime.date().day()
   uiHour  = tDatetime.time().hour()
   uiMin   = tDatetime.time().minute()
   uiSec   = tDatetime.time().second()
  else:
   uiYear = uiMonth = uiDay = uiHour = uiMin = uiSec = 0

  sDate    = ("%02u/%02u/%02u %02u:%02u:%02u"%(uiDay, uiMonth, uiYear, uiHour, uiMin, uiSec))
  sDateRaw = ("%02u%02u%02u%02u%02u%02u"%(uiHour, uiMin, uiSec, uiDay, uiMonth, uiYear))
  print(sDate)
  self.tProduct.ttConfig["PRODUCT"]["uiLogStartYear"]  = uiYear
  self.tProduct.ttConfig["PRODUCT"]["uiLogStartMonth"] = uiMonth
  self.tProduct.ttConfig["PRODUCT"]["uiLogStartDay"]   = uiDay
  self.tProduct.ttConfig["PRODUCT"]["uiLogStartHour"]  = uiHour
  self.tProduct.ttConfig["PRODUCT"]["uiLogStartMin"]   = uiMin
  self.tProduct.ttConfig["PRODUCT"]["uiLogStartSec"]   = uiSec
  self.tProduct.ttConfig["PRODUCT"]["sLogStartDate"]   = sDate
  self.tProduct.ttConfig["PRODUCT"]["sLogDateRaw"]     = sDateRaw

  # Lancement écriture vers sonde
  self.tProduct.bFProductLogStartDateWrite()

 """
 #----------------------------------------------
 # DASHBOARD - Clear memory
 #----------------------------------------------
 def slotClearSondeMemory(self):
  print("== slotClearSondeMemory ==")



  # Lancement écriture vers sonde
  self.tProduct.bFProductClearMemory()


 #----------------------------------------------
 # DASHBOARD - Reset LeveLine
 #----------------------------------------------
 def slotResetLeveLine(self):
  print("== slotResetLeveLine ==")



  # Lancement écriture vers sonde
  self.tProduct.bFProductResetLeveLine()
 """

 #----------------------------------------------
 # Calibration - Ecriture point Restore default
 #----------------------------------------------
 def slotWriteCalibrationErrorMsg( self, sError ):

  uiPointNumber = self.uiPointNumber
  uiCode        = self.uiCode
  # Etat initial du message
  sMessage = sError

  #-- Temperature fail --
  if( sError == "Temperature fail" ):
   sMessage = "The temperature is outside the calibration limits\nPlease investigate and try again"
   # Si point 2
   if( uiPointNumber == 1 ):
    sMessage = "The temperature of Point 2 must be within 1C of Point 1\nPlease correct and try again"
   # Si point 3
   if( uiPointNumber == 2 ):
     sMessage = "The temperature of Point 3 must be at least 10C cooler than Point 1\nPlease correct and try again"

  #-- Range fail --
  if( sError == "Range fail" ):
   sMessage = "The readings are outside the calibration limits\nCheck you are using the correct standard and try again"
   # RapidCal
   if( uiCode == 226 ):
    sMessage = "One or more of the readings are outside the calibration limits\nCheck you are using fresh RapidCal and that all electrodes are covered"

  #-- DO fail --
  if( sError == "DO fail" ):
   sMessage = "There is a problem with the DO sensor.\nPlease investigate and try again"

  # Emet le message d'erreur
  self.siCalibrationCMDPointError.emit(sMessage)


 #----------------------------------------------
 # Calibration - Ecriture point Restore default
 #----------------------------------------------
 def vFCALIBSaveTemperatureCalibEnd( self ):
  ttConfig = self.tProduct.ttConfig
  #-- Temperature
  # EC
  if( self.uiCode == 231 ): ttConfig["SENSOR"]["EC"]["Point"][0]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  if( self.uiCode == 229 ): ttConfig["SENSOR"]["EC"]["Point"][0]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  if( self.uiCode == 210 ): ttConfig["SENSOR"]["EC"]["Point"][0]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]
  if( self.uiCode == 224 ): ttConfig["SENSOR"]["EC"]["Point"][0]["fTemp"] = ttConfig["SENSOR"]["TEMP"]["fResult"]

