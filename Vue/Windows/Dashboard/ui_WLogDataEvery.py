# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WLogDataEvery.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_WLogDataEvery(object):
    def setupUi(self, WLogDataEvery):
        if not WLogDataEvery.objectName():
            WLogDataEvery.setObjectName(u"WLogDataEvery")
        WLogDataEvery.resize(416, 182)
        WLogDataEvery.setStyleSheet(u"#WLogDataEvery {\n"
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
"QSpinBox {\n"
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
        self.verticalLayout = QVBoxLayout(WLogDataEvery)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_Title = QLabel(WLogDataEvery)
        self.label_Title.setObjectName(u"label_Title")
        font = QFont()
        font.setPointSize(12)
        font.setWeight(QFont.DemiBold)
        self.label_Title.setFont(font)
        self.label_Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_Title)

        self.line = QFrame(WLogDataEvery)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.widget = QWidget(WLogDataEvery)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.spinBox_Mins = QSpinBox(self.widget)
        self.spinBox_Mins.setObjectName(u"spinBox_Mins")
        self.spinBox_Mins.setMinimumSize(QSize(0, 28))
        self.spinBox_Mins.setMaximum(59)

        self.gridLayout.addWidget(self.spinBox_Mins, 1, 3, 1, 1)

        self.spinBox_Secs = QSpinBox(self.widget)
        self.spinBox_Secs.setObjectName(u"spinBox_Secs")
        self.spinBox_Secs.setMinimumSize(QSize(0, 28))
        self.spinBox_Secs.setMaximum(59)

        self.gridLayout.addWidget(self.spinBox_Secs, 1, 4, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.spinBox_Hours = QSpinBox(self.widget)
        self.spinBox_Hours.setObjectName(u"spinBox_Hours")
        self.spinBox_Hours.setMinimumSize(QSize(0, 28))
        self.spinBox_Hours.setMaximumSize(QSize(16777215, 28))
        self.spinBox_Hours.setMaximum(119)

        self.gridLayout.addWidget(self.spinBox_Hours, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_3 = QWidget(WLogDataEvery)
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


        self.retranslateUi(WLogDataEvery)
        self.pushButton_Confirm.clicked.connect(WLogDataEvery.accept)
        self.pushButton_Cancel.clicked.connect(WLogDataEvery.reject)

        QMetaObject.connectSlotsByName(WLogDataEvery)
    # setupUi

    def retranslateUi(self, WLogDataEvery):
        WLogDataEvery.setWindowTitle(QCoreApplication.translate("WLogDataEvery", u"Log data period configuration", None))
        self.label_Title.setText(QCoreApplication.translate("WLogDataEvery", u"Setup logging rate", None))
        self.label_4.setText(QCoreApplication.translate("WLogDataEvery", u"Secs", None))
        self.label.setText(QCoreApplication.translate("WLogDataEvery", u"Log data every:", None))
        self.label_3.setText(QCoreApplication.translate("WLogDataEvery", u"Mins", None))
        self.label_2.setText(QCoreApplication.translate("WLogDataEvery", u"Hours", None))
        self.pushButton_Confirm.setText(QCoreApplication.translate("WLogDataEvery", u"Confirm", None))
        self.pushButton_Cancel.setText(QCoreApplication.translate("WLogDataEvery", u"Cancel", None))
    # retranslateUi

