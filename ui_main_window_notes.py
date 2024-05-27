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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFontComboBox, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QTabWidget,
    QTextEdit, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(781, 684)
        icon = QIcon()
        icon.addFile(u":/icons/icons/axolot.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 227, 195, 255), stop:1 rgba(245, 78, 140, 255));\n"
"")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame1 = QFrame(self.centralwidget)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border-radius: 7px;")
        self.horizontalLayout_3 = QHBoxLayout(self.frame1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_back = QPushButton(self.frame1)
        self.btn_back.setObjectName(u"btn_back")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy)
        self.btn_back.setMinimumSize(QSize(80, 25))
        self.btn_back.setMaximumSize(QSize(120, 25))
        font = QFont()
        font.setFamilies([u"Sitka"])
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 255, 245);\n"
"border: 1px solid rgba(255, 255, 255, 70);\n"
"border-radius: 5px;\n"
"font: 13pt \"Sitka\";\n"
"color: black;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(222, 222, 213);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 255, 245);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/arrow_back_ios_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_back.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.btn_back)

        self.frame_3 = QFrame(self.frame1)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 40))
        self.frame_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
"border-radius: 7px;")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_account = QLabel(self.frame_3)
        self.label_account.setObjectName(u"label_account")

        self.verticalLayout_7.addWidget(self.label_account)


        self.horizontalLayout_3.addWidget(self.frame_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label = QLabel(self.frame1)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(400, 100))
        font1 = QFont()
        font1.setFamilies([u"Ravie"])
        font1.setPointSize(30)
        font1.setBold(True)
        font1.setItalic(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"font: 30pt \"Ravie\";\n"
"font-weight: bold;\n"
"background-color: none;\n"
"color: white;")

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(self.frame1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(60, 60))
        self.label_3.setStyleSheet(u"background-color: none;")
        self.label_3.setPixmap(QPixmap(u":/icons/icons/axolot.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout_2.addWidget(self.frame1, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"border-radius: 5px;\n"
"border-color: none;\n"
"font: 11pt \"Sitka\";\n"
"\n"
"\n"
"QPushButton {\n"
"background-color: rgb(255, 255, 245);\n"
"border: 1px solid rgba(255, 255, 255, 70);\n"
"border-radius: 5px;\n"
"font: 13pt \"Sitka\";\n"
"color: black;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(222, 222, 213);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 255, 245);\n"
"}")
        self.notesTab = QWidget()
        self.notesTab.setObjectName(u"notesTab")
        self.verticalLayout_2 = QVBoxLayout(self.notesTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame = QFrame(self.notesTab)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 70);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.buttonsLayout = QVBoxLayout(self.frame)
        self.buttonsLayout.setSpacing(6)
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.buttonsLayout.setContentsMargins(12, 12, 12, 12)
        self.btn_add_note = QPushButton(self.frame)
        self.btn_add_note.setObjectName(u"btn_add_note")
        self.btn_add_note.setMaximumSize(QSize(16777215, 25))
        self.btn_add_note.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 255, 245);\n"
"border: 1px solid rgba(255, 255, 255, 70);\n"
"border-radius: 5px;\n"
"font: 13pt \"Sitka\";\n"
"color: black;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(222, 222, 213);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 255, 245);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/add_box_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_note.setIcon(icon2)
        self.btn_add_note.setIconSize(QSize(16, 16))

        self.buttonsLayout.addWidget(self.btn_add_note)

        self.btn_add_dir = QPushButton(self.frame)
        self.btn_add_dir.setObjectName(u"btn_add_dir")
        self.btn_add_dir.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 255, 245);\n"
"border: 1px solid rgba(255, 255, 255, 70);\n"
"border-radius: 5px;\n"
"font: 13pt \"Sitka\";\n"
"color: black;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(222, 222, 213);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 255, 245);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/create_new_folder_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_dir.setIcon(icon3)

        self.buttonsLayout.addWidget(self.btn_add_dir)

        self.btn_storage = QPushButton(self.frame)
        self.btn_storage.setObjectName(u"btn_storage")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_storage.sizePolicy().hasHeightForWidth())
        self.btn_storage.setSizePolicy(sizePolicy1)
        self.btn_storage.setMaximumSize(QSize(16777215, 25))
        self.btn_storage.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 255, 245);\n"
"border: 1px solid rgba(255, 255, 255, 70);\n"
"border-radius: 5px;\n"
"font: 13pt \"Sitka\";\n"
"color: black;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(222, 222, 213);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 255, 245);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/folder_open_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_storage.setIcon(icon4)

        self.buttonsLayout.addWidget(self.btn_storage)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.buttonsLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_8.addWidget(self.frame)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.fontComboBox = QFontComboBox(self.notesTab)
        self.fontComboBox.setObjectName(u"fontComboBox")
        self.fontComboBox.setMaximumSize(QSize(300, 16777215))
        self.fontComboBox.setStyleSheet(u"background-color: rgba(255, 255, 255, 160);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")

        self.horizontalLayout_4.addWidget(self.fontComboBox)

        self.btn_formatBold = QPushButton(self.notesTab)
        self.btn_formatBold.setObjectName(u"btn_formatBold")
        self.btn_formatBold.setMaximumSize(QSize(35, 35))
        self.btn_formatBold.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 255, 245);\n"
"border: 1px solid rgba(255, 255, 255, 70);\n"
"border-radius: 5px;\n"
"font: 13pt \"Sitka\";\n"
"color: black;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(222, 222, 213);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 255, 245);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/format_bold_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_formatBold.setIcon(icon5)
        self.btn_formatBold.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.btn_formatBold)

        self.btn_formatItalic = QPushButton(self.notesTab)
        self.btn_formatItalic.setObjectName(u"btn_formatItalic")
        self.btn_formatItalic.setMaximumSize(QSize(35, 35))
        self.btn_formatItalic.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 255, 245);\n"
"border: 1px solid rgba(255, 255, 255, 70);\n"
"border-radius: 5px;\n"
"font: 13pt \"Sitka\";\n"
"color: black;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(222, 222, 213);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 255, 245);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/format_italic_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_formatItalic.setIcon(icon6)
        self.btn_formatItalic.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.btn_formatItalic)

        self.btn_formatUnderline = QPushButton(self.notesTab)
        self.btn_formatUnderline.setObjectName(u"btn_formatUnderline")
        self.btn_formatUnderline.setMaximumSize(QSize(35, 35))
        self.btn_formatUnderline.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 255, 245);\n"
"border: 1px solid rgba(255, 255, 255, 70);\n"
"border-radius: 5px;\n"
"font: 13pt \"Sitka\";\n"
"color: black;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(222, 222, 213);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 255, 245);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/format_underlined_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_formatUnderline.setIcon(icon7)
        self.btn_formatUnderline.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.btn_formatUnderline)

        self.fontSizeBox = QComboBox(self.notesTab)
        self.fontSizeBox.setObjectName(u"fontSizeBox")
        self.fontSizeBox.setStyleSheet(u"background-color: rgba(255, 255, 255, 160);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")

        self.horizontalLayout_4.addWidget(self.fontSizeBox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.frame2 = QFrame(self.notesTab)
        self.frame2.setObjectName(u"frame2")
        self.frame2.setStyleSheet(u"background-color: rgba(255, 255, 255, 160);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.horizontalLayout = QHBoxLayout(self.frame2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 12, -1)
        self.treeWidget = QTreeWidget(self.frame2)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"\u0424\u0430\u0439\u043b\u044b");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setMaximumSize(QSize(350, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Sitka"])
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
        self.treeWidget.setFont(font2)
        self.treeWidget.setFrameShadow(QFrame.Shadow.Plain)
        self.treeWidget.setProperty("showDropIndicator", False)
        self.treeWidget.setDragEnabled(False)
        self.treeWidget.setDragDropOverwriteMode(False)
        self.treeWidget.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)
        self.treeWidget.setAlternatingRowColors(False)
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setDefaultSectionSize(100)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setProperty("showSortIndicator", True)

        self.horizontalLayout.addWidget(self.treeWidget)

        self.textEdit = QTextEdit(self.frame2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"background: white")
        self.textEdit.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.textEdit)


        self.verticalLayout.addWidget(self.frame2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 12, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_save_or_del = QLabel(self.notesTab)
        self.label_save_or_del.setObjectName(u"label_save_or_del")
        self.label_save_or_del.setMinimumSize(QSize(0, 0))
        self.label_save_or_del.setMaximumSize(QSize(250, 50))
        self.label_save_or_del.setStyleSheet(u"background-color: none;\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.label_save_or_del)

        self.btn_delete_note = QPushButton(self.notesTab)
        self.btn_delete_note.setObjectName(u"btn_delete_note")
        self.btn_delete_note.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 255, 245);\n"
"border: 1px solid rgba(255, 255, 255, 70);\n"
"border-radius: 5px;\n"
"font: 13pt \"Sitka\";\n"
"color: black;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(222, 222, 213);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 255, 245);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/scan_delete_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_note.setIcon(icon8)

        self.horizontalLayout_2.addWidget(self.btn_delete_note)

        self.btn_save = QPushButton(self.notesTab)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 255, 245);\n"
"border: 1px solid rgba(255, 255, 255, 70);\n"
"border-radius: 5px;\n"
"font: 13pt \"Sitka\";\n"
"color: black;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(222, 222, 213);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 255, 245);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/save_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save.setIcon(icon9)

        self.horizontalLayout_2.addWidget(self.btn_save)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_8.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.tabWidget.addTab(self.notesTab, "")
        self.taskManager_tab = QWidget()
        self.taskManager_tab.setObjectName(u"taskManager_tab")
        self.verticalLayout_3 = QVBoxLayout(self.taskManager_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.taskManager_tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border-radius: 7px;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_taskmanager = QLabel(self.frame_2)
        self.label_taskmanager.setObjectName(u"label_taskmanager")
        self.label_taskmanager.setMaximumSize(QSize(400, 50))
        font3 = QFont()
        font3.setFamilies([u"Ravie"])
        font3.setPointSize(20)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setKerning(True)
        self.label_taskmanager.setFont(font3)
        self.label_taskmanager.setStyleSheet(u"font: 20pt \"Ravie\";\n"
"font-weight: bold;\n"
"background-color: none;\n"
"color: white;")

        self.verticalLayout_8.addWidget(self.label_taskmanager, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.horizontalLayout_9 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setSpacing(12)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(12, 12, 12, 12)
        self.btn_add_task = QPushButton(self.frame_5)
        self.btn_add_task.setObjectName(u"btn_add_task")
        self.btn_add_task.setMinimumSize(QSize(200, 40))
        self.btn_add_task.setMaximumSize(QSize(200, 25))
        self.btn_add_task.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 255, 245);\n"
"border: 1px solid rgba(255, 255, 255, 70);\n"
"border-radius: 5px;\n"
"font: 13pt \"Sitka\";\n"
"color: black;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(222, 222, 213);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 255, 245);\n"
"}")
        self.btn_add_task.setIcon(icon2)
        self.btn_add_task.setIconSize(QSize(16, 16))

        self.horizontalLayout_9.addWidget(self.btn_add_task)

        self.btn_delete_task = QPushButton(self.frame_5)
        self.btn_delete_task.setObjectName(u"btn_delete_task")
        self.btn_delete_task.setMinimumSize(QSize(200, 40))
        self.btn_delete_task.setMaximumSize(QSize(200, 25))
        self.btn_delete_task.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 255, 245);\n"
"border: 1px solid rgba(255, 255, 255, 70);\n"
"border-radius: 5px;\n"
"font: 13pt \"Sitka\";\n"
"color: black;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(222, 222, 213);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 255, 245);\n"
"}")
        self.btn_delete_task.setIcon(icon8)
        self.btn_delete_task.setIconSize(QSize(16, 16))

        self.horizontalLayout_9.addWidget(self.btn_delete_task)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.comboBoxTags = QComboBox(self.frame_5)
        self.comboBoxTags.setObjectName(u"comboBoxTags")
        self.comboBoxTags.setMinimumSize(QSize(100, 50))
        self.comboBoxTags.setMaximumSize(QSize(300, 50))
        self.comboBoxTags.setStyleSheet(u"background-color: rgba(255, 255, 255, 175);\n"
"border-radius: 7px;\n"
"\n"
"font: 15pt;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_6.addWidget(self.comboBoxTags)

        self.btn_filterByTags = QPushButton(self.frame_5)
        self.btn_filterByTags.setObjectName(u"btn_filterByTags")
        self.btn_filterByTags.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 255, 245);\n"
"border: 1px solid rgba(255, 255, 255, 70);\n"
"border-radius: 5px;\n"
"font: 13pt \"Sitka\";\n"
"color: black;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(222, 222, 213);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 255, 245);\n"
"}")

        self.verticalLayout_6.addWidget(self.btn_filterByTags)


        self.horizontalLayout_9.addLayout(self.verticalLayout_6)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 708, 375))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_4.setStyleSheet(u"QGroupBox  {\n"
"background-color: rgba(255, 255, 255, 60);\n"
"border-radius: 7px;\n"
"}\n"
"QLabel {\n"
"background-color: rgba(255, 255, 255, 80);\n"
"border-radius: 7px;\n"
"font: 12pt;\n"
"font-weight: bold;\n"
"}\n"
"QTextBrowser {\n"
"background-color: rgba(255, 255, 255, 150);\n"
"border-radius: 7px;\n"
"font: 15pt;\n"
"}")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.gridLayout.addLayout(self.verticalLayout_4, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 3, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_8.addWidget(self.scrollArea)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.tabWidget.addTab(self.taskManager_tab, "")

        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Axolot's Notes", None))
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.label_account.setText(QCoreApplication.translate("MainWindow", u"A\u043a\u043a\u0430\u0443\u043d\u0442:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Axolot's Notes", None))
        self.label_3.setText("")
        self.btn_add_note.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0437\u0430\u043c\u0435\u0442\u043a\u0430", None))
        self.btn_add_dir.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u043f\u0430\u043f\u043a\u0430", None))
        self.btn_storage.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043f\u043a\u0438", None))
        self.btn_formatBold.setText("")
        self.btn_formatItalic.setText("")
        self.btn_formatUnderline.setText("")
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0444\u0430\u0439\u043b\u0430", None));
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sitka'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_save_or_del.setText("")
        self.btn_delete_note.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.notesTab), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.label_taskmanager.setText(QCoreApplication.translate("MainWindow", u"Task Manager", None))
        self.btn_add_task.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0437\u0430\u0434\u0430\u0447\u0430", None))
        self.btn_delete_task.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
        self.btn_filterByTags.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0444\u0438\u043b\u044c\u0442\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.taskManager_tab), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0438", None))
    # retranslateUi

