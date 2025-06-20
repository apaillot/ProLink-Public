# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WEstimatedBattery.ui'
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
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import rc_ressource

class Ui_WEstimatedBattery(object):
    def setupUi(self, WEstimatedBattery):
        if not WEstimatedBattery.objectName():
            WEstimatedBattery.setObjectName(u"WEstimatedBattery")
        WEstimatedBattery.resize(439, 229)
        WEstimatedBattery.setStyleSheet(u"#WEstimatedBattery {\n"
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
        self.verticalLayout = QVBoxLayout(WEstimatedBattery)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_Title = QLabel(WEstimatedBattery)
        self.label_Title.setObjectName(u"label_Title")
        font = QFont()
        font.setPointSize(12)
        font.setWeight(QFont.DemiBold)
        self.label_Title.setFont(font)
        self.label_Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_Title)

        self.line = QFrame(WEstimatedBattery)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.widget = QWidget(WEstimatedBattery)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(15)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/info-button.svg"))
        self.label.setScaledContents(True)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(True)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_3 = QWidget(WEstimatedBattery)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_Confirm = QPushButton(self.widget_3)
        self.pushButton_Confirm.setObjectName(u"pushButton_Confirm")
        self.pushButton_Confirm.setMinimumSize(QSize(0, 30))
        self.pushButton_Confirm.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_Confirm)


        self.verticalLayout.addWidget(self.widget_3)


        self.retranslateUi(WEstimatedBattery)
        self.pushButton_Confirm.clicked.connect(WEstimatedBattery.accept)

        QMetaObject.connectSlotsByName(WEstimatedBattery)
    # setupUi

    def retranslateUi(self, WEstimatedBattery):
        WEstimatedBattery.setWindowTitle(QCoreApplication.translate("WEstimatedBattery", u"Log data period configuration", None))
        self.label_Title.setText(QCoreApplication.translate("WEstimatedBattery", u"Battery lifespan", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("WEstimatedBattery", u"Please be aware that the battery life estimate is just that: an estimate. The actual battery life will vary with temperature, quality of the battery and previous usage. \n"
"\n"
"Always be sure to leave a little battery life in hand to ensure that no data is lost.", None))
        self.pushButton_Confirm.setText(QCoreApplication.translate("WEstimatedBattery", u"OK", None))
    # retranslateUi

