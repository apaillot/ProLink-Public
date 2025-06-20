# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WChannelSelect.ui'
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

class Ui_WChannelSelect(object):
    def setupUi(self, WChannelSelect):
        if not WChannelSelect.objectName():
            WChannelSelect.setObjectName(u"WChannelSelect")
        WChannelSelect.resize(394, 160)
        WChannelSelect.setStyleSheet(u"#WChannelSelect {\n"
" background-color:white;\n"
" border-radius: 5px;\n"
"}\n"
"#label{\n"
" color: #3E4072;\n"
" font-weight: 800;\n"
"}\n"
"#label_Title{\n"
" color: #8F8F8F;\n"
" font-weight: 600;\n"
"}\n"
"QLineEdit,\n"
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
        self.verticalLayout = QVBoxLayout(WChannelSelect)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_Title = QLabel(WChannelSelect)
        self.label_Title.setObjectName(u"label_Title")
        font = QFont()
        font.setPointSize(12)
        font.setWeight(QFont.DemiBold)
        self.label_Title.setFont(font)
        self.label_Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_Title)

        self.line = QFrame(WChannelSelect)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.widget = QWidget(WChannelSelect)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBox_ChannelSelect = QComboBox(self.widget)
        self.comboBox_ChannelSelect.addItem("")
        self.comboBox_ChannelSelect.addItem("")
        self.comboBox_ChannelSelect.addItem("")
        self.comboBox_ChannelSelect.addItem("")
        self.comboBox_ChannelSelect.addItem("")
        self.comboBox_ChannelSelect.addItem("")
        self.comboBox_ChannelSelect.addItem("")
        self.comboBox_ChannelSelect.addItem("")
        self.comboBox_ChannelSelect.addItem("")
        self.comboBox_ChannelSelect.addItem("")
        self.comboBox_ChannelSelect.addItem("")
        self.comboBox_ChannelSelect.addItem("")
        self.comboBox_ChannelSelect.addItem("")
        self.comboBox_ChannelSelect.addItem("")
        self.comboBox_ChannelSelect.addItem("")
        self.comboBox_ChannelSelect.addItem("")
        self.comboBox_ChannelSelect.setObjectName(u"comboBox_ChannelSelect")
        self.comboBox_ChannelSelect.setMinimumSize(QSize(180, 28))
        self.comboBox_ChannelSelect.setMaximumSize(QSize(180, 16777215))

        self.gridLayout.addWidget(self.comboBox_ChannelSelect, 0, 1, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)

        self.verticalLayout.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_3 = QWidget(WChannelSelect)
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


        self.retranslateUi(WChannelSelect)
        self.pushButton_Confirm.clicked.connect(WChannelSelect.accept)
        self.pushButton_Cancel.clicked.connect(WChannelSelect.reject)

        QMetaObject.connectSlotsByName(WChannelSelect)
    # setupUi

    def retranslateUi(self, WChannelSelect):
        WChannelSelect.setWindowTitle(QCoreApplication.translate("WChannelSelect", u"AUX channel selection", None))
        self.label_Title.setText(QCoreApplication.translate("WChannelSelect", u"Sensors", None))
        self.comboBox_ChannelSelect.setItemText(0, QCoreApplication.translate("WChannelSelect", u"EMPTY", None))
        self.comboBox_ChannelSelect.setItemText(1, QCoreApplication.translate("WChannelSelect", u"Ammonium", None))
        self.comboBox_ChannelSelect.setItemText(2, QCoreApplication.translate("WChannelSelect", u"Chloride", None))
        self.comboBox_ChannelSelect.setItemText(3, QCoreApplication.translate("WChannelSelect", u"Fluoride", None))
        self.comboBox_ChannelSelect.setItemText(4, QCoreApplication.translate("WChannelSelect", u"Nitrate", None))
        self.comboBox_ChannelSelect.setItemText(5, QCoreApplication.translate("WChannelSelect", u"Calcium", None))
        self.comboBox_ChannelSelect.setItemText(6, QCoreApplication.translate("WChannelSelect", u"Turbidity", None))
        self.comboBox_ChannelSelect.setItemText(7, QCoreApplication.translate("WChannelSelect", u"Chlorophyll", None))
        self.comboBox_ChannelSelect.setItemText(8, QCoreApplication.translate("WChannelSelect", u"BGA-PC", None))
        self.comboBox_ChannelSelect.setItemText(9, QCoreApplication.translate("WChannelSelect", u"BGA-PE", None))
        self.comboBox_ChannelSelect.setItemText(10, QCoreApplication.translate("WChannelSelect", u"Rhodamine", None))
        self.comboBox_ChannelSelect.setItemText(11, QCoreApplication.translate("WChannelSelect", u"Fluorescein", None))
        self.comboBox_ChannelSelect.setItemText(12, QCoreApplication.translate("WChannelSelect", u"Refined Oil", None))
        self.comboBox_ChannelSelect.setItemText(13, QCoreApplication.translate("WChannelSelect", u"CDOM", None))
        self.comboBox_ChannelSelect.setItemText(14, QCoreApplication.translate("WChannelSelect", u"Crude Oil", None))
        self.comboBox_ChannelSelect.setItemText(15, QCoreApplication.translate("WChannelSelect", u"Tryptophan", None))

        self.label.setText(QCoreApplication.translate("WChannelSelect", u"Channel select:", None))
        self.pushButton_Confirm.setText(QCoreApplication.translate("WChannelSelect", u"Confirm", None))
        self.pushButton_Cancel.setText(QCoreApplication.translate("WChannelSelect", u"Cancel", None))
    # retranslateUi

