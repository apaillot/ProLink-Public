# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WUpdateProgress - Copie.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QProgressBar, QSizePolicy, QWidget)

class Ui_WUpdateProgress(object):
    def setupUi(self, WUpdateProgress):
        if not WUpdateProgress.objectName():
            WUpdateProgress.setObjectName(u"WUpdateProgress")
        WUpdateProgress.resize(265, 117)
        self.gridLayout = QGridLayout(WUpdateProgress)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.label_FileName = QLabel(WUpdateProgress)
        self.label_FileName.setObjectName(u"label_FileName")

        self.gridLayout.addWidget(self.label_FileName, 1, 0, 1, 1)

        self.label = QLabel(WUpdateProgress)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_FileCount = QLabel(WUpdateProgress)
        self.label_FileCount.setObjectName(u"label_FileCount")

        self.gridLayout.addWidget(self.label_FileCount, 0, 1, 1, 1)

        self.progressBar = QProgressBar(WUpdateProgress)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 2)


        self.retranslateUi(WUpdateProgress)

        QMetaObject.connectSlotsByName(WUpdateProgress)
    # setupUi

    def retranslateUi(self, WUpdateProgress):
        WUpdateProgress.setWindowTitle(QCoreApplication.translate("WUpdateProgress", u"Dialog", None))
        self.label_FileName.setText(QCoreApplication.translate("WUpdateProgress", u"--", None))
        self.label.setText(QCoreApplication.translate("WUpdateProgress", u"Downloading file...", None))
        self.label_FileCount.setText(QCoreApplication.translate("WUpdateProgress", u"--", None))
    # retranslateUi

