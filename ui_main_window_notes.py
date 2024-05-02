# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWNotes.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(737, 643)
        icon = QIcon()
        icon.addFile(u":/icons/icons/axolot.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(161, 134, 165)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(12, -1, 12, -1)
        self.btn_back = QPushButton(self.centralwidget)
        self.btn_back.setObjectName(u"btn_back")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy)
        self.btn_back.setMinimumSize(QSize(80, 25))
        self.btn_back.setMaximumSize(QSize(90, 25))
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setPointSize(11)
        font.setWeight(QFont.Black)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(216, 193, 219);\n"
"font: 900 11pt \"Segoe UI Black\";\n"
"color: rgb(91, 61, 107)\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(191, 171, 194);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(191, 171, 194);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/arrow_back_ios_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_back.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.btn_back)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(300, 100))
        font1 = QFont()
        font1.setFamilies([u"Ravie"])
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setItalic(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"font: 15pt \"Ravie\";\n"
"background-color: none;\n"
"color: white;\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_theme = QPushButton(self.centralwidget)
        self.btn_theme.setObjectName(u"btn_theme")
        self.btn_theme.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(133, 110, 136);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(109, 90, 111);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(109, 90, 111);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/dark_mode_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_theme.setIcon(icon2)
        self.btn_theme.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.btn_theme)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(60, 60))
        self.label_3.setPixmap(QPixmap(u":/icons/icons/axolot.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.buttonsLayout = QVBoxLayout()
        self.buttonsLayout.setSpacing(6)
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.buttonsLayout.setContentsMargins(12, 0, 0, 12)
        self.btn_add_note = QPushButton(self.centralwidget)
        self.btn_add_note.setObjectName(u"btn_add_note")
        self.btn_add_note.setMaximumSize(QSize(90, 25))
        self.btn_add_note.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(216, 193, 219);\n"
"font: 900 10 pt \"Segoe UI Black\";\n"
"color: rgb(91, 61, 107)\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(191, 171, 194);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(191, 171, 194);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/add_box_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_note.setIcon(icon3)
        self.btn_add_note.setIconSize(QSize(16, 16))

        self.buttonsLayout.addWidget(self.btn_add_note)

        self.btn_storage = QPushButton(self.centralwidget)
        self.btn_storage.setObjectName(u"btn_storage")
        self.btn_storage.setMaximumSize(QSize(90, 25))
        self.btn_storage.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(216, 193, 219);\n"
"font: 900 11pt \"Segoe UI Black\";\n"
"color: rgb(91, 61, 107)\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(191, 171, 194);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(191, 171, 194);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/create_new_folder_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_storage.setIcon(icon4)

        self.buttonsLayout.addWidget(self.btn_storage)

        self.btn_settings = QPushButton(self.centralwidget)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMaximumSize(QSize(90, 25))
        self.btn_settings.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(216, 193, 219);\n"
"font: 900 10 pt \"Segoe UI Black\";\n"
"color: rgb(91, 61, 107)\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(191, 171, 194);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(191, 171, 194);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/settings_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings.setIcon(icon5)

        self.buttonsLayout.addWidget(self.btn_settings)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.buttonsLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_4.addLayout(self.buttonsLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 12, -1)
        self.treeWidget = QTreeWidget(self.centralwidget)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setMaximumSize(QSize(150, 16777215))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.treeWidget.setFont(font2)
        self.treeWidget.setFrameShadow(QFrame.Shadow.Plain)
        self.treeWidget.setDragEnabled(True)
        self.treeWidget.setDragDropOverwriteMode(False)
        self.treeWidget.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)
        self.treeWidget.setAlternatingRowColors(False)
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.header().setVisible(False)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setDefaultSectionSize(100)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setProperty("showSortIndicator", True)

        self.horizontalLayout.addWidget(self.treeWidget)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"background: white")
        self.textEdit.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.textEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 12, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_save_or_del = QLabel(self.centralwidget)
        self.label_save_or_del.setObjectName(u"label_save_or_del")
        self.label_save_or_del.setMinimumSize(QSize(0, 0))
        self.label_save_or_del.setMaximumSize(QSize(250, 50))

        self.horizontalLayout_2.addWidget(self.label_save_or_del)

        self.btn_delete_note = QPushButton(self.centralwidget)
        self.btn_delete_note.setObjectName(u"btn_delete_note")
        self.btn_delete_note.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(216, 193, 219);\n"
"font: 900 11pt \"Segoe UI Black\";\n"
"color: rgb(91, 61, 107)\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(191, 171, 194);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(191, 171, 194);\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/scan_delete_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_note.setIcon(icon6)

        self.horizontalLayout_2.addWidget(self.btn_delete_note)

        self.btn_save = QPushButton(self.centralwidget)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(216, 193, 219);\n"
"font: 900 11pt \"Segoe UI Black\";\n"
"color: rgb(91, 61, 107)\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(191, 171, 194);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(191, 171, 194);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/save_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save.setIcon(icon7)

        self.horizontalLayout_2.addWidget(self.btn_save)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Axolot's Notes", None))
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Axolot's Notes", None))
        self.btn_theme.setText("")
        self.label_3.setText("")
        self.btn_add_note.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btn_storage.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043f\u043a\u0438", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_save_or_del.setText("")
        self.btn_delete_note.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

