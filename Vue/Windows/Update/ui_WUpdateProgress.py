# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WUpdateProgress.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QProgressBar, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_WUpdateProgress(object):
    def setupUi(self, WUpdateProgress):
        if not WUpdateProgress.objectName():
            WUpdateProgress.setObjectName(u"WUpdateProgress")
        WUpdateProgress.resize(335, 142)
        WUpdateProgress.setStyleSheet(u"#WUpdateProgress {\n"
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
        self.verticalLayout = QVBoxLayout(WUpdateProgress)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_Title = QLabel(WUpdateProgress)
        self.label_Title.setObjectName(u"label_Title")
        font = QFont()
        font.setPointSize(12)
        font.setWeight(QFont.DemiBold)
        self.label_Title.setFont(font)
        self.label_Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_Title)

        self.line = QFrame(WUpdateProgress)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.widget = QWidget(WUpdateProgress)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_FileCount = QLabel(self.widget)
        self.label_FileCount.setObjectName(u"label_FileCount")

        self.gridLayout.addWidget(self.label_FileCount, 0, 1, 1, 1)

        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.gridLayout.addWidget(self.progressBar, 2, 0, 1, 2)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_FileName = QLabel(self.widget)
        self.label_FileName.setObjectName(u"label_FileName")

        self.gridLayout.addWidget(self.label_FileName, 1, 0, 1, 2)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(WUpdateProgress)

        QMetaObject.connectSlotsByName(WUpdateProgress)
    # setupUi

    def retranslateUi(self, WUpdateProgress):
        WUpdateProgress.setWindowTitle(QCoreApplication.translate("WUpdateProgress", u"Log data period configuration", None))
        self.label_Title.setText(QCoreApplication.translate("WUpdateProgress", u"Update progress", None))
        self.label_FileCount.setText(QCoreApplication.translate("WUpdateProgress", u"--", None))
        self.label.setText(QCoreApplication.translate("WUpdateProgress", u"Downloading file...", None))
        self.label_FileName.setText(QCoreApplication.translate("WUpdateProgress", u"--", None))
    # retranslateUi

