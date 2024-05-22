# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogWNameNote.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import res_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(367, 212)
        Dialog.setMinimumSize(QSize(367, 212))
        Dialog.setMaximumSize(QSize(367, 212))
        icon = QIcon()
        icon.addFile(u":/icons/icons/axolot.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"background:  qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 227, 195, 255), stop:1 rgba(245, 78, 140, 255))")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"font: 15pt \"Segoe UI Black\";\n"
"background-color: none;\n"
"color: rgb(83, 47, 95);\n"
"border-radius: 7px;")

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.labelError = QLabel(Dialog)
        self.labelError.setObjectName(u"labelError")
        self.labelError.setStyleSheet(u"background-color: none;")

        self.verticalLayout_2.addWidget(self.labelError)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(216, 193, 219, 60);\n"
"border: 1px solid rgba(255, 255, 255, 70);\n"
"border-radius: 5px;\n"
"font: 900 11pt \"Segoe UI Black\";\n"
"color: rgb(91, 61, 107)")
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setMouseTracking(True)
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"background-color: white;\n"
"font: 600 11pt \"Segoe UI Black\";\n"
"color: rgb(91, 61, 107);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(225, 225, 225);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(225, 225, 225);\n"
"}")

        self.verticalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u043d\u043e\u0432\u043e\u0433\u043e \u0444\u0430\u0439\u043b\u0430:", None))
        self.labelError.setText("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u043a\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0413\u043e\u0442\u043e\u0432\u043e", None))
    # retranslateUi

