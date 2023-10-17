# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QVBoxLayout, QWidget)

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
"\n"
"#radius_connection{\n"
"	background-color: rgba(249, 240, 107, 0.3);\n"
"	border-radius: 100px;\n"
"}")
        self.action_background = QAction(MainWindow)
        self.action_background.setObjectName(u"action_background")
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.map = QLabel(self.centralwidget)
        self.map.setObjectName(u"map")
        self.map.setGeometry(QRect(0, 0, 850, 650))
        self.camera = QLabel(self.centralwidget)
        self.camera.setObjectName(u"camera")
        self.camera.setGeometry(QRect(1000, 25, 200, 200))
        self.dron = QLabel(self.centralwidget)
        self.dron.setObjectName(u"dron")
        self.dron.setGeometry(QRect(120, 120, 100, 100))
        self.radius_connection = QLabel(self.centralwidget)
        self.radius_connection.setObjectName(u"radius_connection")
        self.radius_connection.setGeometry(QRect(120, 150, 200, 200))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1030, 240, 138, 41))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.control_speed = QLabel(self.layoutWidget)
        self.control_speed.setObjectName(u"control_speed")

        self.verticalLayout.addWidget(self.control_speed)

        self.speed_limiter = QSlider(self.layoutWidget)
        self.speed_limiter.setObjectName(u"speed_limiter")
        self.speed_limiter.setMinimum(1)
        self.speed_limiter.setMaximum(10)
        self.speed_limiter.setOrientation(Qt.Horizontal)
        self.speed_limiter.setInvertedAppearance(False)
        self.speed_limiter.setInvertedControls(False)

        self.verticalLayout.addWidget(self.speed_limiter)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(1030, 340, 141, 60))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(1030, 290, 141, 41))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.error = QLabel(self.layoutWidget2)
        self.error.setObjectName(u"error")
        self.error.setEnabled(False)

        self.verticalLayout_3.addWidget(self.error)

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
#if QT_CONFIG(shortcut)
        self.action_exit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.map.setText("")
        self.camera.setText("")
        self.dron.setText("")
        self.radius_connection.setText("")
        self.control_speed.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u044c \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u0438", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u044b\u0432 \u0441\u0432\u044f\u0437\u0438", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0437\u0432\u0440\u0430\u0442", None))
        self.error.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

