# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow_newgyUGcG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(322, 541)
        MainWindow.setAcceptDrops(True)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(233, 209, 97);")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.centralWidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 27))
        self.header.setMaximumSize(QSize(16777215, 27))
        self.header.setStyleSheet(u"background-color: rgb(233, 209, 97);")
        self.headerLayout = QHBoxLayout(self.header)
        self.headerLayout.setSpacing(2)
        self.headerLayout.setContentsMargins(0, 0, 0, 0)
        self.headerLayout.setObjectName(u"headerLayout")
        self.moreButton = QPushButton(self.header)
        self.moreButton.setObjectName(u"moreButton")
        self.moreButton.setMinimumSize(QSize(25, 25))
        self.moreButton.setMaximumSize(QSize(25, 25))
        self.moreButton.setBaseSize(QSize(2, 0))
        font = QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.moreButton.setFont(font)
        self.moreButton.setLayoutDirection(Qt.LeftToRight)
        self.moreButton.setStyleSheet(u"QPushButton {\n"
"    border: 0px;\n"
"}")

        self.headerLayout.addWidget(self.moreButton)

        self.deleteButton = QPushButton(self.header)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setMinimumSize(QSize(25, 25))
        self.deleteButton.setMaximumSize(QSize(25, 25))
        self.deleteButton.setBaseSize(QSize(2, 0))
        self.deleteButton.setFont(font)
        self.deleteButton.setLayoutDirection(Qt.LeftToRight)
        self.deleteButton.setStyleSheet(u"QPushButton {\n"
"    border: 0px;\n"
"}")

        self.headerLayout.addWidget(self.deleteButton)

        self.horizontalSpacer = QSpacerItem(237, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.headerLayout.addItem(self.horizontalSpacer)

        self.closeButton = QPushButton(self.header)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(25, 25))
        self.closeButton.setMaximumSize(QSize(25, 25))
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet(u"QPushButton {\n"
"    border: 0px;\n"
"}")

        self.headerLayout.addWidget(self.closeButton)


        self.verticalLayout.addWidget(self.header)

        self.line = QFrame(self.centralWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.textEdit = QTextEdit(self.centralWidget)
        self.textEdit.setObjectName(u"textEdit")
        font1 = QFont()
        font1.setPointSize(18)
        self.textEdit.setFont(font1)
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setFrameShadow(QFrame.Plain)
        self.textEdit.setLineWidth(0)

        self.verticalLayout.addWidget(self.textEdit)

        self.line_2 = QFrame(self.centralWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.statusBarLayout = QHBoxLayout()
        self.statusBarLayout.setSpacing(6)
        self.statusBarLayout.setObjectName(u"statusBarLayout")
        self.boldButton = QPushButton(self.centralWidget)
        self.boldButton.setObjectName(u"boldButton")
        self.boldButton.setMinimumSize(QSize(23, 23))
        self.boldButton.setMaximumSize(QSize(23, 23))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.boldButton.setFont(font2)
        self.boldButton.setStyleSheet(u"QPushButton {\n"
"    border: 0px;\n"
"}")
        self.boldButton.setCheckable(True)
        
        self.statusBarLayout.addWidget(self.boldButton)

        self.italicButton = QPushButton(self.centralWidget)
        self.italicButton.setObjectName(u"italicButton")
        self.italicButton.setMinimumSize(QSize(23, 23))
        self.italicButton.setMaximumSize(QSize(23, 23))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(True)
        font3.setWeight(50)
        self.italicButton.setFont(font3)
        self.italicButton.setStyleSheet(u"QPushButton {\n"
"    border: 0px;\n"
"}")

        self.statusBarLayout.addWidget(self.italicButton)

        self.underlineButton = QPushButton(self.centralWidget)
        self.underlineButton.setObjectName(u"underlineButton")
        self.underlineButton.setMinimumSize(QSize(23, 23))
        self.underlineButton.setMaximumSize(QSize(23, 23))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setUnderline(True)
        font4.setWeight(50)
        self.underlineButton.setFont(font4)
        self.underlineButton.setStyleSheet(u"QPushButton {\n"
"    border: 0px;\n"
"}")

        self.statusBarLayout.addWidget(self.underlineButton)

        self.strikeoutButton = QPushButton(self.centralWidget)
        self.strikeoutButton.setObjectName(u"strikeoutButton")
        self.strikeoutButton.setMinimumSize(QSize(23, 23))
        self.strikeoutButton.setMaximumSize(QSize(23, 23))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setWeight(50)
        font5.setStrikeOut(True)
        self.strikeoutButton.setFont(font5)
        self.strikeoutButton.setStyleSheet(u"QPushButton {\n"
"    border: 0px;\n"
"}")

        self.statusBarLayout.addWidget(self.strikeoutButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.statusBarLayout.addItem(self.horizontalSpacer_2)


        self.sizegrip = QSizeGrip(MainWindow)
        self.statusBarLayout.addWidget(self.sizegrip)

        # layout = QVBoxLayout()
  
        # layout.addWidget(sizegrip, 0, Qt.AlignBottom | Qt.AlignRight)
        # MainWindow.setLayout(layout)


        self.verticalLayout.addLayout(self.statusBarLayout)

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sticky Notes", None))
        self.moreButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.closeButton.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.boldButton.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.italicButton.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.underlineButton.setText(QCoreApplication.translate("MainWindow", u"U", None))
        self.strikeoutButton.setText(QCoreApplication.translate("MainWindow", u"S", None))
    # retranslateUi

