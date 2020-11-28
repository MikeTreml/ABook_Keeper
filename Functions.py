import os
import pathlib
import re
import sqlite3

import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from bs4 import BeautifulSoup

import api_keys

goodreads_art_file = 'assets/artwork/goodreads_artwork.jpg'
finished_art_file = 'assets/artwork/finished_artwork.jpg'
google_art_file = 'assets/artwork/google_artwork.jpg'
audible_art_file = 'assets/artwork/audible_artwork.jpg'
ff_art_file = 'assets/artwork/ff_artwork.jpg'
original_art_file = 'assets/artwork/original_artwork.jpg'


def try_check1(book, string1):
    result = ""
    try:
        result = string_cleaner_database(book[string1])
    except:
        result = ""
    return result


def try_check2(book, string1, string2):
    result = ""
    try:
        result = string_cleaner_database(book[string1][string2])
    except:
        result = ""
    return result


def try_check3(book, string1, string2, string3):
    result = ""
    try:
        result = string_cleaner_database(book[string1][string2][string3])
    except:
        result = ""
    return result


def try_check3_array(book, string1, string2, number, string3):
    result = ""
    try:
        result = string_cleaner_database(book[string1][string2][number][string3])
    except:
        result = ""
    return result


def soup_check(soup):
    # some books don't have the requested info. this is to check is it had info to pull
    try:
        # cleaning up the string
        result = re.sub(r"[\n][\W]+[^\w]", "", soup.get_text(strip=True)).replace("Series:", ""). \
            replace(" Series,", "").replace("Narrated by:", "").replace("By:", "").replace("Length: ", "").replace(
            "Release date:", "").replace("Language:", "").replace(" out of 5 stars", " stars ")
    except:
        # if there was no result
        result = ""
    return result


# web scrappers and api search *******************************
def audible_scrapper(input_string):
    series = ""
    book_number = ""
    url = "https://www.audible.com/search?ref=a_search_l1_feature_six_browse-bin_0&feature_six_browse-bin=18685580011&keywords=" + input_string
    page_source = requests.get(url)
    soup = BeautifulSoup(page_source.text, 'lxml')
    books = soup.find_all('li', attrs={"class": "bc-list-item productListItem"})
    book_list = []
    for book in books:
        website = book.find('a', attrs={"class": "bc-link bc-color-link"})['href']
        website_split = website.split('/')
        id = website_split[-1]
        image_url = book.find('img', attrs={"id": "nojs_img_"})['src']
        title = soup_check(book.find('h2', attrs={"class": "bc-heading bc-color-base bc-text-bold"}))
        if ": " in title:
            title, book_number = title.split(": ")
        author = soup_check(book.find('li', attrs={"class": "bc-list-item authorLabel"}))
        narrator = soup_check(book.find('li', attrs={"class": "bc-list-item narratorLabel"}))
        subtitle = soup_check(book.find('li', attrs={"class": "bc-list-item subtitle"}))
        series_book = soup_check(book.find('li', attrs={"class": "bc-list-item seriesLabel"}))
        if series_book != "":
            split_series_book = series_book.split("Book ")
            series = split_series_book[0]
            if len(split_series_book) > 1:
                book_number = split_series_book[1]
        length = soup_check(book.find('li', attrs={"class": "bc-list-item runtimeLabel"}))
        date = soup_check(book.find('li', attrs={"class": "bc-list-item releaseDateLabel"}))
        language = soup_check(book.find('li', attrs={"class": "bc-list-item languageLabel"}))
        rating = soup_check(book.find('li', attrs={"class": "bc-list-item ratingsLabel"}))
        web_url = "https://www.audible.com/pd/" + id

        book_list.append({"id": id, "title": title, "author": author, "narrator": narrator, "series": series,
                          "book_number": book_number, "image_url": image_url, "length": length, "release_date": date,
                          "web_url": web_url, "rating": rating, "subtitle": subtitle, "language": language})
    audible_database_post(book_list)
    return book_list


def ff_scrapper(input_string):
    book_list = []
    ff_database_post(book_list)
    return book_list


def goodreads_srcapper(input_string):
    series = ""
    book_number = ""
    book_list = []
    url = "https://www.goodreads.com/search?utf8=%E2%9C%93&query=" + input_string
    page_source = requests.get(url)
    soup = BeautifulSoup(page_source.text, 'lxml')
    books = soup.find_all('tr')
    for book in books:
        author = soup.find('a', attrs={"class": "authorName"}).get_text(strip=True)
        info = soup.find('a', attrs={"class": "bookTitle"}).get_text(strip=True)
        id = soup.find('div', attrs={"class": "u-anchorTarget"})["id"]
        rating = soup.find('span', attrs={"class": "minirating"}).get_text(strip=True)
        image_url = soup.find('img', attrs={"class": "bookCover"})["src"]
        print(info)
        if ": Book " in info:
            series, book_number = info.split(": Book ")
            title = series
        elif " (" in info:
            title, placeholder = info.split(" (").replace(")", "")
            series, book_number = placeholder.split(", #")
        web_url = "https://www.goodreads.com/book/show/" + id

        book_list.append({"id": id, "title": title, "author": author, "series": series, "book_number": book_number,
                          "image_url": image_url, "web_url": web_url, "rating": rating})
        goodreads_database_post(book_list)
        return book_list


def ff_search(input_string):
    query = input_string.replace(" ", "+")
    url = f"https://www.googleapis.com/customsearch/v1?key={api_keys.API_KEY}&cx={api_keys.SEARCH_ENGINE_ID}&q={query}"
    data = requests.get(url).json()
    book_list = []
    for book in data["items"]:
        title = try_check1(book, "title")
        snippet = try_check1(book, "snippet")
        link = try_check1(book, "link")
        formatted_url = try_check2(book, "formattedUrl")
        book_title = try_check3_array("pagemap", "book", 0, "name")
        person = try_check3_array("pagemap", "person", 0, "name")
        cse_image = try_check3_array("pagemap", "cse_image", 0, "src")
        cse_thumbnail = try_check3_array("pagemap", "cse_thumbnail", 0, "src")

    # book_list.append({"id": link, "title": title, "subtitle": subtitle, "authors": authors, "release_date": date,
    #                "publisher": publisher, "description": description, "image_url": image})
    google_database_post(book_list)
    return book_list


def ff_search(input_string):
    query = input_string.replace(" ", "+")
    string_builder = f"https://www.googleapis.com/books/v1/volumes?q={query}&?key={api_keys.API_KEY}"
    book_list = []
    data = requests.get(string_builder).json()
    for book in data["items"]:
        print(book)
        title = try_check2(book, 'volumeInfo', 'title')
        subtitle = try_check2(book, 'volumeInfo', 'subtitle')
        try:
            authors = book['volumeInfo']['authors'][0]
            print(authors)
        except:
            authors = ''
        date = try_check2(book, 'volumeInfo', 'publishedDate')
        publisher = try_check2(book, 'volumeInfo', 'publisher')
        description = try_check2(book, 'volumeInfo', 'description')
        image = try_check3(book, 'volumeInfo', 'imageLinks', 'thumbnail')
        print(title)
        print(type(title))
        book_id = title + " " + subtitle + " " + authors
        book_list.append({"id": book_id, "title": title, "subtitle": subtitle, "authors": authors, "release_date": date,
                          "publisher": publisher, "description": description, "image_url": image})
        print(book_list)
    google_database_post(book_list)
    return book_list


# database post ********************************
def audible_database_post(book_list):
    db_file = "audiobookspython.db"
    con = sqlite3.connect(db_file)
    for book in book_list:
        con.execute('INSERT INTO audible (id, title, author, narrator, series, book_number, image_url, length, '
                    'release_date, web_url, rating, subtitle, language) '
                    'VALUES (:id, :title, :author, :narrator, :series, :book_number, :image_url, :length, '
                    ':release_date, :web_url, :rating, :subtitle, :language);', book)
    con.commit()


def ff_database_post(book_list):
    db_file = "audiobookspython.db"
    con = sqlite3.connect(db_file)
    for book in book_list:
        con.execute('INSERT INTO fantasticfiction (id, title, author, series, book_number, image_url, web_url) '
                    'VALUES (:id, :title, :author, :series, :book_number, :image_url, :web_url);', book)
    con.commit()


def goodreads_database_post(book_list):
    db_file = "audiobookspython.db"
    con = sqlite3.connect(db_file)
    for book in book_list:
        con.execute('INSERT INTO goodreads (id, title, author, series, book_number, image_url, web_url, rating) '
                    'VALUES (:id, :title, :author, :series, :book_number, :image_url, :web_url, :rating);', book)
    con.commit()


def google_database_post(book_list):
    db_file = "audiobookspython.db"
    con = sqlite3.connect(db_file)
    for book in book_list:
        con.execute(
            'INSERT INTO googlebooks (id, title, subtitle, authors, release_date, publisher,description,image_url) '
            'VALUES (:id, :title, :subtitle, :authors, :release_date, :publisher,:description,:image_url);', book)
    con.commit()


def database_get(id, table):
    con = sqlite3.connect("audiobookspython.db")
    c = con.cursor()
    print(id)
    print(table)
    c.execute("Select * from " + table + " where id='" + id + "'")
    row = c.fetchone()
    return row


def string_cleaner_database(string):
    return string.replace("'", "`")


def delete_artwork():
    deleteExist(goodreads_art_file)
    deleteExist(finished_art_file)
    deleteExist(google_art_file)
    deleteExist(audible_art_file)
    deleteExist(ff_art_file)
    deleteExist(original_art_file)


def image_refresh(self):
    self.google_artwork.setPixmap((QPixmap(google_art_file)).scaled(self.google_artwork.size(), Qt.KeepAspectRatio,
                                                                    Qt.SmoothTransformation))
    self.ff_artwork.setPixmap((QPixmap(ff_art_file)).scaled(self.ff_artwork.size(), Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation))
    self.audible_artwork.setPixmap((QPixmap(audible_art_file)).scaled(self.audible_artwork.size(), Qt.KeepAspectRatio,
                                                                      Qt.SmoothTransformation))
    self.goodreads_artwork.setPixmap((QPixmap(goodreads_art_file)).scaled(self.goodreads_artwork.size(),
                                                                          Qt.KeepAspectRatio, Qt.SmoothTransformation))
    self.finished_artwork.setPixmap((QPixmap(finished_art_file)).scaled(self.finished_artwork.size(),
                                                                        Qt.KeepAspectRatio, Qt.SmoothTransformation))
    self.original_artwork.setPixmap((QPixmap(original_art_file)).scaled(self.original_artwork.size(),
                                                                        Qt.KeepAspectRatio, Qt.SmoothTransformation))


def deleteExist(path):
    file = pathlib.Path(path)
    if file.exists():
        os.remove(path)
