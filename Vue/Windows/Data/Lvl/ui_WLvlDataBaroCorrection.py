# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WLvlDataBaroCorrection.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_WLvlDataBaroCorrection(object):
    def setupUi(self, WLvlDataBaroCorrection):
        if not WLvlDataBaroCorrection.objectName():
            WLvlDataBaroCorrection.setObjectName(u"WLvlDataBaroCorrection")
        WLvlDataBaroCorrection.resize(408, 228)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WLvlDataBaroCorrection.sizePolicy().hasHeightForWidth())
        WLvlDataBaroCorrection.setSizePolicy(sizePolicy)
        WLvlDataBaroCorrection.setStyleSheet(u"#WLvlDataBaroCorrection {\n"
" background-color:white;\n"
" border-radius: 5px;\n"
"}\n"
"#label,\n"
"#label_2,\n"
"#label_4 {\n"
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
"QComboBox,\n"
"QDoubleSpinBox {\n"
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
        self.verticalLayout = QVBoxLayout(WLvlDataBaroCorrection)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_Title = QLabel(WLvlDataBaroCorrection)
        self.label_Title.setObjectName(u"label_Title")
        self.label_Title.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(12)
        font.setWeight(QFont.DemiBold)
        self.label_Title.setFont(font)
        self.label_Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_Title)

        self.line = QFrame(WLvlDataBaroCorrection)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.widget = QWidget(WLvlDataBaroCorrection)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 16777215))
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.comboBox_CorrectionType = QComboBox(self.widget)
        self.comboBox_CorrectionType.addItem("")
        self.comboBox_CorrectionType.addItem("")
        self.comboBox_CorrectionType.addItem("")
        self.comboBox_CorrectionType.addItem("")
        self.comboBox_CorrectionType.setObjectName(u"comboBox_CorrectionType")
        self.comboBox_CorrectionType.setMinimumSize(QSize(180, 28))
        self.comboBox_CorrectionType.setMaximumSize(QSize(180, 16777215))

        self.gridLayout.addWidget(self.comboBox_CorrectionType, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)

        self.verticalLayout.addWidget(self.widget)

        self.widget_PartBaroSelected = QWidget(WLvlDataBaroCorrection)
        self.widget_PartBaroSelected.setObjectName(u"widget_PartBaroSelected")
        self.gridLayout_2 = QGridLayout(self.widget_PartBaroSelected)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.comboBox_BaroSelected = QComboBox(self.widget_PartBaroSelected)
        self.comboBox_BaroSelected.addItem("")
        self.comboBox_BaroSelected.setObjectName(u"comboBox_BaroSelected")
        self.comboBox_BaroSelected.setMinimumSize(QSize(180, 28))
        self.comboBox_BaroSelected.setMaximumSize(QSize(180, 16777215))

        self.gridLayout_2.addWidget(self.comboBox_BaroSelected, 0, 1, 1, 1)

        self.label_2 = QLabel(self.widget_PartBaroSelected)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 16777215))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)

        self.verticalLayout.addWidget(self.widget_PartBaroSelected)

        self.widget_PartFixedValue = QWidget(WLvlDataBaroCorrection)
        self.widget_PartFixedValue.setObjectName(u"widget_PartFixedValue")
        self.gridLayout_4 = QGridLayout(self.widget_PartFixedValue)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_4 = QLabel(self.widget_PartFixedValue)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)

        self.doubleSpinBox_FixedValue = QDoubleSpinBox(self.widget_PartFixedValue)
        self.doubleSpinBox_FixedValue.setObjectName(u"doubleSpinBox_FixedValue")
        self.doubleSpinBox_FixedValue.setMinimumSize(QSize(180, 28))
        self.doubleSpinBox_FixedValue.setMaximumSize(QSize(180, 16777215))

        self.gridLayout_4.addWidget(self.doubleSpinBox_FixedValue, 0, 1, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 1)

        self.verticalLayout.addWidget(self.widget_PartFixedValue)

        self.widget_4 = QWidget(WLvlDataBaroCorrection)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 50))
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


        self.retranslateUi(WLvlDataBaroCorrection)
        self.pushButton_Cancel.clicked.connect(WLvlDataBaroCorrection.reject)
        self.pushButton_Confirm.clicked.connect(WLvlDataBaroCorrection.accept)

        QMetaObject.connectSlotsByName(WLvlDataBaroCorrection)
    # setupUi

    def retranslateUi(self, WLvlDataBaroCorrection):
        WLvlDataBaroCorrection.setWindowTitle(QCoreApplication.translate("WLvlDataBaroCorrection", u"Log data period configuration", None))
        self.label_Title.setText(QCoreApplication.translate("WLvlDataBaroCorrection", u"Baro correction", None))
        self.label.setText(QCoreApplication.translate("WLvlDataBaroCorrection", u"Correction type", None))
        self.comboBox_CorrectionType.setItemText(0, QCoreApplication.translate("WLvlDataBaroCorrection", u"None", None))
        self.comboBox_CorrectionType.setItemText(1, QCoreApplication.translate("WLvlDataBaroCorrection", u"Logged Zeros", None))
        self.comboBox_CorrectionType.setItemText(2, QCoreApplication.translate("WLvlDataBaroCorrection", u"Baro File", None))
        self.comboBox_CorrectionType.setItemText(3, QCoreApplication.translate("WLvlDataBaroCorrection", u"Fixed", None))

        self.comboBox_BaroSelected.setItemText(0, QCoreApplication.translate("WLvlDataBaroCorrection", u"2XXXXXXX", None))

        self.label_2.setText(QCoreApplication.translate("WLvlDataBaroCorrection", u"Baro selected", None))
        self.label_4.setText(QCoreApplication.translate("WLvlDataBaroCorrection", u"Fixed value", None))
        self.pushButton_Confirm.setText(QCoreApplication.translate("WLvlDataBaroCorrection", u"Confirm", None))
        self.pushButton_Cancel.setText(QCoreApplication.translate("WLvlDataBaroCorrection", u"Cancel", None))
    # retranslateUi

