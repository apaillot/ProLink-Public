# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WSetupLoggingState.ui'
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

class Ui_WSetupLoggingState(object):
    def setupUi(self, WSetupLoggingState):
        if not WSetupLoggingState.objectName():
            WSetupLoggingState.setObjectName(u"WSetupLoggingState")
        WSetupLoggingState.resize(350, 160)
        WSetupLoggingState.setStyleSheet(u"#WSetupLoggingState {\n"
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
        self.verticalLayout = QVBoxLayout(WSetupLoggingState)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_Title = QLabel(WSetupLoggingState)
        self.label_Title.setObjectName(u"label_Title")
        font = QFont()
        font.setPointSize(12)
        font.setWeight(QFont.DemiBold)
        self.label_Title.setFont(font)
        self.label_Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_Title)

        self.line = QFrame(WSetupLoggingState)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.widget = QWidget(WSetupLoggingState)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.comboBox_SetupLoggingState = QComboBox(self.widget)
        self.comboBox_SetupLoggingState.addItem("")
        self.comboBox_SetupLoggingState.addItem("")
        self.comboBox_SetupLoggingState.setObjectName(u"comboBox_SetupLoggingState")
        self.comboBox_SetupLoggingState.setMinimumSize(QSize(0, 28))
        self.comboBox_SetupLoggingState.setMaximumSize(QSize(180, 16777215))

        self.gridLayout.addWidget(self.comboBox_SetupLoggingState, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)

        self.verticalLayout.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_3 = QWidget(WSetupLoggingState)
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


        self.retranslateUi(WSetupLoggingState)
        self.pushButton_Confirm.clicked.connect(WSetupLoggingState.accept)
        self.pushButton_Cancel.clicked.connect(WSetupLoggingState.reject)

        QMetaObject.connectSlotsByName(WSetupLoggingState)
    # setupUi

    def retranslateUi(self, WSetupLoggingState):
        WSetupLoggingState.setWindowTitle(QCoreApplication.translate("WSetupLoggingState", u"Log data period configuration", None))
        self.label_Title.setText(QCoreApplication.translate("WSetupLoggingState", u"Event logging", None))
        self.label.setText(QCoreApplication.translate("WSetupLoggingState", u"State:", None))
        self.comboBox_SetupLoggingState.setItemText(0, QCoreApplication.translate("WSetupLoggingState", u"Disable", None))
        self.comboBox_SetupLoggingState.setItemText(1, QCoreApplication.translate("WSetupLoggingState", u"Enable", None))

        self.pushButton_Confirm.setText(QCoreApplication.translate("WSetupLoggingState", u"Confirm", None))
        self.pushButton_Cancel.setText(QCoreApplication.translate("WSetupLoggingState", u"Cancel", None))
    # retranslateUi

