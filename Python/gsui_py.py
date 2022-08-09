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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QWidget)

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
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(160, 230, 581, 331))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Accel = PlotWidget(self.gridLayoutWidget)
        self.Accel.setObjectName(u"Accel")

        self.gridLayout_2.addWidget(self.Accel, 0, 0, 1, 1)

        self.Gyro = PlotWidget(self.gridLayoutWidget)
        self.Gyro.setObjectName(u"Gyro")

        self.gridLayout_2.addWidget(self.Gyro, 1, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 411, 51))
        self.label.setStyleSheet(u"font: 26pt \"Calibri\";\n"
"background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(188, 214, 255);\n"
"border-radius: 10px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.connect_button = QPushButton(self.centralwidget)
        self.connect_button.setObjectName(u"connect_button")
        self.connect_button.setGeometry(QRect(40, 80, 75, 24))
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
        self.disconnect_button = QPushButton(self.centralwidget)
        self.disconnect_button.setObjectName(u"disconnect_button")
        self.disconnect_button.setGeometry(QRect(130, 80, 75, 24))
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Phenoix VI Ground Controll", None))
        self.connect_button.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.disconnect_button.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
    # retranslateUi

