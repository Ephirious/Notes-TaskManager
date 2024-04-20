# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WindowAccountLogin.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import res_rc

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(365, 380)
        LoginWindow.setMinimumSize(QSize(365, 380))
        LoginWindow.setMaximumSize(QSize(365, 380))
        icon = QIcon()
        icon.addFile(u":/icons/icons/axolot.png", QSize(), QIcon.Normal, QIcon.Off)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setStyleSheet(u"background-color: rgb(216, 193, 219)")
        self.label_App = QLabel(LoginWindow)
        self.label_App.setObjectName(u"label_App")
        self.label_App.setGeometry(QRect(97, 9, 171, 25))
        self.label_App.setMaximumSize(QSize(300, 45))
        font = QFont()
        font.setFamilies([u"Snap ITC"])
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        self.label_App.setFont(font)
        self.label_App.setStyleSheet(u"font: 15pt \"Snap ITC\";")
        self.label_App.setTextFormat(Qt.TextFormat.AutoText)
        self.label_App.setScaledContents(True)
        self.label_log = QLabel(LoginWindow)
        self.label_log.setObjectName(u"label_log")
        self.label_log.setGeometry(QRect(160, 40, 45, 16))
        font1 = QFont()
        font1.setFamilies([u"Sitka Subheading Semibold"])
        font1.setPointSize(11)
        font1.setWeight(QFont.DemiBold)
        font1.setItalic(False)
        self.label_log.setFont(font1)
        self.label_log.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_log.setStyleSheet(u"font: 600 11pt \"Sitka Subheading Semibold\";")
        self.label_error = QLabel(LoginWindow)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setGeometry(QRect(20, 180, 331, 71))
        self.layoutWidget = QWidget(LoginWindow)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(140, 320, 77, 54))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_reg = QPushButton(self.layoutWidget)
        self.btn_reg.setObjectName(u"btn_reg")
        self.btn_reg.setStyleSheet(u"background-color: white;\n"
"font: 11pt \"Sitka\";\n"
"")

        self.verticalLayout_2.addWidget(self.btn_reg)

        self.btn_login = QPushButton(self.layoutWidget)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setStyleSheet(u"background-color: white;\n"
"font: 11pt \"Sitka\";\n"
"")

        self.verticalLayout_2.addWidget(self.btn_login)

        self.layoutWidget1 = QWidget(LoginWindow)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 62, 347, 47))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_name = QLabel(self.layoutWidget1)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setMinimumSize(QSize(345, 0))
        self.label_name.setMaximumSize(QSize(400, 300))
        font2 = QFont()
        font2.setFamilies([u"Sitka"])
        font2.setPointSize(13)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_name.setFont(font2)
        self.label_name.setStyleSheet(u"\n"
"font: 13pt \"Sitka\";\n"
"")

        self.verticalLayout.addWidget(self.label_name)

        self.lineEdit_name = QLineEdit(self.layoutWidget1)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setMinimumSize(QSize(345, 22))
        self.lineEdit_name.setStyleSheet(u"background-color: white;")
        self.lineEdit_name.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.lineEdit_name)

        self.layoutWidget2 = QWidget(LoginWindow)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(12, 122, 347, 45))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_password = QLabel(self.layoutWidget2)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setMinimumSize(QSize(345, 0))
        self.label_password.setMaximumSize(QSize(400, 300))
        font3 = QFont()
        font3.setFamilies([u"Sitka"])
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setItalic(False)
        self.label_password.setFont(font3)
        self.label_password.setStyleSheet(u"font: 11pt \"Sitka\";")

        self.verticalLayout_3.addWidget(self.label_password)

        self.lineEdit_password = QLineEdit(self.layoutWidget2)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setMinimumSize(QSize(345, 22))
        self.lineEdit_password.setMaximumSize(QSize(345, 22))
        self.lineEdit_password.setStyleSheet(u"background-color: white;\n"
"")
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.lineEdit_password.setClearButtonEnabled(True)

        self.verticalLayout_3.addWidget(self.lineEdit_password)


        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Axolot's Notes - Login window", None))
        self.label_App.setText(QCoreApplication.translate("LoginWindow", u"Axolot's Notes", None))
        self.label_log.setText(QCoreApplication.translate("LoginWindow", u"LOGIN", None))
        self.label_error.setText("")
        self.btn_reg.setText(QCoreApplication.translate("LoginWindow", u"Sign up", None))
        self.btn_login.setText(QCoreApplication.translate("LoginWindow", u"Log in", None))
        self.label_name.setText(QCoreApplication.translate("LoginWindow", u"Name", None))
        self.label_password.setText(QCoreApplication.translate("LoginWindow", u"Password", None))
    # retranslateUi

