# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WUpdateDetected.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_WUpdateDetected(object):
    def setupUi(self, WUpdateDetected):
        if not WUpdateDetected.objectName():
            WUpdateDetected.setObjectName(u"WUpdateDetected")
        WUpdateDetected.resize(405, 167)
        font = QFont()
        font.setPointSize(12)
        WUpdateDetected.setFont(font)
        WUpdateDetected.setStyleSheet(u"#WUpdateDetected {\n"
" background-color:white;\n"
" border-radius: 5px;\n"
"}\n"
"/*\n"
"#label{\n"
" color: #3E4072;\n"
" font-weight: 800;\n"
"}\n"
"*/\n"
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
        self.verticalLayout_2 = QVBoxLayout(WUpdateDetected)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.label_Title = QLabel(WUpdateDetected)
        self.label_Title.setObjectName(u"label_Title")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setWeight(QFont.DemiBold)
        self.label_Title.setFont(font1)
        self.label_Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_Title)

        self.line = QFrame(WUpdateDetected)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.widget_1 = QWidget(WUpdateDetected)
        self.widget_1.setObjectName(u"widget_1")
        self.widget_1.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.widget_1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 0, 20, 10)
        self.label = QLabel(self.widget_1)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_SoftwareVersion = QLabel(self.widget_1)
        self.label_SoftwareVersion.setObjectName(u"label_SoftwareVersion")

        self.verticalLayout.addWidget(self.label_SoftwareVersion)

        self.label_2 = QLabel(self.widget_1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.widget_1)

        self.widget_3 = QWidget(WUpdateDetected)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 0, 20, 0)
        self.pushButton_Confirm = QPushButton(self.widget_3)
        self.pushButton_Confirm.setObjectName(u"pushButton_Confirm")
        self.pushButton_Confirm.setMinimumSize(QSize(0, 30))
        self.pushButton_Confirm.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_Confirm)

        self.pushButton_Cancel = QPushButton(self.widget_3)
        self.pushButton_Cancel.setObjectName(u"pushButton_Cancel")
        self.pushButton_Cancel.setMinimumSize(QSize(0, 30))
        self.pushButton_Cancel.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_Cancel)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.verticalLayout_2.setStretch(3, 3)
        self.verticalLayout_2.setStretch(4, 2)

        self.retranslateUi(WUpdateDetected)
        self.pushButton_Confirm.clicked.connect(WUpdateDetected.accept)
        self.pushButton_Cancel.clicked.connect(WUpdateDetected.reject)

        QMetaObject.connectSlotsByName(WUpdateDetected)
    # setupUi

    def retranslateUi(self, WUpdateDetected):
        WUpdateDetected.setWindowTitle(QCoreApplication.translate("WUpdateDetected", u"Clear sonde memory", None))
        self.label_Title.setText(QCoreApplication.translate("WUpdateDetected", u"Update detected", None))
        self.label.setText(QCoreApplication.translate("WUpdateDetected", u"New update detected:", None))
        self.label_SoftwareVersion.setText(QCoreApplication.translate("WUpdateDetected", u"--", None))
        self.label_2.setText(QCoreApplication.translate("WUpdateDetected", u"Do you want to update now?", None))
        self.pushButton_Confirm.setText(QCoreApplication.translate("WUpdateDetected", u"Confirm", None))
        self.pushButton_Cancel.setText(QCoreApplication.translate("WUpdateDetected", u"Cancel", None))
    # retranslateUi

