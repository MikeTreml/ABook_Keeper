from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(835, 602)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhDate)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-4, 1, 841, 611))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setObjectName("tabWidget")
        self.main = QtWidgets.QWidget()
        self.main.setObjectName("main")
        self.audibleTitleSearch_tst = QtWidgets.QLineEdit(self.main)
        self.audibleTitleSearch_tst.setGeometry(QtCore.QRect(150, 190, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.audibleTitleSearch_tst.setFont(font)
        self.audibleTitleSearch_tst.setObjectName("audibleTitleSearch_tst")
        self.audibleTrackNo = QtWidgets.QLineEdit(self.main)
        self.audibleTrackNo.setGeometry(QtCore.QRect(90, 190, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.audibleTrackNo.setFont(font)
        self.audibleTrackNo.setText("")
        self.audibleTrackNo.setAlignment(QtCore.Qt.AlignCenter)
        self.audibleTrackNo.setObjectName("audibleTrackNo")
        self.label_62 = QtWidgets.QLabel(self.main)
        self.label_62.setGeometry(QtCore.QRect(200, 472, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_62.setFont(font)
        self.label_62.setObjectName("label_62")
        self.label_49 = QtWidgets.QLabel(self.main)
        self.label_49.setGeometry(QtCore.QRect(12, 340, 51, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.label_45 = QtWidgets.QLabel(self.main)
        self.label_45.setGeometry(QtCore.QRect(12, 78, 51, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.ffSeriesSearch_txt = QtWidgets.QLineEdit(self.main)
        self.ffSeriesSearch_txt.setGeometry(QtCore.QRect(200, 487, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ffSeriesSearch_txt.setFont(font)
        self.ffSeriesSearch_txt.setText("")
        self.ffSeriesSearch_txt.setObjectName("ffSeriesSearch_txt")
        self.audibleSeriesSearch_txt = QtWidgets.QLineEdit(self.main)
        self.audibleSeriesSearch_txt.setGeometry(QtCore.QRect(207, 223, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.audibleSeriesSearch_txt.setFont(font)
        self.audibleSeriesSearch_txt.setObjectName("audibleSeriesSearch_txt")
        self.groupBox_5 = QtWidgets.QGroupBox(self.main)
        self.groupBox_5.setEnabled(False)
        self.groupBox_5.setGeometry(QtCore.QRect(5, 441, 561, 130))
        self.groupBox_5.setStyleSheet("background-color: rgba(10, 95, 255, 100);")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_50 = QtWidgets.QLabel(self.main)
        self.label_50.setGeometry(QtCore.QRect(12, 471, 51, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.label_47 = QtWidgets.QLabel(self.main)
        self.label_47.setGeometry(QtCore.QRect(93, 175, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.ffTitleSearch_txt = QtWidgets.QLineEdit(self.main)
        self.ffTitleSearch_txt.setGeometry(QtCore.QRect(180, 455, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ffTitleSearch_txt.setFont(font)
        self.ffTitleSearch_txt.setObjectName("ffTitleSearch_txt")
        self.audibleAuthorSearch_txt = QtWidgets.QLineEdit(self.main)
        self.audibleAuthorSearch_txt.setGeometry(QtCore.QRect(10, 222, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.audibleAuthorSearch_txt.setFont(font)
        self.audibleAuthorSearch_txt.setText("")
        self.audibleAuthorSearch_txt.setObjectName("audibleAuthorSearch_txt")
        self.label_58 = QtWidgets.QLabel(self.main)
        self.label_58.setGeometry(QtCore.QRect(12, 239, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_58.setFont(font)
        self.label_58.setObjectName("label_58")
        self.googleTitleSearch_tst = QtWidgets.QLineEdit(self.main)
        self.googleTitleSearch_tst.setGeometry(QtCore.QRect(138, 60, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.googleTitleSearch_tst.setFont(font)
        self.googleTitleSearch_tst.setObjectName("googleTitleSearch_tst")
        self.ffURLSearch_txt = QtWidgets.QLineEdit(self.main)
        self.ffURLSearch_txt.setGeometry(QtCore.QRect(10, 518, 411, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ffURLSearch_txt.setFont(font)
        self.ffURLSearch_txt.setInputMethodHints(QtCore.Qt.ImhNone)
        self.ffURLSearch_txt.setReadOnly(True)
        self.ffURLSearch_txt.setObjectName("ffURLSearch_txt")
        self.label_56 = QtWidgets.QLabel(self.main)
        self.label_56.setGeometry(QtCore.QRect(163, 307, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.googleAuthorSearch_txt = QtWidgets.QLineEdit(self.main)
        self.googleAuthorSearch_txt.setGeometry(QtCore.QRect(10, 92, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.googleAuthorSearch_txt.setFont(font)
        self.googleAuthorSearch_txt.setText("")
        self.googleAuthorSearch_txt.setObjectName("googleAuthorSearch_txt")
        self.label_60 = QtWidgets.QLabel(self.main)
        self.label_60.setGeometry(QtCore.QRect(201, 78, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_60.setFont(font)
        self.label_60.setObjectName("label_60")
        self.googleComboBox = QtWidgets.QComboBox(self.main)
        self.googleComboBox.setGeometry(QtCore.QRect(10, 146, 401, 30))
        self.googleComboBox.setObjectName("googleComboBox")
        self.label_46 = QtWidgets.QLabel(self.main)
        self.label_46.setGeometry(QtCore.QRect(12, 208, 51, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.label_65 = QtWidgets.QLabel(self.main)
        self.label_65.setGeometry(QtCore.QRect(12, 374, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_65.setFont(font)
        self.label_65.setObjectName("label_65")
        self.groupBox_3 = QtWidgets.QGroupBox(self.main)
        self.groupBox_3.setEnabled(False)
        self.groupBox_3.setGeometry(QtCore.QRect(5, 309, 561, 130))
        self.groupBox_3.setStyleSheet("background-color: rgba(144, 113, 76, 100);")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_59 = QtWidgets.QLabel(self.main)
        self.label_59.setGeometry(QtCore.QRect(181, 440, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_59.setFont(font)
        self.label_59.setObjectName("label_59")
        self.goodreadsTrackNo = QtWidgets.QLineEdit(self.main)
        self.goodreadsTrackNo.setGeometry(QtCore.QRect(100, 322, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.goodreadsTrackNo.setFont(font)
        self.goodreadsTrackNo.setText("")
        self.goodreadsTrackNo.setAlignment(QtCore.Qt.AlignCenter)
        self.goodreadsTrackNo.setObjectName("goodreadsTrackNo")
        self.label_48 = QtWidgets.QLabel(self.main)
        self.label_48.setGeometry(QtCore.QRect(102, 307, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_48.setFont(font)
        self.label_48.setObjectName("label_48")
        self.label_44 = QtWidgets.QLabel(self.main)
        self.label_44.setGeometry(QtCore.QRect(84, 45, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.ffTrackNo = QtWidgets.QLineEdit(self.main)
        self.ffTrackNo.setGeometry(QtCore.QRect(130, 455, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ffTrackNo.setFont(font)
        self.ffTrackNo.setText("")
        self.ffTrackNo.setAlignment(QtCore.Qt.AlignCenter)
        self.ffTrackNo.setObjectName("ffTrackNo")
        self.ffAuthorSearch_txt = QtWidgets.QLineEdit(self.main)
        self.ffAuthorSearch_txt.setGeometry(QtCore.QRect(10, 486, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ffAuthorSearch_txt.setFont(font)
        self.ffAuthorSearch_txt.setText("")
        self.ffAuthorSearch_txt.setObjectName("ffAuthorSearch_txt")
        self.fileComboBox = QtWidgets.QComboBox(self.main)
        self.fileComboBox.setGeometry(QtCore.QRect(90, 16, 471, 22))
        self.fileComboBox.setObjectName("fileComboBox")
        self.label_64 = QtWidgets.QLabel(self.main)
        self.label_64.setGeometry(QtCore.QRect(210, 341, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_64.setFont(font)
        self.label_64.setObjectName("label_64")
        self.goodreadsURLSearch_txt = QtWidgets.QLineEdit(self.main)
        self.goodreadsURLSearch_txt.setGeometry(QtCore.QRect(10, 389, 411, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.goodreadsURLSearch_txt.setFont(font)
        self.goodreadsURLSearch_txt.setInputMethodHints(QtCore.Qt.ImhNone)
        self.goodreadsURLSearch_txt.setReadOnly(True)
        self.goodreadsURLSearch_txt.setObjectName("goodreadsURLSearch_txt")
        self.audibleArtWork = QtWidgets.QLabel(self.main)
        self.audibleArtWork.setGeometry(QtCore.QRect(420, 177, 120, 120))
        self.audibleArtWork.setStyleSheet("")
        self.audibleArtWork.setText("")
        self.audibleArtWork.setPixmap(QtGui.QPixmap("D:\\../../../Volumes/D/D:/AudibleApp/SL500_.jpg"))
        self.audibleArtWork.setScaledContents(True)
        self.audibleArtWork.setOpenExternalLinks(False)
        self.audibleArtWork.setObjectName("audibleArtWork")
        self.audibleURLSearch_txt = QtWidgets.QLineEdit(self.main)
        self.audibleURLSearch_txt.setGeometry(QtCore.QRect(10, 254, 411, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.audibleURLSearch_txt.setFont(font)
        self.audibleURLSearch_txt.setInputMethodHints(QtCore.Qt.ImhNone)
        self.audibleURLSearch_txt.setReadOnly(True)
        self.audibleURLSearch_txt.setObjectName("audibleURLSearch_txt")
        self.audibleComboBox = QtWidgets.QComboBox(self.main)
        self.audibleComboBox.setGeometry(QtCore.QRect(6, 281, 401, 22))
        self.audibleComboBox.setObjectName("audibleComboBox")
        self.ffArtWork = QtWidgets.QLabel(self.main)
        self.ffArtWork.setGeometry(QtCore.QRect(420, 441, 120, 120))
        self.ffArtWork.setStyleSheet("")
        self.ffArtWork.setText("")
        self.ffArtWork.setPixmap(QtGui.QPixmap("D:\\../../../Volumes/D/D:/AudibleApp/SL500_.jpg"))
        self.ffArtWork.setScaledContents(True)
        self.ffArtWork.setOpenExternalLinks(False)
        self.ffArtWork.setObjectName("ffArtWork")
        self.goodreadsAuthorSearch_txt = QtWidgets.QLineEdit(self.main)
        self.goodreadsAuthorSearch_txt.setGeometry(QtCore.QRect(10, 354, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.goodreadsAuthorSearch_txt.setFont(font)
        self.goodreadsAuthorSearch_txt.setText("")
        self.goodreadsAuthorSearch_txt.setObjectName("goodreadsAuthorSearch_txt")
        self.groupBox_6 = QtWidgets.QGroupBox(self.main)
        self.groupBox_6.setEnabled(False)
        self.groupBox_6.setGeometry(QtCore.QRect(5, 177, 561, 130))
        self.groupBox_6.setStyleSheet("background-color: rgba(254, 172, 12, 100);")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.groupBox_4 = QtWidgets.QGroupBox(self.main)
        self.groupBox_4.setEnabled(True)
        self.groupBox_4.setGeometry(QtCore.QRect(5, 45, 561, 130))
        self.groupBox_4.setStyleSheet("background-color: rgba(157, 51, 214, 70);")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.goodreadsSeriesSearch_txt = QtWidgets.QLineEdit(self.main)
        self.goodreadsSeriesSearch_txt.setGeometry(QtCore.QRect(210, 356, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.goodreadsSeriesSearch_txt.setFont(font)
        self.goodreadsSeriesSearch_txt.setObjectName("goodreadsSeriesSearch_txt")
        self.googleTrackNo_txt = QtWidgets.QLineEdit(self.main)
        self.googleTrackNo_txt.setGeometry(QtCore.QRect(81, 60, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.googleTrackNo_txt.setFont(font)
        self.googleTrackNo_txt.setText("")
        self.googleTrackNo_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.googleTrackNo_txt.setObjectName("googleTrackNo_txt")
        self.goodreadsComboBox = QtWidgets.QComboBox(self.main)
        self.goodreadsComboBox.setGeometry(QtCore.QRect(6, 413, 401, 22))
        self.goodreadsComboBox.setObjectName("goodreadsComboBox")
        self.goodreadsArtWork = QtWidgets.QLabel(self.main)
        self.goodreadsArtWork.setGeometry(QtCore.QRect(420, 309, 120, 120))
        self.goodreadsArtWork.setStyleSheet("")
        self.goodreadsArtWork.setText("")
        self.goodreadsArtWork.setPixmap(QtGui.QPixmap("D:\\../../../Volumes/D/D:/AudibleApp/SL500_.jpg"))
        self.goodreadsArtWork.setScaledContents(True)
        self.goodreadsArtWork.setOpenExternalLinks(False)
        self.goodreadsArtWork.setObjectName("goodreadsArtWork")
        self.goodreadsTitleSearch_tst = QtWidgets.QLineEdit(self.main)
        self.goodreadsTitleSearch_tst.setGeometry(QtCore.QRect(160, 322, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.goodreadsTitleSearch_tst.setFont(font)
        self.goodreadsTitleSearch_tst.setObjectName("goodreadsTitleSearch_tst")
        self.label_61 = QtWidgets.QLabel(self.main)
        self.label_61.setGeometry(QtCore.QRect(210, 208, 30, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_61.setFont(font)
        self.label_61.setObjectName("label_61")
        self.ffComboBox = QtWidgets.QComboBox(self.main)
        self.ffComboBox.setGeometry(QtCore.QRect(6, 543, 400, 22))
        self.ffComboBox.setObjectName("ffComboBox")
        self.label_55 = QtWidgets.QLabel(self.main)
        self.label_55.setGeometry(QtCore.QRect(152, 175, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.googleSeriesSearch_txt = QtWidgets.QLineEdit(self.main)
        self.googleSeriesSearch_txt.setGeometry(QtCore.QRect(199, 93, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.googleSeriesSearch_txt.setFont(font)
        self.googleSeriesSearch_txt.setObjectName("googleSeriesSearch_txt")
        self.googleArtWork = QtWidgets.QLabel(self.main)
        self.googleArtWork.setGeometry(QtCore.QRect(420, 54, 120, 120))
        self.googleArtWork.setStyleSheet("")
        self.googleArtWork.setText("")
        self.googleArtWork.setPixmap(QtGui.QPixmap("D:\\../../../Volumes/D/D:/AudibleApp/SL500_.jpg"))
        self.googleArtWork.setScaledContents(True)
        self.googleArtWork.setOpenExternalLinks(False)
        self.googleArtWork.setObjectName("googleArtWork")
        self.label_51 = QtWidgets.QLabel(self.main)
        self.label_51.setGeometry(QtCore.QRect(130, 440, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_51.setFont(font)
        self.label_51.setObjectName("label_51")
        self.pushButton = QtWidgets.QPushButton(self.main)
        self.pushButton.setGeometry(QtCore.QRect(10, 16, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.googleButton = QtWidgets.QPushButton(self.main)
        self.googleButton.setGeometry(QtCore.QRect(5, 44, 71, 23))
        self.googleButton.setStyleSheet("@QPushButton:checked {\n"
"background-color: blue;\n"
"border: none;\n"
"}")
        self.googleButton.setCheckable(True)
        self.googleButton.setChecked(False)
        self.googleButton.setObjectName("googleButton")
        self.goodreadsGoogleButton = QtWidgets.QPushButton(self.main)
        self.goodreadsGoogleButton.setGeometry(QtCore.QRect(5, 310, 91, 23))
        self.goodreadsGoogleButton.setStyleSheet("@QPushButton:checked {\n"
"background-color: blue;\n"
"border: none;\n"
"}")
        self.goodreadsGoogleButton.setCheckable(True)
        self.goodreadsGoogleButton.setChecked(False)
        self.goodreadsGoogleButton.setObjectName("goodreadsGoogleButton")
        self.ffSearchButton = QtWidgets.QPushButton(self.main)
        self.ffSearchButton.setGeometry(QtCore.QRect(5, 441, 121, 23))
        self.ffSearchButton.setStyleSheet("@QPushButton:checked {\n"
"background-color: blue;\n"
"border: none;\n"
"}")
        self.ffSearchButton.setCheckable(True)
        self.ffSearchButton.setChecked(False)
        self.ffSearchButton.setObjectName("ffSearchButton")
        self.audibleSearchButton = QtWidgets.QPushButton(self.main)
        self.audibleSearchButton.setEnabled(True)
        self.audibleSearchButton.setGeometry(QtCore.QRect(5, 177, 80, 30))
        self.audibleSearchButton.setStyleSheet("@QPushButton:checked {\n"
"background-color: blue;\n"
"border: none;\n"
"}")
        self.audibleSearchButton.setCheckable(True)
        self.audibleSearchButton.setChecked(False)
        self.audibleSearchButton.setObjectName("audibleSearchButton")
        self.audibleFuzzyAV = QtWidgets.QLineEdit(self.main)
        self.audibleFuzzyAV.setGeometry(QtCore.QRect(540, 183, 24, 20))
        self.audibleFuzzyAV.setAlignment(QtCore.Qt.AlignCenter)
        self.audibleFuzzyAV.setObjectName("audibleFuzzyAV")
        self.googleFuzzyAV = QtWidgets.QLineEdit(self.main)
        self.googleFuzzyAV.setGeometry(QtCore.QRect(540, 52, 24, 20))
        self.googleFuzzyAV.setAlignment(QtCore.Qt.AlignCenter)
        self.googleFuzzyAV.setObjectName("googleFuzzyAV")
        self.goodreadsFuzzyAV = QtWidgets.QLineEdit(self.main)
        self.goodreadsFuzzyAV.setEnabled(True)
        self.goodreadsFuzzyAV.setGeometry(QtCore.QRect(540, 315, 24, 20))
        self.goodreadsFuzzyAV.setAlignment(QtCore.Qt.AlignCenter)
        self.goodreadsFuzzyAV.setObjectName("goodreadsFuzzyAV")
        self.ffFuzzyAV = QtWidgets.QLineEdit(self.main)
        self.ffFuzzyAV.setGeometry(QtCore.QRect(540, 445, 24, 20))
        self.ffFuzzyAV.setAlignment(QtCore.Qt.AlignCenter)
        self.ffFuzzyAV.setObjectName("ffFuzzyAV")
        self.label_54 = QtWidgets.QLabel(self.main)
        self.label_54.setGeometry(QtCore.QRect(140, 45, 61, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(25, 64, 255, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 64, 255, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 64, 255, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 64, 255, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 64, 255, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 64, 255, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 64, 255, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 64, 255, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 64, 255, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_54.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_54.setFont(font)
        self.label_54.setStyleSheet("")
        self.label_54.setObjectName("label_54")
        self.label_66 = QtWidgets.QLabel(self.main)
        self.label_66.setGeometry(QtCore.QRect(12, 503, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_66.setFont(font)
        self.label_66.setObjectName("label_66")
        self.audibleArtist_txt = QtWidgets.QLineEdit(self.main)
        self.audibleArtist_txt.setGeometry(QtCore.QRect(581, 546, 241, 20))
        self.audibleArtist_txt.setText("")
        self.audibleArtist_txt.setObjectName("audibleArtist_txt")
        self.label_16 = QtWidgets.QLabel(self.main)
        self.label_16.setGeometry(QtCore.QRect(581, 493, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.audibleTrack_txt = QtWidgets.QLineEdit(self.main)
        self.audibleTrack_txt.setGeometry(QtCore.QRect(578, 476, 241, 20))
        self.audibleTrack_txt.setObjectName("audibleTrack_txt")
        self.audibleTrackNo_txt = QtWidgets.QLineEdit(self.main)
        self.audibleTrackNo_txt.setGeometry(QtCore.QRect(579, 439, 61, 20))
        self.audibleTrackNo_txt.setObjectName("audibleTrackNo_txt")
        self.groupBox_2 = QtWidgets.QGroupBox(self.main)
        self.groupBox_2.setEnabled(False)
        self.groupBox_2.setGeometry(QtCore.QRect(575, 331, 257, 241))
        self.groupBox_2.setStyleSheet("background-color: rgba(41, 200, 50, 80);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_18 = QtWidgets.QLabel(self.main)
        self.label_18.setGeometry(QtCore.QRect(583, 529, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_12 = QtWidgets.QLabel(self.main)
        self.label_12.setGeometry(QtCore.QRect(581, 421, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_4 = QtWidgets.QLabel(self.main)
        self.label_4.setGeometry(QtCore.QRect(580, 460, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.audibleAlbum_txt = QtWidgets.QLineEdit(self.main)
        self.audibleAlbum_txt.setGeometry(QtCore.QRect(581, 511, 241, 20))
        self.audibleAlbum_txt.setObjectName("audibleAlbum_txt")
        self.label_3 = QtWidgets.QLabel(self.main)
        self.label_3.setGeometry(QtCore.QRect(580, 240, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.fileArtist_txt = QtWidgets.QLineEdit(self.main)
        self.fileArtist_txt.setGeometry(QtCore.QRect(580, 258, 241, 20))
        self.fileArtist_txt.setObjectName("fileArtist_txt")
        self.fileAlbum_txt = QtWidgets.QLineEdit(self.main)
        self.fileAlbum_txt.setGeometry(QtCore.QRect(580, 221, 241, 20))
        self.fileAlbum_txt.setObjectName("fileAlbum_txt")
        self.label_2 = QtWidgets.QLabel(self.main)
        self.label_2.setGeometry(QtCore.QRect(580, 203, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.fileTrackNo_txt = QtWidgets.QLineEdit(self.main)
        self.fileTrackNo_txt.setGeometry(QtCore.QRect(580, 143, 61, 20))
        self.fileTrackNo_txt.setObjectName("fileTrackNo_txt")
        self.groupBox = QtWidgets.QGroupBox(self.main)
        self.groupBox.setEnabled(False)
        self.groupBox.setGeometry(QtCore.QRect(575, 30, 257, 251))
        self.groupBox.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
        self.groupBox.setObjectName("groupBox")
        self.fileTrack_txt = QtWidgets.QLineEdit(self.main)
        self.fileTrack_txt.setGeometry(QtCore.QRect(580, 183, 241, 20))
        self.fileTrack_txt.setText("")
        self.fileTrack_txt.setObjectName("fileTrack_txt")
        self.label = QtWidgets.QLabel(self.main)
        self.label.setGeometry(QtCore.QRect(582, 163, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_10 = QtWidgets.QLabel(self.main)
        self.label_10.setGeometry(QtCore.QRect(580, 123, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.SearchButton = QtWidgets.QPushButton(self.main)
        self.SearchButton.setGeometry(QtCore.QRect(573, 3, 71, 27))
        self.SearchButton.setObjectName("SearchButton")
        self.saveButton_2 = QtWidgets.QPushButton(self.main)
        self.saveButton_2.setGeometry(QtCore.QRect(760, 290, 71, 31))
        self.saveButton_2.setObjectName("saveButton_2")
        self.googlePickButton = QtWidgets.QPushButton(self.main)
        self.googlePickButton.setGeometry(QtCore.QRect(690, 303, 71, 23))
        self.googlePickButton.setStyleSheet("color: rgb(157, 51, 214);")
        self.googlePickButton.setObjectName("googlePickButton")
        self.goodreadsPullButton = QtWidgets.QPushButton(self.main)
        self.goodreadsPullButton.setGeometry(QtCore.QRect(573, 303, 101, 23))
        self.goodreadsPullButton.setStyleSheet("color: rgb(110, 59, 0);")
        self.goodreadsPullButton.setObjectName("goodreadsPullButton")
        self.ffPullButton = QtWidgets.QPushButton(self.main)
        self.ffPullButton.setGeometry(QtCore.QRect(573, 283, 121, 23))
        self.ffPullButton.setStyleSheet("color: rgb(8, 79, 209);")
        self.ffPullButton.setObjectName("ffPullButton")
        self.audiblePullButton = QtWidgets.QPushButton(self.main)
        self.audiblePullButton.setGeometry(QtCore.QRect(690, 283, 71, 23))
        self.audiblePullButton.setStyleSheet("color: rgb(251, 139, 43);")
        self.audiblePullButton.setObjectName("audiblePullButton")
        self.originalArtWork = QtWidgets.QLabel(self.main)
        self.originalArtWork.setGeometry(QtCore.QRect(643, 33, 191, 151))
        self.originalArtWork.setStyleSheet("border-color: rgb(135, 135, 135);")
        self.originalArtWork.setText("")
        self.originalArtWork.setPixmap(QtGui.QPixmap("D:\\../../../Volumes/D/D:/AudibleApp/SL500_.jpg"))
        self.originalArtWork.setScaledContents(True)
        self.originalArtWork.setOpenExternalLinks(False)
        self.originalArtWork.setObjectName("originalArtWork")
        self.groupBox_4.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.groupBox_6.raise_()
        self.groupBox_3.raise_()
        self.groupBox_5.raise_()
        self.audibleTitleSearch_tst.raise_()
        self.audibleTrackNo.raise_()
        self.label_62.raise_()
        self.label_49.raise_()
        self.label_45.raise_()
        self.ffSeriesSearch_txt.raise_()
        self.audibleSeriesSearch_txt.raise_()
        self.label_50.raise_()
        self.label_47.raise_()
        self.ffTitleSearch_txt.raise_()
        self.audibleAuthorSearch_txt.raise_()
        self.label_58.raise_()
        self.googleTitleSearch_tst.raise_()
        self.ffURLSearch_txt.raise_()
        self.label_56.raise_()
        self.googleAuthorSearch_txt.raise_()
        self.label_60.raise_()
        self.googleComboBox.raise_()
        self.label_46.raise_()
        self.label_65.raise_()
        self.label_59.raise_()
        self.goodreadsTrackNo.raise_()
        self.label_48.raise_()
        self.label_44.raise_()
        self.ffTrackNo.raise_()
        self.ffAuthorSearch_txt.raise_()
        self.fileComboBox.raise_()
        self.label_64.raise_()
        self.goodreadsURLSearch_txt.raise_()
        self.audibleURLSearch_txt.raise_()
        self.audibleComboBox.raise_()
        self.ffArtWork.raise_()
        self.goodreadsAuthorSearch_txt.raise_()
        self.goodreadsSeriesSearch_txt.raise_()
        self.googleTrackNo_txt.raise_()
        self.goodreadsComboBox.raise_()
        self.goodreadsArtWork.raise_()
        self.goodreadsTitleSearch_tst.raise_()
        self.label_61.raise_()
        self.ffComboBox.raise_()
        self.label_55.raise_()
        self.googleSeriesSearch_txt.raise_()
        self.googleArtWork.raise_()
        self.label_51.raise_()
        self.pushButton.raise_()
        self.googleButton.raise_()
        self.goodreadsGoogleButton.raise_()
        self.ffSearchButton.raise_()
        self.audibleArtWork.raise_()
        self.audibleSearchButton.raise_()
        self.audibleFuzzyAV.raise_()
        self.googleFuzzyAV.raise_()
        self.goodreadsFuzzyAV.raise_()
        self.ffFuzzyAV.raise_()
        self.label_54.raise_()
        self.label_66.raise_()
        self.audibleArtist_txt.raise_()
        self.label_16.raise_()
        self.audibleTrack_txt.raise_()
        self.audibleTrackNo_txt.raise_()
        self.label_18.raise_()
        self.label_12.raise_()
        self.label_4.raise_()
        self.audibleAlbum_txt.raise_()
        self.label_3.raise_()
        self.fileArtist_txt.raise_()
        self.fileAlbum_txt.raise_()
        self.label_2.raise_()
        self.fileTrackNo_txt.raise_()
        self.fileTrack_txt.raise_()
        self.label.raise_()
        self.label_10.raise_()
        self.SearchButton.raise_()
        self.saveButton_2.raise_()
        self.googlePickButton.raise_()
        self.goodreadsPullButton.raise_()
        self.ffPullButton.raise_()
        self.audiblePullButton.raise_()
        self.originalArtWork.raise_()
        self.tabWidget.addTab(self.main, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.SaveFormatText = QtWidgets.QLineEdit(self.settings)
        self.SaveFormatText.setGeometry(QtCore.QRect(10, 170, 529, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.SaveFormatText.setFont(font)
        self.SaveFormatText.setObjectName("SaveFormatText")
        self.label_15 = QtWidgets.QLabel(self.settings)
        self.label_15.setGeometry(QtCore.QRect(20, 150, 529, 15))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_15.setObjectName("label_15")
        self.FileLocation = QtWidgets.QLineEdit(self.settings)
        self.FileLocation.setGeometry(QtCore.QRect(10, 50, 529, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.FileLocation.setFont(font)
        self.FileLocation.setObjectName("FileLocation")
        self.label_9 = QtWidgets.QLabel(self.settings)
        self.label_9.setGeometry(QtCore.QRect(20, 30, 529, 15))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_9.setObjectName("label_9")
        self.label_14 = QtWidgets.QLabel(self.settings)
        self.label_14.setGeometry(QtCore.QRect(20, 90, 529, 15))
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_14.setObjectName("label_14")
        self.FinishedLocation = QtWidgets.QLineEdit(self.settings)
        self.FinishedLocation.setGeometry(QtCore.QRect(10, 110, 529, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.FinishedLocation.setFont(font)
        self.FinishedLocation.setObjectName("FinishedLocation")
        self.saveSettingsButton = QtWidgets.QPushButton(self.settings)
        self.saveSettingsButton.setGeometry(QtCore.QRect(0, 210, 113, 32))
        self.saveSettingsButton.setObjectName("saveSettingsButton")
        self.WebSitecomboBox = QtWidgets.QComboBox(self.settings)
        self.WebSitecomboBox.setGeometry(QtCore.QRect(10, 250, 461, 22))
        self.WebSitecomboBox.setObjectName("WebSitecomboBox")
        self.tabWidget.addTab(self.settings, "")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(1060, -90, 81, 27))
        self.saveButton.setObjectName("saveButton")
        self.finishedArtWork = QtWidgets.QLabel(self.centralwidget)
        self.finishedArtWork.setGeometry(QtCore.QRect(642, 363, 191, 141))
        self.finishedArtWork.setStyleSheet("border-color: rgb(135, 135, 100);")
        self.finishedArtWork.setText("")
        self.finishedArtWork.setPixmap(QtGui.QPixmap("D:\\../../../Volumes/D/D:/AudibleApp/SL500_.jpg"))
        self.finishedArtWork.setScaledContents(True)
        self.finishedArtWork.setOpenExternalLinks(False)
        self.finishedArtWork.setObjectName("finishedArtWork")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_62.setText(_translate("MainWindow", "Series"))
        self.label_49.setText(_translate("MainWindow", "Author"))
        self.label_45.setText(_translate("MainWindow", "Author"))
        self.label_50.setText(_translate("MainWindow", "Author"))
        self.label_47.setText(_translate("MainWindow", "Book #"))
        self.label_58.setText(_translate("MainWindow", "URL"))
        self.label_56.setText(_translate("MainWindow", "Title"))
        self.label_60.setText(_translate("MainWindow", "Series"))
        self.label_46.setText(_translate("MainWindow", "Author"))
        self.label_65.setText(_translate("MainWindow", "URL"))
        self.label_59.setText(_translate("MainWindow", "Title"))
        self.label_48.setText(_translate("MainWindow", "Book #"))
        self.label_44.setText(_translate("MainWindow", "Book #"))
        self.label_64.setText(_translate("MainWindow", "Series"))
        self.label_61.setText(_translate("MainWindow", "Series"))
        self.label_55.setText(_translate("MainWindow", "Title"))
        self.label_51.setText(_translate("MainWindow", "Book #"))
        self.pushButton.setText(_translate("MainWindow", "Open Folder"))
        self.googleButton.setText(_translate("MainWindow", "Google"))
        self.goodreadsGoogleButton.setText(_translate("MainWindow", "Goodreads"))
        self.ffSearchButton.setText(_translate("MainWindow", "FantasticFiction"))
        self.audibleSearchButton.setText(_translate("MainWindow", "Audible"))
        self.label_54.setText(_translate("MainWindow", "Title"))
        self.label_66.setText(_translate("MainWindow", "URL"))
        self.label_16.setText(_translate("MainWindow", "Series"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Final"))
        self.label_18.setText(_translate("MainWindow", "Author"))
        self.label_12.setText(_translate("MainWindow", "Book #"))
        self.label_4.setText(_translate("MainWindow", "Title"))
        self.label_3.setText(_translate("MainWindow", "Author"))
        self.label_2.setText(_translate("MainWindow", "Series"))
        self.fileTrackNo_txt.setText(_translate("MainWindow", "001"))
        self.groupBox.setTitle(_translate("MainWindow", "Original"))
        self.label.setText(_translate("MainWindow", "Title"))
        self.label_10.setText(_translate("MainWindow", "Book #"))
        self.SearchButton.setText(_translate("MainWindow", "Search"))
        self.saveButton_2.setText(_translate("MainWindow", "SAVE"))
        self.googlePickButton.setText(_translate("MainWindow", "Google"))
        self.goodreadsPullButton.setText(_translate("MainWindow", "GoodReads"))
        self.ffPullButton.setText(_translate("MainWindow", "FantasticFiction"))
        self.audiblePullButton.setText(_translate("MainWindow", "Audible"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main), _translate("MainWindow", "Main"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Detailed"))
        self.label_15.setText(_translate("MainWindow", "Save format"))
        self.label_9.setText(_translate("MainWindow", "Audiobooks location"))
        self.label_14.setText(_translate("MainWindow", "Finished Location"))
        self.saveSettingsButton.setText(_translate("MainWindow", "Save Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), _translate("MainWindow", "Settings"))
        self.saveButton.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
