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
        LoginWindow.resize(498, 514)
        LoginWindow.setMinimumSize(QSize(498, 514))
        LoginWindow.setMaximumSize(QSize(498, 514))
        icon = QIcon()
        icon.addFile(u":/icons/icons/axolot.png", QSize(), QIcon.Normal, QIcon.Off)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setStyleSheet(u"background-color: rgb(216, 193, 219)")
        self.label_error = QLabel(LoginWindow)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setGeometry(QRect(40, 240, 421, 121))
        self.label_error.setStyleSheet(u"background-color: none;\n"
"")
        self.layoutWidget = QWidget(LoginWindow)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(170, 380, 161, 121))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_reg = QPushButton(self.layoutWidget)
        self.btn_reg.setObjectName(u"btn_reg")
        self.btn_reg.setStyleSheet(u"QPushButton {\n"
"background-color: white;\n"
"font: 11pt \"Sitka\";\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(225, 225, 225);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(225, 225, 225);\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_reg)

        self.btn_login = QPushButton(self.layoutWidget)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setStyleSheet(u"QPushButton {\n"
"background-color: white;\n"
"font: 11pt \"Sitka\";\n"
"color: black;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(225, 225, 225);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(225, 225, 225);\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_login)

        self.btn_login.raise_()
        self.btn_reg.raise_()
        self.layoutWidget1 = QWidget(LoginWindow)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(40, 100, 421, 131))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_name = QLabel(self.layoutWidget1)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setMinimumSize(QSize(345, 0))
        self.label_name.setMaximumSize(QSize(400, 300))
        font = QFont()
        font.setFamilies([u"Sitka"])
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet(u"font: 13pt \"Sitka\";\n"
"background-color: none;\n"
"")

        self.verticalLayout.addWidget(self.label_name)

        self.lineEdit_name = QLineEdit(self.layoutWidget1)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setMinimumSize(QSize(345, 22))
        self.lineEdit_name.setStyleSheet(u"QLineEdit {\n"
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
        self.lineEdit_name.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_name.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.lineEdit_name)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_password = QLabel(self.layoutWidget1)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setMinimumSize(QSize(345, 0))
        self.label_password.setMaximumSize(QSize(400, 300))
        self.label_password.setFont(font)
        self.label_password.setStyleSheet(u"font: 13pt \"Sitka\";\n"
"background-color: none;")

        self.verticalLayout_3.addWidget(self.label_password)

        self.lineEdit_password = QLineEdit(self.layoutWidget1)
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
        self.lineEdit_password.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_password.setClearButtonEnabled(True)

        self.verticalLayout_3.addWidget(self.lineEdit_password)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.layoutWidget2 = QWidget(LoginWindow)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(140, 10, 211, 81))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_App = QLabel(self.layoutWidget2)
        self.label_App.setObjectName(u"label_App")
        font1 = QFont()
        font1.setFamilies([u"Snap ITC"])
        font1.setPointSize(17)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        self.label_App.setFont(font1)
        self.label_App.setStyleSheet(u"font: 17pt \"Snap ITC\";\n"
"background-color: none;")
        self.label_App.setTextFormat(Qt.TextFormat.AutoText)
        self.label_App.setScaledContents(True)
        self.label_App.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_App)

        self.label_log = QLabel(self.layoutWidget2)
        self.label_log.setObjectName(u"label_log")
        self.label_log.setFont(font)
        self.label_log.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_log.setStyleSheet(u"font: 13pt \"Sitka\";;\n"
"background-color: none;\n"
"")
        self.label_log.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_log, 0, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Axolot's Notes - Login window", None))
        self.label_error.setText("")
        self.btn_reg.setText(QCoreApplication.translate("LoginWindow", u"Sign up", None))
        self.btn_login.setText(QCoreApplication.translate("LoginWindow", u"Log in", None))
        self.label_name.setText(QCoreApplication.translate("LoginWindow", u"Name:", None))
        self.lineEdit_name.setPlaceholderText("")
        self.label_password.setText(QCoreApplication.translate("LoginWindow", u"Password:", None))
        self.lineEdit_password.setPlaceholderText("")
        self.label_App.setText(QCoreApplication.translate("LoginWindow", u"Axolot's Notes", None))
#if QT_CONFIG(whatsthis)
        self.label_log.setWhatsThis(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_log.setText(QCoreApplication.translate("LoginWindow", u"LOG IN", None))
    # retranslateUi

