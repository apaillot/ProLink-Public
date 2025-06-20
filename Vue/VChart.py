# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

import random
import traceback

from PySide6.QtCharts import QChart, QSplineSeries, QValueAxis, QDateTimeAxis, QLineSeries, QLegend
from PySide6.QtCore   import Qt, QTimer, Slot, QRectF, QMargins
from PySide6.QtGui    import QPen, QColor, QBrush, QFont

tSensorColor = [
 QColor(0xFF03A9F4), # S00 - Pression constante
 QColor(0xFFF44336), # S01 - Pression Keller
 QColor(0xFFF44336), # S02 - Temperature Keller
 QColor(0xFFF44336), # S03 - Temperature CT
 QColor(0xFF26A69A), # S04 - Conductivité CT
 QColor(0xFF048B9A), # S05 - Turbidité
 QColor(0xFF193D8A), # S06 - Oxygène concentration
 QColor(0xFF193D8A), # S07 - Oxygène saturation
 QColor(0xFFB0C0E0), # S08 - pH
 QColor(0xFF8BC34A), # S09 - Turner Chla
 QColor(0xFF285C8C), # S10 - Turner 1 - Fluo-PC
 QColor(0xFF9B0015), # S11 - Turner 2 - Fluo-PE
 QColor(0xFFA1CF62), # S12 - Turner CDOM
 QColor(0xFF8BC34A), # S13 - Fluo CHLA
 QColor(0xFFFFB300), # S14 - PAR
 QColor(0xFF285C8C), # S15 - nke Fluo-PC
 QColor(0xFF9B0015), # S16 - nke Fluo-PE
 QColor(0xFFA1CF62), # S17 - nke CDOM
 QColor(0xFFCC3399), # S18 - nke Trypto
 QColor(0xFFCC3399), # S19 - Turner Trypto
 QColor(0xFFE23E42), # S20 - Redox
 QColor(0xFF1A4973), # S21 - Ammonium
 QColor(0xFF77807D), # S22 - Potassium
 QColor(0xFF339966), # S23 - Nitrate
 QColor(0xFF0099FF), # S24 - ISE-5
 QColor(0xFFFE1B00), # S25 - Oxygen temperature
 QColor(0xFF4F463F), # S26 - Hydrocarbon
 QColor(0xFF4F463F), # S27 - Crude oil
 QColor(0xFFB0C0E0), #
 QColor(0xFFB0C0E0), #
 QColor(0xFFB0C0E0), #
 QColor(0xFFB0C0E0)  #
]

class VChart(QChart):
 def __init__(self, ucChannelNumber, parent=None):
  print("-- VChart > __init__ --")
  super().__init__(QChart.ChartTypeCartesian, parent, Qt.WindowFlags())
  # Animation
  # Conservation du nombre de voie de mesure
  self.ucChannelNumber = ucChannelNumber
  # Init des variables du graphique
  self._titles = []
  self.tColor = [Qt.red, Qt.blue, Qt.red, Qt.green]
  # Création axe X
  self._axisX = QValueAxis()
  # Selon le nombre d'échantillon de profondeur
  self.uiSampleDepth = 32
  self.uiSampleCount = 0
  self._axisX.setTickCount(self.uiSampleDepth)
  self._axisX.setRange(0, 1)
  self.addAxis( self._axisX, Qt.AlignBottom )
  # Pas d'affichage glissant
  self._step = 0
  # Première donnée
  self._x = 0
  self._y = 5
  # Init des séries
  self._series  = []
  self._axisY   = []
  self._tfY     = [None for _ in range(ucChannelNumber)]
  tPen = []

  self.tfMin = []
  self.tfMax = []

  self.tPenTemplate = QPen()
  self.tPenTemplate.setMiterLimit(0)
  self.tPenTemplate.setWidth(2);
  # On boucle sur les voies de mesure
  for ucChannelCpt in range(0, self.ucChannelNumber):
   self._series.append( QLineSeries(self) )
   self._axisY.append( QValueAxis() )
   self._series[ucChannelCpt].setPointsVisible(True)
   self._series[ucChannelCpt].setPen( self.tPenTemplate )
   # Ajout du nom de la série
   self._series[ucChannelCpt].setName("Line 2")
   self.addSeries(self._series[ucChannelCpt])
   # Y
   self._axisY[ucChannelCpt].setRange(-5, 262144)

   '''
   # Test changement de couleur axes
   self._axisY[ucChannelCpt].setLabelsColor(QColor(0xFFF44336))
   self._axisY[ucChannelCpt].setShadesBorderColor(QColor(0xFFF44336))
   self._axisY[ucChannelCpt].setShadesColor (QColor(0xFFF44336))
   self.tAxisPen = QPen()
   self.tAxisPen.setBrush( QColor(0xFFF44336) )
   self._axisY[ucChannelCpt].setLinePen( self.tAxisPen )
   '''

   # Customize axis label font
   labelsFont = QFont()
   labelsFont.setPixelSize(10)
   self._axisX.setLabelsFont(labelsFont)
   self._axisY[ucChannelCpt].setLabelsFont(labelsFont)
   # Chiffre entier sur axe des X
   self._axisX.setLabelFormat("%.0f");

   ##self.addAxis(self._axisY[ucChannelCpt], Qt.AlignLeft)
   ###self._series[ucChannelCpt].attachAxis(self._axisX)
   ###self._series[ucChannelCpt].attachAxis(self._axisY[ucChannelCpt])

  # Ajout des axes inversés
  # On boucle sur les voies de mesure
  print("BEFORE")
  for ucChannelCpt in range(0, self.ucChannelNumber):
   self.addAxis(self._axisY[self.ucChannelNumber-1-ucChannelCpt], Qt.AlignLeft)
  print("AFTER")

  # On boucle sur les voies de mesure
  for ucChannelCpt in range(0, self.ucChannelNumber):
   # Lien axes avec séries
   self._series[ucChannelCpt].attachAxis(self._axisX)
   self._series[ucChannelCpt].attachAxis(self._axisY[ucChannelCpt])

  # Test diminution marge
  self.layout().setContentsMargins(0, 0, 0, 0)
  self.setContentsMargins(0, 0, 0, 0)
  self.setBackgroundRoundness(0)
  # Legende
  self.legend().setAlignment(Qt.AlignTop)
  self.legend().setShowToolTips(True)

 #--------------------------------------
 # TEST - Ajout série
 #--------------------------------------
 def vFAddSeries(self, uiChannelIndex):
  '''
  print("-- vFRemoveSeries --")
  print("self.ucChannelNumber = %u"%self.ucChannelNumber)
  print("uiChannelIndex = %u"%uiChannelIndex)
  print("self._series[uiChannelIndex]")
  print(self._series[uiChannelIndex])
  print("self._series[uiChannelIndex].name()")
  print(self._series[uiChannelIndex].name())
  print(self._series[uiChannelIndex])
  print(len(self._series))
  '''

  #self.addSeries( self._series[uiChannelIndex] )
  #self.addAxis(self._axisY[uiChannelIndex], Qt.AlignLeft)
  try:
   self._series[uiChannelIndex].setVisible( True )
   self._axisY[uiChannelIndex].setVisible( True )
  except Exception as err:
   print(err)
   print("uiChannelIndex = %u"%uiChannelIndex)
   print(self._series)
   quit()
  ###
  '''
  # On boucle sur les voies de mesure
  for ucChannelCpt in range(0, self.ucChannelNumber):
   # Ajout du nom de la série
   self.addSeries(self._series[ucChannelCpt])
  '''
  ###

 #--------------------------------------
 # TEST - Suppression série
 #--------------------------------------
 def vFRemoveSeries(self, uiChannelIndex):
  '''
  print("-- vFRemoveSeries --")
  print("self.ucChannelNumber = %u"%self.ucChannelNumber)
  print("uiChannelIndex = %u"%uiChannelIndex)
  print("self._series[uiChannelIndex]")
  print(self._series[uiChannelIndex])
  print("self._series[uiChannelIndex].name()")
  print(self._series[uiChannelIndex].name())
  print(self._series[uiChannelIndex])
  print(len(self._series))
  '''
  #self.removeSeries( self._series[uiChannelIndex] )
  #self.removeAxis(self._axisY[uiChannelIndex])
  self._series[uiChannelIndex].setVisible( False )
  self._axisY[uiChannelIndex].setVisible( False )

 #--------------------------------------
 # Clear du graph
 #--------------------------------------
 def vFClear(self):
  print( "== vFClear ==" )
  print("Channel 0 count : %u" % self._series[ 0 ].count())
  # Réinit du min et max
  self.tfMin = []
  self.tfMax = []
  # On boucle sur les voies de mesure
  for ucChannelCpt in range(0, self.ucChannelNumber):
   # Point count
   uiPointCount = self._series[ ucChannelCpt ].count()
   # Remove all points
   self._series[ ucChannelCpt ].removePoints(0,uiPointCount)
  print("After count()")
  print("Channel 0 count : %u" % self._series[ 0 ].count())
  # Sample count
  self.uiSampleCount = 0

 #--------------------------------------
 # Clear du graph
 #--------------------------------------
 def vFSetSampleDepth(self, uiSampleDepth):
  # Sauv du nombre d'échantillon de profondeur
  self.uiSampleDepth = uiSampleDepth-2
  #self._axisX.setTickCount(uiSampleDepth)

 #--------------------------------------
 # Add sample
 #--------------------------------------
 def vFAddSample(self, tResult):
  #print("== vFAddSample ==")

  #print(self._series[0])
  uiStart = self.uiSampleCount - self.uiSampleDepth
  uiStop  = self.uiSampleCount

  # Gestion de la profondeur d'affichage
  if(   ( self.uiSampleDepth > 0 )
    and ( self.uiSampleCount > self.uiSampleDepth ) ):
   self._axisX.setRange(uiStart, uiStop)
  else:
   self._axisX.setRange(0, uiStop)

  y = (self._axisX.max() - self._axisX.min()) / self._axisX.tickCount()

  # On boucle sur les voies de mesure
  for ucChannelCpt in range(len(tResult)):
   #print(ucChannelCpt)
   #print(tResult[ucChannelCpt])
   self._tfY[ucChannelCpt]  = tResult[ucChannelCpt]
   # Ajout du point à la fin de la série
   self._series[ucChannelCpt].append(self.uiSampleCount,
                                     self._tfY[ucChannelCpt] )
   # Premier échantillon
   if( self._series[ucChannelCpt].count() <= 1 ):
    self.tfMin.append( tResult[ucChannelCpt] )
    self.tfMax.append( tResult[ucChannelCpt] )
   # Si profondeur du graphique restreint
   if(   ( self.uiSampleDepth > 0 )
     and ( self.uiSampleCount > self.uiSampleDepth ) ):
    ''''''
    self.tfMin[ucChannelCpt] = tResult[ucChannelCpt]
    self.tfMax[ucChannelCpt] = tResult[ucChannelCpt]

    #print("uiStart = %d"%uiStart)
    #print("uiStop  = %d"%uiStop)
    # Parcours des points de la série
    for uiCpt in range(1, int(uiStop)-int(uiStart)+2):
     #print("uiCpt = %d"%uiCpt)
     #print("self._series[ucChannelCpt].at(uiCpt).y() = %f"%self._series[ucChannelCpt].at(uiCpt).y())

     if( self._series[ucChannelCpt].at(uiCpt).y() < self.tfMin[ucChannelCpt] ):
      self.tfMin[ucChannelCpt] = self._series[ucChannelCpt].at(uiCpt).y()
     if( self._series[ucChannelCpt].at(uiCpt).y() > self.tfMax[ucChannelCpt] ):
      self.tfMax[ucChannelCpt] = self._series[ucChannelCpt].at(uiCpt).y()

    #print("=== POP ===")
    #print(self._series[ucChannelCpt])
    self._series[ucChannelCpt].remove(0)
    #print(self._series[ucChannelCpt])
   # Profondeur de graphique illimité
   else:
    uiLast = self._series[ucChannelCpt].count()-1
    #print("uiLast = %d"%uiLast)
    if( self._series[ucChannelCpt].at(uiLast).y() < self.tfMin[ucChannelCpt] ):
     self.tfMin[ucChannelCpt] = self._series[ucChannelCpt].at(uiLast).y()
    if( self._series[ucChannelCpt].at(uiLast).y() > self.tfMax[ucChannelCpt] ):
     self.tfMax[ucChannelCpt] = self._series[ucChannelCpt].at(uiLast).y()

   fDelta = ( self.tfMax[ucChannelCpt] - self.tfMin[ucChannelCpt] ) / 32
   # Patch pour redimensionner les axes
   self._axisY[ucChannelCpt].setRange(0,1)

   if( fDelta == 0 ):
    fDelta = self.tfMin[ucChannelCpt] * 1 / 100
    self._axisY[ucChannelCpt].setRange(self.tfMin[ucChannelCpt]-fDelta, self.tfMax[ucChannelCpt]+fDelta)
   else:
    #
    self._axisY[ucChannelCpt].setRange(self.tfMin[ucChannelCpt]-fDelta, self.tfMax[ucChannelCpt]+fDelta)

  # Incrément
  self.uiSampleCount = self.uiSampleCount + 1
  # Mise à jour (pour test)
  self.update()



 #------------------------------------------------------------------------------------
 #--------------------------------------
 # Add sample
 #--------------------------------------
 def vFAddSample_old(self, tResult):
  #print("== vFAddSample ==")
  # Gestion axe des X
  uiStart = self._series[0].count() - self.uiSampleDepth
  uiStop  = self._series[0].count()

  # Gestion de la profondeur d'affichage
  if(   ( self.uiSampleDepth > 0 )
    and ( self._series[0].count() > self.uiSampleDepth ) ):
   self._axisX.setRange(uiStart, uiStop)
  else:
   self._axisX.setRange(0, uiStop)

  y = (self._axisX.max() - self._axisX.min()) / self._axisX.tickCount()

  # On boucle sur les voies de mesure
  for ucChannelCpt in range(len(tResult)):
   print(ucChannelCpt)
   print(tResult[ucChannelCpt])
   self._tfY[ucChannelCpt]  = tResult[ucChannelCpt]
   # Ajout du point à la fin de la série
   self._series[ucChannelCpt].append(self._series[ucChannelCpt].count(),
                                     self._tfY[ucChannelCpt] )
   # Premier échantillon
   if( self._series[ucChannelCpt].count() <= 1 ):
    self.tfMin.append( tResult[ucChannelCpt] )
    self.tfMax.append( tResult[ucChannelCpt] )
   # Si profondeur du graphique restreint
   if(   ( self.uiSampleDepth > 0 )
     and ( self._series[ucChannelCpt].count() > self.uiSampleDepth ) ):
    self.tfMin[ucChannelCpt] = tResult[ucChannelCpt]
    self.tfMax[ucChannelCpt] = tResult[ucChannelCpt]

    for uiCpt in range(int(uiStart), int(self._series[ucChannelCpt].count())):
     if( self._series[ucChannelCpt].at(uiCpt).y() < self.tfMin[ucChannelCpt] ):
      self.tfMin[ucChannelCpt] = self._series[ucChannelCpt].at(uiCpt).y()
     if( self._series[ucChannelCpt].at(uiCpt).y() > self.tfMax[ucChannelCpt] ):
      self.tfMax[ucChannelCpt] = self._series[ucChannelCpt].at(uiCpt).y()
   # Profondeur de graphique illimité
   else:
    uiLast = self._series[ucChannelCpt].count()-1
    #print("uiLast = %d"%uiLast)
    if( self._series[ucChannelCpt].at(uiLast).y() < self.tfMin[ucChannelCpt] ):
     self.tfMin[ucChannelCpt] = self._series[ucChannelCpt].at(uiLast).y()
    if( self._series[ucChannelCpt].at(uiLast).y() > self.tfMax[ucChannelCpt] ):
     self.tfMax[ucChannelCpt] = self._series[ucChannelCpt].at(uiLast).y()

   fDelta = ( self.tfMax[ucChannelCpt] - self.tfMin[ucChannelCpt] ) / 32
   self._axisY[ucChannelCpt].setRange(self.tfMin[ucChannelCpt]-fDelta, self.tfMax[ucChannelCpt]+fDelta)


#----------------------------------------------------------------------------#
# Programme principal
#----------------------------------------------------------------------------#
if __name__ == '__main__':
 print("Test")
