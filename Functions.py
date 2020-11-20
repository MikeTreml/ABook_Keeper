import os
import shutil
import pathlib
import eyed3 as eyed3

import main


def OpenFolderBtn(self):
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(main.Ui_MainWindow.file_locations()):
        listOfFiles = [os.path.join(dirpath, file) for file in filenames]
    for elem in listOfFiles:
        self.fileComboBox.addItem(elem)


def Save(self):
    offMin = int(self.SkipSpinBox.value()) - int(abs(self.lcdNumber.value()))
    if abs(offMin) <= int(self.SkipSpinBox.value()):
        audiofile = eyed3.load(self.fileComboBox.currentText())
        audiofile.tag.artist = self.audibleArtist_txt.text()
        audiofile.tag.album = self.audibleAlbum_txt.text()
        audiofile.tag.title = self.audibleTrack_txt.text()
        audiofile.tag.artist_url = self.aURLSearch_txt.text()
        audiofile.tag.commercial_url = self.ffURLSearch_txt.text()
        audiofile.tag.copyright_url = self.grURLSearch_txt.text()
        audiofile.tag.internet_radio_url = self.gaURLSearch_txt.text()
        if len(self.ABdict['GA_title']) > 0:
            audiofile.tag.album_artist = self.ABdict['GA_publisher']
            audiofile.tag.composer = self.ABdict['GA_narrator']
            audiofile.tag.comments.set(self.ABdict['GA_rating'])
        else:
            audiofile.tag.album_artist = self.ABdict['A_publisher']
            audiofile.tag.release_date = self.ABdict['A_releaseDate']
            audiofile.tag.composer = self.ABdict['A_narrator']
            print("rating ", self.ABdict['A_rating'])
            audiofile.tag.comments.set(str(self.ABdict['A_rating']))
            audiofile.tag.genre = self.ABdict['A_genre']

        imagedata = open('D:\AudibleApp\PICaudible.jpg', "rb").read()
        audiofile.tag.images.set(1, imagedata, 'image/jpeg', u"icon 2")
        audiofile.tag.save()

        audiofile1 = eyed3.load(self.fileComboBox.currentText())
        audiofile1.tag.images.set(3, imagedata, 'image/jpeg', u'front 3')
        audiofile1.tag.save()
        locat = "D:\AudibleApp\Done"
        dst = locat + '\\' + os.path.basename(self.fileComboBox.currentText())
        shutil.move(self.fileComboBox.currentText(), dst)
        extension = os.path.splitext(os.path.basename(self.fileComboBox.currentText()))[1]
        new_filename = "{4}\{0} - {1} {2}{3}".format(self.audibleAlbum_txt.text().replace(':', ''),
                                                     self.audibleTrackNo_txt.text().replace(':', ''),
                                                     self.audibleTrack_txt.text().replace('\\', ''), extension,
                                                     locat)
        print('dst', dst)
        print(new_filename)
        file = pathlib.Path(new_filename)
        if file.exists():
            print("File exist")
        else:
            os.rename(dst, new_filename)
    else:
        self.WebSave()
        locat = r"D:\AudibleApp\NeedsWork"
        dst = locat + "\\" + os.path.basename(self.fileComboBox.currentText())
        print(dst)
        shutil.move(self.fileComboBox.currentText(), dst)
        extension = os.path.splitext(os.path.basename(self.fileComboBox.currentText()))[1]
        # print(extension)
        new_filename = "{5}\{4} mins {0} - {1} {2}{3}".format(self.audibleAlbum_txt.text(),
                                                              self.audibleTrackNo_txt.text(),
                                                              self.audibleTrack_txt.text(), extension, abs(offMin),
                                                              locat)
        file = pathlib.Path(new_filename)
        if file.exists():
            print("File exist")
        else:
            os.rename(dst, new_filename)
    self.ClearFields()
    self.fileComboBox.removeItem(self.fileComboBox.currentIndex())
    print('files left ', self.fileComboBox.count())

def WebSave(self):
    audiofile = eyed3.load(self.fileComboBox.currentText())
    audiofile.tag.artist_url = self.aURLSearch_txt.text()
    audiofile.tag.commercial_url = self.ffURLSearch_txt.text()
    audiofile.tag.copyright_url = self.grURLSearch_txt.text()
    audiofile.tag.internet_radio_url = self.gaURLSearch_txt.text()
    audiofile.tag.save()

def dict_clear(self):
    self.google_books = {
        "title": "",
        "author": "",
        "narrator": "",
        "series": "",
        "book_number": "",
        "publisher": "",
        "genre": "",
        "image_url": "",
        "length": "",
        "release_date": "",
        "web_url": "",
        "tag": ""
    }
    self.goodreads = {
        "title": "",
        "author": "",
        "narrator": "",
        "series": "",
        "book_number": "",
        "publisher": "",
        "genre": "",
        "image_url": "",
        "length": "",
        "release_date": "",
        "web_url": "",
        "tag": ""
    }
    self.fantasticfiction = {
        "title": "",
        "author": "",
        "narrator": "",
        "series": "",
        "book_number": "",
        "publisher": "",
        "genre": "",
        "image_url": "",
        "length": "",
        "release_date": "",
        "web_url": "",
        "tag": ""
    }
    self.audible = {
        "title": "",
        "author": "",
        "narrator": "",
        "series": "",
        "book_number": "",
        "publisher": "",
        "genre": "",
        "image_url": "",
        "length": "",
        "release_date": "",
        "web_url": "",
        "tag": ""
    }
    self.amazon = {
        "title": "",
        "author": "",
        "narrator": "",
        "series": "",
        "book_number": "",
        "publisher": "",
        "genre": "",
        "image_url": "",
        "length": "",
        "release_date": "",
        "web_url": "",
        "tag": ""
    }