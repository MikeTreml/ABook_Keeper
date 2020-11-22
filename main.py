import os
import pathlib
import sqlite3
import urllib.request as req

import eyed3
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, QMetaObject
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget, QLineEdit, QLabel, QGroupBox, QComboBox, \
    QTabWidget
from fuzzywuzzy import fuzz

import Functions


class Ui_MainWindow(object):

    def __init__(self):
        self.main = QWidget()
        self.centralwidget = QWidget(MainWindow)
        self.settings = QWidget()
        self.groupBox_3 = QGroupBox(self.main)
        self.groupBox_6 = QGroupBox(self.main)
        self.groupBox_4 = QGroupBox(self.main)
        self.groupBox_5 = QGroupBox(self.main)
        self.groupBox_2 = QGroupBox(self.main)
        self.groupBox = QGroupBox(self.main)

        self.audibleArtWork = QLabel(self.main)
        self.audibleAuthorSearch = QLineEdit(self.main)
        self.audibleComboBox = QComboBox(self.main)
        self.audibleFuzzyAV = QLineEdit(self.main)
        self.audible_data_post = QPushButton(self.main)
        self.audible_search_toggle = QPushButton(self.main)
        self.audibleSeriesSearch = QLineEdit(self.main)
        self.audibleTitleSearch = QLineEdit(self.main)
        self.audibleTrackNoSearch = QLineEdit(self.main)
        self.audible_URL = QLineEdit(self.main)
        self.ffArtWork = QLabel(self.main)
        self.ff_author = QLineEdit(self.main)
        self.ffComboBox = QComboBox(self.main)
        self.ffFuzzyAV = QLineEdit(self.main)
        self.ffPullButton = QPushButton(self.main)
        self.ff_search_toggle = QPushButton(self.main)
        self.ff_series = QLineEdit(self.main)
        self.ff_title = QLineEdit(self.main)
        self.ffTrackNo = QLineEdit(self.main)
        self.ff_URL = QLineEdit(self.main)
        self.file_series = QLineEdit(self.main)
        self.file_author = QLineEdit(self.main)
        self.file_ComboBox = QComboBox(self.main)
        self.FileLocation = QLineEdit(self.settings)
        self.file_title = QLineEdit(self.main)
        self.file_book_number = QLineEdit(self.main)
        self.finalAlbum = QLineEdit(self.main)
        self.finalArtist = QLineEdit(self.main)
        self.finalTrack = QLineEdit(self.main)
        self.finalTrackNo = QLineEdit(self.main)
        self.finishedArtWork = QLabel(self.centralwidget)
        self.FinishedLocation = QLineEdit(self.settings)
        self.goodreadsArtWork = QLabel(self.main)
        self.goodreads_author = QLineEdit(self.main)
        self.goodreadsComboBox = QComboBox(self.main)
        self.goodreadsFuzzyAV = QLineEdit(self.main)
        self.goodreads_search_toggle = QPushButton(self.main)
        self.goodreadsPullButton = QPushButton(self.main)
        self.goodreads_series = QLineEdit(self.main)
        self.goodreads_title = QLineEdit(self.main)
        self.goodreads_book_number = QLineEdit(self.main)
        self.goodreads_URL = QLineEdit(self.main)
        self.googleArtWork = QLabel(self.main)
        self.google_author = QLineEdit(self.main)
        self.google_search_toggle = QPushButton(self.main)
        self.google_combobox = QComboBox(self.main)
        self.googleFuzzyAV = QLineEdit(self.main)
        self.googlePullButton = QPushButton(self.main)
        self.google_series = QLineEdit(self.main)
        self.google_title = QLineEdit(self.main)
        self.google_book_number = QLineEdit(self.main)
        self.label = QLabel(self.main)
        self.label_10 = QLabel(self.main)
        self.label_12 = QLabel(self.main)
        self.label_14 = QLabel(self.settings)
        self.label_15 = QLabel(self.settings)
        self.label_16 = QLabel(self.main)
        self.label_18 = QLabel(self.main)
        self.label_2 = QLabel(self.main)
        self.label_3 = QLabel(self.main)
        self.label_4 = QLabel(self.main)
        self.label_44 = QLabel(self.main)
        self.label_45 = QLabel(self.main)
        self.label_46 = QLabel(self.main)
        self.label_47 = QLabel(self.main)
        self.label_48 = QLabel(self.main)
        self.label_49 = QLabel(self.main)
        self.label_50 = QLabel(self.main)
        self.label_51 = QLabel(self.main)
        self.label_54 = QLabel(self.main)
        self.label_55 = QLabel(self.main)
        self.label_56 = QLabel(self.main)
        self.label_58 = QLabel(self.main)
        self.label_59 = QLabel(self.main)
        self.label_60 = QLabel(self.main)
        self.label_61 = QLabel(self.main)
        self.label_62 = QLabel(self.main)
        self.label_64 = QLabel(self.main)
        self.label_65 = QLabel(self.main)
        self.label_66 = QLabel(self.main)
        self.label_9 = QLabel(self.settings)
        self.open_folder_button = QPushButton(self.main)
        self.originalArtWork = QLabel(self.main)
        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton_2 = QPushButton(self.main)
        self.SaveFormatText = QLineEdit(self.settings)
        self.saveSettingsButton = QPushButton(self.settings)
        self.search_button = QPushButton(self.main)
        self.tab = QWidget()
        self.tabWidget = QTabWidget(self.centralwidget)
        self.WebSitecomboBox = QComboBox(self.settings)

    def setupUi(self, MainWindow):
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.resize(835, 602)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhDate)
        MainWindow.setCentralWidget(self.centralwidget)
        QMetaObject.connectSlotsByName(MainWindow)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(100, 100, 100))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(80, 80, 80))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.black)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(60, 60, 60))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        app.setPalette(palette)

        self.groupBox.setEnabled(False)
        self.groupBox.setGeometry(QtCore.QRect(575, 30, 257, 251))
        self.groupBox.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
        self.groupBox_5.setEnabled(False)
        self.groupBox_5.setGeometry(QtCore.QRect(5, 441, 561, 130))
        self.groupBox_5.setStyleSheet("background-color: rgba(10, 95, 255, 100);")
        self.groupBox_3.setEnabled(False)
        self.groupBox_3.setGeometry(QtCore.QRect(5, 309, 561, 130))
        self.groupBox_3.setStyleSheet("background-color: rgba(144, 113, 76, 100);")
        self.groupBox_6.setEnabled(False)
        self.groupBox_6.setGeometry(QtCore.QRect(5, 177, 561, 130))
        self.groupBox_6.setStyleSheet("background-color: rgba(254, 172, 12, 100);")
        self.groupBox_4.setEnabled(False)
        self.groupBox_4.setGeometry(QtCore.QRect(5, 45, 561, 130))
        self.groupBox_4.setStyleSheet("background-color: rgba(157, 51, 214, 70);")
        self.groupBox_2.setGeometry(QtCore.QRect(575, 331, 257, 241))
        self.groupBox_2.setStyleSheet("background-color: rgba(41, 200, 50, 80);")

        self.tabWidget.addTab(self.main, "")
        self.tabWidget.addTab(self.tab, "")
        self.tabWidget.addTab(self.settings, "")

        self.audibleArtWork.setGeometry(QtCore.QRect(420, 177, 120, 120))
        self.audibleArtWork.setScaledContents(True)
        self.audibleArtWork.setStyleSheet("")
        self.audibleAuthorSearch.setGeometry(QtCore.QRect(10, 222, 181, 20))
        self.audibleComboBox.setGeometry(QtCore.QRect(6, 281, 401, 22))
        self.audibleFuzzyAV.setAlignment(QtCore.Qt.AlignCenter)
        self.audibleFuzzyAV.setGeometry(QtCore.QRect(540, 183, 24, 20))
        self.audible_data_post.setGeometry(QtCore.QRect(690, 283, 71, 23))
        self.audible_data_post.setStyleSheet("background-color: rgb(98, 78, 14);")
        self.audible_search_toggle.setCheckable(True)
        self.audible_search_toggle.setChecked(False)
        self.audible_search_toggle.setEnabled(True)
        self.audible_search_toggle.setGeometry(QtCore.QRect(5, 177, 80, 30))
        self.audible_search_toggle.setStyleSheet("@QPushButton:checked {background-color: blue;}")
        self.audibleSeriesSearch.setGeometry(QtCore.QRect(207, 223, 211, 20))
        self.audibleTitleSearch.setGeometry(QtCore.QRect(150, 190, 271, 20))
        self.audibleTrackNoSearch.setAlignment(QtCore.Qt.AlignCenter)
        self.audibleTrackNoSearch.setGeometry(QtCore.QRect(90, 190, 51, 20))
        self.audible_URL.setGeometry(QtCore.QRect(10, 254, 411, 20))
        self.audible_URL.setInputMethodHints(QtCore.Qt.ImhNone)
        self.ffArtWork.setGeometry(QtCore.QRect(420, 441, 120, 120))
        self.ffArtWork.setScaledContents(True)
        self.ff_author.setGeometry(QtCore.QRect(10, 486, 171, 20))
        self.ffComboBox.setGeometry(QtCore.QRect(6, 543, 400, 22))
        self.ffFuzzyAV.setAlignment(QtCore.Qt.AlignCenter)
        self.ffFuzzyAV.setGeometry(QtCore.QRect(540, 445, 24, 20))
        self.ffPullButton.setGeometry(QtCore.QRect(573, 283, 121, 23))
        self.ffPullButton.setStyleSheet("background-color: rgb(22, 53, 142);")
        self.ff_search_toggle.setCheckable(True)
        self.ff_search_toggle.setChecked(False)
        self.ff_search_toggle.setGeometry(QtCore.QRect(5, 441, 121, 23))
        self.ff_search_toggle.setStyleSheet("@QPushButton:checked {background-color: blue;}")
        self.ff_series.setGeometry(QtCore.QRect(200, 487, 221, 20))
        self.ff_title.setGeometry(QtCore.QRect(180, 455, 241, 20))
        self.ffTrackNo.setAlignment(QtCore.Qt.AlignCenter)
        self.ffTrackNo.setGeometry(QtCore.QRect(130, 455, 41, 20))
        self.ff_URL.setGeometry(QtCore.QRect(10, 518, 411, 20))
        self.ff_URL.setInputMethodHints(QtCore.Qt.ImhNone)
        self.file_series.setGeometry(QtCore.QRect(580, 221, 241, 20))
        self.file_author.setGeometry(QtCore.QRect(580, 258, 241, 20))
        self.file_ComboBox.setGeometry(QtCore.QRect(110, 16, 451, 22))
        self.FileLocation.setGeometry(QtCore.QRect(10, 50, 529, 21))
        self.file_title.setGeometry(QtCore.QRect(580, 183, 241, 20))
        self.file_book_number.setGeometry(QtCore.QRect(580, 143, 61, 20))
        self.finalAlbum.setGeometry(QtCore.QRect(581, 511, 241, 20))
        self.finalArtist.setGeometry(QtCore.QRect(581, 546, 241, 20))
        self.finalTrack.setGeometry(QtCore.QRect(578, 476, 241, 20))
        self.finalTrackNo.setGeometry(QtCore.QRect(579, 439, 61, 20))
        self.finishedArtWork.setGeometry(QtCore.QRect(642, 363, 191, 141))
        self.finishedArtWork.setOpenExternalLinks(False)
        self.finishedArtWork.setScaledContents(True)
        self.finishedArtWork.setStyleSheet("border-color: rgb(135, 135, 100);")
        self.FinishedLocation.setGeometry(QtCore.QRect(10, 110, 529, 21))
        self.goodreadsArtWork.setGeometry(QtCore.QRect(420, 309, 120, 120))
        self.goodreadsArtWork.setScaledContents(True)
        self.goodreads_author.setGeometry(QtCore.QRect(10, 354, 181, 20))
        self.goodreadsComboBox.setGeometry(QtCore.QRect(6, 413, 401, 22))
        self.goodreadsFuzzyAV.setAlignment(QtCore.Qt.AlignCenter)
        self.goodreadsFuzzyAV.setEnabled(True)
        self.goodreadsFuzzyAV.setGeometry(QtCore.QRect(540, 315, 24, 20))
        self.goodreads_search_toggle.setCheckable(True)
        self.goodreads_search_toggle.setChecked(False)
        self.goodreads_search_toggle.setGeometry(QtCore.QRect(5, 310, 91, 23))
        self.goodreads_search_toggle.setStyleSheet("@QPushButton:checked {background-color: blue;}")
        self.goodreadsPullButton.setGeometry(QtCore.QRect(573, 303, 101, 23))
        self.goodreadsPullButton.setStyleSheet("background-color: rgb(110, 59, 0);")
        self.goodreads_series.setGeometry(QtCore.QRect(210, 356, 211, 20))
        self.goodreads_title.setGeometry(QtCore.QRect(160, 322, 261, 20))
        self.goodreads_book_number.setAlignment(QtCore.Qt.AlignCenter)
        self.goodreads_book_number.setGeometry(QtCore.QRect(100, 322, 51, 20))
        self.goodreads_URL.setGeometry(QtCore.QRect(10, 389, 411, 20))
        self.googleArtWork.setGeometry(QtCore.QRect(420, 54, 120, 120))
        self.googleArtWork.setScaledContents(True)
        self.google_author.setGeometry(QtCore.QRect(10, 92, 171, 20))
        self.google_search_toggle.setCheckable(True)
        self.google_search_toggle.setChecked(False)
        self.google_search_toggle.setGeometry(QtCore.QRect(5, 44, 71, 23))
        self.google_search_toggle.setStyleSheet("@QPushButton:checked {background-color: blue;}")
        self.google_combobox.setGeometry(QtCore.QRect(10, 146, 401, 30))
        self.googleFuzzyAV.setAlignment(QtCore.Qt.AlignCenter)
        self.googleFuzzyAV.setGeometry(QtCore.QRect(540, 52, 24, 20))
        self.googlePullButton.setGeometry(QtCore.QRect(690, 303, 71, 23))
        self.googlePullButton.setStyleSheet("background-color: rgb(80, 0, 94);")
        self.google_series.setGeometry(QtCore.QRect(199, 93, 221, 20))
        self.google_title.setGeometry(QtCore.QRect(138, 60, 281, 20))
        self.google_book_number.setAlignment(QtCore.Qt.AlignCenter)
        self.google_book_number.setGeometry(QtCore.QRect(81, 60, 51, 20))
        self.label_10.setGeometry(QtCore.QRect(580, 123, 71, 20))
        self.label_12.setGeometry(QtCore.QRect(581, 421, 41, 20))
        self.label_14.setGeometry(QtCore.QRect(20, 90, 529, 15))
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_15.setGeometry(QtCore.QRect(20, 150, 529, 15))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_16.setGeometry(QtCore.QRect(581, 493, 41, 20))
        self.label_18.setGeometry(QtCore.QRect(583, 529, 51, 20))
        self.label_2.setGeometry(QtCore.QRect(580, 203, 41, 20))
        self.label_3.setGeometry(QtCore.QRect(580, 240, 51, 20))
        self.label_4.setGeometry(QtCore.QRect(580, 460, 61, 20))
        self.label_44.setGeometry(QtCore.QRect(84, 45, 41, 20))
        self.label_45.setGeometry(QtCore.QRect(12, 78, 51, 19))
        self.label_46.setGeometry(QtCore.QRect(12, 208, 51, 19))
        self.label_47.setGeometry(QtCore.QRect(93, 175, 41, 20))
        self.label_48.setGeometry(QtCore.QRect(102, 307, 41, 20))
        self.label_49.setGeometry(QtCore.QRect(12, 340, 51, 19))
        self.label_50.setGeometry(QtCore.QRect(12, 471, 51, 19))
        self.label_51.setGeometry(QtCore.QRect(130, 440, 41, 20))
        self.label_54.setGeometry(QtCore.QRect(140, 45, 61, 20))
        self.label_55.setGeometry(QtCore.QRect(152, 175, 61, 20))
        self.label_56.setGeometry(QtCore.QRect(163, 307, 61, 20))
        self.label_58.setGeometry(QtCore.QRect(12, 239, 21, 20))
        self.label_59.setGeometry(QtCore.QRect(181, 440, 61, 20))
        self.label_60.setGeometry(QtCore.QRect(201, 78, 31, 20))
        self.label_61.setGeometry(QtCore.QRect(210, 208, 30, 20))
        self.label_62.setGeometry(QtCore.QRect(200, 472, 31, 20))
        self.label_64.setGeometry(QtCore.QRect(210, 341, 31, 20))
        self.label_65.setGeometry(QtCore.QRect(12, 374, 21, 20))
        self.label_66.setGeometry(QtCore.QRect(12, 503, 21, 20))
        self.label_9.setGeometry(QtCore.QRect(20, 30, 529, 15))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label.setGeometry(QtCore.QRect(582, 163, 61, 20))
        self.open_folder_button.setGeometry(QtCore.QRect(10, 13, 91, 30))
        self.originalArtWork.setGeometry(QtCore.QRect(643, 33, 191, 151))
        self.originalArtWork.setOpenExternalLinks(False)
        self.originalArtWork.setScaledContents(True)
        self.originalArtWork.setStyleSheet("border-color: rgb(180, 180, 180);")
        self.saveButton_2.setGeometry(QtCore.QRect(760, 290, 71, 31))
        self.saveButton.setGeometry(QtCore.QRect(1060, -90, 81, 27))
        self.SaveFormatText.setGeometry(QtCore.QRect(10, 170, 529, 21))
        self.saveSettingsButton.setGeometry(QtCore.QRect(0, 210, 113, 32))
        self.search_button.setGeometry(QtCore.QRect(573, 3, 71, 27))
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setGeometry(QtCore.QRect(-4, 1, 841, 611))
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(False)
        self.WebSitecomboBox.setGeometry(QtCore.QRect(10, 250, 461, 22))

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)

        #added by Mike Treml
        self.button_configure()
        self.restore_settings()
        self.combobox_configure()
        self.image_refresh()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.audible_data_post.setText(_translate("MainWindow", "Audible"))
        self.audible_search_toggle.setText(_translate("MainWindow", "Audible"))
        self.ffPullButton.setText(_translate("MainWindow", "FantasticFiction"))
        self.ff_search_toggle.setText(_translate("MainWindow", "FantasticFiction"))
        self.file_book_number.setText(_translate("MainWindow", "001"))
        self.goodreads_search_toggle.setText(_translate("MainWindow", "Goodreads"))
        self.goodreadsPullButton.setText(_translate("MainWindow", "GoodReads"))
        self.google_search_toggle.setText(_translate("MainWindow", "Google"))
        self.googlePullButton.setText(_translate("MainWindow", "Google"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Final"))
        self.groupBox.setTitle(_translate("MainWindow", "Original"))
        self.label_10.setText(_translate("MainWindow", "Book #"))
        self.label_12.setText(_translate("MainWindow", "Book #"))
        self.label_14.setText(_translate("MainWindow", "Finished Location"))
        self.label_15.setText(_translate("MainWindow", "Save format"))
        self.label_16.setText(_translate("MainWindow", "Series"))
        self.label_18.setText(_translate("MainWindow", "Author"))
        self.label_2.setText(_translate("MainWindow", "Series"))
        self.label_3.setText(_translate("MainWindow", "Author"))
        self.label_4.setText(_translate("MainWindow", "Title"))
        self.label_44.setText(_translate("MainWindow", "Book #"))
        self.label_45.setText(_translate("MainWindow", "Author"))
        self.label_46.setText(_translate("MainWindow", "Author"))
        self.label_47.setText(_translate("MainWindow", "Book #"))
        self.label_48.setText(_translate("MainWindow", "Book #"))
        self.label_49.setText(_translate("MainWindow", "Author"))
        self.label_50.setText(_translate("MainWindow", "Author"))
        self.label_51.setText(_translate("MainWindow", "Book #"))
        self.label_54.setText(_translate("MainWindow", "Title"))
        self.label_55.setText(_translate("MainWindow", "Title"))
        self.label_56.setText(_translate("MainWindow", "Title"))
        self.label_58.setText(_translate("MainWindow", "URL"))
        self.label_59.setText(_translate("MainWindow", "Title"))
        self.label_60.setText(_translate("MainWindow", "Series"))
        self.label_61.setText(_translate("MainWindow", "Series"))
        self.label_62.setText(_translate("MainWindow", "Series"))
        self.label_64.setText(_translate("MainWindow", "Series"))
        self.label_65.setText(_translate("MainWindow", "URL"))
        self.label_66.setText(_translate("MainWindow", "URL"))
        self.label_9.setText(_translate("MainWindow", "Audiobooks location"))
        self.label.setText(_translate("MainWindow", "Title"))
        self.open_folder_button.setText(_translate("MainWindow", "Open Folder"))
        self.saveButton_2.setText(_translate("MainWindow", "SAVE"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.saveSettingsButton.setText(_translate("MainWindow", "Save Settings"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main), _translate("MainWindow", "Main"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), _translate("MainWindow", "Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Detailed"))

    def clear_fields(self):
        self.ffTrackNo.setText("")
        self.ff_title.setText("")
        self.ff_author.setText("")
        self.ff_series.setText("")
        self.ff_URL.setText("")
        self.ffFuzzyAV.setText("")

        self.google_book_number.setText("")
        self.google_title.setText("")
        self.google_author.setText("")
        self.google_series.setText("")
        self.googleFuzzyAV.setText("")

        self.goodreads_book_number.setText("")
        self.goodreads_title.setText("")
        self.goodreads_author.setText("")
        self.goodreads_series.setText("")
        self.goodreads_URL.setText("")
        self.goodreadsFuzzyAV.setText("")

        self.finalTrackNo.setText("")
        self.audibleTitleSearch.setText("")
        self.audibleAuthorSearch.setText("")
        self.audibleSeriesSearch.setText("")
        self.audible_URL.setText("")
        self.audibleFuzzyAV.setText("")

        self.audibleComboBox.clear()
        self.ffComboBox.clear()
        self.google_combobox.clear()

        self.deleteExist('assets/artwork/goodreadsArtWork.jpg')
        self.deleteExist('assets/artwork/finishedArtWork.jpg')
        self.deleteExist('assets/artwork/googleArtWork.jpg')
        self.deleteExist('assets/artwork/audibleArtWork.jpg')
        self.deleteExist('assets/artwork/ffArtWork.jpg')
        self.deleteExist('assets/artwork/originalArtWork.jpg')
        self.audibleComboBox = []
        self.ffComboBox = []
        self.goodreadsComboBox = []

    def button_configure(self):
        self.audible_data_post.clicked.connect(self.audible_save)
        self.ffPullButton.clicked.connect(self.ff_save)
        self.goodreadsPullButton.clicked.connect(self.goodreads_save)
        self.googlePullButton.clicked.connect(self.google_save)
        self.saveSettingsButton.clicked.connect(self.save_settings)
        self.search_button.clicked.connect(self.run_searches)
        #self.saveButton.clicked.connect(self.SaveBtn)
        self.open_folder_button.clicked.connect(self.file_combobox_update)

    def combobox_configure(self):
        self.file_ComboBox.currentIndexChanged.connect(self.file_combobox_select)
        self.google_combobox.currentIndexChanged.connect(self.google_ComboBox_select)
    # self.goodreadsComboBox.currentIndexChanged.connect(self.grComboBoxSelect)
    # self.audibleComboBox.currentIndexChanged.connect(self.aComboBoxSelect)
    #  self.ffComboBox.currentIndexChanged.connect(self.ffComboBoxSelect)




    def audible_save(self):
        self.finalTrack.setText(self.audibleTitleSearch.text())
        self.finalArtist.setText(self.audibleAuthorSearch.text())
        self.finalAlbum.setText(self.audibleSeriesSearch.text())
        self.finalTrackNo.setText(self.audibleTrackNoSearch.text())
        # artwork transfer

    def goodreads_save(self):
        self.finalTrack.setText(self.goodreads_title.text())
        self.finalArtist.setText(self.goodreads_author.text())
        self.finalAlbum.setText(self.goodreads_series.text())
        self.finalTrackNo.setText(self.goodreads_book_number.text())

    def ff_save(self):
        self.finalTrack.setText(self.ff_title.text())
        self.finalArtist.setText(self.ff_author.text())
        self.finalAlbum.setText(self.ff_series.text())
        self.finalTrackNo.setText(self.ffTrackNo.text())

    def google_save(self):
        self.finalTrack.setText(self.google_title.text())
        self.finalArtist.setText(self.google_author.text())
        self.finalAlbum.setText(self.google_series.text())
        self.finalTrackNo.setText(self.google_book_number.text())

    def image_refresh(self):
        self.googleArtWork.setPixmap(
            (QtGui.QPixmap("assets/artwork/googleArtWork.jpg")).scaled(self.googleArtWork.size(),
                                                                       QtCore.Qt.KeepAspectRatio))
        self.ffArtWork.setPixmap(
            (QtGui.QPixmap("assets/artwork/ffArtWork.jpg")).scaled(self.ffArtWork.size(),
                                                                   QtCore.Qt.KeepAspectRatio))
        self.audibleArtWork.setPixmap(
            (QtGui.QPixmap("assets/artwork/audibleArtWork.jpg")).scaled(self.audibleArtWork.size(),
                                                                        QtCore.Qt.KeepAspectRatio))
        self.goodreadsArtWork.setPixmap(
            (QtGui.QPixmap("assets/artwork/goodreadsArtWork.jpg")).scaled(self.goodreadsArtWork.size(),
                                                                          QtCore.Qt.KeepAspectRatio))
        self.finishedArtWork.setPixmap(
            (QtGui.QPixmap("assets/artwork/finishedArtWork.jpg")).scaled(self.finishedArtWork.size(),
                                                                         QtCore.Qt.KeepAspectRatio))
        self.originalArtWork.setPixmap(
            (QtGui.QPixmap("assets/artwork/originalArtWork.jpg")).scaled(self.originalArtWork.size(),
                                                                         QtCore.Qt.KeepAspectRatio))

    def deleteExist(self, path):
        file = pathlib.Path(path)
        if file.exists():
            os.remove(path)

    def file_locations(self):
        return self.FileLocation.text()

    def save_locations(self):
        return self.FinishedLocation.text()

    def save_format(self):
        return self.SaveFormatText.text()

    def restore_settings(self):
        db_file = "audiobookspython.db"
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        c = cur.execute("SELECT * FROM settings")
        settings = c.fetchall()
        print(settings[0])
        print()
        # ** needs a try catch if empty
        self.FileLocation.setText(settings[0][1])
        self.FinishedLocation.setText(settings[1][1])
        self.SaveFormatText.setText(settings[2][1])

    def save_settings(self):
        db_file = "audiobookspython.db"
        con = sqlite3.connect(db_file)
        query = "UPDATE settings SET setting = '" + self.FileLocation.text() + "' WHERE id = 1;"
        con.execute(query)
        query = " UPDATE settings SET setting= '" + self.FinishedLocation.text() + "' WHERE id=2;"
        con.execute(query)
        query = " UPDATE settings SET setting= '" + self.SaveFormatText.text() + "' WHERE id=3;"
        con.execute(query)
        con.commit()
        # **Create messagebox

    def file_combobox_update(self):
        self.file_ComboBox.clear()
        list_of_files = []
        for (dir_path, dir_names, filenames) in os.walk(self.file_locations()):
            for file in filenames:
                if "mp3" in file.lower():
                    self.file_ComboBox.addItem(file)

    def file_combobox_select(self):
        self.clear_fields()
        if self.file_ComboBox.currentText() != "":
            audio_file = eyed3.load(os.path.join(self.file_locations(), self.file_ComboBox.currentText()))
            title = str(audio_file.tag.title)
            author = str(audio_file.tag.artist)
            series = str(audio_file.tag.album)
            track_No = str(audio_file.tag.track_num[0])
            narrator = str(audio_file.tag.composer)
            release_Date = str(audio_file.tag.release_date)
            narrator = str(audio_file.tag.album_artist)
            genre = str(audio_file.tag.genre)
            audible_URL = str(audio_file.tag.artist_url).replace('None', '')
            ff_URL = str(audio_file.tag.commercial_url).replace('None', '')
            # google_URL = str(audio_file.tag.internet_radio_url).replace('None', '')
            goodreads_URL = str(audio_file.tag.copyright_url).replace('None', '')
            self.file_title.setText(title)
            self.file_author.setText(author)
            self.file_series.setText(series)
            self.file_book_number.setText(track_No)
            self.audible_URL.setText(audible_URL)
            self.ff_URL.setText(ff_URL)
            # self.google_URL.setText(google_URL)
            self.goodreads_URL.setText(goodreads_URL)
            for image in audio_file.tag.images:
                image_file = open("assets/artwork/{0}.jpg".format("originalArtWork"), "wb")
                image_file.write(image.image_data)
                image_file.close()
            self.image_refresh()

    def google_combobox_update(self, book_list):
        self.google_combobox.clear()
        for book in book_list:
            self.google_combobox.addItem(book['id'])

    def google_ComboBox_select(self):
        if self.google_combobox.currentIndex() >= 0:
            record = Functions.database_get(self.google_combobox.currentText(), "googlebooks")
            self.google_title.setText(record[1])
            self.google_author.setText(record[2])
            self.google_series.setText(record[4])
            try:
                req.urlretrieve(record[6], "assets/artwork/googleArtWork.jpg")
            except:
                print("image issue")
            self.image_refresh()
            self.googleFuzzyAV.setText(str(self.fuzzyRateFeild(record[1] + " " + record[2] + " " + record[4])))

    def run_searches(self):
        searchstring = self.file_title.text() + " " + self.ff_author.text() + " " + self.file_series.text()
        if self.google_search_toggle.isChecked():
            book_list = Functions.google_search(searchstring)
            self.google_combobox_update(book_list)
        # if self.audible_search_toggle.isChecked():
        # book_list = Functions.google_search(searchstring)
        # self.google_combobox_update(book_list)

    def fuzzyRateFeild(self, new_info):
        file_info: str = self.file_title.text() + ' ' + self.file_author.text() + ' ' + self.file_series.text()
        return fuzz.token_set_ratio(new_info, file_info.replace('None', ''))

if __name__ == "__main__":
    import sys

    app = QApplication([])
    app.setStyle("Fusion")
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
