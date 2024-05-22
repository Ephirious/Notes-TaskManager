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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import res_rc

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(498, 514)
        LoginWindow.setMinimumSize(QSize(498, 514))
        LoginWindow.setMaximumSize(QSize(498, 514))
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 1, 1)
        gradient.setSpread(QGradient.RepeatSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(255, 227, 195, 255))
        gradient.setColorAt(1, QColor(245, 78, 140, 255))
        brush = QBrush(gradient)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        gradient1 = QLinearGradient(0, 0, 1, 1)
        gradient1.setSpread(QGradient.RepeatSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(255, 227, 195, 255))
        gradient1.setColorAt(1, QColor(245, 78, 140, 255))
        brush1 = QBrush(gradient1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        gradient2 = QLinearGradient(0, 0, 1, 1)
        gradient2.setSpread(QGradient.RepeatSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(255, 227, 195, 255))
        gradient2.setColorAt(1, QColor(245, 78, 140, 255))
        brush2 = QBrush(gradient2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush2)
        gradient3 = QLinearGradient(0, 0, 1, 1)
        gradient3.setSpread(QGradient.RepeatSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(255, 227, 195, 255))
        gradient3.setColorAt(1, QColor(245, 78, 140, 255))
        brush3 = QBrush(gradient3)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        gradient4 = QLinearGradient(0, 0, 1, 1)
        gradient4.setSpread(QGradient.RepeatSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(255, 227, 195, 255))
        gradient4.setColorAt(1, QColor(245, 78, 140, 255))
        brush4 = QBrush(gradient4)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        gradient5 = QLinearGradient(0, 0, 1, 1)
        gradient5.setSpread(QGradient.RepeatSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(255, 227, 195, 255))
        gradient5.setColorAt(1, QColor(245, 78, 140, 255))
        brush5 = QBrush(gradient5)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        gradient6 = QLinearGradient(0, 0, 1, 1)
        gradient6.setSpread(QGradient.RepeatSpread)
        gradient6.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(255, 227, 195, 255))
        gradient6.setColorAt(1, QColor(245, 78, 140, 255))
        brush6 = QBrush(gradient6)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        gradient7 = QLinearGradient(0, 0, 1, 1)
        gradient7.setSpread(QGradient.RepeatSpread)
        gradient7.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(255, 227, 195, 255))
        gradient7.setColorAt(1, QColor(245, 78, 140, 255))
        brush7 = QBrush(gradient7)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        gradient8 = QLinearGradient(0, 0, 1, 1)
        gradient8.setSpread(QGradient.RepeatSpread)
        gradient8.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(255, 227, 195, 255))
        gradient8.setColorAt(1, QColor(245, 78, 140, 255))
        brush8 = QBrush(gradient8)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        LoginWindow.setPalette(palette)
        icon = QIcon()
        icon.addFile(u":/icons/icons/axolot.png", QSize(), QIcon.Normal, QIcon.Off)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 227, 195, 255), stop:1 rgba(245, 78, 140, 255));\n"
"")
        self.label_error = QLabel(LoginWindow)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setGeometry(QRect(40, 240, 421, 121))
        self.label_error.setStyleSheet(u"background-color: none;\n"
"")
        self.frame = QFrame(LoginWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(110, 350, 291, 141))
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_reg = QPushButton(self.frame)
        self.btn_reg.setObjectName(u"btn_reg")
        self.btn_reg.setMaximumSize(QSize(16777215, 18))
        self.btn_reg.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.btn_reg)

        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMaximumSize(QSize(16777215, 18))
        self.btn_login.setStyleSheet(u"QPushButton {\n"
"background-color: white;\n"
"font: 14pt \"Sitka\";\n"
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
        self.frame_2 = QFrame(LoginWindow)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(40, 120, 421, 131))
        self.frame_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_name = QLabel(self.frame_2)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setMinimumSize(QSize(345, 0))
        self.label_name.setMaximumSize(QSize(400, 300))
        font = QFont()
        font.setFamilies([u"Sitka"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet(u"font: 16pt \"Sitka\";\n"
"background-color: none;\n"
"color: rgb(91, 61, 107)\n"
"")

        self.verticalLayout.addWidget(self.label_name)

        self.lineEdit_name = QLineEdit(self.frame_2)
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
        self.label_password = QLabel(self.frame_2)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setMinimumSize(QSize(345, 0))
        self.label_password.setMaximumSize(QSize(400, 300))
        self.label_password.setFont(font)
        self.label_password.setStyleSheet(u"font: 16pt \"Sitka\";\n"
"background-color: none;\n"
"color: rgb(91, 61, 107)")

        self.verticalLayout_3.addWidget(self.label_password)

        self.lineEdit_password = QLineEdit(self.frame_2)
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

        self.frame_3 = QFrame(LoginWindow)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(90, 10, 331, 83))
        self.frame_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border-radius: 7px;")
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_App = QLabel(self.frame_3)
        self.label_App.setObjectName(u"label_App")
        font1 = QFont()
        font1.setFamilies([u"Ravie"])
        font1.setPointSize(30)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        self.label_App.setFont(font1)
        self.label_App.setStyleSheet(u"font: 30pt \"Ravie\";\n"
"font-weight: bold;\n"
"background-color: none;\n"
"color: white;")
        self.label_App.setTextFormat(Qt.TextFormat.AutoText)
        self.label_App.setScaledContents(True)
        self.label_App.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_App)

        self.label_log = QLabel(self.frame_3)
        self.label_log.setObjectName(u"label_log")
        font2 = QFont()
        font2.setFamilies([u"Sitka"])
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_log.setFont(font2)
        self.label_log.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_log.setStyleSheet(u"font: 20pt \"Sitka\";;\n"
"background-color: none;\n"
"color: rgb(91, 61, 107)\n"
"")
        self.label_log.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_log, 0, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Axolot's Notes - Login window", None))
        self.label_error.setText("")
        self.btn_reg.setText(QCoreApplication.translate("LoginWindow", u"\u0417\u0430\u0440\u0435\u0433\u0435\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.btn_login.setText(QCoreApplication.translate("LoginWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.label_name.setText(QCoreApplication.translate("LoginWindow", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f:", None))
        self.lineEdit_name.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label_password.setText(QCoreApplication.translate("LoginWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.lineEdit_password.setText("")
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_App.setText(QCoreApplication.translate("LoginWindow", u"Axolot's Notes", None))
#if QT_CONFIG(whatsthis)
        self.label_log.setWhatsThis(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_log.setText(QCoreApplication.translate("LoginWindow", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
    # retranslateUi

