# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pengumuman.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableView, QTextEdit,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(492, 401)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 121, 31))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.tablePengumuman = QTableView(Form)
        self.tablePengumuman.setObjectName(u"tablePengumuman")
        self.tablePengumuman.setGeometry(QRect(20, 280, 451, 111))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 70, 49, 16))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 110, 49, 16))
        self.lineJudul = QLineEdit(Form)
        self.lineJudul.setObjectName(u"lineJudul")
        self.lineJudul.setGeometry(QRect(100, 70, 113, 22))
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(100, 110, 271, 81))
        self.pushSimpan = QPushButton(Form)
        self.pushSimpan.setObjectName(u"pushSimpan")
        self.pushSimpan.setGeometry(QRect(150, 210, 75, 24))
        self.pushUbah = QPushButton(Form)
        self.pushUbah.setObjectName(u"pushUbah")
        self.pushUbah.setGeometry(QRect(250, 210, 75, 24))
        self.pushHapus = QPushButton(Form)
        self.pushHapus.setObjectName(u"pushHapus")
        self.pushHapus.setGeometry(QRect(350, 210, 75, 24))
        self.pushReset = QPushButton(Form)
        self.pushReset.setObjectName(u"pushReset")
        self.pushReset.setGeometry(QRect(50, 210, 75, 24))
        self.lineCari = QLineEdit(Form)
        self.lineCari.setObjectName(u"lineCari")
        self.lineCari.setGeometry(QRect(20, 250, 451, 22))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Pengumuman", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Judul", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Isi", None))
        self.pushSimpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.pushUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.pushHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.pushReset.setText(QCoreApplication.translate("Form", u"Reset", None))
    # retranslateUi
