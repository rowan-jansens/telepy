# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gsui.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
    QStatusBar, QTabWidget, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1075, 638)
        MainWindow.setStyleSheet(u"QMainWindow#MainWindow{\n"
"background-color:rgb(53, 53, 53);\n"
"}")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"	background-color: rgb(58, 58, 58);\n"
"}")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.resize_button = QPushButton(self.centralwidget)
        self.resize_button.setObjectName(u"resize_button")
        self.resize_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(132, 132, 132);\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(100, 100, 100);\n"
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

        self.gridLayout_2.addWidget(self.resize_button, 3, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(240, 100))
        self.label.setText(u"")
        self.label.setPixmap(QPixmap(u"telepy_name.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.phase_indicator = QLabel(self.centralwidget)
        self.phase_indicator.setObjectName(u"phase_indicator")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.phase_indicator.sizePolicy().hasHeightForWidth())
        self.phase_indicator.setSizePolicy(sizePolicy1)
        self.phase_indicator.setMinimumSize(QSize(0, 32))
        self.phase_indicator.setStyleSheet(u"font: 20pt \"Calibri\";\n"
"background-color: rgb(85, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(188, 214, 255);\n"
"border-radius: 10px;")
        self.phase_indicator.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.phase_indicator, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(132, 132, 132);\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(100, 100, 100);\n"
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

        self.gridLayout.addWidget(self.save_button, 5, 1, 1, 1)

        self.save_data_option = QCheckBox(self.centralwidget)
        self.save_data_option.setObjectName(u"save_data_option")
        self.save_data_option.setStyleSheet(u"QCheckBox {\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.save_data_option, 4, 1, 1, 2)

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

        self.gridLayout.addWidget(self.serial_baud, 2, 2, 1, 1)

        self.disconnect_button = QPushButton(self.centralwidget)
        self.disconnect_button.setObjectName(u"disconnect_button")
        self.disconnect_button.setStyleSheet(u"QPushButton {\n"
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
"	background-color: rgb(191, 64, 0);\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"")

        self.gridLayout.addWidget(self.disconnect_button, 2, 1, 1, 1)

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
"	background-color: rgb(67, 135, 202);\n"
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

        self.gridLayout.addWidget(self.connect_button, 0, 1, 1, 1)

        self.data_points_in_file = QLabel(self.centralwidget)
        self.data_points_in_file.setObjectName(u"data_points_in_file")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.data_points_in_file.sizePolicy().hasHeightForWidth())
        self.data_points_in_file.setSizePolicy(sizePolicy2)
        self.data_points_in_file.setMinimumSize(QSize(0, 4))
        self.data_points_in_file.setStyleSheet(u"font: 9pt \"Segoe UI\";\n"
"background-color: rgb(132, 132, 132);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(188, 214, 255);\n"
"border-radius: 5px;")
        self.data_points_in_file.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.data_points_in_file, 5, 2, 1, 1)

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

        self.gridLayout.addWidget(self.serial_port, 0, 2, 1, 1)

        self.on_time = QLabel(self.centralwidget)
        self.on_time.setObjectName(u"on_time")
        sizePolicy1.setHeightForWidth(self.on_time.sizePolicy().hasHeightForWidth())
        self.on_time.setSizePolicy(sizePolicy1)
        self.on_time.setStyleSheet(u"font: 20pt \"Calibri\";\n"
"background-color: rgb(132, 132, 132);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(188, 214, 255);\n"
"border-radius: 10px;")
        self.on_time.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.on_time, 6, 1, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 3, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setMargin(13)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 2, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Orientation = PlotWidget(self.centralwidget)
        self.Orientation.setObjectName(u"Orientation")
        self.Orientation.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.Orientation, 0, 2, 1, 1)

        self.Gyro = PlotWidget(self.centralwidget)
        self.Gyro.setObjectName(u"Gyro")
        self.Gyro.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.Gyro, 0, 1, 1, 1)

        self.Accel = PlotWidget(self.centralwidget)
        self.Accel.setObjectName(u"Accel")
        self.Accel.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.Accel, 0, 0, 1, 1)

        self.Altitude = PlotWidget(self.centralwidget)
        self.Altitude.setObjectName(u"Altitude")
        self.Altitude.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.Altitude, 1, 1, 1, 1)

        self.Velocity = PlotWidget(self.centralwidget)
        self.Velocity.setObjectName(u"Velocity")
        self.Velocity.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.Velocity, 1, 2, 1, 1)

        self.Position = PlotWidget(self.centralwidget)
        self.Position.setObjectName(u"Position")
        self.Position.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.Position, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 2, 0, 1, 4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.plot_speed = QSlider(self.centralwidget)
        self.plot_speed.setObjectName(u"plot_speed")
        sizePolicy2.setHeightForWidth(self.plot_speed.sizePolicy().hasHeightForWidth())
        self.plot_speed.setSizePolicy(sizePolicy2)
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


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 3, 1, 1, 1)

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
        self.resize_button.setText(QCoreApplication.translate("MainWindow", u"Resize All Plots", None))
        self.phase_indicator.setText(QCoreApplication.translate("MainWindow", u"Phase: 1", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save Now", None))
        self.save_data_option.setText(QCoreApplication.translate("MainWindow", u"Auto Data Logging", None))
        self.serial_baud.setItemText(0, QCoreApplication.translate("MainWindow", u"9600", None))
        self.serial_baud.setItemText(1, QCoreApplication.translate("MainWindow", u"14400", None))
        self.serial_baud.setItemText(2, QCoreApplication.translate("MainWindow", u"19200", None))
        self.serial_baud.setItemText(3, QCoreApplication.translate("MainWindow", u"28800", None))
        self.serial_baud.setItemText(4, QCoreApplication.translate("MainWindow", u"31250", None))
        self.serial_baud.setItemText(5, QCoreApplication.translate("MainWindow", u"38400", None))
        self.serial_baud.setItemText(6, QCoreApplication.translate("MainWindow", u"57600", None))
        self.serial_baud.setItemText(7, QCoreApplication.translate("MainWindow", u"115200", None))

        self.disconnect_button.setText(QCoreApplication.translate("MainWindow", u" Disconnect ", None))
        self.connect_button.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.data_points_in_file.setText(QCoreApplication.translate("MainWindow", u"Data Points", None))
        self.serial_port.setItemText(0, QCoreApplication.translate("MainWindow", u"COM4", None))

        self.on_time.setText(QCoreApplication.translate("MainWindow", u"  000:00.000  ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pyro 1: \n"
"Pyro 2: \n"
"GPS Lat: \n"
"GPS Lon: \n"
"GPS Alt: \n"
"Data Rate: \n"
"Packet Age:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"cont\n"
"cont \n"
"12.234.124N \n"
"-12,34,5W \n"
"345m \n"
"20 \n"
"000ms", None))
    # retranslateUi

