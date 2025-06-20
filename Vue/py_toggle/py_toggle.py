
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

#class PyToggle(QCheckBox):
class PyToggle(QCheckBox):
 def __init__(self):
  '''
  def __init__(self,
               width = 30,
               bg_color = "#D2D2D2",
               circle_color = "#FFFFFD",
               active_color = "#4F5184",
               animation_curve = QEasingCurve.OutQuint):'''
  # Init
  QCheckBox.__init__(self)
  width = 30
  bg_color = "#D2D2D2"
  circle_color = "#FFFFFD"
  active_color = "#4F5184"
  animation_curve = QEasingCurve.OutQuint

  # Set defautl parameters
  #self.setFixedSize(width, 28)
  self.setFixedSize(width, 16)
  self.setCursor(Qt.PointingHandCursor)

  # Colors
  self._bg_color     = bg_color
  self._circle_color = circle_color
  self._active_color = active_color

  # Create animation
  self._circle_position = 3
  self.animation = QPropertyAnimation(self, b"circle_position", self)
  self.animation.setEasingCurve(animation_curve)
  self.animation.setDuration(500) # Time in miliseconds

  # Connect state changed
  #self.stateChanged.connect(self.debug)
  self.stateChanged.connect(self.start_transition)

 # Create new set and get propertie
 @Property(float) # Get
 def circle_position(self):
  return self._circle_position

 @circle_position.setter
 def circle_position(self, pos):
  self._circle_position = pos
  self.update()

 def start_transition(self, value):
  print(f"Status: {self.isChecked()}")
  self.animation.stop() # Stop animation if running
  if( value ):
   self.animation.setEndValue(self.width() - 13)
  else:
   self.animation.setEndValue(3)
  # Start animation
  self.animation.start()

 # Set new hit area
 def hitButton(self, pos: QPoint):
  return(self.contentsRect().contains(pos))

 def paintEvent(self, e):
  # Set painter
  p = QPainter(self)
  p.setRenderHint(QPainter.Antialiasing)

  # Set as no pen
  p.setPen(Qt.NoPen)

  # Draw rectangle
  rect = QRect(0, 0, self.width(), self.height())

  #♥ Check if is checked
  if( not self.isChecked() ):
   # Draw BG
   p.setBrush(QColor(self._bg_color))
   p.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)
   # Draw circle
   p.setBrush(QColor(self._circle_color))
   #p.drawEllipse(3, 3, 22, 22)
   p.drawEllipse(self._circle_position, 3, 10, 10)
  else:
   # Draw BG
   p.setBrush(QColor(self._active_color))
   p.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)
   # Draw circle
   p.setBrush(QColor(self._circle_color))
   #p.drawEllipse(self.width() - 26, 3, 22, 22)
   p.drawEllipse(self._circle_position, 3, 10, 10)

  # End draw
  p.end()
