# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 400)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionOptions = QAction(MainWindow)
        self.actionOptions.setObjectName(u"actionOptions")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.txtUrl = QLineEdit(self.centralwidget)
        self.txtUrl.setObjectName(u"txtUrl")

        self.gridLayout.addWidget(self.txtUrl, 0, 0, 1, 1)

        self.btnProcess = QPushButton(self.centralwidget)
        self.btnProcess.setObjectName(u"btnProcess")
        self.btnProcess.setEnabled(False)
        self.btnProcess.setStyleSheet(u"padding-top: 4px;\n"
"padding-bottom: 4px;\n"
"padding-left: 12px;\n"
"padding-right: 12px;")

        self.gridLayout.addWidget(self.btnProcess, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.txtVideoTitle = QLineEdit(self.centralwidget)
        self.txtVideoTitle.setObjectName(u"txtVideoTitle")
        self.txtVideoTitle.setReadOnly(True)

        self.gridLayout_2.addWidget(self.txtVideoTitle, 0, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.cmbVideoFormats = QComboBox(self.centralwidget)
        self.cmbVideoFormats.setObjectName(u"cmbVideoFormats")
        self.cmbVideoFormats.setEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cmbVideoFormats)

        self.cmbAudioFormats = QComboBox(self.centralwidget)
        self.cmbAudioFormats.setObjectName(u"cmbAudioFormats")
        self.cmbAudioFormats.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cmbAudioFormats)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)


        self.gridLayout_2.addLayout(self.formLayout, 3, 0, 1, 1)

        self.txtVideoDescription = QPlainTextEdit(self.centralwidget)
        self.txtVideoDescription.setObjectName(u"txtVideoDescription")
        self.txtVideoDescription.setReadOnly(True)

        self.gridLayout_2.addWidget(self.txtVideoDescription, 1, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(300, 168))
        self.frame.setMaximumSize(QSize(300, 168))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.imgThumbnail = QLabel(self.frame)
        self.imgThumbnail.setObjectName(u"imgThumbnail")
        self.imgThumbnail.setGeometry(QRect(0, 0, 300, 168))
        self.lblDuration = QLabel(self.frame)
        self.lblDuration.setObjectName(u"lblDuration")
        self.lblDuration.setEnabled(True)
        self.lblDuration.setGeometry(QRect(2, 142, 49, 21))
        sizePolicy.setHeightForWidth(self.lblDuration.sizePolicy().hasHeightForWidth())
        self.lblDuration.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lblDuration.setFont(font)
        self.lblDuration.setToolTipDuration(-1)
        self.lblDuration.setLayoutDirection(Qt.LeftToRight)
        self.lblDuration.setStyleSheet(u"background-color: rgba(38, 46, 56, 0.8);\n"
"border-top-left-radius: 5px;\n"
"padding-left: 6px;\n"
"padding-right: 6px;")
        self.lblDuration.setScaledContents(True)
        self.lblDuration.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.frame)

        self.chkSaveThumbnail = QCheckBox(self.centralwidget)
        self.chkSaveThumbnail.setObjectName(u"chkSaveThumbnail")
        self.chkSaveThumbnail.setEnabled(True)

        self.verticalLayout_2.addWidget(self.chkSaveThumbnail)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 4, 1)

        self.chkQuality = QCheckBox(self.centralwidget)
        self.chkQuality.setObjectName(u"chkQuality")
        self.chkQuality.setChecked(True)

        self.gridLayout_2.addWidget(self.chkQuality, 2, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btnDownload = QPushButton(self.centralwidget)
        self.btnDownload.setObjectName(u"btnDownload")
        self.btnDownload.setEnabled(False)
        self.btnDownload.setStyleSheet(u"padding-top: 4px;\n"
"padding-bottom: 4px;\n"
"padding-left: 12px;\n"
"padding-right: 12px;")

        self.gridLayout_3.addWidget(self.btnDownload, 1, 2, 1, 1)

        self.txtOutputFilename = QLineEdit(self.centralwidget)
        self.txtOutputFilename.setObjectName(u"txtOutputFilename")
        self.txtOutputFilename.setEnabled(False)

        self.gridLayout_3.addWidget(self.txtOutputFilename, 1, 0, 1, 1)

        self.btnBrowse = QPushButton(self.centralwidget)
        self.btnBrowse.setObjectName(u"btnBrowse")
        self.btnBrowse.setEnabled(False)
        self.btnBrowse.setStyleSheet(u"padding-top: 4px;\n"
"padding-bottom: 4px;\n"
"padding-left: 12px;\n"
"padding-right: 12px;")

        self.gridLayout_3.addWidget(self.btnBrowse, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuTools.addAction(self.actionOptions)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)
        self.btnProcess.clicked.connect(MainWindow.process_button_clicked)
        self.txtUrl.textChanged.connect(MainWindow.url_text_changed)
        self.actionExit.triggered.connect(MainWindow.close)
        self.btnBrowse.clicked.connect(MainWindow.browse_button_clicked)
        self.btnDownload.clicked.connect(MainWindow.download_button_clicked)
        self.cmbVideoFormats.currentIndexChanged.connect(MainWindow.video_format_changed)
        self.chkQuality.toggled.connect(MainWindow.quality_toggled)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"yt-dlp-gui-qt", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionOptions.setText(QCoreApplication.translate("MainWindow", u"Options", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.txtUrl.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Video URL", None))
        self.btnProcess.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.txtVideoTitle.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Video title", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Video format:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Audio format:", None))
        self.txtVideoDescription.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Video description", None))
        self.imgThumbnail.setText("")
        self.lblDuration.setText("")
        self.chkSaveThumbnail.setText(QCoreApplication.translate("MainWindow", u"Save thumbnail", None))
        self.chkQuality.setText(QCoreApplication.translate("MainWindow", u"Automatic best quality", None))
        self.btnDownload.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.btnBrowse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

