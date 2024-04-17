# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowAccountLogin.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import res

class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(350, 400)
        MainWindow.setMinimumSize(QSize(350, 400))
        MainWindow.setMaximumSize(QSize(350, 400))
        icon = QIcon()
        icon.addFile(u":/icons/icons/axolot.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_App = QLabel(self.centralwidget)
        self.label_App.setObjectName(u"label_App")
        self.label_App.setMaximumSize(QSize(300, 45))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(30)
        font.setBold(False)
        font.setUnderline(False)
        self.label_App.setFont(font)
        self.label_App.setCursor(QCursor(Qt.ArrowCursor))
        self.label_App.setTextFormat(Qt.AutoText)
        self.label_App.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.label_App, 0, Qt.AlignHCenter)

        self.label_log = QLabel(self.centralwidget)
        self.label_log.setObjectName(u"label_log")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(False)
        self.label_log.setFont(font1)
        self.label_log.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_5.addWidget(self.label_log, 0, Qt.AlignHCenter)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setMaximumSize(QSize(400, 300))
        font2 = QFont()
        font2.setPointSize(12)
        self.label_name.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_name)

        self.lineEdit_name = QLineEdit(self.centralwidget)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.verticalLayout_2.addWidget(self.lineEdit_name)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_password = QLabel(self.centralwidget)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setMaximumSize(QSize(400, 300))
        self.label_password.setFont(font2)

        self.verticalLayout.addWidget(self.label_password)

        self.lineEdit_password = QLineEdit(self.centralwidget)
        self.lineEdit_password.setObjectName(u"lineEdit_password")

        self.verticalLayout.addWidget(self.lineEdit_password)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.label_error = QLabel(self.centralwidget)
        self.label_error.setObjectName(u"label_error")

        self.verticalLayout_5.addWidget(self.label_error)

        self.verticalSpacer = QSpacerItem(0, 126, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_5.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Axolot's Notes - account login", None))
        self.label_App.setText(QCoreApplication.translate("MainWindow", u"Axolot's Notes", None))
        self.label_log.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_error.setText(QCoreApplication.translate("MainWindow", u"error test", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

