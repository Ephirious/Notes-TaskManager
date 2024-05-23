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
        SigninWindow.setStyleSheet(u"background-color:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 227, 195, 255), stop:1 rgba(245, 78, 140, 255))")
        self.verticalLayout_7 = QVBoxLayout(SigninWindow)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(50, -1, 50, -1)
        self.label = QLabel(SigninWindow)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Ravie"])
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 30pt \"Ravie\";\n"
"font-weight: bold;\n"
"background-color: none;\n"
"color: white;")

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_3 = QLabel(SigninWindow)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Sitka"])
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"font: 20pt \"Sitka\";\n"
"background-color: none;\n"
"color: black;\n"
"")

        self.verticalLayout_3.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_7.addLayout(self.verticalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.Frame = QFrame(SigninWindow)
        self.Frame.setObjectName(u"Frame")
        self.Frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 70);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.verticalLayout_4 = QVBoxLayout(self.Frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(30, -1, 30, -1)

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
"color: black;")

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
"color: black;")

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


        self.verticalLayout_7.addWidget(self.Frame)

        self.label_error = QLabel(SigninWindow)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setStyleSheet(u"background: none;")

        self.verticalLayout_7.addWidget(self.label_error)

        self.label_error = QLabel(SigninWindow)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_2.addWidget(self.label_error)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.verticalFrame = QFrame(SigninWindow)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.verticalLayout_6 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_signup = QPushButton(self.verticalFrame)
        self.btn_signup.setObjectName(u"btn_signup")
        font3 = QFont()
        font3.setFamilies([u"Sitka"])
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setItalic(False)
        self.btn_signup.setFont(font3)
        self.btn_signup.setStyleSheet(u"QPushButton {\n"
"background-color: white;\n"
"font: 14pt \"Sitka\";\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(225, 225, 225);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(225, 225, 225);\n"
"}")

        self.verticalLayout_6.addWidget(self.btn_signup)


        self.verticalLayout_7.addWidget(self.verticalFrame)


        self.retranslateUi(SigninWindow)

        QMetaObject.connectSlotsByName(SigninWindow)
    # setupUi

    def retranslateUi(self, SigninWindow):
        SigninWindow.setWindowTitle(QCoreApplication.translate("SigninWindow", u"Axolot's Notes - sign in", None))
        self.label.setText(QCoreApplication.translate("SigninWindow", u"Axolot's Notes", None))
        self.label_3.setText(QCoreApplication.translate("SigninWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.label_login.setText(QCoreApplication.translate("SigninWindow", u"\u041f\u0440\u0438\u0434\u0443\u043c\u0430\u0439\u0442\u0435 \u043b\u043e\u0433\u0438\u043d:", None))
        self.lineEdit_login.setInputMask("")
        self.lineEdit_login.setText("")
        self.lineEdit_login.setPlaceholderText(QCoreApplication.translate("SigninWindow", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label_password.setText(QCoreApplication.translate("SigninWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("SigninWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_error.setText("")
        self.btn_signup.setText(QCoreApplication.translate("SigninWindow", u"\u0417\u0430\u0440\u0435\u0433\u0435\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
    # retranslateUi

