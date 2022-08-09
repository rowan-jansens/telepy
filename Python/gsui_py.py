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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(893, 638)
        MainWindow.setStyleSheet(u"QMainWindow#MainWindow{\n"
"background-color:rgb(85, 170, 255)\n"
"}")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"	background-color: rgb(58, 58, 58);\n"
"}")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
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


        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 0, 1, 3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.connect_button = QPushButton(self.centralwidget)
        self.connect_button.setObjectName(u"connect_button")
        self.connect_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(67, 135, 202)\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(85, 170, 0)\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"")

        self.gridLayout.addWidget(self.connect_button, 0, 0, 1, 1)

        self.serial_port = QComboBox(self.centralwidget)
        self.serial_port.setObjectName(u"serial_port")

        self.gridLayout.addWidget(self.serial_port, 0, 1, 1, 1)

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
"	background-color: rgb(67, 135, 202)\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(85, 170, 0)\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"")

        self.gridLayout.addWidget(self.disconnect_button, 2, 0, 1, 1)

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

        self.gridLayout.addWidget(self.serial_baud, 2, 1, 1, 1)

        self.resize_button = QPushButton(self.centralwidget)
        self.resize_button.setObjectName(u"resize_button")
        self.resize_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(117, 117, 117);\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(67, 135, 202)\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(85, 170, 0)\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}")

        self.gridLayout.addWidget(self.resize_button, 3, 0, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 26pt \"Calibri\";\n"
"background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(188, 214, 255);\n"
"border-radius: 10px;")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 893, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.connect_button.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.disconnect_button.setText(QCoreApplication.translate("MainWindow", u" Disconnect ", None))
        self.serial_baud.setItemText(0, QCoreApplication.translate("MainWindow", u"9600", None))
        self.serial_baud.setItemText(1, QCoreApplication.translate("MainWindow", u"14400", None))
        self.serial_baud.setItemText(2, QCoreApplication.translate("MainWindow", u"19200", None))
        self.serial_baud.setItemText(3, QCoreApplication.translate("MainWindow", u"28800", None))
        self.serial_baud.setItemText(4, QCoreApplication.translate("MainWindow", u"31250", None))
        self.serial_baud.setItemText(5, QCoreApplication.translate("MainWindow", u"38400", None))
        self.serial_baud.setItemText(6, QCoreApplication.translate("MainWindow", u"57600", None))
        self.serial_baud.setItemText(7, QCoreApplication.translate("MainWindow", u"115200", None))

        self.resize_button.setText(QCoreApplication.translate("MainWindow", u"Resize All Plots", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u" Phenoix VI Ground Controll ", None))
    # retranslateUi

