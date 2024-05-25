# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Add_new_task_Window.ui'
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QDialog, QFrame,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(359, 503)
        Dialog.setMinimumSize(QSize(0, 0))
        Dialog.setMaximumSize(QSize(16777215, 16777215))
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 227, 195, 255), stop:1 rgba(245, 78, 140, 255));\n"
"")
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.dateTimeEdit = QDateTimeEdit(self.frame)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setMinimumSize(QSize(0, 40))
        self.dateTimeEdit.setStyleSheet(u"font: 13pt \"Sitka\";\n"
"color: black;\n"
"background-color: rgb(255, 255, 245, 100);")
        self.dateTimeEdit.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))
        self.dateTimeEdit.setCalendarPopup(False)

        self.gridLayout.addWidget(self.dateTimeEdit, 4, 0, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamilies([u"Sitka"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"font: 12pt \"Sitka\";\n"
"color: black;\n"
"background-color: none;")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 90, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 9, 1, 1, 1)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 50))
        self.lineEdit.setStyleSheet(u"font: 13pt \"Sitka\";\n"
"color: black;\n"
"background-color: rgb(255, 255, 245, 100);")

        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 1)

        self.dateTimeEdit_2 = QDateTimeEdit(self.frame)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")
        self.dateTimeEdit_2.setMinimumSize(QSize(0, 40))
        self.dateTimeEdit_2.setStyleSheet(u"font: 13pt \"Sitka\";\n"
"color: black;\n"
"background-color: rgb(255, 255, 245, 100);")
        self.dateTimeEdit_2.setDate(QDate(2024, 1, 2))

        self.gridLayout.addWidget(self.dateTimeEdit_2, 6, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 12pt \"Sitka\";\n"
"color: black;\n"
"background-color: none;")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 255, 245);\n"
"border: 1px solid rgba(255, 255, 255, 70);\n"
"border-radius: 5px;\n"
"font: 13pt \"Sitka\";\n"
"color: black;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(227, 227, 227);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 255, 245);\n"
"}")

        self.gridLayout.addWidget(self.pushButton, 10, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(19)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"font-weight: bold;\n"
"background-color: none;\n"
"color: white;")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"font: 12pt \"Sitka\";\n"
"color: black;\n"
"background-color: none;")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 2)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"font: 12pt \"Sitka\";\n"
"color: black;\n"
"background-color: none;")

        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 2)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 50))
        self.lineEdit_2.setStyleSheet(u"font: 13pt \"Sitka\";\n"
"color: black;\n"
"background-color: rgb(255, 255, 245, 100);")

        self.gridLayout.addWidget(self.lineEdit_2, 8, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u0435 \u0434\u0430\u0442\u0443 \u0438 \u0432\u0440\u0435\u043c\u044f \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u0434\u0443\u043c\u0430\u0439\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438:", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0439 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u0435 \u0434\u0430\u0442\u0443 \u0438 \u0432\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u041a \u043a\u0430\u043a\u043e\u0439 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0441\u044f \u0437\u0430\u0434\u0430\u0447\u0430?", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e \u0437\u0430\u0434\u0430\u0447\u0438", None))
    # retranslateUi

