# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gsui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1075, 627)
        MainWindow.setStyleSheet(u"QMainWindow#MainWindow{\n"
"background-color: rgb(40, 40, 40);\n"
"}")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"	background-color: rgb(58, 58, 58);\n"
"}")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.plot_speed = QSlider(self.centralwidget)
        self.plot_speed.setObjectName(u"plot_speed")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_speed.sizePolicy().hasHeightForWidth())
        self.plot_speed.setSizePolicy(sizePolicy)
        self.plot_speed.setMinimumSize(QSize(130, 0))
        self.plot_speed.setMinimum(20)
        self.plot_speed.setMaximum(300)
        self.plot_speed.setValue(200)
        self.plot_speed.setOrientation(Qt.Horizontal)
        self.plot_speed.setTickPosition(QSlider.TicksAbove)
        self.plot_speed.setTickInterval(10)

        self.horizontalLayout_4.addWidget(self.plot_speed)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setStyleSheet(u"\n"
"	background-color: rgb(132, 132, 132);\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_9)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 2, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(240, 100))
        self.label.setText(u"")
        self.label.setPixmap(QPixmap(u"telepy_name.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)

        self.gridLayout_5.addWidget(self.label, 3, 0, 2, 1)


        self.gridLayout_2.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Plot3 = PlotWidget(self.centralwidget)
        self.Plot3.setObjectName(u"Plot3")
        self.Plot3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.Plot3, 0, 2, 1, 1)

        self.Plot2 = PlotWidget(self.centralwidget)
        self.Plot2.setObjectName(u"Plot2")
        self.Plot2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.Plot2, 0, 1, 1, 1)

        self.Plot1 = PlotWidget(self.centralwidget)
        self.Plot1.setObjectName(u"Plot1")
        self.Plot1.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.Plot1, 0, 0, 1, 1)

        self.Plot5 = PlotWidget(self.centralwidget)
        self.Plot5.setObjectName(u"Plot5")
        self.Plot5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.Plot5, 1, 1, 1, 1)

        self.Plot6 = PlotWidget(self.centralwidget)
        self.Plot6.setObjectName(u"Plot6")
        self.Plot6.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.Plot6, 1, 2, 1, 1)

        self.Plot4 = PlotWidget(self.centralwidget)
        self.Plot4.setObjectName(u"Plot4")
        self.Plot4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.Plot4, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 0, 1, 5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.resize_button = QPushButton(self.centralwidget)
        self.resize_button.setObjectName(u"resize_button")
        self.resize_button.setStyleSheet(u"QPushButton#resize_button {\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#resize_button:hover {\n"
"	background-color: rgb(67, 135, 202);\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#resize_button:pressed {\n"
"	background-color: rgb(85, 170, 0);\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.resize_button)


        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setStyleSheet(u"\n"
"	background-color: rgb(132, 132, 132);\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 2, 1, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(9)
        self.gridLayout_6.setVerticalSpacing(1)
        self.serial_port = QComboBox(self.centralwidget)
        self.serial_port.addItem("")
        self.serial_port.setObjectName(u"serial_port")
        self.serial_port.setMinimumSize(QSize(55, 0))
        self.serial_port.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(132, 132, 132);\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}")

        self.gridLayout_6.addWidget(self.serial_port, 0, 1, 1, 1)

        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 85, 0);\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(198, 66, 0);\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(85, 170, 0);\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"")

        self.gridLayout_6.addWidget(self.save_button, 3, 0, 1, 1)

        self.connect_button = QPushButton(self.centralwidget)
        self.connect_button.setObjectName(u"connect_button")
        self.connect_button.setStyleSheet(u"QPushButton#connect_button {\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#connect_button:hover {\n"
"	background-color: rgb(85, 170, 0);\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#connect_button:pressed {\n"
"	background-color: rgb(85, 170, 0);\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"")

        self.gridLayout_6.addWidget(self.connect_button, 0, 0, 1, 1)

        self.data_points_in_file = QLabel(self.centralwidget)
        self.data_points_in_file.setObjectName(u"data_points_in_file")
        sizePolicy.setHeightForWidth(self.data_points_in_file.sizePolicy().hasHeightForWidth())
        self.data_points_in_file.setSizePolicy(sizePolicy)
        self.data_points_in_file.setMinimumSize(QSize(0, 4))
        self.data_points_in_file.setStyleSheet(u"font: 9pt \"Segoe UI\";\n"
"background-color: rgb(132, 132, 132);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(188, 214, 255);\n"
"border-radius: 5px;")
        self.data_points_in_file.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.data_points_in_file, 3, 1, 1, 1)

        self.disconnect_button = QPushButton(self.centralwidget)
        self.disconnect_button.setObjectName(u"disconnect_button")
        self.disconnect_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 0, 0);\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(198, 0, 0);\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(85, 170, 0);\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}")

        self.gridLayout_6.addWidget(self.disconnect_button, 1, 0, 1, 1)

        self.serial_baud = QComboBox(self.centralwidget)
        self.serial_baud.addItem("")
        self.serial_baud.addItem("")
        self.serial_baud.addItem("")
        self.serial_baud.addItem("")
        self.serial_baud.addItem("")
        self.serial_baud.addItem("")
        self.serial_baud.addItem("")
        self.serial_baud.addItem("")
        self.serial_baud.setObjectName(u"serial_baud")
        self.serial_baud.setMinimumSize(QSize(63, 0))
        self.serial_baud.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(132, 132, 132);\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}")

        self.gridLayout_6.addWidget(self.serial_baud, 1, 1, 1, 1)

        self.save_data_option = QCheckBox(self.centralwidget)
        self.save_data_option.setObjectName(u"save_data_option")
        self.save_data_option.setStyleSheet(u"QCheckBox {\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_6.addWidget(self.save_data_option, 2, 0, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout_6, 0, 4, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(16)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.stats_1_labels = QLabel(self.centralwidget)
        self.stats_1_labels.setObjectName(u"stats_1_labels")
        self.stats_1_labels.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.stats_1_labels)

        self.stats_1 = QLabel(self.centralwidget)
        self.stats_1.setObjectName(u"stats_1")
        self.stats_1.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.stats_1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.stats_2_labels = QLabel(self.centralwidget)
        self.stats_2_labels.setObjectName(u"stats_2_labels")
        self.stats_2_labels.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stats_2_labels.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.stats_2_labels)

        self.stats_2 = QLabel(self.centralwidget)
        self.stats_2.setObjectName(u"stats_2")
        self.stats_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stats_2.setMargin(13)

        self.horizontalLayout_3.addWidget(self.stats_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 2, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setStyleSheet(u"\n"
"	background-color: rgb(132, 132, 132);\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.on_time = QLabel(self.centralwidget)
        self.on_time.setObjectName(u"on_time")
        sizePolicy2.setHeightForWidth(self.on_time.sizePolicy().hasHeightForWidth())
        self.on_time.setSizePolicy(sizePolicy2)
        self.on_time.setStyleSheet(u"font: 20pt \"Calibri\";\n"
"background-color: rgb(132, 132, 132);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(188, 214, 255);\n"
"border-radius: 10px;")
        self.on_time.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.on_time)

        self.phase_indicator = QLabel(self.centralwidget)
        self.phase_indicator.setObjectName(u"phase_indicator")
        sizePolicy2.setHeightForWidth(self.phase_indicator.sizePolicy().hasHeightForWidth())
        self.phase_indicator.setSizePolicy(sizePolicy2)
        self.phase_indicator.setMinimumSize(QSize(0, 32))
        self.phase_indicator.setStyleSheet(u"font: 20pt \"Calibri\";\n"
"background-color: rgb(85, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(188, 214, 255);\n"
"border-radius: 10px;")
        
        self.phase_indicator.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.phase_indicator)

        self.system_indicator = QLabel(self.centralwidget)
        self.system_indicator.setObjectName(u"system_indicator")
        sizePolicy2.setHeightForWidth(self.system_indicator.sizePolicy().hasHeightForWidth())
        self.system_indicator.setSizePolicy(sizePolicy2)
        self.system_indicator.setMinimumSize(QSize(0, 32))
        self.system_indicator.setStyleSheet(u"font: 20pt \"Calibri\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(188, 214, 255);\n"
"border-radius: 10px;")
        
        self.system_indicator.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.system_indicator)

        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.print_debug = QLabel(self.centralwidget)
        self.print_debug.setObjectName(u"print_debug")
        self.print_debug.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.print_debug, 2, 4, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1075, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"  status:  ", None))
        self.resize_button.setText(QCoreApplication.translate("MainWindow", u"Resize All Plots", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"  Plot Speed:  ", None))
        self.serial_port.setItemText(0, QCoreApplication.translate("MainWindow", u"COM4", None))

        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save Now", None))
        self.connect_button.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.data_points_in_file.setText(QCoreApplication.translate("MainWindow", u"Data Points", None))
        self.disconnect_button.setText(QCoreApplication.translate("MainWindow", u" Disconnect ", None))
        self.serial_baud.setItemText(0, QCoreApplication.translate("MainWindow", u"9600", None))
        self.serial_baud.setItemText(1, QCoreApplication.translate("MainWindow", u"14400", None))
        self.serial_baud.setItemText(2, QCoreApplication.translate("MainWindow", u"19200", None))
        self.serial_baud.setItemText(3, QCoreApplication.translate("MainWindow", u"28800", None))
        self.serial_baud.setItemText(4, QCoreApplication.translate("MainWindow", u"31250", None))
        self.serial_baud.setItemText(5, QCoreApplication.translate("MainWindow", u"38400", None))
        self.serial_baud.setItemText(6, QCoreApplication.translate("MainWindow", u"57600", None))
        self.serial_baud.setItemText(7, QCoreApplication.translate("MainWindow", u"115200", None))

        self.save_data_option.setText(QCoreApplication.translate("MainWindow", u"Auto Data Logging", None))
        self.stats_1_labels.setText(QCoreApplication.translate("MainWindow", u"Data Rate: \n"
"Packet Age:\n"
"Voltage:\n"
"RSSI:", None))
        self.stats_1.setText(QCoreApplication.translate("MainWindow", u"20 \n"
"000ms\n"
"3.2V\n"
"89%", None))
        self.stats_2_labels.setText(QCoreApplication.translate("MainWindow", u"Pyros: \n"
"GPS Lat: \n"
"GPS Lon: \n"
"GPS Alt:", None))
        self.stats_2.setText(QCoreApplication.translate("MainWindow", u"[1, 1] \n"
"12.234.124N \n"
"-12,34,5W \n"
"345m", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Mission Time", None))
        self.on_time.setText(QCoreApplication.translate("MainWindow", u"  000:00.000  ", None))
        self.phase_indicator.setText(QCoreApplication.translate("MainWindow", u"Phase: 1", None))
        self.system_indicator.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.print_debug.setText(QCoreApplication.translate("MainWindow", u"none", None))
    # retranslateUi

