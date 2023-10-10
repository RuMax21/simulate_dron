# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setStyleSheet(u"#map{\n"
"	background-color: red;\n"
"}\n"
"\n"
"#camera{\n"
"	background-color: gray;\n"
"}\n"
"")
        self.action_background = QAction(MainWindow)
        self.action_background.setObjectName(u"action_background")
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.map = QLabel(self.centralwidget)
        self.map.setObjectName(u"map")
        self.map.setGeometry(QRect(35, 25, 850, 650))
        self.camera = QLabel(self.centralwidget)
        self.camera.setObjectName(u"camera")
        self.camera.setGeometry(QRect(1000, 25, 200, 200))
        self.dron = QLabel(self.centralwidget)
        self.dron.setObjectName(u"dron")
        self.dron.setGeometry(QRect(120, 120, 100, 100))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.action_background)
        self.menuFile.addAction(self.action_exit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_background.setText(QCoreApplication.translate("MainWindow", u"Change image for map", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.map.setText("")
        self.camera.setText("")
        self.dron.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

