import operator
import os
import os.path
import pathlib
import shutil
import sqlite3
import ssl
import urllib.request as req
from os import path

import eyed3
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QMetaObject, QCoreApplication, QSize
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget, QLineEdit, QLabel, QGroupBox, QComboBox, \
    QTabWidget, QCheckBox
from fuzzywuzzy import fuzz

import Functions
import ui_items

audible_artwork = 'assets/artwork/audible_artwork.jpg'
google_artwork = 'assets/artwork/google_artwork.jpg'
ff_artwork = 'assets/artwork/ff_artwork.jpg'
goodreads_artwork = 'assets/artwork/goodreads_artwork.jpg'
finished_artwork = 'assets/artwork/finished_artwork.jpg'
database = "audiobookspython.db"


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
        self.audible_author = QPushButton(self.main)

        self.audible_combobox = QComboBox(self.main)
        self.audible_fuzzy = QLineEdit(self.main)
        self.audible_post_button = QPushButton(self.main)
        self.audible_search_toggle = QCheckBox(self.main)
        self.audible_series = QPushButton(self.main)
        self.audible_title = QPushButton(self.main)
        self.audible_book_number = QPushButton(self.main)
        self.audible_URL = QLineEdit(self.main)
        self.ff_artwork = QLabel(self.main)
        self.ff_author = QPushButton(self.main)
        self.ff_combobox = QComboBox(self.main)
        self.ff_fuzzy = QLineEdit(self.main)
        self.ff_post_button = QPushButton(self.main)
        self.ff_search_toggle = QCheckBox(self.main)
        self.ff_series = QPushButton(self.main)
        self.ff_title = QPushButton(self.main)
        self.ff_book_number = QPushButton(self.main)
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
        self.goodreads_author = QPushButton(self.main)
        self.goodreads_combobox = QComboBox(self.main)
        self.goodreads_fuzzy = QLineEdit(self.main)
        self.goodreads_search_toggle = QCheckBox(self.main)
        self.goodreads_post_button = QPushButton(self.main)
        self.goodreads_series = QPushButton(self.main)
        self.goodreads_title = QPushButton(self.main)
        self.goodreads_book_number = QPushButton(self.main)
        self.goodreads_URL = QLineEdit(self.main)
        self.google_artwork = QLabel(self.main)
        self.google_author = QPushButton(self.main)
        self.google_artwork_button = QPushButton(self.main)
        self.audible_artwork_button = QPushButton(self.main)
        self.ff_artwork_button = QPushButton(self.main)
        self.goodreads_artwork_button = QPushButton(self.main)

        self.google_search_toggle = QCheckBox(self.main)
        self.google_combobox = QComboBox(self.main)
        self.google_fuzzy = QLineEdit(self.main)
        self.google_post_button = QPushButton(self.main)
        self.google_series = QPushButton(self.main)
        self.google_title = QPushButton(self.main)
        self.google_book_number = QPushButton(self.main)
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
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.settings)

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
        ui_items.set_ui_readonly(self)
        ui_items.set_ui_font(self)
        ui_items.set_ui_size(self)
        ui_items.set_ui_color(self)

        self.tabWidget.addTab(self.main, "")
        self.tabWidget.addTab(self.tab, "")
        self.tabWidget.addTab(self.settings, "")

        # self.audible_book_number.setAlignment(Qt.AlignCenter)
        self.audible_fuzzy.setAlignment(Qt.AlignCenter)
        self.audible_search_toggle.setCheckable(True)
        self.audible_search_toggle.setChecked(True)
        self.audible_URL.setInputMethodHints(Qt.ImhNone)
        # self.ff_book_number.setAlignment(Qt.AlignCenter)
        self.ff_fuzzy.setAlignment(Qt.AlignCenter)
        self.ff_search_toggle.setCheckable(True)
        self.ff_search_toggle.setChecked(False)
        self.ff_URL.setInputMethodHints(Qt.ImhNone)
        # self.goodreads_book_number.setAlignment(Qt.AlignCenter)
        self.goodreads_fuzzy.setAlignment(Qt.AlignCenter)
        self.goodreads_search_toggle.setCheckable(True)
        self.goodreads_search_toggle.setChecked(False)
        # self.google_book_number.setAlignment(Qt.AlignCenter)
        self.google_fuzzy.setAlignment(Qt.AlignCenter)
        self.google_search_toggle.setCheckable(True)
        self.google_search_toggle.setChecked(False)
        self.label_14.setMaximumSize(QSize(16777215, 15))
        self.label_15.setMaximumSize(QSize(16777215, 15))
        self.label_9.setMaximumSize(QSize(16777215, 15))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(False)

        # added by Mike Treml
        ui_items.set_ui_button(self)
        self.button_configure()
        self.restore_settings()
        self.combobox_configure()
        Functions.delete_artwork()
        Functions.image_refresh(self)

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
        file_loacation = self.file_locations() + self.file_combobox.currentText()
        file = self.file_combobox.currentText()
        audiofile = eyed3.load(file_loacation)
        audiofile.tag.artist = self.final_author.text()
        audiofile.tag.album = self.final_series.text()
        audiofile.tag.title = self.final_title.text()

        # posting twice for the same artwork. one for file view and one shows up in itunes
        try:
            imagedata = open(finished_artwork, "rb").read()
            audiofile.tag.images.set(1, imagedata, 'image/jpeg', u"icon 2")
            audiofile.tag.save()
            audiofile1 = eyed3.load(file_loacation)
            audiofile1.tag.images.set(3, imagedata, 'image/jpeg', u'front 3')
            audiofile1.tag.save()
        except:
            print("no new artwork")
        save_string_settings = str(self.save_format()).replace("<series>", "{1}").replace("<book #>", "{2}").replace(
            "<title>", "{3}").replace("<author>", "{4}").replace("<folder>", "/")
        save_pattern = "{0}" + save_string_settings + "{5}"
        locat = self.FinishedLocation.text()
        extension = os.path.splitext(os.path.basename(file))[1]
        folders = save_pattern.split("/")
        folders_pattern = save_pattern.replace(folders[-1], "")
        new_folders = folders_pattern.format(locat, self.final_series.text(), self.final_book_number.text(),
                                             self.final_title.text(), self.audible_author.text(), extension)
        if not os.path.exists(new_folders):
            os.makedirs(new_folders)

        dst = locat + os.path.basename(file)
        shutil.move(file_loacation, dst)

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
            Functions.image_refresh(self)

    def combobox_google_select(self):
        if self.google_combobox.currentIndex() >= 0:
            print(self.google_combobox.currentIndex())
            record = Functions.database_get(self.google_combobox.currentText(), "googlebooks")
            print(record)
            self.google_title.setText(record[1])
            self.google_author.setText(record[2])
            self.google_series.setText(record[4])

            try:
                req.urlretrieve(record[6], google_artwork)
            except:
                print("image issue")
            Functions.image_refresh(self)
            fuzzy = self.fuzzyRateFeild(record[1] + " " + record[2] + " " + record[4])
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
            print(id)
            record = Functions.database_get(id, "audible")
            print(record)
            self.audible_title.setText(record[1])
            self.audible_author.setText(record[2])
            self.audible_series.setText(record[4])
            self.audible_book_number.setText(record[5])
            self.audible_URL.setText(record[11])
            print(record[8])
            try:
                ssl._create_default_https_context = ssl._create_unverified_context
                req.urlretrieve(record[8], audible_artwork)
            except:
                print("image issue")
            Functions.image_refresh(self)
            fuzzy = self.fuzzyRateFeild(record[1] + " " + record[2] + " " + record[4])
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
            print(record)
            self.goodreads_title.setText(record[1])
            self.goodreads_author.setText(record[2])
            self.goodreads_series.setText(record[4])
            self.goodreads_URL.setText(record[11])
            self.goodreads_book_number.setText(record[5])
            print(record[8])
            try:
                ssl._create_default_https_context = ssl._create_unverified_context
                req.urlretrieve(record[8], goodreads_artwork)
            except:
                print("image issue")
            Functions.image_refresh(self)
            fuzzy = self.fuzzyRateFeild(record[1] + " " + record[2] + " " + record[4])
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
        if self.file_combobox.currentIndex() >= 0:
            search_fields = self.word_duplicate_remove(self.file_title.text() + " " + self.file_author.text() + " " +
                                                       self.file_series.text()).lower()
            search_string = search_fields.replace("book", "").replace("0", "").replace(" ", "+")
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
                try:
                    book_list = Functions.ff_search(search_string)
                    self.ff_combobox_update(book_list)
                except:
                    print("result error")

    def word_duplicate_remove(self, string):
        list_string = string.split(" ")
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


if __name__ == "__main__":
    import sys

    app = QApplication([])
    app.setStyle("Fusion")
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
