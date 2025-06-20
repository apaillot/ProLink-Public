# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WSetupLoggingCheck.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_WSetupLoggingCheck(object):
    def setupUi(self, WSetupLoggingCheck):
        if not WSetupLoggingCheck.objectName():
            WSetupLoggingCheck.setObjectName(u"WSetupLoggingCheck")
        WSetupLoggingCheck.resize(408, 160)
        WSetupLoggingCheck.setStyleSheet(u"#WSetupLoggingCheck {\n"
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
"QComboBox {\n"
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
        self.verticalLayout = QVBoxLayout(WSetupLoggingCheck)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_Title = QLabel(WSetupLoggingCheck)
        self.label_Title.setObjectName(u"label_Title")
        font = QFont()
        font.setPointSize(12)
        font.setWeight(QFont.DemiBold)
        self.label_Title.setFont(font)
        self.label_Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_Title)

        self.line = QFrame(WSetupLoggingCheck)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.widget = QWidget(WSetupLoggingCheck)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(50, 16777215))
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.comboBox_SetupLoggingCheck = QComboBox(self.widget)
        self.comboBox_SetupLoggingCheck.addItem("")
        self.comboBox_SetupLoggingCheck.addItem("")
        self.comboBox_SetupLoggingCheck.addItem("")
        self.comboBox_SetupLoggingCheck.addItem("")
        self.comboBox_SetupLoggingCheck.addItem("")
        self.comboBox_SetupLoggingCheck.addItem("")
        self.comboBox_SetupLoggingCheck.addItem("")
        self.comboBox_SetupLoggingCheck.addItem("")
        self.comboBox_SetupLoggingCheck.addItem("")
        self.comboBox_SetupLoggingCheck.addItem("")
        self.comboBox_SetupLoggingCheck.addItem("")
        self.comboBox_SetupLoggingCheck.addItem("")
        self.comboBox_SetupLoggingCheck.setObjectName(u"comboBox_SetupLoggingCheck")
        self.comboBox_SetupLoggingCheck.setMinimumSize(QSize(180, 28))
        self.comboBox_SetupLoggingCheck.setMaximumSize(QSize(180, 16777215))

        self.gridLayout.addWidget(self.comboBox_SetupLoggingCheck, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)

        self.verticalLayout.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_4 = QWidget(WSetupLoggingCheck)
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


        self.retranslateUi(WSetupLoggingCheck)
        self.pushButton_Cancel.clicked.connect(WSetupLoggingCheck.reject)
        self.pushButton_Confirm.clicked.connect(WSetupLoggingCheck.accept)

        QMetaObject.connectSlotsByName(WSetupLoggingCheck)
    # setupUi

    def retranslateUi(self, WSetupLoggingCheck):
        WSetupLoggingCheck.setWindowTitle(QCoreApplication.translate("WSetupLoggingCheck", u"Log data period configuration", None))
        self.label_Title.setText(QCoreApplication.translate("WSetupLoggingCheck", u"Event logging", None))
        self.label.setText(QCoreApplication.translate("WSetupLoggingCheck", u"Check:", None))
        self.comboBox_SetupLoggingCheck.setItemText(0, QCoreApplication.translate("WSetupLoggingCheck", u"Temperature", None))
        self.comboBox_SetupLoggingCheck.setItemText(1, QCoreApplication.translate("WSetupLoggingCheck", u"Depth", None))
        self.comboBox_SetupLoggingCheck.setItemText(2, QCoreApplication.translate("WSetupLoggingCheck", u"pH", None))
        self.comboBox_SetupLoggingCheck.setItemText(3, QCoreApplication.translate("WSetupLoggingCheck", u"ORP", None))
        self.comboBox_SetupLoggingCheck.setItemText(4, QCoreApplication.translate("WSetupLoggingCheck", u"EC", None))
        self.comboBox_SetupLoggingCheck.setItemText(5, QCoreApplication.translate("WSetupLoggingCheck", u"DO", None))
        self.comboBox_SetupLoggingCheck.setItemText(6, QCoreApplication.translate("WSetupLoggingCheck", u"AUX1", None))
        self.comboBox_SetupLoggingCheck.setItemText(7, QCoreApplication.translate("WSetupLoggingCheck", u"AUX2", None))
        self.comboBox_SetupLoggingCheck.setItemText(8, QCoreApplication.translate("WSetupLoggingCheck", u"AUX3", None))
        self.comboBox_SetupLoggingCheck.setItemText(9, QCoreApplication.translate("WSetupLoggingCheck", u"AUX4", None))
        self.comboBox_SetupLoggingCheck.setItemText(10, QCoreApplication.translate("WSetupLoggingCheck", u"AUX5", None))
        self.comboBox_SetupLoggingCheck.setItemText(11, QCoreApplication.translate("WSetupLoggingCheck", u"AUX6", None))

        self.pushButton_Confirm.setText(QCoreApplication.translate("WSetupLoggingCheck", u"Confirm", None))
        self.pushButton_Cancel.setText(QCoreApplication.translate("WSetupLoggingCheck", u"Cancel", None))
    # retranslateUi

