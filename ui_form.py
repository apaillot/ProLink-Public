# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QDateTimeEdit, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QTextBrowser,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)
import rc_ressource

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1060, 729)
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        icon = QIcon()
        icon.addFile(u":/Logo/nav-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"#left_menu_main_cont  QPushButton,\n"
"#toggle_button_cont  QPushButton{\n"
"background-color: transparent;\n"
"padding: 0;\n"
"margin: 0;\n"
"border: none;\n"
"color: #fff;\n"
"}\n"
"\n"
"QComboBox{\n"
"color: black;\n"
"}\n"
"QScrollArea {\n"
"border: none;\n"
"}\n"
"\n"
"#centralwidget{\n"
"background-color: #4E5183;\n"
"}\n"
"#toggle_button_cont{\n"
"background-color: #ffffff;\n"
"}\n"
"#left_menu_main_cont > QWidget{\n"
"border-bottom: 2px solid rgb(28, 37, 49);\n"
"}\n"
"#left_menu_main_cont QPushButton{\n"
"padding: 10px 5px;\n"
"text-align: left;\n"
"}\n"
"QStackedWidget > QWidget{\n"
"background-color: #EFEFEF;\n"
"}\n"
"\n"
"#left_menu_main_cont QPushButton{\n"
"background-color: #3E4072;\n"
"}\n"
"\n"
"#left_menu_main_cont QPushButton:hover,\n"
"#left_menu_main_cont QPushButton:hover,\n"
"#left_menu_main_cont QPushButton:hover{\n"
"background-color: #3E4072;\n"
"border: 1px solid rgb(255,255,255);\n"
"}\n"
"\n"
"#connect_btn{\n"
"background-color: #3E4072;\n"
"border: none;\n"
"color: #fff;\n"
"}\n"
""
                        "#connect_btn:hover {\n"
"background-color: #3E4072;\n"
"border: 1px solid rgb(255,255,255);\n"
"}\n"
"\n"
"#version_label{\n"
"color: #FFFFFF\n"
"}\n"
"\n"
"/*---------------------*/\n"
"/* Groupbox                */\n"
"/*---------------------*/\n"
"#page_1_DashboardSonde QGroupBox,\n"
"#page_2_Liveview QGroupBox,\n"
"#page_4_Calibration QGroupBox,\n"
"#page_6_PC_Config QGroupBox,\n"
"#page_8_DashboardLeveLine QGroupBox {\n"
" padding-top: 25px;\n"
" font-size: 14px; \n"
" background-color:white;\n"
" font: 12px \"Open Sans\";\n"
" font-weight: 600;\n"
" border: 2px solid #eaeaea; \n"
"}\n"
"#page_1_DashboardSonde QGroupBox::title,\n"
"#page_2_Liveview QGroupBox::title,\n"
"#page_4_Calibration QGroupBox::title,\n"
"#page_6_PC_Config QGroupBox::title,\n"
"#page_8_DashboardLeveLine QGroupBox::title {\n"
" padding: 5px 5000%;\n"
" background-color: #3E4072; \n"
" color: #ffffff;\n"
" font-weight: bold;\n"
" border-left: 2px solid #eaeaea; \n"
" border-right: 2px solid #eaeaea; \n"
"}\n"
"\n"
"#stackedWidget_Nav2"
                        ",\n"
"#stackedWidget_Nav2 > QWidget{\n"
" background-color: transparent;\n"
"}\n"
"\n"
"\n"
"/*--------------------------*/\n"
"/* Menu top                         */\n"
"/*--------------------------*/\n"
"#clearSondeMem_btn,\n"
"#newBatteryFitted_btn,\n"
"#resyncClockWithPC_btn,\n"
"#clearMeasure_btn,\n"
"#recordMeasure_btn,\n"
"#startMeasure_btn,\n"
"#pushButton_SetBaro,\n"
"#getMeasureData_btn,\n"
"#exportToCSV_btn,\n"
"#exportToTAB_btn,\n"
"#exportToRAW_btn,\n"
"#exportToTxt_btn, \n"
"#rapidCal_btn,\n"
"#clearGraphCal_btn,\n"
"#pushButton_DataGraphView, \n"
"#pushButton_DataTabView,\n"
"#pushButton_LiveViewRecord,\n"
"#pushButton_LiveViewRecordStop,\n"
"#pushButton_CalibRecord,\n"
"#pushButton_CalibRecordStop,\n"
"/* Probe */\n"
"#pushButton_LiveviewSetBaro,\n"
"/* LeveLine */\n"
"#clearSondeMem_btn_2,\n"
"#resetLeveLine_btn_2,\n"
"#resyncClockWithPC_btn_2,\n"
"#startProductLeveLine_btn_3,\n"
"#startProductLeveLine_btn {\n"
" background-color: transparent; \n"
" padding: 0; \n"
" padding-left: 10px;\n"
" p"
                        "adding-right: 10px;\n"
" margin: 0; \n"
" color: #fff;\n"
" border: none;\n"
" border-left: 1px solid rgb(255,255,255);\n"
" border-right: 1px solid rgb(255,255,255);\n"
"}\n"
"\n"
"#stopMeasure_btn {\n"
" background-color: #777;\n"
" padding: 0; \n"
" padding-left: 10px;\n"
" padding-right: 10px;\n"
" margin: 0; \n"
" color: #fff;\n"
" border: none;\n"
" border-left: 1px solid rgb(255,255,255);\n"
" border-right: 1px solid rgb(255,255,255);\n"
"}\n"
"\n"
"#exportToPdf_btn, \n"
"#cleanSonde_btn,\n"
"#setBaroCal_btn {\n"
" background-color: transparent; \n"
" padding: 0; \n"
" padding-left: 10px;\n"
" padding-right: 10px;\n"
" margin: 0; \n"
" color: #fff;\n"
" border: none;\n"
" border-left: 1px solid rgb(255,255,255);\n"
" /*border-right: 1px solid rgb(255,255,255);*/\n"
"}\n"
"\n"
"#clearSondeMem_btn:hover,\n"
"#newBatteryFitted_btn:hover,\n"
"#resyncClockWithPC_btn:hover,\n"
"#clearMeasure_btn:hover,\n"
"#recordMeasure_btn:hover,\n"
"#startMeasure_btn:hover,\n"
"#stopMeasure_btn:hover,\n"
"#pushButton_SetBa"
                        "ro:hover,\n"
"#getMeasureData_btn:hover,\n"
"#exportToCSV_btn:hover,\n"
"#exportToTAB_btn:hover,\n"
"#exportToRAW_btn:hover,\n"
"#exportToPdf_btn:hover,\n"
"#exportToTxt_btn:hover,\n"
"#cleanSonde_btn:hover, \n"
"#rapidCal_btn:hover,\n"
"#setBaroCal_btn:hover,\n"
"#clearGraphCal_btn:hover,\n"
"#pushButton_DataGraphView:hover, \n"
"#pushButton_DataTabView:hover,\n"
"#pushButton_LiveViewRecord:enabled:hover,\n"
"#pushButton_LiveViewRecordStop:hover,\n"
"#pushButton_CalibRecord:enabled:hover,\n"
"#pushButton_CalibRecordStop:hover,\n"
"/* Probe */\n"
"#pushButton_LiveviewSetBaro:hover,\n"
"/* LeveLine */\n"
"#clearSondeMem_btn_2:hover,\n"
"#resetLeveLine_btn_2:hover,\n"
"#resyncClockWithPC_btn_2:hover,\n"
"#startProductLeveLine_btn_3:hover,\n"
"#startProductLeveLine_btn:hover  {\n"
" border: 1px solid rgb(255,255,255);\n"
"}\n"
"\n"
"#pushButton_LiveViewRecord:disabled,\n"
"#pushButton_CalibRecord:disabled {\n"
" background-color: #55F1F1F1;\n"
" color:#BABABA;\n"
"}\n"
"\n"
"/*************************************"
                        "****/\n"
"/* Connexion */\n"
"/*****************************************/\n"
"#scrollArea_2{\n"
" border: none;\n"
"}\n"
"#widget_ConnectSondeList > QWidget{\n"
" background-color: white;\n"
"}\n"
"\n"
"#widget_ConnectSondeList QPushButton,\n"
"#pushButton_detectProduct,\n"
"#pushButton_detectProbe,\n"
"#pushButton_detectLeveLine,\n"
"#pushButton_openRawFile {\n"
" background-color: #3E4072;\n"
" border: none;\n"
" color: white;\n"
" padding-top: 5px;\n"
" padding-bottom: 5px;\n"
"}\n"
"#widget_ConnectSondeList QPushButton:hover,\n"
"#pushButton_detectProduct:hover,\n"
"#pushButton_detectProbe:hover,\n"
"#pushButton_detectLeveLine:hover,\n"
"#pushButton_openRawFile:hover {\n"
" background-color: #595D89;\n"
" border: 1px solid #fff;\n"
"}\n"
"#widget_onlineHelp{\n"
" background-color: white;\n"
"}\n"
"\n"
"/*****************************************/\n"
"/* Dashboard Sonde */\n"
"/*****************************************/\n"
"#label_Model,\n"
"#label_SerialNo,\n"
"#label_InterfaceCom,\n"
"#label_SWRev,\n"
"#la"
                        "bel_RecordsStored,\n"
"#label_MemoryRemaining,\n"
"#label_BatteryRemaining,\n"
"#label_BatteryVoltage,\n"
"#label_sondeClockDate,\n"
"#label_sondeClockTime,\n"
"#label_SiteID,\n"
"#label_SiteLat,\n"
"#label_SiteLong,\n"
"#label_LogDataEvery,\n"
"#label_CleanEvery,\n"
"#label_UntilMemFull,\n"
"#label_UntilBattDead,\n"
"#label_EventLogState,\n"
"#label_EventLogCheck,\n"
"#label_EventLogEvery,\n"
"#label_EventLogThreshold,\n"
"#label_DepthRating,\n"
"#label_SiteAltitude,\n"
"/*#label_MeasStatusState,*/\n"
"#label_LogStartMode,\n"
"#label_LogStartAt,\n"
"#label_LogEndDateTime,\n"
"#label_LogDataFor,\n"
"#label_EventLogLevelValue,\n"
"#label_EventLogTemperatureValue,\n"
"#label_EventLogSalinityValue\n"
"{\n"
" color: rgb(84,84,84);\n"
"}\n"
"\n"
"#label_txtModel,\n"
"#label_txtSN,\n"
"#label_txtInterfaceCom,\n"
"#label_txtSWRev,\n"
"#label_txtRecordsStored,\n"
"#label_txtMemRemaining,\n"
"#label_txtBatteryRemaining,\n"
"#label_txtBatteryVoltage,\n"
"#label_txtSiteID,\n"
"#label_txtSiteLat,\n"
"#label_txtSiteLong,\n"
""
                        "#label_txtLogDataEvery,\n"
"#label_txtCleanEvery,\n"
"#label_txtUntilMemFull,\n"
"#label_txtUntilBattDead,\n"
"#label_txtEventLogState,\n"
"#label_txtEventLogCheck,\n"
"#label_txtEventLogEvery,\n"
"#label_txtEventLogThreshold{\n"
" font-weight: 500;\n"
"}\n"
"\n"
"#groupBox_SondeInfo > QWidget,\n"
"#groupBox_SondeClock > QWidget,\n"
"#groupBox_SiteIDLocation > QWidget,\n"
"#groupBox_DashboardSensors > QWidget,\n"
"#groupBox_SetupLogRate > QWidget,\n"
"#groupBox_EstimatedLogLife > QWidget,\n"
"#groupBox_EventLogging > QWidget, \n"
"#widget_OpticalAveraging,\n"
"#groupBox_MeasurementStatus > QWidget {\n"
" border-bottom: 1px solid #ccc;\n"
"}\n"
"\n"
"#widget_BatteryRemaining:hover,\n"
"#groupBox_EstimatedLogLife > QWidget:hover {\n"
" background-color: #efefef;\n"
"}\n"
"/*\n"
"#widget_BatteryRemaining:hover,\n"
"#groupBox_SondeClock > QWidget:hover,\n"
"#groupBox_SiteIDLocation > QWidget:hover,\n"
"#groupBox_SetupLogRate > QWidget:hover,\n"
"#groupBox_EstimatedLogLife > QWidget:hover,\n"
"#groupBox_EventLoggin"
                        "g > QWidget:hover,\n"
"#widget_OpticalAveraging:hover {\n"
" background-color: #efefef;\n"
"}\n"
"*/\n"
"\n"
"/*****************************************/\n"
"/* Dashboard LeveLine */\n"
"/*****************************************/\n"
"#label_Model_2,\n"
"#label_SerialNo_2,\n"
"#label_InterfaceCom_2,\n"
"#label_SWRev_2,\n"
"#label_RecordsStored_2,\n"
"#label_MemoryRemaining_2,\n"
"#label_BatteryRemaining_2,\n"
"#label_BatteryVoltage_2,\n"
"#label_sondeClockDate_2,\n"
"#label_sondeClockTime_2,\n"
"#label_SiteID_2,\n"
"#label_SiteLat_2,\n"
"#label_SiteLong_2,\n"
"#label_LogDataEvery_2,\n"
"#label_CleanEvery_2,\n"
"#label_UntilMemFull_2,\n"
"#label_UntilBattDead_2,\n"
"#label_EventLogState_2,\n"
"#label_EventLogCheck_2,\n"
"#label_EventLogEvery_2,\n"
"#label_EventLogThreshold_2\n"
"{\n"
" color: rgb(84,84,84);\n"
"}\n"
"\n"
"#label_txtModel_2,\n"
"#label_txtSN_2,\n"
"#label_txtInterfaceCom_2,\n"
"#label_txtSWRev_2,\n"
"#label_txtRecordsStored_2,\n"
"#label_txtMemRemaining_2,\n"
"#label_txtBatteryRemaining_2,\n"
"#"
                        "label_txtBatteryVoltage_2,\n"
"#label_txtSiteID_2,\n"
"#label_txtSiteLat_2,\n"
"#label_txtSiteLong_2,\n"
"#label_txtLogDataEvery_2,\n"
"#label_txtCleanEvery_2,\n"
"#label_txtUntilMemFull_2,\n"
"#label_txtUntilBattDead_2,\n"
"#label_txtEventLogState_2,\n"
"#label_txtEventLogCheck_2,\n"
"#label_txtEventLogEvery_2,\n"
"#label_txtEventLogThreshold_2\n"
"{\n"
" font-weight: 500;\n"
"}\n"
"\n"
"#groupBox_SondeInfo_2 > QWidget,\n"
"#groupBox_SondeClock_2 > QWidget,\n"
"#groupBox_SiteIDLocation_2 > QWidget,\n"
"#groupBox_DashboardSensors_2 > QWidget,\n"
"#groupBox_SetupLogRate_2 > QWidget,\n"
"#groupBox_EstimatedLogLife_2 > QWidget,\n"
"#groupBox_EventLogging_2 > QWidget, \n"
"#widget_OpticalAveraging_2 {\n"
" border-bottom: 1px solid #ccc;\n"
"}\n"
"\n"
"#widget_BatteryRemaining:hover,\n"
"#groupBox_EstimatedLogLife > QWidget:hover {\n"
" background-color: #efefef;\n"
"}\n"
"/*\n"
"#widget_BatteryRemaining:hover,\n"
"#groupBox_SondeClock > QWidget:hover,\n"
"#groupBox_SiteIDLocation > QWidget:hover,\n"
"#groupBox_Set"
                        "upLogRate > QWidget:hover,\n"
"#groupBox_EstimatedLogLife > QWidget:hover,\n"
"#groupBox_EventLogging > QWidget:hover,\n"
"#widget_OpticalAveraging:hover {\n"
" background-color: #efefef;\n"
"}\n"
"*/\n"
"\n"
"/*****************************************/\n"
"/* Liveview */\n"
"/*****************************************/\n"
"#gridLayout_10  QWidget {\n"
" background-color: white;\n"
"}\n"
"#widget_11 > QWidget {\n"
" background-color: white;\n"
" /*border-bottom-left-radius: 8px;\n"
" border-bottom-right-radius: 8px;\n"
"*/\n"
" border-radius: 8px;\n"
"}\n"
"#widget_11 > QWidget:hover {\n"
" /*background-color: #f5f5f5;*/\n"
" border: 1px solid rgb(128,128,128);\n"
"}\n"
"#widget_11 QWidget QLabel{\n"
" background-color: transparent;\n"
"}\n"
"#widget_11 QWidget QPushButton {\n"
" background-color: #843C0C;\n"
" border: none;\n"
" color: white;\n"
" padding-top: 5px;\n"
" padding-bottom: 5px;\n"
" border-radius: 0;\n"
" border-top-left-radius: 8px;\n"
" border-top-right-radius: 8px;\n"
"}\n"
"#widget_11 > QWidge"
                        "t:hover QPushButton {\n"
" background-color: #A75B28;\n"
"}\n"
"\n"
"#widget_11 QWidget #widget_8 {\n"
" background-color: #843C0C;\n"
" border: none;\n"
" color: white;\n"
" padding-top: 5px;\n"
" padding-bottom: 5px;\n"
" border-radius: 0;\n"
" border-top-left-radius: 8px;\n"
" border-top-right-radius: 8px;\n"
"}\n"
"\n"
"#widget_11 QWidget QWidget::item:first QLabel {\n"
" color: white;\n"
"}\n"
"#widget_18{\n"
" background-color: white;\n"
"}\n"
"\n"
"/******************************************************************/\n"
"/* Calibration */\n"
"/******************************************************************/\n"
"#widget_CalibNav__{\n"
"border: none;\n"
"}\n"
"\n"
".buttonColorGreen { background-color: rgba(185, 245, 144, 0.9); }\n"
".colorRed { color: Red; }\n"
"\n"
"#widget_calibNavPH, \n"
"#widget_calibNavPH_2 {\n"
"background-color: #ffe3a3;\n"
"}\n"
"#widget_calibNavORP,\n"
"#widget_calibNavORP_2 {\n"
"background-color: #C5D3ED;\n"
"}\n"
"#widget_calibNavDOEC,\n"
"#widget_calibNavDOEC_2 {\n"
"backg"
                        "round-color: #2FBDFF;\n"
"}\n"
"#widget_CalibNav QLabel,\n"
"#widget_calibNavORP QLabel,\n"
"#widget_calibNavDOEC QLabel {\n"
"color: #ffffff;\n"
"}\n"
"\n"
"#widget_CalibNav > QWidget:hover{\n"
"border:   5px solid rgb(255,255,255);\n"
"}\n"
"\n"
"QWidget#objectNameTest { \n"
"border: 5px solid rgb(255,255,255);\n"
"}\n"
"\n"
"#groupBox_pHCal7 > QWidget,\n"
"#groupBox_pHCal4 > QWidget,\n"
"#groupBox_pHCal10 > QWidget,\n"
"#groupBox_ORPCal > QWidget,\n"
"#groupBox_DOCal0 > QWidget,\n"
"#groupBox_DOCal100 > QWidget,\n"
"#groupBox_ECCal > QWidget,\n"
"#groupBox_AUX_PT1 > QWidget,\n"
"#groupBox_AUX_PT2 > QWidget,\n"
"#groupBox_AUX_PT3 > QWidget,\n"
"#groupBox_CalibrationParameters > QWidget {\n"
" border-bottom: 1px solid #ccc;\n"
"}\n"
"\n"
"#widget_pHCal7Value:hover,\n"
"#widget_DOCal0Value:hover,\n"
"#widget_DOCal100Value:hover,\n"
"#widget_AuxGSFactor:hover,\n"
"#widget_AuxPt1Value:hover,\n"
"#widget_AuxPt2Value:hover,\n"
"#widget_AuxPt3Value:hover {\n"
" background-color: #efefef;\n"
"}\n"
"QTextBrowser {\n"
""
                        " padding:15px;\n"
" background-color: white;\n"
"}\n"
"#widget_PHCalMeasure7,\n"
"#widget_graphPHCal7 {\n"
" background-color: white;\n"
"}\n"
"#stackedWidget_calibrationMain QPushButton {\n"
" background-color: #3E4072;\n"
" border: none;\n"
" color: white;\n"
" padding-top: 5px;\n"
" padding-bottom: 5px;\n"
"}\n"
"#stackedWidget_calibrationMain QPushButton:hover {\n"
" background-color: #595D89;\n"
" border: 1px solid #fff;\n"
"}\n"
"#groupBox_CalibrationParameters{\n"
" \n"
"}\n"
"#scrollArea_3,\n"
"#widget_CalibNav QWidget QWidget{\n"
" border: none;\n"
"}\n"
"\n"
"/*****************************************/\n"
"/* Data */\n"
"/*****************************************/\n"
"#label_dataStartDatetime,\n"
"#label_dataStopDatetime{\n"
" color:#3E4072;\n"
" font-weight: 800;\n"
"}\n"
"#dateTimeEdit_dataStart,\n"
"#dateTimeEdit_dataEnd {\n"
" background-color:#DFDFDF;\n"
" border-radius: 3px;\n"
" height: 30px;\n"
"}\n"
"#page_3_DataSonde QPushButton {\n"
" background-color: #3E4072;\n"
" border: none;\n"
" colo"
                        "r: white;\n"
" padding-top: 5px;\n"
" padding-bottom: 5px;\n"
"}\n"
"#page_3_DataSonde QPushButton:hover {\n"
" background-color: #595D89;\n"
" border: 1px solid #fff;\n"
"}\n"
"\n"
"/*****************************************/\n"
"/* About */\n"
"/*****************************************/\n"
"#widget_AboutLicensesBtn{\n"
" background-color: #3E4072;\n"
" color: white;\n"
"}\n"
"#widget_AboutLicensesBtn:hover {\n"
" background-color: #595D89;\n"
" border: 1px solid #fff;\n"
"}\n"
"#widget_AboutLicensesBtn QLabel{\n"
" color: white;\n"
"}\n"
"\n"
"/*****************************************/\n"
"/* PC Config */\n"
"/*****************************************/\n"
"#label_EventLogEvery,\n"
"#label_EventLogThreshold\n"
"{\n"
" color: rgb(84,84,84);\n"
"}\n"
"#label_txtEventLogEvery,\n"
"#label_txtEventLogThreshold\n"
"{\n"
" font-weight: 500;\n"
"}\n"
"#groupBox_PCConf_Measure > QWidget, \n"
"#groupBox_PCConf_AppSettings > QWidget {\n"
" border-bottom: 1px solid #ccc;\n"
"}\n"
"#groupBox_PCConf_Measure > QWidget:hov"
                        "er, \n"
"#groupBox_PCConf_AppSettings > QWidget:hover {\n"
" background-color: #efefef;\n"
"}\n"
"#page_6_PC_Config {\n"
" /*background-image: url( ':/Logo/Dashboard/Sonde info/3-Software-version-grey.svg' );*/\n"
" border-image: url(:/Logo/PCConf/3-Software-version-grey.svg) 0 0 0 0 stretch stretch;\n"
"}\n"
"\n"
"/*******************************************************************************\n"
"/* LeveLine */\n"
"\n"
"/********************************/\n"
"/* Dashboard */\n"
"/********************************/\n"
"#label_MeasStatusState{\n"
" font-weight: 800;\n"
" color: red;\n"
"}\n"
"\n"
"#startProductLeveLine_btn{\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_8 = QGridLayout(self.centralwidget)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 60))
        self.header.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_5 = QHBoxLayout(self.header)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.toggle_button_cont = QWidget(self.header)
        self.toggle_button_cont.setObjectName(u"toggle_button_cont")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggle_button_cont.sizePolicy().hasHeightForWidth())
        self.toggle_button_cont.setSizePolicy(sizePolicy)
        self.toggle_button_cont.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_4 = QHBoxLayout(self.toggle_button_cont)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggle_button = QPushButton(self.toggle_button_cont)
        self.toggle_button.setObjectName(u"toggle_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toggle_button.sizePolicy().hasHeightForWidth())
        self.toggle_button.setSizePolicy(sizePolicy1)
        self.toggle_button.setMinimumSize(QSize(180, 0))
        icon1 = QIcon()
        icon1.addFile(u":/Logo/Aquaread Logo bleu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toggle_button.setIcon(icon1)
        self.toggle_button.setIconSize(QSize(150, 30))

        self.horizontalLayout_4.addWidget(self.toggle_button)


        self.horizontalLayout_5.addWidget(self.toggle_button_cont)

        self.widget_4 = QWidget(self.header)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy2)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_Nav2 = QStackedWidget(self.widget_4)
        self.stackedWidget_Nav2.setObjectName(u"stackedWidget_Nav2")
        self.menu_connexion = QWidget()
        self.menu_connexion.setObjectName(u"menu_connexion")
        self.stackedWidget_Nav2.addWidget(self.menu_connexion)
        self.menu_dashboard = QWidget()
        self.menu_dashboard.setObjectName(u"menu_dashboard")
        self.horizontalLayout_36 = QHBoxLayout(self.menu_dashboard)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.widget_DashboardNavBtn = QWidget(self.menu_dashboard)
        self.widget_DashboardNavBtn.setObjectName(u"widget_DashboardNavBtn")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_DashboardNavBtn)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.clearSondeMem_btn = QPushButton(self.widget_DashboardNavBtn)
        self.clearSondeMem_btn.setObjectName(u"clearSondeMem_btn")
        self.clearSondeMem_btn.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setPointSize(8)
        self.clearSondeMem_btn.setFont(font)
        self.clearSondeMem_btn.setAutoFillBackground(False)
        self.clearSondeMem_btn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/Logo/Dashboard/Nav/Clear-sonde.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clearSondeMem_btn.setIcon(icon2)
        self.clearSondeMem_btn.setIconSize(QSize(24, 24))
        self.clearSondeMem_btn.setFlat(False)

        self.horizontalLayout_7.addWidget(self.clearSondeMem_btn)

        self.newBatteryFitted_btn = QPushButton(self.widget_DashboardNavBtn)
        self.newBatteryFitted_btn.setObjectName(u"newBatteryFitted_btn")
        self.newBatteryFitted_btn.setMinimumSize(QSize(0, 40))
        self.newBatteryFitted_btn.setFont(font)
        self.newBatteryFitted_btn.setAutoFillBackground(False)
        self.newBatteryFitted_btn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/Logo/Dashboard/Nav/New-battery-fitted.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.newBatteryFitted_btn.setIcon(icon3)
        self.newBatteryFitted_btn.setIconSize(QSize(24, 24))
        self.newBatteryFitted_btn.setFlat(False)

        self.horizontalLayout_7.addWidget(self.newBatteryFitted_btn)

        self.resyncClockWithPC_btn = QPushButton(self.widget_DashboardNavBtn)
        self.resyncClockWithPC_btn.setObjectName(u"resyncClockWithPC_btn")
        self.resyncClockWithPC_btn.setMinimumSize(QSize(0, 40))
        self.resyncClockWithPC_btn.setFont(font)
        self.resyncClockWithPC_btn.setAutoFillBackground(False)
        self.resyncClockWithPC_btn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/Logo/Dashboard/Nav/Resync-clock-with-PC.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.resyncClockWithPC_btn.setIcon(icon4)
        self.resyncClockWithPC_btn.setIconSize(QSize(24, 24))
        self.resyncClockWithPC_btn.setFlat(False)

        self.horizontalLayout_7.addWidget(self.resyncClockWithPC_btn)


        self.horizontalLayout_36.addWidget(self.widget_DashboardNavBtn)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_10)

        self.stackedWidget_Nav2.addWidget(self.menu_dashboard)
        self.menu_liveview = QWidget()
        self.menu_liveview.setObjectName(u"menu_liveview")
        self.horizontalLayout_62 = QHBoxLayout(self.menu_liveview)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(-1, -1, 50, -1)
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(20, -1, -1, -1)
        self.startMeasure_btn = QPushButton(self.menu_liveview)
        self.startMeasure_btn.setObjectName(u"startMeasure_btn")
        self.startMeasure_btn.setMinimumSize(QSize(120, 40))
        self.startMeasure_btn.setFont(font)
        self.startMeasure_btn.setAutoFillBackground(False)
        self.startMeasure_btn.setStyleSheet(u"")
        self.startMeasure_btn.setIcon(icon2)
        self.startMeasure_btn.setIconSize(QSize(0, 0))
        self.startMeasure_btn.setFlat(False)

        self.horizontalLayout_26.addWidget(self.startMeasure_btn)

        self.stopMeasure_btn = QPushButton(self.menu_liveview)
        self.stopMeasure_btn.setObjectName(u"stopMeasure_btn")
        self.stopMeasure_btn.setMinimumSize(QSize(120, 40))
        self.stopMeasure_btn.setFont(font)
        self.stopMeasure_btn.setAutoFillBackground(False)
        self.stopMeasure_btn.setStyleSheet(u"")
        self.stopMeasure_btn.setIcon(icon2)
        self.stopMeasure_btn.setIconSize(QSize(0, 0))
        self.stopMeasure_btn.setFlat(False)

        self.horizontalLayout_26.addWidget(self.stopMeasure_btn)

        self.clearMeasure_btn = QPushButton(self.menu_liveview)
        self.clearMeasure_btn.setObjectName(u"clearMeasure_btn")
        self.clearMeasure_btn.setMinimumSize(QSize(120, 40))
        self.clearMeasure_btn.setFont(font)
        self.clearMeasure_btn.setAutoFillBackground(False)
        self.clearMeasure_btn.setStyleSheet(u"")
        self.clearMeasure_btn.setIcon(icon3)
        self.clearMeasure_btn.setIconSize(QSize(0, 0))
        self.clearMeasure_btn.setFlat(False)

        self.horizontalLayout_26.addWidget(self.clearMeasure_btn)


        self.horizontalLayout_62.addLayout(self.horizontalLayout_26)

        self.horizontalSpacer_14 = QSpacerItem(222, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_14)

        self.pushButton_LiveviewSetBaro = QPushButton(self.menu_liveview)
        self.pushButton_LiveviewSetBaro.setObjectName(u"pushButton_LiveviewSetBaro")
        self.pushButton_LiveviewSetBaro.setEnabled(True)
        self.pushButton_LiveviewSetBaro.setMinimumSize(QSize(80, 40))
        icon5 = QIcon()
        icon5.addFile(u":/Logo/Sensor/SVG_blanc/F09_Baro.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_LiveviewSetBaro.setIcon(icon5)

        self.horizontalLayout_62.addWidget(self.pushButton_LiveviewSetBaro)

        self.horizontalSpacer_7 = QSpacerItem(222, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_7)

        self.pushButton_LiveViewRecord = QPushButton(self.menu_liveview)
        self.pushButton_LiveViewRecord.setObjectName(u"pushButton_LiveViewRecord")
        self.pushButton_LiveViewRecord.setEnabled(False)
        self.pushButton_LiveViewRecord.setMinimumSize(QSize(120, 40))

        self.horizontalLayout_62.addWidget(self.pushButton_LiveViewRecord)

        self.pushButton_LiveViewRecordStop = QPushButton(self.menu_liveview)
        self.pushButton_LiveViewRecordStop.setObjectName(u"pushButton_LiveViewRecordStop")
        self.pushButton_LiveViewRecordStop.setMinimumSize(QSize(120, 40))

        self.horizontalLayout_62.addWidget(self.pushButton_LiveViewRecordStop)

        self.stackedWidget_Nav2.addWidget(self.menu_liveview)
        self.menu_data = QWidget()
        self.menu_data.setObjectName(u"menu_data")
        self.horizontalLayout_58 = QHBoxLayout(self.menu_data)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(20, -1, -1, -1)
        self.getMeasureData_btn = QPushButton(self.menu_data)
        self.getMeasureData_btn.setObjectName(u"getMeasureData_btn")
        self.getMeasureData_btn.setMinimumSize(QSize(0, 40))
        self.getMeasureData_btn.setFont(font)
        self.getMeasureData_btn.setAutoFillBackground(False)
        self.getMeasureData_btn.setStyleSheet(u"")
        self.getMeasureData_btn.setIcon(icon2)
        self.getMeasureData_btn.setIconSize(QSize(24, 24))
        self.getMeasureData_btn.setFlat(False)

        self.horizontalLayout_25.addWidget(self.getMeasureData_btn)


        self.horizontalLayout_58.addLayout(self.horizontalLayout_25)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_58.addItem(self.horizontalSpacer_5)

        self.pushButton_DataTabView = QPushButton(self.menu_data)
        self.pushButton_DataTabView.setObjectName(u"pushButton_DataTabView")
        icon6 = QIcon()
        icon6.addFile(u":/Logo/Data/Numeric-W.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_DataTabView.setIcon(icon6)
        self.pushButton_DataTabView.setIconSize(QSize(35, 35))

        self.horizontalLayout_58.addWidget(self.pushButton_DataTabView)

        self.pushButton_DataGraphView = QPushButton(self.menu_data)
        self.pushButton_DataGraphView.setObjectName(u"pushButton_DataGraphView")
        icon7 = QIcon()
        icon7.addFile(u":/Logo/Data/Realtime-W.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_DataGraphView.setIcon(icon7)
        self.pushButton_DataGraphView.setIconSize(QSize(35, 35))

        self.horizontalLayout_58.addWidget(self.pushButton_DataGraphView)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_58.addItem(self.horizontalSpacer_6)

        self.widget_34 = QWidget(self.menu_data)
        self.widget_34.setObjectName(u"widget_34")
        self.horizontalLayout_40 = QHBoxLayout(self.widget_34)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(9, -1, 9, -1)
        self.exportToRAW_btn = QPushButton(self.widget_34)
        self.exportToRAW_btn.setObjectName(u"exportToRAW_btn")
        self.exportToRAW_btn.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_40.addWidget(self.exportToRAW_btn)

        self.exportToTAB_btn = QPushButton(self.widget_34)
        self.exportToTAB_btn.setObjectName(u"exportToTAB_btn")
        self.exportToTAB_btn.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_40.addWidget(self.exportToTAB_btn)

        self.exportToCSV_btn = QPushButton(self.widget_34)
        self.exportToCSV_btn.setObjectName(u"exportToCSV_btn")
        self.exportToCSV_btn.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_40.addWidget(self.exportToCSV_btn)


        self.horizontalLayout_58.addWidget(self.widget_34)

        self.stackedWidget_Nav2.addWidget(self.menu_data)
        self.menu_calibration = QWidget()
        self.menu_calibration.setObjectName(u"menu_calibration")
        self.horizontalLayout_72 = QHBoxLayout(self.menu_calibration)
        self.horizontalLayout_72.setSpacing(0)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(40, -1, 40, -1)
        self.cleanSonde_btn = QPushButton(self.menu_calibration)
        self.cleanSonde_btn.setObjectName(u"cleanSonde_btn")
        self.cleanSonde_btn.setMinimumSize(QSize(0, 40))
        self.cleanSonde_btn.setFont(font)
        self.cleanSonde_btn.setAutoFillBackground(False)
        self.cleanSonde_btn.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/Logo/Calibration/Clean-sonde.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cleanSonde_btn.setIcon(icon8)
        self.cleanSonde_btn.setIconSize(QSize(30, 30))
        self.cleanSonde_btn.setFlat(False)

        self.horizontalLayout_72.addWidget(self.cleanSonde_btn)

        self.exportToPdf_btn = QPushButton(self.menu_calibration)
        self.exportToPdf_btn.setObjectName(u"exportToPdf_btn")
        self.exportToPdf_btn.setMinimumSize(QSize(0, 40))
        self.exportToPdf_btn.setFont(font)
        self.exportToPdf_btn.setAutoFillBackground(False)
        self.exportToPdf_btn.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/Logo/Calibration/Export-to-pdf.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exportToPdf_btn.setIcon(icon9)
        self.exportToPdf_btn.setIconSize(QSize(28, 28))
        self.exportToPdf_btn.setFlat(False)

        self.horizontalLayout_72.addWidget(self.exportToPdf_btn)

        self.exportToTxt_btn = QPushButton(self.menu_calibration)
        self.exportToTxt_btn.setObjectName(u"exportToTxt_btn")
        self.exportToTxt_btn.setMinimumSize(QSize(0, 40))
        self.exportToTxt_btn.setFont(font)
        self.exportToTxt_btn.setAutoFillBackground(False)
        self.exportToTxt_btn.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u":/Logo/Calibration/txt.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exportToTxt_btn.setIcon(icon10)
        self.exportToTxt_btn.setIconSize(QSize(28, 28))
        self.exportToTxt_btn.setFlat(False)

        self.horizontalLayout_72.addWidget(self.exportToTxt_btn)

        self.horizontalSpacer_9 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_72.addItem(self.horizontalSpacer_9)

        self.rapidCal_btn = QPushButton(self.menu_calibration)
        self.rapidCal_btn.setObjectName(u"rapidCal_btn")
        self.rapidCal_btn.setMinimumSize(QSize(0, 40))
        self.rapidCal_btn.setFont(font)
        self.rapidCal_btn.setAutoFillBackground(False)
        self.rapidCal_btn.setStyleSheet(u"")
        icon11 = QIcon()
        icon11.addFile(u":/Logo/Calibration/calibration-W.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.rapidCal_btn.setIcon(icon11)
        self.rapidCal_btn.setIconSize(QSize(28, 28))
        self.rapidCal_btn.setFlat(False)

        self.horizontalLayout_72.addWidget(self.rapidCal_btn)

        self.horizontalSpacer_8 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_72.addItem(self.horizontalSpacer_8)

        self.stackedWidget_Nav2.addWidget(self.menu_calibration)
        self.menu_about = QWidget()
        self.menu_about.setObjectName(u"menu_about")
        self.stackedWidget_Nav2.addWidget(self.menu_about)
        self.menu_PC_Config = QWidget()
        self.menu_PC_Config.setObjectName(u"menu_PC_Config")
        self.stackedWidget_Nav2.addWidget(self.menu_PC_Config)
        self.menu_dashboard_lvl = QWidget()
        self.menu_dashboard_lvl.setObjectName(u"menu_dashboard_lvl")
        self.horizontalLayout_100 = QHBoxLayout(self.menu_dashboard_lvl)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.widget_DashboardNavBtn_2 = QWidget(self.menu_dashboard_lvl)
        self.widget_DashboardNavBtn_2.setObjectName(u"widget_DashboardNavBtn_2")
        self.horizontalLayout_93 = QHBoxLayout(self.widget_DashboardNavBtn_2)
        self.horizontalLayout_93.setSpacing(0)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(-1, 0, -1, 0)
        self.clearSondeMem_btn_2 = QPushButton(self.widget_DashboardNavBtn_2)
        self.clearSondeMem_btn_2.setObjectName(u"clearSondeMem_btn_2")
        self.clearSondeMem_btn_2.setMinimumSize(QSize(0, 40))
        self.clearSondeMem_btn_2.setFont(font)
        self.clearSondeMem_btn_2.setAutoFillBackground(False)
        self.clearSondeMem_btn_2.setStyleSheet(u"")
        self.clearSondeMem_btn_2.setIcon(icon2)
        self.clearSondeMem_btn_2.setIconSize(QSize(24, 24))
        self.clearSondeMem_btn_2.setFlat(False)

        self.horizontalLayout_93.addWidget(self.clearSondeMem_btn_2)

        self.resetLeveLine_btn_2 = QPushButton(self.widget_DashboardNavBtn_2)
        self.resetLeveLine_btn_2.setObjectName(u"resetLeveLine_btn_2")
        self.resetLeveLine_btn_2.setMinimumSize(QSize(0, 40))
        self.resetLeveLine_btn_2.setFont(font)
        self.resetLeveLine_btn_2.setAutoFillBackground(False)
        self.resetLeveLine_btn_2.setStyleSheet(u"")
        self.resetLeveLine_btn_2.setIcon(icon3)
        self.resetLeveLine_btn_2.setIconSize(QSize(24, 24))
        self.resetLeveLine_btn_2.setFlat(False)

        self.horizontalLayout_93.addWidget(self.resetLeveLine_btn_2)

        self.resyncClockWithPC_btn_2 = QPushButton(self.widget_DashboardNavBtn_2)
        self.resyncClockWithPC_btn_2.setObjectName(u"resyncClockWithPC_btn_2")
        self.resyncClockWithPC_btn_2.setMinimumSize(QSize(0, 40))
        self.resyncClockWithPC_btn_2.setFont(font)
        self.resyncClockWithPC_btn_2.setAutoFillBackground(False)
        self.resyncClockWithPC_btn_2.setStyleSheet(u"")
        self.resyncClockWithPC_btn_2.setIcon(icon4)
        self.resyncClockWithPC_btn_2.setIconSize(QSize(24, 24))
        self.resyncClockWithPC_btn_2.setFlat(False)

        self.horizontalLayout_93.addWidget(self.resyncClockWithPC_btn_2)


        self.horizontalLayout_100.addWidget(self.widget_DashboardNavBtn_2)

        self.horizontalSpacer_12 = QSpacerItem(421, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_100.addItem(self.horizontalSpacer_12)

        self.startProductLeveLine_btn = QPushButton(self.menu_dashboard_lvl)
        self.startProductLeveLine_btn.setObjectName(u"startProductLeveLine_btn")
        self.startProductLeveLine_btn.setMinimumSize(QSize(0, 40))
        self.startProductLeveLine_btn.setFont(font)
        self.startProductLeveLine_btn.setAutoFillBackground(False)
        self.startProductLeveLine_btn.setStyleSheet(u"")
        self.startProductLeveLine_btn.setIcon(icon4)
        self.startProductLeveLine_btn.setIconSize(QSize(24, 24))
        self.startProductLeveLine_btn.setFlat(False)

        self.horizontalLayout_100.addWidget(self.startProductLeveLine_btn)

        self.horizontalSpacer_13 = QSpacerItem(160, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_100.addItem(self.horizontalSpacer_13)

        self.stackedWidget_Nav2.addWidget(self.menu_dashboard_lvl)
        self.menu_calibration_ASAP_2 = QWidget()
        self.menu_calibration_ASAP_2.setObjectName(u"menu_calibration_ASAP_2")
        self.horizontalLayout_38 = QHBoxLayout(self.menu_calibration_ASAP_2)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalSpacer_15 = QSpacerItem(655, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_15)

        self.setBaroCal_btn = QPushButton(self.menu_calibration_ASAP_2)
        self.setBaroCal_btn.setObjectName(u"setBaroCal_btn")
        self.setBaroCal_btn.setMinimumSize(QSize(0, 40))
        self.setBaroCal_btn.setFont(font)
        self.setBaroCal_btn.setAutoFillBackground(False)
        self.setBaroCal_btn.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u":/Logo/Sensor/SVG_blanc/F08_Pressure.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setBaroCal_btn.setIcon(icon12)
        self.setBaroCal_btn.setIconSize(QSize(28, 28))
        self.setBaroCal_btn.setFlat(False)

        self.horizontalLayout_38.addWidget(self.setBaroCal_btn)

        self.clearGraphCal_btn = QPushButton(self.menu_calibration_ASAP_2)
        self.clearGraphCal_btn.setObjectName(u"clearGraphCal_btn")
        self.clearGraphCal_btn.setMinimumSize(QSize(0, 40))
        self.clearGraphCal_btn.setFont(font)
        self.clearGraphCal_btn.setAutoFillBackground(False)
        self.clearGraphCal_btn.setStyleSheet(u"")
        icon13 = QIcon()
        icon13.addFile(u":/Logo/Calibration/Clear.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clearGraphCal_btn.setIcon(icon13)
        self.clearGraphCal_btn.setIconSize(QSize(28, 28))
        self.clearGraphCal_btn.setFlat(False)

        self.horizontalLayout_38.addWidget(self.clearGraphCal_btn)

        self.horizontalSpacer_16 = QSpacerItem(655, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_16)

        self.pushButton_CalibRecord = QPushButton(self.menu_calibration_ASAP_2)
        self.pushButton_CalibRecord.setObjectName(u"pushButton_CalibRecord")
        self.pushButton_CalibRecord.setEnabled(False)
        self.pushButton_CalibRecord.setMinimumSize(QSize(120, 40))

        self.horizontalLayout_38.addWidget(self.pushButton_CalibRecord)

        self.pushButton_CalibRecordStop = QPushButton(self.menu_calibration_ASAP_2)
        self.pushButton_CalibRecordStop.setObjectName(u"pushButton_CalibRecordStop")
        self.pushButton_CalibRecordStop.setMinimumSize(QSize(120, 40))

        self.horizontalLayout_38.addWidget(self.pushButton_CalibRecordStop)

        self.stackedWidget_Nav2.addWidget(self.menu_calibration_ASAP_2)

        self.horizontalLayout_6.addWidget(self.stackedWidget_Nav2)


        self.horizontalLayout_5.addWidget(self.widget_4)


        self.gridLayout_8.addWidget(self.header, 0, 0, 1, 1)

        self.body = QWidget(self.centralwidget)
        self.body.setObjectName(u"body")
        self.horizontalLayout_3 = QHBoxLayout(self.body)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.left_menu_main_cont = QWidget(self.body)
        self.left_menu_main_cont.setObjectName(u"left_menu_main_cont")
        self.left_menu_main_cont.setMinimumSize(QSize(180, 0))
        self.verticalLayout_4 = QVBoxLayout(self.left_menu_main_cont)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.top_menu_container = QWidget(self.left_menu_main_cont)
        self.top_menu_container.setObjectName(u"top_menu_container")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.top_menu_container.sizePolicy().hasHeightForWidth())
        self.top_menu_container.setSizePolicy(sizePolicy3)
        self.verticalLayout_3 = QVBoxLayout(self.top_menu_container)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.top_menu_container)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 40, 0, 9)
        self.connexion_btn = QPushButton(self.widget)
        self.connexion_btn.setObjectName(u"connexion_btn")
        self.connexion_btn.setFont(font)
        self.connexion_btn.setStyleSheet(u"background-color: #3E4072;\n"
"/*border-left: 3px solid rgb(7 ,98 ,160);*/\n"
"border-left: 3px solid rgb(255,255,255);")
        icon14 = QIcon()
        icon14.addFile(u":/icons_default/slack.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.connexion_btn.setIcon(icon14)
        self.connexion_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.connexion_btn)

        self.dashboard_btn = QPushButton(self.widget)
        self.dashboard_btn.setObjectName(u"dashboard_btn")
        self.dashboard_btn.setFont(font)
        self.dashboard_btn.setStyleSheet(u"background-color: #3E4072;\n"
"/*border-left: 3px solid rgb(7 ,98 ,160);*/\n"
"border-left: 3px solid rgb(255,255,255);")
        icon15 = QIcon()
        icon15.addFile(u":/icons_default/airplay.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dashboard_btn.setIcon(icon15)
        self.dashboard_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.dashboard_btn)

        self.liveview_btn = QPushButton(self.widget)
        self.liveview_btn.setObjectName(u"liveview_btn")
        self.liveview_btn.setFont(font)
        icon16 = QIcon()
        icon16.addFile(u":/icons_default/activity.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.liveview_btn.setIcon(icon16)
        self.liveview_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.liveview_btn)

        self.calibration_btn = QPushButton(self.widget)
        self.calibration_btn.setObjectName(u"calibration_btn")
        self.calibration_btn.setFont(font)
        icon17 = QIcon()
        icon17.addFile(u":/icons_default/sliders.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.calibration_btn.setIcon(icon17)
        self.calibration_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.calibration_btn)

        self.data_btn = QPushButton(self.widget)
        self.data_btn.setObjectName(u"data_btn")
        self.data_btn.setFont(font)
        icon18 = QIcon()
        icon18.addFile(u":/icons_default/list.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.data_btn.setIcon(icon18)
        self.data_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.data_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pcConfig_btn = QPushButton(self.widget)
        self.pcConfig_btn.setObjectName(u"pcConfig_btn")
        self.pcConfig_btn.setFont(font)
        icon19 = QIcon()
        icon19.addFile(u":/icons_default/toggle-right.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pcConfig_btn.setIcon(icon19)
        self.pcConfig_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.pcConfig_btn)

        self.about_btn = QPushButton(self.widget)
        self.about_btn.setObjectName(u"about_btn")
        self.about_btn.setFont(font)
        icon20 = QIcon()
        icon20.addFile(u":/icons_default/zoom-in.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.about_btn.setIcon(icon20)
        self.about_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.about_btn)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(130, 40))
        self.label_12.setPixmap(QPixmap(u":/Logo/group blanc noir.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_12)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.version_label = QLabel(self.widget)
        self.version_label.setObjectName(u"version_label")
        self.version_label.setMinimumSize(QSize(0, 0))
        self.version_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.version_label)


        self.verticalLayout_3.addWidget(self.widget)


        self.verticalLayout_4.addWidget(self.top_menu_container)


        self.horizontalLayout_3.addWidget(self.left_menu_main_cont)

        self.widget_2 = QWidget(self.body)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.widget_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_0_Connection = QWidget()
        self.page_0_Connection.setObjectName(u"page_0_Connection")
        self.verticalLayout_36 = QVBoxLayout(self.page_0_Connection)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.scrollArea_2 = QScrollArea(self.page_0_Connection)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 531, 640))
        self.verticalLayout_35 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.widget_bannierePhoto = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_bannierePhoto.setObjectName(u"widget_bannierePhoto")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_bannierePhoto.sizePolicy().hasHeightForWidth())
        self.widget_bannierePhoto.setSizePolicy(sizePolicy4)
        self.widget_bannierePhoto.setMaximumSize(QSize(16777215, 180))
        self.verticalLayout_26 = QVBoxLayout(self.widget_bannierePhoto)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_8 = QLabel(self.widget_bannierePhoto)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setPixmap(QPixmap(u":/Photo/slide8.jpg"))
        self.label_8.setScaledContents(False)

        self.verticalLayout_26.addWidget(self.label_8)


        self.verticalLayout_35.addWidget(self.widget_bannierePhoto)

        self.widget_ConnectSondeList = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_ConnectSondeList.setObjectName(u"widget_ConnectSondeList")

        self.verticalLayout_35.addWidget(self.widget_ConnectSondeList)

        self.widget_10 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy)
        self.widget_10.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_15 = QGridLayout(self.widget_10)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_photoProbe = QLabel(self.widget_10)
        self.label_photoProbe.setObjectName(u"label_photoProbe")
        sizePolicy.setHeightForWidth(self.label_photoProbe.sizePolicy().hasHeightForWidth())
        self.label_photoProbe.setSizePolicy(sizePolicy)
        self.label_photoProbe.setMaximumSize(QSize(200, 200))
        self.label_photoProbe.setPixmap(QPixmap(u":/Photo/20-AP-2000.jpg"))
        self.label_photoProbe.setScaledContents(True)
        self.label_photoProbe.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_photoProbe, 1, 1, 1, 1)

        self.pushButton_detectProduct = QPushButton(self.widget_10)
        self.pushButton_detectProduct.setObjectName(u"pushButton_detectProduct")
        self.pushButton_detectProduct.setMinimumSize(QSize(0, 35))
        self.pushButton_detectProduct.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_15.addWidget(self.pushButton_detectProduct, 3, 0, 1, 1)

        self.pushButton_openRawFile = QPushButton(self.widget_10)
        self.pushButton_openRawFile.setObjectName(u"pushButton_openRawFile")
        self.pushButton_openRawFile.setMinimumSize(QSize(0, 35))
        self.pushButton_openRawFile.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_15.addWidget(self.pushButton_openRawFile, 4, 0, 1, 1)

        self.pushButton_detectProbe = QPushButton(self.widget_10)
        self.pushButton_detectProbe.setObjectName(u"pushButton_detectProbe")
        self.pushButton_detectProbe.setMinimumSize(QSize(0, 35))
        self.pushButton_detectProbe.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_15.addWidget(self.pushButton_detectProbe, 3, 1, 1, 1)

        self.pushButton_detectLeveLine = QPushButton(self.widget_10)
        self.pushButton_detectLeveLine.setObjectName(u"pushButton_detectLeveLine")
        self.pushButton_detectLeveLine.setMinimumSize(QSize(0, 35))
        self.pushButton_detectLeveLine.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_15.addWidget(self.pushButton_detectLeveLine, 3, 2, 1, 1)

        self.label_photoLeveLine = QLabel(self.widget_10)
        self.label_photoLeveLine.setObjectName(u"label_photoLeveLine")
        sizePolicy.setHeightForWidth(self.label_photoLeveLine.sizePolicy().hasHeightForWidth())
        self.label_photoLeveLine.setSizePolicy(sizePolicy)
        self.label_photoLeveLine.setMaximumSize(QSize(200, 200))
        self.label_photoLeveLine.setPixmap(QPixmap(u":/Photo/LeveLine-Baro.jpg"))
        self.label_photoLeveLine.setScaledContents(True)
        self.label_photoLeveLine.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_photoLeveLine, 1, 2, 1, 1)

        self.label_photoSonde = QLabel(self.widget_10)
        self.label_photoSonde.setObjectName(u"label_photoSonde")
        sizePolicy.setHeightForWidth(self.label_photoSonde.sizePolicy().hasHeightForWidth())
        self.label_photoSonde.setSizePolicy(sizePolicy)
        self.label_photoSonde.setMaximumSize(QSize(200, 200))
        self.label_photoSonde.setPixmap(QPixmap(u":/Photo/20-AS-2000.jpg"))
        self.label_photoSonde.setScaledContents(True)
        self.label_photoSonde.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_photoSonde, 1, 0, 1, 1)


        self.verticalLayout_35.addWidget(self.widget_10)

        self.widget_12 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_39 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalSpacer_2 = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_2)

        self.widget_onlineHelp = QWidget(self.widget_12)
        self.widget_onlineHelp.setObjectName(u"widget_onlineHelp")
        self.widget_onlineHelp.setMinimumSize(QSize(160, 90))
        self.widget_onlineHelp.setMaximumSize(QSize(160, 90))
        self.gridLayout_3 = QGridLayout(self.widget_onlineHelp)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_6 = QLabel(self.widget_onlineHelp)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(40, 40))
        self.label_6.setPixmap(QPixmap(u":/Logo/Connexion/dashboard-help.png"))
        self.label_6.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 2, 1)

        self.label_4 = QLabel(self.widget_onlineHelp)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(14)
        self.label_4.setFont(font1)

        self.gridLayout_3.addWidget(self.label_4, 0, 1, 1, 1)

        self.label_5 = QLabel(self.widget_onlineHelp)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 1, 1, 1, 1)

        self.pushButton = QPushButton(self.widget_onlineHelp)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 2, 0, 1, 2)


        self.horizontalLayout_39.addWidget(self.widget_onlineHelp)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer)


        self.verticalLayout_35.addWidget(self.widget_12)

        self.verticalSpacer_8 = QSpacerItem(20, 800, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_8)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_36.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.page_0_Connection)
        self.page_1_DashboardSonde = QWidget()
        self.page_1_DashboardSonde.setObjectName(u"page_1_DashboardSonde")
        self.page_1_DashboardSonde.setMinimumSize(QSize(0, 0))
        self.gridLayout_5 = QGridLayout(self.page_1_DashboardSonde)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.page_1_DashboardSonde)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 463, 718))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_5 = QWidget(self.scrollAreaWidgetContents)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 700))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_7 = QWidget(self.widget_5)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(500, 16777215))
        self.verticalLayout_11 = QVBoxLayout(self.widget_7)
        self.verticalLayout_11.setSpacing(20)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.groupBox_SondeInfo = QGroupBox(self.widget_7)
        self.groupBox_SondeInfo.setObjectName(u"groupBox_SondeInfo")
        sizePolicy3.setHeightForWidth(self.groupBox_SondeInfo.sizePolicy().hasHeightForWidth())
        self.groupBox_SondeInfo.setSizePolicy(sizePolicy3)
        self.groupBox_SondeInfo.setMinimumSize(QSize(0, 0))
        self.groupBox_SondeInfo.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_SondeInfo.setStyleSheet(u"Line{\n"
"/*background-color: rgba(0, 0, 0, 0.2);*/\n"
" /*color: rgba(0, 0, 255, 0.5);*/\n"
"/*border: 0.5px solid green;*/\n"
"/*border-style: inset;*/\n"
"}")
        self.groupBox_SondeInfo.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_SondeInfo)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget_21 = QWidget(self.groupBox_SondeInfo)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 5, 9, 5)
        self.label_2 = QLabel(self.widget_21)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 20))
        self.label_2.setMaximumSize(QSize(20, 20))
        self.label_2.setSizeIncrement(QSize(0, 0))
        self.label_2.setBaseSize(QSize(0, 0))
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/1-Model.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setMargin(0)

        self.horizontalLayout_13.addWidget(self.label_2)

        self.label_txtModel = QLabel(self.widget_21)
        self.label_txtModel.setObjectName(u"label_txtModel")

        self.horizontalLayout_13.addWidget(self.label_txtModel)

        self.label_Model = QLabel(self.widget_21)
        self.label_Model.setObjectName(u"label_Model")
        self.label_Model.setMinimumSize(QSize(0, 20))
        self.label_Model.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_13.addWidget(self.label_Model)

        self.label_80 = QLabel(self.widget_21)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label_80.sizePolicy().hasHeightForWidth())
        self.label_80.setSizePolicy(sizePolicy)
        self.label_80.setMinimumSize(QSize(0, 0))
        self.label_80.setMaximumSize(QSize(20, 20))
        self.label_80.setSizeIncrement(QSize(0, 0))
        self.label_80.setBaseSize(QSize(0, 0))
        self.label_80.setLayoutDirection(Qt.LeftToRight)
        self.label_80.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version - W.svg"))
        self.label_80.setScaledContents(True)
        self.label_80.setAlignment(Qt.AlignCenter)
        self.label_80.setWordWrap(False)
        self.label_80.setMargin(0)

        self.horizontalLayout_13.addWidget(self.label_80)


        self.verticalLayout_17.addWidget(self.widget_21)

        self.widget_22 = QWidget(self.groupBox_SondeInfo)
        self.widget_22.setObjectName(u"widget_22")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 5, -1, 5)
        self.label_28 = QLabel(self.widget_22)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(0, 15))
        self.label_28.setMaximumSize(QSize(18, 18))
        self.label_28.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/2-SN.svg"))
        self.label_28.setScaledContents(True)
        self.label_28.setMargin(0)

        self.horizontalLayout_14.addWidget(self.label_28)

        self.label_txtSN = QLabel(self.widget_22)
        self.label_txtSN.setObjectName(u"label_txtSN")

        self.horizontalLayout_14.addWidget(self.label_txtSN)

        self.label_SerialNo = QLabel(self.widget_22)
        self.label_SerialNo.setObjectName(u"label_SerialNo")
        self.label_SerialNo.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_14.addWidget(self.label_SerialNo)

        self.label_79 = QLabel(self.widget_22)
        self.label_79.setObjectName(u"label_79")
        sizePolicy.setHeightForWidth(self.label_79.sizePolicy().hasHeightForWidth())
        self.label_79.setSizePolicy(sizePolicy)
        self.label_79.setMinimumSize(QSize(0, 0))
        self.label_79.setMaximumSize(QSize(20, 20))
        self.label_79.setSizeIncrement(QSize(0, 0))
        self.label_79.setBaseSize(QSize(0, 0))
        self.label_79.setLayoutDirection(Qt.LeftToRight)
        self.label_79.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version - W.svg"))
        self.label_79.setScaledContents(True)
        self.label_79.setAlignment(Qt.AlignCenter)
        self.label_79.setWordWrap(False)
        self.label_79.setMargin(0)

        self.horizontalLayout_14.addWidget(self.label_79)


        self.verticalLayout_17.addWidget(self.widget_22)

        self.widget_SondeInfoInterface = QWidget(self.groupBox_SondeInfo)
        self.widget_SondeInfoInterface.setObjectName(u"widget_SondeInfoInterface")
        self.horizontalLayout_34 = QHBoxLayout(self.widget_SondeInfoInterface)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(-1, 5, -1, 5)
        self.label_39 = QLabel(self.widget_SondeInfoInterface)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(0, 15))
        self.label_39.setMaximumSize(QSize(18, 18))
        self.label_39.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/Connected-sensor.svg"))
        self.label_39.setScaledContents(True)
        self.label_39.setMargin(0)

        self.horizontalLayout_34.addWidget(self.label_39)

        self.label_txtInterfaceCom = QLabel(self.widget_SondeInfoInterface)
        self.label_txtInterfaceCom.setObjectName(u"label_txtInterfaceCom")

        self.horizontalLayout_34.addWidget(self.label_txtInterfaceCom)

        self.label_InterfaceCom = QLabel(self.widget_SondeInfoInterface)
        self.label_InterfaceCom.setObjectName(u"label_InterfaceCom")
        self.label_InterfaceCom.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_34.addWidget(self.label_InterfaceCom)

        self.label_87 = QLabel(self.widget_SondeInfoInterface)
        self.label_87.setObjectName(u"label_87")
        sizePolicy.setHeightForWidth(self.label_87.sizePolicy().hasHeightForWidth())
        self.label_87.setSizePolicy(sizePolicy)
        self.label_87.setMinimumSize(QSize(0, 0))
        self.label_87.setMaximumSize(QSize(20, 20))
        self.label_87.setSizeIncrement(QSize(0, 0))
        self.label_87.setBaseSize(QSize(0, 0))
        self.label_87.setLayoutDirection(Qt.LeftToRight)
        self.label_87.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version - W.svg"))
        self.label_87.setScaledContents(True)
        self.label_87.setAlignment(Qt.AlignCenter)
        self.label_87.setWordWrap(False)
        self.label_87.setMargin(0)

        self.horizontalLayout_34.addWidget(self.label_87)


        self.verticalLayout_17.addWidget(self.widget_SondeInfoInterface)

        self.widget_23 = QWidget(self.groupBox_SondeInfo)
        self.widget_23.setObjectName(u"widget_23")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 5, -1, 5)
        self.label_29 = QLabel(self.widget_23)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 0))
        self.label_29.setMaximumSize(QSize(20, 20))
        self.label_29.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_29.setScaledContents(True)
        self.label_29.setMargin(0)

        self.horizontalLayout_15.addWidget(self.label_29)

        self.label_txtSWRev = QLabel(self.widget_23)
        self.label_txtSWRev.setObjectName(u"label_txtSWRev")

        self.horizontalLayout_15.addWidget(self.label_txtSWRev)

        self.label_SWRev = QLabel(self.widget_23)
        self.label_SWRev.setObjectName(u"label_SWRev")
        self.label_SWRev.setMinimumSize(QSize(0, 22))
        self.label_SWRev.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_15.addWidget(self.label_SWRev)

        self.label_78 = QLabel(self.widget_23)
        self.label_78.setObjectName(u"label_78")
        sizePolicy.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy)
        self.label_78.setMinimumSize(QSize(0, 0))
        self.label_78.setMaximumSize(QSize(20, 20))
        self.label_78.setSizeIncrement(QSize(0, 0))
        self.label_78.setBaseSize(QSize(0, 0))
        self.label_78.setLayoutDirection(Qt.LeftToRight)
        self.label_78.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version - W.svg"))
        self.label_78.setScaledContents(True)
        self.label_78.setAlignment(Qt.AlignCenter)
        self.label_78.setWordWrap(False)
        self.label_78.setMargin(0)

        self.horizontalLayout_15.addWidget(self.label_78)


        self.verticalLayout_17.addWidget(self.widget_23)

        self.widget_RecordsStored = QWidget(self.groupBox_SondeInfo)
        self.widget_RecordsStored.setObjectName(u"widget_RecordsStored")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_RecordsStored)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 5, -1, 5)
        self.label_30 = QLabel(self.widget_RecordsStored)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 0))
        self.label_30.setMaximumSize(QSize(20, 20))
        self.label_30.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/4-Records-stored.svg"))
        self.label_30.setScaledContents(True)
        self.label_30.setMargin(0)

        self.horizontalLayout_16.addWidget(self.label_30)

        self.label_txtRecordsStored = QLabel(self.widget_RecordsStored)
        self.label_txtRecordsStored.setObjectName(u"label_txtRecordsStored")

        self.horizontalLayout_16.addWidget(self.label_txtRecordsStored)

        self.label_RecordsStored = QLabel(self.widget_RecordsStored)
        self.label_RecordsStored.setObjectName(u"label_RecordsStored")
        self.label_RecordsStored.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_16.addWidget(self.label_RecordsStored)

        self.label_77 = QLabel(self.widget_RecordsStored)
        self.label_77.setObjectName(u"label_77")
        sizePolicy.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy)
        self.label_77.setMinimumSize(QSize(0, 0))
        self.label_77.setMaximumSize(QSize(20, 20))
        self.label_77.setSizeIncrement(QSize(0, 0))
        self.label_77.setBaseSize(QSize(0, 0))
        self.label_77.setLayoutDirection(Qt.LeftToRight)
        self.label_77.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version - W.svg"))
        self.label_77.setScaledContents(True)
        self.label_77.setAlignment(Qt.AlignCenter)
        self.label_77.setWordWrap(False)
        self.label_77.setMargin(0)

        self.horizontalLayout_16.addWidget(self.label_77)


        self.verticalLayout_17.addWidget(self.widget_RecordsStored)

        self.widget_MemoryRemaining = QWidget(self.groupBox_SondeInfo)
        self.widget_MemoryRemaining.setObjectName(u"widget_MemoryRemaining")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_MemoryRemaining)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 5, -1, 5)
        self.label_31 = QLabel(self.widget_MemoryRemaining)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(0, 0))
        self.label_31.setMaximumSize(QSize(20, 20))
        self.label_31.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/5-Memory-card.svg"))
        self.label_31.setScaledContents(True)
        self.label_31.setMargin(0)

        self.horizontalLayout_17.addWidget(self.label_31)

        self.label_txtMemRemaining = QLabel(self.widget_MemoryRemaining)
        self.label_txtMemRemaining.setObjectName(u"label_txtMemRemaining")

        self.horizontalLayout_17.addWidget(self.label_txtMemRemaining)

        self.label_MemoryRemaining = QLabel(self.widget_MemoryRemaining)
        self.label_MemoryRemaining.setObjectName(u"label_MemoryRemaining")
        self.label_MemoryRemaining.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_17.addWidget(self.label_MemoryRemaining)

        self.label_76 = QLabel(self.widget_MemoryRemaining)
        self.label_76.setObjectName(u"label_76")
        sizePolicy.setHeightForWidth(self.label_76.sizePolicy().hasHeightForWidth())
        self.label_76.setSizePolicy(sizePolicy)
        self.label_76.setMinimumSize(QSize(0, 0))
        self.label_76.setMaximumSize(QSize(20, 20))
        self.label_76.setSizeIncrement(QSize(0, 0))
        self.label_76.setBaseSize(QSize(0, 0))
        self.label_76.setLayoutDirection(Qt.LeftToRight)
        self.label_76.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version - W.svg"))
        self.label_76.setScaledContents(True)
        self.label_76.setAlignment(Qt.AlignCenter)
        self.label_76.setWordWrap(False)
        self.label_76.setMargin(0)

        self.horizontalLayout_17.addWidget(self.label_76)


        self.verticalLayout_17.addWidget(self.widget_MemoryRemaining)

        self.widget_BatteryRemaining = QWidget(self.groupBox_SondeInfo)
        self.widget_BatteryRemaining.setObjectName(u"widget_BatteryRemaining")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_BatteryRemaining)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 5, -1, 5)
        self.label_32 = QLabel(self.widget_BatteryRemaining)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(0, 0))
        self.label_32.setMaximumSize(QSize(20, 20))
        self.label_32.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/6-Battery-remaining.svg"))
        self.label_32.setScaledContents(True)
        self.label_32.setMargin(0)

        self.horizontalLayout_18.addWidget(self.label_32)

        self.label_txtBatteryRemaining = QLabel(self.widget_BatteryRemaining)
        self.label_txtBatteryRemaining.setObjectName(u"label_txtBatteryRemaining")

        self.horizontalLayout_18.addWidget(self.label_txtBatteryRemaining)

        self.label_BatteryRemaining = QLabel(self.widget_BatteryRemaining)
        self.label_BatteryRemaining.setObjectName(u"label_BatteryRemaining")
        self.label_BatteryRemaining.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_18.addWidget(self.label_BatteryRemaining)

        self.label_75 = QLabel(self.widget_BatteryRemaining)
        self.label_75.setObjectName(u"label_75")
        sizePolicy.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy)
        self.label_75.setMinimumSize(QSize(20, 20))
        self.label_75.setMaximumSize(QSize(20, 20))
        self.label_75.setSizeIncrement(QSize(0, 0))
        self.label_75.setBaseSize(QSize(0, 0))
        self.label_75.setLayoutDirection(Qt.LeftToRight)
        self.label_75.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/info-button.svg"))
        self.label_75.setScaledContents(True)
        self.label_75.setAlignment(Qt.AlignCenter)
        self.label_75.setWordWrap(False)
        self.label_75.setMargin(0)

        self.horizontalLayout_18.addWidget(self.label_75)


        self.verticalLayout_17.addWidget(self.widget_BatteryRemaining)

        self.widget_BatteryVoltage = QWidget(self.groupBox_SondeInfo)
        self.widget_BatteryVoltage.setObjectName(u"widget_BatteryVoltage")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_BatteryVoltage)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, 5, -1, 5)
        self.label_33 = QLabel(self.widget_BatteryVoltage)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(0, 0))
        self.label_33.setMaximumSize(QSize(20, 20))
        self.label_33.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/7-Battery-voltage.svg"))
        self.label_33.setScaledContents(True)
        self.label_33.setMargin(0)

        self.horizontalLayout_19.addWidget(self.label_33)

        self.label_txtBatteryVoltage = QLabel(self.widget_BatteryVoltage)
        self.label_txtBatteryVoltage.setObjectName(u"label_txtBatteryVoltage")

        self.horizontalLayout_19.addWidget(self.label_txtBatteryVoltage)

        self.label_BatteryVoltage = QLabel(self.widget_BatteryVoltage)
        self.label_BatteryVoltage.setObjectName(u"label_BatteryVoltage")
        self.label_BatteryVoltage.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_19.addWidget(self.label_BatteryVoltage)

        self.label_81 = QLabel(self.widget_BatteryVoltage)
        self.label_81.setObjectName(u"label_81")
        sizePolicy.setHeightForWidth(self.label_81.sizePolicy().hasHeightForWidth())
        self.label_81.setSizePolicy(sizePolicy)
        self.label_81.setMinimumSize(QSize(0, 0))
        self.label_81.setMaximumSize(QSize(20, 20))
        self.label_81.setSizeIncrement(QSize(0, 0))
        self.label_81.setBaseSize(QSize(0, 0))
        self.label_81.setLayoutDirection(Qt.LeftToRight)
        self.label_81.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version - W.svg"))
        self.label_81.setScaledContents(True)
        self.label_81.setAlignment(Qt.AlignCenter)
        self.label_81.setWordWrap(False)
        self.label_81.setMargin(0)

        self.horizontalLayout_19.addWidget(self.label_81)


        self.verticalLayout_17.addWidget(self.widget_BatteryVoltage)


        self.verticalLayout_11.addWidget(self.groupBox_SondeInfo)

        self.groupBox_EstimatedLogLife = QGroupBox(self.widget_7)
        self.groupBox_EstimatedLogLife.setObjectName(u"groupBox_EstimatedLogLife")
        sizePolicy.setHeightForWidth(self.groupBox_EstimatedLogLife.sizePolicy().hasHeightForWidth())
        self.groupBox_EstimatedLogLife.setSizePolicy(sizePolicy)
        self.groupBox_EstimatedLogLife.setMinimumSize(QSize(0, 0))
        self.groupBox_EstimatedLogLife.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_EstimatedLogLife.setStyleSheet(u"Line{\n"
"/*background-color: rgba(0, 0, 0, 0.2);*/\n"
" /*color: rgba(0, 0, 255, 0.5);*/\n"
"/*border: 0.5px solid green;*/\n"
"/*border-style: inset;*/\n"
"}")
        self.groupBox_EstimatedLogLife.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_EstimatedLogLife)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.widget_UntilMemFull = QWidget(self.groupBox_EstimatedLogLife)
        self.widget_UntilMemFull.setObjectName(u"widget_UntilMemFull")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_UntilMemFull)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(-1, 3, -1, 5)
        self.label_69 = QLabel(self.widget_UntilMemFull)
        self.label_69.setObjectName(u"label_69")
        sizePolicy.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy)
        self.label_69.setMinimumSize(QSize(0, 0))
        self.label_69.setMaximumSize(QSize(20, 20))
        self.label_69.setSizeIncrement(QSize(0, 0))
        self.label_69.setBaseSize(QSize(0, 0))
        self.label_69.setLayoutDirection(Qt.LeftToRight)
        self.label_69.setPixmap(QPixmap(u":/Logo/Dashboard/6-Estimated-logging-life/1-Until-memory-full.svg"))
        self.label_69.setScaledContents(True)
        self.label_69.setAlignment(Qt.AlignCenter)
        self.label_69.setWordWrap(False)
        self.label_69.setMargin(0)

        self.horizontalLayout_22.addWidget(self.label_69)

        self.label_txtUntilMemFull = QLabel(self.widget_UntilMemFull)
        self.label_txtUntilMemFull.setObjectName(u"label_txtUntilMemFull")

        self.horizontalLayout_22.addWidget(self.label_txtUntilMemFull)

        self.label_UntilMemFull = QLabel(self.widget_UntilMemFull)
        self.label_UntilMemFull.setObjectName(u"label_UntilMemFull")
        self.label_UntilMemFull.setMinimumSize(QSize(0, 0))
        self.label_UntilMemFull.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_22.addWidget(self.label_UntilMemFull)

        self.label_82 = QLabel(self.widget_UntilMemFull)
        self.label_82.setObjectName(u"label_82")
        sizePolicy.setHeightForWidth(self.label_82.sizePolicy().hasHeightForWidth())
        self.label_82.setSizePolicy(sizePolicy)
        self.label_82.setMinimumSize(QSize(0, 0))
        self.label_82.setMaximumSize(QSize(20, 20))
        self.label_82.setSizeIncrement(QSize(0, 0))
        self.label_82.setBaseSize(QSize(0, 0))
        self.label_82.setLayoutDirection(Qt.LeftToRight)
        self.label_82.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/info-button.svg"))
        self.label_82.setScaledContents(True)
        self.label_82.setAlignment(Qt.AlignCenter)
        self.label_82.setWordWrap(False)
        self.label_82.setMargin(0)

        self.horizontalLayout_22.addWidget(self.label_82)


        self.verticalLayout_20.addWidget(self.widget_UntilMemFull)

        self.widget_UntilBattFull = QWidget(self.groupBox_EstimatedLogLife)
        self.widget_UntilBattFull.setObjectName(u"widget_UntilBattFull")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_UntilBattFull)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(-1, 3, -1, 5)
        self.label_71 = QLabel(self.widget_UntilBattFull)
        self.label_71.setObjectName(u"label_71")
        sizePolicy.setHeightForWidth(self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy)
        self.label_71.setMinimumSize(QSize(0, 0))
        self.label_71.setMaximumSize(QSize(20, 20))
        self.label_71.setSizeIncrement(QSize(0, 0))
        self.label_71.setBaseSize(QSize(0, 0))
        self.label_71.setLayoutDirection(Qt.LeftToRight)
        self.label_71.setPixmap(QPixmap(u":/Logo/Dashboard/6-Estimated-logging-life/2-Until-battery-dead.svg"))
        self.label_71.setScaledContents(True)
        self.label_71.setAlignment(Qt.AlignCenter)
        self.label_71.setWordWrap(False)
        self.label_71.setMargin(0)

        self.horizontalLayout_23.addWidget(self.label_71)

        self.label_txtUntilBattDead = QLabel(self.widget_UntilBattFull)
        self.label_txtUntilBattDead.setObjectName(u"label_txtUntilBattDead")
        self.label_txtUntilBattDead.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_23.addWidget(self.label_txtUntilBattDead)

        self.label_UntilBattDead = QLabel(self.widget_UntilBattFull)
        self.label_UntilBattDead.setObjectName(u"label_UntilBattDead")
        self.label_UntilBattDead.setMinimumSize(QSize(0, 0))
        self.label_UntilBattDead.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_23.addWidget(self.label_UntilBattDead)

        self.label_83 = QLabel(self.widget_UntilBattFull)
        self.label_83.setObjectName(u"label_83")
        sizePolicy.setHeightForWidth(self.label_83.sizePolicy().hasHeightForWidth())
        self.label_83.setSizePolicy(sizePolicy)
        self.label_83.setMinimumSize(QSize(0, 0))
        self.label_83.setMaximumSize(QSize(20, 20))
        self.label_83.setSizeIncrement(QSize(0, 0))
        self.label_83.setBaseSize(QSize(0, 0))
        self.label_83.setLayoutDirection(Qt.LeftToRight)
        self.label_83.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/info-button.svg"))
        self.label_83.setScaledContents(True)
        self.label_83.setAlignment(Qt.AlignCenter)
        self.label_83.setWordWrap(False)
        self.label_83.setMargin(0)

        self.horizontalLayout_23.addWidget(self.label_83)


        self.verticalLayout_20.addWidget(self.widget_UntilBattFull)


        self.verticalLayout_11.addWidget(self.groupBox_EstimatedLogLife)

        self.groupBox_SondeClock = QGroupBox(self.widget_7)
        self.groupBox_SondeClock.setObjectName(u"groupBox_SondeClock")
        sizePolicy.setHeightForWidth(self.groupBox_SondeClock.sizePolicy().hasHeightForWidth())
        self.groupBox_SondeClock.setSizePolicy(sizePolicy)
        self.groupBox_SondeClock.setMinimumSize(QSize(0, 0))
        self.groupBox_SondeClock.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_SondeClock.setStyleSheet(u"Line{\n"
"/*background-color: rgba(0, 0, 0, 0.2);*/\n"
" /*color: rgba(0, 0, 255, 0.5);*/\n"
"/*border: 0.5px solid green;*/\n"
"/*border-style: inset;*/\n"
"}")
        self.groupBox_SondeClock.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayout_19 = QVBoxLayout(self.groupBox_SondeClock)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.widget_SondeDate = QWidget(self.groupBox_SondeClock)
        self.widget_SondeDate.setObjectName(u"widget_SondeDate")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_SondeDate)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 3, -1, 5)
        self.label_54 = QLabel(self.widget_SondeDate)
        self.label_54.setObjectName(u"label_54")
        sizePolicy.setHeightForWidth(self.label_54.sizePolicy().hasHeightForWidth())
        self.label_54.setSizePolicy(sizePolicy)
        self.label_54.setMinimumSize(QSize(0, 20))
        self.label_54.setMaximumSize(QSize(20, 20))
        self.label_54.setSizeIncrement(QSize(0, 0))
        self.label_54.setBaseSize(QSize(0, 0))
        self.label_54.setLayoutDirection(Qt.LeftToRight)
        self.label_54.setPixmap(QPixmap(u":/Logo/Dashboard/2-Sonde-clock/1-Date.svg"))
        self.label_54.setScaledContents(True)
        self.label_54.setAlignment(Qt.AlignCenter)
        self.label_54.setWordWrap(False)
        self.label_54.setMargin(0)

        self.horizontalLayout_20.addWidget(self.label_54)

        self.label_19 = QLabel(self.widget_SondeDate)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_20.addWidget(self.label_19)

        self.label_sondeClockDate = QLabel(self.widget_SondeDate)
        self.label_sondeClockDate.setObjectName(u"label_sondeClockDate")
        self.label_sondeClockDate.setMinimumSize(QSize(0, 0))
        self.label_sondeClockDate.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_20.addWidget(self.label_sondeClockDate)

        self.label_setSondeClockDate = QLabel(self.widget_SondeDate)
        self.label_setSondeClockDate.setObjectName(u"label_setSondeClockDate")
        sizePolicy.setHeightForWidth(self.label_setSondeClockDate.sizePolicy().hasHeightForWidth())
        self.label_setSondeClockDate.setSizePolicy(sizePolicy)
        self.label_setSondeClockDate.setMinimumSize(QSize(0, 0))
        self.label_setSondeClockDate.setMaximumSize(QSize(20, 20))
        self.label_setSondeClockDate.setSizeIncrement(QSize(0, 0))
        self.label_setSondeClockDate.setBaseSize(QSize(0, 0))
        self.label_setSondeClockDate.setLayoutDirection(Qt.LeftToRight)
        self.label_setSondeClockDate.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_setSondeClockDate.setScaledContents(True)
        self.label_setSondeClockDate.setAlignment(Qt.AlignCenter)
        self.label_setSondeClockDate.setWordWrap(False)
        self.label_setSondeClockDate.setMargin(0)

        self.horizontalLayout_20.addWidget(self.label_setSondeClockDate)


        self.verticalLayout_19.addWidget(self.widget_SondeDate)

        self.widget_SondeTime = QWidget(self.groupBox_SondeClock)
        self.widget_SondeTime.setObjectName(u"widget_SondeTime")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_SondeTime)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 5, -1, 5)
        self.label_46 = QLabel(self.widget_SondeTime)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(0, 15))
        self.label_46.setMaximumSize(QSize(20, 20))
        self.label_46.setPixmap(QPixmap(u":/Logo/Dashboard/2-Sonde-clock/2-Time.svg"))
        self.label_46.setScaledContents(True)
        self.label_46.setMargin(0)

        self.horizontalLayout_21.addWidget(self.label_46)

        self.label_48 = QLabel(self.widget_SondeTime)
        self.label_48.setObjectName(u"label_48")

        self.horizontalLayout_21.addWidget(self.label_48)

        self.label_sondeClockTime = QLabel(self.widget_SondeTime)
        self.label_sondeClockTime.setObjectName(u"label_sondeClockTime")
        self.label_sondeClockTime.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_21.addWidget(self.label_sondeClockTime)

        self.label_setSondeClockTime = QLabel(self.widget_SondeTime)
        self.label_setSondeClockTime.setObjectName(u"label_setSondeClockTime")
        sizePolicy.setHeightForWidth(self.label_setSondeClockTime.sizePolicy().hasHeightForWidth())
        self.label_setSondeClockTime.setSizePolicy(sizePolicy)
        self.label_setSondeClockTime.setMinimumSize(QSize(0, 0))
        self.label_setSondeClockTime.setMaximumSize(QSize(20, 20))
        self.label_setSondeClockTime.setSizeIncrement(QSize(0, 0))
        self.label_setSondeClockTime.setBaseSize(QSize(0, 0))
        self.label_setSondeClockTime.setLayoutDirection(Qt.LeftToRight)
        self.label_setSondeClockTime.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_setSondeClockTime.setScaledContents(True)
        self.label_setSondeClockTime.setAlignment(Qt.AlignCenter)
        self.label_setSondeClockTime.setWordWrap(False)
        self.label_setSondeClockTime.setMargin(0)

        self.horizontalLayout_21.addWidget(self.label_setSondeClockTime)


        self.verticalLayout_19.addWidget(self.widget_SondeTime)


        self.verticalLayout_11.addWidget(self.groupBox_SondeClock)

        self.groupBox_SiteIDLocation = QGroupBox(self.widget_7)
        self.groupBox_SiteIDLocation.setObjectName(u"groupBox_SiteIDLocation")
        self.groupBox_SiteIDLocation.setMinimumSize(QSize(0, 0))
        self.groupBox_SiteIDLocation.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_SiteIDLocation)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.widget_SiteID = QWidget(self.groupBox_SiteIDLocation)
        self.widget_SiteID.setObjectName(u"widget_SiteID")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_SiteID)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 3, -1, 5)
        self.label_55 = QLabel(self.widget_SiteID)
        self.label_55.setObjectName(u"label_55")
        sizePolicy.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy)
        self.label_55.setMinimumSize(QSize(20, 20))
        self.label_55.setMaximumSize(QSize(15, 20))
        self.label_55.setSizeIncrement(QSize(0, 0))
        self.label_55.setBaseSize(QSize(0, 0))
        self.label_55.setLayoutDirection(Qt.LeftToRight)
        self.label_55.setPixmap(QPixmap(u":/Logo/Dashboard/3-Site-ID-And-Location/1-Model.svg"))
        self.label_55.setScaledContents(True)
        self.label_55.setAlignment(Qt.AlignCenter)
        self.label_55.setWordWrap(False)
        self.label_55.setMargin(0)

        self.horizontalLayout_8.addWidget(self.label_55)

        self.label_txtSiteID = QLabel(self.widget_SiteID)
        self.label_txtSiteID.setObjectName(u"label_txtSiteID")

        self.horizontalLayout_8.addWidget(self.label_txtSiteID)

        self.label_SiteID = QLabel(self.widget_SiteID)
        self.label_SiteID.setObjectName(u"label_SiteID")
        self.label_SiteID.setMinimumSize(QSize(0, 20))
        self.label_SiteID.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_8.addWidget(self.label_SiteID)

        self.label_setSiteID = QLabel(self.widget_SiteID)
        self.label_setSiteID.setObjectName(u"label_setSiteID")
        sizePolicy.setHeightForWidth(self.label_setSiteID.sizePolicy().hasHeightForWidth())
        self.label_setSiteID.setSizePolicy(sizePolicy)
        self.label_setSiteID.setMinimumSize(QSize(0, 0))
        self.label_setSiteID.setMaximumSize(QSize(20, 20))
        self.label_setSiteID.setSizeIncrement(QSize(0, 0))
        self.label_setSiteID.setBaseSize(QSize(0, 0))
        self.label_setSiteID.setLayoutDirection(Qt.LeftToRight)
        self.label_setSiteID.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_setSiteID.setScaledContents(True)
        self.label_setSiteID.setAlignment(Qt.AlignCenter)
        self.label_setSiteID.setWordWrap(False)
        self.label_setSiteID.setMargin(0)

        self.horizontalLayout_8.addWidget(self.label_setSiteID)


        self.verticalLayout_14.addWidget(self.widget_SiteID)

        self.widget_SiteLatitude = QWidget(self.groupBox_SiteIDLocation)
        self.widget_SiteLatitude.setObjectName(u"widget_SiteLatitude")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_SiteLatitude)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 5, -1, 5)
        self.label_34 = QLabel(self.widget_SiteLatitude)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(0, 0))
        self.label_34.setMaximumSize(QSize(20, 20))
        self.label_34.setPixmap(QPixmap(u":/Logo/Dashboard/3-Site-ID-And-Location/2-Site-lat.svg"))
        self.label_34.setScaledContents(True)
        self.label_34.setMargin(0)

        self.horizontalLayout_9.addWidget(self.label_34)

        self.label_txtSiteLat = QLabel(self.widget_SiteLatitude)
        self.label_txtSiteLat.setObjectName(u"label_txtSiteLat")

        self.horizontalLayout_9.addWidget(self.label_txtSiteLat)

        self.label_SiteLat = QLabel(self.widget_SiteLatitude)
        self.label_SiteLat.setObjectName(u"label_SiteLat")
        self.label_SiteLat.setMinimumSize(QSize(0, 20))
        self.label_SiteLat.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_9.addWidget(self.label_SiteLat)

        self.label_setSiteLatitude = QLabel(self.widget_SiteLatitude)
        self.label_setSiteLatitude.setObjectName(u"label_setSiteLatitude")
        sizePolicy.setHeightForWidth(self.label_setSiteLatitude.sizePolicy().hasHeightForWidth())
        self.label_setSiteLatitude.setSizePolicy(sizePolicy)
        self.label_setSiteLatitude.setMinimumSize(QSize(0, 0))
        self.label_setSiteLatitude.setMaximumSize(QSize(20, 20))
        self.label_setSiteLatitude.setSizeIncrement(QSize(0, 0))
        self.label_setSiteLatitude.setBaseSize(QSize(0, 0))
        self.label_setSiteLatitude.setLayoutDirection(Qt.LeftToRight)
        self.label_setSiteLatitude.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_setSiteLatitude.setScaledContents(True)
        self.label_setSiteLatitude.setAlignment(Qt.AlignCenter)
        self.label_setSiteLatitude.setWordWrap(False)
        self.label_setSiteLatitude.setMargin(0)

        self.horizontalLayout_9.addWidget(self.label_setSiteLatitude)


        self.verticalLayout_14.addWidget(self.widget_SiteLatitude)

        self.widget_SiteLongitude = QWidget(self.groupBox_SiteIDLocation)
        self.widget_SiteLongitude.setObjectName(u"widget_SiteLongitude")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_SiteLongitude)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 5, -1, 5)
        self.label_56 = QLabel(self.widget_SiteLongitude)
        self.label_56.setObjectName(u"label_56")
        sizePolicy.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy)
        self.label_56.setMinimumSize(QSize(20, 20))
        self.label_56.setMaximumSize(QSize(15, 20))
        self.label_56.setSizeIncrement(QSize(0, 0))
        self.label_56.setBaseSize(QSize(0, 0))
        self.label_56.setLayoutDirection(Qt.LeftToRight)
        self.label_56.setPixmap(QPixmap(u":/Logo/Dashboard/3-Site-ID-And-Location/3-Site-long.svg"))
        self.label_56.setScaledContents(True)
        self.label_56.setAlignment(Qt.AlignCenter)
        self.label_56.setWordWrap(False)
        self.label_56.setMargin(0)

        self.horizontalLayout_10.addWidget(self.label_56)

        self.label_txtSiteLong = QLabel(self.widget_SiteLongitude)
        self.label_txtSiteLong.setObjectName(u"label_txtSiteLong")

        self.horizontalLayout_10.addWidget(self.label_txtSiteLong)

        self.label_SiteLong = QLabel(self.widget_SiteLongitude)
        self.label_SiteLong.setObjectName(u"label_SiteLong")
        self.label_SiteLong.setMinimumSize(QSize(0, 20))
        self.label_SiteLong.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_10.addWidget(self.label_SiteLong)

        self.label_setSiteLong = QLabel(self.widget_SiteLongitude)
        self.label_setSiteLong.setObjectName(u"label_setSiteLong")
        sizePolicy.setHeightForWidth(self.label_setSiteLong.sizePolicy().hasHeightForWidth())
        self.label_setSiteLong.setSizePolicy(sizePolicy)
        self.label_setSiteLong.setMinimumSize(QSize(0, 0))
        self.label_setSiteLong.setMaximumSize(QSize(20, 20))
        self.label_setSiteLong.setSizeIncrement(QSize(0, 0))
        self.label_setSiteLong.setBaseSize(QSize(0, 0))
        self.label_setSiteLong.setLayoutDirection(Qt.LeftToRight)
        self.label_setSiteLong.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_setSiteLong.setScaledContents(True)
        self.label_setSiteLong.setAlignment(Qt.AlignCenter)
        self.label_setSiteLong.setWordWrap(False)
        self.label_setSiteLong.setMargin(0)

        self.horizontalLayout_10.addWidget(self.label_setSiteLong)


        self.verticalLayout_14.addWidget(self.widget_SiteLongitude)


        self.verticalLayout_11.addWidget(self.groupBox_SiteIDLocation)

        self.pushButton_TestDashboard = QPushButton(self.widget_7)
        self.pushButton_TestDashboard.setObjectName(u"pushButton_TestDashboard")

        self.verticalLayout_11.addWidget(self.pushButton_TestDashboard)

        self.verticalSpacer_15 = QSpacerItem(20, 800, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_15)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addWidget(self.widget_7)

        self.widget_3 = QWidget(self.widget_5)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(500, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.widget_3)
        self.verticalLayout_8.setSpacing(20)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox_DashboardSensors = QGroupBox(self.widget_3)
        self.groupBox_DashboardSensors.setObjectName(u"groupBox_DashboardSensors")
        sizePolicy.setHeightForWidth(self.groupBox_DashboardSensors.sizePolicy().hasHeightForWidth())
        self.groupBox_DashboardSensors.setSizePolicy(sizePolicy)
        self.groupBox_DashboardSensors.setMinimumSize(QSize(0, 0))
        self.groupBox_DashboardSensors.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_DashboardSensors.setStyleSheet(u"Line{\n"
"/*background-color: rgba(0, 0, 0, 0.2);*/\n"
" /*color: rgba(0, 0, 255, 0.5);*/\n"
"/*border: 0.5px solid green;*/\n"
"/*border-style: inset;*/\n"
"}")
        self.groupBox_DashboardSensors.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_DashboardSensors)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_8.addWidget(self.groupBox_DashboardSensors)

        self.groupBox_SetupLogRate = QGroupBox(self.widget_3)
        self.groupBox_SetupLogRate.setObjectName(u"groupBox_SetupLogRate")
        sizePolicy.setHeightForWidth(self.groupBox_SetupLogRate.sizePolicy().hasHeightForWidth())
        self.groupBox_SetupLogRate.setSizePolicy(sizePolicy)
        self.groupBox_SetupLogRate.setMinimumSize(QSize(0, 0))
        self.groupBox_SetupLogRate.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_SetupLogRate.setStyleSheet(u"Line{\n"
"/*background-color: rgba(0, 0, 0, 0.2);*/\n"
" /*color: rgba(0, 0, 255, 0.5);*/\n"
"/*border: 0.5px solid green;*/\n"
"/*border-style: inset;*/\n"
"}")
        self.groupBox_SetupLogRate.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_SetupLogRate)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.widget_LogDataEvery = QWidget(self.groupBox_SetupLogRate)
        self.widget_LogDataEvery.setObjectName(u"widget_LogDataEvery")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_LogDataEvery)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 3, -1, 5)
        self.label_60 = QLabel(self.widget_LogDataEvery)
        self.label_60.setObjectName(u"label_60")
        sizePolicy.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy)
        self.label_60.setMinimumSize(QSize(0, 0))
        self.label_60.setMaximumSize(QSize(20, 20))
        self.label_60.setSizeIncrement(QSize(0, 0))
        self.label_60.setBaseSize(QSize(0, 0))
        self.label_60.setLayoutDirection(Qt.LeftToRight)
        self.label_60.setPixmap(QPixmap(u":/Logo/Dashboard/5-Setup-logging-rate/3-Log-data-every.svg"))
        self.label_60.setScaledContents(True)
        self.label_60.setAlignment(Qt.AlignCenter)
        self.label_60.setWordWrap(False)
        self.label_60.setMargin(0)

        self.horizontalLayout_11.addWidget(self.label_60)

        self.label_txtLogDataEvery = QLabel(self.widget_LogDataEvery)
        self.label_txtLogDataEvery.setObjectName(u"label_txtLogDataEvery")

        self.horizontalLayout_11.addWidget(self.label_txtLogDataEvery)

        self.label_LogDataEvery = QLabel(self.widget_LogDataEvery)
        self.label_LogDataEvery.setObjectName(u"label_LogDataEvery")
        self.label_LogDataEvery.setMinimumSize(QSize(0, 0))
        self.label_LogDataEvery.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_11.addWidget(self.label_LogDataEvery)

        self.label_setLogDataEvery = QLabel(self.widget_LogDataEvery)
        self.label_setLogDataEvery.setObjectName(u"label_setLogDataEvery")
        sizePolicy.setHeightForWidth(self.label_setLogDataEvery.sizePolicy().hasHeightForWidth())
        self.label_setLogDataEvery.setSizePolicy(sizePolicy)
        self.label_setLogDataEvery.setMinimumSize(QSize(0, 0))
        self.label_setLogDataEvery.setMaximumSize(QSize(20, 20))
        self.label_setLogDataEvery.setSizeIncrement(QSize(0, 0))
        self.label_setLogDataEvery.setBaseSize(QSize(0, 0))
        self.label_setLogDataEvery.setLayoutDirection(Qt.LeftToRight)
        self.label_setLogDataEvery.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_setLogDataEvery.setScaledContents(True)
        self.label_setLogDataEvery.setAlignment(Qt.AlignCenter)
        self.label_setLogDataEvery.setWordWrap(False)
        self.label_setLogDataEvery.setMargin(0)

        self.horizontalLayout_11.addWidget(self.label_setLogDataEvery)


        self.verticalLayout_16.addWidget(self.widget_LogDataEvery)

        self.widget_CleanEvery = QWidget(self.groupBox_SetupLogRate)
        self.widget_CleanEvery.setObjectName(u"widget_CleanEvery")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_CleanEvery)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 3, -1, 5)
        self.label_61 = QLabel(self.widget_CleanEvery)
        self.label_61.setObjectName(u"label_61")
        sizePolicy.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy)
        self.label_61.setMinimumSize(QSize(0, 0))
        self.label_61.setMaximumSize(QSize(20, 20))
        self.label_61.setSizeIncrement(QSize(0, 0))
        self.label_61.setBaseSize(QSize(0, 0))
        self.label_61.setLayoutDirection(Qt.LeftToRight)
        self.label_61.setPixmap(QPixmap(u":/Logo/Dashboard/5-Setup-logging-rate/2-Clean-every.svg"))
        self.label_61.setScaledContents(True)
        self.label_61.setAlignment(Qt.AlignCenter)
        self.label_61.setWordWrap(False)
        self.label_61.setMargin(0)

        self.horizontalLayout_12.addWidget(self.label_61)

        self.label_txtCleanEvery = QLabel(self.widget_CleanEvery)
        self.label_txtCleanEvery.setObjectName(u"label_txtCleanEvery")
        self.label_txtCleanEvery.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_12.addWidget(self.label_txtCleanEvery)

        self.label_CleanEvery = QLabel(self.widget_CleanEvery)
        self.label_CleanEvery.setObjectName(u"label_CleanEvery")
        self.label_CleanEvery.setMinimumSize(QSize(0, 0))
        self.label_CleanEvery.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_12.addWidget(self.label_CleanEvery)

        self.label_setCleanEvery = QLabel(self.widget_CleanEvery)
        self.label_setCleanEvery.setObjectName(u"label_setCleanEvery")
        sizePolicy.setHeightForWidth(self.label_setCleanEvery.sizePolicy().hasHeightForWidth())
        self.label_setCleanEvery.setSizePolicy(sizePolicy)
        self.label_setCleanEvery.setMinimumSize(QSize(0, 0))
        self.label_setCleanEvery.setMaximumSize(QSize(20, 20))
        self.label_setCleanEvery.setSizeIncrement(QSize(0, 0))
        self.label_setCleanEvery.setBaseSize(QSize(0, 0))
        self.label_setCleanEvery.setLayoutDirection(Qt.LeftToRight)
        self.label_setCleanEvery.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_setCleanEvery.setScaledContents(True)
        self.label_setCleanEvery.setAlignment(Qt.AlignCenter)
        self.label_setCleanEvery.setWordWrap(False)
        self.label_setCleanEvery.setMargin(0)

        self.horizontalLayout_12.addWidget(self.label_setCleanEvery)


        self.verticalLayout_16.addWidget(self.widget_CleanEvery)


        self.verticalLayout_8.addWidget(self.groupBox_SetupLogRate)

        self.groupBox_EventLogging = QGroupBox(self.widget_3)
        self.groupBox_EventLogging.setObjectName(u"groupBox_EventLogging")
        sizePolicy.setHeightForWidth(self.groupBox_EventLogging.sizePolicy().hasHeightForWidth())
        self.groupBox_EventLogging.setSizePolicy(sizePolicy)
        self.groupBox_EventLogging.setMinimumSize(QSize(0, 0))
        self.groupBox_EventLogging.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_EventLogging.setStyleSheet(u"Line{\n"
"/*background-color: rgba(0, 0, 0, 0.2);*/\n"
" /*color: rgba(0, 0, 255, 0.5);*/\n"
"/*border: 0.5px solid green;*/\n"
"/*border-style: inset;*/\n"
"}")
        self.groupBox_EventLogging.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayout_24 = QVBoxLayout(self.groupBox_EventLogging)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.widget_EventLogState = QWidget(self.groupBox_EventLogging)
        self.widget_EventLogState.setObjectName(u"widget_EventLogState")
        self.horizontalLayout_32 = QHBoxLayout(self.widget_EventLogState)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(-1, 3, -1, 5)
        self.label_94 = QLabel(self.widget_EventLogState)
        self.label_94.setObjectName(u"label_94")
        sizePolicy.setHeightForWidth(self.label_94.sizePolicy().hasHeightForWidth())
        self.label_94.setSizePolicy(sizePolicy)
        self.label_94.setMinimumSize(QSize(0, 0))
        self.label_94.setMaximumSize(QSize(20, 20))
        self.label_94.setSizeIncrement(QSize(0, 0))
        self.label_94.setBaseSize(QSize(0, 0))
        self.label_94.setLayoutDirection(Qt.LeftToRight)
        self.label_94.setPixmap(QPixmap(u":/Logo/Dashboard/7-Event-logging/1-State.svg"))
        self.label_94.setScaledContents(True)
        self.label_94.setAlignment(Qt.AlignCenter)
        self.label_94.setWordWrap(False)
        self.label_94.setMargin(0)

        self.horizontalLayout_32.addWidget(self.label_94)

        self.label_txtEventLogState = QLabel(self.widget_EventLogState)
        self.label_txtEventLogState.setObjectName(u"label_txtEventLogState")

        self.horizontalLayout_32.addWidget(self.label_txtEventLogState)

        self.label_EventLogState = QLabel(self.widget_EventLogState)
        self.label_EventLogState.setObjectName(u"label_EventLogState")
        self.label_EventLogState.setMinimumSize(QSize(0, 0))
        self.label_EventLogState.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_32.addWidget(self.label_EventLogState)

        self.label_setEventLogState = QLabel(self.widget_EventLogState)
        self.label_setEventLogState.setObjectName(u"label_setEventLogState")
        sizePolicy.setHeightForWidth(self.label_setEventLogState.sizePolicy().hasHeightForWidth())
        self.label_setEventLogState.setSizePolicy(sizePolicy)
        self.label_setEventLogState.setMinimumSize(QSize(0, 0))
        self.label_setEventLogState.setMaximumSize(QSize(20, 20))
        self.label_setEventLogState.setSizeIncrement(QSize(0, 0))
        self.label_setEventLogState.setBaseSize(QSize(0, 0))
        self.label_setEventLogState.setLayoutDirection(Qt.LeftToRight)
        self.label_setEventLogState.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_setEventLogState.setScaledContents(True)
        self.label_setEventLogState.setAlignment(Qt.AlignCenter)
        self.label_setEventLogState.setWordWrap(False)
        self.label_setEventLogState.setMargin(0)

        self.horizontalLayout_32.addWidget(self.label_setEventLogState)


        self.verticalLayout_24.addWidget(self.widget_EventLogState)

        self.widget_EventLogCheck = QWidget(self.groupBox_EventLogging)
        self.widget_EventLogCheck.setObjectName(u"widget_EventLogCheck")
        self.horizontalLayout_31 = QHBoxLayout(self.widget_EventLogCheck)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(-1, 3, -1, 5)
        self.label_logoEventLogCheck = QLabel(self.widget_EventLogCheck)
        self.label_logoEventLogCheck.setObjectName(u"label_logoEventLogCheck")
        sizePolicy.setHeightForWidth(self.label_logoEventLogCheck.sizePolicy().hasHeightForWidth())
        self.label_logoEventLogCheck.setSizePolicy(sizePolicy)
        self.label_logoEventLogCheck.setMinimumSize(QSize(0, 0))
        self.label_logoEventLogCheck.setMaximumSize(QSize(20, 20))
        self.label_logoEventLogCheck.setSizeIncrement(QSize(0, 0))
        self.label_logoEventLogCheck.setBaseSize(QSize(0, 0))
        self.label_logoEventLogCheck.setLayoutDirection(Qt.LeftToRight)
        self.label_logoEventLogCheck.setPixmap(QPixmap(u":/Logo/Dashboard/7-Event-logging/2-Check.svg"))
        self.label_logoEventLogCheck.setScaledContents(True)
        self.label_logoEventLogCheck.setAlignment(Qt.AlignCenter)
        self.label_logoEventLogCheck.setWordWrap(False)
        self.label_logoEventLogCheck.setMargin(0)

        self.horizontalLayout_31.addWidget(self.label_logoEventLogCheck)

        self.label_txtEventLogCheck = QLabel(self.widget_EventLogCheck)
        self.label_txtEventLogCheck.setObjectName(u"label_txtEventLogCheck")
        self.label_txtEventLogCheck.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_31.addWidget(self.label_txtEventLogCheck)

        self.label_EventLogCheck = QLabel(self.widget_EventLogCheck)
        self.label_EventLogCheck.setObjectName(u"label_EventLogCheck")
        self.label_EventLogCheck.setMinimumSize(QSize(0, 0))
        self.label_EventLogCheck.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_31.addWidget(self.label_EventLogCheck)

        self.label_setEventLogCheck = QLabel(self.widget_EventLogCheck)
        self.label_setEventLogCheck.setObjectName(u"label_setEventLogCheck")
        sizePolicy.setHeightForWidth(self.label_setEventLogCheck.sizePolicy().hasHeightForWidth())
        self.label_setEventLogCheck.setSizePolicy(sizePolicy)
        self.label_setEventLogCheck.setMinimumSize(QSize(0, 0))
        self.label_setEventLogCheck.setMaximumSize(QSize(20, 20))
        self.label_setEventLogCheck.setSizeIncrement(QSize(0, 0))
        self.label_setEventLogCheck.setBaseSize(QSize(0, 0))
        self.label_setEventLogCheck.setLayoutDirection(Qt.LeftToRight)
        self.label_setEventLogCheck.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_setEventLogCheck.setScaledContents(True)
        self.label_setEventLogCheck.setAlignment(Qt.AlignCenter)
        self.label_setEventLogCheck.setWordWrap(False)
        self.label_setEventLogCheck.setMargin(0)

        self.horizontalLayout_31.addWidget(self.label_setEventLogCheck)


        self.verticalLayout_24.addWidget(self.widget_EventLogCheck)

        self.widget_EventLogEvery = QWidget(self.groupBox_EventLogging)
        self.widget_EventLogEvery.setObjectName(u"widget_EventLogEvery")
        self.horizontalLayout_28 = QHBoxLayout(self.widget_EventLogEvery)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(-1, 3, -1, 5)
        self.label_logoEventLogEvery = QLabel(self.widget_EventLogEvery)
        self.label_logoEventLogEvery.setObjectName(u"label_logoEventLogEvery")
        sizePolicy.setHeightForWidth(self.label_logoEventLogEvery.sizePolicy().hasHeightForWidth())
        self.label_logoEventLogEvery.setSizePolicy(sizePolicy)
        self.label_logoEventLogEvery.setMinimumSize(QSize(0, 0))
        self.label_logoEventLogEvery.setMaximumSize(QSize(20, 20))
        self.label_logoEventLogEvery.setSizeIncrement(QSize(0, 0))
        self.label_logoEventLogEvery.setBaseSize(QSize(0, 0))
        self.label_logoEventLogEvery.setLayoutDirection(Qt.LeftToRight)
        self.label_logoEventLogEvery.setPixmap(QPixmap(u":/Logo/Dashboard/7-Event-logging/3-Every.svg"))
        self.label_logoEventLogEvery.setScaledContents(True)
        self.label_logoEventLogEvery.setAlignment(Qt.AlignCenter)
        self.label_logoEventLogEvery.setWordWrap(False)
        self.label_logoEventLogEvery.setMargin(0)

        self.horizontalLayout_28.addWidget(self.label_logoEventLogEvery)

        self.label_txtEventLogEvery = QLabel(self.widget_EventLogEvery)
        self.label_txtEventLogEvery.setObjectName(u"label_txtEventLogEvery")

        self.horizontalLayout_28.addWidget(self.label_txtEventLogEvery)

        self.label_EventLogEvery = QLabel(self.widget_EventLogEvery)
        self.label_EventLogEvery.setObjectName(u"label_EventLogEvery")
        self.label_EventLogEvery.setMinimumSize(QSize(0, 0))
        self.label_EventLogEvery.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_28.addWidget(self.label_EventLogEvery)

        self.label_setEventLogEvery = QLabel(self.widget_EventLogEvery)
        self.label_setEventLogEvery.setObjectName(u"label_setEventLogEvery")
        sizePolicy.setHeightForWidth(self.label_setEventLogEvery.sizePolicy().hasHeightForWidth())
        self.label_setEventLogEvery.setSizePolicy(sizePolicy)
        self.label_setEventLogEvery.setMinimumSize(QSize(0, 0))
        self.label_setEventLogEvery.setMaximumSize(QSize(20, 20))
        self.label_setEventLogEvery.setSizeIncrement(QSize(0, 0))
        self.label_setEventLogEvery.setBaseSize(QSize(0, 0))
        self.label_setEventLogEvery.setLayoutDirection(Qt.LeftToRight)
        self.label_setEventLogEvery.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_setEventLogEvery.setScaledContents(True)
        self.label_setEventLogEvery.setAlignment(Qt.AlignCenter)
        self.label_setEventLogEvery.setWordWrap(False)
        self.label_setEventLogEvery.setMargin(0)

        self.horizontalLayout_28.addWidget(self.label_setEventLogEvery)


        self.verticalLayout_24.addWidget(self.widget_EventLogEvery)

        self.widget_EventLogThreshold = QWidget(self.groupBox_EventLogging)
        self.widget_EventLogThreshold.setObjectName(u"widget_EventLogThreshold")
        self.horizontalLayout_29 = QHBoxLayout(self.widget_EventLogThreshold)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(-1, 3, -1, 5)
        self.label_logoEventLogThreshold = QLabel(self.widget_EventLogThreshold)
        self.label_logoEventLogThreshold.setObjectName(u"label_logoEventLogThreshold")
        sizePolicy.setHeightForWidth(self.label_logoEventLogThreshold.sizePolicy().hasHeightForWidth())
        self.label_logoEventLogThreshold.setSizePolicy(sizePolicy)
        self.label_logoEventLogThreshold.setMinimumSize(QSize(0, 0))
        self.label_logoEventLogThreshold.setMaximumSize(QSize(20, 20))
        self.label_logoEventLogThreshold.setSizeIncrement(QSize(0, 0))
        self.label_logoEventLogThreshold.setBaseSize(QSize(0, 0))
        self.label_logoEventLogThreshold.setLayoutDirection(Qt.LeftToRight)
        self.label_logoEventLogThreshold.setPixmap(QPixmap(u":/Logo/Dashboard/7-Event-logging/4-Log-data-if.svg"))
        self.label_logoEventLogThreshold.setScaledContents(True)
        self.label_logoEventLogThreshold.setAlignment(Qt.AlignCenter)
        self.label_logoEventLogThreshold.setWordWrap(False)
        self.label_logoEventLogThreshold.setMargin(0)

        self.horizontalLayout_29.addWidget(self.label_logoEventLogThreshold)

        self.label_txtEventLogThreshold = QLabel(self.widget_EventLogThreshold)
        self.label_txtEventLogThreshold.setObjectName(u"label_txtEventLogThreshold")
        self.label_txtEventLogThreshold.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_29.addWidget(self.label_txtEventLogThreshold)

        self.label_EventLogThreshold = QLabel(self.widget_EventLogThreshold)
        self.label_EventLogThreshold.setObjectName(u"label_EventLogThreshold")
        self.label_EventLogThreshold.setMinimumSize(QSize(0, 0))
        self.label_EventLogThreshold.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_29.addWidget(self.label_EventLogThreshold)

        self.label_setEventLogThreshold = QLabel(self.widget_EventLogThreshold)
        self.label_setEventLogThreshold.setObjectName(u"label_setEventLogThreshold")
        sizePolicy.setHeightForWidth(self.label_setEventLogThreshold.sizePolicy().hasHeightForWidth())
        self.label_setEventLogThreshold.setSizePolicy(sizePolicy)
        self.label_setEventLogThreshold.setMinimumSize(QSize(0, 0))
        self.label_setEventLogThreshold.setMaximumSize(QSize(20, 20))
        self.label_setEventLogThreshold.setSizeIncrement(QSize(0, 0))
        self.label_setEventLogThreshold.setBaseSize(QSize(0, 0))
        self.label_setEventLogThreshold.setLayoutDirection(Qt.LeftToRight)
        self.label_setEventLogThreshold.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_setEventLogThreshold.setScaledContents(True)
        self.label_setEventLogThreshold.setAlignment(Qt.AlignCenter)
        self.label_setEventLogThreshold.setWordWrap(False)
        self.label_setEventLogThreshold.setMargin(0)

        self.horizontalLayout_29.addWidget(self.label_setEventLogThreshold)


        self.verticalLayout_24.addWidget(self.widget_EventLogThreshold)


        self.verticalLayout_8.addWidget(self.groupBox_EventLogging)

        self.groupBox_Averaging = QGroupBox(self.widget_3)
        self.groupBox_Averaging.setObjectName(u"groupBox_Averaging")
        sizePolicy.setHeightForWidth(self.groupBox_Averaging.sizePolicy().hasHeightForWidth())
        self.groupBox_Averaging.setSizePolicy(sizePolicy)
        self.groupBox_Averaging.setMinimumSize(QSize(0, 0))
        self.groupBox_Averaging.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_Averaging.setStyleSheet(u"Line{\n"
"/*background-color: rgba(0, 0, 0, 0.2);*/\n"
" /*color: rgba(0, 0, 255, 0.5);*/\n"
"/*border: 0.5px solid green;*/\n"
"/*border-style: inset;*/\n"
"}")
        self.groupBox_Averaging.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayout_40 = QVBoxLayout(self.groupBox_Averaging)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.widget_OpticalAveraging = QWidget(self.groupBox_Averaging)
        self.widget_OpticalAveraging.setObjectName(u"widget_OpticalAveraging")
        self.horizontalLayout_79 = QHBoxLayout(self.widget_OpticalAveraging)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(-1, 3, -1, 5)
        self.label_115 = QLabel(self.widget_OpticalAveraging)
        self.label_115.setObjectName(u"label_115")
        sizePolicy.setHeightForWidth(self.label_115.sizePolicy().hasHeightForWidth())
        self.label_115.setSizePolicy(sizePolicy)
        self.label_115.setMinimumSize(QSize(0, 0))
        self.label_115.setMaximumSize(QSize(20, 20))
        self.label_115.setSizeIncrement(QSize(0, 0))
        self.label_115.setBaseSize(QSize(0, 0))
        self.label_115.setLayoutDirection(Qt.LeftToRight)
        self.label_115.setPixmap(QPixmap(u":/Logo/Dashboard/5-Setup-logging-rate/3-Log-data-every.svg"))
        self.label_115.setScaledContents(True)
        self.label_115.setAlignment(Qt.AlignCenter)
        self.label_115.setWordWrap(False)
        self.label_115.setMargin(0)

        self.horizontalLayout_79.addWidget(self.label_115)

        self.label_txtAveraging = QLabel(self.widget_OpticalAveraging)
        self.label_txtAveraging.setObjectName(u"label_txtAveraging")

        self.horizontalLayout_79.addWidget(self.label_txtAveraging)

        self.label_AveragingValue = QLabel(self.widget_OpticalAveraging)
        self.label_AveragingValue.setObjectName(u"label_AveragingValue")
        self.label_AveragingValue.setMinimumSize(QSize(0, 0))
        self.label_AveragingValue.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_79.addWidget(self.label_AveragingValue)

        self.label_116 = QLabel(self.widget_OpticalAveraging)
        self.label_116.setObjectName(u"label_116")
        sizePolicy.setHeightForWidth(self.label_116.sizePolicy().hasHeightForWidth())
        self.label_116.setSizePolicy(sizePolicy)
        self.label_116.setMinimumSize(QSize(0, 0))
        self.label_116.setMaximumSize(QSize(20, 20))
        self.label_116.setSizeIncrement(QSize(0, 0))
        self.label_116.setBaseSize(QSize(0, 0))
        self.label_116.setLayoutDirection(Qt.LeftToRight)
        self.label_116.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_116.setScaledContents(True)
        self.label_116.setAlignment(Qt.AlignCenter)
        self.label_116.setWordWrap(False)
        self.label_116.setMargin(0)

        self.horizontalLayout_79.addWidget(self.label_116)


        self.verticalLayout_40.addWidget(self.widget_OpticalAveraging)


        self.verticalLayout_8.addWidget(self.groupBox_Averaging)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addWidget(self.widget_3)

        self.horizontalSpacer_3 = QSpacerItem(0, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_2.setStretch(0, 300)
        self.horizontalLayout_2.setStretch(1, 300)

        self.verticalLayout_7.addWidget(self.widget_5)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_5.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_1_DashboardSonde)
        self.page_2_Liveview = QWidget()
        self.page_2_Liveview.setObjectName(u"page_2_Liveview")
        self.verticalLayout_9 = QVBoxLayout(self.page_2_Liveview)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget_46 = QWidget(self.page_2_Liveview)
        self.widget_46.setObjectName(u"widget_46")
        self.widget_46.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_77 = QHBoxLayout(self.widget_46)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(-1, 0, -1, 0)
        self.label_101 = QLabel(self.widget_46)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setMaximumSize(QSize(15, 15))
        self.label_101.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/info-button.svg"))
        self.label_101.setScaledContents(True)

        self.horizontalLayout_77.addWidget(self.label_101)

        self.label_49 = QLabel(self.widget_46)
        self.label_49.setObjectName(u"label_49")

        self.horizontalLayout_77.addWidget(self.label_49)


        self.verticalLayout_9.addWidget(self.widget_46)

        self.widget_11 = QWidget(self.page_2_Liveview)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(0, 250))
        self.widget_11.setMaximumSize(QSize(16777215, 300))
        self.widget_11.setAcceptDrops(False)
        self.gridLayout_9 = QGridLayout(self.widget_11)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.widget_14 = QWidget(self.widget_11)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(110, 100))
        self.widget_14.setMaximumSize(QSize(110, 100))
        self.widget_14.setStyleSheet(u"")
        self.verticalLayout_22 = QVBoxLayout(self.widget_14)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, -1)
        self.widget_8 = QWidget(self.widget_14)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(9, 5, 9, 5)
        self.label_3 = QLabel(self.widget_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(20, 20))
        self.label_3.setMaximumSize(QSize(20, 20))
        self.label_3.setPixmap(QPixmap(u":/Logo/Sensor/SVG_blanc/S06_DO.svg"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_24.addWidget(self.label_3)

        self.label = QLabel(self.widget_8)
        self.label.setObjectName(u"label")

        self.horizontalLayout_24.addWidget(self.label)


        self.verticalLayout_22.addWidget(self.widget_8)

        self.label_70 = QLabel(self.widget_14)
        self.label_70.setObjectName(u"label_70")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.label_70.setFont(font2)
        self.label_70.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_70)

        self.label_72 = QLabel(self.widget_14)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_72)

        self.verticalLayout_22.setStretch(1, 4)

        self.gridLayout_9.addWidget(self.widget_14, 0, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.widget_11)

        self.widget_15 = QWidget(self.page_2_Liveview)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_41 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.widget_CalculatedResult = QWidget(self.widget_15)
        self.widget_CalculatedResult.setObjectName(u"widget_CalculatedResult")
        self.widget_CalculatedResult.setMinimumSize(QSize(200, 0))
        self.widget_CalculatedResult.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_12 = QVBoxLayout(self.widget_CalculatedResult)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.groupBox_CalculatedResult = QGroupBox(self.widget_CalculatedResult)
        self.groupBox_CalculatedResult.setObjectName(u"groupBox_CalculatedResult")
        self.groupBox_CalculatedResult.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayout_23 = QVBoxLayout(self.groupBox_CalculatedResult)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.widget_SondeDate_2 = QWidget(self.groupBox_CalculatedResult)
        self.widget_SondeDate_2.setObjectName(u"widget_SondeDate_2")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_SondeDate_2)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(-1, 3, -1, 5)
        self.label_57 = QLabel(self.widget_SondeDate_2)
        self.label_57.setObjectName(u"label_57")
        sizePolicy.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy)
        self.label_57.setMinimumSize(QSize(0, 20))
        self.label_57.setMaximumSize(QSize(20, 20))
        self.label_57.setSizeIncrement(QSize(0, 0))
        self.label_57.setBaseSize(QSize(0, 0))
        self.label_57.setLayoutDirection(Qt.LeftToRight)
        self.label_57.setPixmap(QPixmap(u":/Logo/Dashboard/2-Sonde-clock/1-Date.svg"))
        self.label_57.setScaledContents(True)
        self.label_57.setAlignment(Qt.AlignCenter)
        self.label_57.setWordWrap(False)
        self.label_57.setMargin(0)

        self.horizontalLayout_27.addWidget(self.label_57)

        self.label_20 = QLabel(self.widget_SondeDate_2)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_27.addWidget(self.label_20)

        self.label_LV_salinity = QLabel(self.widget_SondeDate_2)
        self.label_LV_salinity.setObjectName(u"label_LV_salinity")
        self.label_LV_salinity.setMinimumSize(QSize(0, 0))
        self.label_LV_salinity.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_27.addWidget(self.label_LV_salinity)


        self.verticalLayout_23.addWidget(self.widget_SondeDate_2)

        self.widget_SondeDate_3 = QWidget(self.groupBox_CalculatedResult)
        self.widget_SondeDate_3.setObjectName(u"widget_SondeDate_3")
        self.horizontalLayout_30 = QHBoxLayout(self.widget_SondeDate_3)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(-1, 3, -1, 5)
        self.label_85 = QLabel(self.widget_SondeDate_3)
        self.label_85.setObjectName(u"label_85")
        sizePolicy.setHeightForWidth(self.label_85.sizePolicy().hasHeightForWidth())
        self.label_85.setSizePolicy(sizePolicy)
        self.label_85.setMinimumSize(QSize(0, 20))
        self.label_85.setMaximumSize(QSize(20, 20))
        self.label_85.setSizeIncrement(QSize(0, 0))
        self.label_85.setBaseSize(QSize(0, 0))
        self.label_85.setLayoutDirection(Qt.LeftToRight)
        self.label_85.setPixmap(QPixmap(u":/Logo/Dashboard/2-Sonde-clock/1-Date.svg"))
        self.label_85.setScaledContents(True)
        self.label_85.setAlignment(Qt.AlignCenter)
        self.label_85.setWordWrap(False)
        self.label_85.setMargin(0)

        self.horizontalLayout_30.addWidget(self.label_85)

        self.label_21 = QLabel(self.widget_SondeDate_3)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_30.addWidget(self.label_21)

        self.label_LV_SSG = QLabel(self.widget_SondeDate_3)
        self.label_LV_SSG.setObjectName(u"label_LV_SSG")
        self.label_LV_SSG.setMinimumSize(QSize(0, 0))
        self.label_LV_SSG.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_30.addWidget(self.label_LV_SSG)


        self.verticalLayout_23.addWidget(self.widget_SondeDate_3)

        self.widget_SondeDate_4 = QWidget(self.groupBox_CalculatedResult)
        self.widget_SondeDate_4.setObjectName(u"widget_SondeDate_4")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_SondeDate_4)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(-1, 3, -1, 5)
        self.label_88 = QLabel(self.widget_SondeDate_4)
        self.label_88.setObjectName(u"label_88")
        sizePolicy.setHeightForWidth(self.label_88.sizePolicy().hasHeightForWidth())
        self.label_88.setSizePolicy(sizePolicy)
        self.label_88.setMinimumSize(QSize(0, 20))
        self.label_88.setMaximumSize(QSize(20, 20))
        self.label_88.setSizeIncrement(QSize(0, 0))
        self.label_88.setBaseSize(QSize(0, 0))
        self.label_88.setLayoutDirection(Qt.LeftToRight)
        self.label_88.setPixmap(QPixmap(u":/Logo/Dashboard/2-Sonde-clock/1-Date.svg"))
        self.label_88.setScaledContents(True)
        self.label_88.setAlignment(Qt.AlignCenter)
        self.label_88.setWordWrap(False)
        self.label_88.setMargin(0)

        self.horizontalLayout_33.addWidget(self.label_88)

        self.label_35 = QLabel(self.widget_SondeDate_4)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_33.addWidget(self.label_35)

        self.label_LV_TDS = QLabel(self.widget_SondeDate_4)
        self.label_LV_TDS.setObjectName(u"label_LV_TDS")
        self.label_LV_TDS.setMinimumSize(QSize(0, 0))
        self.label_LV_TDS.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_33.addWidget(self.label_LV_TDS)


        self.verticalLayout_23.addWidget(self.widget_SondeDate_4)

        self.widget_LVCalculatedAmmonia = QWidget(self.groupBox_CalculatedResult)
        self.widget_LVCalculatedAmmonia.setObjectName(u"widget_LVCalculatedAmmonia")
        self.horizontalLayout_42 = QHBoxLayout(self.widget_LVCalculatedAmmonia)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(-1, 3, -1, 5)
        self.label_96 = QLabel(self.widget_LVCalculatedAmmonia)
        self.label_96.setObjectName(u"label_96")
        sizePolicy.setHeightForWidth(self.label_96.sizePolicy().hasHeightForWidth())
        self.label_96.setSizePolicy(sizePolicy)
        self.label_96.setMinimumSize(QSize(0, 20))
        self.label_96.setMaximumSize(QSize(20, 20))
        self.label_96.setSizeIncrement(QSize(0, 0))
        self.label_96.setBaseSize(QSize(0, 0))
        self.label_96.setLayoutDirection(Qt.LeftToRight)
        self.label_96.setPixmap(QPixmap(u":/Logo/Dashboard/2-Sonde-clock/1-Date.svg"))
        self.label_96.setScaledContents(True)
        self.label_96.setAlignment(Qt.AlignCenter)
        self.label_96.setWordWrap(False)
        self.label_96.setMargin(0)

        self.horizontalLayout_42.addWidget(self.label_96)

        self.label_40 = QLabel(self.widget_LVCalculatedAmmonia)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_42.addWidget(self.label_40)

        self.label_LV_Ammonia = QLabel(self.widget_LVCalculatedAmmonia)
        self.label_LV_Ammonia.setObjectName(u"label_LV_Ammonia")
        self.label_LV_Ammonia.setMinimumSize(QSize(0, 0))
        self.label_LV_Ammonia.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_42.addWidget(self.label_LV_Ammonia)


        self.verticalLayout_23.addWidget(self.widget_LVCalculatedAmmonia)


        self.verticalLayout_12.addWidget(self.groupBox_CalculatedResult)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_4)


        self.horizontalLayout_41.addWidget(self.widget_CalculatedResult)

        self.widget_18 = QWidget(self.widget_15)
        self.widget_18.setObjectName(u"widget_18")

        self.horizontalLayout_41.addWidget(self.widget_18)


        self.verticalLayout_9.addWidget(self.widget_15)

        self.stackedWidget.addWidget(self.page_2_Liveview)
        self.page_3_DataSonde = QWidget()
        self.page_3_DataSonde.setObjectName(u"page_3_DataSonde")
        self.gridLayout = QGridLayout(self.page_3_DataSonde)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_dataDateFilter = QWidget(self.page_3_DataSonde)
        self.widget_dataDateFilter.setObjectName(u"widget_dataDateFilter")
        self.widget_dataDateFilter.setMinimumSize(QSize(150, 0))
        self.widget_dataDateFilter.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_27 = QVBoxLayout(self.widget_dataDateFilter)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_dataStartDatetime = QLabel(self.widget_dataDateFilter)
        self.label_dataStartDatetime.setObjectName(u"label_dataStartDatetime")

        self.verticalLayout_27.addWidget(self.label_dataStartDatetime)

        self.dateTimeEdit_dataStart = QDateTimeEdit(self.widget_dataDateFilter)
        self.dateTimeEdit_dataStart.setObjectName(u"dateTimeEdit_dataStart")
        self.dateTimeEdit_dataStart.setMinimumSize(QSize(0, 28))

        self.verticalLayout_27.addWidget(self.dateTimeEdit_dataStart)

        self.label_dataStopDatetime = QLabel(self.widget_dataDateFilter)
        self.label_dataStopDatetime.setObjectName(u"label_dataStopDatetime")

        self.verticalLayout_27.addWidget(self.label_dataStopDatetime)

        self.dateTimeEdit_dataEnd = QDateTimeEdit(self.widget_dataDateFilter)
        self.dateTimeEdit_dataEnd.setObjectName(u"dateTimeEdit_dataEnd")
        self.dateTimeEdit_dataEnd.setMinimumSize(QSize(0, 28))

        self.verticalLayout_27.addWidget(self.dateTimeEdit_dataEnd)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_5)

        self.pushButton_dataSelectAll = QPushButton(self.widget_dataDateFilter)
        self.pushButton_dataSelectAll.setObjectName(u"pushButton_dataSelectAll")

        self.verticalLayout_27.addWidget(self.pushButton_dataSelectAll)

        self.pushButton_dataDeselectAll = QPushButton(self.widget_dataDateFilter)
        self.pushButton_dataDeselectAll.setObjectName(u"pushButton_dataDeselectAll")

        self.verticalLayout_27.addWidget(self.pushButton_dataDeselectAll)


        self.gridLayout.addWidget(self.widget_dataDateFilter, 1, 0, 1, 1)

        self.widget_dataChanneCheckbox = QWidget(self.page_3_DataSonde)
        self.widget_dataChanneCheckbox.setObjectName(u"widget_dataChanneCheckbox")
        self.horizontalLayout_47 = QHBoxLayout(self.widget_dataChanneCheckbox)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.groupBox_Environment = QGroupBox(self.widget_dataChanneCheckbox)
        self.groupBox_Environment.setObjectName(u"groupBox_Environment")
        self.groupBox_Environment.setMinimumSize(QSize(110, 0))
        self.groupBox_Environment.setMaximumSize(QSize(130, 16777215))

        self.horizontalLayout_47.addWidget(self.groupBox_Environment)

        self.widget_38 = QWidget(self.widget_dataChanneCheckbox)
        self.widget_38.setObjectName(u"widget_38")
        self.widget_38.setMinimumSize(QSize(130, 0))
        self.verticalLayout_29 = QVBoxLayout(self.widget_38)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.groupBox_pHORPDOEC = QGroupBox(self.widget_38)
        self.groupBox_pHORPDOEC.setObjectName(u"groupBox_pHORPDOEC")
        self.groupBox_pHORPDOEC.setMinimumSize(QSize(110, 0))
        self.groupBox_pHORPDOEC.setMaximumSize(QSize(130, 16777215))

        self.verticalLayout_29.addWidget(self.groupBox_pHORPDOEC)

        self.verticalLayout_29.setStretch(0, 15)

        self.horizontalLayout_47.addWidget(self.widget_38)

        self.widget_35 = QWidget(self.widget_dataChanneCheckbox)
        self.widget_35.setObjectName(u"widget_35")
        self.widget_35.setMinimumSize(QSize(130, 0))
        self.verticalLayout_28 = QVBoxLayout(self.widget_35)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.groupBox_calculated = QGroupBox(self.widget_35)
        self.groupBox_calculated.setObjectName(u"groupBox_calculated")
        self.groupBox_calculated.setMinimumSize(QSize(110, 0))
        self.groupBox_calculated.setMaximumSize(QSize(130, 16777215))

        self.verticalLayout_28.addWidget(self.groupBox_calculated)

        self.verticalLayout_28.setStretch(0, 15)

        self.horizontalLayout_47.addWidget(self.widget_35)

        self.groupBox_Aux = QGroupBox(self.widget_dataChanneCheckbox)
        self.groupBox_Aux.setObjectName(u"groupBox_Aux")
        self.groupBox_Aux.setMinimumSize(QSize(0, 0))
        self.groupBox_Aux.setMaximumSize(QSize(130, 16777215))

        self.horizontalLayout_47.addWidget(self.groupBox_Aux)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_4)


        self.gridLayout.addWidget(self.widget_dataChanneCheckbox, 1, 1, 1, 1)

        self.stackedWidget_DataTabChart = QStackedWidget(self.page_3_DataSonde)
        self.stackedWidget_DataTabChart.setObjectName(u"stackedWidget_DataTabChart")
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.gridLayout_4 = QGridLayout(self.page_8)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.treeWidget = QTreeWidget(self.page_8)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(15, u"16");
        __qtreewidgetitem.setText(14, u"15");
        __qtreewidgetitem.setText(13, u"14");
        __qtreewidgetitem.setText(12, u"13");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        QTreeWidgetItem(self.treeWidget)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setMaximumSize(QSize(16777215, 16777215))
        self.treeWidget.setFont(font)
        self.treeWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.treeWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.treeWidget.setAutoExpandDelay(1)
        self.treeWidget.setIndentation(0)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setExpandsOnDoubleClick(True)
        self.treeWidget.setColumnCount(16)
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setMinimumSectionSize(30)
        self.treeWidget.header().setDefaultSectionSize(70)
        self.treeWidget.header().setProperty(u"showSortIndicator", True)
        self.treeWidget.header().setStretchLastSection(False)

        self.gridLayout_4.addWidget(self.treeWidget, 0, 0, 1, 1)

        self.stackedWidget_DataTabChart.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.gridLayout_6 = QGridLayout(self.page_9)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.widget_DataChart = QWidget(self.page_9)
        self.widget_DataChart.setObjectName(u"widget_DataChart")

        self.gridLayout_6.addWidget(self.widget_DataChart, 0, 0, 1, 1)

        self.stackedWidget_DataTabChart.addWidget(self.page_9)

        self.gridLayout.addWidget(self.stackedWidget_DataTabChart, 2, 0, 1, 2)

        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 15)
        self.stackedWidget.addWidget(self.page_3_DataSonde)
        self.page_4_Calibration = QWidget()
        self.page_4_Calibration.setObjectName(u"page_4_Calibration")
        self.gridLayout_2 = QGridLayout(self.page_4_Calibration)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget_calibrationMain = QStackedWidget(self.page_4_Calibration)
        self.stackedWidget_calibrationMain.setObjectName(u"stackedWidget_calibrationMain")
        self.calibration_main = QWidget()
        self.calibration_main.setObjectName(u"calibration_main")
        self.verticalLayout_18 = QVBoxLayout(self.calibration_main)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_CalibNav__ = QScrollArea(self.calibration_main)
        self.widget_CalibNav__.setObjectName(u"widget_CalibNav__")
        self.widget_CalibNav__.setMinimumSize(QSize(0, 130))
        self.widget_CalibNav__.setWidgetResizable(True)
        self.widget_CalibNav = QWidget()
        self.widget_CalibNav.setObjectName(u"widget_CalibNav")
        self.widget_CalibNav.setGeometry(QRect(0, 0, 844, 130))
        self.widget_CalibNav.setMinimumSize(QSize(0, 0))
        self.widget_CalibNav.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_35 = QHBoxLayout(self.widget_CalibNav)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.widget_calibNavPH_2 = QWidget(self.widget_CalibNav)
        self.widget_calibNavPH_2.setObjectName(u"widget_calibNavPH_2")
        self.widget_calibNavPH_2.setMinimumSize(QSize(90, 90))
        self.widget_calibNavPH_2.setMaximumSize(QSize(90, 90))
        self.widget_calibNavPH_2.setStyleSheet(u"")
        self.gridLayout_16 = QGridLayout(self.widget_calibNavPH_2)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.widget_calibNavPH_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_22, 1, 0, 1, 1)

        self.label_26 = QLabel(self.widget_calibNavPH_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(40, 40))
        self.label_26.setMaximumSize(QSize(40, 40))
        self.label_26.setPixmap(QPixmap(u":/Logo/Sensor/SVG_blanc/F05_pH.svg"))
        self.label_26.setScaledContents(True)
        self.label_26.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_26, 0, 0, 1, 1)


        self.horizontalLayout_35.addWidget(self.widget_calibNavPH_2)

        self.widget_calibNavDOEC_2 = QWidget(self.widget_CalibNav)
        self.widget_calibNavDOEC_2.setObjectName(u"widget_calibNavDOEC_2")
        self.widget_calibNavDOEC_2.setMinimumSize(QSize(90, 90))
        self.widget_calibNavDOEC_2.setMaximumSize(QSize(90, 90))
        self.widget_calibNavDOEC_2.setStyleSheet(u"")
        self.gridLayout_18 = QGridLayout(self.widget_calibNavDOEC_2)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setVerticalSpacing(20)
        self.label_42 = QLabel(self.widget_calibNavDOEC_2)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(50, 50))
        self.label_42.setMaximumSize(QSize(30, 30))
        self.label_42.setLayoutDirection(Qt.LeftToRight)
        self.label_42.setPixmap(QPixmap(u":/Logo/Sensor/SVG_blanc/F03_DO.svg"))
        self.label_42.setScaledContents(True)
        self.label_42.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.label_42, 0, 0, 1, 1)

        self.label_45 = QLabel(self.widget_calibNavDOEC_2)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.label_45, 1, 0, 1, 1)


        self.horizontalLayout_35.addWidget(self.widget_calibNavDOEC_2)

        self.widget_6 = QWidget(self.widget_CalibNav)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(90, 90))
        self.verticalLayout_10 = QVBoxLayout(self.widget_6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_calibNavPH = QWidget(self.widget_6)
        self.widget_calibNavPH.setObjectName(u"widget_calibNavPH")
        self.widget_calibNavPH.setMinimumSize(QSize(80, 80))
        self.widget_calibNavPH.setMaximumSize(QSize(80, 80))
        self.widget_calibNavPH.setStyleSheet(u"")
        self.gridLayout_14 = QGridLayout(self.widget_calibNavPH)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_calibNavPH)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_10 = QLabel(self.widget_calibNavPH)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(40, 40))
        self.label_10.setMaximumSize(QSize(40, 40))
        self.label_10.setPixmap(QPixmap(u":/Logo/Sensor/SVG_blanc/F05_pH.svg"))
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.label_10, 0, 0, 1, 1)


        self.verticalLayout_10.addWidget(self.widget_calibNavPH)


        self.horizontalLayout_35.addWidget(self.widget_6)

        self.widget_9 = QWidget(self.widget_CalibNav)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(90, 90))
        self.widget_9.setMaximumSize(QSize(90, 90))
        self.verticalLayout_37 = QVBoxLayout(self.widget_9)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.widget_calibNavORP = QWidget(self.widget_9)
        self.widget_calibNavORP.setObjectName(u"widget_calibNavORP")
        self.widget_calibNavORP.setMinimumSize(QSize(90, 90))
        self.widget_calibNavORP.setMaximumSize(QSize(90, 90))
        self.widget_calibNavORP.setStyleSheet(u"")
        self.gridLayout_19 = QGridLayout(self.widget_calibNavORP)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setVerticalSpacing(20)
        self.label_47 = QLabel(self.widget_calibNavORP)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(50, 50))
        self.label_47.setMaximumSize(QSize(30, 30))
        self.label_47.setLayoutDirection(Qt.LeftToRight)
        self.label_47.setPixmap(QPixmap(u":/Logo/Sensor/SVG_blanc/F07_ORP.svg"))
        self.label_47.setScaledContents(True)
        self.label_47.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.label_47, 0, 0, 1, 1)

        self.label_53 = QLabel(self.widget_calibNavORP)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.label_53, 1, 0, 1, 1)


        self.verticalLayout_37.addWidget(self.widget_calibNavORP)


        self.horizontalLayout_35.addWidget(self.widget_9)

        self.widget_calibNavORP_2 = QWidget(self.widget_CalibNav)
        self.widget_calibNavORP_2.setObjectName(u"widget_calibNavORP_2")
        self.widget_calibNavORP_2.setMinimumSize(QSize(90, 90))
        self.widget_calibNavORP_2.setMaximumSize(QSize(90, 90))
        self.widget_calibNavORP_2.setStyleSheet(u"")
        self.gridLayout_17 = QGridLayout(self.widget_calibNavORP_2)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setVerticalSpacing(20)
        self.label_37 = QLabel(self.widget_calibNavORP_2)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(50, 50))
        self.label_37.setMaximumSize(QSize(30, 30))
        self.label_37.setLayoutDirection(Qt.LeftToRight)
        self.label_37.setPixmap(QPixmap(u":/Logo/Sensor/SVG_blanc/F07_ORP.svg"))
        self.label_37.setScaledContents(True)
        self.label_37.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.label_37, 0, 0, 1, 1)

        self.label_41 = QLabel(self.widget_calibNavORP_2)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.label_41, 1, 0, 1, 1)


        self.horizontalLayout_35.addWidget(self.widget_calibNavORP_2)

        self.widget_calibNavDOEC = QWidget(self.widget_CalibNav)
        self.widget_calibNavDOEC.setObjectName(u"widget_calibNavDOEC")
        self.widget_calibNavDOEC.setMinimumSize(QSize(90, 90))
        self.widget_calibNavDOEC.setMaximumSize(QSize(90, 90))
        self.widget_calibNavDOEC.setStyleSheet(u"")
        self.gridLayout_12 = QGridLayout(self.widget_calibNavDOEC)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setVerticalSpacing(20)
        self.label_15 = QLabel(self.widget_calibNavDOEC)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(50, 50))
        self.label_15.setMaximumSize(QSize(30, 30))
        self.label_15.setLayoutDirection(Qt.LeftToRight)
        self.label_15.setPixmap(QPixmap(u":/Logo/Sensor/SVG_blanc/F03_DO.svg"))
        self.label_15.setScaledContents(True)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_14 = QLabel(self.widget_calibNavDOEC)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_14, 1, 0, 1, 1)


        self.horizontalLayout_35.addWidget(self.widget_calibNavDOEC)

        self.widget_CalibNav__.setWidget(self.widget_CalibNav)

        self.verticalLayout_18.addWidget(self.widget_CalibNav__)

        self.scrollArea_3 = QScrollArea(self.calibration_main)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setMinimumSize(QSize(0, 0))
        self.scrollArea_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 827, 832))
        self.horizontalLayout_43 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.widget_17 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_44 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_44.setSpacing(12)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.widget_19 = QWidget(self.widget_17)
        self.widget_19.setObjectName(u"widget_19")
        self.verticalLayout_15 = QVBoxLayout(self.widget_19)
        self.verticalLayout_15.setSpacing(9)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.groupBox_AUX_PT1 = QGroupBox(self.widget_19)
        self.groupBox_AUX_PT1.setObjectName(u"groupBox_AUX_PT1")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.groupBox_AUX_PT1.sizePolicy().hasHeightForWidth())
        self.groupBox_AUX_PT1.setSizePolicy(sizePolicy5)
        self.groupBox_AUX_PT1.setMinimumSize(QSize(0, 0))
        self.groupBox_AUX_PT1.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_AUX_PT1.setStyleSheet(u"Line{\n"
"/*background-color: rgba(0, 0, 0, 0.2);*/\n"
" /*color: rgba(0, 0, 255, 0.5);*/\n"
"/*border: 0.5px solid green;*/\n"
"/*border-style: inset;*/\n"
"}")
        self.groupBox_AUX_PT1.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayout_31 = QVBoxLayout(self.groupBox_AUX_PT1)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.widget_AuxPt1Date = QWidget(self.groupBox_AUX_PT1)
        self.widget_AuxPt1Date.setObjectName(u"widget_AuxPt1Date")
        self.widget_AuxPt1Date.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_63 = QHBoxLayout(self.widget_AuxPt1Date)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(-1, 5, 9, 5)
        self.label_74 = QLabel(self.widget_AuxPt1Date)
        self.label_74.setObjectName(u"label_74")
        sizePolicy.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy)
        self.label_74.setMinimumSize(QSize(0, 20))
        self.label_74.setMaximumSize(QSize(20, 20))
        self.label_74.setSizeIncrement(QSize(0, 0))
        self.label_74.setBaseSize(QSize(0, 0))
        self.label_74.setLayoutDirection(Qt.LeftToRight)
        self.label_74.setPixmap(QPixmap(u":/Logo/Calibration/Date.svg"))
        self.label_74.setScaledContents(True)
        self.label_74.setAlignment(Qt.AlignCenter)
        self.label_74.setWordWrap(False)
        self.label_74.setMargin(0)

        self.horizontalLayout_63.addWidget(self.label_74)

        self.label_txtModel_15 = QLabel(self.widget_AuxPt1Date)
        self.label_txtModel_15.setObjectName(u"label_txtModel_15")

        self.horizontalLayout_63.addWidget(self.label_txtModel_15)

        self.label_AuxPt1Date = QLabel(self.widget_AuxPt1Date)
        self.label_AuxPt1Date.setObjectName(u"label_AuxPt1Date")
        self.label_AuxPt1Date.setMinimumSize(QSize(0, 20))
        self.label_AuxPt1Date.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_63.addWidget(self.label_AuxPt1Date)

        self.label_111 = QLabel(self.widget_AuxPt1Date)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label_111.sizePolicy().hasHeightForWidth())
        self.label_111.setSizePolicy(sizePolicy)
        self.label_111.setMinimumSize(QSize(0, 0))
        self.label_111.setMaximumSize(QSize(20, 20))
        self.label_111.setSizeIncrement(QSize(0, 0))
        self.label_111.setBaseSize(QSize(0, 0))
        self.label_111.setLayoutDirection(Qt.LeftToRight)
        self.label_111.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version - W.svg"))
        self.label_111.setScaledContents(True)
        self.label_111.setAlignment(Qt.AlignCenter)
        self.label_111.setWordWrap(False)
        self.label_111.setMargin(0)

        self.horizontalLayout_63.addWidget(self.label_111)


        self.verticalLayout_31.addWidget(self.widget_AuxPt1Date)

        self.widget_AuxPt1Value = QWidget(self.groupBox_AUX_PT1)
        self.widget_AuxPt1Value.setObjectName(u"widget_AuxPt1Value")
        self.widget_AuxPt1Value.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_64 = QHBoxLayout(self.widget_AuxPt1Value)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(-1, 5, -1, 5)
        self.label_112 = QLabel(self.widget_AuxPt1Value)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setMinimumSize(QSize(0, 15))
        self.label_112.setMaximumSize(QSize(18, 18))
        self.label_112.setPixmap(QPixmap(u":/Logo/Calibration/Value.svg"))
        self.label_112.setScaledContents(True)
        self.label_112.setMargin(0)

        self.horizontalLayout_64.addWidget(self.label_112)

        self.label_txtSN_13 = QLabel(self.widget_AuxPt1Value)
        self.label_txtSN_13.setObjectName(u"label_txtSN_13")

        self.horizontalLayout_64.addWidget(self.label_txtSN_13)

        self.label_AuxPt1Value = QLabel(self.widget_AuxPt1Value)
        self.label_AuxPt1Value.setObjectName(u"label_AuxPt1Value")
        self.label_AuxPt1Value.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_64.addWidget(self.label_AuxPt1Value)

        self.label_113 = QLabel(self.widget_AuxPt1Value)
        self.label_113.setObjectName(u"label_113")
        sizePolicy.setHeightForWidth(self.label_113.sizePolicy().hasHeightForWidth())
        self.label_113.setSizePolicy(sizePolicy)
        self.label_113.setMinimumSize(QSize(0, 0))
        self.label_113.setMaximumSize(QSize(20, 20))
        self.label_113.setSizeIncrement(QSize(0, 0))
        self.label_113.setBaseSize(QSize(0, 0))
        self.label_113.setLayoutDirection(Qt.LeftToRight)
        self.label_113.setPixmap(QPixmap(u":/Logo/Calibration/calibrationGo.svg"))
        self.label_113.setScaledContents(True)
        self.label_113.setAlignment(Qt.AlignCenter)
        self.label_113.setWordWrap(False)
        self.label_113.setMargin(0)

        self.horizontalLayout_64.addWidget(self.label_113)


        self.verticalLayout_31.addWidget(self.widget_AuxPt1Value)


        self.verticalLayout_15.addWidget(self.groupBox_AUX_PT1)

        self.groupBox_AUX_PT2 = QGroupBox(self.widget_19)
        self.groupBox_AUX_PT2.setObjectName(u"groupBox_AUX_PT2")
        sizePolicy5.setHeightForWidth(self.groupBox_AUX_PT2.sizePolicy().hasHeightForWidth())
        self.groupBox_AUX_PT2.setSizePolicy(sizePolicy5)
        self.groupBox_AUX_PT2.setMinimumSize(QSize(0, 0))
        self.groupBox_AUX_PT2.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_AUX_PT2.setStyleSheet(u"Line{\n"
"/*background-color: rgba(0, 0, 0, 0.2);*/\n"
" /*color: rgba(0, 0, 255, 0.5);*/\n"
"/*border: 0.5px solid green;*/\n"
"/*border-style: inset;*/\n"
"}")
        self.groupBox_AUX_PT2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayout_33 = QVBoxLayout(self.groupBox_AUX_PT2)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.widget_33 = QWidget(self.groupBox_AUX_PT2)
        self.widget_33.setObjectName(u"widget_33")
        self.horizontalLayout_60 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(-1, 5, 9, 5)
        self.label_58 = QLabel(self.widget_33)
        self.label_58.setObjectName(u"label_58")
        sizePolicy.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy)
        self.label_58.setMinimumSize(QSize(0, 20))
        self.label_58.setMaximumSize(QSize(20, 20))
        self.label_58.setSizeIncrement(QSize(0, 0))
        self.label_58.setBaseSize(QSize(0, 0))
        self.label_58.setLayoutDirection(Qt.LeftToRight)
        self.label_58.setPixmap(QPixmap(u":/Logo/Calibration/Date.svg"))
        self.label_58.setScaledContents(True)
        self.label_58.setAlignment(Qt.AlignCenter)
        self.label_58.setWordWrap(False)
        self.label_58.setMargin(0)

        self.horizontalLayout_60.addWidget(self.label_58)

        self.label_txtModel_16 = QLabel(self.widget_33)
        self.label_txtModel_16.setObjectName(u"label_txtModel_16")

        self.horizontalLayout_60.addWidget(self.label_txtModel_16)

        self.label_AuxPt2Date = QLabel(self.widget_33)
        self.label_AuxPt2Date.setObjectName(u"label_AuxPt2Date")
        self.label_AuxPt2Date.setMinimumSize(QSize(0, 20))
        self.label_AuxPt2Date.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_60.addWidget(self.label_AuxPt2Date)

        self.label_108 = QLabel(self.widget_33)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label_108.sizePolicy().hasHeightForWidth())
        self.label_108.setSizePolicy(sizePolicy)
        self.label_108.setMinimumSize(QSize(0, 0))
        self.label_108.setMaximumSize(QSize(20, 20))
        self.label_108.setSizeIncrement(QSize(0, 0))
        self.label_108.setBaseSize(QSize(0, 0))
        self.label_108.setLayoutDirection(Qt.LeftToRight)
        self.label_108.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version - W.svg"))
        self.label_108.setScaledContents(True)
        self.label_108.setAlignment(Qt.AlignCenter)
        self.label_108.setWordWrap(False)
        self.label_108.setMargin(0)

        self.horizontalLayout_60.addWidget(self.label_108)


        self.verticalLayout_33.addWidget(self.widget_33)

        self.widget_AuxPt2Value = QWidget(self.groupBox_AUX_PT2)
        self.widget_AuxPt2Value.setObjectName(u"widget_AuxPt2Value")
        self.horizontalLayout_61 = QHBoxLayout(self.widget_AuxPt2Value)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(-1, 5, -1, 5)
        self.label_59 = QLabel(self.widget_AuxPt2Value)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(0, 15))
        self.label_59.setMaximumSize(QSize(18, 18))
        self.label_59.setPixmap(QPixmap(u":/Logo/Calibration/Value.svg"))
        self.label_59.setScaledContents(True)
        self.label_59.setMargin(0)

        self.horizontalLayout_61.addWidget(self.label_59)

        self.label_txtSN_10 = QLabel(self.widget_AuxPt2Value)
        self.label_txtSN_10.setObjectName(u"label_txtSN_10")

        self.horizontalLayout_61.addWidget(self.label_txtSN_10)

        self.label_AuxPt2Value = QLabel(self.widget_AuxPt2Value)
        self.label_AuxPt2Value.setObjectName(u"label_AuxPt2Value")
        self.label_AuxPt2Value.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_61.addWidget(self.label_AuxPt2Value)

        self.label_109 = QLabel(self.widget_AuxPt2Value)
        self.label_109.setObjectName(u"label_109")
        sizePolicy.setHeightForWidth(self.label_109.sizePolicy().hasHeightForWidth())
        self.label_109.setSizePolicy(sizePolicy)
        self.label_109.setMinimumSize(QSize(0, 0))
        self.label_109.setMaximumSize(QSize(20, 20))
        self.label_109.setSizeIncrement(QSize(0, 0))
        self.label_109.setBaseSize(QSize(0, 0))
        self.label_109.setLayoutDirection(Qt.LeftToRight)
        self.label_109.setPixmap(QPixmap(u":/Logo/Calibration/calibrationGo.svg"))
        self.label_109.setScaledContents(True)
        self.label_109.setAlignment(Qt.AlignCenter)
        self.label_109.setWordWrap(False)
        self.label_109.setMargin(0)

        self.horizontalLayout_61.addWidget(self.label_109)


        self.verticalLayout_33.addWidget(self.widget_AuxPt2Value)


        self.verticalLayout_15.addWidget(self.groupBox_AUX_PT2)

        self.groupBox_AUX_PT3 = QGroupBox(self.widget_19)
        self.groupBox_AUX_PT3.setObjectName(u"groupBox_AUX_PT3")
        sizePolicy5.setHeightForWidth(self.groupBox_AUX_PT3.sizePolicy().hasHeightForWidth())
        self.groupBox_AUX_PT3.setSizePolicy(sizePolicy5)
        self.groupBox_AUX_PT3.setMinimumSize(QSize(0, 0))
        self.groupBox_AUX_PT3.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_AUX_PT3.setStyleSheet(u"Line{\n"
"/*background-color: rgba(0, 0, 0, 0.2);*/\n"
" /*color: rgba(0, 0, 255, 0.5);*/\n"
"/*border: 0.5px solid green;*/\n"
"/*border-style: inset;*/\n"
"}")
        self.groupBox_AUX_PT3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayout_32 = QVBoxLayout(self.groupBox_AUX_PT3)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.widget_36 = QWidget(self.groupBox_AUX_PT3)
        self.widget_36.setObjectName(u"widget_36")
        self.horizontalLayout_56 = QHBoxLayout(self.widget_36)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(-1, 5, 9, 5)
        self.label_51 = QLabel(self.widget_36)
        self.label_51.setObjectName(u"label_51")
        sizePolicy.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy)
        self.label_51.setMinimumSize(QSize(0, 20))
        self.label_51.setMaximumSize(QSize(20, 20))
        self.label_51.setSizeIncrement(QSize(0, 0))
        self.label_51.setBaseSize(QSize(0, 0))
        self.label_51.setLayoutDirection(Qt.LeftToRight)
        self.label_51.setPixmap(QPixmap(u":/Logo/Calibration/Date.svg"))
        self.label_51.setScaledContents(True)
        self.label_51.setAlignment(Qt.AlignCenter)
        self.label_51.setWordWrap(False)
        self.label_51.setMargin(0)

        self.horizontalLayout_56.addWidget(self.label_51)

        self.label_txtModel_13 = QLabel(self.widget_36)
        self.label_txtModel_13.setObjectName(u"label_txtModel_13")

        self.horizontalLayout_56.addWidget(self.label_txtModel_13)

        self.label_AuxPt3Date = QLabel(self.widget_36)
        self.label_AuxPt3Date.setObjectName(u"label_AuxPt3Date")
        self.label_AuxPt3Date.setMinimumSize(QSize(0, 20))
        self.label_AuxPt3Date.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_56.addWidget(self.label_AuxPt3Date)

        self.label_104 = QLabel(self.widget_36)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label_104.sizePolicy().hasHeightForWidth())
        self.label_104.setSizePolicy(sizePolicy)
        self.label_104.setMinimumSize(QSize(0, 0))
        self.label_104.setMaximumSize(QSize(20, 20))
        self.label_104.setSizeIncrement(QSize(0, 0))
        self.label_104.setBaseSize(QSize(0, 0))
        self.label_104.setLayoutDirection(Qt.LeftToRight)
        self.label_104.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version - W.svg"))
        self.label_104.setScaledContents(True)
        self.label_104.setAlignment(Qt.AlignCenter)
        self.label_104.setWordWrap(False)
        self.label_104.setMargin(0)

        self.horizontalLayout_56.addWidget(self.label_104)


        self.verticalLayout_32.addWidget(self.widget_36)

        self.widget_AuxPt3Value = QWidget(self.groupBox_AUX_PT3)
        self.widget_AuxPt3Value.setObjectName(u"widget_AuxPt3Value")
        self.horizontalLayout_57 = QHBoxLayout(self.widget_AuxPt3Value)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(-1, 5, 9, 5)
        self.label_52 = QLabel(self.widget_AuxPt3Value)
        self.label_52.setObjectName(u"label_52")
        sizePolicy.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy)
        self.label_52.setMinimumSize(QSize(0, 20))
        self.label_52.setMaximumSize(QSize(20, 20))
        self.label_52.setSizeIncrement(QSize(0, 0))
        self.label_52.setBaseSize(QSize(0, 0))
        self.label_52.setLayoutDirection(Qt.LeftToRight)
        self.label_52.setPixmap(QPixmap(u":/Logo/Calibration/Value.svg"))
        self.label_52.setScaledContents(True)
        self.label_52.setAlignment(Qt.AlignCenter)
        self.label_52.setWordWrap(False)
        self.label_52.setMargin(0)

        self.horizontalLayout_57.addWidget(self.label_52)

        self.label_txtModel_14 = QLabel(self.widget_AuxPt3Value)
        self.label_txtModel_14.setObjectName(u"label_txtModel_14")

        self.horizontalLayout_57.addWidget(self.label_txtModel_14)

        self.label_AuxPt3Value = QLabel(self.widget_AuxPt3Value)
        self.label_AuxPt3Value.setObjectName(u"label_AuxPt3Value")
        self.label_AuxPt3Value.setMinimumSize(QSize(0, 20))
        self.label_AuxPt3Value.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_57.addWidget(self.label_AuxPt3Value)

        self.label_105 = QLabel(self.widget_AuxPt3Value)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label_105.sizePolicy().hasHeightForWidth())
        self.label_105.setSizePolicy(sizePolicy)
        self.label_105.setMinimumSize(QSize(0, 0))
        self.label_105.setMaximumSize(QSize(20, 20))
        self.label_105.setSizeIncrement(QSize(0, 0))
        self.label_105.setBaseSize(QSize(0, 0))
        self.label_105.setLayoutDirection(Qt.LeftToRight)
        self.label_105.setPixmap(QPixmap(u":/Logo/Calibration/calibrationGo.svg"))
        self.label_105.setScaledContents(True)
        self.label_105.setAlignment(Qt.AlignCenter)
        self.label_105.setWordWrap(False)
        self.label_105.setMargin(0)

        self.horizontalLayout_57.addWidget(self.label_105)


        self.verticalLayout_32.addWidget(self.widget_AuxPt3Value)


        self.verticalLayout_15.addWidget(self.groupBox_AUX_PT3)

        self.groupBox_CalibrationParameters = QGroupBox(self.widget_19)
        self.groupBox_CalibrationParameters.setObjectName(u"groupBox_CalibrationParameters")
        sizePolicy5.setHeightForWidth(self.groupBox_CalibrationParameters.sizePolicy().hasHeightForWidth())
        self.groupBox_CalibrationParameters.setSizePolicy(sizePolicy5)
        self.groupBox_CalibrationParameters.setMinimumSize(QSize(0, 0))
        self.groupBox_CalibrationParameters.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_CalibrationParameters.setStyleSheet(u"Line{\n"
"/*background-color: rgba(0, 0, 0, 0.2);*/\n"
" /*color: rgba(0, 0, 255, 0.5);*/\n"
"/*border: 0.5px solid green;*/\n"
"/*border-style: inset;*/\n"
"}")
        self.groupBox_CalibrationParameters.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayout_34 = QVBoxLayout(self.groupBox_CalibrationParameters)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.widget_ORPCalValue = QWidget(self.groupBox_CalibrationParameters)
        self.widget_ORPCalValue.setObjectName(u"widget_ORPCalValue")
        self.widget_ORPCalValue.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_65 = QHBoxLayout(self.widget_ORPCalValue)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(-1, 5, -1, 5)
        self.label_98 = QLabel(self.widget_ORPCalValue)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setMinimumSize(QSize(0, 15))
        self.label_98.setMaximumSize(QSize(18, 18))
        self.label_98.setPixmap(QPixmap(u":/Logo/Dashboard/5-Setup-logging-rate/3-Log-data-every.svg"))
        self.label_98.setScaledContents(True)
        self.label_98.setMargin(0)

        self.horizontalLayout_65.addWidget(self.label_98)

        self.label_txtSN_14 = QLabel(self.widget_ORPCalValue)
        self.label_txtSN_14.setObjectName(u"label_txtSN_14")

        self.horizontalLayout_65.addWidget(self.label_txtSN_14)

        self.label_ORPCalValueType = QLabel(self.widget_ORPCalValue)
        self.label_ORPCalValueType.setObjectName(u"label_ORPCalValueType")
        self.label_ORPCalValueType.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_65.addWidget(self.label_ORPCalValueType)

        self.label_114 = QLabel(self.widget_ORPCalValue)
        self.label_114.setObjectName(u"label_114")
        sizePolicy.setHeightForWidth(self.label_114.sizePolicy().hasHeightForWidth())
        self.label_114.setSizePolicy(sizePolicy)
        self.label_114.setMinimumSize(QSize(0, 0))
        self.label_114.setMaximumSize(QSize(20, 20))
        self.label_114.setSizeIncrement(QSize(0, 0))
        self.label_114.setBaseSize(QSize(0, 0))
        self.label_114.setLayoutDirection(Qt.LeftToRight)
        self.label_114.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version - W.svg"))
        self.label_114.setScaledContents(True)
        self.label_114.setAlignment(Qt.AlignCenter)
        self.label_114.setWordWrap(False)
        self.label_114.setMargin(0)

        self.horizontalLayout_65.addWidget(self.label_114)


        self.verticalLayout_34.addWidget(self.widget_ORPCalValue)

        self.widget_AuxGSFactor = QWidget(self.groupBox_CalibrationParameters)
        self.widget_AuxGSFactor.setObjectName(u"widget_AuxGSFactor")
        self.widget_AuxGSFactor.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_55 = QHBoxLayout(self.widget_AuxGSFactor)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(-1, 5, 9, 5)
        self.label_50 = QLabel(self.widget_AuxGSFactor)
        self.label_50.setObjectName(u"label_50")
        sizePolicy.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy)
        self.label_50.setMinimumSize(QSize(0, 20))
        self.label_50.setMaximumSize(QSize(20, 20))
        self.label_50.setSizeIncrement(QSize(0, 0))
        self.label_50.setBaseSize(QSize(0, 0))
        self.label_50.setLayoutDirection(Qt.LeftToRight)
        self.label_50.setPixmap(QPixmap(u":/Logo/Calibration/calibration.svg"))
        self.label_50.setScaledContents(True)
        self.label_50.setAlignment(Qt.AlignCenter)
        self.label_50.setWordWrap(False)
        self.label_50.setMargin(0)

        self.horizontalLayout_55.addWidget(self.label_50)

        self.label_txtModel_17 = QLabel(self.widget_AuxGSFactor)
        self.label_txtModel_17.setObjectName(u"label_txtModel_17")

        self.horizontalLayout_55.addWidget(self.label_txtModel_17)

        self.label_AuxGSFactor = QLabel(self.widget_AuxGSFactor)
        self.label_AuxGSFactor.setObjectName(u"label_AuxGSFactor")
        self.label_AuxGSFactor.setMinimumSize(QSize(0, 20))
        self.label_AuxGSFactor.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_55.addWidget(self.label_AuxGSFactor)

        self.label_103 = QLabel(self.widget_AuxGSFactor)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label_103.sizePolicy().hasHeightForWidth())
        self.label_103.setSizePolicy(sizePolicy)
        self.label_103.setMinimumSize(QSize(0, 0))
        self.label_103.setMaximumSize(QSize(20, 20))
        self.label_103.setSizeIncrement(QSize(0, 0))
        self.label_103.setBaseSize(QSize(0, 0))
        self.label_103.setLayoutDirection(Qt.LeftToRight)
        self.label_103.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version - W.svg"))
        self.label_103.setScaledContents(True)
        self.label_103.setAlignment(Qt.AlignCenter)
        self.label_103.setWordWrap(False)
        self.label_103.setMargin(0)

        self.horizontalLayout_55.addWidget(self.label_103)


        self.verticalLayout_34.addWidget(self.widget_AuxGSFactor)

        self.widget_CalSensor_ECCalValue = QWidget(self.groupBox_CalibrationParameters)
        self.widget_CalSensor_ECCalValue.setObjectName(u"widget_CalSensor_ECCalValue")
        self.widget_CalSensor_ECCalValue.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_73 = QHBoxLayout(self.widget_CalSensor_ECCalValue)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(-1, 5, 9, 5)
        self.label_73 = QLabel(self.widget_CalSensor_ECCalValue)
        self.label_73.setObjectName(u"label_73")
        sizePolicy.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy)
        self.label_73.setMinimumSize(QSize(0, 20))
        self.label_73.setMaximumSize(QSize(20, 20))
        self.label_73.setSizeIncrement(QSize(0, 0))
        self.label_73.setBaseSize(QSize(0, 0))
        self.label_73.setLayoutDirection(Qt.LeftToRight)
        self.label_73.setPixmap(QPixmap(u":/Logo/Dashboard/5-Setup-logging-rate/3-Log-data-every.svg"))
        self.label_73.setScaledContents(True)
        self.label_73.setAlignment(Qt.AlignCenter)
        self.label_73.setWordWrap(False)
        self.label_73.setMargin(0)

        self.horizontalLayout_73.addWidget(self.label_73)

        self.label_txtModel_19 = QLabel(self.widget_CalSensor_ECCalValue)
        self.label_txtModel_19.setObjectName(u"label_txtModel_19")

        self.horizontalLayout_73.addWidget(self.label_txtModel_19)

        self.label_CalSensor_ECCalValue = QLabel(self.widget_CalSensor_ECCalValue)
        self.label_CalSensor_ECCalValue.setObjectName(u"label_CalSensor_ECCalValue")
        self.label_CalSensor_ECCalValue.setMinimumSize(QSize(0, 20))
        self.label_CalSensor_ECCalValue.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_73.addWidget(self.label_CalSensor_ECCalValue)

        self.label_106 = QLabel(self.widget_CalSensor_ECCalValue)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label_106.sizePolicy().hasHeightForWidth())
        self.label_106.setSizePolicy(sizePolicy)
        self.label_106.setMinimumSize(QSize(0, 0))
        self.label_106.setMaximumSize(QSize(20, 20))
        self.label_106.setSizeIncrement(QSize(0, 0))
        self.label_106.setBaseSize(QSize(0, 0))
        self.label_106.setLayoutDirection(Qt.LeftToRight)
        self.label_106.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version - W.svg"))
        self.label_106.setScaledContents(True)
        self.label_106.setAlignment(Qt.AlignCenter)
        self.label_106.setWordWrap(False)
        self.label_106.setMargin(0)

        self.horizontalLayout_73.addWidget(self.label_106)


        self.verticalLayout_34.addWidget(self.widget_CalSensor_ECCalValue)

        self.widget_CalSensor_ECUserValue = QWidget(self.groupBox_CalibrationParameters)
        self.widget_CalSensor_ECUserValue.setObjectName(u"widget_CalSensor_ECUserValue")
        self.widget_CalSensor_ECUserValue.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_75 = QHBoxLayout(self.widget_CalSensor_ECUserValue)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(-1, 5, 9, 5)
        self.label_100 = QLabel(self.widget_CalSensor_ECUserValue)
        self.label_100.setObjectName(u"label_100")
        sizePolicy.setHeightForWidth(self.label_100.sizePolicy().hasHeightForWidth())
        self.label_100.setSizePolicy(sizePolicy)
        self.label_100.setMinimumSize(QSize(0, 20))
        self.label_100.setMaximumSize(QSize(20, 20))
        self.label_100.setSizeIncrement(QSize(0, 0))
        self.label_100.setBaseSize(QSize(0, 0))
        self.label_100.setLayoutDirection(Qt.LeftToRight)
        self.label_100.setPixmap(QPixmap(u":/Logo/Calibration/calibration.svg"))
        self.label_100.setScaledContents(True)
        self.label_100.setAlignment(Qt.AlignCenter)
        self.label_100.setWordWrap(False)
        self.label_100.setMargin(0)

        self.horizontalLayout_75.addWidget(self.label_100)

        self.label_txtModel_20 = QLabel(self.widget_CalSensor_ECUserValue)
        self.label_txtModel_20.setObjectName(u"label_txtModel_20")

        self.horizontalLayout_75.addWidget(self.label_txtModel_20)

        self.label_CalSensor_ECUserValue = QLabel(self.widget_CalSensor_ECUserValue)
        self.label_CalSensor_ECUserValue.setObjectName(u"label_CalSensor_ECUserValue")
        self.label_CalSensor_ECUserValue.setMinimumSize(QSize(0, 20))
        self.label_CalSensor_ECUserValue.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_75.addWidget(self.label_CalSensor_ECUserValue)

        self.label_107 = QLabel(self.widget_CalSensor_ECUserValue)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label_107.sizePolicy().hasHeightForWidth())
        self.label_107.setSizePolicy(sizePolicy)
        self.label_107.setMinimumSize(QSize(0, 0))
        self.label_107.setMaximumSize(QSize(20, 20))
        self.label_107.setSizeIncrement(QSize(0, 0))
        self.label_107.setBaseSize(QSize(0, 0))
        self.label_107.setLayoutDirection(Qt.LeftToRight)
        self.label_107.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version - W.svg"))
        self.label_107.setScaledContents(True)
        self.label_107.setAlignment(Qt.AlignCenter)
        self.label_107.setWordWrap(False)
        self.label_107.setMargin(0)

        self.horizontalLayout_75.addWidget(self.label_107)


        self.verticalLayout_34.addWidget(self.widget_CalSensor_ECUserValue)


        self.verticalLayout_15.addWidget(self.groupBox_CalibrationParameters)

        self.verticalSpacer_9 = QSpacerItem(20, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_15.addItem(self.verticalSpacer_9)

        self.pushButton_RestoreDefaultCalibration = QPushButton(self.widget_19)
        self.pushButton_RestoreDefaultCalibration.setObjectName(u"pushButton_RestoreDefaultCalibration")
        self.pushButton_RestoreDefaultCalibration.setMinimumSize(QSize(0, 30))
        self.pushButton_RestoreDefaultCalibration.setStyleSheet(u"margin: 0px 50px;")
        icon21 = QIcon()
        icon21.addFile(u":/Logo/Calibration/calibration-restore.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_RestoreDefaultCalibration.setIcon(icon21)

        self.verticalLayout_15.addWidget(self.pushButton_RestoreDefaultCalibration)

        self.label_ASAPpro_calibRestore = QLabel(self.widget_19)
        self.label_ASAPpro_calibRestore.setObjectName(u"label_ASAPpro_calibRestore")
        self.label_ASAPpro_calibRestore.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.label_ASAPpro_calibRestore)

        self.widget_45 = QWidget(self.widget_19)
        self.widget_45.setObjectName(u"widget_45")
        self.widget_45.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_54 = QHBoxLayout(self.widget_45)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_CalibHiddenChannelName = QLabel(self.widget_45)
        self.label_CalibHiddenChannelName.setObjectName(u"label_CalibHiddenChannelName")
        self.label_CalibHiddenChannelName.setStyleSheet(u"color:transparent;")

        self.horizontalLayout_54.addWidget(self.label_CalibHiddenChannelName)

        self.label_13 = QLabel(self.widget_45)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color:transparent;")

        self.horizontalLayout_54.addWidget(self.label_13)


        self.verticalLayout_15.addWidget(self.widget_45)

        self.verticalSpacer_7 = QSpacerItem(20, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_7)


        self.horizontalLayout_44.addWidget(self.widget_19)

        self.textBrowser_6 = QTextBrowser(self.widget_17)
        self.textBrowser_6.setObjectName(u"textBrowser_6")
        self.textBrowser_6.setStyleSheet(u"")

        self.horizontalLayout_44.addWidget(self.textBrowser_6)

        self.horizontalLayout_44.setStretch(0, 3)
        self.horizontalLayout_44.setStretch(1, 4)

        self.horizontalLayout_43.addWidget(self.widget_17)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_18.addWidget(self.scrollArea_3)

        self.verticalLayout_18.setStretch(0, 1)
        self.verticalLayout_18.setStretch(1, 4)
        self.stackedWidget_calibrationMain.addWidget(self.calibration_main)
        self.calibration_page = QWidget()
        self.calibration_page.setObjectName(u"calibration_page")
        self.calibration_page.setMinimumSize(QSize(0, 0))
        self.gridLayout_11 = QGridLayout(self.calibration_page)
        self.gridLayout_11.setSpacing(10)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.widget_calibGraph = QWidget(self.calibration_page)
        self.widget_calibGraph.setObjectName(u"widget_calibGraph")
        self.widget_calibGraph.setMinimumSize(QSize(0, 100))

        self.gridLayout_11.addWidget(self.widget_calibGraph, 2, 0, 1, 3)

        self.widget_30 = QWidget(self.calibration_page)
        self.widget_30.setObjectName(u"widget_30")
        self.horizontalLayout_45 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_hiddenChannelName = QLabel(self.widget_30)
        self.label_hiddenChannelName.setObjectName(u"label_hiddenChannelName")
        self.label_hiddenChannelName.setStyleSheet(u"color:transparent;")

        self.horizontalLayout_45.addWidget(self.label_hiddenChannelName)

        self.label_7 = QLabel(self.widget_30)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color:transparent;")

        self.horizontalLayout_45.addWidget(self.label_7)

        self.label_hiddenPointNumber = QLabel(self.widget_30)
        self.label_hiddenPointNumber.setObjectName(u"label_hiddenPointNumber")
        self.label_hiddenPointNumber.setStyleSheet(u"color:transparent;")

        self.horizontalLayout_45.addWidget(self.label_hiddenPointNumber)


        self.gridLayout_11.addWidget(self.widget_30, 0, 1, 1, 1)

        self.widget_37 = QWidget(self.calibration_page)
        self.widget_37.setObjectName(u"widget_37")
        self.widget_37.setMinimumSize(QSize(0, 200))
        self.horizontalLayout_46 = QHBoxLayout(self.widget_37)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.widget_PHCalMeasure7 = QWidget(self.widget_37)
        self.widget_PHCalMeasure7.setObjectName(u"widget_PHCalMeasure7")
        self.widget_PHCalMeasure7.setMinimumSize(QSize(320, 0))
        self.verticalLayout = QVBoxLayout(self.widget_PHCalMeasure7)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_calibRTValue = QLabel(self.widget_PHCalMeasure7)
        self.label_calibRTValue.setObjectName(u"label_calibRTValue")
        font3 = QFont()
        font3.setPointSize(40)
        font3.setBold(True)
        self.label_calibRTValue.setFont(font3)
        self.label_calibRTValue.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_calibRTValue)

        self.label_calibRTUnit = QLabel(self.widget_PHCalMeasure7)
        self.label_calibRTUnit.setObjectName(u"label_calibRTUnit")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(False)
        self.label_calibRTUnit.setFont(font4)
        self.label_calibRTUnit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_calibRTUnit)

        self.widget_calibRTpHmV = QWidget(self.widget_PHCalMeasure7)
        self.widget_calibRTpHmV.setObjectName(u"widget_calibRTpHmV")
        self.horizontalLayout_48 = QHBoxLayout(self.widget_calibRTpHmV)
        self.horizontalLayout_48.setSpacing(15)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(-1, 4, -1, 4)
        self.label_23 = QLabel(self.widget_calibRTpHmV)
        self.label_23.setObjectName(u"label_23")
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.label_23.setFont(font5)
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_48.addWidget(self.label_23)

        self.label_calibRT_pHmvValue = QLabel(self.widget_calibRTpHmV)
        self.label_calibRT_pHmvValue.setObjectName(u"label_calibRT_pHmvValue")
        self.label_calibRT_pHmvValue.setFont(font4)
        self.label_calibRT_pHmvValue.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_48.addWidget(self.label_calibRT_pHmvValue)


        self.verticalLayout.addWidget(self.widget_calibRTpHmV)

        self.widget_16 = QWidget(self.widget_PHCalMeasure7)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_49 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_49.setSpacing(15)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(-1, 4, -1, 4)
        self.label_25 = QLabel(self.widget_16)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font5)
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_49.addWidget(self.label_25)

        self.label_calibRT_tempValue = QLabel(self.widget_16)
        self.label_calibRT_tempValue.setObjectName(u"label_calibRT_tempValue")
        self.label_calibRT_tempValue.setFont(font4)
        self.label_calibRT_tempValue.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_49.addWidget(self.label_calibRT_tempValue)


        self.verticalLayout.addWidget(self.widget_16)

        self.widget_20 = QWidget(self.widget_PHCalMeasure7)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_50 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_50.setSpacing(15)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(-1, 4, -1, 4)
        self.label_27 = QLabel(self.widget_20)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font5)
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_50.addWidget(self.label_27)

        self.label_calibRT_baroValue = QLabel(self.widget_20)
        self.label_calibRT_baroValue.setObjectName(u"label_calibRT_baroValue")
        self.label_calibRT_baroValue.setFont(font4)
        self.label_calibRT_baroValue.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_50.addWidget(self.label_calibRT_baroValue)


        self.verticalLayout.addWidget(self.widget_20)

        self.widget_31 = QWidget(self.widget_PHCalMeasure7)
        self.widget_31.setObjectName(u"widget_31")
        self.widget_31.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_52 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(-1, 4, -1, 4)
        self.label_43 = QLabel(self.widget_31)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_52.addWidget(self.label_43)

        self.label_calibPointLastCalibDate = QLabel(self.widget_31)
        self.label_calibPointLastCalibDate.setObjectName(u"label_calibPointLastCalibDate")

        self.horizontalLayout_52.addWidget(self.label_calibPointLastCalibDate)


        self.verticalLayout.addWidget(self.widget_31)

        self.widget_32 = QWidget(self.widget_PHCalMeasure7)
        self.widget_32.setObjectName(u"widget_32")
        self.widget_32.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_53 = QHBoxLayout(self.widget_32)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(-1, 4, -1, 4)
        self.label_44 = QLabel(self.widget_32)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_53.addWidget(self.label_44)

        self.label_calibPointLastCalibValue = QLabel(self.widget_32)
        self.label_calibPointLastCalibValue.setObjectName(u"label_calibPointLastCalibValue")

        self.horizontalLayout_53.addWidget(self.label_calibPointLastCalibValue)


        self.verticalLayout.addWidget(self.widget_32)

        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)

        self.horizontalLayout_46.addWidget(self.widget_PHCalMeasure7)

        self.textBrowser_calPoint = QTextBrowser(self.widget_37)
        self.textBrowser_calPoint.setObjectName(u"textBrowser_calPoint")

        self.horizontalLayout_46.addWidget(self.textBrowser_calPoint)

        self.widget_39 = QWidget(self.widget_37)
        self.widget_39.setObjectName(u"widget_39")
        self.widget_39.setMinimumSize(QSize(0, 0))
        self.verticalLayout_6 = QVBoxLayout(self.widget_39)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.groupBox_CalibrationParameters_Point = QGroupBox(self.widget_39)
        self.groupBox_CalibrationParameters_Point.setObjectName(u"groupBox_CalibrationParameters_Point")
        sizePolicy3.setHeightForWidth(self.groupBox_CalibrationParameters_Point.sizePolicy().hasHeightForWidth())
        self.groupBox_CalibrationParameters_Point.setSizePolicy(sizePolicy3)
        self.groupBox_CalibrationParameters_Point.setMinimumSize(QSize(230, 0))
        self.groupBox_CalibrationParameters_Point.setMaximumSize(QSize(300, 16777215))
        self.groupBox_CalibrationParameters_Point.setStyleSheet(u"Line{\n"
"/*background-color: rgba(0, 0, 0, 0.2);*/\n"
" /*color: rgba(0, 0, 255, 0.5);*/\n"
"/*border: 0.5px solid green;*/\n"
"/*border-style: inset;*/\n"
"}")
        self.groupBox_CalibrationParameters_Point.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayout_38 = QVBoxLayout(self.groupBox_CalibrationParameters_Point)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.widget_ORPCalValue_Point = QWidget(self.groupBox_CalibrationParameters_Point)
        self.widget_ORPCalValue_Point.setObjectName(u"widget_ORPCalValue_Point")
        self.widget_ORPCalValue_Point.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_70 = QHBoxLayout(self.widget_ORPCalValue_Point)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(-1, 5, -1, 5)
        self.label_txtSN_15 = QLabel(self.widget_ORPCalValue_Point)
        self.label_txtSN_15.setObjectName(u"label_txtSN_15")

        self.horizontalLayout_70.addWidget(self.label_txtSN_15)

        self.comboBox_ORPCalValue_Point = QComboBox(self.widget_ORPCalValue_Point)
        self.comboBox_ORPCalValue_Point.addItem("")
        self.comboBox_ORPCalValue_Point.addItem("")
        self.comboBox_ORPCalValue_Point.setObjectName(u"comboBox_ORPCalValue_Point")

        self.horizontalLayout_70.addWidget(self.comboBox_ORPCalValue_Point)


        self.verticalLayout_38.addWidget(self.widget_ORPCalValue_Point)

        self.widget_ECCalValue_Point = QWidget(self.groupBox_CalibrationParameters_Point)
        self.widget_ECCalValue_Point.setObjectName(u"widget_ECCalValue_Point")
        self.widget_ECCalValue_Point.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_74 = QHBoxLayout(self.widget_ECCalValue_Point)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(-1, 5, -1, 5)
        self.label_txtSN_18 = QLabel(self.widget_ECCalValue_Point)
        self.label_txtSN_18.setObjectName(u"label_txtSN_18")

        self.horizontalLayout_74.addWidget(self.label_txtSN_18)

        self.comboBox_ECCalValue_Point = QComboBox(self.widget_ECCalValue_Point)
        self.comboBox_ECCalValue_Point.addItem("")
        self.comboBox_ECCalValue_Point.addItem("")
        self.comboBox_ECCalValue_Point.addItem("")
        self.comboBox_ECCalValue_Point.setObjectName(u"comboBox_ECCalValue_Point")

        self.horizontalLayout_74.addWidget(self.comboBox_ECCalValue_Point)


        self.verticalLayout_38.addWidget(self.widget_ECCalValue_Point)

        self.widget_ECCalValue_Point_2 = QWidget(self.groupBox_CalibrationParameters_Point)
        self.widget_ECCalValue_Point_2.setObjectName(u"widget_ECCalValue_Point_2")
        self.widget_ECCalValue_Point_2.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_71 = QHBoxLayout(self.widget_ECCalValue_Point_2)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(-1, 5, -1, 5)
        self.label_txtSN_16 = QLabel(self.widget_ECCalValue_Point_2)
        self.label_txtSN_16.setObjectName(u"label_txtSN_16")

        self.horizontalLayout_71.addWidget(self.label_txtSN_16)

        self.spinBox_ECCalValue_2_Point = QSpinBox(self.widget_ECCalValue_Point_2)
        self.spinBox_ECCalValue_2_Point.setObjectName(u"spinBox_ECCalValue_2_Point")
        self.spinBox_ECCalValue_2_Point.setMinimum(100)
        self.spinBox_ECCalValue_2_Point.setMaximum(99999)
        self.spinBox_ECCalValue_2_Point.setSingleStep(1)

        self.horizontalLayout_71.addWidget(self.spinBox_ECCalValue_2_Point)


        self.verticalLayout_38.addWidget(self.widget_ECCalValue_Point_2)

        self.widget_ECCalValue_Point_3 = QWidget(self.groupBox_CalibrationParameters_Point)
        self.widget_ECCalValue_Point_3.setObjectName(u"widget_ECCalValue_Point_3")
        self.widget_ECCalValue_Point_3.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_78 = QHBoxLayout(self.widget_ECCalValue_Point_3)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(-1, 5, -1, 5)
        self.label_txtSN_17 = QLabel(self.widget_ECCalValue_Point_3)
        self.label_txtSN_17.setObjectName(u"label_txtSN_17")

        self.horizontalLayout_78.addWidget(self.label_txtSN_17)

        self.spinBox_ECCalValue_2_Point_2 = QSpinBox(self.widget_ECCalValue_Point_3)
        self.spinBox_ECCalValue_2_Point_2.setObjectName(u"spinBox_ECCalValue_2_Point_2")
        self.spinBox_ECCalValue_2_Point_2.setEnabled(False)
        self.spinBox_ECCalValue_2_Point_2.setMinimum(100)
        self.spinBox_ECCalValue_2_Point_2.setMaximum(99999)
        self.spinBox_ECCalValue_2_Point_2.setSingleStep(1)

        self.horizontalLayout_78.addWidget(self.spinBox_ECCalValue_2_Point_2)


        self.verticalLayout_38.addWidget(self.widget_ECCalValue_Point_3)

        self.widget_ProbeAUXCalValue_Point = QWidget(self.groupBox_CalibrationParameters_Point)
        self.widget_ProbeAUXCalValue_Point.setObjectName(u"widget_ProbeAUXCalValue_Point")
        self.widget_ProbeAUXCalValue_Point.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_111 = QHBoxLayout(self.widget_ProbeAUXCalValue_Point)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.horizontalLayout_111.setContentsMargins(-1, 5, -1, 5)
        self.label_txtSN_20 = QLabel(self.widget_ProbeAUXCalValue_Point)
        self.label_txtSN_20.setObjectName(u"label_txtSN_20")

        self.horizontalLayout_111.addWidget(self.label_txtSN_20)

        self.spinBox_ProbeAUXCalValueP2 = QSpinBox(self.widget_ProbeAUXCalValue_Point)
        self.spinBox_ProbeAUXCalValueP2.setObjectName(u"spinBox_ProbeAUXCalValueP2")
        self.spinBox_ProbeAUXCalValueP2.setEnabled(True)
        self.spinBox_ProbeAUXCalValueP2.setMinimum(5)
        self.spinBox_ProbeAUXCalValueP2.setMaximum(500000)
        self.spinBox_ProbeAUXCalValueP2.setSingleStep(1)
        self.spinBox_ProbeAUXCalValueP2.setValue(500)

        self.horizontalLayout_111.addWidget(self.spinBox_ProbeAUXCalValueP2)


        self.verticalLayout_38.addWidget(self.widget_ProbeAUXCalValue_Point)


        self.verticalLayout_6.addWidget(self.groupBox_CalibrationParameters_Point)

        self.verticalSpacer_6 = QSpacerItem(20, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)


        self.horizontalLayout_46.addWidget(self.widget_39)


        self.gridLayout_11.addWidget(self.widget_37, 1, 0, 1, 3)

        self.label_calibPointName = QLabel(self.calibration_page)
        self.label_calibPointName.setObjectName(u"label_calibPointName")
        font6 = QFont()
        font6.setPointSize(19)
        font6.setBold(True)
        self.label_calibPointName.setFont(font6)

        self.gridLayout_11.addWidget(self.label_calibPointName, 0, 0, 1, 1)

        self.widget_28 = QWidget(self.calibration_page)
        self.widget_28.setObjectName(u"widget_28")
        self.horizontalLayout_51 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_51.setSpacing(50)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(50, -1, 50, -1)
        self.pushButton_calibrateCancel = QPushButton(self.widget_28)
        self.pushButton_calibrateCancel.setObjectName(u"pushButton_calibrateCancel")
        self.pushButton_calibrateCancel.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_51.addWidget(self.pushButton_calibrateCancel)

        self.pushButton_calibrateAndExit = QPushButton(self.widget_28)
        self.pushButton_calibrateAndExit.setObjectName(u"pushButton_calibrateAndExit")
        self.pushButton_calibrateAndExit.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_51.addWidget(self.pushButton_calibrateAndExit)


        self.gridLayout_11.addWidget(self.widget_28, 3, 0, 1, 3)

        self.gridLayout_11.setRowStretch(0, 1)
        self.gridLayout_11.setRowStretch(1, 15)
        self.gridLayout_11.setRowStretch(2, 15)
        self.stackedWidget_calibrationMain.addWidget(self.calibration_page)

        self.gridLayout_2.addWidget(self.stackedWidget_calibrationMain, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4_Calibration)
        self.page_5_About = QWidget()
        self.page_5_About.setObjectName(u"page_5_About")
        self.gridLayout_10 = QGridLayout(self.page_5_About)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.stackedWidget_2 = QStackedWidget(self.page_5_About)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.horizontalLayout_37 = QHBoxLayout(self.page_10)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.textBrowser_4 = QTextBrowser(self.page_10)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        font7 = QFont()
        font7.setPointSize(10)
        self.textBrowser_4.setFont(font7)

        self.horizontalLayout_37.addWidget(self.textBrowser_4)

        self.widget_26 = QWidget(self.page_10)
        self.widget_26.setObjectName(u"widget_26")
        sizePolicy.setHeightForWidth(self.widget_26.sizePolicy().hasHeightForWidth())
        self.widget_26.setSizePolicy(sizePolicy)
        self.widget_26.setMinimumSize(QSize(80, 0))
        self.verticalLayout_25 = QVBoxLayout(self.widget_26)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(20, -1, 20, -1)
        self.label_QtLogo = QLabel(self.widget_26)
        self.label_QtLogo.setObjectName(u"label_QtLogo")
        sizePolicy.setHeightForWidth(self.label_QtLogo.sizePolicy().hasHeightForWidth())
        self.label_QtLogo.setSizePolicy(sizePolicy)
        self.label_QtLogo.setMinimumSize(QSize(50, 50))
        self.label_QtLogo.setMaximumSize(QSize(50, 50))
        self.label_QtLogo.setPixmap(QPixmap(u":/Logo/About/built-with-Qt_40px_606060.png"))
        self.label_QtLogo.setScaledContents(True)
        self.label_QtLogo.setAlignment(Qt.AlignCenter)
        self.label_QtLogo.setWordWrap(False)
        self.label_QtLogo.setMargin(0)

        self.verticalLayout_25.addWidget(self.label_QtLogo)

        self.verticalSpacer_12 = QSpacerItem(20, 428, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_12)


        self.horizontalLayout_37.addWidget(self.widget_26)

        self.stackedWidget_2.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.stackedWidget_2.addWidget(self.page_11)

        self.gridLayout_10.addWidget(self.stackedWidget_2, 1, 0, 1, 1)

        self.widget_13 = QWidget(self.page_5_About)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(0, 100))
        self.horizontalLayout_76 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.widget_AboutLicensesBtn = QWidget(self.widget_13)
        self.widget_AboutLicensesBtn.setObjectName(u"widget_AboutLicensesBtn")
        self.widget_AboutLicensesBtn.setMinimumSize(QSize(90, 80))
        self.widget_AboutLicensesBtn.setMaximumSize(QSize(90, 80))
        self.gridLayout_7 = QGridLayout(self.widget_AboutLicensesBtn)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_24 = QLabel(self.widget_AboutLicensesBtn)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(30, 16777215))
        font8 = QFont()
        font8.setPointSize(1)
        self.label_24.setFont(font8)
        self.label_24.setAutoFillBackground(False)
        self.label_24.setPixmap(QPixmap(u":/Logo/About/software-license-min.svg"))
        self.label_24.setScaledContents(True)
        self.label_24.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_24, 0, 0, 1, 1)

        self.label_11 = QLabel(self.widget_AboutLicensesBtn)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_7.addWidget(self.label_11, 1, 0, 1, 1)


        self.horizontalLayout_76.addWidget(self.widget_AboutLicensesBtn)


        self.gridLayout_10.addWidget(self.widget_13, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_5_About)
        self.page_6_PC_Config = QWidget()
        self.page_6_PC_Config.setObjectName(u"page_6_PC_Config")
        self.horizontalLayout_85 = QHBoxLayout(self.page_6_PC_Config)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.widget_PCConfig_left = QWidget(self.page_6_PC_Config)
        self.widget_PCConfig_left.setObjectName(u"widget_PCConfig_left")
        sizePolicy.setHeightForWidth(self.widget_PCConfig_left.sizePolicy().hasHeightForWidth())
        self.widget_PCConfig_left.setSizePolicy(sizePolicy)
        self.verticalLayout_43 = QVBoxLayout(self.widget_PCConfig_left)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(18, 6, -1, -1)
        self.widget_47 = QWidget(self.widget_PCConfig_left)
        self.widget_47.setObjectName(u"widget_47")
        self.widget_47.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_86 = QHBoxLayout(self.widget_47)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.label_131 = QLabel(self.widget_47)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setMaximumSize(QSize(60, 60))
        self.label_131.setStyleSheet(u"background-color:white;\n"
"border-radius:30px;")
        self.label_131.setPixmap(QPixmap(u":/Logo/PCConf/3-Software-version-black.svg"))
        self.label_131.setScaledContents(True)
        self.label_131.setMargin(12)

        self.horizontalLayout_86.addWidget(self.label_131)

        self.label_130 = QLabel(self.widget_47)
        self.label_130.setObjectName(u"label_130")
        font9 = QFont()
        font9.setPointSize(13)
        font9.setWeight(QFont.DemiBold)
        self.label_130.setFont(font9)

        self.horizontalLayout_86.addWidget(self.label_130)


        self.verticalLayout_43.addWidget(self.widget_47)

        self.groupBox_PCConf_Measure = QGroupBox(self.widget_PCConfig_left)
        self.groupBox_PCConf_Measure.setObjectName(u"groupBox_PCConf_Measure")
        sizePolicy.setHeightForWidth(self.groupBox_PCConf_Measure.sizePolicy().hasHeightForWidth())
        self.groupBox_PCConf_Measure.setSizePolicy(sizePolicy)
        self.groupBox_PCConf_Measure.setMinimumSize(QSize(0, 0))
        self.groupBox_PCConf_Measure.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_PCConf_Measure.setStyleSheet(u"Line{\n"
"/*background-color: rgba(0, 0, 0, 0.2);*/\n"
" /*color: rgba(0, 0, 255, 0.5);*/\n"
"/*border: 0.5px solid green;*/\n"
"/*border-style: inset;*/\n"
"}")
        self.groupBox_PCConf_Measure.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayout_41 = QVBoxLayout(self.groupBox_PCConf_Measure)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.widget_ECRefTemp = QWidget(self.groupBox_PCConf_Measure)
        self.widget_ECRefTemp.setObjectName(u"widget_ECRefTemp")
        self.horizontalLayout_83 = QHBoxLayout(self.widget_ECRefTemp)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(-1, 5, -1, 5)
        self.label_124 = QLabel(self.widget_ECRefTemp)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setMinimumSize(QSize(0, 15))
        self.label_124.setMaximumSize(QSize(20, 20))
        self.label_124.setPixmap(QPixmap(u":/Logo/Dashboard/2-Sonde-clock/2-Time.svg"))
        self.label_124.setScaledContents(True)
        self.label_124.setMargin(0)

        self.horizontalLayout_83.addWidget(self.label_124)

        self.label_125 = QLabel(self.widget_ECRefTemp)
        self.label_125.setObjectName(u"label_125")

        self.horizontalLayout_83.addWidget(self.label_125)

        self.label_Config_ECRefTemp = QLabel(self.widget_ECRefTemp)
        self.label_Config_ECRefTemp.setObjectName(u"label_Config_ECRefTemp")
        self.label_Config_ECRefTemp.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_83.addWidget(self.label_Config_ECRefTemp)

        self.label_126 = QLabel(self.widget_ECRefTemp)
        self.label_126.setObjectName(u"label_126")
        sizePolicy.setHeightForWidth(self.label_126.sizePolicy().hasHeightForWidth())
        self.label_126.setSizePolicy(sizePolicy)
        self.label_126.setMinimumSize(QSize(0, 0))
        self.label_126.setMaximumSize(QSize(20, 20))
        self.label_126.setSizeIncrement(QSize(0, 0))
        self.label_126.setBaseSize(QSize(0, 0))
        self.label_126.setLayoutDirection(Qt.LeftToRight)
        self.label_126.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_126.setScaledContents(True)
        self.label_126.setAlignment(Qt.AlignCenter)
        self.label_126.setWordWrap(False)
        self.label_126.setMargin(0)

        self.horizontalLayout_83.addWidget(self.label_126)


        self.verticalLayout_41.addWidget(self.widget_ECRefTemp)

        self.widget_TempUnit = QWidget(self.groupBox_PCConf_Measure)
        self.widget_TempUnit.setObjectName(u"widget_TempUnit")
        self.horizontalLayout_82 = QHBoxLayout(self.widget_TempUnit)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(-1, 5, -1, 5)
        self.label_121 = QLabel(self.widget_TempUnit)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setMinimumSize(QSize(0, 15))
        self.label_121.setMaximumSize(QSize(20, 20))
        self.label_121.setPixmap(QPixmap(u":/Logo/Dashboard/2-Sonde-clock/2-Time.svg"))
        self.label_121.setScaledContents(True)
        self.label_121.setMargin(0)

        self.horizontalLayout_82.addWidget(self.label_121)

        self.label_122 = QLabel(self.widget_TempUnit)
        self.label_122.setObjectName(u"label_122")

        self.horizontalLayout_82.addWidget(self.label_122)

        self.label_Config_TempUnit = QLabel(self.widget_TempUnit)
        self.label_Config_TempUnit.setObjectName(u"label_Config_TempUnit")
        self.label_Config_TempUnit.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_82.addWidget(self.label_Config_TempUnit)

        self.label_123 = QLabel(self.widget_TempUnit)
        self.label_123.setObjectName(u"label_123")
        sizePolicy.setHeightForWidth(self.label_123.sizePolicy().hasHeightForWidth())
        self.label_123.setSizePolicy(sizePolicy)
        self.label_123.setMinimumSize(QSize(0, 0))
        self.label_123.setMaximumSize(QSize(20, 20))
        self.label_123.setSizeIncrement(QSize(0, 0))
        self.label_123.setBaseSize(QSize(0, 0))
        self.label_123.setLayoutDirection(Qt.LeftToRight)
        self.label_123.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_123.setScaledContents(True)
        self.label_123.setAlignment(Qt.AlignCenter)
        self.label_123.setWordWrap(False)
        self.label_123.setMargin(0)

        self.horizontalLayout_82.addWidget(self.label_123)


        self.verticalLayout_41.addWidget(self.widget_TempUnit)

        self.widget_DepthUnit = QWidget(self.groupBox_PCConf_Measure)
        self.widget_DepthUnit.setObjectName(u"widget_DepthUnit")
        self.horizontalLayout_80 = QHBoxLayout(self.widget_DepthUnit)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(-1, 3, -1, 5)
        self.label_102 = QLabel(self.widget_DepthUnit)
        self.label_102.setObjectName(u"label_102")
        sizePolicy.setHeightForWidth(self.label_102.sizePolicy().hasHeightForWidth())
        self.label_102.setSizePolicy(sizePolicy)
        self.label_102.setMinimumSize(QSize(0, 20))
        self.label_102.setMaximumSize(QSize(20, 20))
        self.label_102.setSizeIncrement(QSize(0, 0))
        self.label_102.setBaseSize(QSize(0, 0))
        self.label_102.setLayoutDirection(Qt.LeftToRight)
        self.label_102.setPixmap(QPixmap(u":/Logo/Dashboard/2-Sonde-clock/1-Date.svg"))
        self.label_102.setScaledContents(True)
        self.label_102.setAlignment(Qt.AlignCenter)
        self.label_102.setWordWrap(False)
        self.label_102.setMargin(0)

        self.horizontalLayout_80.addWidget(self.label_102)

        self.label_110 = QLabel(self.widget_DepthUnit)
        self.label_110.setObjectName(u"label_110")

        self.horizontalLayout_80.addWidget(self.label_110)

        self.label_Config_DepthUnit = QLabel(self.widget_DepthUnit)
        self.label_Config_DepthUnit.setObjectName(u"label_Config_DepthUnit")
        self.label_Config_DepthUnit.setMinimumSize(QSize(0, 0))
        self.label_Config_DepthUnit.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_80.addWidget(self.label_Config_DepthUnit)

        self.label_117 = QLabel(self.widget_DepthUnit)
        self.label_117.setObjectName(u"label_117")
        sizePolicy.setHeightForWidth(self.label_117.sizePolicy().hasHeightForWidth())
        self.label_117.setSizePolicy(sizePolicy)
        self.label_117.setMinimumSize(QSize(0, 0))
        self.label_117.setMaximumSize(QSize(20, 20))
        self.label_117.setSizeIncrement(QSize(0, 0))
        self.label_117.setBaseSize(QSize(0, 0))
        self.label_117.setLayoutDirection(Qt.LeftToRight)
        self.label_117.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_117.setScaledContents(True)
        self.label_117.setAlignment(Qt.AlignCenter)
        self.label_117.setWordWrap(False)
        self.label_117.setMargin(0)

        self.horizontalLayout_80.addWidget(self.label_117)


        self.verticalLayout_41.addWidget(self.widget_DepthUnit)

        self.widget_TDSFactor = QWidget(self.groupBox_PCConf_Measure)
        self.widget_TDSFactor.setObjectName(u"widget_TDSFactor")
        self.horizontalLayout_81 = QHBoxLayout(self.widget_TDSFactor)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(-1, 5, -1, 5)
        self.label_118 = QLabel(self.widget_TDSFactor)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setMinimumSize(QSize(0, 15))
        self.label_118.setMaximumSize(QSize(20, 20))
        self.label_118.setPixmap(QPixmap(u":/Logo/Dashboard/2-Sonde-clock/2-Time.svg"))
        self.label_118.setScaledContents(True)
        self.label_118.setMargin(0)

        self.horizontalLayout_81.addWidget(self.label_118)

        self.label_119 = QLabel(self.widget_TDSFactor)
        self.label_119.setObjectName(u"label_119")

        self.horizontalLayout_81.addWidget(self.label_119)

        self.label_Config_TDSFactor = QLabel(self.widget_TDSFactor)
        self.label_Config_TDSFactor.setObjectName(u"label_Config_TDSFactor")
        self.label_Config_TDSFactor.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_81.addWidget(self.label_Config_TDSFactor)

        self.label_120 = QLabel(self.widget_TDSFactor)
        self.label_120.setObjectName(u"label_120")
        sizePolicy.setHeightForWidth(self.label_120.sizePolicy().hasHeightForWidth())
        self.label_120.setSizePolicy(sizePolicy)
        self.label_120.setMinimumSize(QSize(0, 0))
        self.label_120.setMaximumSize(QSize(20, 20))
        self.label_120.setSizeIncrement(QSize(0, 0))
        self.label_120.setBaseSize(QSize(0, 0))
        self.label_120.setLayoutDirection(Qt.LeftToRight)
        self.label_120.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_120.setScaledContents(True)
        self.label_120.setAlignment(Qt.AlignCenter)
        self.label_120.setWordWrap(False)
        self.label_120.setMargin(0)

        self.horizontalLayout_81.addWidget(self.label_120)


        self.verticalLayout_41.addWidget(self.widget_TDSFactor)


        self.verticalLayout_43.addWidget(self.groupBox_PCConf_Measure)

        self.widget_48 = QWidget(self.widget_PCConfig_left)
        self.widget_48.setObjectName(u"widget_48")
        self.widget_48.setMinimumSize(QSize(0, 18))

        self.verticalLayout_43.addWidget(self.widget_48)

        self.groupBox_PCConf_AppSettings = QGroupBox(self.widget_PCConfig_left)
        self.groupBox_PCConf_AppSettings.setObjectName(u"groupBox_PCConf_AppSettings")
        sizePolicy.setHeightForWidth(self.groupBox_PCConf_AppSettings.sizePolicy().hasHeightForWidth())
        self.groupBox_PCConf_AppSettings.setSizePolicy(sizePolicy)
        self.groupBox_PCConf_AppSettings.setMinimumSize(QSize(0, 0))
        self.groupBox_PCConf_AppSettings.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_PCConf_AppSettings.setStyleSheet(u"Line{\n"
"/*background-color: rgba(0, 0, 0, 0.2);*/\n"
" /*color: rgba(0, 0, 255, 0.5);*/\n"
"/*border: 0.5px solid green;*/\n"
"/*border-style: inset;*/\n"
"}")
        self.groupBox_PCConf_AppSettings.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayout_42 = QVBoxLayout(self.groupBox_PCConf_AppSettings)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.widget_GraphicalDepth = QWidget(self.groupBox_PCConf_AppSettings)
        self.widget_GraphicalDepth.setObjectName(u"widget_GraphicalDepth")
        self.horizontalLayout_84 = QHBoxLayout(self.widget_GraphicalDepth)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(-1, 5, -1, 5)
        self.label_127 = QLabel(self.widget_GraphicalDepth)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setMinimumSize(QSize(0, 15))
        self.label_127.setMaximumSize(QSize(20, 20))
        self.label_127.setPixmap(QPixmap(u":/Logo/Dashboard/2-Sonde-clock/2-Time.svg"))
        self.label_127.setScaledContents(True)
        self.label_127.setMargin(0)

        self.horizontalLayout_84.addWidget(self.label_127)

        self.label_128 = QLabel(self.widget_GraphicalDepth)
        self.label_128.setObjectName(u"label_128")

        self.horizontalLayout_84.addWidget(self.label_128)

        self.label_Config_GraphDepth = QLabel(self.widget_GraphicalDepth)
        self.label_Config_GraphDepth.setObjectName(u"label_Config_GraphDepth")
        self.label_Config_GraphDepth.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_84.addWidget(self.label_Config_GraphDepth)

        self.label_129 = QLabel(self.widget_GraphicalDepth)
        self.label_129.setObjectName(u"label_129")
        sizePolicy.setHeightForWidth(self.label_129.sizePolicy().hasHeightForWidth())
        self.label_129.setSizePolicy(sizePolicy)
        self.label_129.setMinimumSize(QSize(0, 0))
        self.label_129.setMaximumSize(QSize(20, 20))
        self.label_129.setSizeIncrement(QSize(0, 0))
        self.label_129.setBaseSize(QSize(0, 0))
        self.label_129.setLayoutDirection(Qt.LeftToRight)
        self.label_129.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_129.setScaledContents(True)
        self.label_129.setAlignment(Qt.AlignCenter)
        self.label_129.setWordWrap(False)
        self.label_129.setMargin(0)

        self.horizontalLayout_84.addWidget(self.label_129)


        self.verticalLayout_42.addWidget(self.widget_GraphicalDepth)

        self.widget_Config_DisplayCalculated = QWidget(self.groupBox_PCConf_AppSettings)
        self.widget_Config_DisplayCalculated.setObjectName(u"widget_Config_DisplayCalculated")
        self.horizontalLayout_88 = QHBoxLayout(self.widget_Config_DisplayCalculated)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(-1, 5, -1, 5)
        self.label_135 = QLabel(self.widget_Config_DisplayCalculated)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setMinimumSize(QSize(0, 15))
        self.label_135.setMaximumSize(QSize(20, 20))
        self.label_135.setPixmap(QPixmap(u":/Logo/Dashboard/2-Sonde-clock/2-Time.svg"))
        self.label_135.setScaledContents(True)
        self.label_135.setMargin(0)

        self.horizontalLayout_88.addWidget(self.label_135)

        self.label_136 = QLabel(self.widget_Config_DisplayCalculated)
        self.label_136.setObjectName(u"label_136")

        self.horizontalLayout_88.addWidget(self.label_136)

        self.label_Config_DisplayCalculated = QLabel(self.widget_Config_DisplayCalculated)
        self.label_Config_DisplayCalculated.setObjectName(u"label_Config_DisplayCalculated")
        self.label_Config_DisplayCalculated.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_88.addWidget(self.label_Config_DisplayCalculated)

        self.label_137 = QLabel(self.widget_Config_DisplayCalculated)
        self.label_137.setObjectName(u"label_137")
        sizePolicy.setHeightForWidth(self.label_137.sizePolicy().hasHeightForWidth())
        self.label_137.setSizePolicy(sizePolicy)
        self.label_137.setMinimumSize(QSize(0, 0))
        self.label_137.setMaximumSize(QSize(20, 20))
        self.label_137.setSizeIncrement(QSize(0, 0))
        self.label_137.setBaseSize(QSize(0, 0))
        self.label_137.setLayoutDirection(Qt.LeftToRight)
        self.label_137.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_137.setScaledContents(True)
        self.label_137.setAlignment(Qt.AlignCenter)
        self.label_137.setWordWrap(False)
        self.label_137.setMargin(0)

        self.horizontalLayout_88.addWidget(self.label_137)


        self.verticalLayout_42.addWidget(self.widget_Config_DisplayCalculated)


        self.verticalLayout_43.addWidget(self.groupBox_PCConf_AppSettings)

        self.widget_49 = QWidget(self.widget_PCConfig_left)
        self.widget_49.setObjectName(u"widget_49")
        self.widget_49.setMinimumSize(QSize(0, 18))

        self.verticalLayout_43.addWidget(self.widget_49)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_43.addItem(self.verticalSpacer_10)


        self.horizontalLayout_85.addWidget(self.widget_PCConfig_left)

        self.widget_PCConfig_right = QWidget(self.page_6_PC_Config)
        self.widget_PCConfig_right.setObjectName(u"widget_PCConfig_right")
        sizePolicy4.setHeightForWidth(self.widget_PCConfig_right.sizePolicy().hasHeightForWidth())
        self.widget_PCConfig_right.setSizePolicy(sizePolicy4)
        self.widget_PCConfig_right.setLayoutDirection(Qt.RightToLeft)
        self.verticalLayout_44 = QVBoxLayout(self.widget_PCConfig_right)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(9, 18, 18, -1)
        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_44.addItem(self.verticalSpacer_11)


        self.horizontalLayout_85.addWidget(self.widget_PCConfig_right)

        self.horizontalLayout_85.setStretch(0, 1)
        self.horizontalLayout_85.setStretch(1, 1)
        self.stackedWidget.addWidget(self.page_6_PC_Config)
        self.page_8_DashboardLeveLine = QWidget()
        self.page_8_DashboardLeveLine.setObjectName(u"page_8_DashboardLeveLine")
        self.gridLayout_13 = QGridLayout(self.page_8_DashboardLeveLine)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.scrollArea_4 = QScrollArea(self.page_8_DashboardLeveLine)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 561, 700))
        self.verticalLayout_30 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.widget_29 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setMinimumSize(QSize(0, 700))
        self.horizontalLayout_59 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.widget_40 = QWidget(self.widget_29)
        self.widget_40.setObjectName(u"widget_40")
        self.widget_40.setMaximumSize(QSize(500, 16777215))
        self.verticalLayout_39 = QVBoxLayout(self.widget_40)
        self.verticalLayout_39.setSpacing(20)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.groupBox_SondeInfo_2 = QGroupBox(self.widget_40)
        self.groupBox_SondeInfo_2.setObjectName(u"groupBox_SondeInfo_2")
        sizePolicy3.setHeightForWidth(self.groupBox_SondeInfo_2.sizePolicy().hasHeightForWidth())
        self.groupBox_SondeInfo_2.setSizePolicy(sizePolicy3)
        self.groupBox_SondeInfo_2.setMinimumSize(QSize(0, 0))
        self.groupBox_SondeInfo_2.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_SondeInfo_2.setStyleSheet(u"Line{\n"
"/*background-color: rgba(0, 0, 0, 0.2);*/\n"
" /*color: rgba(0, 0, 255, 0.5);*/\n"
"/*border: 0.5px solid green;*/\n"
"/*border-style: inset;*/\n"
"}")
        self.groupBox_SondeInfo_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayout_45 = QVBoxLayout(self.groupBox_SondeInfo_2)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.widget_41 = QWidget(self.groupBox_SondeInfo_2)
        self.widget_41.setObjectName(u"widget_41")
        sizePolicy.setHeightForWidth(self.widget_41.sizePolicy().hasHeightForWidth())
        self.widget_41.setSizePolicy(sizePolicy)
        self.horizontalLayout_66 = QHBoxLayout(self.widget_41)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(-1, 5, 9, 5)
        self.label_16 = QLabel(self.widget_41)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QSize(0, 20))
        self.label_16.setMaximumSize(QSize(20, 20))
        self.label_16.setSizeIncrement(QSize(0, 0))
        self.label_16.setBaseSize(QSize(0, 0))
        self.label_16.setLayoutDirection(Qt.LeftToRight)
        self.label_16.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/1-Model.svg"))
        self.label_16.setScaledContents(True)
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_16.setWordWrap(False)
        self.label_16.setMargin(0)

        self.horizontalLayout_66.addWidget(self.label_16)

        self.label_txtModel_2 = QLabel(self.widget_41)
        self.label_txtModel_2.setObjectName(u"label_txtModel_2")

        self.horizontalLayout_66.addWidget(self.label_txtModel_2)

        self.label_Model_2 = QLabel(self.widget_41)
        self.label_Model_2.setObjectName(u"label_Model_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_Model_2.sizePolicy().hasHeightForWidth())
        self.label_Model_2.setSizePolicy(sizePolicy6)
        self.label_Model_2.setMinimumSize(QSize(0, 20))
        self.label_Model_2.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_66.addWidget(self.label_Model_2)

        self.label_84 = QLabel(self.widget_41)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label_84.sizePolicy().hasHeightForWidth())
        self.label_84.setSizePolicy(sizePolicy)
        self.label_84.setMinimumSize(QSize(0, 0))
        self.label_84.setMaximumSize(QSize(20, 20))
        self.label_84.setSizeIncrement(QSize(0, 0))
        self.label_84.setBaseSize(QSize(0, 0))
        self.label_84.setLayoutDirection(Qt.LeftToRight)
        self.label_84.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version - W.svg"))
        self.label_84.setScaledContents(True)
        self.label_84.setAlignment(Qt.AlignCenter)
        self.label_84.setWordWrap(False)
        self.label_84.setMargin(0)

        self.horizontalLayout_66.addWidget(self.label_84)


        self.verticalLayout_45.addWidget(self.widget_41)

        self.widget_51 = QWidget(self.groupBox_SondeInfo_2)
        self.widget_51.setObjectName(u"widget_51")
        self.horizontalLayout_91 = QHBoxLayout(self.widget_51)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(-1, 5, -1, 5)
        self.label_66 = QLabel(self.widget_51)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(0, 0))
        self.label_66.setMaximumSize(QSize(20, 20))
        self.label_66.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/7-Battery-voltage.svg"))
        self.label_66.setScaledContents(True)
        self.label_66.setMargin(0)

        self.horizontalLayout_91.addWidget(self.label_66)

        self.label_txtBatteryVoltage_2 = QLabel(self.widget_51)
        self.label_txtBatteryVoltage_2.setObjectName(u"label_txtBatteryVoltage_2")

        self.horizontalLayout_91.addWidget(self.label_txtBatteryVoltage_2)

        self.label_DepthRating = QLabel(self.widget_51)
        self.label_DepthRating.setObjectName(u"label_DepthRating")
        self.label_DepthRating.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_91.addWidget(self.label_DepthRating)

        self.label_95 = QLabel(self.widget_51)
        self.label_95.setObjectName(u"label_95")
        sizePolicy.setHeightForWidth(self.label_95.sizePolicy().hasHeightForWidth())
        self.label_95.setSizePolicy(sizePolicy)
        self.label_95.setMinimumSize(QSize(0, 0))
        self.label_95.setMaximumSize(QSize(20, 20))
        self.label_95.setSizeIncrement(QSize(0, 0))
        self.label_95.setBaseSize(QSize(0, 0))
        self.label_95.setLayoutDirection(Qt.LeftToRight)
        self.label_95.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version - W.svg"))
        self.label_95.setScaledContents(True)
        self.label_95.setAlignment(Qt.AlignCenter)
        self.label_95.setWordWrap(False)
        self.label_95.setMargin(0)

        self.horizontalLayout_91.addWidget(self.label_95)


        self.verticalLayout_45.addWidget(self.widget_51)

        self.widget_42 = QWidget(self.groupBox_SondeInfo_2)
        self.widget_42.setObjectName(u"widget_42")
        self.horizontalLayout_67 = QHBoxLayout(self.widget_42)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(-1, 5, -1, 5)
        self.label_36 = QLabel(self.widget_42)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(0, 15))
        self.label_36.setMaximumSize(QSize(18, 18))
        self.label_36.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/2-SN.svg"))
        self.label_36.setScaledContents(True)
        self.label_36.setMargin(0)

        self.horizontalLayout_67.addWidget(self.label_36)

        self.label_txtSN_2 = QLabel(self.widget_42)
        self.label_txtSN_2.setObjectName(u"label_txtSN_2")

        self.horizontalLayout_67.addWidget(self.label_txtSN_2)

        self.label_SerialNo_2 = QLabel(self.widget_42)
        self.label_SerialNo_2.setObjectName(u"label_SerialNo_2")
        self.label_SerialNo_2.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_67.addWidget(self.label_SerialNo_2)

        self.label_86 = QLabel(self.widget_42)
        self.label_86.setObjectName(u"label_86")
        sizePolicy.setHeightForWidth(self.label_86.sizePolicy().hasHeightForWidth())
        self.label_86.setSizePolicy(sizePolicy)
        self.label_86.setMinimumSize(QSize(0, 0))
        self.label_86.setMaximumSize(QSize(20, 20))
        self.label_86.setSizeIncrement(QSize(0, 0))
        self.label_86.setBaseSize(QSize(0, 0))
        self.label_86.setLayoutDirection(Qt.LeftToRight)
        self.label_86.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version - W.svg"))
        self.label_86.setScaledContents(True)
        self.label_86.setAlignment(Qt.AlignCenter)
        self.label_86.setWordWrap(False)
        self.label_86.setMargin(0)

        self.horizontalLayout_67.addWidget(self.label_86)


        self.verticalLayout_45.addWidget(self.widget_42)

        self.widget_SondeInfoInterface_2 = QWidget(self.groupBox_SondeInfo_2)
        self.widget_SondeInfoInterface_2.setObjectName(u"widget_SondeInfoInterface_2")
        self.horizontalLayout_68 = QHBoxLayout(self.widget_SondeInfoInterface_2)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(-1, 5, -1, 5)
        self.label_62 = QLabel(self.widget_SondeInfoInterface_2)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(0, 15))
        self.label_62.setMaximumSize(QSize(18, 18))
        self.label_62.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/Connected-sensor.svg"))
        self.label_62.setScaledContents(True)
        self.label_62.setMargin(0)

        self.horizontalLayout_68.addWidget(self.label_62)

        self.label_txtInterfaceCom_2 = QLabel(self.widget_SondeInfoInterface_2)
        self.label_txtInterfaceCom_2.setObjectName(u"label_txtInterfaceCom_2")

        self.horizontalLayout_68.addWidget(self.label_txtInterfaceCom_2)

        self.label_InterfaceCom_2 = QLabel(self.widget_SondeInfoInterface_2)
        self.label_InterfaceCom_2.setObjectName(u"label_InterfaceCom_2")
        self.label_InterfaceCom_2.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_68.addWidget(self.label_InterfaceCom_2)

        self.label_89 = QLabel(self.widget_SondeInfoInterface_2)
        self.label_89.setObjectName(u"label_89")
        sizePolicy.setHeightForWidth(self.label_89.sizePolicy().hasHeightForWidth())
        self.label_89.setSizePolicy(sizePolicy)
        self.label_89.setMinimumSize(QSize(0, 0))
        self.label_89.setMaximumSize(QSize(20, 20))
        self.label_89.setSizeIncrement(QSize(0, 0))
        self.label_89.setBaseSize(QSize(0, 0))
        self.label_89.setLayoutDirection(Qt.LeftToRight)
        self.label_89.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version - W.svg"))
        self.label_89.setScaledContents(True)
        self.label_89.setAlignment(Qt.AlignCenter)
        self.label_89.setWordWrap(False)
        self.label_89.setMargin(0)

        self.horizontalLayout_68.addWidget(self.label_89)


        self.verticalLayout_45.addWidget(self.widget_SondeInfoInterface_2)

        self.widget_43 = QWidget(self.groupBox_SondeInfo_2)
        self.widget_43.setObjectName(u"widget_43")
        self.horizontalLayout_69 = QHBoxLayout(self.widget_43)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(-1, 5, -1, 5)
        self.label_38 = QLabel(self.widget_43)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(0, 0))
        self.label_38.setMaximumSize(QSize(20, 20))
        self.label_38.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_38.setScaledContents(True)
        self.label_38.setMargin(0)

        self.horizontalLayout_69.addWidget(self.label_38)

        self.label_txtSWRev_2 = QLabel(self.widget_43)
        self.label_txtSWRev_2.setObjectName(u"label_txtSWRev_2")

        self.horizontalLayout_69.addWidget(self.label_txtSWRev_2)

        self.label_SWRev_2 = QLabel(self.widget_43)
        self.label_SWRev_2.setObjectName(u"label_SWRev_2")
        self.label_SWRev_2.setMinimumSize(QSize(0, 22))
        self.label_SWRev_2.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_69.addWidget(self.label_SWRev_2)

        self.label_90 = QLabel(self.widget_43)
        self.label_90.setObjectName(u"label_90")
        sizePolicy.setHeightForWidth(self.label_90.sizePolicy().hasHeightForWidth())
        self.label_90.setSizePolicy(sizePolicy)
        self.label_90.setMinimumSize(QSize(0, 0))
        self.label_90.setMaximumSize(QSize(20, 20))
        self.label_90.setSizeIncrement(QSize(0, 0))
        self.label_90.setBaseSize(QSize(0, 0))
        self.label_90.setLayoutDirection(Qt.LeftToRight)
        self.label_90.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version - W.svg"))
        self.label_90.setScaledContents(True)
        self.label_90.setAlignment(Qt.AlignCenter)
        self.label_90.setWordWrap(False)
        self.label_90.setMargin(0)

        self.horizontalLayout_69.addWidget(self.label_90)


        self.verticalLayout_45.addWidget(self.widget_43)

        self.widget_44 = QWidget(self.groupBox_SondeInfo_2)
        self.widget_44.setObjectName(u"widget_44")
        self.horizontalLayout_87 = QHBoxLayout(self.widget_44)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(-1, 5, -1, 5)
        self.label_63 = QLabel(self.widget_44)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(0, 0))
        self.label_63.setMaximumSize(QSize(20, 20))
        self.label_63.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/4-Records-stored.svg"))
        self.label_63.setScaledContents(True)
        self.label_63.setMargin(0)

        self.horizontalLayout_87.addWidget(self.label_63)

        self.label_txtRecordsStored_2 = QLabel(self.widget_44)
        self.label_txtRecordsStored_2.setObjectName(u"label_txtRecordsStored_2")

        self.horizontalLayout_87.addWidget(self.label_txtRecordsStored_2)

        self.label_RecordsStored_2 = QLabel(self.widget_44)
        self.label_RecordsStored_2.setObjectName(u"label_RecordsStored_2")
        self.label_RecordsStored_2.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_87.addWidget(self.label_RecordsStored_2)

        self.label_91 = QLabel(self.widget_44)
        self.label_91.setObjectName(u"label_91")
        sizePolicy.setHeightForWidth(self.label_91.sizePolicy().hasHeightForWidth())
        self.label_91.setSizePolicy(sizePolicy)
        self.label_91.setMinimumSize(QSize(0, 0))
        self.label_91.setMaximumSize(QSize(20, 20))
        self.label_91.setSizeIncrement(QSize(0, 0))
        self.label_91.setBaseSize(QSize(0, 0))
        self.label_91.setLayoutDirection(Qt.LeftToRight)
        self.label_91.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version - W.svg"))
        self.label_91.setScaledContents(True)
        self.label_91.setAlignment(Qt.AlignCenter)
        self.label_91.setWordWrap(False)
        self.label_91.setMargin(0)

        self.horizontalLayout_87.addWidget(self.label_91)


        self.verticalLayout_45.addWidget(self.widget_44)

        self.widget_50 = QWidget(self.groupBox_SondeInfo_2)
        self.widget_50.setObjectName(u"widget_50")
        self.horizontalLayout_89 = QHBoxLayout(self.widget_50)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(-1, 5, -1, 5)
        self.label_64 = QLabel(self.widget_50)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(0, 0))
        self.label_64.setMaximumSize(QSize(20, 20))
        self.label_64.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/5-Memory-card.svg"))
        self.label_64.setScaledContents(True)
        self.label_64.setMargin(0)

        self.horizontalLayout_89.addWidget(self.label_64)

        self.label_txtMemRemaining_2 = QLabel(self.widget_50)
        self.label_txtMemRemaining_2.setObjectName(u"label_txtMemRemaining_2")

        self.horizontalLayout_89.addWidget(self.label_txtMemRemaining_2)

        self.label_MemoryRemaining_2 = QLabel(self.widget_50)
        self.label_MemoryRemaining_2.setObjectName(u"label_MemoryRemaining_2")
        self.label_MemoryRemaining_2.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_89.addWidget(self.label_MemoryRemaining_2)

        self.label_92 = QLabel(self.widget_50)
        self.label_92.setObjectName(u"label_92")
        sizePolicy.setHeightForWidth(self.label_92.sizePolicy().hasHeightForWidth())
        self.label_92.setSizePolicy(sizePolicy)
        self.label_92.setMinimumSize(QSize(0, 0))
        self.label_92.setMaximumSize(QSize(20, 20))
        self.label_92.setSizeIncrement(QSize(0, 0))
        self.label_92.setBaseSize(QSize(0, 0))
        self.label_92.setLayoutDirection(Qt.LeftToRight)
        self.label_92.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version - W.svg"))
        self.label_92.setScaledContents(True)
        self.label_92.setAlignment(Qt.AlignCenter)
        self.label_92.setWordWrap(False)
        self.label_92.setMargin(0)

        self.horizontalLayout_89.addWidget(self.label_92)


        self.verticalLayout_45.addWidget(self.widget_50)

        self.widget_BatteryRemaining_2 = QWidget(self.groupBox_SondeInfo_2)
        self.widget_BatteryRemaining_2.setObjectName(u"widget_BatteryRemaining_2")
        self.horizontalLayout_90 = QHBoxLayout(self.widget_BatteryRemaining_2)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(-1, 5, -1, 5)
        self.label_65 = QLabel(self.widget_BatteryRemaining_2)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMinimumSize(QSize(0, 0))
        self.label_65.setMaximumSize(QSize(20, 20))
        self.label_65.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/6-Battery-remaining.svg"))
        self.label_65.setScaledContents(True)
        self.label_65.setMargin(0)

        self.horizontalLayout_90.addWidget(self.label_65)

        self.label_txtBatteryRemaining_2 = QLabel(self.widget_BatteryRemaining_2)
        self.label_txtBatteryRemaining_2.setObjectName(u"label_txtBatteryRemaining_2")

        self.horizontalLayout_90.addWidget(self.label_txtBatteryRemaining_2)

        self.label_BatteryRemaining_2 = QLabel(self.widget_BatteryRemaining_2)
        self.label_BatteryRemaining_2.setObjectName(u"label_BatteryRemaining_2")
        self.label_BatteryRemaining_2.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_90.addWidget(self.label_BatteryRemaining_2)

        self.label_93 = QLabel(self.widget_BatteryRemaining_2)
        self.label_93.setObjectName(u"label_93")
        sizePolicy.setHeightForWidth(self.label_93.sizePolicy().hasHeightForWidth())
        self.label_93.setSizePolicy(sizePolicy)
        self.label_93.setMinimumSize(QSize(0, 0))
        self.label_93.setMaximumSize(QSize(20, 20))
        self.label_93.setSizeIncrement(QSize(0, 0))
        self.label_93.setBaseSize(QSize(0, 0))
        self.label_93.setLayoutDirection(Qt.LeftToRight)
        self.label_93.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/info-button.svg"))
        self.label_93.setScaledContents(True)
        self.label_93.setAlignment(Qt.AlignCenter)
        self.label_93.setWordWrap(False)
        self.label_93.setMargin(0)

        self.horizontalLayout_90.addWidget(self.label_93)


        self.verticalLayout_45.addWidget(self.widget_BatteryRemaining_2)


        self.verticalLayout_39.addWidget(self.groupBox_SondeInfo_2)

        self.groupBox_SondeClock_2 = QGroupBox(self.widget_40)
        self.groupBox_SondeClock_2.setObjectName(u"groupBox_SondeClock_2")
        sizePolicy.setHeightForWidth(self.groupBox_SondeClock_2.sizePolicy().hasHeightForWidth())
        self.groupBox_SondeClock_2.setSizePolicy(sizePolicy)
        self.groupBox_SondeClock_2.setMinimumSize(QSize(0, 0))
        self.groupBox_SondeClock_2.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_SondeClock_2.setStyleSheet(u"Line{\n"
"/*background-color: rgba(0, 0, 0, 0.2);*/\n"
" /*color: rgba(0, 0, 255, 0.5);*/\n"
"/*border: 0.5px solid green;*/\n"
"/*border-style: inset;*/\n"
"}")
        self.groupBox_SondeClock_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayout_47 = QVBoxLayout(self.groupBox_SondeClock_2)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.widget_SondeDate_5 = QWidget(self.groupBox_SondeClock_2)
        self.widget_SondeDate_5.setObjectName(u"widget_SondeDate_5")
        self.horizontalLayout_94 = QHBoxLayout(self.widget_SondeDate_5)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(-1, 3, -1, 5)
        self.label_67 = QLabel(self.widget_SondeDate_5)
        self.label_67.setObjectName(u"label_67")
        sizePolicy.setHeightForWidth(self.label_67.sizePolicy().hasHeightForWidth())
        self.label_67.setSizePolicy(sizePolicy)
        self.label_67.setMinimumSize(QSize(0, 20))
        self.label_67.setMaximumSize(QSize(20, 20))
        self.label_67.setSizeIncrement(QSize(0, 0))
        self.label_67.setBaseSize(QSize(0, 0))
        self.label_67.setLayoutDirection(Qt.LeftToRight)
        self.label_67.setPixmap(QPixmap(u":/Logo/Dashboard/2-Sonde-clock/1-Date.svg"))
        self.label_67.setScaledContents(True)
        self.label_67.setAlignment(Qt.AlignCenter)
        self.label_67.setWordWrap(False)
        self.label_67.setMargin(0)

        self.horizontalLayout_94.addWidget(self.label_67)

        self.label_68 = QLabel(self.widget_SondeDate_5)
        self.label_68.setObjectName(u"label_68")

        self.horizontalLayout_94.addWidget(self.label_68)

        self.label_sondeClockDate_2 = QLabel(self.widget_SondeDate_5)
        self.label_sondeClockDate_2.setObjectName(u"label_sondeClockDate_2")
        self.label_sondeClockDate_2.setMinimumSize(QSize(0, 0))
        self.label_sondeClockDate_2.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_94.addWidget(self.label_sondeClockDate_2)

        self.label_setSondeClockDate_2 = QLabel(self.widget_SondeDate_5)
        self.label_setSondeClockDate_2.setObjectName(u"label_setSondeClockDate_2")
        sizePolicy.setHeightForWidth(self.label_setSondeClockDate_2.sizePolicy().hasHeightForWidth())
        self.label_setSondeClockDate_2.setSizePolicy(sizePolicy)
        self.label_setSondeClockDate_2.setMinimumSize(QSize(0, 0))
        self.label_setSondeClockDate_2.setMaximumSize(QSize(20, 20))
        self.label_setSondeClockDate_2.setSizeIncrement(QSize(0, 0))
        self.label_setSondeClockDate_2.setBaseSize(QSize(0, 0))
        self.label_setSondeClockDate_2.setLayoutDirection(Qt.LeftToRight)
        self.label_setSondeClockDate_2.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_setSondeClockDate_2.setScaledContents(True)
        self.label_setSondeClockDate_2.setAlignment(Qt.AlignCenter)
        self.label_setSondeClockDate_2.setWordWrap(False)
        self.label_setSondeClockDate_2.setMargin(0)

        self.horizontalLayout_94.addWidget(self.label_setSondeClockDate_2)


        self.verticalLayout_47.addWidget(self.widget_SondeDate_5)

        self.widget_SondeTime_2 = QWidget(self.groupBox_SondeClock_2)
        self.widget_SondeTime_2.setObjectName(u"widget_SondeTime_2")
        self.horizontalLayout_95 = QHBoxLayout(self.widget_SondeTime_2)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(-1, 5, -1, 5)
        self.label_134 = QLabel(self.widget_SondeTime_2)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setMinimumSize(QSize(0, 15))
        self.label_134.setMaximumSize(QSize(20, 20))
        self.label_134.setPixmap(QPixmap(u":/Logo/Dashboard/2-Sonde-clock/2-Time.svg"))
        self.label_134.setScaledContents(True)
        self.label_134.setMargin(0)

        self.horizontalLayout_95.addWidget(self.label_134)

        self.label_138 = QLabel(self.widget_SondeTime_2)
        self.label_138.setObjectName(u"label_138")

        self.horizontalLayout_95.addWidget(self.label_138)

        self.label_sondeClockTime_2 = QLabel(self.widget_SondeTime_2)
        self.label_sondeClockTime_2.setObjectName(u"label_sondeClockTime_2")
        self.label_sondeClockTime_2.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_95.addWidget(self.label_sondeClockTime_2)

        self.label_setSondeClockTime_2 = QLabel(self.widget_SondeTime_2)
        self.label_setSondeClockTime_2.setObjectName(u"label_setSondeClockTime_2")
        sizePolicy.setHeightForWidth(self.label_setSondeClockTime_2.sizePolicy().hasHeightForWidth())
        self.label_setSondeClockTime_2.setSizePolicy(sizePolicy)
        self.label_setSondeClockTime_2.setMinimumSize(QSize(0, 0))
        self.label_setSondeClockTime_2.setMaximumSize(QSize(20, 20))
        self.label_setSondeClockTime_2.setSizeIncrement(QSize(0, 0))
        self.label_setSondeClockTime_2.setBaseSize(QSize(0, 0))
        self.label_setSondeClockTime_2.setLayoutDirection(Qt.LeftToRight)
        self.label_setSondeClockTime_2.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_setSondeClockTime_2.setScaledContents(True)
        self.label_setSondeClockTime_2.setAlignment(Qt.AlignCenter)
        self.label_setSondeClockTime_2.setWordWrap(False)
        self.label_setSondeClockTime_2.setMargin(0)

        self.horizontalLayout_95.addWidget(self.label_setSondeClockTime_2)


        self.verticalLayout_47.addWidget(self.widget_SondeTime_2)


        self.verticalLayout_39.addWidget(self.groupBox_SondeClock_2)

        self.groupBox_SiteIDLocation_2 = QGroupBox(self.widget_40)
        self.groupBox_SiteIDLocation_2.setObjectName(u"groupBox_SiteIDLocation_2")
        self.groupBox_SiteIDLocation_2.setMinimumSize(QSize(0, 0))
        self.groupBox_SiteIDLocation_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayout_48 = QVBoxLayout(self.groupBox_SiteIDLocation_2)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.widget_SiteID_2 = QWidget(self.groupBox_SiteIDLocation_2)
        self.widget_SiteID_2.setObjectName(u"widget_SiteID_2")
        self.horizontalLayout_96 = QHBoxLayout(self.widget_SiteID_2)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(-1, 3, -1, 5)
        self.label_139 = QLabel(self.widget_SiteID_2)
        self.label_139.setObjectName(u"label_139")
        sizePolicy.setHeightForWidth(self.label_139.sizePolicy().hasHeightForWidth())
        self.label_139.setSizePolicy(sizePolicy)
        self.label_139.setMinimumSize(QSize(20, 20))
        self.label_139.setMaximumSize(QSize(15, 20))
        self.label_139.setSizeIncrement(QSize(0, 0))
        self.label_139.setBaseSize(QSize(0, 0))
        self.label_139.setLayoutDirection(Qt.LeftToRight)
        self.label_139.setPixmap(QPixmap(u":/Logo/Dashboard/3-Site-ID-And-Location/1-Model.svg"))
        self.label_139.setScaledContents(True)
        self.label_139.setAlignment(Qt.AlignCenter)
        self.label_139.setWordWrap(False)
        self.label_139.setMargin(0)

        self.horizontalLayout_96.addWidget(self.label_139)

        self.label_txtSiteID_2 = QLabel(self.widget_SiteID_2)
        self.label_txtSiteID_2.setObjectName(u"label_txtSiteID_2")

        self.horizontalLayout_96.addWidget(self.label_txtSiteID_2)

        self.label_SiteID_2 = QLabel(self.widget_SiteID_2)
        self.label_SiteID_2.setObjectName(u"label_SiteID_2")
        self.label_SiteID_2.setMinimumSize(QSize(0, 20))
        self.label_SiteID_2.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_96.addWidget(self.label_SiteID_2)

        self.label_setSiteID_2 = QLabel(self.widget_SiteID_2)
        self.label_setSiteID_2.setObjectName(u"label_setSiteID_2")
        sizePolicy.setHeightForWidth(self.label_setSiteID_2.sizePolicy().hasHeightForWidth())
        self.label_setSiteID_2.setSizePolicy(sizePolicy)
        self.label_setSiteID_2.setMinimumSize(QSize(0, 0))
        self.label_setSiteID_2.setMaximumSize(QSize(20, 20))
        self.label_setSiteID_2.setSizeIncrement(QSize(0, 0))
        self.label_setSiteID_2.setBaseSize(QSize(0, 0))
        self.label_setSiteID_2.setLayoutDirection(Qt.LeftToRight)
        self.label_setSiteID_2.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_setSiteID_2.setScaledContents(True)
        self.label_setSiteID_2.setAlignment(Qt.AlignCenter)
        self.label_setSiteID_2.setWordWrap(False)
        self.label_setSiteID_2.setMargin(0)

        self.horizontalLayout_96.addWidget(self.label_setSiteID_2)


        self.verticalLayout_48.addWidget(self.widget_SiteID_2)

        self.widget_SiteLatitude_2 = QWidget(self.groupBox_SiteIDLocation_2)
        self.widget_SiteLatitude_2.setObjectName(u"widget_SiteLatitude_2")
        self.horizontalLayout_97 = QHBoxLayout(self.widget_SiteLatitude_2)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalLayout_97.setContentsMargins(-1, 5, -1, 5)
        self.label_140 = QLabel(self.widget_SiteLatitude_2)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setMinimumSize(QSize(0, 0))
        self.label_140.setMaximumSize(QSize(20, 20))
        self.label_140.setPixmap(QPixmap(u":/Logo/Dashboard/3-Site-ID-And-Location/2-Site-lat.svg"))
        self.label_140.setScaledContents(True)
        self.label_140.setMargin(0)

        self.horizontalLayout_97.addWidget(self.label_140)

        self.label_txtSiteLat_2 = QLabel(self.widget_SiteLatitude_2)
        self.label_txtSiteLat_2.setObjectName(u"label_txtSiteLat_2")

        self.horizontalLayout_97.addWidget(self.label_txtSiteLat_2)

        self.label_SiteLat_2 = QLabel(self.widget_SiteLatitude_2)
        self.label_SiteLat_2.setObjectName(u"label_SiteLat_2")
        self.label_SiteLat_2.setMinimumSize(QSize(0, 20))
        self.label_SiteLat_2.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_97.addWidget(self.label_SiteLat_2)

        self.label_setSiteLatitude_2 = QLabel(self.widget_SiteLatitude_2)
        self.label_setSiteLatitude_2.setObjectName(u"label_setSiteLatitude_2")
        sizePolicy.setHeightForWidth(self.label_setSiteLatitude_2.sizePolicy().hasHeightForWidth())
        self.label_setSiteLatitude_2.setSizePolicy(sizePolicy)
        self.label_setSiteLatitude_2.setMinimumSize(QSize(0, 0))
        self.label_setSiteLatitude_2.setMaximumSize(QSize(20, 20))
        self.label_setSiteLatitude_2.setSizeIncrement(QSize(0, 0))
        self.label_setSiteLatitude_2.setBaseSize(QSize(0, 0))
        self.label_setSiteLatitude_2.setLayoutDirection(Qt.LeftToRight)
        self.label_setSiteLatitude_2.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_setSiteLatitude_2.setScaledContents(True)
        self.label_setSiteLatitude_2.setAlignment(Qt.AlignCenter)
        self.label_setSiteLatitude_2.setWordWrap(False)
        self.label_setSiteLatitude_2.setMargin(0)

        self.horizontalLayout_97.addWidget(self.label_setSiteLatitude_2)


        self.verticalLayout_48.addWidget(self.widget_SiteLatitude_2)

        self.widget_SiteLongitude_2 = QWidget(self.groupBox_SiteIDLocation_2)
        self.widget_SiteLongitude_2.setObjectName(u"widget_SiteLongitude_2")
        self.horizontalLayout_98 = QHBoxLayout(self.widget_SiteLongitude_2)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalLayout_98.setContentsMargins(-1, 5, -1, 5)
        self.label_141 = QLabel(self.widget_SiteLongitude_2)
        self.label_141.setObjectName(u"label_141")
        sizePolicy.setHeightForWidth(self.label_141.sizePolicy().hasHeightForWidth())
        self.label_141.setSizePolicy(sizePolicy)
        self.label_141.setMinimumSize(QSize(20, 20))
        self.label_141.setMaximumSize(QSize(15, 20))
        self.label_141.setSizeIncrement(QSize(0, 0))
        self.label_141.setBaseSize(QSize(0, 0))
        self.label_141.setLayoutDirection(Qt.LeftToRight)
        self.label_141.setPixmap(QPixmap(u":/Logo/Dashboard/3-Site-ID-And-Location/3-Site-long.svg"))
        self.label_141.setScaledContents(True)
        self.label_141.setAlignment(Qt.AlignCenter)
        self.label_141.setWordWrap(False)
        self.label_141.setMargin(0)

        self.horizontalLayout_98.addWidget(self.label_141)

        self.label_txtSiteLong_2 = QLabel(self.widget_SiteLongitude_2)
        self.label_txtSiteLong_2.setObjectName(u"label_txtSiteLong_2")

        self.horizontalLayout_98.addWidget(self.label_txtSiteLong_2)

        self.label_SiteLong_2 = QLabel(self.widget_SiteLongitude_2)
        self.label_SiteLong_2.setObjectName(u"label_SiteLong_2")
        self.label_SiteLong_2.setMinimumSize(QSize(0, 20))
        self.label_SiteLong_2.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_98.addWidget(self.label_SiteLong_2)

        self.label_setSiteLong_2 = QLabel(self.widget_SiteLongitude_2)
        self.label_setSiteLong_2.setObjectName(u"label_setSiteLong_2")
        sizePolicy.setHeightForWidth(self.label_setSiteLong_2.sizePolicy().hasHeightForWidth())
        self.label_setSiteLong_2.setSizePolicy(sizePolicy)
        self.label_setSiteLong_2.setMinimumSize(QSize(0, 0))
        self.label_setSiteLong_2.setMaximumSize(QSize(20, 20))
        self.label_setSiteLong_2.setSizeIncrement(QSize(0, 0))
        self.label_setSiteLong_2.setBaseSize(QSize(0, 0))
        self.label_setSiteLong_2.setLayoutDirection(Qt.LeftToRight)
        self.label_setSiteLong_2.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_setSiteLong_2.setScaledContents(True)
        self.label_setSiteLong_2.setAlignment(Qt.AlignCenter)
        self.label_setSiteLong_2.setWordWrap(False)
        self.label_setSiteLong_2.setMargin(0)

        self.horizontalLayout_98.addWidget(self.label_setSiteLong_2)


        self.verticalLayout_48.addWidget(self.widget_SiteLongitude_2)

        self.widget_SiteAltitude = QWidget(self.groupBox_SiteIDLocation_2)
        self.widget_SiteAltitude.setObjectName(u"widget_SiteAltitude")
        self.horizontalLayout_107 = QHBoxLayout(self.widget_SiteAltitude)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalLayout_107.setContentsMargins(-1, 5, -1, 5)
        self.label_148 = QLabel(self.widget_SiteAltitude)
        self.label_148.setObjectName(u"label_148")
        sizePolicy.setHeightForWidth(self.label_148.sizePolicy().hasHeightForWidth())
        self.label_148.setSizePolicy(sizePolicy)
        self.label_148.setMinimumSize(QSize(20, 20))
        self.label_148.setMaximumSize(QSize(15, 20))
        self.label_148.setSizeIncrement(QSize(0, 0))
        self.label_148.setBaseSize(QSize(0, 0))
        self.label_148.setLayoutDirection(Qt.LeftToRight)
        self.label_148.setPixmap(QPixmap(u":/Logo/Dashboard/3-Site-ID-And-Location/3-Site-long.svg"))
        self.label_148.setScaledContents(True)
        self.label_148.setAlignment(Qt.AlignCenter)
        self.label_148.setWordWrap(False)
        self.label_148.setMargin(0)

        self.horizontalLayout_107.addWidget(self.label_148)

        self.label_txtSiteLong_4 = QLabel(self.widget_SiteAltitude)
        self.label_txtSiteLong_4.setObjectName(u"label_txtSiteLong_4")

        self.horizontalLayout_107.addWidget(self.label_txtSiteLong_4)

        self.label_SiteAltitude = QLabel(self.widget_SiteAltitude)
        self.label_SiteAltitude.setObjectName(u"label_SiteAltitude")
        self.label_SiteAltitude.setMinimumSize(QSize(0, 20))
        self.label_SiteAltitude.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_107.addWidget(self.label_SiteAltitude)

        self.label_setSiteLong_4 = QLabel(self.widget_SiteAltitude)
        self.label_setSiteLong_4.setObjectName(u"label_setSiteLong_4")
        sizePolicy.setHeightForWidth(self.label_setSiteLong_4.sizePolicy().hasHeightForWidth())
        self.label_setSiteLong_4.setSizePolicy(sizePolicy)
        self.label_setSiteLong_4.setMinimumSize(QSize(0, 0))
        self.label_setSiteLong_4.setMaximumSize(QSize(20, 20))
        self.label_setSiteLong_4.setSizeIncrement(QSize(0, 0))
        self.label_setSiteLong_4.setBaseSize(QSize(0, 0))
        self.label_setSiteLong_4.setLayoutDirection(Qt.LeftToRight)
        self.label_setSiteLong_4.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_setSiteLong_4.setScaledContents(True)
        self.label_setSiteLong_4.setAlignment(Qt.AlignCenter)
        self.label_setSiteLong_4.setWordWrap(False)
        self.label_setSiteLong_4.setMargin(0)

        self.horizontalLayout_107.addWidget(self.label_setSiteLong_4)


        self.verticalLayout_48.addWidget(self.widget_SiteAltitude)


        self.verticalLayout_39.addWidget(self.groupBox_SiteIDLocation_2)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_39.addItem(self.verticalSpacer_13)


        self.horizontalLayout_59.addWidget(self.widget_40)

        self.widget_52 = QWidget(self.widget_29)
        self.widget_52.setObjectName(u"widget_52")
        self.widget_52.setMaximumSize(QSize(500, 16777215))
        self.verticalLayout_49 = QVBoxLayout(self.widget_52)
        self.verticalLayout_49.setSpacing(20)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.groupBox_DashboardSensors_2 = QGroupBox(self.widget_52)
        self.groupBox_DashboardSensors_2.setObjectName(u"groupBox_DashboardSensors_2")
        sizePolicy.setHeightForWidth(self.groupBox_DashboardSensors_2.sizePolicy().hasHeightForWidth())
        self.groupBox_DashboardSensors_2.setSizePolicy(sizePolicy)
        self.groupBox_DashboardSensors_2.setMinimumSize(QSize(0, 0))
        self.groupBox_DashboardSensors_2.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_DashboardSensors_2.setStyleSheet(u"Line{\n"
"/*background-color: rgba(0, 0, 0, 0.2);*/\n"
" /*color: rgba(0, 0, 255, 0.5);*/\n"
"/*border: 0.5px solid green;*/\n"
"/*border-style: inset;*/\n"
"}")
        self.groupBox_DashboardSensors_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayout_50 = QVBoxLayout(self.groupBox_DashboardSensors_2)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_49.addWidget(self.groupBox_DashboardSensors_2)

        self.groupBox_MeasurementStatus = QGroupBox(self.widget_52)
        self.groupBox_MeasurementStatus.setObjectName(u"groupBox_MeasurementStatus")
        sizePolicy.setHeightForWidth(self.groupBox_MeasurementStatus.sizePolicy().hasHeightForWidth())
        self.groupBox_MeasurementStatus.setSizePolicy(sizePolicy)
        self.groupBox_MeasurementStatus.setMinimumSize(QSize(0, 0))
        self.groupBox_MeasurementStatus.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_MeasurementStatus.setStyleSheet(u"Line{\n"
"/*background-color: rgba(0, 0, 0, 0.2);*/\n"
" /*color: rgba(0, 0, 255, 0.5);*/\n"
"/*border: 0.5px solid green;*/\n"
"/*border-style: inset;*/\n"
"}")
        self.groupBox_MeasurementStatus.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayout_53 = QVBoxLayout(self.groupBox_MeasurementStatus)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.widget_MeasStatus = QWidget(self.groupBox_MeasurementStatus)
        self.widget_MeasStatus.setObjectName(u"widget_MeasStatus")
        self.horizontalLayout_102 = QHBoxLayout(self.widget_MeasStatus)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.horizontalLayout_102.setContentsMargins(-1, 3, -1, 5)
        self.label_145 = QLabel(self.widget_MeasStatus)
        self.label_145.setObjectName(u"label_145")
        sizePolicy.setHeightForWidth(self.label_145.sizePolicy().hasHeightForWidth())
        self.label_145.setSizePolicy(sizePolicy)
        self.label_145.setMinimumSize(QSize(0, 0))
        self.label_145.setMaximumSize(QSize(20, 20))
        self.label_145.setSizeIncrement(QSize(0, 0))
        self.label_145.setBaseSize(QSize(0, 0))
        self.label_145.setLayoutDirection(Qt.LeftToRight)
        self.label_145.setPixmap(QPixmap(u":/Logo/Dashboard/5-Setup-logging-rate/3-Log-data-every.svg"))
        self.label_145.setScaledContents(True)
        self.label_145.setAlignment(Qt.AlignCenter)
        self.label_145.setWordWrap(False)
        self.label_145.setMargin(0)

        self.horizontalLayout_102.addWidget(self.label_145)

        self.label_txtLogDataEvery_3 = QLabel(self.widget_MeasStatus)
        self.label_txtLogDataEvery_3.setObjectName(u"label_txtLogDataEvery_3")

        self.horizontalLayout_102.addWidget(self.label_txtLogDataEvery_3)

        self.label_MeasStatusState = QLabel(self.widget_MeasStatus)
        self.label_MeasStatusState.setObjectName(u"label_MeasStatusState")
        self.label_MeasStatusState.setMinimumSize(QSize(0, 0))
        self.label_MeasStatusState.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_102.addWidget(self.label_MeasStatusState)

        self.label_setLogDataEvery_3 = QLabel(self.widget_MeasStatus)
        self.label_setLogDataEvery_3.setObjectName(u"label_setLogDataEvery_3")
        sizePolicy.setHeightForWidth(self.label_setLogDataEvery_3.sizePolicy().hasHeightForWidth())
        self.label_setLogDataEvery_3.setSizePolicy(sizePolicy)
        self.label_setLogDataEvery_3.setMinimumSize(QSize(0, 0))
        self.label_setLogDataEvery_3.setMaximumSize(QSize(20, 20))
        self.label_setLogDataEvery_3.setSizeIncrement(QSize(0, 0))
        self.label_setLogDataEvery_3.setBaseSize(QSize(0, 0))
        self.label_setLogDataEvery_3.setLayoutDirection(Qt.LeftToRight)
        self.label_setLogDataEvery_3.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version - W.svg"))
        self.label_setLogDataEvery_3.setScaledContents(True)
        self.label_setLogDataEvery_3.setAlignment(Qt.AlignCenter)
        self.label_setLogDataEvery_3.setWordWrap(False)
        self.label_setLogDataEvery_3.setMargin(0)

        self.horizontalLayout_102.addWidget(self.label_setLogDataEvery_3)


        self.verticalLayout_53.addWidget(self.widget_MeasStatus)

        self.widget_LogStartMode = QWidget(self.groupBox_MeasurementStatus)
        self.widget_LogStartMode.setObjectName(u"widget_LogStartMode")
        self.horizontalLayout_106 = QHBoxLayout(self.widget_LogStartMode)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.horizontalLayout_106.setContentsMargins(-1, 3, -1, 5)
        self.label_146 = QLabel(self.widget_LogStartMode)
        self.label_146.setObjectName(u"label_146")
        sizePolicy.setHeightForWidth(self.label_146.sizePolicy().hasHeightForWidth())
        self.label_146.setSizePolicy(sizePolicy)
        self.label_146.setMinimumSize(QSize(0, 0))
        self.label_146.setMaximumSize(QSize(20, 20))
        self.label_146.setSizeIncrement(QSize(0, 0))
        self.label_146.setBaseSize(QSize(0, 0))
        self.label_146.setLayoutDirection(Qt.LeftToRight)
        self.label_146.setPixmap(QPixmap(u":/Logo/Dashboard/5-Setup-logging-rate/2-Clean-every.svg"))
        self.label_146.setScaledContents(True)
        self.label_146.setAlignment(Qt.AlignCenter)
        self.label_146.setWordWrap(False)
        self.label_146.setMargin(0)

        self.horizontalLayout_106.addWidget(self.label_146)

        self.label_txtCleanEvery_4 = QLabel(self.widget_LogStartMode)
        self.label_txtCleanEvery_4.setObjectName(u"label_txtCleanEvery_4")
        self.label_txtCleanEvery_4.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_106.addWidget(self.label_txtCleanEvery_4)

        self.label_LogStartMode = QLabel(self.widget_LogStartMode)
        self.label_LogStartMode.setObjectName(u"label_LogStartMode")
        self.label_LogStartMode.setMinimumSize(QSize(0, 0))
        self.label_LogStartMode.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_106.addWidget(self.label_LogStartMode)

        self.label_setCleanEvery_4 = QLabel(self.widget_LogStartMode)
        self.label_setCleanEvery_4.setObjectName(u"label_setCleanEvery_4")
        sizePolicy.setHeightForWidth(self.label_setCleanEvery_4.sizePolicy().hasHeightForWidth())
        self.label_setCleanEvery_4.setSizePolicy(sizePolicy)
        self.label_setCleanEvery_4.setMinimumSize(QSize(0, 0))
        self.label_setCleanEvery_4.setMaximumSize(QSize(20, 20))
        self.label_setCleanEvery_4.setSizeIncrement(QSize(0, 0))
        self.label_setCleanEvery_4.setBaseSize(QSize(0, 0))
        self.label_setCleanEvery_4.setLayoutDirection(Qt.LeftToRight)
        self.label_setCleanEvery_4.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_setCleanEvery_4.setScaledContents(True)
        self.label_setCleanEvery_4.setAlignment(Qt.AlignCenter)
        self.label_setCleanEvery_4.setWordWrap(False)
        self.label_setCleanEvery_4.setMargin(0)

        self.horizontalLayout_106.addWidget(self.label_setCleanEvery_4)


        self.verticalLayout_53.addWidget(self.widget_LogStartMode)

        self.widget_LogDataStartAt = QWidget(self.groupBox_MeasurementStatus)
        self.widget_LogDataStartAt.setObjectName(u"widget_LogDataStartAt")
        self.horizontalLayout_113 = QHBoxLayout(self.widget_LogDataStartAt)
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.horizontalLayout_113.setContentsMargins(-1, 3, -1, 5)
        self.label_150 = QLabel(self.widget_LogDataStartAt)
        self.label_150.setObjectName(u"label_150")
        sizePolicy.setHeightForWidth(self.label_150.sizePolicy().hasHeightForWidth())
        self.label_150.setSizePolicy(sizePolicy)
        self.label_150.setMinimumSize(QSize(0, 0))
        self.label_150.setMaximumSize(QSize(20, 20))
        self.label_150.setSizeIncrement(QSize(0, 0))
        self.label_150.setBaseSize(QSize(0, 0))
        self.label_150.setLayoutDirection(Qt.LeftToRight)
        self.label_150.setPixmap(QPixmap(u":/Logo/Dashboard/5-Setup-logging-rate/2-Clean-every.svg"))
        self.label_150.setScaledContents(True)
        self.label_150.setAlignment(Qt.AlignCenter)
        self.label_150.setWordWrap(False)
        self.label_150.setMargin(0)

        self.horizontalLayout_113.addWidget(self.label_150)

        self.label_txtCleanEvery_8 = QLabel(self.widget_LogDataStartAt)
        self.label_txtCleanEvery_8.setObjectName(u"label_txtCleanEvery_8")
        self.label_txtCleanEvery_8.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_113.addWidget(self.label_txtCleanEvery_8)

        self.label_LogStartAt = QLabel(self.widget_LogDataStartAt)
        self.label_LogStartAt.setObjectName(u"label_LogStartAt")
        self.label_LogStartAt.setMinimumSize(QSize(0, 0))
        self.label_LogStartAt.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_113.addWidget(self.label_LogStartAt)

        self.label_setCleanEvery_8 = QLabel(self.widget_LogDataStartAt)
        self.label_setCleanEvery_8.setObjectName(u"label_setCleanEvery_8")
        sizePolicy.setHeightForWidth(self.label_setCleanEvery_8.sizePolicy().hasHeightForWidth())
        self.label_setCleanEvery_8.setSizePolicy(sizePolicy)
        self.label_setCleanEvery_8.setMinimumSize(QSize(0, 0))
        self.label_setCleanEvery_8.setMaximumSize(QSize(20, 20))
        self.label_setCleanEvery_8.setSizeIncrement(QSize(0, 0))
        self.label_setCleanEvery_8.setBaseSize(QSize(0, 0))
        self.label_setCleanEvery_8.setLayoutDirection(Qt.LeftToRight)
        self.label_setCleanEvery_8.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version - W.svg"))
        self.label_setCleanEvery_8.setScaledContents(True)
        self.label_setCleanEvery_8.setAlignment(Qt.AlignCenter)
        self.label_setCleanEvery_8.setWordWrap(False)
        self.label_setCleanEvery_8.setMargin(0)

        self.horizontalLayout_113.addWidget(self.label_setCleanEvery_8)


        self.verticalLayout_53.addWidget(self.widget_LogDataStartAt)

        self.widget_LogEndDateTime = QWidget(self.groupBox_MeasurementStatus)
        self.widget_LogEndDateTime.setObjectName(u"widget_LogEndDateTime")
        self.horizontalLayout_114 = QHBoxLayout(self.widget_LogEndDateTime)
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.horizontalLayout_114.setContentsMargins(-1, 3, -1, 5)
        self.label_154 = QLabel(self.widget_LogEndDateTime)
        self.label_154.setObjectName(u"label_154")
        sizePolicy.setHeightForWidth(self.label_154.sizePolicy().hasHeightForWidth())
        self.label_154.setSizePolicy(sizePolicy)
        self.label_154.setMinimumSize(QSize(0, 0))
        self.label_154.setMaximumSize(QSize(20, 20))
        self.label_154.setSizeIncrement(QSize(0, 0))
        self.label_154.setBaseSize(QSize(0, 0))
        self.label_154.setLayoutDirection(Qt.LeftToRight)
        self.label_154.setPixmap(QPixmap(u":/Logo/Dashboard/5-Setup-logging-rate/2-Clean-every.svg"))
        self.label_154.setScaledContents(True)
        self.label_154.setAlignment(Qt.AlignCenter)
        self.label_154.setWordWrap(False)
        self.label_154.setMargin(0)

        self.horizontalLayout_114.addWidget(self.label_154)

        self.label_txtCleanEvery_9 = QLabel(self.widget_LogEndDateTime)
        self.label_txtCleanEvery_9.setObjectName(u"label_txtCleanEvery_9")
        self.label_txtCleanEvery_9.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_114.addWidget(self.label_txtCleanEvery_9)

        self.label_LogEndDateTime = QLabel(self.widget_LogEndDateTime)
        self.label_LogEndDateTime.setObjectName(u"label_LogEndDateTime")
        self.label_LogEndDateTime.setMinimumSize(QSize(0, 0))
        self.label_LogEndDateTime.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_114.addWidget(self.label_LogEndDateTime)

        self.label_setCleanEvery_9 = QLabel(self.widget_LogEndDateTime)
        self.label_setCleanEvery_9.setObjectName(u"label_setCleanEvery_9")
        sizePolicy.setHeightForWidth(self.label_setCleanEvery_9.sizePolicy().hasHeightForWidth())
        self.label_setCleanEvery_9.setSizePolicy(sizePolicy)
        self.label_setCleanEvery_9.setMinimumSize(QSize(0, 0))
        self.label_setCleanEvery_9.setMaximumSize(QSize(20, 20))
        self.label_setCleanEvery_9.setSizeIncrement(QSize(0, 0))
        self.label_setCleanEvery_9.setBaseSize(QSize(0, 0))
        self.label_setCleanEvery_9.setLayoutDirection(Qt.LeftToRight)
        self.label_setCleanEvery_9.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version - W.svg"))
        self.label_setCleanEvery_9.setScaledContents(True)
        self.label_setCleanEvery_9.setAlignment(Qt.AlignCenter)
        self.label_setCleanEvery_9.setWordWrap(False)
        self.label_setCleanEvery_9.setMargin(0)

        self.horizontalLayout_114.addWidget(self.label_setCleanEvery_9)


        self.verticalLayout_53.addWidget(self.widget_LogEndDateTime)


        self.verticalLayout_49.addWidget(self.groupBox_MeasurementStatus)

        self.groupBox_SetupLogRate_2 = QGroupBox(self.widget_52)
        self.groupBox_SetupLogRate_2.setObjectName(u"groupBox_SetupLogRate_2")
        sizePolicy.setHeightForWidth(self.groupBox_SetupLogRate_2.sizePolicy().hasHeightForWidth())
        self.groupBox_SetupLogRate_2.setSizePolicy(sizePolicy)
        self.groupBox_SetupLogRate_2.setMinimumSize(QSize(0, 0))
        self.groupBox_SetupLogRate_2.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_SetupLogRate_2.setStyleSheet(u"Line{\n"
"/*background-color: rgba(0, 0, 0, 0.2);*/\n"
" /*color: rgba(0, 0, 255, 0.5);*/\n"
"/*border: 0.5px solid green;*/\n"
"/*border-style: inset;*/\n"
"}")
        self.groupBox_SetupLogRate_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayout_51 = QVBoxLayout(self.groupBox_SetupLogRate_2)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.widget_LogDataEvery_2 = QWidget(self.groupBox_SetupLogRate_2)
        self.widget_LogDataEvery_2.setObjectName(u"widget_LogDataEvery_2")
        self.horizontalLayout_99 = QHBoxLayout(self.widget_LogDataEvery_2)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalLayout_99.setContentsMargins(-1, 3, -1, 5)
        self.label_142 = QLabel(self.widget_LogDataEvery_2)
        self.label_142.setObjectName(u"label_142")
        sizePolicy.setHeightForWidth(self.label_142.sizePolicy().hasHeightForWidth())
        self.label_142.setSizePolicy(sizePolicy)
        self.label_142.setMinimumSize(QSize(0, 0))
        self.label_142.setMaximumSize(QSize(20, 20))
        self.label_142.setSizeIncrement(QSize(0, 0))
        self.label_142.setBaseSize(QSize(0, 0))
        self.label_142.setLayoutDirection(Qt.LeftToRight)
        self.label_142.setPixmap(QPixmap(u":/Logo/Dashboard/5-Setup-logging-rate/3-Log-data-every.svg"))
        self.label_142.setScaledContents(True)
        self.label_142.setAlignment(Qt.AlignCenter)
        self.label_142.setWordWrap(False)
        self.label_142.setMargin(0)

        self.horizontalLayout_99.addWidget(self.label_142)

        self.label_txtLogDataEvery_2 = QLabel(self.widget_LogDataEvery_2)
        self.label_txtLogDataEvery_2.setObjectName(u"label_txtLogDataEvery_2")

        self.horizontalLayout_99.addWidget(self.label_txtLogDataEvery_2)

        self.label_LogDataEvery_2 = QLabel(self.widget_LogDataEvery_2)
        self.label_LogDataEvery_2.setObjectName(u"label_LogDataEvery_2")
        self.label_LogDataEvery_2.setMinimumSize(QSize(0, 0))
        self.label_LogDataEvery_2.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_99.addWidget(self.label_LogDataEvery_2)

        self.label_setLogDataEvery_2 = QLabel(self.widget_LogDataEvery_2)
        self.label_setLogDataEvery_2.setObjectName(u"label_setLogDataEvery_2")
        sizePolicy.setHeightForWidth(self.label_setLogDataEvery_2.sizePolicy().hasHeightForWidth())
        self.label_setLogDataEvery_2.setSizePolicy(sizePolicy)
        self.label_setLogDataEvery_2.setMinimumSize(QSize(0, 0))
        self.label_setLogDataEvery_2.setMaximumSize(QSize(20, 20))
        self.label_setLogDataEvery_2.setSizeIncrement(QSize(0, 0))
        self.label_setLogDataEvery_2.setBaseSize(QSize(0, 0))
        self.label_setLogDataEvery_2.setLayoutDirection(Qt.LeftToRight)
        self.label_setLogDataEvery_2.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_setLogDataEvery_2.setScaledContents(True)
        self.label_setLogDataEvery_2.setAlignment(Qt.AlignCenter)
        self.label_setLogDataEvery_2.setWordWrap(False)
        self.label_setLogDataEvery_2.setMargin(0)

        self.horizontalLayout_99.addWidget(self.label_setLogDataEvery_2)


        self.verticalLayout_51.addWidget(self.widget_LogDataEvery_2)

        self.widget_LogDataFor = QWidget(self.groupBox_SetupLogRate_2)
        self.widget_LogDataFor.setObjectName(u"widget_LogDataFor")
        self.horizontalLayout_110 = QHBoxLayout(self.widget_LogDataFor)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.horizontalLayout_110.setContentsMargins(-1, 3, -1, 5)
        self.label_151 = QLabel(self.widget_LogDataFor)
        self.label_151.setObjectName(u"label_151")
        sizePolicy.setHeightForWidth(self.label_151.sizePolicy().hasHeightForWidth())
        self.label_151.setSizePolicy(sizePolicy)
        self.label_151.setMinimumSize(QSize(0, 0))
        self.label_151.setMaximumSize(QSize(20, 20))
        self.label_151.setSizeIncrement(QSize(0, 0))
        self.label_151.setBaseSize(QSize(0, 0))
        self.label_151.setLayoutDirection(Qt.LeftToRight)
        self.label_151.setPixmap(QPixmap(u":/Logo/Dashboard/5-Setup-logging-rate/2-Clean-every.svg"))
        self.label_151.setScaledContents(True)
        self.label_151.setAlignment(Qt.AlignCenter)
        self.label_151.setWordWrap(False)
        self.label_151.setMargin(0)

        self.horizontalLayout_110.addWidget(self.label_151)

        self.label_txtCleanEvery_5 = QLabel(self.widget_LogDataFor)
        self.label_txtCleanEvery_5.setObjectName(u"label_txtCleanEvery_5")
        self.label_txtCleanEvery_5.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_110.addWidget(self.label_txtCleanEvery_5)

        self.label_LogDataFor = QLabel(self.widget_LogDataFor)
        self.label_LogDataFor.setObjectName(u"label_LogDataFor")
        self.label_LogDataFor.setMinimumSize(QSize(0, 0))
        self.label_LogDataFor.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_110.addWidget(self.label_LogDataFor)

        self.label_setCleanEvery_5 = QLabel(self.widget_LogDataFor)
        self.label_setCleanEvery_5.setObjectName(u"label_setCleanEvery_5")
        sizePolicy.setHeightForWidth(self.label_setCleanEvery_5.sizePolicy().hasHeightForWidth())
        self.label_setCleanEvery_5.setSizePolicy(sizePolicy)
        self.label_setCleanEvery_5.setMinimumSize(QSize(0, 0))
        self.label_setCleanEvery_5.setMaximumSize(QSize(20, 20))
        self.label_setCleanEvery_5.setSizeIncrement(QSize(0, 0))
        self.label_setCleanEvery_5.setBaseSize(QSize(0, 0))
        self.label_setCleanEvery_5.setLayoutDirection(Qt.LeftToRight)
        self.label_setCleanEvery_5.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_setCleanEvery_5.setScaledContents(True)
        self.label_setCleanEvery_5.setAlignment(Qt.AlignCenter)
        self.label_setCleanEvery_5.setWordWrap(False)
        self.label_setCleanEvery_5.setMargin(0)

        self.horizontalLayout_110.addWidget(self.label_setCleanEvery_5)


        self.verticalLayout_51.addWidget(self.widget_LogDataFor)


        self.verticalLayout_49.addWidget(self.groupBox_SetupLogRate_2)

        self.groupBox_EventLogging_2 = QGroupBox(self.widget_52)
        self.groupBox_EventLogging_2.setObjectName(u"groupBox_EventLogging_2")
        sizePolicy.setHeightForWidth(self.groupBox_EventLogging_2.sizePolicy().hasHeightForWidth())
        self.groupBox_EventLogging_2.setSizePolicy(sizePolicy)
        self.groupBox_EventLogging_2.setMinimumSize(QSize(0, 0))
        self.groupBox_EventLogging_2.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_EventLogging_2.setStyleSheet(u"Line{\n"
"/*background-color: rgba(0, 0, 0, 0.2);*/\n"
" /*color: rgba(0, 0, 255, 0.5);*/\n"
"/*border: 0.5px solid green;*/\n"
"/*border-style: inset;*/\n"
"}")
        self.groupBox_EventLogging_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayout_52 = QVBoxLayout(self.groupBox_EventLogging_2)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.widget_EventLogState_2 = QWidget(self.groupBox_EventLogging_2)
        self.widget_EventLogState_2.setObjectName(u"widget_EventLogState_2")
        self.horizontalLayout_101 = QHBoxLayout(self.widget_EventLogState_2)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_101.setContentsMargins(-1, 3, -1, 5)
        self.label_144 = QLabel(self.widget_EventLogState_2)
        self.label_144.setObjectName(u"label_144")
        sizePolicy.setHeightForWidth(self.label_144.sizePolicy().hasHeightForWidth())
        self.label_144.setSizePolicy(sizePolicy)
        self.label_144.setMinimumSize(QSize(0, 0))
        self.label_144.setMaximumSize(QSize(20, 20))
        self.label_144.setSizeIncrement(QSize(0, 0))
        self.label_144.setBaseSize(QSize(0, 0))
        self.label_144.setLayoutDirection(Qt.LeftToRight)
        self.label_144.setPixmap(QPixmap(u":/Logo/Dashboard/7-Event-logging/1-State.svg"))
        self.label_144.setScaledContents(True)
        self.label_144.setAlignment(Qt.AlignCenter)
        self.label_144.setWordWrap(False)
        self.label_144.setMargin(0)

        self.horizontalLayout_101.addWidget(self.label_144)

        self.label_txtEventLogState_2 = QLabel(self.widget_EventLogState_2)
        self.label_txtEventLogState_2.setObjectName(u"label_txtEventLogState_2")

        self.horizontalLayout_101.addWidget(self.label_txtEventLogState_2)

        self.label_EventLogState_2 = QLabel(self.widget_EventLogState_2)
        self.label_EventLogState_2.setObjectName(u"label_EventLogState_2")
        self.label_EventLogState_2.setMinimumSize(QSize(0, 0))
        self.label_EventLogState_2.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_101.addWidget(self.label_EventLogState_2)

        self.label_setEventLogState_2 = QLabel(self.widget_EventLogState_2)
        self.label_setEventLogState_2.setObjectName(u"label_setEventLogState_2")
        sizePolicy.setHeightForWidth(self.label_setEventLogState_2.sizePolicy().hasHeightForWidth())
        self.label_setEventLogState_2.setSizePolicy(sizePolicy)
        self.label_setEventLogState_2.setMinimumSize(QSize(0, 0))
        self.label_setEventLogState_2.setMaximumSize(QSize(20, 20))
        self.label_setEventLogState_2.setSizeIncrement(QSize(0, 0))
        self.label_setEventLogState_2.setBaseSize(QSize(0, 0))
        self.label_setEventLogState_2.setLayoutDirection(Qt.LeftToRight)
        self.label_setEventLogState_2.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_setEventLogState_2.setScaledContents(True)
        self.label_setEventLogState_2.setAlignment(Qt.AlignCenter)
        self.label_setEventLogState_2.setWordWrap(False)
        self.label_setEventLogState_2.setMargin(0)

        self.horizontalLayout_101.addWidget(self.label_setEventLogState_2)


        self.verticalLayout_52.addWidget(self.widget_EventLogState_2)

        self.widget_EventLogEvery_2 = QWidget(self.groupBox_EventLogging_2)
        self.widget_EventLogEvery_2.setObjectName(u"widget_EventLogEvery_2")
        self.horizontalLayout_103 = QHBoxLayout(self.widget_EventLogEvery_2)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.horizontalLayout_103.setContentsMargins(-1, 3, -1, 5)
        self.label_logoEventLogEvery_2 = QLabel(self.widget_EventLogEvery_2)
        self.label_logoEventLogEvery_2.setObjectName(u"label_logoEventLogEvery_2")
        sizePolicy.setHeightForWidth(self.label_logoEventLogEvery_2.sizePolicy().hasHeightForWidth())
        self.label_logoEventLogEvery_2.setSizePolicy(sizePolicy)
        self.label_logoEventLogEvery_2.setMinimumSize(QSize(0, 0))
        self.label_logoEventLogEvery_2.setMaximumSize(QSize(20, 20))
        self.label_logoEventLogEvery_2.setSizeIncrement(QSize(0, 0))
        self.label_logoEventLogEvery_2.setBaseSize(QSize(0, 0))
        self.label_logoEventLogEvery_2.setLayoutDirection(Qt.LeftToRight)
        self.label_logoEventLogEvery_2.setPixmap(QPixmap(u":/Logo/Dashboard/7-Event-logging/3-Every.svg"))
        self.label_logoEventLogEvery_2.setScaledContents(True)
        self.label_logoEventLogEvery_2.setAlignment(Qt.AlignCenter)
        self.label_logoEventLogEvery_2.setWordWrap(False)
        self.label_logoEventLogEvery_2.setMargin(0)

        self.horizontalLayout_103.addWidget(self.label_logoEventLogEvery_2)

        self.label_txtEventLogEvery_2 = QLabel(self.widget_EventLogEvery_2)
        self.label_txtEventLogEvery_2.setObjectName(u"label_txtEventLogEvery_2")

        self.horizontalLayout_103.addWidget(self.label_txtEventLogEvery_2)

        self.label_EventLogEvery_2 = QLabel(self.widget_EventLogEvery_2)
        self.label_EventLogEvery_2.setObjectName(u"label_EventLogEvery_2")
        self.label_EventLogEvery_2.setMinimumSize(QSize(0, 0))
        self.label_EventLogEvery_2.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_103.addWidget(self.label_EventLogEvery_2)

        self.label_setEventLogEvery_2 = QLabel(self.widget_EventLogEvery_2)
        self.label_setEventLogEvery_2.setObjectName(u"label_setEventLogEvery_2")
        sizePolicy.setHeightForWidth(self.label_setEventLogEvery_2.sizePolicy().hasHeightForWidth())
        self.label_setEventLogEvery_2.setSizePolicy(sizePolicy)
        self.label_setEventLogEvery_2.setMinimumSize(QSize(0, 0))
        self.label_setEventLogEvery_2.setMaximumSize(QSize(20, 20))
        self.label_setEventLogEvery_2.setSizeIncrement(QSize(0, 0))
        self.label_setEventLogEvery_2.setBaseSize(QSize(0, 0))
        self.label_setEventLogEvery_2.setLayoutDirection(Qt.LeftToRight)
        self.label_setEventLogEvery_2.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_setEventLogEvery_2.setScaledContents(True)
        self.label_setEventLogEvery_2.setAlignment(Qt.AlignCenter)
        self.label_setEventLogEvery_2.setWordWrap(False)
        self.label_setEventLogEvery_2.setMargin(0)

        self.horizontalLayout_103.addWidget(self.label_setEventLogEvery_2)


        self.verticalLayout_52.addWidget(self.widget_EventLogEvery_2)

        self.widget_EventLogLimitTxt = QWidget(self.groupBox_EventLogging_2)
        self.widget_EventLogLimitTxt.setObjectName(u"widget_EventLogLimitTxt")
        self.horizontalLayout_92 = QHBoxLayout(self.widget_EventLogLimitTxt)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.label_17 = QLabel(self.widget_EventLogLimitTxt)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_92.addWidget(self.label_17)


        self.verticalLayout_52.addWidget(self.widget_EventLogLimitTxt)

        self.widget_EventLogLevelValue = QWidget(self.groupBox_EventLogging_2)
        self.widget_EventLogLevelValue.setObjectName(u"widget_EventLogLevelValue")
        self.horizontalLayout_104 = QHBoxLayout(self.widget_EventLogLevelValue)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.horizontalLayout_104.setContentsMargins(-1, 3, -1, 5)
        self.label_logoEventLogLevelValue = QLabel(self.widget_EventLogLevelValue)
        self.label_logoEventLogLevelValue.setObjectName(u"label_logoEventLogLevelValue")
        sizePolicy.setHeightForWidth(self.label_logoEventLogLevelValue.sizePolicy().hasHeightForWidth())
        self.label_logoEventLogLevelValue.setSizePolicy(sizePolicy)
        self.label_logoEventLogLevelValue.setMinimumSize(QSize(0, 0))
        self.label_logoEventLogLevelValue.setMaximumSize(QSize(20, 20))
        self.label_logoEventLogLevelValue.setSizeIncrement(QSize(0, 0))
        self.label_logoEventLogLevelValue.setBaseSize(QSize(0, 0))
        self.label_logoEventLogLevelValue.setLayoutDirection(Qt.LeftToRight)
        self.label_logoEventLogLevelValue.setPixmap(QPixmap(u":/Logo/Dashboard/7-Event-logging/4-Log-data-if.svg"))
        self.label_logoEventLogLevelValue.setScaledContents(True)
        self.label_logoEventLogLevelValue.setAlignment(Qt.AlignCenter)
        self.label_logoEventLogLevelValue.setWordWrap(False)
        self.label_logoEventLogLevelValue.setMargin(0)

        self.horizontalLayout_104.addWidget(self.label_logoEventLogLevelValue)

        self.label_txtEventLogLevelValue = QLabel(self.widget_EventLogLevelValue)
        self.label_txtEventLogLevelValue.setObjectName(u"label_txtEventLogLevelValue")
        self.label_txtEventLogLevelValue.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_104.addWidget(self.label_txtEventLogLevelValue)

        self.label_EventLogLevelValue = QLabel(self.widget_EventLogLevelValue)
        self.label_EventLogLevelValue.setObjectName(u"label_EventLogLevelValue")
        self.label_EventLogLevelValue.setMinimumSize(QSize(0, 0))
        self.label_EventLogLevelValue.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_104.addWidget(self.label_EventLogLevelValue)

        self.label_setEventLogLevelValue = QLabel(self.widget_EventLogLevelValue)
        self.label_setEventLogLevelValue.setObjectName(u"label_setEventLogLevelValue")
        sizePolicy.setHeightForWidth(self.label_setEventLogLevelValue.sizePolicy().hasHeightForWidth())
        self.label_setEventLogLevelValue.setSizePolicy(sizePolicy)
        self.label_setEventLogLevelValue.setMinimumSize(QSize(0, 0))
        self.label_setEventLogLevelValue.setMaximumSize(QSize(20, 20))
        self.label_setEventLogLevelValue.setSizeIncrement(QSize(0, 0))
        self.label_setEventLogLevelValue.setBaseSize(QSize(0, 0))
        self.label_setEventLogLevelValue.setLayoutDirection(Qt.LeftToRight)
        self.label_setEventLogLevelValue.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_setEventLogLevelValue.setScaledContents(True)
        self.label_setEventLogLevelValue.setAlignment(Qt.AlignCenter)
        self.label_setEventLogLevelValue.setWordWrap(False)
        self.label_setEventLogLevelValue.setMargin(0)

        self.horizontalLayout_104.addWidget(self.label_setEventLogLevelValue)


        self.verticalLayout_52.addWidget(self.widget_EventLogLevelValue)

        self.widget_EventLogTemperatureValue = QWidget(self.groupBox_EventLogging_2)
        self.widget_EventLogTemperatureValue.setObjectName(u"widget_EventLogTemperatureValue")
        self.horizontalLayout_105 = QHBoxLayout(self.widget_EventLogTemperatureValue)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.horizontalLayout_105.setContentsMargins(-1, 3, -1, 5)
        self.label_logoEventLogTemperatureValue = QLabel(self.widget_EventLogTemperatureValue)
        self.label_logoEventLogTemperatureValue.setObjectName(u"label_logoEventLogTemperatureValue")
        sizePolicy.setHeightForWidth(self.label_logoEventLogTemperatureValue.sizePolicy().hasHeightForWidth())
        self.label_logoEventLogTemperatureValue.setSizePolicy(sizePolicy)
        self.label_logoEventLogTemperatureValue.setMinimumSize(QSize(0, 0))
        self.label_logoEventLogTemperatureValue.setMaximumSize(QSize(20, 20))
        self.label_logoEventLogTemperatureValue.setSizeIncrement(QSize(0, 0))
        self.label_logoEventLogTemperatureValue.setBaseSize(QSize(0, 0))
        self.label_logoEventLogTemperatureValue.setLayoutDirection(Qt.LeftToRight)
        self.label_logoEventLogTemperatureValue.setPixmap(QPixmap(u":/Logo/Dashboard/7-Event-logging/4-Log-data-if.svg"))
        self.label_logoEventLogTemperatureValue.setScaledContents(True)
        self.label_logoEventLogTemperatureValue.setAlignment(Qt.AlignCenter)
        self.label_logoEventLogTemperatureValue.setWordWrap(False)
        self.label_logoEventLogTemperatureValue.setMargin(0)

        self.horizontalLayout_105.addWidget(self.label_logoEventLogTemperatureValue)

        self.label_txtEventLogTemperatureValue = QLabel(self.widget_EventLogTemperatureValue)
        self.label_txtEventLogTemperatureValue.setObjectName(u"label_txtEventLogTemperatureValue")
        self.label_txtEventLogTemperatureValue.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_105.addWidget(self.label_txtEventLogTemperatureValue)

        self.label_EventLogTemperatureValue = QLabel(self.widget_EventLogTemperatureValue)
        self.label_EventLogTemperatureValue.setObjectName(u"label_EventLogTemperatureValue")
        self.label_EventLogTemperatureValue.setMinimumSize(QSize(0, 0))
        self.label_EventLogTemperatureValue.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_105.addWidget(self.label_EventLogTemperatureValue)

        self.label_setEventLogTemperatureValue = QLabel(self.widget_EventLogTemperatureValue)
        self.label_setEventLogTemperatureValue.setObjectName(u"label_setEventLogTemperatureValue")
        sizePolicy.setHeightForWidth(self.label_setEventLogTemperatureValue.sizePolicy().hasHeightForWidth())
        self.label_setEventLogTemperatureValue.setSizePolicy(sizePolicy)
        self.label_setEventLogTemperatureValue.setMinimumSize(QSize(0, 0))
        self.label_setEventLogTemperatureValue.setMaximumSize(QSize(20, 20))
        self.label_setEventLogTemperatureValue.setSizeIncrement(QSize(0, 0))
        self.label_setEventLogTemperatureValue.setBaseSize(QSize(0, 0))
        self.label_setEventLogTemperatureValue.setLayoutDirection(Qt.LeftToRight)
        self.label_setEventLogTemperatureValue.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_setEventLogTemperatureValue.setScaledContents(True)
        self.label_setEventLogTemperatureValue.setAlignment(Qt.AlignCenter)
        self.label_setEventLogTemperatureValue.setWordWrap(False)
        self.label_setEventLogTemperatureValue.setMargin(0)

        self.horizontalLayout_105.addWidget(self.label_setEventLogTemperatureValue)


        self.verticalLayout_52.addWidget(self.widget_EventLogTemperatureValue)

        self.widget_EventLogSalinityValue = QWidget(self.groupBox_EventLogging_2)
        self.widget_EventLogSalinityValue.setObjectName(u"widget_EventLogSalinityValue")
        self.horizontalLayout_109 = QHBoxLayout(self.widget_EventLogSalinityValue)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.horizontalLayout_109.setContentsMargins(-1, 3, -1, 5)
        self.label_logoEventLogSalinityValue = QLabel(self.widget_EventLogSalinityValue)
        self.label_logoEventLogSalinityValue.setObjectName(u"label_logoEventLogSalinityValue")
        sizePolicy.setHeightForWidth(self.label_logoEventLogSalinityValue.sizePolicy().hasHeightForWidth())
        self.label_logoEventLogSalinityValue.setSizePolicy(sizePolicy)
        self.label_logoEventLogSalinityValue.setMinimumSize(QSize(0, 0))
        self.label_logoEventLogSalinityValue.setMaximumSize(QSize(20, 20))
        self.label_logoEventLogSalinityValue.setSizeIncrement(QSize(0, 0))
        self.label_logoEventLogSalinityValue.setBaseSize(QSize(0, 0))
        self.label_logoEventLogSalinityValue.setLayoutDirection(Qt.LeftToRight)
        self.label_logoEventLogSalinityValue.setPixmap(QPixmap(u":/Logo/Dashboard/7-Event-logging/4-Log-data-if.svg"))
        self.label_logoEventLogSalinityValue.setScaledContents(True)
        self.label_logoEventLogSalinityValue.setAlignment(Qt.AlignCenter)
        self.label_logoEventLogSalinityValue.setWordWrap(False)
        self.label_logoEventLogSalinityValue.setMargin(0)

        self.horizontalLayout_109.addWidget(self.label_logoEventLogSalinityValue)

        self.label_txtEventLogSalinityValue = QLabel(self.widget_EventLogSalinityValue)
        self.label_txtEventLogSalinityValue.setObjectName(u"label_txtEventLogSalinityValue")
        self.label_txtEventLogSalinityValue.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_109.addWidget(self.label_txtEventLogSalinityValue)

        self.label_EventLogSalinityValue = QLabel(self.widget_EventLogSalinityValue)
        self.label_EventLogSalinityValue.setObjectName(u"label_EventLogSalinityValue")
        self.label_EventLogSalinityValue.setMinimumSize(QSize(0, 0))
        self.label_EventLogSalinityValue.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_109.addWidget(self.label_EventLogSalinityValue)

        self.label_setEventLogSalinityValue = QLabel(self.widget_EventLogSalinityValue)
        self.label_setEventLogSalinityValue.setObjectName(u"label_setEventLogSalinityValue")
        sizePolicy.setHeightForWidth(self.label_setEventLogSalinityValue.sizePolicy().hasHeightForWidth())
        self.label_setEventLogSalinityValue.setSizePolicy(sizePolicy)
        self.label_setEventLogSalinityValue.setMinimumSize(QSize(0, 0))
        self.label_setEventLogSalinityValue.setMaximumSize(QSize(20, 20))
        self.label_setEventLogSalinityValue.setSizeIncrement(QSize(0, 0))
        self.label_setEventLogSalinityValue.setBaseSize(QSize(0, 0))
        self.label_setEventLogSalinityValue.setLayoutDirection(Qt.LeftToRight)
        self.label_setEventLogSalinityValue.setPixmap(QPixmap(u":/Logo/Dashboard/Sonde info/3-Software-version.svg"))
        self.label_setEventLogSalinityValue.setScaledContents(True)
        self.label_setEventLogSalinityValue.setAlignment(Qt.AlignCenter)
        self.label_setEventLogSalinityValue.setWordWrap(False)
        self.label_setEventLogSalinityValue.setMargin(0)

        self.horizontalLayout_109.addWidget(self.label_setEventLogSalinityValue)


        self.verticalLayout_52.addWidget(self.widget_EventLogSalinityValue)


        self.verticalLayout_49.addWidget(self.groupBox_EventLogging_2)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_49.addItem(self.verticalSpacer_14)


        self.horizontalLayout_59.addWidget(self.widget_52)

        self.horizontalSpacer_11 = QSpacerItem(0, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_11)

        self.horizontalLayout_59.setStretch(0, 300)
        self.horizontalLayout_59.setStretch(1, 300)

        self.verticalLayout_30.addWidget(self.widget_29)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_13.addWidget(self.scrollArea_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_8_DashboardLeveLine)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_3.addWidget(self.widget_2)


        self.gridLayout_8.addWidget(self.body, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1060, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.stackedWidget_Nav2.setCurrentIndex(7)
        self.clearSondeMem_btn.setDefault(False)
        self.newBatteryFitted_btn.setDefault(False)
        self.resyncClockWithPC_btn.setDefault(False)
        self.startMeasure_btn.setDefault(False)
        self.stopMeasure_btn.setDefault(False)
        self.clearMeasure_btn.setDefault(False)
        self.getMeasureData_btn.setDefault(False)
        self.cleanSonde_btn.setDefault(False)
        self.exportToPdf_btn.setDefault(False)
        self.exportToTxt_btn.setDefault(False)
        self.rapidCal_btn.setDefault(False)
        self.clearSondeMem_btn_2.setDefault(False)
        self.resetLeveLine_btn_2.setDefault(False)
        self.resyncClockWithPC_btn_2.setDefault(False)
        self.startProductLeveLine_btn.setDefault(False)
        self.setBaroCal_btn.setDefault(False)
        self.clearGraphCal_btn.setDefault(False)
        self.stackedWidget.setCurrentIndex(4)
        self.stackedWidget_DataTabChart.setCurrentIndex(0)
        self.stackedWidget_calibrationMain.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ProLink", None))
        self.toggle_button.setText("")
        self.clearSondeMem_btn.setText(QCoreApplication.translate("MainWindow", u"Clear \n"
"memory", None))
        self.newBatteryFitted_btn.setText(QCoreApplication.translate("MainWindow", u"New battery \n"
"fitted", None))
        self.resyncClockWithPC_btn.setText(QCoreApplication.translate("MainWindow", u"Resync clock \n"
"with PC", None))
        self.startMeasure_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stopMeasure_btn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.clearMeasure_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton_LiveviewSetBaro.setText(QCoreApplication.translate("MainWindow", u"Set Baro", None))
        self.pushButton_LiveViewRecord.setText(QCoreApplication.translate("MainWindow", u"Start\n"
"Logging", None))
        self.pushButton_LiveViewRecordStop.setText(QCoreApplication.translate("MainWindow", u"Stop\n"
"Logging", None))
        self.getMeasureData_btn.setText(QCoreApplication.translate("MainWindow", u"Get data from sonde", None))
        self.pushButton_DataTabView.setText("")
        self.pushButton_DataGraphView.setText("")
        self.exportToRAW_btn.setText(QCoreApplication.translate("MainWindow", u"Save as\n"
"Raw Data", None))
        self.exportToTAB_btn.setText(QCoreApplication.translate("MainWindow", u"Export to\n"
".TAB File", None))
        self.exportToCSV_btn.setText(QCoreApplication.translate("MainWindow", u"Export to \n"
".CSV File", None))
        self.cleanSonde_btn.setText(QCoreApplication.translate("MainWindow", u"Clean", None))
        self.exportToPdf_btn.setText(QCoreApplication.translate("MainWindow", u"Export\n"
"to PDF", None))
        self.exportToTxt_btn.setText(QCoreApplication.translate("MainWindow", u"Export calibration\n"
"report to TXT", None))
        self.rapidCal_btn.setText(QCoreApplication.translate("MainWindow", u"RapidCal", None))
        self.clearSondeMem_btn_2.setText(QCoreApplication.translate("MainWindow", u"Clear \n"
"memory", None))
        self.resetLeveLine_btn_2.setText(QCoreApplication.translate("MainWindow", u"Reset\n"
"LeveLine", None))
        self.resyncClockWithPC_btn_2.setText(QCoreApplication.translate("MainWindow", u"Resync clock \n"
"with PC", None))
        self.startProductLeveLine_btn.setText(QCoreApplication.translate("MainWindow", u"Start\n"
"product", None))
        self.setBaroCal_btn.setText(QCoreApplication.translate("MainWindow", u"Set Baro", None))
        self.clearGraphCal_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton_CalibRecord.setText(QCoreApplication.translate("MainWindow", u"Start\n"
"Logging", None))
        self.pushButton_CalibRecordStop.setText(QCoreApplication.translate("MainWindow", u"Stop\n"
"Logging", None))
        self.connexion_btn.setText(QCoreApplication.translate("MainWindow", u"CONNECTION", None))
        self.dashboard_btn.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.liveview_btn.setText(QCoreApplication.translate("MainWindow", u"LIVEVIEW", None))
        self.calibration_btn.setText(QCoreApplication.translate("MainWindow", u"CALIBRATION", None))
        self.data_btn.setText(QCoreApplication.translate("MainWindow", u"DATA", None))
        self.pcConfig_btn.setText(QCoreApplication.translate("MainWindow", u"APP CONFIG", None))
        self.about_btn.setText(QCoreApplication.translate("MainWindow", u"ABOUT", None))
        self.label_12.setText("")
        self.version_label.setText(QCoreApplication.translate("MainWindow", u"V1.0.2", None))
        self.label_8.setText("")
        self.label_photoProbe.setText("")
        self.pushButton_detectProduct.setText(QCoreApplication.translate("MainWindow", u"Detect sonde", None))
        self.pushButton_openRawFile.setText(QCoreApplication.translate("MainWindow", u"Open sonde raw file...", None))
        self.pushButton_detectProbe.setText(QCoreApplication.translate("MainWindow", u"Detect probe", None))
        self.pushButton_detectLeveLine.setText(QCoreApplication.translate("MainWindow", u"Detect LeveLine", None))
        self.label_photoLeveLine.setText("")
        self.label_photoSonde.setText("")
        self.label_6.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"online support", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.groupBox_SondeInfo.setTitle(QCoreApplication.translate("MainWindow", u"General info", None))
        self.label_2.setText("")
        self.label_txtModel.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.label_Model.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_80.setText("")
        self.label_28.setText("")
        self.label_txtSN.setText(QCoreApplication.translate("MainWindow", u"Serial No", None))
        self.label_SerialNo.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_79.setText("")
        self.label_39.setText("")
        self.label_txtInterfaceCom.setText(QCoreApplication.translate("MainWindow", u"Interface", None))
        self.label_InterfaceCom.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_87.setText("")
        self.label_29.setText("")
        self.label_txtSWRev.setText(QCoreApplication.translate("MainWindow", u"SW Rev", None))
        self.label_SWRev.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_78.setText("")
        self.label_30.setText("")
        self.label_txtRecordsStored.setText(QCoreApplication.translate("MainWindow", u"Records Stored", None))
        self.label_RecordsStored.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_77.setText("")
        self.label_31.setText("")
        self.label_txtMemRemaining.setText(QCoreApplication.translate("MainWindow", u"Memory remaining", None))
        self.label_MemoryRemaining.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_76.setText("")
        self.label_32.setText("")
        self.label_txtBatteryRemaining.setText(QCoreApplication.translate("MainWindow", u"Battery remaining", None))
        self.label_BatteryRemaining.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_75.setText("")
        self.label_33.setText("")
        self.label_txtBatteryVoltage.setText(QCoreApplication.translate("MainWindow", u"Battery voltage", None))
        self.label_BatteryVoltage.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_81.setText("")
        self.groupBox_EstimatedLogLife.setTitle(QCoreApplication.translate("MainWindow", u"Estimated logging life", None))
        self.label_69.setText("")
        self.label_txtUntilMemFull.setText(QCoreApplication.translate("MainWindow", u"Until memory full", None))
        self.label_UntilMemFull.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_82.setText("")
        self.label_71.setText("")
        self.label_txtUntilBattDead.setText(QCoreApplication.translate("MainWindow", u"Until battery dead", None))
        self.label_UntilBattDead.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_83.setText("")
        self.groupBox_SondeClock.setTitle(QCoreApplication.translate("MainWindow", u"Clock", None))
        self.label_54.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_sondeClockDate.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setSondeClockDate.setText("")
        self.label_46.setText("")
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.label_sondeClockTime.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setSondeClockTime.setText("")
        self.groupBox_SiteIDLocation.setTitle(QCoreApplication.translate("MainWindow", u"Site ID and location", None))
        self.label_55.setText("")
        self.label_txtSiteID.setText(QCoreApplication.translate("MainWindow", u"Site ID", None))
        self.label_SiteID.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setSiteID.setText("")
        self.label_34.setText("")
        self.label_txtSiteLat.setText(QCoreApplication.translate("MainWindow", u"Site latitude", None))
        self.label_SiteLat.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setSiteLatitude.setText("")
        self.label_56.setText("")
        self.label_txtSiteLong.setText(QCoreApplication.translate("MainWindow", u"Site longitude", None))
        self.label_SiteLong.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setSiteLong.setText("")
        self.pushButton_TestDashboard.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.groupBox_DashboardSensors.setTitle(QCoreApplication.translate("MainWindow", u"Sensors", None))
        self.groupBox_SetupLogRate.setTitle(QCoreApplication.translate("MainWindow", u"Setup logging rate", None))
        self.label_60.setText("")
        self.label_txtLogDataEvery.setText(QCoreApplication.translate("MainWindow", u"Log Data every", None))
        self.label_LogDataEvery.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setLogDataEvery.setText("")
        self.label_61.setText("")
        self.label_txtCleanEvery.setText(QCoreApplication.translate("MainWindow", u"Clean every", None))
        self.label_CleanEvery.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setCleanEvery.setText("")
        self.groupBox_EventLogging.setTitle(QCoreApplication.translate("MainWindow", u"Event logging", None))
        self.label_94.setText("")
        self.label_txtEventLogState.setText(QCoreApplication.translate("MainWindow", u"State", None))
        self.label_EventLogState.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setEventLogState.setText("")
        self.label_logoEventLogCheck.setText("")
        self.label_txtEventLogCheck.setText(QCoreApplication.translate("MainWindow", u"Check", None))
        self.label_EventLogCheck.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setEventLogCheck.setText("")
        self.label_logoEventLogEvery.setText("")
        self.label_txtEventLogEvery.setText(QCoreApplication.translate("MainWindow", u"Every", None))
        self.label_EventLogEvery.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setEventLogEvery.setText("")
        self.label_logoEventLogThreshold.setText("")
        self.label_txtEventLogThreshold.setText(QCoreApplication.translate("MainWindow", u"Log data if there is \n"
"a change >", None))
        self.label_EventLogThreshold.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setEventLogThreshold.setText("")
        self.groupBox_Averaging.setTitle(QCoreApplication.translate("MainWindow", u"Averaging", None))
        self.label_115.setText("")
        self.label_txtAveraging.setText(QCoreApplication.translate("MainWindow", u"Optical Electrodes\n"
"Averaging Time\n"
"Constant (Samples)", None))
        self.label_AveragingValue.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_116.setText("")
        self.label_101.setText("")
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Click on numerical box to hide/show corresponding curve.", None))
        self.label_3.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"98", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"(%)", None))
        self.groupBox_CalculatedResult.setTitle(QCoreApplication.translate("MainWindow", u"Calculated result", None))
        self.label_57.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Salinity", None))
        self.label_LV_salinity.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_85.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"SSG", None))
        self.label_LV_SSG.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_88.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"TDS", None))
        self.label_LV_TDS.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_96.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Ammonia", None))
        self.label_LV_Ammonia.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_dataStartDatetime.setText(QCoreApplication.translate("MainWindow", u"Start datetime", None))
        self.dateTimeEdit_dataStart.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy HH:mm:ss", None))
        self.label_dataStopDatetime.setText(QCoreApplication.translate("MainWindow", u"End datetime", None))
        self.dateTimeEdit_dataEnd.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy HH:mm:ss", None))
        self.pushButton_dataSelectAll.setText(QCoreApplication.translate("MainWindow", u"Select All", None))
        self.pushButton_dataDeselectAll.setText(QCoreApplication.translate("MainWindow", u"Deselect All", None))
        self.groupBox_Environment.setTitle(QCoreApplication.translate("MainWindow", u"Env sensors", None))
        self.groupBox_pHORPDOEC.setTitle(QCoreApplication.translate("MainWindow", u"pH/ORP DO/EC", None))
        self.groupBox_calculated.setTitle(QCoreApplication.translate("MainWindow", u"Calculated", None))
        self.groupBox_Aux.setTitle(QCoreApplication.translate("MainWindow", u"AUX sensor", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(11, QCoreApplication.translate("MainWindow", u"Tbd", None));
        ___qtreewidgetitem.setText(10, QCoreApplication.translate("MainWindow", u"EC", None));
        ___qtreewidgetitem.setText(9, QCoreApplication.translate("MainWindow", u"DO ", None));
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"DO Sat", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"ORP", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"pH mV", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"pH", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"BARO", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Depth", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Temp", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"DateTime", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Point", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(11, QCoreApplication.translate("MainWindow", u"12.2", None));
        ___qtreewidgetitem1.setText(10, QCoreApplication.translate("MainWindow", u"6", None));
        ___qtreewidgetitem1.setText(9, QCoreApplication.translate("MainWindow", u"7.8", None));
        ___qtreewidgetitem1.setText(8, QCoreApplication.translate("MainWindow", u"98.3", None));
        ___qtreewidgetitem1.setText(7, QCoreApplication.translate("MainWindow", u"5", None));
        ___qtreewidgetitem1.setText(6, QCoreApplication.translate("MainWindow", u"125", None));
        ___qtreewidgetitem1.setText(5, QCoreApplication.translate("MainWindow", u"7.2", None));
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"1018", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"310", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"20", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"2024/03/14 08:55:50", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"1", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.label_22.setText(QCoreApplication.translate("MainWindow", u"pH", None))
        self.label_26.setText("")
        self.label_42.setText("")
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"DO/EC", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"pH", None))
        self.label_10.setText("")
        self.label_47.setText("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"ORP", None))
        self.label_37.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"ORP", None))
        self.label_15.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"DO/EC", None))
        self.groupBox_AUX_PT1.setTitle(QCoreApplication.translate("MainWindow", u"AUX PT1", None))
        self.label_74.setText("")
        self.label_txtModel_15.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_AuxPt1Date.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_111.setText("")
#if QT_CONFIG(tooltip)
        self.widget_AuxPt1Value.setToolTip(QCoreApplication.translate("MainWindow", u"Click to calibrate", None))
#endif // QT_CONFIG(tooltip)
        self.label_112.setText("")
        self.label_txtSN_13.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_AuxPt1Value.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_113.setText("")
        self.groupBox_AUX_PT2.setTitle(QCoreApplication.translate("MainWindow", u"AUX PT2", None))
        self.label_58.setText("")
        self.label_txtModel_16.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_AuxPt2Date.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_108.setText("")
#if QT_CONFIG(tooltip)
        self.widget_AuxPt2Value.setToolTip(QCoreApplication.translate("MainWindow", u"Click to calibrate", None))
#endif // QT_CONFIG(tooltip)
        self.label_59.setText("")
        self.label_txtSN_10.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_AuxPt2Value.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_109.setText("")
        self.groupBox_AUX_PT3.setTitle(QCoreApplication.translate("MainWindow", u"AUX PT3", None))
        self.label_51.setText("")
        self.label_txtModel_13.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_AuxPt3Date.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_104.setText("")
#if QT_CONFIG(tooltip)
        self.widget_AuxPt3Value.setToolTip(QCoreApplication.translate("MainWindow", u"Click to calibrate", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.widget_AuxPt3Value.setWhatsThis(QCoreApplication.translate("MainWindow", u"Click to calibrate", None))
#endif // QT_CONFIG(whatsthis)
        self.label_52.setText("")
        self.label_txtModel_14.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_AuxPt3Value.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_105.setText("")
        self.groupBox_CalibrationParameters.setTitle(QCoreApplication.translate("MainWindow", u"Calibration parameters", None))
#if QT_CONFIG(tooltip)
        self.widget_ORPCalValue.setToolTip(QCoreApplication.translate("MainWindow", u"Click to calibrate", None))
#endif // QT_CONFIG(tooltip)
        self.label_98.setText("")
        self.label_txtSN_14.setText(QCoreApplication.translate("MainWindow", u"ORP Cal value", None))
        self.label_ORPCalValueType.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_114.setText("")
        self.label_50.setText("")
        self.label_txtModel_17.setText(QCoreApplication.translate("MainWindow", u"GS Factor", None))
        self.label_AuxGSFactor.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_103.setText("")
        self.label_73.setText("")
        self.label_txtModel_19.setText(QCoreApplication.translate("MainWindow", u"EC Cal value", None))
        self.label_CalSensor_ECCalValue.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_106.setText("")
        self.label_100.setText("")
        self.label_txtModel_20.setText(QCoreApplication.translate("MainWindow", u"Cal Value", None))
        self.label_CalSensor_ECUserValue.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_107.setText("")
        self.pushButton_RestoreDefaultCalibration.setText(QCoreApplication.translate("MainWindow", u" Restore default calibration", None))
        self.label_ASAPpro_calibRestore.setText(QCoreApplication.translate("MainWindow", u"With AS/AP-Pro, sonde/probe must be disconnected and powered off and back on for AUX \"Restore default calibration\" button to take effect.", None))
        self.label_CalibHiddenChannelName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.textBrowser_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Open Sans'; font-weight:700; color:#000000;\">Calibrating the Turbidity Electrode</span> </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px"
                        ";\"><span style=\" font-family:'Open Sans'; color:#000000;\">The Sonde Sleeve, Measurement Chamber and Wiper all form an integral, working part of the Sonde\u2019s turbidity measurement system, and MUST be fitted during calibration and measurement for correct operation.</span> </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Open Sans'; color:#000000;\">Turbidity electrodes have three calibration points. Careful calibration is essential in order to ensure consistent and reliable results across the full measurement range.</span> </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; marg"
                        "in-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Open Sans'; color:#000000;\">When a turbidity electrode is first installed, it should be calibrated at the Zero point in order to correct for any small differences in the Measurement Chamber.</span> </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Open Sans'; color:#000000;\">The Turbidity electrode should subsequently be Zeroed (calibrated at the Zero NTU point) before each day\u2019s use. A three point calibration should be carried out once a month to ensure optimum accuracy.</span> </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
""
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Open Sans'; color:#000000;\">During full calibration, the Zero NTU point must always be calibrated first, followed by the 1000NTU point, both within the same calibration session (i.e. without turning the Aquameter\u00ae off). The third calibration point (20NTU) is optional and can be used if enhanced accuracy is required at very low levels.</span> </p></body></html>", None))
        self.label_hiddenChannelName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_hiddenPointNumber.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_calibRTValue.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_calibRTUnit.setText(QCoreApplication.translate("MainWindow", u"(%)", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"pHmv", None))
        self.label_calibRT_pHmvValue.setText(QCoreApplication.translate("MainWindow", u"-- mV", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.label_calibRT_tempValue.setText(QCoreApplication.translate("MainWindow", u"-- \u00b0C", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"BARO", None))
        self.label_calibRT_baroValue.setText(QCoreApplication.translate("MainWindow", u"-- mB", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Last calibration date", None))
        self.label_calibPointLastCalibDate.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Last calibration value", None))
        self.label_calibPointLastCalibValue.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.textBrowser_calPoint.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.groupBox_CalibrationParameters_Point.setTitle(QCoreApplication.translate("MainWindow", u"Calibration parameters", None))
#if QT_CONFIG(tooltip)
        self.widget_ORPCalValue_Point.setToolTip(QCoreApplication.translate("MainWindow", u"Click to calibrate", None))
#endif // QT_CONFIG(tooltip)
        self.label_txtSN_15.setText(QCoreApplication.translate("MainWindow", u"ORP Cal value", None))
        self.comboBox_ORPCalValue_Point.setItemText(0, QCoreApplication.translate("MainWindow", u"250 mV", None))
        self.comboBox_ORPCalValue_Point.setItemText(1, QCoreApplication.translate("MainWindow", u"229 mV", None))

#if QT_CONFIG(tooltip)
        self.widget_ECCalValue_Point.setToolTip(QCoreApplication.translate("MainWindow", u"Click to calibrate", None))
#endif // QT_CONFIG(tooltip)
        self.label_txtSN_18.setText(QCoreApplication.translate("MainWindow", u"EC Cal value", None))
        self.comboBox_ECCalValue_Point.setItemText(0, QCoreApplication.translate("MainWindow", u"RapidCal", None))
        self.comboBox_ECCalValue_Point.setItemText(1, QCoreApplication.translate("MainWindow", u"User", None))
        self.comboBox_ECCalValue_Point.setItemText(2, QCoreApplication.translate("MainWindow", u"SC-35", None))

#if QT_CONFIG(tooltip)
        self.widget_ECCalValue_Point_2.setToolTip(QCoreApplication.translate("MainWindow", u"Click to calibrate", None))
#endif // QT_CONFIG(tooltip)
        self.label_txtSN_16.setText(QCoreApplication.translate("MainWindow", u"User Cal (uS/cm)", None))
#if QT_CONFIG(tooltip)
        self.widget_ECCalValue_Point_3.setToolTip(QCoreApplication.translate("MainWindow", u"Click to calibrate", None))
#endif // QT_CONFIG(tooltip)
        self.label_txtSN_17.setText(QCoreApplication.translate("MainWindow", u"Value (uS/cm)", None))
#if QT_CONFIG(tooltip)
        self.widget_ProbeAUXCalValue_Point.setToolTip(QCoreApplication.translate("MainWindow", u"Click to calibrate", None))
#endif // QT_CONFIG(tooltip)
        self.label_txtSN_20.setText(QCoreApplication.translate("MainWindow", u"Calibration value", None))
        self.label_calibPointName.setText(QCoreApplication.translate("MainWindow", u"Point pH 7.00", None))
        self.pushButton_calibrateCancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton_calibrateAndExit.setText(QCoreApplication.translate("MainWindow", u"Calibrate\n"
"and exit", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<h3 align=\"center\" style=\" margin-top:17px; margin-bottom:11px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; color:#333333; background-color:#ffffff;\">GNU GENERAL PUBLIC LICENSE</span></h3>\n"
"<p align=\"center\" style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:"
                        "'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">Version 3, 29 June 2007</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">Copyright \u00a9 2007 Free Software Foundation, Inc. &lt;</span><a href=\"https://fsf.org/\"><span style=\" font-family:'sans-serif'; font-size:9pt; text-decoration: underline; text-decoration-color:#bbbbbb; color:#004499;\">https://fsf.org/</span></a><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222;\">&gt;</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">Everyone is permitted to copy and distribute verbatim"
                        " copies of this license document, but changing it is not allowed.</span></p>\n"
"<h4 style=\" margin-top:17px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><a name=\"preamble\"></a><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; color:#505050; background-color:#ffffff;\">P</span><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; color:#505050; background-color:#ffffff;\">reamble</span></h4>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">The GNU General Public License is a free, copyleft license for software and other kinds of works.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; backgrou"
                        "nd-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">The licenses for most software and other practical works are designed to take away your freedom to share and change the works. By contrast, the GNU General Public License is intended to guarantee your freedom to share and change all versions of a program--to make sure it remains free software for all its users. We, the Free Software Foundation, use the GNU General Public License for most of our software; it applies also to any other work released this way by its authors. You can apply it to your programs, too.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">When we speak of free software, we are referring to freedom, not price. Our General Public Licenses are designed to m"
                        "ake sure that you have the freedom to distribute copies of free software (and charge for them if you wish), that you receive source code or can get it if you want it, that you can change the software or use pieces of it in new free programs, and that you know you can do these things.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">To protect your rights, we need to prevent others from denying you these rights or asking you to surrender the rights. Therefore, you have certain responsibilities if you distribute copies of the software, or if you modify it: responsibilities to respect the freedom of others.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Ti"
                        "mes New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">For example, if you distribute copies of such a program, whether gratis or for a fee, you must pass on to the recipients the same freedoms that you received. You must make sure that they, too, receive or can get the source code. And you must show them these terms so they know their rights.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">Developers that use the GNU GPL protect your rights with two steps: (1) assert copyright on the software, and (2) offer you this License giving you legal permission to copy, distribute and/or modify it.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-famil"
                        "y:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">For the developers' and authors' protection, the GPL clearly explains that there is no warranty for this free software. For both users' and authors' sake, the GPL requires that modified versions be marked as changed, so that their problems will not be attributed erroneously to authors of previous versions.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">Some devices are designed to deny users access to install or run modified versions of the software inside them, although the manufacturer can do so. This is fundamentally incompatible with the aim of protecting users' freedom to change the software. The systematic pattern of such abuse occurs in the area of products for individuals to use, which is precisely where it "
                        "is most unacceptable. Therefore, we have designed this version of the GPL to prohibit the practice for those products. If such problems arise substantially in other domains, we stand ready to extend this provision to those domains in future versions of the GPL, as needed to protect the freedom of users.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">Finally, every program is threatened constantly by software patents. States should not allow patents to restrict development and use of software on general-purpose computers, but in those that do, we wish to avoid the special danger that patents applied to a free program could make it effectively proprietary. To prevent this, the GPL assures that patents cannot be used to render the program non-free.</span></p>\n"
"<p style=\" margin-top:17px; marg"
                        "in-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">The precise terms and conditions for copying, distribution and modification follow.</span></p>\n"
"<h4 style=\" margin-top:17px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><a name=\"terms\"></a><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; color:#505050; background-color:#ffffff;\">T</span><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; color:#505050; background-color:#ffffff;\">ERMS AND CONDITIONS</span></h4>\n"
"<h5 style=\" margin-top:18px; margin-bottom:13px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><a name=\"section0\"></a><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:"
                        "700; font-style:italic; color:#222222; background-color:#ffffff;\">0</span><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">. Definitions.</span></h5>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">\u201cThis License\u201d refers to version 3 of the GNU General Public License.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">\u201cCopyright\u201d also means copyright-like laws that apply to other kinds of works, such as semiconductor masks.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17"
                        "px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">\u201cThe Program\u201d refers to any copyrightable work licensed under this License. Each licensee is addressed as \u201cyou\u201d. \u201cLicensees\u201d and \u201crecipients\u201d may be individuals or organizations.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">To \u201cmodify\u201d a work means to copy from or adapt all or part of the work in a fashion requiring copyright permission, other than the making of an exact copy. The resulting work is called a \u201cmodified version\u201d of the earlier work or a work \u201cbased on\u201d the earlier work.</span></p>\n"
"<p style=\" margin-t"
                        "op:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">A \u201ccovered work\u201d means either the unmodified Program or a work based on the Program.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">To \u201cpropagate\u201d a work means to do anything with it that, without permission, would make you directly or secondarily liable for infringement under applicable copyright law, except executing it on a computer or modifying a private copy. Propagation includes copying, distribution (with or without modification), making available to the public, and in some countries other activities as well.</span></p>\n"
"<p style=\" ma"
                        "rgin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">To \u201cconvey\u201d a work means any kind of propagation that enables other parties to make or receive copies. Mere interaction with a user through a computer network, with no transfer of a copy, is not conveying.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">An interactive user interface displays \u201cAppropriate Legal Notices\u201d to the extent that it includes a convenient and prominently visible feature that (1) displays an appropriate copyright notice, and (2) tells the user that there is no warranty for the work (except to the extent that warrantie"
                        "s are provided), that licensees may convey the work under this License, and how to view a copy of this License. If the interface presents a list of user commands or options, such as a menu, a prominent item in the list meets this criterion.</span></p>\n"
"<h5 style=\" margin-top:18px; margin-bottom:13px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><a name=\"section1\"></a><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">1</span><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">. Source Code.</span></h5>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">The \u201csource code\u201d"
                        " for a work means the preferred form of the work for making modifications to it. \u201cObject code\u201d means any non-source form of a work.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">A \u201cStandard Interface\u201d means an interface that either is an official standard defined by a recognized standards body, or, in the case of interfaces specified for a particular programming language, one that is widely used among developers working in that language.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">The \u201cSystem Libraries\u201d of an executable work include anything, "
                        "other than the work as a whole, that (a) is included in the normal form of packaging a Major Component, but which is not part of that Major Component, and (b) serves only to enable use of the work with that Major Component, or to implement a Standard Interface for which an implementation is available to the public in source code form. A \u201cMajor Component\u201d, in this context, means a major essential component (kernel, window system, and so on) of the specific operating system (if any) on which the executable work runs, or a compiler used to produce the work, or an object code interpreter used to run it.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">The \u201cCorresponding Source\u201d for a work in object code form means all the source code needed to generate, install, and (for an execu"
                        "table work) run the object code and to modify the work, including scripts to control those activities. However, it does not include the work's System Libraries, or general-purpose tools or generally available free programs which are used unmodified in performing those activities but which are not part of the work. For example, Corresponding Source includes interface definition files associated with source files for the work, and the source code for shared libraries and dynamically linked subprograms that the work is specifically designed to require, such as by intimate data communication or control flow between those subprograms and other parts of the work.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">The Corresponding Source need not include anything that users can regenerate automatically "
                        "from other parts of the Corresponding Source.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">The Corresponding Source for a work in source code form is that same work.</span></p>\n"
"<h5 style=\" margin-top:18px; margin-bottom:13px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><a name=\"section2\"></a><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">2</span><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">. Basic Permissions.</span></h5>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; "
                        "background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">All rights granted under this License are granted for the term of copyright on the Program, and are irrevocable provided the stated conditions are met. This License explicitly affirms your unlimited permission to run the unmodified Program. The output from running a covered work is covered by this License only if the output, given its content, constitutes a covered work. This License acknowledges your rights of fair use or other equivalent, as provided by copyright law.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">You may make, run and propagate covered works that you do not convey, without conditions so long as your license otherwise remains in force. You may c"
                        "onvey covered works to others for the sole purpose of having them make modifications exclusively for you, or provide you with facilities for running those works, provided that you comply with the terms of this License in conveying all material for which you do not control copyright. Those thus making or running the covered works for you must do so exclusively on your behalf, under your direction and control, on terms that prohibit them from making any copies of your copyrighted material outside their relationship with you.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">Conveying under any other circumstances is permitted solely under the conditions stated below. Sublicensing is not allowed; section 10 makes it unnecessary.</span></p>\n"
"<h5 style=\" margin-top:18px; margin-bottom:13px; margin"
                        "-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><a name=\"section3\"></a><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">3</span><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">. Protecting Users' Legal Rights From Anti-Circumvention Law.</span></h5>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">No covered work shall be deemed part of an effective technological measure under any applicable law fulfilling obligations under article 11 of the WIPO copyright treaty adopted on 20 December 1996, or similar laws prohibiting or restricting circumvention of such measures.</span></p>\n"
""
                        "<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">When you convey a covered work, you waive any legal power to forbid circumvention of technological measures to the extent such circumvention is effected by exercising rights under this License with respect to the covered work, and you disclaim any intention to limit operation or modification of the work as a means of enforcing, against the work's users, your or third parties' legal rights to forbid circumvention of technological measures.</span></p>\n"
"<h5 style=\" margin-top:18px; margin-bottom:13px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><a name=\"section4\"></a><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\""
                        ">4</span><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">. Conveying Verbatim Copies.</span></h5>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">You may convey verbatim copies of the Program's source code as you receive it, in any medium, provided that you conspicuously and appropriately publish on each copy an appropriate copyright notice; keep intact all notices stating that this License and any non-permissive terms added in accord with section 7 apply to the code; keep intact all notices of the absence of any warranty; and give all recipients a copy of this License along with the Program.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-"
                        "indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">You may charge any price or no price for each copy that you convey, and you may offer support or warranty protection for a fee.</span></p>\n"
"<h5 style=\" margin-top:18px; margin-bottom:13px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><a name=\"section5\"></a><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">5</span><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">. Conveying Modified Source Versions.</span></h5>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#2222"
                        "22; background-color:#ffffff;\">You may convey a work based on the Program, or the modifications to produce it from the Program, in the form of source code under the terms of section 4, provided that you also meet all of these conditions:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\" style=\" margin-top:17px; margin-bottom:0px; margin-left:28px; margin-right:12px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">a) The work must carry prominent notices stating that you modified it, and giving a relevant date.</span></li>\n"
"<li style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\" style=\" margin-top:8px; margin-bottom:0px; margin-left:28px; margin-right:12px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">b) The work must carry prominent"
                        " notices stating that it is released under this License and any conditions added under section 7. This requirement modifies the requirement in section 4 to \u201ckeep intact all notices\u201d.</span></li>\n"
"<li style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\" style=\" margin-top:8px; margin-bottom:0px; margin-left:28px; margin-right:12px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">c) You must license the entire work, as a whole, under this License to anyone who comes into possession of a copy. This License will therefore apply, along with any applicable section 7 additional terms, to the whole of the work, and all its parts, regardless of how they are packaged. This License gives no permission to license the work in any other way, but it does not invalidate such permission if you have separately received it.</span></li>\n"
"<li style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\" style=\""
                        " margin-top:8px; margin-bottom:17px; margin-left:28px; margin-right:12px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">d) If the work has interactive user interfaces, each must display Appropriate Legal Notices; however, if the Program has interactive interfaces that do not display Appropriate Legal Notices, your work need not make them do so.</span></li></ul>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">A compilation of a covered work with other separate and independent works, which are not by their nature extensions of the covered work, and which are not combined with it such as to form a larger program, in or on a volume of a storage or distribution medium, is called an \u201caggregate\u201d if the compilation and its resulting copyright are not used to limit the access or"
                        " legal rights of the compilation's users beyond what the individual works permit. Inclusion of a covered work in an aggregate does not cause this License to apply to the other parts of the aggregate.</span></p>\n"
"<h5 style=\" margin-top:18px; margin-bottom:13px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><a name=\"section6\"></a><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">6</span><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">. Conveying Non-Source Forms.</span></h5>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">You may convey a covered work in object code for"
                        "m under the terms of sections 4 and 5, provided that you also convey the machine-readable Corresponding Source under the terms of this License, in one of these ways:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\" style=\" margin-top:17px; margin-bottom:0px; margin-left:28px; margin-right:12px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">a) Convey the object code in, or embodied in, a physical product (including a physical distribution medium), accompanied by the Corresponding Source fixed on a durable physical medium customarily used for software interchange.</span></li>\n"
"<li style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\" style=\" margin-top:8px; margin-bottom:0px; margin-left:28px; margin-right:12px; -qt-block-indent:0; text-indent:0px;\"><span styl"
                        "e=\" font-size:16px;\">b) Convey the object code in, or embodied in, a physical product (including a physical distribution medium), accompanied by a written offer, valid for at least three years and valid for as long as you offer spare parts or customer support for that product model, to give anyone who possesses the object code either (1) a copy of the Corresponding Source for all the software in the product that is covered by this License, on a durable physical medium customarily used for software interchange, for a price no more than your reasonable cost of physically performing this conveying of source, or (2) access to copy the Corresponding Source from a network server at no charge.</span></li>\n"
"<li style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\" style=\" margin-top:8px; margin-bottom:0px; margin-left:28px; margin-right:12px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">c) Convey individual copies of the object code with a co"
                        "py of the written offer to provide the Corresponding Source. This alternative is allowed only occasionally and noncommercially, and only if you received the object code with such an offer, in accord with subsection 6b.</span></li>\n"
"<li style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\" style=\" margin-top:8px; margin-bottom:0px; margin-left:28px; margin-right:12px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">d) Convey the object code by offering access from a designated place (gratis or for a charge), and offer equivalent access to the Corresponding Source in the same way through the same place at no further charge. You need not require recipients to copy the Corresponding Source along with the object code. If the place to copy the object code is a network server, the Corresponding Source may be on a different server (operated by you or a third party) that supports equivalent copying facilities, provided you maintain clear directions"
                        " next to the object code saying where to find the Corresponding Source. Regardless of what server hosts the Corresponding Source, you remain obligated to ensure that it is available for as long as needed to satisfy these requirements.</span></li>\n"
"<li style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\" style=\" margin-top:8px; margin-bottom:17px; margin-left:28px; margin-right:12px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">e) Convey the object code using peer-to-peer transmission, provided you inform other peers where the object code and Corresponding Source of the work are being offered to the general public at no charge under subsection 6d.</span></li></ul>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">A separable portion "
                        "of the object code, whose source code is excluded from the Corresponding Source as a System Library, need not be included in conveying the object code work.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">A \u201cUser Product\u201d is either (1) a \u201cconsumer product\u201d, which means any tangible personal property which is normally used for personal, family, or household purposes, or (2) anything designed or sold for incorporation into a dwelling. In determining whether a product is a consumer product, doubtful cases shall be resolved in favor of coverage. For a particular product received by a particular user, \u201cnormally used\u201d refers to a typical or common use of that class of product, regardless of the status of the particular user or of the way in which the particular user actu"
                        "ally uses, or expects or is expected to use, the product. A product is a consumer product regardless of whether the product has substantial commercial, industrial or non-consumer uses, unless such uses represent the only significant mode of use of the product.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">\u201cInstallation Information\u201d for a User Product means any methods, procedures, authorization keys, or other information required to install and execute modified versions of a covered work in that User Product from a modified version of its Corresponding Source. The information must suffice to ensure that the continued functioning of the modified object code is in no case prevented or interfered with solely because modification has been made.</span></p>\n"
"<p style=\" margin-top:17px"
                        "; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">If you convey an object code work under this section in, or with, or specifically for use in, a User Product, and the conveying occurs as part of a transaction in which the right of possession and use of the User Product is transferred to the recipient in perpetuity or for a fixed term (regardless of how the transaction is characterized), the Corresponding Source conveyed under this section must be accompanied by the Installation Information. But this requirement does not apply if neither you nor any third party retains the ability to install modified object code on the User Product (for example, the work has been installed in ROM).</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffff"
                        "ff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">The requirement to provide Installation Information does not include a requirement to continue to provide support service, warranty, or updates for a work that has been modified or installed by the recipient, or for the User Product in which it has been modified or installed. Access to a network may be denied when the modification itself materially and adversely affects the operation of the network or violates the rules and protocols for communication across the network.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">Corresponding Source conveyed, and Installation Information provided, in accord with this section must be in a format that is publicly documented (and with an implementati"
                        "on available to the public in source code form), and must require no special password or key for unpacking, reading or copying.</span></p>\n"
"<h5 style=\" margin-top:18px; margin-bottom:13px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><a name=\"section7\"></a><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">7</span><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">. Additional Terms.</span></h5>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">\u201cAdditional permissions\u201d are terms that supplement the terms of this License by making exceptions from one or more of it"
                        "s conditions. Additional permissions that are applicable to the entire Program shall be treated as though they were included in this License, to the extent that they are valid under applicable law. If additional permissions apply only to part of the Program, that part may be used separately under those permissions, but the entire Program remains governed by this License without regard to the additional permissions.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">When you convey a copy of a covered work, you may at your option remove any additional permissions from that copy, or from any part of it. (Additional permissions may be written to require their own removal in certain cases when you modify the work.) You may place additional permissions on material, added by you to a covered work, for w"
                        "hich you have or can give appropriate copyright permission.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">Notwithstanding any other provision of this License, for material you add to a covered work, you may (if authorized by the copyright holders of that material) supplement the terms of this License with terms:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\" style=\" margin-top:17px; margin-bottom:0px; margin-left:28px; margin-right:12px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">a) Disclaiming warranty or limiting liability differently from the terms of sections 15 and 16 of this Li"
                        "cense; or</span></li>\n"
"<li style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\" style=\" margin-top:8px; margin-bottom:0px; margin-left:28px; margin-right:12px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">b) Requiring preservation of specified reasonable legal notices or author attributions in that material or in the Appropriate Legal Notices displayed by works containing it; or</span></li>\n"
"<li style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\" style=\" margin-top:8px; margin-bottom:0px; margin-left:28px; margin-right:12px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">c) Prohibiting misrepresentation of the origin of that material, or requiring that modified versions of such material be marked in reasonable ways as different from the original version; or</span></li>\n"
"<li style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color"
                        ":#ffffff;\" style=\" margin-top:8px; margin-bottom:0px; margin-left:28px; margin-right:12px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">d) Limiting the use for publicity purposes of names of licensors or authors of the material; or</span></li>\n"
"<li style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\" style=\" margin-top:8px; margin-bottom:0px; margin-left:28px; margin-right:12px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">e) Declining to grant rights under trademark law for use of some trade names, trademarks, or service marks; or</span></li>\n"
"<li style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\" style=\" margin-top:8px; margin-bottom:17px; margin-left:28px; margin-right:12px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">f) Requiring indemnification of licensors and authors of that material by anyone who conveys the material (or "
                        "modified versions of it) with contractual assumptions of liability to the recipient, for any liability that these contractual assumptions directly impose on those licensors and authors.</span></li></ul>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">All other non-permissive additional terms are considered \u201cfurther restrictions\u201d within the meaning of section 10. If the Program as you received it, or any part of it, contains a notice stating that it is governed by this License along with a term that is a further restriction, you may remove that term. If a license document contains a further restriction but permits relicensing or conveying under this License, you may add to a covered work material governed by the terms of that license document, provided that the further restriction does not surviv"
                        "e such relicensing or conveying.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">If you add terms to a covered work in accord with this section, you must place, in the relevant source files, a statement of the additional terms that apply to those files, or a notice indicating where to find the applicable terms.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">Additional terms, permissive or non-permissive, may be stated in the form of a separately written license, or stated as exceptions; the above requirements apply either way.</span></p>\n"
"<h5 style=\" margin-top:18px; margin"
                        "-bottom:13px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><a name=\"section8\"></a><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">8</span><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">. Termination.</span></h5>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">You may not propagate or modify a covered work except as expressly provided under this License. Any attempt otherwise to propagate or modify it is void, and will automatically terminate your rights under this License (including any patent licenses granted under the third paragraph of section 11).</span></p>\n"
"<"
                        "p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">However, if you cease all violation of this License, then your license from a particular copyright holder is reinstated (a) provisionally, unless and until the copyright holder explicitly and finally terminates your license, and (b) permanently, if the copyright holder fails to notify you of the violation by some reasonable means prior to 60 days after the cessation.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">Moreover, your license from a particular copyright holder is reinstated permanently if the copyright holder notifies you of the violati"
                        "on by some reasonable means, this is the first time you have received notice of violation of this License (for any work) from that copyright holder, and you cure the violation prior to 30 days after your receipt of the notice.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">Termination of your rights under this section does not terminate the licenses of parties who have received copies or rights from you under this License. If your rights have been terminated and not permanently reinstated, you do not qualify to receive new licenses for the same material under section 10.</span></p>\n"
"<h5 style=\" margin-top:18px; margin-bottom:13px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><a name=\"section9\"></a><span style=\" font-family:'Times Ne"
                        "w Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">9</span><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">. Acceptance Not Required for Having Copies.</span></h5>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">You are not required to accept this License in order to receive or run a copy of the Program. Ancillary propagation of a covered work occurring solely as a consequence of using peer-to-peer transmission to receive a copy likewise does not require acceptance. However, nothing other than this License grants you permission to propagate or modify any covered work. These actions infringe copyright if you do not accept this License. Therefore, by modifying or p"
                        "ropagating a covered work, you indicate your acceptance of this License to do so.</span></p>\n"
"<h5 style=\" margin-top:18px; margin-bottom:13px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><a name=\"section10\"></a><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">1</span><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">0. Automatic Licensing of Downstream Recipients.</span></h5>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">Each time you convey a covered work, the recipient automatically receives a license from the original licensors, to run, modify and propagate that"
                        " work, subject to this License. You are not responsible for enforcing compliance by third parties with this License.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">An \u201centity transaction\u201d is a transaction transferring control of an organization, or substantially all assets of one, or subdividing an organization, or merging organizations. If propagation of a covered work results from an entity transaction, each party to that transaction who receives a copy of the work also receives whatever licenses to the work the party's predecessor in interest had or could give under the previous paragraph, plus a right to possession of the Corresponding Source of the work from the predecessor in interest, if the predecessor has it or can get it with reasonable efforts.</span></p>\n"
"<p style=\" m"
                        "argin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">You may not impose any further restrictions on the exercise of the rights granted or affirmed under this License. For example, you may not impose a license fee, royalty, or other charge for exercise of rights granted under this License, and you may not initiate litigation (including a cross-claim or counterclaim in a lawsuit) alleging that any patent claim is infringed by making, using, selling, offering for sale, or importing the Program or any portion of it.</span></p>\n"
"<h5 style=\" margin-top:18px; margin-bottom:13px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><a name=\"section11\"></a><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:"
                        "#ffffff;\">1</span><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">1. Patents.</span></h5>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">A \u201ccontributor\u201d is a copyright holder who authorizes use under this License of the Program or a work on which the Program is based. The work thus licensed is called the contributor's \u201ccontributor version\u201d.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">A contributor's \u201cessential patent claims\u201d are all patent claims owned or controll"
                        "ed by the contributor, whether already acquired or hereafter acquired, that would be infringed by some manner, permitted by this License, of making, using, or selling its contributor version, but do not include claims that would be infringed only as a consequence of further modification of the contributor version. For purposes of this definition, \u201ccontrol\u201d includes the right to grant patent sublicenses in a manner consistent with the requirements of this License.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">Each contributor grants you a non-exclusive, worldwide, royalty-free patent license under the contributor's essential patent claims, to make, use, sell, offer for sale, import and otherwise run, modify and propagate the contents of its contributor version.</span></p>\n"
"<p styl"
                        "e=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">In the following three paragraphs, a \u201cpatent license\u201d is any express agreement or commitment, however denominated, not to enforce a patent (such as an express permission to practice a patent or covenant not to sue for patent infringement). To \u201cgrant\u201d such a patent license to a party means to make such an agreement or commitment not to enforce a patent against the party.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">If you convey a covered work, knowingly relying on a patent license, and the Corresponding Source of the work is not a"
                        "vailable for anyone to copy, free of charge and under the terms of this License, through a publicly available network server or other readily accessible means, then you must either (1) cause the Corresponding Source to be so available, or (2) arrange to deprive yourself of the benefit of the patent license for this particular work, or (3) arrange, in a manner consistent with the requirements of this License, to extend the patent license to downstream recipients. \u201cKnowingly relying\u201d means you have actual knowledge that, but for the patent license, your conveying the covered work in a country, or your recipient's use of the covered work in a country, would infringe one or more identifiable patents in that country that you have reason to believe are valid.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-"
                        "color:#ffffff;\">If, pursuant to or in connection with a single transaction or arrangement, you convey, or propagate by procuring conveyance of, a covered work, and grant a patent license to some of the parties receiving the covered work authorizing them to use, propagate, modify or convey a specific copy of the covered work, then the patent license you grant is automatically extended to all recipients of the covered work and works based on it.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">A patent license is \u201cdiscriminatory\u201d if it does not include within the scope of its coverage, prohibits the exercise of, or is conditioned on the non-exercise of one or more of the rights that are specifically granted under this License. You may not convey a covered work if you are a party to an a"
                        "rrangement with a third party that is in the business of distributing software, under which you make payment to the third party based on the extent of your activity of conveying the work, and under which the third party grants, to any of the parties who would receive the covered work from you, a discriminatory patent license (a) in connection with copies of the covered work conveyed by you (or copies made from those copies), or (b) primarily for and in connection with specific products or compilations that contain the covered work, unless you entered into that arrangement, or that patent license was granted, prior to 28 March 2007.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">Nothing in this License shall be construed as excluding or limiting any implied license or other defenses to infringe"
                        "ment that may otherwise be available to you under applicable patent law.</span></p>\n"
"<h5 style=\" margin-top:18px; margin-bottom:13px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><a name=\"section12\"></a><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">1</span><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">2. No Surrender of Others' Freedom.</span></h5>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">If conditions are imposed on you (whether by court order, agreement or otherwise) that contradict the conditions of this License, they do not excuse you from the condit"
                        "ions of this License. If you cannot convey a covered work so as to satisfy simultaneously your obligations under this License and any other pertinent obligations, then as a consequence you may not convey it at all. For example, if you agree to terms that obligate you to collect a royalty for further conveying from those to whom you convey the Program, the only way you could satisfy both those terms and this License would be to refrain entirely from conveying the Program.</span></p>\n"
"<h5 style=\" margin-top:18px; margin-bottom:13px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><a name=\"section13\"></a><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">1</span><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">3. Use with the GNU Affero General Public License.</span></h5>\n"
"<p "
                        "style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">Notwithstanding any other provision of this License, you have permission to link or combine any covered work with a work licensed under version 3 of the GNU Affero General Public License into a single combined work, and to convey the resulting work. The terms of this License will continue to apply to the part which is the covered work, but the special requirements of the GNU Affero General Public License, section 13, concerning interaction through a network will apply to the combination as such.</span></p>\n"
"<h5 style=\" margin-top:18px; margin-bottom:13px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><a name=\"section14\"></a><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-"
                        "style:italic; color:#222222; background-color:#ffffff;\">1</span><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">4. Revised Versions of this License.</span></h5>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">The Free Software Foundation may publish revised and/or new versions of the GNU General Public License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffff"
                        "ff;\">Each version is given a distinguishing version number. If the Program specifies that a certain numbered version of the GNU General Public License \u201cor any later version\u201d applies to it, you have the option of following the terms and conditions either of that numbered version or of any later version published by the Free Software Foundation. If the Program does not specify a version number of the GNU General Public License, you may choose any version ever published by the Free Software Foundation.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">If the Program specifies that a proxy can decide which future versions of the GNU General Public License can be used, that proxy's public statement of acceptance of a version permanently authorizes you to choose that version for the Program."
                        "</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">Later license versions may give you additional or different permissions. However, no additional obligations are imposed on any author or copyright holder as a result of your choosing to follow a later version.</span></p>\n"
"<h5 style=\" margin-top:18px; margin-bottom:13px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><a name=\"section15\"></a><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">1</span><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">5. Disclaimer of Warranty.</span></h5>\n"
"<p style=\" margin-top:1"
                        "7px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM \u201cAS IS\u201d WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.</span></p>\n"
"<h5 style=\" margin-top:18px; margin-bottom:13px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><a name=\"section16\"></a><span style=\" font-family:'Times New Roman'; fon"
                        "t-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">1</span><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">6. Limitation of Liability.</span></h5>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE "
                        "WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.</span></p>\n"
"<h5 style=\" margin-top:18px; margin-bottom:13px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><a name=\"section17\"></a><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">1</span><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; font-style:italic; color:#222222; background-color:#ffffff;\">7. Interpretation of Sections 15 and 16.</span></h5>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">If the disclaimer of warranty and limitation of liability provided above cannot be given local legal effect according to t"
                        "heir terms, reviewing courts shall apply local law that most closely approximates an absolute waiver of all civil liability in connection with the Program, unless a warranty or assumption of liability accompanies a copy of the Program in return for a fee.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">END OF TERMS AND CONDITIONS</span></p>\n"
"<h4 style=\" margin-top:17px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><a name=\"howto\"></a><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; color:#505050; background-color:#ffffff;\">H</span><span style=\" font-family:'Times New Roman'; font-size:9pt; font-weight:700; color:#505050; background-color:#ffffff;\">ow to Apply These Terms to Your New "
                        "Programs</span></h4>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">If you develop a new program, and you want it to be of the greatest possible use to the public, the best way to achieve this is to make it free software which everyone can redistribute and change under these terms.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">To do so, attach the following notices to the program. It is safest to attach them to the start of each source file to most effectively state the exclusion of warranty; and each file should have at least the \u201ccopyright\u201d line and a pointer to where the fu"
                        "ll notice is found.</span></p>\n"
"<p style=\" margin-top:16px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Courier New'; font-size:9pt; color:#222222; background-color:#ffffff;\">    &lt;one line to give the program's name and a brief idea of what it does.&gt;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Courier New'; font-size:9pt; color:#222222; background-color:#ffffff;\">    Copyright (C) &lt;year&gt;  &lt;name of author&gt;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier New'; font-size:9pt; color:#222222; background-color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -q"
                        "t-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Courier New'; font-size:9pt; color:#222222; background-color:#ffffff;\">    This program is free software: you can redistribute it and/or modify</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Courier New'; font-size:9pt; color:#222222; background-color:#ffffff;\">    it under the terms of the GNU General Public License as published by</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Courier New'; font-size:9pt; color:#222222; background-color:#ffffff;\">    the Free Software Foundation, either version 3 of the License, or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-"
                        "indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Courier New'; font-size:9pt; color:#222222; background-color:#ffffff;\">    (at your option) any later version.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier New'; font-size:9pt; color:#222222; background-color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Courier New'; font-size:9pt; color:#222222; background-color:#ffffff;\">    This program is distributed in the hope that it will be useful,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Courier New'; font-size:9pt; color:#222222; background-color:#ffffff;\">    but W"
                        "ITHOUT ANY WARRANTY; without even the implied warranty of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Courier New'; font-size:9pt; color:#222222; background-color:#ffffff;\">    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Courier New'; font-size:9pt; color:#222222; background-color:#ffffff;\">    GNU General Public License for more details.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier New'; font-size:9pt; color:#222222; background-color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margi"
                        "n-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Courier New'; font-size:9pt; color:#222222; background-color:#ffffff;\">    You should have received a copy of the GNU General Public License</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:16px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Courier New'; font-size:9pt; color:#222222; background-color:#ffffff;\">    along with this program.  If not, see &lt;https://www.gnu.org/licenses/&gt;.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">Also add information on how to contact you by electronic and paper mail.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-righ"
                        "t:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">If the program does terminal interaction, make it output a short notice like this when it starts in an interactive mode:</span></p>\n"
"<p style=\" margin-top:16px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Courier New'; font-size:9pt; color:#222222; background-color:#ffffff;\">    &lt;program&gt;  Copyright (C) &lt;year&gt;  &lt;name of author&gt;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Courier New'; font-size:9pt; color:#222222; background-color:#ffffff;\">    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.</span></p>\n"
"<p style=\" margin-top:0px; margin-bo"
                        "ttom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Courier New'; font-size:9pt; color:#222222; background-color:#ffffff;\">    This is free software, and you are welcome to redistribute it</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:16px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Courier New'; font-size:9pt; color:#222222; background-color:#ffffff;\">    under certain conditions; type `show c' for details.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">The hypothetical commands `show w' and `show c' should show the appropriate parts of the General Public License. Of course, your program's commands might be diff"
                        "erent; for a GUI interface, you would use an \u201cabout box\u201d.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">You should also get your employer (if you work as a programmer) or school, if any, to sign a \u201ccopyright disclaimer\u201d for the program, if necessary. For more information on this, and how to apply and follow the GNU GPL, see &lt;</span><a href=\"https://www.gnu.org/licenses/\"><span style=\" font-family:'sans-serif'; font-size:9pt; text-decoration: underline; text-decoration-color:#bbbbbb; color:#004499;\">https://www.gnu.org/licenses/</span></a><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222;\">&gt;.</span></p>\n"
"<p style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-c"
                        "olor:#ffffff;\"><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222; background-color:#ffffff;\">The GNU General Public License does not permit incorporating your program into proprietary programs. If your program is a subroutine library, you may consider it more useful to permit linking proprietary applications with the library. If this is what you want to do, use the GNU Lesser General Public License instead of this License. But first, please read &lt;</span><a href=\"https://www.gnu.org/licenses/why-not-lgpl.html\"><span style=\" font-family:'sans-serif'; font-size:9pt; text-decoration: underline; text-decoration-color:#bbbbbb; color:#004499;\">https://www.gnu.org/licenses/why-not-lgpl.html</span></a><span style=\" font-family:'Times New Roman'; font-size:9pt; color:#222222;\">&gt;.</span></p></body></html>", None))
        self.label_QtLogo.setText("")
        self.label_24.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Licenses", None))
        self.label_131.setText("")
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"PC Configuration", None))
        self.groupBox_PCConf_Measure.setTitle(QCoreApplication.translate("MainWindow", u"Measure", None))
        self.label_124.setText("")
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"EC Ref temperature", None))
        self.label_Config_ECRefTemp.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_126.setText("")
        self.label_121.setText("")
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"Temperature Unit", None))
        self.label_Config_TempUnit.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_123.setText("")
        self.label_102.setText("")
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Depth Unit", None))
        self.label_Config_DepthUnit.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_117.setText("")
        self.label_118.setText("")
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"TDS Factor", None))
        self.label_Config_TDSFactor.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_120.setText("")
        self.groupBox_PCConf_AppSettings.setTitle(QCoreApplication.translate("MainWindow", u"Liveview", None))
        self.label_127.setText("")
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"Graphical depth", None))
        self.label_Config_GraphDepth.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_129.setText("")
        self.label_135.setText("")
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"Display calculated\n"
"measurement", None))
        self.label_Config_DisplayCalculated.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_137.setText("")
        self.groupBox_SondeInfo_2.setTitle(QCoreApplication.translate("MainWindow", u"Sonde info", None))
        self.label_16.setText("")
        self.label_txtModel_2.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.label_Model_2.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_84.setText("")
        self.label_66.setText("")
        self.label_txtBatteryVoltage_2.setText(QCoreApplication.translate("MainWindow", u"Depth rating", None))
        self.label_DepthRating.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_95.setText("")
        self.label_36.setText("")
        self.label_txtSN_2.setText(QCoreApplication.translate("MainWindow", u"Serial No", None))
        self.label_SerialNo_2.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_86.setText("")
        self.label_62.setText("")
        self.label_txtInterfaceCom_2.setText(QCoreApplication.translate("MainWindow", u"Interface", None))
        self.label_InterfaceCom_2.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_89.setText("")
        self.label_38.setText("")
        self.label_txtSWRev_2.setText(QCoreApplication.translate("MainWindow", u"SW Rev", None))
        self.label_SWRev_2.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_90.setText("")
        self.label_63.setText("")
        self.label_txtRecordsStored_2.setText(QCoreApplication.translate("MainWindow", u"Records Stored", None))
        self.label_RecordsStored_2.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_91.setText("")
        self.label_64.setText("")
        self.label_txtMemRemaining_2.setText(QCoreApplication.translate("MainWindow", u"Memory remaining", None))
        self.label_MemoryRemaining_2.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_92.setText("")
        self.label_65.setText("")
        self.label_txtBatteryRemaining_2.setText(QCoreApplication.translate("MainWindow", u"Battery remaining", None))
        self.label_BatteryRemaining_2.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_93.setText("")
        self.groupBox_SondeClock_2.setTitle(QCoreApplication.translate("MainWindow", u"Clock", None))
        self.label_67.setText("")
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_sondeClockDate_2.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setSondeClockDate_2.setText("")
        self.label_134.setText("")
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.label_sondeClockTime_2.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setSondeClockTime_2.setText("")
        self.groupBox_SiteIDLocation_2.setTitle(QCoreApplication.translate("MainWindow", u"Site ID and Deployment Position", None))
        self.label_139.setText("")
        self.label_txtSiteID_2.setText(QCoreApplication.translate("MainWindow", u"Site Ident", None))
        self.label_SiteID_2.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setSiteID_2.setText("")
        self.label_140.setText("")
        self.label_txtSiteLat_2.setText(QCoreApplication.translate("MainWindow", u"Site latitude", None))
        self.label_SiteLat_2.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setSiteLatitude_2.setText("")
        self.label_141.setText("")
        self.label_txtSiteLong_2.setText(QCoreApplication.translate("MainWindow", u"Site longitude", None))
        self.label_SiteLong_2.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setSiteLong_2.setText("")
        self.label_148.setText("")
        self.label_txtSiteLong_4.setText(QCoreApplication.translate("MainWindow", u"Site altitude", None))
        self.label_SiteAltitude.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setSiteLong_4.setText("")
        self.groupBox_DashboardSensors_2.setTitle(QCoreApplication.translate("MainWindow", u"Sensors", None))
        self.groupBox_MeasurementStatus.setTitle(QCoreApplication.translate("MainWindow", u"Measurement Status", None))
        self.label_145.setText("")
        self.label_txtLogDataEvery_3.setText(QCoreApplication.translate("MainWindow", u"State", None))
        self.label_MeasStatusState.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setLogDataEvery_3.setText("")
        self.label_146.setText("")
        self.label_txtCleanEvery_4.setText(QCoreApplication.translate("MainWindow", u"Start mode", None))
        self.label_LogStartMode.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setCleanEvery_4.setText("")
        self.label_150.setText("")
        self.label_txtCleanEvery_8.setText(QCoreApplication.translate("MainWindow", u"Start logging at", None))
        self.label_LogStartAt.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setCleanEvery_8.setText("")
        self.label_154.setText("")
        self.label_txtCleanEvery_9.setText(QCoreApplication.translate("MainWindow", u"End date time", None))
        self.label_LogEndDateTime.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setCleanEvery_9.setText("")
        self.groupBox_SetupLogRate_2.setTitle(QCoreApplication.translate("MainWindow", u"Logging configuration", None))
        self.label_142.setText("")
        self.label_txtLogDataEvery_2.setText(QCoreApplication.translate("MainWindow", u"Log Data every", None))
        self.label_LogDataEvery_2.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setLogDataEvery_2.setText("")
        self.label_151.setText("")
        self.label_txtCleanEvery_5.setText(QCoreApplication.translate("MainWindow", u"Log data for", None))
        self.label_LogDataFor.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setCleanEvery_5.setText("")
        self.groupBox_EventLogging_2.setTitle(QCoreApplication.translate("MainWindow", u"Event logging", None))
        self.label_144.setText("")
        self.label_txtEventLogState_2.setText(QCoreApplication.translate("MainWindow", u"State", None))
        self.label_EventLogState_2.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setEventLogState_2.setText("")
        self.label_logoEventLogEvery_2.setText("")
        self.label_txtEventLogEvery_2.setText(QCoreApplication.translate("MainWindow", u"Check event every", None))
        self.label_EventLogEvery_2.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setEventLogEvery_2.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Log data when change exceeds either of these limits :", None))
        self.label_logoEventLogLevelValue.setText("")
        self.label_txtEventLogLevelValue.setText(QCoreApplication.translate("MainWindow", u"Level +/-", None))
        self.label_EventLogLevelValue.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setEventLogLevelValue.setText("")
        self.label_logoEventLogTemperatureValue.setText("")
        self.label_txtEventLogTemperatureValue.setText(QCoreApplication.translate("MainWindow", u"Temperature +/-", None))
        self.label_EventLogTemperatureValue.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setEventLogTemperatureValue.setText("")
        self.label_logoEventLogSalinityValue.setText("")
        self.label_txtEventLogSalinityValue.setText(QCoreApplication.translate("MainWindow", u"Salinity +/-", None))
        self.label_EventLogSalinityValue.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_setEventLogSalinityValue.setText("")
    # retranslateUi

