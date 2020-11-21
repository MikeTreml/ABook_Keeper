import os
import shutil
import pathlib
import eyed3 as eyed3

import main



def try_check(book,string1):
    result =""
    try:
        result = book[string1]
    except:
        result= ""
    return result
def try_check2(book,string1,string2):
    result =""
    try:
        result = book[string1][string2]
    except:
        result= ""
    return result
def try_check3(book,string1,string2,string3):
    result =""
    try:
        result = book[string1][string2][string3]
    except:
        result= ""
    return result

























def OpenFolderBtn(self):
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(main.Ui_MainWindow.file_locations()):
        listOfFiles = [os.path.join(dirpath, file) for file in filenames]
    for elem in listOfFiles:
        main.self.fileComboBox.addItem(elem)

def Save(self):
    offMin = int(main.self.SkipSpinBox.value()) - int(abs(main.self.lcdNumber.value()))
    if abs(offMin) <= int(main.self.SkipSpinBox.value()):
        audiofile = eyed3.load(main.self.fileComboBox.currentText())
        audiofile.tag.artist = main.self.audibleArtist_txt.text()
        audiofile.tag.album = main.self.audibleAlbum_txt.text()
        audiofile.tag.title = main.self.audibleTrack_txt.text()
        audiofile.tag.artist_url = main.self.aURLSearch_txt.text()
        audiofile.tag.commercial_url = main.self.ffURLSearch_txt.text()
        audiofile.tag.copyright_url = main.self.grURLSearch_txt.text()
        audiofile.tag.internet_radio_url = main.self.gaURLSearch_txt.text()
        if len(main.self.ABdict['GA_title']) > 0:
            audiofile.tag.album_artist = main.self.ABdict['GA_publisher']
            audiofile.tag.composer = main.self.ABdict['GA_narrator']
            audiofile.tag.comments.set(main.self.ABdict['GA_rating'])
        else:
            audiofile.tag.album_artist = main.self.ABdict['A_publisher']
            audiofile.tag.release_date = main.self.ABdict['A_releaseDate']
            audiofile.tag.composer = main.self.ABdict['A_narrator']
            print("rating ", main.self.ABdict['A_rating'])
            audiofile.tag.comments.set(str(main.self.ABdict['A_rating']))
            audiofile.tag.genre = main.self.ABdict['A_genre']

        imagedata = open('D:\AudibleApp\PICaudible.jpg', "rb").read()
        audiofile.tag.images.set(1, imagedata, 'image/jpeg', u"icon 2")
        audiofile.tag.save()

        audiofile1 = eyed3.load(main.self.fileComboBox.currentText())
        audiofile1.tag.images.set(3, imagedata, 'image/jpeg', u'front 3')
        audiofile1.tag.save()
        locat = "D:\AudibleApp\Done"
        dst = locat + '\\' + os.path.basename(main.self.fileComboBox.currentText())
        shutil.move(main.self.fileComboBox.currentText(), dst)
        extension = os.path.splitext(os.path.basename(main.self.fileComboBox.currentText()))[1]
        new_filename = "{4}\{0} - {1} {2}{3}".format(main.self.audibleAlbum_txt.text().replace(':', ''),
                                                     main.self.audibleTrackNo_txt.text().replace(':', ''),
                                                     main.self.audibleTrack_txt.text().replace('\\', ''), extension,
                                                     locat)
        print('dst', dst)
        print(new_filename)
        file = pathlib.Path(new_filename)
        if file.exists():
            print("File exist")
        else:
            os.rename(dst, new_filename)
    else:
        main.self.WebSave()
        locat = r"D:\AudibleApp\NeedsWork"
        dst = locat + "\\" + os.path.basename(main.self.fileComboBox.currentText())
        print(dst)
        shutil.move(main.self.fileComboBox.currentText(), dst)
        extension = os.path.splitext(os.path.basename(main.self.fileComboBox.currentText()))[1]
        # print(extension)
        new_filename = "{5}\{4} mins {0} - {1} {2}{3}".format(main.self.audibleAlbum_txt.text(),
                                                              main.self.audibleTrackNo_txt.text(),
                                                              main.self.audibleTrack_txt.text(), extension, abs(offMin),
                                                              locat)
        file = pathlib.Path(new_filename)
        if file.exists():
            print("File exist")
        else:
            os.rename(dst, new_filename)
    main.self.ClearFields()
    main.self.fileComboBox.removeItem(main.self.fileComboBox.currentIndex())
    print('files left ', main.self.fileComboBox.count())

def WebSave(self):
    audiofile = eyed3.load(main.self.fileComboBox.currentText())
    audiofile.tag.artist_url = main.self.aURLSearch_txt.text()
    audiofile.tag.commercial_url = main.self.ffURLSearch_txt.text()
    audiofile.tag.copyright_url = main.self.grURLSearch_txt.text()
    audiofile.tag.internet_radio_url = main.self.gaURLSearch_txt.text()
    audiofile.tag.save()

def dict_clear(self):
    main.self.google_books = {
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
    main.self.goodreads = {
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
    main.self.fantasticfiction = {
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
    main.self.audible = {
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
    main.self.amazon = {
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