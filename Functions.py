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
    print(type(soup))

    if soup is None:
        soup_string = ""
    elif type(soup) != str:
        soup_string = str(soup.get_text(strip=True))
    else:
        soup_string = soup

    clean_soup = soup_string.replace("Series:", "").replace(" Series,", "").replace(
        "Narrated by:", "").replace("By:", "").replace("Length: ", "").replace("Release date:", "").replace(
        "Language:", "").replace(" out of 5 stars", " stars ")
    try:
        # cleaning up the string
        result = re.sub(r"[\n][\W]+[^\w]", "", clean_soup)
    except:
        # if there was no result
        result = clean_soup
    clean_result = string_cleaner_database(result)
    return clean_result


# web scrappers and api search *******************************
def audible_scrapper(input_string):
    series = "Novel"
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
        title = soup_check(book.find('h2', attrs={"class": "bc-heading bc-color-base bc-text-bold"})).replace(": ", "~")
        if "~" in title:
            title, book_number = title.split("~")
        author = soup_check(book.find('li', attrs={"class": "bc-list-item authorLabel"}))
        narrator = soup_check(book.find('li', attrs={"class": "bc-list-item narratorLabel"}))
        subtitle = soup_check(book.find('li', attrs={"class": "bc-list-item subtitle"}))
        series_book = soup_check(book.find('li', attrs={"class": "bc-list-item seriesLabel"}))
        if series_book != "":
            split_series_book = series_book.split("Book ")
            series = split_series_book[0]
            if len(split_series_book) > 1:
                book_number = split_series_book[1]
        else:
            split_subtitle_book = subtitle.split("Book ")
            series = split_subtitle_book[0]
            if len(split_subtitle_book) > 1:
                book_number = split_subtitle_book[1]
        length = soup_check(book.find('li', attrs={"class": "bc-list-item runtimeLabel"}))
        date = soup_check(book.find('li', attrs={"class": "bc-list-item releaseDateLabel"}))
        language = soup_check(book.find('li', attrs={"class": "bc-list-item languageLabel"}))
        rating = soup_check(book.find('li', attrs={"class": "bc-list-item ratingsLabel"}))
        web_url = "https://www.audible.com/pd/" + id
        if series == "":
            series = "Novel"
        book_list.append({"id": id, "title": title, "author": author, "narrator": narrator, "series": series,
                          "book_number": book_number, "image_url": image_url, "length": length, "release_date": date,
                          "web_url": web_url, "rating": rating, "subtitle": subtitle, "language": language})
    audible_database_post(book_list)
    return book_list


def goodreads_srcapper(input_string):
    series = "Novel"
    book_number = ""
    title = ""
    book_list = []
    url = "https://www.goodreads.com/search?utf8=%E2%9C%93&query=" + input_string
    page_source = requests.get(url)
    soup = BeautifulSoup(page_source.text, 'lxml')
    books = soup.find_all('tr')
    for book in books:
        author = soup_check(book.find('a', attrs={"class": "authorName"}))
        info = soup_check(book.find('a', attrs={"class": "bookTitle"})).replace(": Book ", "~").replace(" Book #",
                                                                                                        "~").replace(
            " (", "~").replace(")", "").replace(", #", "~")
        id = soup_check(book.find('div', attrs={"class": "u-anchorTarget"})["id"])
        rating = soup_check(book.find('span', attrs={"class": "minirating"}))
        image_url = book.find('img', attrs={"class": "bookCover"})["src"]
        print("info " + info)
        info_split = info.split("~")
        if len(info_split) == 1:
            try:
                title, series = info_split[0].split("∶")
                book_number = "0"
            except:
                title = info_split[0]

        elif len(info_split) == 2:
            series = info_split[0]
            book_number = info_split[1]
            title = series
        elif len(info_split) == 3:
            title = info_split[0]
            series = info_split[1]
            book_number = info_split[2]
        web_url = "https://www.goodreads.com/book/show/" + id
        if series == "":
            series = "Novel"
        book_list.append({"id": id, "title": title, "author": author, "series": series, "book_number": book_number,
                          "image_url": image_url, "web_url": web_url, "rating": rating})
        goodreads_database_post(book_list)
        return book_list


def ff_search(input_string):
    query = input_string.replace(" ", "+")
    url = f"https://www.googleapis.com/customsearch/v1?key={api_keys.API_KEY}&cx={api_keys.SEARCH_ENGINE_ID}&q={query}"
    data = requests.get(url).json()
    print(data)
    book_list = []
    for book in data["items"]:
        link = book["link"]
        if ".htm" in link:
            soup = ff_direct_search(link)
            try:
                image = soup.find('img', attrs={'class': 'bookimage'})['data-us']
                image_url = "https://m.media-amazon.com/images/I/" + image
            except:
                print("no image")
            info = soup.find('title').get_text(strip=True).replace(") by ", "~").replace(" by ", "~").replace(' (', "~").replace(
                ', book ', "~")
            print(info)
            info_split = info.split("~")
            series = 'Novel'
            book_number = "0"
            if len(info_split) == 2:
                title = info_split[0]
                author = info_split[1]
            if len(info_split) == 1:
                title, book_number = info.split(": Book ")
                series = title
            elif len(info_split) == 4:
                title = info_split[0]
                series = info_split[1]
                book_number = info_split[2]
                author = info_split[3]
            else:
                print("error")
                print(info_split)
            if series == "":
                series = "Novel"
            book_list.append({"id": link, "title": title, "series": series, "author": author,
                              "book_number": book_number, "web_url": link, "image_url": image_url})
    ff_database_post(book_list)
    return book_list


def google_search(input_string):
    query = input_string.replace(" ", "+")
    string_builder = f"https://www.googleapis.com/books/v1/volumes?q={query}&?key={api_keys.API_KEY}"
    book_list = []
    series = "Novel"
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
        try:
            image = book['volumeInfo']['imageLinks']['thumbnail']
        except:
            print("image issue")
        print(title)
        print(type(title))
        book_id = title + " " + subtitle + " " + authors
        if series == "":
            series = "Novel"
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
    return string.replace("'", "`").replace(":", "∶").replace(",", "")


def delete_artwork():
    delete_exist(goodreads_art_file)
    delete_exist(finished_art_file)
    delete_exist(google_art_file)
    delete_exist(audible_art_file)
    delete_exist(ff_art_file)
    delete_exist(original_art_file)


def ff_direct_search(link):
    page_source = requests.get(link)
    soup = BeautifulSoup(page_source.text, 'lxml')

    return soup


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


def delete_exist(path):
    file = pathlib.Path(path)
    if file.exists():
        os.remove(path)
