# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WSiteAltitude.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_WSiteAltitude(object):
    def setupUi(self, WSiteAltitude):
        if not WSiteAltitude.objectName():
            WSiteAltitude.setObjectName(u"WSiteAltitude")
        WSiteAltitude.resize(405, 160)
        WSiteAltitude.setStyleSheet(u"#WSiteAltitude {\n"
" background-color:white;\n"
" border-radius: 5px;\n"
"}\n"
"#label{\n"
" color: #3E4072;\n"
" font-weight: 800;\n"
"}\n"
"#buttonBox{\n"
" background-color: #3E4072;\n"
"}\n"
"#label_Title{\n"
" color: #8F8F8F;\n"
" font-weight: 600;\n"
"}\n"
"QComboBox, \n"
"QSpinBox,\n"
"QDoubleSpinBox {\n"
" background-color:#DFDFDF;\n"
" border-radius: 3px;\n"
" color: black;\n"
"}\n"
"#pushButton_Confirm,\n"
"#pushButton_Cancel {\n"
" border: none;\n"
" border-radius: 8px;\n"
"}\n"
"#pushButton_Confirm {\n"
" color: white;\n"
" background-color: #3E4072;\n"
"}\n"
"#pushButton_Confirm:hover {\n"
" color: white;\n"
" background-color: #595D89;\n"
"}\n"
"#pushButton_Cancel {\n"
" background-color: #D8D8D8;\n"
"}\n"
"#pushButton_Cancel:hover {\n"
" background-color: #ACACAC;\n"
"}")
        self.verticalLayout = QVBoxLayout(WSiteAltitude)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_Title = QLabel(WSiteAltitude)
        self.label_Title.setObjectName(u"label_Title")
        font = QFont()
        font.setPointSize(12)
        font.setWeight(QFont.DemiBold)
        self.label_Title.setFont(font)
        self.label_Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_Title)

        self.line = QFrame(WSiteAltitude)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.widget = QWidget(WSiteAltitude)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.spinBox_Altitude = QSpinBox(self.widget)
        self.spinBox_Altitude.setObjectName(u"spinBox_Altitude")
        self.spinBox_Altitude.setMinimumSize(QSize(0, 28))
        self.spinBox_Altitude.setMinimum(-500)
        self.spinBox_Altitude.setMaximum(10000)

        self.gridLayout.addWidget(self.spinBox_Altitude, 0, 1, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_3 = QWidget(WSiteAltitude)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_Confirm = QPushButton(self.widget_3)
        self.pushButton_Confirm.setObjectName(u"pushButton_Confirm")
        self.pushButton_Confirm.setMinimumSize(QSize(0, 30))
        self.pushButton_Confirm.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_Confirm)

        self.pushButton_Cancel = QPushButton(self.widget_3)
        self.pushButton_Cancel.setObjectName(u"pushButton_Cancel")
        self.pushButton_Cancel.setMinimumSize(QSize(120, 30))
        self.pushButton_Cancel.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_Cancel)


        self.verticalLayout.addWidget(self.widget_3)


        self.retranslateUi(WSiteAltitude)
        self.pushButton_Confirm.clicked.connect(WSiteAltitude.accept)
        self.pushButton_Cancel.clicked.connect(WSiteAltitude.reject)

        QMetaObject.connectSlotsByName(WSiteAltitude)
    # setupUi

    def retranslateUi(self, WSiteAltitude):
        WSiteAltitude.setWindowTitle(QCoreApplication.translate("WSiteAltitude", u"Log data period configuration", None))
        self.label_Title.setText(QCoreApplication.translate("WSiteAltitude", u"Site ID and location", None))
        self.label_2.setText(QCoreApplication.translate("WSiteAltitude", u"m", None))
        self.label.setText(QCoreApplication.translate("WSiteAltitude", u"Site altitude:", None))
        self.pushButton_Confirm.setText(QCoreApplication.translate("WSiteAltitude", u"Confirm", None))
        self.pushButton_Cancel.setText(QCoreApplication.translate("WSiteAltitude", u"Cancel", None))
    # retranslateUi

