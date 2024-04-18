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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import res

class Ui_LoginWindow(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(365, 380)
        Dialog.setMinimumSize(QSize(365, 380))
        Dialog.setMaximumSize(QSize(365, 380))
        icon = QIcon()
        icon.addFile(u":/icons/icons/axolot.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_App = QLabel(Dialog)
        self.label_App.setObjectName(u"label_App")
        self.label_App.setMaximumSize(QSize(300, 45))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(30)
        font.setBold(False)
        font.setUnderline(False)
        self.label_App.setFont(font)
        self.label_App.setTextFormat(Qt.TextFormat.AutoText)
        self.label_App.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label_App, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_log = QLabel(Dialog)
        self.label_log.setObjectName(u"label_log")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(False)
        self.label_log.setFont(font1)
        self.label_log.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout_3.addWidget(self.label_log, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_name = QLabel(Dialog)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setMaximumSize(QSize(400, 300))
        font2 = QFont()
        font2.setPointSize(12)
        self.label_name.setFont(font2)

        self.verticalLayout.addWidget(self.label_name)

        self.lineEdit_name = QLineEdit(Dialog)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.verticalLayout.addWidget(self.lineEdit_name)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_password = QLabel(Dialog)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setMaximumSize(QSize(400, 300))
        self.label_password.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_password)

        self.lineEdit_password = QLineEdit(Dialog)
        self.lineEdit_password.setObjectName(u"lineEdit_password")

        self.verticalLayout_2.addWidget(self.lineEdit_password)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.label_error = QLabel(Dialog)
        self.label_error.setObjectName(u"label_error")

        self.verticalLayout_3.addWidget(self.label_error)

        self.verticalSpacer = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.btn_reg = QPushButton(Dialog)
        self.btn_reg.setObjectName(u"btn_reg")

        self.verticalLayout_3.addWidget(self.btn_reg)

        self.btn_login = QPushButton(Dialog)
        self.btn_login.setObjectName(u"btn_login")

        self.verticalLayout_3.addWidget(self.btn_login)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Axolot's Notes - Login window", None))
        self.label_App.setText(QCoreApplication.translate("Dialog", u"Axolot's Notes", None))
        self.label_log.setText(QCoreApplication.translate("Dialog", u"LOGIN", None))
        self.label_name.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.label_password.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.label_error.setText("")
        self.btn_reg.setText(QCoreApplication.translate("Dialog", u"Reg", None))
        self.btn_login.setText(QCoreApplication.translate("Dialog", u"Login", None))
    # retranslateUi

