# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WOpticalAvg.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_WOpticalAvg(object):
    def setupUi(self, WOpticalAvg):
        if not WOpticalAvg.objectName():
            WOpticalAvg.setObjectName(u"WOpticalAvg")
        WOpticalAvg.resize(358, 180)
        WOpticalAvg.setStyleSheet(u"#WOpticalAvg {\n"
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
"QSpinBox {\n"
" background-color:#DFDFDF;\n"
" border-radius: 3px;\n"
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
        self.verticalLayout = QVBoxLayout(WOpticalAvg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_Title = QLabel(WOpticalAvg)
        self.label_Title.setObjectName(u"label_Title")
        font = QFont()
        font.setPointSize(12)
        font.setWeight(QFont.DemiBold)
        self.label_Title.setFont(font)
        self.label_Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_Title)

        self.line = QFrame(WOpticalAvg)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.widget = QWidget(WOpticalAvg)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.spinBox_OpticalAvg = QSpinBox(self.widget)
        self.spinBox_OpticalAvg.setObjectName(u"spinBox_OpticalAvg")
        self.spinBox_OpticalAvg.setMinimumSize(QSize(0, 28))
        self.spinBox_OpticalAvg.setMaximumSize(QSize(150, 16777215))
        self.spinBox_OpticalAvg.setReadOnly(False)
        self.spinBox_OpticalAvg.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinBox_OpticalAvg.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.spinBox_OpticalAvg.setMinimum(16)
        self.spinBox_OpticalAvg.setMaximum(192)
        self.spinBox_OpticalAvg.setSingleStep(16)
        self.spinBox_OpticalAvg.setValue(128)

        self.gridLayout.addWidget(self.spinBox_OpticalAvg, 0, 1, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_4 = QWidget(WOpticalAvg)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_Confirm = QPushButton(self.widget_4)
        self.pushButton_Confirm.setObjectName(u"pushButton_Confirm")
        self.pushButton_Confirm.setMinimumSize(QSize(0, 30))
        self.pushButton_Confirm.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_Confirm)

        self.pushButton_Cancel = QPushButton(self.widget_4)
        self.pushButton_Cancel.setObjectName(u"pushButton_Cancel")
        self.pushButton_Cancel.setMinimumSize(QSize(120, 30))
        self.pushButton_Cancel.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_Cancel)


        self.verticalLayout.addWidget(self.widget_4)


        self.retranslateUi(WOpticalAvg)
        self.pushButton_Confirm.clicked.connect(WOpticalAvg.accept)
        self.pushButton_Cancel.clicked.connect(WOpticalAvg.reject)

        QMetaObject.connectSlotsByName(WOpticalAvg)
    # setupUi

    def retranslateUi(self, WOpticalAvg):
        WOpticalAvg.setWindowTitle(QCoreApplication.translate("WOpticalAvg", u"Log data period configuration", None))
        self.label_Title.setText(QCoreApplication.translate("WOpticalAvg", u"Averaging", None))
        self.spinBox_OpticalAvg.setSuffix("")
        self.spinBox_OpticalAvg.setPrefix("")
        self.label.setText(QCoreApplication.translate("WOpticalAvg", u"Optical Electrodes\n"
"averaging time\n"
"constant (samples)", None))
        self.pushButton_Confirm.setText(QCoreApplication.translate("WOpticalAvg", u"Confirm", None))
        self.pushButton_Cancel.setText(QCoreApplication.translate("WOpticalAvg", u"Cancel", None))
    # retranslateUi

