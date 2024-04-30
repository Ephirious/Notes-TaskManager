# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WindowSignin.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import res_rc

class Ui_SigninWindow(object):
    def setupUi(self, SigninWindow):
        if not SigninWindow.objectName():
            SigninWindow.setObjectName(u"SigninWindow")
        SigninWindow.resize(500, 600)
        SigninWindow.setMaximumSize(QSize(500, 600))
        icon = QIcon()
        icon.addFile(u":/icons/icons/axolot.png", QSize(), QIcon.Normal, QIcon.Off)
        SigninWindow.setWindowIcon(icon)
        SigninWindow.setStyleSheet(u"background-color: rgb(216, 193, 219);")
        self.verticalLayout_6 = QVBoxLayout(SigninWindow)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(50, -1, 50, -1)
        self.label = QLabel(SigninWindow)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Snap ITC"])
        font.setPointSize(27)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 27pt \"Snap ITC\";\n"
"background-color: none;")

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.Frame = QFrame(SigninWindow)
        self.Frame.setObjectName(u"Frame")
        self.Frame.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.Frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(30, -1, 30, -1)
        self.label_3 = QLabel(self.Frame)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Sitka"])
        font1.setPointSize(25)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"font: 25pt \"Sitka\";\n"
"background-color: none;\n"
"color: rgb(91, 61, 107)")

        self.verticalLayout_5.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_4.addLayout(self.verticalLayout_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(50, 40, 50, 40)
        self.label_login = QLabel(self.Frame)
        self.label_login.setObjectName(u"label_login")
        font2 = QFont()
        font2.setFamilies([u"Sitka"])
        font2.setPointSize(17)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_login.setFont(font2)
        self.label_login.setStyleSheet(u"font: 17pt \"Sitka\";\n"
"color: rgb(91, 61, 107)")

        self.verticalLayout.addWidget(self.label_login)

        self.lineEdit_login = QLineEdit(self.Frame)
        self.lineEdit_login.setObjectName(u"lineEdit_login")
        self.lineEdit_login.setStyleSheet(u"QLineEdit {\n"
"background-color: white;\n"
"font: 11pt \"Sitka\";\n"
"color: black;\n"
"}\n"
"QLineEdit:hover {\n"
"background-color: rgb(225, 225, 225);\n"
"}\n"
"\n"
"QLineEdit:pressed {\n"
"background-color: white;\n"
"}")
        self.lineEdit_login.setFrame(True)
        self.lineEdit_login.setReadOnly(False)
        self.lineEdit_login.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.lineEdit_login)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(50, 40, 50, 40)
        self.label_password = QLabel(self.Frame)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setFont(font2)
        self.label_password.setStyleSheet(u"font: 17pt \"Sitka\";\n"
"color: rgb(91, 61, 107)")

        self.verticalLayout_2.addWidget(self.label_password)

        self.lineEdit_password = QLineEdit(self.Frame)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setStyleSheet(u"QLineEdit {\n"
"background-color: white;\n"
"font: 11pt \"Sitka\";\n"
"color: black;\n"
"}\n"
"QLineEdit:hover {\n"
"background-color: rgb(225, 225, 225);\n"
"}\n"
"\n"
"QLineEdit:pressed {\n"
"background-color: white;\n"
"}")
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.lineEdit_password.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.lineEdit_password)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.verticalLayout_6.addWidget(self.Frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.btn_signup = QPushButton(SigninWindow)
        self.btn_signup.setObjectName(u"btn_signup")
        font3 = QFont()
        font3.setFamilies([u"Sitka"])
        font3.setPointSize(15)
        font3.setBold(False)
        font3.setItalic(False)
        self.btn_signup.setFont(font3)
        self.btn_signup.setStyleSheet(u"QPushButton {\n"
"background-color: white;\n"
"font: 15pt \"Sitka\";\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(225, 225, 225);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(225, 225, 225);\n"
"}")

        self.verticalLayout_6.addWidget(self.btn_signup)


        self.retranslateUi(SigninWindow)

        QMetaObject.connectSlotsByName(SigninWindow)
    # setupUi

    def retranslateUi(self, SigninWindow):
        SigninWindow.setWindowTitle(QCoreApplication.translate("SigninWindow", u"Axolot's Notes - sign in", None))
        self.label.setText(QCoreApplication.translate("SigninWindow", u"Axolot's Notes", None))
        self.label_3.setText(QCoreApplication.translate("SigninWindow", u"Register", None))
        self.label_login.setText(QCoreApplication.translate("SigninWindow", u"Login:", None))
        self.lineEdit_login.setInputMask("")
        self.lineEdit_login.setText("")
        self.lineEdit_login.setPlaceholderText(QCoreApplication.translate("SigninWindow", u"Name", None))
        self.label_password.setText(QCoreApplication.translate("SigninWindow", u"Password:", None))
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("SigninWindow", u"Password", None))
        self.btn_signup.setText(QCoreApplication.translate("SigninWindow", u"Sign up", None))
    # retranslateUi

