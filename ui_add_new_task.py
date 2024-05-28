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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QDialog,
    QFrame, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_AddNewTask(object):
    def setupUi(self, AddNewTask):
        if not AddNewTask.objectName():
            AddNewTask.setObjectName(u"AddNewTask")
        AddNewTask.resize(551, 600)
        AddNewTask.setMinimumSize(QSize(551, 600))
        AddNewTask.setMaximumSize(QSize(551, 600))
        AddNewTask.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 227, 195, 255), stop:1 rgba(245, 78, 140, 255));\n"
"")
        self.gridLayout_6 = QGridLayout(AddNewTask)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame = QFrame(AddNewTask)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font-weight: bold;\n"
"font: 25pt;\n"
"background-color: none;\n"
"color: white;")

        self.verticalLayout_5.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border-radius: 7px;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 12pt \"Sitka\";\n"
"color: black;\n"
"background-color: none;")

        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit_task = QLineEdit(self.frame_2)
        self.lineEdit_task.setObjectName(u"lineEdit_task")
        self.lineEdit_task.setMinimumSize(QSize(0, 50))
        self.lineEdit_task.setStyleSheet(u"font: 13pt \"Sitka\";\n"
"color: black;\n"
"background-color: rgb(255, 255, 245, 100);")

        self.verticalLayout.addWidget(self.lineEdit_task)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border-radius: 7px;")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Sitka"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"font: 12pt \"Sitka\";\n"
"color: black;\n"
"background-color: none;")

        self.verticalLayout_2.addWidget(self.label_3)

        self.dateTimeEdit_start = QDateTimeEdit(self.frame_3)
        self.dateTimeEdit_start.setObjectName(u"dateTimeEdit_start")
        self.dateTimeEdit_start.setMinimumSize(QSize(0, 40))
        self.dateTimeEdit_start.setStyleSheet(u"font: 13pt \"Sitka\";\n"
"color: black;\n"
"background-color: rgb(255, 255, 245, 100);")
        self.dateTimeEdit_start.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))
        self.dateTimeEdit_start.setCalendarPopup(False)

        self.verticalLayout_2.addWidget(self.dateTimeEdit_start)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border-radius: 7px;")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"font: 12pt \"Sitka\";\n"
"color: black;\n"
"background-color: none;")

        self.verticalLayout_3.addWidget(self.label_4)

        self.dateTimeEdit_end = QDateTimeEdit(self.frame_5)
        self.dateTimeEdit_end.setObjectName(u"dateTimeEdit_end")
        self.dateTimeEdit_end.setMinimumSize(QSize(0, 40))
        self.dateTimeEdit_end.setStyleSheet(u"font: 13pt \"Sitka\";\n"
"color: black;\n"
"background-color: rgb(255, 255, 245, 100);")
        self.dateTimeEdit_end.setDate(QDate(2024, 1, 2))

        self.verticalLayout_3.addWidget(self.dateTimeEdit_end)


        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border-radius: 7px;")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"font: 12pt \"Sitka\";\n"
"color: black;\n"
"background-color: none;")

        self.verticalLayout_4.addWidget(self.label_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lineEdit_category = QLineEdit(self.frame_6)
        self.lineEdit_category.setObjectName(u"lineEdit_category")
        self.lineEdit_category.setMinimumSize(QSize(0, 50))
        self.lineEdit_category.setStyleSheet(u"font: 13pt \"Sitka\";\n"
"color: black;\n"
"background-color: rgb(255, 255, 245, 100);")

        self.verticalLayout_6.addWidget(self.lineEdit_category)

        self.comboBoxTags = QComboBox(self.frame_6)
        self.comboBoxTags.setObjectName(u"comboBoxTags")
        self.comboBoxTags.setMinimumSize(QSize(100, 50))
        self.comboBoxTags.setMaximumSize(QSize(200, 43))
        self.comboBoxTags.setStyleSheet(u"font: 13pt \"Sitka\";\n"
"color: black;\n"
"background-color: rgb(255, 255, 245, 100);")

        self.verticalLayout_6.addWidget(self.comboBoxTags)


        self.verticalLayout_4.addLayout(self.verticalLayout_6)


        self.gridLayout_5.addLayout(self.verticalLayout_4, 1, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_6)

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

        self.verticalLayout_5.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(AddNewTask)

        QMetaObject.connectSlotsByName(AddNewTask)
    # setupUi

    def retranslateUi(self, AddNewTask):
        AddNewTask.setWindowTitle(QCoreApplication.translate("AddNewTask", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0439 \u0437\u0430\u0434\u0430\u0447\u0438 ", None))
        self.label.setText(QCoreApplication.translate("AddNewTask", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0439 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.label_2.setText(QCoreApplication.translate("AddNewTask", u"\u041f\u0440\u0438\u0434\u0443\u043c\u0430\u0439\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438:", None))
        self.lineEdit_task.setPlaceholderText(QCoreApplication.translate("AddNewTask", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.label_3.setText(QCoreApplication.translate("AddNewTask", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u0435 \u0434\u0430\u0442\u0443 \u0438 \u0432\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430", None))
        self.label_4.setText(QCoreApplication.translate("AddNewTask", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u0435 \u0434\u0430\u0442\u0443 \u0438 \u0432\u0440\u0435\u043c\u044f \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f", None))
        self.label_5.setText(QCoreApplication.translate("AddNewTask", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438\u043b\u0438 \u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.lineEdit_category.setPlaceholderText(QCoreApplication.translate("AddNewTask", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u043e\u0432\u0443\u044e \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.pushButton.setText(QCoreApplication.translate("AddNewTask", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
    # retranslateUi

