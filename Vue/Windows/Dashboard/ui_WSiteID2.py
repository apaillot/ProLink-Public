# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WSiteID2.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_WSiteID(object):
    def setupUi(self, WSiteID):
        if not WSiteID.objectName():
            WSiteID.setObjectName(u"WSiteID")
        WSiteID.resize(449, 160)
        WSiteID.setWindowOpacity(0.000000000000000)
        WSiteID.setAutoFillBackground(False)
        WSiteID.setStyleSheet(u"#WSiteID {\n"
" /*background-color:transparent;*/\n"
" /*background-color: rgba(255,255,255,10);*/\n"
" /*opacity: 0.5;*/\n"
"}\n"
"#WSiteID {\n"
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
"#lineEdit_SiteID{\n"
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
"}\n"
"\n"
"/*\n"
"#widget{\n"
" background-color:white;\n"
"}\n"
"#widget_2{\n"
" background-color: #F0F0F0;\n"
" border-top: 1px solid #DFDFDF;\n"
"}\n"
""
                        "*/")
        self.gridLayout_2 = QGridLayout(WSiteID)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line = QFrame(WSiteID)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.widget_2 = QWidget(WSiteID)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_Confirm = QPushButton(self.widget_2)
        self.pushButton_Confirm.setObjectName(u"pushButton_Confirm")
        self.pushButton_Confirm.setMinimumSize(QSize(0, 30))
        self.pushButton_Confirm.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_Confirm)

        self.pushButton_Cancel = QPushButton(self.widget_2)
        self.pushButton_Cancel.setObjectName(u"pushButton_Cancel")
        self.pushButton_Cancel.setMinimumSize(QSize(120, 30))
        self.pushButton_Cancel.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_Cancel)


        self.gridLayout_2.addWidget(self.widget_2, 5, 0, 1, 1)

        self.label_Title = QLabel(WSiteID)
        self.label_Title.setObjectName(u"label_Title")
        font = QFont()
        font.setPointSize(12)
        font.setWeight(QFont.DemiBold)
        self.label_Title.setFont(font)
        self.label_Title.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_Title, 1, 0, 1, 1)

        self.widget = QWidget(WSiteID)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(180, 16777215))
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_SiteID = QLineEdit(self.widget)
        self.lineEdit_SiteID.setObjectName(u"lineEdit_SiteID")
        self.lineEdit_SiteID.setMinimumSize(QSize(0, 28))
        self.lineEdit_SiteID.setMaximumSize(QSize(180, 16777215))

        self.gridLayout.addWidget(self.lineEdit_SiteID, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 2)

        self.gridLayout_2.addWidget(self.widget, 3, 0, 1, 1)


        self.retranslateUi(WSiteID)
        self.pushButton_Cancel.clicked.connect(WSiteID.reject)
        self.pushButton_Confirm.clicked.connect(WSiteID.accept)

        QMetaObject.connectSlotsByName(WSiteID)
    # setupUi

    def retranslateUi(self, WSiteID):
        WSiteID.setWindowTitle(QCoreApplication.translate("WSiteID", u"Form", None))
        self.pushButton_Confirm.setText(QCoreApplication.translate("WSiteID", u"Confirm", None))
        self.pushButton_Cancel.setText(QCoreApplication.translate("WSiteID", u"Cancel", None))
        self.label_Title.setText(QCoreApplication.translate("WSiteID", u"Site ID configuration", None))
        self.label.setText(QCoreApplication.translate("WSiteID", u"Site ID:", None))
    # retranslateUi

