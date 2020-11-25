import os
import pathlib
import shutil
import sqlite3
import ssl
import urllib.request as req

import eyed3
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QMetaObject, QCoreApplication, QRect, QSize
from PyQt5.QtGui import QPalette, QColor, QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget, QLineEdit, QLabel, QGroupBox, QComboBox, \
    QTabWidget, QCheckBox
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

        self.audible_artwork = QLabel(self.main)
        self.audible_author = QLineEdit(self.main)
        self.audible_combobox = QComboBox(self.main)
        self.audible_fuzzy = QLineEdit(self.main)
        self.audible_post_button = QPushButton(self.main)
        self.audible_search_toggle = QCheckBox(self.main)
        self.audible_series = QLineEdit(self.main)
        self.audible_title = QLineEdit(self.main)
        self.audible_book_number = QLineEdit(self.main)
        self.audible_URL = QLineEdit(self.main)
        self.ff_artwork = QLabel(self.main)
        self.ff_author = QLineEdit(self.main)
        self.ff_combobox = QComboBox(self.main)
        self.ff_fuzzy = QLineEdit(self.main)
        self.ff_post_button = QPushButton(self.main)
        self.ff_search_toggle = QCheckBox(self.main)
        self.ff_series = QLineEdit(self.main)
        self.ff_title = QLineEdit(self.main)
        self.ff_book_number = QLineEdit(self.main)
        self.ff_URL = QLineEdit(self.main)
        self.file_series = QLineEdit(self.main)
        self.file_author = QLineEdit(self.main)
        self.file_combobox = QComboBox(self.main)
        self.FileLocation = QLineEdit(self.settings)
        self.file_title = QLineEdit(self.main)
        self.file_book_number = QLineEdit(self.main)
        self.final_series = QLineEdit(self.main)
        self.final_author = QLineEdit(self.main)
        self.final_title = QLineEdit(self.main)
        self.final_book_number = QLineEdit(self.main)
        self.finished_artwork = QLabel(self.main)
        self.FinishedLocation = QLineEdit(self.settings)
        self.goodreads_artwork = QLabel(self.main)
        self.goodreads_author = QLineEdit(self.main)
        self.goodreads_combobox = QComboBox(self.main)
        self.goodreads_fuzzy = QLineEdit(self.main)
        self.goodreads_search_toggle = QCheckBox(self.main)
        self.goodreads_post_button = QPushButton(self.main)
        self.goodreads_series = QLineEdit(self.main)
        self.goodreads_title = QLineEdit(self.main)
        self.goodreads_book_number = QLineEdit(self.main)
        self.goodreads_URL = QLineEdit(self.main)
        self.google_artwork = QLabel(self.main)
        self.google_author = QLineEdit(self.main)
        self.google_search_toggle = QCheckBox(self.main)
        self.google_combobox = QComboBox(self.main)
        self.google_fuzzy = QLineEdit(self.main)
        self.google_post_button = QPushButton(self.main)
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
        self.original_artwork = QLabel(self.main)
        self.save_button = QPushButton(self.main)
        self.SaveFormatText = QLineEdit(self.settings)
        self.save_settings_button = QPushButton(self.settings)
        self.search_button = QPushButton(self.main)
        self.tab = QWidget()
        self.tabWidget = QTabWidget(self.centralwidget)

    def setupUi(self, MainWindow):
        font = QFont()
        font.setPointSize(7)
        MainWindow.resize(1140, 620)
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
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        app.setPalette(palette)

        self.groupBox.setGeometry(QRect(570, 0, 250, 290))
        self.groupBox.setStyleSheet("background-color: rgba(0, 0, 0, 100);")

        self.groupBox_5.setGeometry(QRect(5, 450, 560, 130))
        self.groupBox_5.setStyleSheet("background-color: rgba(10, 95, 255, 100);")

        self.groupBox_3.setGeometry(QRect(5, 315, 560, 130))
        self.groupBox_3.setStyleSheet("background-color: rgba(144, 113, 76, 100);")

        self.groupBox_6.setGeometry(QRect(5, 180, 560, 130))
        self.groupBox_6.setStyleSheet("background-color: rgba(254, 172, 12, 100);")

        self.groupBox_4.setGeometry(QRect(5, 45, 560, 130))
        self.groupBox_4.setStyleSheet("background-color: rgba(157, 51, 214, 70);")
        self.groupBox_2.setGeometry(QRect(570, 295, 250, 290))
        self.groupBox_2.setStyleSheet("background-color: rgba(41, 200, 50, 80);")

        self.audible_post_button.setStyleSheet("background-color: rgb(118, 81, 8);")
        self.ff_post_button.setStyleSheet("background-color: rgb(7, 44, 108);")
        self.goodreads_post_button.setStyleSheet("background-color: rgb(75, 59, 39);")
        self.google_post_button.setStyleSheet("background-color: rgb(71, 24, 95);")

        self.tabWidget.addTab(self.main, "")
        self.tabWidget.addTab(self.tab, "")
        self.tabWidget.addTab(self.settings, "")

        self.audible_author.setGeometry(QRect(10, 228, 190, 20))
        self.audible_combobox.setGeometry(QRect(10, 285, 420, 22))
        self.audible_series.setGeometry(QRect(210, 228, 220, 20))
        self.audible_title.setGeometry(QRect(180, 198, 250, 20))
        self.audible_post_button.setGeometry(QRect(730, 340, 70, 25))
        self.audible_book_number.setGeometry(QRect(130, 198, 40, 20))
        self.audible_URL.setGeometry(QRect(10, 260, 420, 20))

        self.ff_post_button.setGeometry(QRect(590, 340, 120, 25))

        self.google_post_button.setGeometry(QRect(730, 380, 70, 25))

        self.save_settings_button.setGeometry(QRect(0, 210, 113, 25))
        self.search_button.setGeometry(QRect(650, 60, 71, 30))
        self.save_button.setGeometry(QRect(680, 420, 70, 30))
        self.open_folder_button.setGeometry(QRect(5, 15, 90, 25))
        self.search_button.setStyleSheet("background-color: rgb(120, 120, 120);")

        self.audible_search_toggle.setCheckable(True)
        self.audible_search_toggle.setChecked(True)

        self.audible_book_number.setAlignment(Qt.AlignCenter)

        self.audible_URL.setInputMethodHints(Qt.ImhNone)
        self.audible_fuzzy.setAlignment(Qt.AlignCenter)
        self.audible_fuzzy.setStyleSheet("background-color: green")

        self.ff_combobox.setGeometry(QRect(10, 555, 420, 22))

        self.ff_author.setGeometry(QRect(10, 498, 190, 20))

        self.ff_series.setGeometry(QRect(210, 498, 220, 20))
        self.ff_title.setGeometry(QRect(180, 468, 250, 20))
        self.ff_book_number.setGeometry(QRect(130, 468, 40, 20))
        self.ff_URL.setGeometry(QRect(10, 530, 420, 20))

        self.file_series.setGeometry(QRect(580, 221, 230, 20))
        self.file_author.setGeometry(QRect(580, 258, 230, 20))
        self.file_combobox.setGeometry(QRect(110, 16, 230, 22))
        self.file_title.setGeometry(QRect(580, 183, 230, 20))
        self.file_book_number.setGeometry(QRect(580, 143, 60, 20))

        self.final_series.setGeometry(QRect(580, 511, 230, 20))
        self.final_author.setGeometry(QRect(580, 546, 230, 20))
        self.final_title.setGeometry(QRect(580, 476, 230, 20))
        self.final_book_number.setGeometry(QRect(580, 439, 60, 20))

        self.FileLocation.setGeometry(QRect(10, 50, 529, 21))

        self.ff_book_number.setAlignment(Qt.AlignCenter)
        self.ff_URL.setInputMethodHints(Qt.ImhNone)
        self.ff_fuzzy.setAlignment(Qt.AlignCenter)
        # artwork
        self.finished_artwork.setGeometry(QRect(835, 295, 290, 290))
        self.original_artwork.setGeometry(QRect(835, 0, 290, 290))

        self.google_artwork.setGeometry(QRect(432, 45, 130, 130))
        self.ff_artwork.setGeometry(QRect(432, 450, 130, 130))
        self.audible_artwork.setGeometry(QRect(432, 180, 130, 130))
        self.goodreads_artwork.setGeometry(QRect(432, 315, 130, 130))

        self.FinishedLocation.setGeometry(QRect(10, 110, 529, 21))

        self.ff_search_toggle.setCheckable(True)
        self.ff_search_toggle.setChecked(False)
        self.goodreads_fuzzy.setAlignment(Qt.AlignCenter)
        self.goodreads_author.setGeometry(QRect(10, 363, 190, 20))
        self.goodreads_combobox.setGeometry(QRect(10, 420, 420, 22))
        self.goodreads_post_button.setGeometry(QRect(590, 380, 100, 25))

        self.goodreads_series.setGeometry(QRect(210, 363, 220, 20))
        self.goodreads_title.setGeometry(QRect(180, 333, 250, 20))
        self.goodreads_book_number.setGeometry(QRect(130, 333, 40, 20))
        self.goodreads_URL.setGeometry(QRect(10, 395, 420, 20))

        self.goodreads_search_toggle.setCheckable(True)
        self.goodreads_search_toggle.setChecked(False)

        self.google_author.setGeometry(QRect(10, 93, 190, 20))
        self.google_combobox.setGeometry(QRect(10, 150, 420, 22))

        self.google_fuzzy.setGeometry(QRect(535, 48, 24, 20))
        self.goodreads_fuzzy.setGeometry(QRect(535, 318, 24, 20))
        self.ff_fuzzy.setGeometry(QRect(535, 453, 24, 20))
        self.audible_fuzzy.setGeometry(QRect(535, 183, 24, 20))

        self.audible_search_toggle.setGeometry(QRect(8, 178, 70, 25))
        self.ff_search_toggle.setGeometry(QRect(8, 447, 115, 25))
        self.goodreads_search_toggle.setGeometry(QRect(8, 313, 100, 25))
        self.google_search_toggle.setGeometry(QRect(8, 42, 65, 25))

        self.google_search_toggle.setCheckable(True)
        self.google_search_toggle.setChecked(False)

        self.goodreads_book_number.setAlignment(Qt.AlignCenter)
        self.google_fuzzy.setAlignment(Qt.AlignCenter)
        self.google_book_number.setAlignment(Qt.AlignCenter)

        self.google_series.setGeometry(QRect(210, 93, 220, 20))
        self.google_title.setGeometry(QRect(180, 63, 250, 20))
        self.google_book_number.setGeometry(QRect(130, 63, 40, 20))
        self.label_10.setGeometry(QRect(580, 123, 71, 20))
        self.label_12.setGeometry(QRect(581, 421, 41, 20))
        self.label_14.setGeometry(QRect(20, 90, 529, 15))

        self.label_15.setGeometry(QRect(20, 150, 529, 15))
        self.label_14.setMaximumSize(QSize(16777215, 15))
        self.label_15.setMaximumSize(QSize(16777215, 15))
        self.label_16.setGeometry(QRect(581, 493, 41, 20))
        self.label_18.setGeometry(QRect(583, 529, 51, 20))
        self.label_2.setGeometry(QRect(580, 203, 41, 20))
        self.label_3.setGeometry(QRect(580, 240, 51, 20))
        self.label_4.setGeometry(QRect(580, 460, 61, 20))
        self.label_44.setGeometry(QRect(131, 48, 41, 20))
        self.label_45.setGeometry(QRect(13, 78, 51, 19))
        self.label_46.setGeometry(QRect(13, 213, 51, 19))
        self.label_47.setGeometry(QRect(131, 184, 41, 20))
        self.label_48.setGeometry(QRect(131, 318, 41, 20))
        self.label_49.setGeometry(QRect(13, 348, 51, 19))
        self.label_50.setGeometry(QRect(13, 483, 51, 19))
        self.label_51.setGeometry(QRect(131, 453, 41, 20))
        self.label_54.setGeometry(QRect(182, 48, 61, 20))
        self.label_55.setGeometry(QRect(182, 184, 61, 20))
        self.label_56.setGeometry(QRect(182, 318, 61, 20))
        self.label_58.setGeometry(QRect(13, 245, 21, 20))
        self.label_59.setGeometry(QRect(182, 454, 61, 20))
        self.label_60.setGeometry(QRect(211, 78, 40, 20))
        self.label_61.setGeometry(QRect(211, 213, 40, 20))
        self.label_62.setGeometry(QRect(211, 483, 40, 20))
        self.label_64.setGeometry(QRect(211, 348, 40, 20))
        self.label_65.setGeometry(QRect(13, 380, 21, 20))
        self.label_66.setGeometry(QRect(13, 515, 25, 20))
        self.label_9.setGeometry(QRect(20, 30, 529, 15))
        self.label_9.setMaximumSize(QSize(16777215, 15))
        self.label.setGeometry(QRect(582, 163, 61, 20))

        self.SaveFormatText.setGeometry(QRect(10, 170, 529, 21))

        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tabWidget.setGeometry(QRect(0, 0, 1140, 620))
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(False)

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.settings)
        self.plainTextEdit.setGeometry(QRect(120, 200, 671, 221))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)

        # added by Mike Treml
        self.button_configure()
        self.restore_settings()
        self.combobox_configure()
        Functions.delete_artwork()
        self.image_refresh()

    def retranslateUi(self, MainWindow):
        font = QFont()
        font.setPointSize(9)
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
        self.groupBox_2.setTitle(_translate("MainWindow", "Final"))
        self.groupBox.setTitle(_translate("MainWindow", "Original"))
        self.label_10.setFont(font)
        self.label.setFont(font)
        self.label_12.setFont(font)
        self.label_14.setFont(font)
        self.label_15.setFont(font)
        self.label_16.setFont(font)
        self.label_18.setFont(font)
        self.label_2.setFont(font)
        self.label_3.setFont(font)
        self.label_4.setFont(font)
        self.label_44.setFont(font)
        self.label_45.setFont(font)
        self.label_46.setFont(font)
        self.label_47.setFont(font)
        self.label_48.setFont(font)
        self.label_49.setFont(font)
        self.label_50.setFont(font)
        self.label_51.setFont(font)
        self.label_54.setFont(font)
        self.label_55.setFont(font)

        self.label_56.setFont(font)
        self.label_58.setFont(font)
        self.label_59.setFont(font)
        self.label_60.setFont(font)
        self.label_61.setFont(font)
        self.label_62.setFont(font)
        self.label_64.setFont(font)
        self.label_65.setFont(font)
        self.label_66.setFont(font)
        self.label_9.setFont(font)
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
        self.audible_author.setText(_translate("MainWindow", "Author"))
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
        self.save_button.setText(_translate("MainWindow", "SAVE"))
        self.save_settings_button.setText(_translate("MainWindow", "Save Settings"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main), _translate("MainWindow", "Main"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), _translate("MainWindow", "Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Detailed"))
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

        self.goodreads_book_number.setText("")
        self.goodreads_title.setText("")
        self.goodreads_author.setText("")
        self.goodreads_series.setText("")
        self.goodreads_URL.setText("")
        self.goodreads_fuzzy.setText("")

        self.final_book_number.setText("")
        self.audible_title.setText("")
        self.audible_author.setText("")
        self.audible_series.setText("")
        self.audible_URL.setText("")
        self.audible_fuzzy.setText("")
        self.audible_combobox.clear()
        self.ff_combobox.clear()
        self.google_combobox.clear()
        self.goodreads_combobox.clear()

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

    def combobox_configure(self):
        self.file_combobox.currentIndexChanged.connect(self.file_combobox_select)
        self.google_combobox.currentIndexChanged.connect(self.combobox_google_select)
        self.audible_combobox.currentIndexChanged.connect(self.combobox_audible_select)
        # self.goodreads_combobox.currentIndexChanged.connect(self.grComboBoxSelect)
        #  self.ff_combobox.currentIndexChanged.connect(self.ff_comboboxSelect)

    def audible_save(self):
        self.final_title.setText(self.audible_title.text())
        self.final_author.setText(self.audible_author.text())
        self.final_series.setText(self.audible_series.text())
        self.final_book_number.setText(self.audible_book_number.text())
        shutil.copy('assets/artwork/audible_artwork.jpg', 'assets/artwork/finished_artwork.jpg')
        self.image_refresh()

    def goodreads_save(self):
        self.final_title.setText(self.goodreads_title.text())
        self.final_author.setText(self.goodreads_author.text())
        self.final_series.setText(self.goodreads_series.text())
        self.final_book_number.setText(self.goodreads_book_number.text())

    def ff_save(self):
        self.final_title.setText(self.ff_title.text())
        self.final_author.setText(self.ff_author.text())
        self.final_series.setText(self.ff_series.text())
        self.final_book_number.setText(self.ff_book_number.text())

    def google_save(self):
        self.final_title.setText(self.google_title.text())
        self.final_author.setText(self.google_author.text())
        self.final_series.setText(self.google_series.text())
        self.final_book_number.setText(self.google_book_number.text())
        shutil.copy('assets/artwork/google_artwork.jpg', 'assets/artwork/finished_artwork.jpg')
        self.image_refresh()

    def image_refresh(self):
        self.google_artwork.setPixmap((QPixmap("assets/artwork/google_artwork.jpg")).scaled(self.google_artwork.size(),
                                                                                            Qt.KeepAspectRatio,
                                                                                            Qt.SmoothTransformation))
        self.ff_artwork.setPixmap((QPixmap("assets/artwork/ff_artwork.jpg")).scaled(self.ff_artwork.size(),
                                                                                    Qt.KeepAspectRatio,
                                                                                    Qt.SmoothTransformation))
        self.audible_artwork.setPixmap(
            (QPixmap("assets/artwork/audible_artwork.jpg")).scaled(self.audible_artwork.size(),
                                                                   Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.goodreads_artwork.setPixmap(
            (QPixmap("assets/artwork/goodreads_artwork.jpg")).scaled(self.goodreads_artwork.size(),
                                                                     Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.finished_artwork.setPixmap(
            (QPixmap("assets/artwork/finished_artwork.jpg")).scaled(self.finished_artwork.size(),
                                                                    Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.original_artwork.setPixmap(
            (QPixmap("assets/artwork/original_artwork.jpg")).scaled(self.original_artwork.size(),
                                                                    Qt.KeepAspectRatio, Qt.SmoothTransformation))

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

    def save(self):
        file_loacation = self.file_locations() + self.file_combobox.currentText()
        audiofile = eyed3.load(file_loacation)
        audiofile.tag.artist = self.file_author.text()
        audiofile.tag.album = self.final_series.text()
        audiofile.tag.title = self.file_title.text()
        audiofile.tag.composer = self.ABdict['A_narrator']
        audiofile.tag.release_date = self.ABdict['A_releaseDate']
        audiofile.tag.album_artist = self.ABdict['A_publisher']
        audiofile.tag.genre = self.ABdict['A_genre']
        audiofile.tag.comments.set(str(self.ABdict['A_rating']))

        # post twice for the same artwork. one for file view and one shows up in itunes
        imagedata = open('D:\AudibleApp\PICaudible.jpg', "rb").read()
        audiofile.tag.images.set(1, imagedata, 'image/jpeg', u"icon 2")
        audiofile.tag.save()

        audiofile1 = eyed3.load(self.fileComboBox.currentText())
        audiofile1.tag.images.set(3, imagedata, 'image/jpeg', u'front 3')
        audiofile1.tag.save()

        locat = self.FinishedLocation.text()

        dst = locat + '\\' + os.path.basename(self.fileComboBox.currentText())
        shutil.move(self.fileComboBox.currentText(), dst)
        extension = os.path.splitext(os.path.basename(self.fileComboBox.currentText()))[1]
        save_string_settings = self.save_format().text().replace("<series>", "{1}").replace("<book #>", "{2}").replace(
            "<title>", "{3}").replace("<author>", "{4}").replace("<folder>", "/")
        save_pattern = "{0/" + save_string_settings + "{5}"
        new_filename = save_pattern.format(locat, self.final_series.text(), self.final_book_number.text(),
                                           self.final_title.text(), self.audible_author.text(), extension).replace(':',
                                                                                                                   '').replace(
            '\\', '')
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

    def file_combobox_select(self):
        self.clear_fields()
        if self.file_combobox.currentText() != "":
            audio_file = eyed3.load(os.path.join(self.file_locations(), self.file_combobox.currentText()))
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
                image_file = open("assets/artwork/{0}.jpg".format("original_artwork"), "wb")
                image_file.write(image.image_data)
                image_file.close()
            self.image_refresh()

    def combobox_google_select(self):
        if self.google_combobox.currentIndex() >= 0:
            print(self.google_combobox.currentIndex())
            record = Functions.database_get(self.google_combobox.currentText(), "googlebooks")
            print(record)
            self.google_title.setText(record[1])
            self.google_author.setText(record[2])
            self.google_series.setText(record[4])
            try:
                req.urlretrieve(record[6], "assets/artwork/google_artwork.jpg")
            except:
                print("image issue")
            self.image_refresh()
            self.google_fuzzy.setText(str(self.fuzzyRateFeild(record[1] + " " + record[2] + " " + record[4])))

    def combobox_audible_select(self):
        if self.audible_combobox.currentIndex() >= 0:
            id = self.audible_combobox.currentText().split(" - ")[-1]
            print(id)
            record = Functions.database_get(id, "audible")
            print(record)
            self.audible_title.setText(record[1])
            self.audible_author.setText(record[2])
            self.audible_series.setText(record[4])
            print(record[8])
            try:
                ssl._create_default_https_context = ssl._create_unverified_context
                req.urlretrieve(record[8], "assets/artwork/audible_artwork.jpg")
            except:
                print("image issue")
            self.image_refresh()
            self.audible_fuzzy.setText(str(self.fuzzyRateFeild(record[1] + " " + record[2] + " " + record[4])))

    def file_combobox_update(self):
        self.file_combobox.clear()
        list_of_files = []
        for (dir_path, dir_names, filenames) in os.walk(self.file_locations()):
            for file in filenames:
                if "mp3" in file.lower():
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

    def run_searches(self):
        searchfields = (self.file_title.text() + " " + self.file_author.text() + " " + self.file_series.text()).lower()
        searchstring = searchfields.replace("book", "").replace("0", "").replace(" ", "+")
        if self.google_search_toggle.isChecked():
            book_list = Functions.google_search(searchstring)
            self.google_combobox_update(book_list)
        if self.audible_search_toggle.isChecked():
            book_list = Functions.audible_search(searchstring)
            print(searchstring)
            self.audible_combobox_update(book_list)

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
