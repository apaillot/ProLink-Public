# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WUpdateDetected - Copie.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

class Ui_WUpdateDetected(object):
    def setupUi(self, WUpdateDetected):
        if not WUpdateDetected.objectName():
            WUpdateDetected.setObjectName(u"WUpdateDetected")
        WUpdateDetected.resize(240, 102)
        WUpdateDetected.setStyleSheet(u"\n"
"#widget{\n"
" background-color: #F0F0F0;\n"
" border-top: 1px solid #DFDFDF;\n"
"}\n"
"#widget_2{\n"
" background-color:white;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(WUpdateDetected)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(WUpdateDetected)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 0, 20, 10)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_SoftwareVersion = QLabel(self.widget_2)
        self.label_SoftwareVersion.setObjectName(u"label_SoftwareVersion")

        self.verticalLayout.addWidget(self.label_SoftwareVersion)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget = QWidget(WUpdateDetected)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 0, 20, 0)
        self.buttonBox = QDialogButtonBox(self.widget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.No|QDialogButtonBox.Yes)

        self.verticalLayout_3.addWidget(self.buttonBox)


        self.verticalLayout_2.addWidget(self.widget)


        self.retranslateUi(WUpdateDetected)
        self.buttonBox.accepted.connect(WUpdateDetected.accept)
        self.buttonBox.rejected.connect(WUpdateDetected.reject)

        QMetaObject.connectSlotsByName(WUpdateDetected)
    # setupUi

    def retranslateUi(self, WUpdateDetected):
        WUpdateDetected.setWindowTitle(QCoreApplication.translate("WUpdateDetected", u"Update", None))
        self.label.setText(QCoreApplication.translate("WUpdateDetected", u"New update detected:", None))
        self.label_SoftwareVersion.setText(QCoreApplication.translate("WUpdateDetected", u"--", None))
        self.label_2.setText(QCoreApplication.translate("WUpdateDetected", u"Do you want to update now ?", None))
    # retranslateUi

