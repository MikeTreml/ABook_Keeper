import operator
import os
import os.path
import pathlib
import shutil
import sqlite3
import ssl
import urllib.request as req
from datetime import datetime
from os import path
from pathlib import Path

import eyed3
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QMetaObject, QCoreApplication, QSize, QRect
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget, QLineEdit, QLabel, QGroupBox, QComboBox, \
    QTabWidget, QCheckBox
from fuzzywuzzy import fuzz

import Functions

audible_artwork = 'assets/artwork/audible_artwork.jpg'
google_artwork = 'assets/artwork/google_artwork.jpg'
ff_artwork = 'assets/artwork/ff_artwork.jpg'
goodreads_artwork = 'assets/artwork/goodreads_artwork.jpg'
finished_artwork = 'assets/artwork/finished_artwork.jpg'
database = "audiobookspython.db"
textbox_grey = "background-color: rgb(80, 80, 80);"
font_size = "Text-align:left; font-size: 10px"


class Ui_MainWindow(object):
    def __init__(self):
        self.main = QWidget()
        self.centralwidget = QWidget(MainWindow)

        self.settings = QWidget()
        self.goodreads_groupbox = QGroupBox(self.main)
        self.audible_groupbox = QtWidgets.QFrame(self.main)
        self.google_groupbox = QtWidgets.QFrame(self.main)
        self.final_groupbox = QtWidgets.QFrame(self.main)
        self.ff_groupbox = QtWidgets.QFrame(self.main)
        self.final_groupbox.lower()
        self.file_groupbox = QtWidgets.QFrame(self.main)
        self.audible_artwork = QLabel(self.audible_groupbox)
        self.audible_author = QPushButton(self.audible_groupbox)
        self.title_original_label = QLabel(self.file_groupbox)
        self.book_original_label = QLabel(self.file_groupbox)
        self.book_final_label = QLabel(self.final_groupbox)
        self.finished_location_label = QLabel(self.settings)
        self.save_format_label = QLabel(self.settings)
        self.series_final_label = QLabel(self.final_groupbox)
        self.author_final_label = QLabel(self.final_groupbox)
        self.series_original_label = QLabel(self.file_groupbox)
        self.author_original_label = QLabel(self.file_groupbox)
        self.filename_original_label = QLabel(self.file_groupbox)
        self.title_final_label = QLabel(self.final_groupbox)
        self.book_google_label = QLabel(self.google_groupbox)
        self.author_google_label = QLabel(self.google_groupbox)
        self.author_audible_label = QLabel(self.audible_groupbox)
        self.book_audible_label = QLabel(self.audible_groupbox)
        self.book_goodreads_label = QLabel(self.goodreads_groupbox)
        self.author_goodreads_label = QLabel(self.goodreads_groupbox)
        self.author_ff_label = QLabel(self.ff_groupbox)
        self.book_ff_label = QLabel(self.ff_groupbox)
        self.title_google_label = QLabel(self.google_groupbox)
        self.title_audible_label = QLabel(self.audible_groupbox)
        self.title_goodreads_label = QLabel(self.goodreads_groupbox)
        self.url_audible_label = QLabel(self.audible_groupbox)
        self.title_ff_label = QLabel(self.ff_groupbox)
        self.series_google_label = QLabel(self.google_groupbox)
        self.series_audible_label = QLabel(self.audible_groupbox)
        self.series_ff_label = QLabel(self.ff_groupbox)
        self.series_goodreads_label = QLabel(self.goodreads_groupbox)
        self.url_goodreads_label = QLabel(self.goodreads_groupbox)

        self.google_artwork = QLabel(self.google_groupbox)
        self.url_ff_label = QLabel(self.ff_groupbox)
        self.settings_file_location = QLabel(self.settings)
        self.original_artwork = QLabel(self.file_groupbox)
        self.ff_artwork = QLabel(self.ff_groupbox)
        self.finished_artwork = QLabel(self.final_groupbox)
        self.goodreads_artwork = QLabel(self.goodreads_groupbox)

        self.audible_combobox = QComboBox(self.audible_groupbox)
        self.audible_fuzzy = QLineEdit(self.audible_groupbox)
        self.audible_post_button = QPushButton(self.final_groupbox)
        self.audible_search_toggle = QCheckBox(self.main)

        self.audible_series = QPushButton(self.audible_groupbox)
        self.audible_title = QPushButton(self.audible_groupbox)
        self.audible_book_number = QPushButton(self.audible_groupbox)
        self.audible_URL = QLineEdit(self.audible_groupbox)

        self.ff_author = QPushButton(self.ff_groupbox)
        self.ff_combobox = QComboBox(self.ff_groupbox)
        self.ff_fuzzy = QLineEdit(self.ff_groupbox)
        self.ff_post_button = QPushButton(self.final_groupbox)
        self.ff_search_toggle = QCheckBox(self.main)
        self.ff_series = QPushButton(self.ff_groupbox)
        self.ff_title = QPushButton(self.ff_groupbox)
        self.ff_book_number = QPushButton(self.ff_groupbox)
        self.ff_URL = QLineEdit(self.ff_groupbox)
        self.file_series = QLineEdit(self.file_groupbox)
        self.file_author = QLineEdit(self.file_groupbox)
        self.file_name = QLineEdit(self.file_groupbox)
        self.file_combobox = QComboBox(self.main)
        self.FileLocation = QLineEdit(self.settings)
        self.file_title = QLineEdit(self.file_groupbox)
        self.file_book_number = QLineEdit(self.file_groupbox)
        self.final_series = QLineEdit(self.final_groupbox)
        self.final_author = QLineEdit(self.final_groupbox)
        self.final_title = QLineEdit(self.final_groupbox)
        self.final_book_number = QLineEdit(self.final_groupbox)

        self.FinishedLocation = QLineEdit(self.settings)

        self.goodreads_author = QPushButton(self.goodreads_groupbox)
        self.goodreads_combobox = QComboBox(self.goodreads_groupbox)
        self.goodreads_fuzzy = QLineEdit(self.goodreads_groupbox)
        self.goodreads_search_toggle = QCheckBox(self.main)
        self.goodreads_post_button = QPushButton(self.final_groupbox)
        self.goodreads_series = QPushButton(self.goodreads_groupbox)
        self.goodreads_title = QPushButton(self.goodreads_groupbox)
        self.goodreads_book_number = QPushButton(self.goodreads_groupbox)
        self.goodreads_URL = QLineEdit(self.goodreads_groupbox)

        self.google_author = QPushButton(self.google_groupbox)
        self.google_artwork_button = QPushButton(self.google_groupbox)
        self.audible_artwork_button = QPushButton(self.audible_groupbox)
        self.ff_artwork_button = QPushButton(self.ff_groupbox)
        self.goodreads_artwork_button = QPushButton(self.goodreads_groupbox)

        self.google_search_toggle = QCheckBox(self.main)
        self.google_combobox = QComboBox(self.google_groupbox)
        self.google_fuzzy = QLineEdit(self.google_groupbox)
        self.google_post_button = QPushButton(self.final_groupbox)
        self.google_series = QPushButton(self.google_groupbox)
        self.google_title = QPushButton(self.google_groupbox)
        self.google_book_number = QPushButton(self.google_groupbox)

        self.open_folder_button = QPushButton(self.main)

        self.save_button = QPushButton(self.final_groupbox)
        self.SaveFormatText = QLineEdit(self.settings)
        self.save_settings_button = QPushButton(self.settings)
        self.search_button = QPushButton(self.file_groupbox)

        self.tab = QWidget()
        self.tabWidget = QTabWidget(self.centralwidget)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.settings)

    def set_text_field(self):
        self.file_title.setStyleSheet(textbox_grey + font_size)
        self.file_book_number.setStyleSheet(textbox_grey)
        self.file_author.setStyleSheet(textbox_grey + font_size)
        self.file_name.setStyleSheet(textbox_grey + font_size)
        self.file_series.setStyleSheet(textbox_grey + font_size)

    def setupUi(self, MainWindow):
        font = QFont()
        font.setPointSize(7)
        MainWindow.resize(1112, 620)
        MainWindow.setInputMethodHints(Qt.ImhDate)
        MainWindow.setCentralWidget(self.centralwidget)
        QMetaObject.connectSlotsByName(MainWindow)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(30, 30, 30))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(100, 100, 100))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.black)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(50, 50, 50))
        palette.setColor(QPalette.ButtonText, Qt.black)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, Qt.black)
        palette.setColor(QPalette.HighlightedText, QColor(150, 150, 150))
        app.setPalette(palette)

        self.tabWidget.addTab(self.main, "")
        # self.tabWidget.addTab(self.tab, "")
        self.tabWidget.addTab(self.settings, "")

        # self.audible_book_number.setAlignment(Qt.AlignCenter)
        self.audible_fuzzy.setAlignment(Qt.AlignCenter)
        self.audible_search_toggle.setCheckable(True)
        self.audible_search_toggle.setChecked(True)
        self.audible_URL.setInputMethodHints(Qt.ImhNone)
        # self.ff_book_number.setAlignment(Qt.AlignCenter)
        self.ff_fuzzy.setAlignment(Qt.AlignCenter)
        self.ff_search_toggle.setCheckable(True)
        self.ff_search_toggle.setChecked(True)
        self.ff_URL.setInputMethodHints(Qt.ImhNone)
        # self.goodreads_book_number.setAlignment(Qt.AlignCenter)
        self.goodreads_fuzzy.setAlignment(Qt.AlignCenter)
        self.goodreads_search_toggle.setCheckable(True)
        self.goodreads_search_toggle.setChecked(True)
        # self.google_book_number.setAlignment(Qt.AlignCenter)
        self.google_fuzzy.setAlignment(Qt.AlignCenter)
        self.google_search_toggle.setCheckable(True)
        self.google_search_toggle.setChecked(True)
        self.finished_location_label.setMaximumSize(QSize(16777215, 15))
        self.save_format_label.setMaximumSize(QSize(16777215, 15))
        self.settings_file_location.setMaximumSize(QSize(16777215, 15))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(False)

        # added by Mike Treml
        self.set_ui_button()
        self.button_configure()
        self.restore_settings()
        self.combobox_configure()
        self.set_ui_color()
        Functions.delete_artwork()
        Functions.image_refresh(self)
        self.set_text_field()
        self.set_ui_readonly()
        self.set_ui_font()
        self.set_ui_size()
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.audible_post_button.setText(_translate("MainWindow", "Audible"))
        self.audible_search_toggle.setText(_translate("MainWindow", "Audible"))
        self.ff_post_button.setText(_translate("MainWindow", "FantasticFiction"))
        self.ff_search_toggle.setText(_translate("MainWindow", "FantasticFiction"))
        self.file_book_number.setText(_translate("MainWindow", "01"))
        self.goodreads_search_toggle.setText(_translate("MainWindow", "GoodReads"))
        self.goodreads_post_button.setText(_translate("MainWindow", "GoodReads"))
        self.google_search_toggle.setText(_translate("MainWindow", "Google"))
        self.google_post_button.setText(_translate("MainWindow", "Google"))

        self.book_original_label.setText(_translate("MainWindow", "Book #"))
        self.book_final_label.setText(_translate("MainWindow", "Book #"))
        self.finished_location_label.setText(_translate("MainWindow", "Finished Location"))
        self.save_format_label.setText(_translate("MainWindow", "Save format"))
        self.series_final_label.setText(_translate("MainWindow", "Series"))
        self.author_final_label.setText(_translate("MainWindow", "Author"))
        self.series_original_label.setText(_translate("MainWindow", "Series"))
        self.author_original_label.setText(_translate("MainWindow", "Author"))
        self.filename_original_label.setText(_translate("MainWindow", "File Name"))
        self.title_final_label.setText(_translate("MainWindow", "Title"))
        self.book_google_label.setText(_translate("MainWindow", "Book #"))
        self.author_google_label.setText(_translate("MainWindow", "Author"))
        self.author_audible_label.setText(_translate("MainWindow", "Author"))
        self.book_audible_label.setText(_translate("MainWindow", "Book #"))
        self.book_goodreads_label.setText(_translate("MainWindow", "Book #"))
        self.author_goodreads_label.setText(_translate("MainWindow", "Author"))
        self.author_ff_label.setText(_translate("MainWindow", "Author"))
        self.book_ff_label.setText(_translate("MainWindow", "Book #"))
        self.title_google_label.setText(_translate("MainWindow", "Title"))
        self.title_audible_label.setText(_translate("MainWindow", "Title"))
        self.title_goodreads_label.setText(_translate("MainWindow", "Title"))
        self.url_audible_label.setText(_translate("MainWindow", "URL"))
        self.title_ff_label.setText(_translate("MainWindow", "Title"))
        self.series_google_label.setText(_translate("MainWindow", "Series"))
        self.series_audible_label.setText(_translate("MainWindow", "Series"))
        self.series_ff_label.setText(_translate("MainWindow", "Series"))
        self.series_goodreads_label.setText(_translate("MainWindow", "Series"))
        self.url_goodreads_label.setText(_translate("MainWindow", "URL"))
        self.url_ff_label.setText(_translate("MainWindow", "URL"))
        self.settings_file_location.setText(_translate("MainWindow", "Audiobooks location"))
        self.title_original_label.setText(_translate("MainWindow", "Title"))
        self.open_folder_button.setText(_translate("MainWindow", "Open Folder"))
        self.save_button.setText(_translate("MainWindow", "SAVE"))
        self.save_settings_button.setText(_translate("MainWindow", "Save Settings"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main), _translate("MainWindow", "Main"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), _translate("MainWindow", "Settings"))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Detailed"))
        self.plainTextEdit.setPlainText(
            _translate("MainWindow", "Example: <author><folder><series> - <book #> <title> (<author>)\n"
                                     "\n"
                                     "Patrick Rothfuss\\The Kingkiller Chronicle - 03 The Doors of Stone (Patrick Rothfuss)\n"
                                     "\n"
                                     "Options:\n"
                                     "<folder>\n"
                                     "<author>\n"
                                     "<series>\n"
                                     "<title>\n"
                                     "<book #>"))

    def set_ui_readonly(self):
        self.ff_fuzzy.setReadOnly(True)
        self.audible_fuzzy.setReadOnly(True)
        self.goodreads_fuzzy.setReadOnly(True)
        self.google_fuzzy.setReadOnly(True)

    def set_ui_font(self):
        font = QFont()
        font.setPointSize(10)
        self.book_original_label.setFont(font)
        self.title_original_label.setFont(font)
        self.book_final_label.setFont(font)
        self.finished_location_label.setFont(font)
        self.save_format_label.setFont(font)
        self.series_final_label.setFont(font)
        self.author_final_label.setFont(font)
        self.series_original_label.setFont(font)
        self.author_original_label.setFont(font)
        self.filename_original_label.setFont(font)
        self.title_final_label.setFont(font)
        self.book_google_label.setFont(font)
        self.author_google_label.setFont(font)
        self.author_audible_label.setFont(font)
        self.book_audible_label.setFont(font)
        self.book_goodreads_label.setFont(font)
        self.author_goodreads_label.setFont(font)
        self.author_ff_label.setFont(font)
        self.book_ff_label.setFont(font)
        self.title_google_label.setFont(font)
        self.title_audible_label.setFont(font)
        self.title_goodreads_label.setFont(font)
        self.url_audible_label.setFont(font)
        self.title_ff_label.setFont(font)
        self.series_google_label.setFont(font)
        self.series_audible_label.setFont(font)
        self.series_ff_label.setFont(font)
        self.series_goodreads_label.setFont(font)
        self.url_goodreads_label.setFont(font)
        self.url_ff_label.setFont(font)
        self.settings_file_location.setFont(font)

    def set_ui_size(self):
        self.final_groupbox.setGeometry(QRect(570, 295, 540, 290))
        self.goodreads_groupbox.setGeometry(QRect(5, 315, 560, 130))
        self.google_groupbox.setGeometry(QRect(5, 45, 560, 130))
        self.ff_groupbox.setGeometry(QRect(5, 450, 560, 130))
        self.audible_groupbox.setGeometry(QRect(5, 180, 560, 130))
        self.file_groupbox.setGeometry(QRect(570, 0, 540, 290))
        self.final_groupbox.lower()

        fuzzy = QRect(533, 0, 27, 20)
        self.google_fuzzy.setGeometry(fuzzy)
        self.goodreads_fuzzy.setGeometry(fuzzy)
        self.ff_fuzzy.setGeometry(fuzzy)
        self.audible_fuzzy.setGeometry(fuzzy)

        self.audible_search_toggle.setGeometry(QRect(7, 180, 120, 20))
        self.ff_search_toggle.setGeometry(QRect(7, 450, 120, 20))
        self.goodreads_search_toggle.setGeometry(QRect(7, 315, 120, 20))
        self.google_search_toggle.setGeometry(QRect(7, 45, 120, 20))
        self.audible_search_toggle.raise_()
        self.ff_search_toggle.raise_()
        self.goodreads_search_toggle.raise_()
        self.google_search_toggle.raise_()

        author = QRect(10, 47, 190, 20)
        self.audible_author.setGeometry(author)
        self.ff_author.setGeometry(author)
        self.goodreads_author.setGeometry(author)
        self.google_author.setGeometry(author)

        book_number = QRect(130, 15, 40, 20)
        self.google_book_number.setGeometry(book_number)
        self.goodreads_book_number.setGeometry(book_number)
        self.ff_book_number.setGeometry(book_number)
        self.audible_book_number.setGeometry(book_number)

        small_artwork = QRect(432, 0, 130, 130)
        self.goodreads_artwork_button.setGeometry(small_artwork)
        self.goodreads_artwork.setGeometry(small_artwork)
        self.google_artwork.setGeometry(small_artwork)
        self.google_artwork_button.setGeometry(small_artwork)
        self.ff_artwork_button.setGeometry(small_artwork)
        self.audible_artwork_button.setGeometry(small_artwork)
        self.ff_artwork.setGeometry(small_artwork)
        self.audible_artwork.setGeometry(small_artwork)

        series = QRect(210, 47, 220, 20)
        self.goodreads_series.setGeometry(series)
        self.audible_series.setGeometry(series)
        self.ff_series.setGeometry(series)
        self.google_series.setGeometry(series)

        title = QRect(180, 15, 250, 20)
        self.audible_title.setGeometry(title)
        self.google_title.setGeometry(title)
        self.goodreads_title.setGeometry(title)
        self.ff_title.setGeometry(title)

        url = QRect(10, 80, 420, 20)
        self.goodreads_URL.setGeometry(url)
        self.ff_URL.setGeometry(url)
        self.audible_URL.setGeometry(url)

        combobox = QRect(10, 105, 420, 22)
        self.audible_combobox.setGeometry(combobox)
        self.goodreads_combobox.setGeometry(combobox)
        self.google_combobox.setGeometry(combobox)
        self.ff_combobox.setGeometry(combobox)

        main_book_number = QRect(10, 90, 60, 20)
        self.final_book_number.setGeometry(main_book_number)
        self.file_book_number.setGeometry(main_book_number)

        main_author = QRect(10, 210, 230, 20)
        self.file_author.setGeometry(main_author)
        self.final_author.setGeometry(main_author)

        self.file_name.setGeometry(QRect(10, 250, 230, 20))

        main_series = QRect(10, 170, 230, 20)
        self.final_series.setGeometry(main_series)
        self.file_series.setGeometry(main_series)

        main_title = QRect(10, 130, 230, 20)
        self.final_title.setGeometry(main_title)
        self.file_title.setGeometry(main_title)

        book_label = QRect(132, 0, 60, 20)
        self.book_google_label.setGeometry(book_label)
        self.book_ff_label.setGeometry(book_label)
        self.book_audible_label.setGeometry(book_label)
        self.book_goodreads_label.setGeometry(book_label)

        series_label = QRect(212, 32, 60, 20)
        self.series_google_label.setGeometry(series_label)
        self.series_audible_label.setGeometry(series_label)
        self.series_ff_label.setGeometry(series_label)
        self.series_goodreads_label.setGeometry(series_label)

        title_label = QRect(182, 0, 80, 20)
        self.title_ff_label.setGeometry(title_label)
        self.title_google_label.setGeometry(title_label)
        self.title_audible_label.setGeometry(title_label)
        self.title_goodreads_label.setGeometry(title_label)

        author_label = QRect(13, 32, 60, 19)
        self.author_google_label.setGeometry(author_label)
        self.author_audible_label.setGeometry(author_label)
        self.author_goodreads_label.setGeometry(author_label)
        self.author_ff_label.setGeometry(author_label)
        self.author_audible_label.lower()

        url_label = QRect(13, 65, 30, 20)
        self.url_audible_label.setGeometry(url_label)
        self.url_goodreads_label.setGeometry(url_label)
        self.url_ff_label.setGeometry(url_label)
        self.url_audible_label.lower()

        main_book_label = QRect(10, 74, 71, 20)
        self.book_original_label.setGeometry(main_book_label)
        self.book_final_label.setGeometry(main_book_label)

        main_title_label = QRect(10, 114, 61, 20)
        self.title_original_label.setGeometry(main_title_label)
        self.title_final_label.setGeometry(main_title_label)

        main_author_label = QRect(10, 194, 51, 20)
        self.author_original_label.setGeometry(main_author_label)
        self.author_final_label.setGeometry(main_author_label)

        self.filename_original_label.setGeometry(QRect(10, 234, 51, 20))

        main_series_label = QRect(10, 154, 41, 20)
        self.series_original_label.setGeometry(main_series_label)
        self.series_final_label.setGeometry(main_series_label)

        main_artwork = QRect(243, 0, 290, 290)
        self.original_artwork.setGeometry(main_artwork)
        self.finished_artwork.setGeometry(main_artwork)
        self.google_post_button.setGeometry(QRect(150, 40, 70, 20))
        self.ff_post_button.setGeometry(QRect(10, 10, 120, 20))
        self.audible_post_button.setGeometry(QRect(150, 10, 70, 20))
        self.goodreads_post_button.setGeometry(QRect(10, 40, 100, 20))
        self.save_button.setGeometry(QRect(90, 70, 70, 30))
        self.search_button.setGeometry(QRect(80, 60, 71, 30))
        self.save_format_label.setGeometry(QRect(20, 150, 529, 15))
        self.file_combobox.setGeometry(QRect(110, 16, 450, 22))
        self.finished_location_label.setGeometry(QRect(20, 90, 529, 15))
        self.settings_file_location.setGeometry(QRect(20, 30, 529, 15))
        self.open_folder_button.setGeometry(QRect(5, 15, 90, 25))
        self.FileLocation.setGeometry(QRect(10, 50, 529, 21))
        self.FinishedLocation.setGeometry(QRect(10, 110, 529, 21))
        self.plainTextEdit.setGeometry(QRect(5, 200, 671, 221))
        self.save_settings_button.setGeometry(QRect(10, 450, 113, 25))  #
        self.SaveFormatText.setGeometry(QRect(10, 170, 529, 21))
        self.tabWidget.setGeometry(QRect(0, 0, 1140, 620))

    def set_ui_color(self):
        self.google_groupbox.setStyleSheet("background-color: rgb(71, 24, 95);")
        self.final_groupbox.setStyleSheet("background-color: rgb(0, 60, 0);")
        self.goodreads_groupbox.setStyleSheet("background-color: rgb(75, 59, 39);")
        self.ff_groupbox.setStyleSheet("background-color: rgb(7, 44, 108);")
        self.audible_groupbox.setStyleSheet("background-color: rgb(118, 81, 8);")
        self.file_groupbox.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.search_button.setStyleSheet("background-color: rgb(100, 100, 100);")
        self.save_settings_button.setStyleSheet("background-color: rgb(100, 100, 100);")
        self.audible_post_button.setStyleSheet("background-color: rgb(118, 81, 8);")
        self.ff_post_button.setStyleSheet("background-color: rgb(7, 44, 108);")
        self.goodreads_post_button.setStyleSheet("background-color: rgb(75, 59, 39);")
        self.google_post_button.setStyleSheet("background-color: rgb(71, 24, 95);")

        self.audible_search_toggle.raise_()

    def set_ui_button(self):
        self.final_series.setStyleSheet(textbox_grey + font_size)
        self.final_book_number.setStyleSheet(textbox_grey + font_size)
        self.final_title.setStyleSheet(textbox_grey + font_size)
        self.final_author.setStyleSheet(textbox_grey + font_size)

        self.ff_book_number.setStyleSheet(textbox_grey)
        self.ff_title.setStyleSheet(textbox_grey + font_size)
        self.ff_author.setStyleSheet(textbox_grey + font_size)
        self.ff_series.setStyleSheet(textbox_grey + font_size)
        self.ff_URL.setStyleSheet("background-color: rgb(100, 100, 100);" + font_size)

        self.google_book_number.setStyleSheet(textbox_grey)
        self.google_title.setStyleSheet(textbox_grey + font_size)
        self.google_author.setStyleSheet(textbox_grey + font_size)
        self.google_series.setStyleSheet(textbox_grey + font_size)
        # self.google_URL.setStyleSheet(textbox_grey +font_size)

        self.goodreads_book_number.setStyleSheet(textbox_grey)
        self.goodreads_title.setStyleSheet(textbox_grey + font_size)
        self.goodreads_author.setStyleSheet(textbox_grey + font_size)
        self.goodreads_series.setStyleSheet(textbox_grey + font_size)
        self.goodreads_URL.setStyleSheet("background-color: rgb(100, 100, 100);" + font_size)

        self.audible_book_number.setStyleSheet(textbox_grey)
        self.audible_title.setStyleSheet(textbox_grey + font_size)
        self.audible_author.setStyleSheet(textbox_grey + font_size)
        self.audible_series.setStyleSheet(textbox_grey + font_size)
        self.audible_URL.setStyleSheet("background-color: rgb(100, 100, 100); color: rgb(0, 0, 0);" + font_size)
        self.goodreads_URL.setStyleSheet("background-color: rgb(100, 100, 100); color: rgb(0, 0, 0);" + font_size)
        self.ff_URL.setStyleSheet("background-color: rgb(100, 100, 100); color: rgb(0, 0, 0);" + font_size)
        self.search_button.setStyleSheet(textbox_grey + " font-size: 12px")
        self.open_folder_button.setStyleSheet("background-color: rgb(100, 100, 100);")
        self.save_button.setStyleSheet("background-color: rgb(100, 100, 100);")
        self.ff_combobox.setStyleSheet("background-color: rgb(60, 60, 60);" + font_size)
        self.audible_combobox.setStyleSheet("background-color: rgb(60, 60, 60);" + font_size)
        self.goodreads_combobox.setStyleSheet("background-color: rgb(60, 60, 60);" + font_size)
        self.google_combobox.setStyleSheet("background-color: rgb(60, 60, 60);" + font_size)
        self.file_combobox.setStyleSheet("color: rgb(255, 255, 255);")
        self.google_artwork_button.setFlat(True)
        self.audible_artwork_button.setFlat(True)
        self.ff_artwork_button.setFlat(True)
        self.goodreads_artwork_button.setFlat(True)

    def clear_fields(self):
        self.ff_book_number.setText("")
        self.ff_title.setText("")
        self.ff_author.setText("")
        self.ff_series.setText("")
        self.ff_URL.setText("")
        self.ff_fuzzy.setText("")

        self.google_book_number.setText("")
        self.google_title.setText("")
        self.google_author.setText("")
        self.google_series.setText("")
        self.google_fuzzy.setText("")

        self.final_book_number.setText("")
        self.final_title.setText("")
        self.final_author.setText("")
        self.final_series.setText("")

        self.goodreads_book_number.setText("")
        self.goodreads_title.setText("")
        self.goodreads_author.setText("")
        self.goodreads_series.setText("")
        self.goodreads_URL.setText("")
        self.goodreads_fuzzy.setText("")

        self.audible_title.setText("")
        self.audible_author.setText("")
        self.audible_series.setText("")
        self.audible_URL.setText("")
        self.audible_fuzzy.setText("")
        self.audible_book_number.setText("")

        self.audible_combobox.clear()
        self.ff_combobox.clear()
        self.google_combobox.clear()
        self.goodreads_combobox.clear()
        self.audible_fuzzy.setStyleSheet("background-color: grey")
        self.google_fuzzy.setStyleSheet("background-color: grey")
        self.goodreads_fuzzy.setStyleSheet("background-color: grey")
        self.ff_fuzzy.setStyleSheet("background-color: grey")

        # self.audible_combobox = []
        # self.ff_combobox = []
        # self.goodreads_combobox = []
        # self.google_combobox = []
        Functions.delete_artwork()

    def button_configure(self):
        self.audible_post_button.clicked.connect(self.audible_save)
        self.ff_post_button.clicked.connect(self.ff_save)
        self.goodreads_post_button.clicked.connect(self.goodreads_save)
        self.google_post_button.clicked.connect(self.google_save)
        self.save_settings_button.clicked.connect(self.save_settings)
        self.search_button.clicked.connect(self.run_searches)
        self.save_button.clicked.connect(self.save)
        self.open_folder_button.clicked.connect(self.file_combobox_update)

        self.ff_book_number.clicked.connect(self.final_number_ff)
        self.google_book_number.clicked.connect(self.final_number_google)
        self.goodreads_book_number.clicked.connect(self.final_number_goodreads)
        self.audible_book_number.clicked.connect(self.final_number_audible)

        self.ff_title.clicked.connect(self.final_title_ff)
        self.google_title.clicked.connect(self.final_title_google)
        self.goodreads_title.clicked.connect(self.final_title_goodreads)
        self.audible_title.clicked.connect(self.final_title_audible)

        self.ff_author.clicked.connect(self.final_author_ff)
        self.google_author.clicked.connect(self.final_author_google)
        self.goodreads_author.clicked.connect(self.final_author_goodreads)
        self.audible_author.clicked.connect(self.final_author_audible)

        self.ff_series.clicked.connect(self.final_series_ff)
        self.google_series.clicked.connect(self.final_series_google)
        self.goodreads_series.clicked.connect(self.final_series_goodreads)
        self.audible_series.clicked.connect(self.final_series_audible)

        self.google_artwork_button.clicked.connect(self.final_artwork_google)
        self.audible_artwork_button.clicked.connect(self.final_artwork_audible)
        self.ff_artwork_button.clicked.connect(self.final_artwork_ff)
        self.goodreads_artwork_button.clicked.connect(self.final_artwork_goodreads)

    def combobox_configure(self):
        self.file_combobox.currentIndexChanged.connect(self.file_combobox_select)
        self.google_combobox.currentIndexChanged.connect(self.combobox_google_select)
        self.audible_combobox.currentIndexChanged.connect(self.combobox_audible_select)
        self.goodreads_combobox.currentIndexChanged.connect(self.combobox_goodreads_select)
        self.ff_combobox.currentIndexChanged.connect(self.combobox_ff_select)

    # button fields to transfer info to the final result*************
    def final_artwork_audible(self):
        if path.exists(audible_artwork):
            shutil.copy(audible_artwork, finished_artwork)
            Functions.image_refresh(self)

    def final_artwork_goodreads(self):
        if path.exists(goodreads_artwork):
            shutil.copy(goodreads_artwork, finished_artwork)
            Functions.image_refresh(self)

    def final_artwork_google(self):
        if path.exists(google_artwork):
            shutil.copy(google_artwork, finished_artwork)
            Functions.image_refresh(self)

    def final_artwork_ff(self):
        if path.exists(ff_artwork):
            shutil.copy(ff_artwork, finished_artwork)
            Functions.image_refresh(self)

    def final_series_ff(self):
        self.final_series.setText(self.ff_series.text())

    def final_series_google(self):
        self.final_series.setText(self.google_series.text())

    def final_series_goodreads(self):
        self.final_series.setText(self.goodreads_series.text())

    def final_series_audible(self):
        self.final_series.setText(self.audible_series.text())

    def final_title_ff(self):
        self.final_title.setText(self.ff_title.text())

    def final_title_google(self):
        self.final_title.setText(self.google_title.text())

    def final_title_goodreads(self):
        self.final_title.setText(self.goodreads_title.text())

    def final_title_audible(self):
        self.final_title.setText(self.audible_title.text())

    def final_author_ff(self):
        self.final_author.setText(self.ff_author.text())

    def final_author_google(self):
        self.final_author.setText(self.google_author.text())

    def final_author_goodreads(self):
        self.final_author.setText(self.goodreads_author.text())

    def final_author_audible(self):
        self.final_author.setText(self.audible_author.text())

    def final_number_ff(self):
        self.final_book_number.setText(self.ff_book_number.text())

    def final_number_google(self):
        self.final_book_number.setText(self.google_book_number.text())

    def final_number_goodreads(self):
        self.final_book_number.setText(self.goodreads_book_number.text())

    def final_number_audible(self):
        self.final_book_number.setText(self.audible_book_number.text())

    def audible_save(self):
        self.final_title.setText(self.audible_title.text())
        self.final_author.setText(self.audible_author.text())
        self.final_series.setText(self.audible_series.text())
        self.final_book_number.setText(self.audible_book_number.text())
        if os.path.exists(audible_artwork):
            shutil.copy(audible_artwork, finished_artwork)
        Functions.image_refresh(self)

    def goodreads_save(self):
        self.final_title.setText(self.goodreads_title.text())
        self.final_author.setText(self.goodreads_author.text())
        self.final_series.setText(self.goodreads_series.text())
        self.final_book_number.setText(self.goodreads_book_number.text())
        if os.path.exists(goodreads_artwork):
            shutil.copy(goodreads_artwork, finished_artwork)
        Functions.image_refresh(self)

    def ff_save(self):
        self.final_title.setText(self.ff_title.text())
        self.final_author.setText(self.ff_author.text())
        self.final_series.setText(self.ff_series.text())
        self.final_book_number.setText(self.ff_book_number.text())
        if os.path.exists(ff_artwork):
            shutil.copy(ff_artwork, finished_artwork)
        Functions.image_refresh(self)

    def google_save(self):
        self.final_title.setText(self.google_title.text())
        self.final_author.setText(self.google_author.text())
        self.final_series.setText(self.google_series.text())
        self.final_book_number.setText(self.google_book_number.text())
        if os.path.exists(google_artwork):
            shutil.copy(google_artwork, finished_artwork)
        Functions.image_refresh(self)

    def file_locations(self):
        return self.FileLocation.text()

    def save_locations(self):
        return self.FinishedLocation.text()

    def save_format(self):
        return self.SaveFormatText.text()

    def restore_settings(self):
        db_file = database
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        c = cur.execute("SELECT * FROM settings")
        settings = c.fetchall()
        # ** needs a try catch if empty
        self.FileLocation.setText(settings[0][1])
        self.FinishedLocation.setText(settings[1][1])
        self.SaveFormatText.setText(settings[2][1])

    def save_settings(self):
        db_file = database
        con = sqlite3.connect(db_file)
        query = "UPDATE settings SET setting = '" + self.FileLocation.text() + "' WHERE id = 1;"
        con.execute(query)
        query = " UPDATE settings SET setting= '" + self.FinishedLocation.text() + "' WHERE id=2;"
        con.execute(query)
        query = " UPDATE settings SET setting= '" + self.SaveFormatText.text() + "' WHERE id=3;"
        con.execute(query)
        con.commit()
        # **Create messagebox

    def save(self):
        if self.final_author.text() + self.final_series.text() + self.final_title.text() != "":
            # file_loacation = self.file_locations() + self.file_combobox.currentText()
            file = self.file_combobox.currentText().replace("\u202a", "")
            audiofile = eyed3.load(file)
            audiofile.tag.artist = self.final_author.text().replace("∶", "")
            audiofile.tag.album = self.final_series.text().replace("∶", "")
            audiofile.tag.title = self.final_title.text().replace("∶", "")
            audiofile.tag.save()
            # posting twice for the same artwork. one for file view and one shows up in itunes
            try:
                imagedata = open(finished_artwork, "rb").read()
                audiofile.tag.images.set(1, imagedata, 'image/jpeg', u"")
                audiofile.tag.save()
                audiofile1 = eyed3.load(file)
                audiofile1.tag.images.set(3, imagedata, 'image/jpeg', u'front 3')
                audiofile1.tag.save()
            except:
                print("no new artwork")
            save_format = self.save_format()
            save_string_settings = str(save_format).replace("<series>", "{1}").replace("<book #>", "{2}").replace(
                "<title>", "{3}").replace("<author>", "{4}").replace("<folder>", "/")
            save_pattern = "{0}" + save_string_settings + "{5}"
            locat = self.FinishedLocation.text()
            extension = os.path.splitext(os.path.basename(file))[1]
            if "<folder>" in save_format:
                folders = save_pattern.split("/")
                folders_pattern = save_pattern.replace(folders[-1], "")
                new_folders = folders_pattern.format(locat, self.final_series.text(), self.final_book_number.text(),
                                                     self.final_title.text(), self.audible_author.text(), extension)
                if not os.path.exists(new_folders):
                    os.makedirs(new_folders)

            dst = locat + os.path.basename(file)
            shutil.move(file, dst)

            new_filename = save_pattern.format(locat, self.final_series.text(), self.final_book_number.text(),
                                               self.final_title.text(), self.audible_author.text(), extension)
            print('dst', dst)
            print(new_filename)
            file = pathlib.Path(new_filename)
            if file.exists():
                print("File exist")
            else:
                os.rename(dst, new_filename)

            self.clear_fields()
            self.file_combobox.removeItem(self.file_combobox.currentIndex())
            print('files left ', self.file_combobox.count())
        Functions.delete_artwork()
        Functions.image_refresh(self)

    def file_combobox_select(self):
        self.clear_fields()
        combobox_string = self.file_combobox.currentText()
        if combobox_string != "":
            try:
                audio_file = eyed3.load(os.path.join(self.file_locations(), Path(self.file_combobox.currentText())))
            except:
                audio_file = eyed3.load(combobox_string)
            if "/" in combobox_string:
                file = combobox_string.split("/")[-1]
            else:
                file = combobox_string.split("\\")[-1]
            title = str(audio_file.tag.title)
            author = str(audio_file.tag.artist)
            series = str(audio_file.tag.album)
            track_No = str(audio_file.tag.track_num[0])
            # narrator = str(audio_file.tag.composer)
            # release_Date = str(audio_file.tag.release_date)
            # narrator = str(audio_file.tag.album_artist)
            # genre = str(audio_file.tag.genre)
            audible_URL = str(audio_file.tag.artist_url).replace('None', '')
            ff_URL = str(audio_file.tag.commercial_url).replace('None', '')
            # google_URL = str(audio_file.tag.internet_radio_url).replace('None', '')
            goodreads_URL = str(audio_file.tag.copyright_url).replace('None', '')
            self.file_title.setText(title.replace("None", ""))
            self.file_author.setText(author.replace("None", ""))
            self.file_name.setText(file.replace(".mp3", "").replace("None", ""))
            self.file_series.setText(series.replace("None", ""))
            self.file_book_number.setText(track_No.replace("None", ""))
            self.audible_URL.setText(audible_URL)
            self.ff_URL.setText(ff_URL)
            # self.google_URL.setText(google_URL)
            self.goodreads_URL.setText(goodreads_URL)
            for image in audio_file.tag.images:
                image_file = open("assets/artwork/{0}.jpg".format("original_artwork"), "wb")
                image_file.write(image.image_data)
                image_file.close()
            Functions.image_refresh(self)

    def combobox_google_select(self):
        if self.google_combobox.currentIndex() >= 0:
            print(self.google_combobox.currentIndex())
            record = Functions.database_get(self.google_combobox.currentText(), "googlebooks")
            # print(record)
            self.google_title.setText(record[1])
            self.google_author.setText(record[2])
            self.google_series.setText(record[4])
            try:
                req.urlretrieve(record[6], google_artwork)
            except:
                print("image issue")
            Functions.image_refresh(self)
            fuzzy = self.fuzzyRateFeild(record[1] + " " + record[2] + " " + record[4])
            fuzzy = fuzzy - self.fuzzy_blank_adjustment(self.google_title, self.google_author, self.google_series)
            self.google_fuzzy.setText(str(fuzzy))
            if fuzzy >= 90:
                self.google_fuzzy.setStyleSheet("background-color: green; color: black")
            elif fuzzy >= 60:
                self.google_fuzzy.setStyleSheet("background-color: yellow; color: black")
            else:
                self.google_fuzzy.setStyleSheet("background-color: red; color: black")

    def combobox_ff_select(self):
        if self.ff_combobox.currentIndex() >= 0:
            print(self.google_combobox.currentIndex())
            record = Functions.database_get(self.ff_combobox.currentText(), "fantasticfiction")
            print(record)
            self.ff_title.setText(record[1])
            self.ff_author.setText(record[2])
            self.ff_series.setText(record[4])
            self.ff_book_number.setText(record[5])
            self.ff_URL.setText(record[11])
            try:
                ssl._create_default_https_context = ssl._create_unverified_context
                req.urlretrieve(record[8], ff_artwork)
            except:
                print("image issue")
            Functions.image_refresh(self)
            fuzzy = self.fuzzyRateFeild(record[1] + " " + record[2] + " " + record[4])
            fuzzy = fuzzy - self.fuzzy_blank_adjustment(self.ff_title, self.ff_author, self.ff_series)
            self.ff_fuzzy.setText(str(fuzzy))
            if fuzzy >= 90:
                self.ff_fuzzy.setStyleSheet("background-color: green; color: black")
            elif fuzzy >= 60:
                self.ff_fuzzy.setStyleSheet("background-color: yellow; color: black")
            else:
                self.ff_fuzzy.setStyleSheet("background-color: red; color: black")

    def combobox_audible_select(self):
        if self.audible_combobox.currentIndex() >= 0:
            id = self.audible_combobox.currentText().split(" - ")[-1]
            #print(id)
            record = Functions.database_get(id, "audible")
            #print(record)
            self.audible_title.setText(record[1])
            self.audible_author.setText(record[2])
            self.audible_series.setText(record[4])
            self.audible_book_number.setText(record[5])
            self.audible_URL.setText(record[11])
            #print(record[8])
            try:
                ssl._create_default_https_context = ssl._create_unverified_context
                req.urlretrieve(record[8], audible_artwork)
            except:
                print("image issue")
            Functions.image_refresh(self)
            fuzzy = self.fuzzyRateFeild(record[1] + " " + record[2] + " " + record[4])
            fuzzy = fuzzy - self.fuzzy_blank_adjustment(self.audible_title, self.audible_author, self.audible_series)
            self.audible_fuzzy.setText(str(fuzzy))
            if fuzzy >= 90:
                self.audible_fuzzy.setStyleSheet("background-color: green; color: black")
            elif fuzzy >= 60:
                self.audible_fuzzy.setStyleSheet("background-color: yellow; color: black")
            else:
                self.audible_fuzzy.setStyleSheet("background-color: red; color: black")

    def combobox_goodreads_select(self):
        if self.goodreads_combobox.currentIndex() >= 0:
            id = self.goodreads_combobox.currentText().split(" - ")[-1]
            record = Functions.database_get(id, "goodreads")
            #print(record)
            self.goodreads_title.setText(record[1])
            self.goodreads_author.setText(record[2])
            self.goodreads_series.setText(record[4])
            self.goodreads_URL.setText(record[11])
            self.goodreads_book_number.setText(record[5])
            # print(record[8])
            try:
                ssl._create_default_https_context = ssl._create_unverified_context
                req.urlretrieve(record[8], goodreads_artwork)
            except:
                print("image issue")
            Functions.image_refresh(self)
            fuzzy = self.fuzzyRateFeild(record[1] + " " + record[2] + " " + record[4])
            fuzzy = fuzzy - self.fuzzy_blank_adjustment(self.goodreads_title, self.goodreads_author,
                                                        self.goodreads_series)
            self.goodreads_fuzzy.setText(str(fuzzy))
            if fuzzy >= 90:
                self.goodreads_fuzzy.setStyleSheet("background-color: green; color: black")
            elif fuzzy >= 60:
                self.goodreads_fuzzy.setStyleSheet("background-color: yellow; color: black")
            else:
                self.goodreads_fuzzy.setStyleSheet("background-color: red; color: black")

    # combobox update ********************************
    def file_combobox_update(self):
        self.file_combobox.clear()
        files = self.file_locations().replace("\u202a", "")
        self.path = files
        for (dir_path, dir_names, file_names) in os.walk(self.path):
            listOfFiles = [os.path.join(dir_path, file) for file in file_names]
            for file in listOfFiles:
                if "mp3" in file:
                    # print(file)
                    self.file_combobox.addItem(file)

    def google_combobox_update(self, book_list):
        self.google_combobox.blockSignals(True)
        self.google_combobox.clear()
        self.google_combobox.blockSignals(False)
        for book in book_list:
            self.google_combobox.addItem(book['id'])

    def audible_combobox_update(self, book_list):
        self.audible_combobox.blockSignals(True)
        self.audible_combobox.clear()
        self.audible_combobox.blockSignals(False)
        for book in book_list:
            self.audible_combobox.addItem(
                book['title'] + " " + book['series'] + " " + book['author'] + " - " + book['id'])

    def goodreads_combobox_update(self, book_list):
        self.goodreads_combobox.blockSignals(True)
        self.goodreads_combobox.clear()
        self.goodreads_combobox.blockSignals(False)
        if book_list is not None:
            for book in book_list:
                self.goodreads_combobox.addItem(
                    book['title'] + " " + book['series'] + " " + book['author'] + " - " + book['id'])

    def ff_combobox_update(self, book_list):
        self.ff_combobox.blockSignals(True)
        self.ff_combobox.clear()
        self.ff_combobox.blockSignals(False)
        for book in book_list:
            self.ff_combobox.addItem(book['id'])

    def run_searches(self):
        start = datetime.now()
        QApplication.setOverrideCursor(Qt.WaitCursor)
        if self.file_combobox.currentIndex() >= 0:
            search_fields = self.word_duplicate_remove(self.file_title.text() + " " +
                                                       self.file_author.text() + " " +
                                                       self.file_series.text() + " " +
                                                       self.file_name.text())
            search_string = search_fields.replace(";", "").replace(":", "").replace("'", "").replace(",", "+").replace(
                "-", "+").replace("book", "").replace("0", "").replace("None", "").replace(" ", "+")
            if self.google_search_toggle.isChecked():
                book_list = Functions.google_search(search_string)
                self.google_combobox_update(book_list)
            if self.audible_search_toggle.isChecked():
                book_list = Functions.audible_scrapper(search_string)
                book_list_sorted = self.fuzzy_sort(book_list)
                self.audible_combobox_update(book_list_sorted)
            if self.goodreads_search_toggle.isChecked():
                book_list = Functions.goodreads_srcapper(search_string)
                self.goodreads_combobox_update(book_list)
            if self.ff_search_toggle.isChecked():
                book_list = Functions.ff_search(search_string)
                self.ff_combobox_update(book_list)
        QApplication.restoreOverrideCursor()
        print('GradeWebsite', datetime.now() - start)

    def word_duplicate_remove(self, string):
        list_string = string.lower().split(" ")
        new_string = ""
        for word in list_string:
            if word not in new_string:
                new_string += " " + word
        return new_string

    def fuzzyRateFeild(self, new_info):
        file_info: str = self.file_title.text() + ' ' + self.file_author.text() + ' ' + self.file_series.text()
        return fuzz.token_set_ratio(new_info, file_info.replace('None', ''))

    def fuzzy_sort(self, book_list):
        rating_list = []
        search_string = self.word_duplicate_remove(
            self.file_title.text() + " " + self.file_author.text() + " " + self.file_series.text()).lower().replace(
            "None", "")
        for book in book_list:
            rating_list.append(
                [fuzz.token_set_ratio(search_string, book['title'] + " " + book['series'] + " " + book['author']),
                 book])
        sorted_list = sorted(rating_list, key=operator.itemgetter(0), reverse=True)
        result = [item[1] for item in sorted_list]
        return result

    def fuzzy_blank_adjustment(self, string1, string2, string3):
        count = 0
        if string1 == "":
            count += 10
        if string2 == "":
            count += 10
        if string3 == "":
            count += 10
        return count

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
