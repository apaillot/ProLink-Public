# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WBatteryRemaining.ui'
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
    QSpacerItem, QVBoxLayout, QWidget)
import rc_ressource

class Ui_WBatteryRemaining(object):
    def setupUi(self, WBatteryRemaining):
        if not WBatteryRemaining.objectName():
            WBatteryRemaining.setObjectName(u"WBatteryRemaining")
        WBatteryRemaining.resize(435, 172)
        WBatteryRemaining.setStyleSheet(u"#WBatteryRemaining {\n"
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
"QLineEdit {\n"
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
        self.verticalLayout = QVBoxLayout(WBatteryRemaining)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_Title = QLabel(WBatteryRemaining)
        self.label_Title.setObjectName(u"label_Title")
        font = QFont()
        font.setPointSize(12)
        font.setWeight(QFont.DemiBold)
        self.label_Title.setFont(font)
        self.label_Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_Title)

        self.line = QFrame(WBatteryRemaining)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.widget = QWidget(WBatteryRemaining)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(15)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(True)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/info-button.svg"))
        self.label.setScaledContents(True)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.verticalSpacer_2 = QSpacerItem(20, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.widget_3 = QWidget(WBatteryRemaining)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 9, -1)
        self.pushButton_Confirm = QPushButton(self.widget_3)
        self.pushButton_Confirm.setObjectName(u"pushButton_Confirm")
        self.pushButton_Confirm.setMinimumSize(QSize(120, 30))
        self.pushButton_Confirm.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_Confirm)


        self.verticalLayout.addWidget(self.widget_3)


        self.retranslateUi(WBatteryRemaining)
        self.pushButton_Confirm.clicked.connect(WBatteryRemaining.accept)

        QMetaObject.connectSlotsByName(WBatteryRemaining)
    # setupUi

    def retranslateUi(self, WBatteryRemaining):
        WBatteryRemaining.setWindowTitle(QCoreApplication.translate("WBatteryRemaining", u"Log data period configuration", None))
        self.label_Title.setText(QCoreApplication.translate("WBatteryRemaining", u"Battery remaining info", None))
        self.label_2.setText(QCoreApplication.translate("WBatteryRemaining", u"It is advisable not to deploy with less than 20% battery capacity available.", None))
        self.label.setText("")
        self.pushButton_Confirm.setText(QCoreApplication.translate("WBatteryRemaining", u"OK", None))
    # retranslateUi

