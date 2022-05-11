# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow_greenhslsVf.ui'
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
        MainWindow.resize(420, 694)
        MainWindow.setAcceptDrops(True)
        MainWindow.setWindowTitle(u"Sticky Notes")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setAutoFillBackground(False)
        self.centralWidget.setStyleSheet(u"background-color: rgb(195, 195, 195);\n"
"QPushButton {border: 0px;}")
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.centralWidget)
        self.header.setObjectName(u"header")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy1)
        self.header.setMinimumSize(QSize(0, 28))
        self.header.setMaximumSize(QSize(16777215, 25))
        self.header.setAutoFillBackground(False)
        self.header.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.moreButton = QPushButton(self.header)
        self.moreButton.setObjectName(u"moreButton")
        self.moreButton.setMinimumSize(QSize(25, 25))
        self.moreButton.setMaximumSize(QSize(25, 25))
        self.moreButton.setBaseSize(QSize(2, 0))
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.moreButton.setFont(font)
        self.moreButton.setLayoutDirection(Qt.LeftToRight)
        self.moreButton.setText(u"\ud83d\udfa2")
        self.moreButton.setIconSize(QSize(12, 12))

        self.horizontalLayout_2.addWidget(self.moreButton)

        self.deleteButton = QPushButton(self.header)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setMinimumSize(QSize(25, 25))
        self.deleteButton.setMaximumSize(QSize(25, 25))
        self.deleteButton.setBaseSize(QSize(2, 0))
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(False)
        font1.setWeight(50)
        self.deleteButton.setFont(font1)
        self.deleteButton.setLayoutDirection(Qt.LeftToRight)
        self.deleteButton.setStyleSheet(u"color: rgb(170, 0, 0);")
        self.deleteButton.setText(u"-")
        self.deleteButton.setFlat(True)

        self.horizontalLayout_2.addWidget(self.deleteButton)

        self.horizontalSpacer = QSpacerItem(259, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.closeButton = QPushButton(self.header)
        self.closeButton.setObjectName(u"closeButton")
        sizePolicy1.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy1)
        self.closeButton.setMinimumSize(QSize(25, 25))
        self.closeButton.setMaximumSize(QSize(25, 25))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setWeight(50)
        self.closeButton.setFont(font2)
#if QT_CONFIG(statustip)
        self.closeButton.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.closeButton.setText(u"\u00d7")
        self.closeButton.setFlat(True)

        self.horizontalLayout_2.addWidget(self.closeButton)


        self.verticalLayout.addWidget(self.header)

        self.textEdit = QTextEdit(self.centralWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setPointSize(14)
        self.textEdit.setFont(font3)
        self.textEdit.setStyleSheet(u"")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setFrameShadow(QFrame.Plain)
        self.textEdit.setLineWidth(0)

        self.verticalLayout.addWidget(self.textEdit)

        self.line = QFrame(self.centralWidget)
        self.line.setObjectName(u"line")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy3)
        self.line.setMaximumSize(QSize(16777215, 1))
        font4 = QFont()
        font4.setPointSize(1)
        self.line.setFont(font4)
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet(u"background-color: rgb(195, 195, 195);")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line)

        self.footer = QWidget(self.centralWidget)
        self.footer.setObjectName(u"footer")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.footer.sizePolicy().hasHeightForWidth())
        self.footer.setSizePolicy(sizePolicy4)
        self.footer.setMaximumSize(QSize(16777215, 25))
        self.footer.setLayoutDirection(Qt.LeftToRight)
        self.footer.setAutoFillBackground(False)
        self.footer.setStyleSheet(u"QPushButton::checked{	background-color: rgba(195, 195, 195, 150);}")
        self.footerLayout = QHBoxLayout(self.footer)
        self.footerLayout.setSpacing(5)
        self.footerLayout.setContentsMargins(11, 11, 11, 11)
        self.footerLayout.setObjectName(u"footerLayout")
        self.footerLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.footerLayout.setContentsMargins(0, 0, 0, 0)
        self.boldButton = QPushButton(self.footer)
        self.boldButton.setObjectName(u"boldButton")
        self.boldButton.setMinimumSize(QSize(23, 23))
        self.boldButton.setMaximumSize(QSize(23, 23))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.boldButton.setFont(font5)
        self.boldButton.setText(u"B")
        self.boldButton.setCheckable(True)
        self.boldButton.setFlat(False)

        self.footerLayout.addWidget(self.boldButton)

        self.italicButton = QPushButton(self.footer)
        self.italicButton.setObjectName(u"italicButton")
        self.italicButton.setMinimumSize(QSize(23, 23))
        self.italicButton.setMaximumSize(QSize(23, 23))
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(False)
        font6.setItalic(True)
        font6.setWeight(50)
        self.italicButton.setFont(font6)
        self.italicButton.setText(u"I")
        self.italicButton.setCheckable(True)

        self.footerLayout.addWidget(self.italicButton)

        self.underlineButton = QPushButton(self.footer)
        self.underlineButton.setObjectName(u"underlineButton")
        self.underlineButton.setMinimumSize(QSize(23, 23))
        self.underlineButton.setMaximumSize(QSize(23, 23))
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(False)
        font7.setUnderline(True)
        font7.setWeight(50)
        self.underlineButton.setFont(font7)
        self.underlineButton.setText(u"U")
        self.underlineButton.setCheckable(True)

        self.footerLayout.addWidget(self.underlineButton)

        self.strikeoutButton = QPushButton(self.footer)
        self.strikeoutButton.setObjectName(u"strikeoutButton")
        self.strikeoutButton.setMinimumSize(QSize(23, 23))
        self.strikeoutButton.setMaximumSize(QSize(23, 23))
        font8 = QFont()
        font8.setPointSize(12)
        font8.setBold(False)
        font8.setWeight(50)
        font8.setStrikeOut(True)
        self.strikeoutButton.setFont(font8)
        self.strikeoutButton.setText(u"S")
        self.strikeoutButton.setCheckable(True)
        self.strikeoutButton.setChecked(False)

        self.footerLayout.addWidget(self.strikeoutButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.footerLayout.addItem(self.horizontalSpacer_2)

#---------------------------------------------------------------------------
        self.sizegrip = QSizeGrip(MainWindow)
        #
        self.footerLayout.addWidget(self.sizegrip, alignment=Qt.AlignRight | Qt.AlignBottom)
        #self.sizegrip.set
        self.verticalLayout.addWidget(self.footer)
        #self.verticalLayout.addWidget(self.sizegrip)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        pass
    # retranslateUi


