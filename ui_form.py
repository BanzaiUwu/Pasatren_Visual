# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionSantri = QAction(MainWindow)
        self.actionSantri.setObjectName(u"actionSantri")
        self.actionProgram = QAction(MainWindow)
        self.actionProgram.setObjectName(u"actionProgram")
        self.actionPembayaran = QAction(MainWindow)
        self.actionPembayaran.setObjectName(u"actionPembayaran")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuMain = QMenu(self.menubar)
        self.menuMain.setObjectName(u"menuMain")
        self.menuPengumuman = QMenu(self.menubar)
        self.menuPengumuman.setObjectName(u"menuPengumuman")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuPengumuman.menuAction())
        self.menuMain.addAction(self.actionSantri)
        self.menuMain.addAction(self.actionProgram)
        self.menuMain.addAction(self.actionPembayaran)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSantri.setText(QCoreApplication.translate("MainWindow", u"Santri", None))
        self.actionProgram.setText(QCoreApplication.translate("MainWindow", u"Program", None))
        self.actionPembayaran.setText(QCoreApplication.translate("MainWindow", u"Pembayaran", None))
        self.menuMain.setTitle(QCoreApplication.translate("MainWindow", u"Main", None))
        self.menuPengumuman.setTitle(QCoreApplication.translate("MainWindow", u"Pengumuman", None))
    # retranslateUi
