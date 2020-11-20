import os
from . import main


def OpenFolderBtn(self):
    #start = datetime.now()
    # self.fileComboBox.clear()
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(self.path):
        listOfFiles = [os.path.join(dirpath, file) for file in filenames]
    for elem in listOfFiles:
        self.fileComboBox.addItem(elem)

    # print('open folder', datetime.now() - start)


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