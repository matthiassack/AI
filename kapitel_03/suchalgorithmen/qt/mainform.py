# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainform.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(900, 600)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.suchenButton = QPushButton(self.centralwidget)
        self.suchenButton.setObjectName(u"suchenButton")
        self.suchenButton.setGeometry(QRect(500, 30, 121, 31))
        font = QFont()
        font.setPointSize(11)
        self.suchenButton.setFont(font)
        self.comboSuche = QComboBox(self.centralwidget)
        self.comboSuche.addItem("")
        self.comboSuche.addItem("")
        self.comboSuche.setObjectName(u"comboSuche")
        self.comboSuche.setGeometry(QRect(50, 30, 161, 31))
        self.comboSuche.setFont(font)
        self.labelHoehe = QLabel(self.centralwidget)
        self.labelHoehe.setObjectName(u"labelHoehe")
        self.labelHoehe.setGeometry(QRect(260, 30, 81, 31))
        self.labelHoehe.setFont(font)
        self.labelBreite = QLabel(self.centralwidget)
        self.labelBreite.setObjectName(u"labelBreite")
        self.labelBreite.setGeometry(QRect(260, 70, 81, 31))
        self.labelBreite.setFont(font)
        self.editHoehe = QTextEdit(self.centralwidget)
        self.editHoehe.setObjectName(u"editHoehe")
        self.editHoehe.setGeometry(QRect(330, 30, 104, 31))
        self.editHoehe.setFont(font)
        self.editBreite = QTextEdit(self.centralwidget)
        self.editBreite.setObjectName(u"editBreite")
        self.editBreite.setGeometry(QRect(330, 70, 104, 31))
        self.editBreite.setFont(font)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Suchalgorithmen", None))
        self.suchenButton.setText(QCoreApplication.translate("mainWindow", u"Suchen", None))
        self.comboSuche.setItemText(0, QCoreApplication.translate("mainWindow", u"Breitensuche", None))
        self.comboSuche.setItemText(1, QCoreApplication.translate("mainWindow", u"Tiefensuche", None))

        self.labelHoehe.setText(QCoreApplication.translate("mainWindow", u"H\u00f6he", None))
        self.labelBreite.setText(QCoreApplication.translate("mainWindow", u"Breite", None))
    # retranslateUi

