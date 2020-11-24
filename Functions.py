import os
import pathlib
import re
import sqlite3

import requests
from bs4 import BeautifulSoup

import api_keys


def try_check(book, string1):
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


def soup_check(soup):
    # some books don't have the requested info. this is to check is it had info to pull
    try:
        # cleaning up the string
        result = re.sub(r"[\n][\W]+[^\w]", "", soup.get_text(strip=True))
    except:
        # if there was no result
        result = ""
    return result


def audible_search(input_string):
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
        print(image_url)

        title = soup_check(book.find('h2', attrs={"class": "bc-heading bc-color-base bc-text-bold"}))
        author = soup_check(book.find('li', attrs={"class": "bc-list-item authorLabel"})).replace("By:", "")
        narrator = soup_check(book.find('li', attrs={"class": "bc-list-item narratorLabel"})).replace("Narrated by:",
                                                                                                      "")
        subtitle = soup_check(book.find('li', attrs={"class": "bc-list-item subtitle"})).replace("Series:", "")

        series_book = soup_check(book.find('li', attrs={"class": "bc-list-item seriesLabel"})).replace("Series:",
                                                                                                       "").replace(
            " Series,", "")
        print(series_book)
        if series_book != "":
            split_series_book = series_book.split("Book ")
            print(split_series_book)
            series = split_series_book[0]
            print(len(split_series_book))
            if len(split_series_book) > 1:
                book_number = split_series_book[1]
        length = soup_check(book.find('li', attrs={"class": "bc-list-item runtimeLabel"})).replace("Length: ", "")
        date = soup_check(book.find('li', attrs={"class": "bc-list-item releaseDateLabel"})).replace("Release date:",
                                                                                                     "")
        language = soup_check(book.find('li', attrs={"class": "bc-list-item languageLabel"})).replace("Language:", "")
        rating = soup_check(book.find('li', attrs={"class": "bc-list-item ratingsLabel"})).replace(" out of 5 stars",
                                                                                                   " stars ")
        web_url = "https://www.audible.com/pd/" + id

        book_list.append({"id": id, "title": title, "author": author, "narrator": narrator, "series": series,
                          "book_number": book_number, "image_url": image_url, "length": length, "release_date": date,
                          "web_url": web_url, "rating": rating, "subtitle": subtitle, "language": language})
    print(book_list)
    audible_database_post(book_list)
    return book_list


def audible_database_post(book_list):
    db_file = "audiobookspython.db"
    con = sqlite3.connect(db_file)
    for book in book_list:
        con.execute(
            'INSERT INTO audible (id, title, author, narrator, series, book_number, image_url, length, release_date, web_url, rating, subtitle, language) '
            'VALUES (:id, :title, :author, :narrator, :series, :book_number, :image_url, :length, :release_date, :web_url, :rating, :subtitle, :language);',
            book)
    con.commit()


def google_search(input_string):
    search_string = input_string.replace(" ", "+")
    string_builder = "https://www.googleapis.com/books/v1/volumes?q=" + search_string + api_keys.google_api_key
    book_list = []
    google_request = requests.get(string_builder)
    data = google_request.json()
    print(data)
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
    deleteExist('assets/artwork/goodreads_artwork.jpg')
    deleteExist('assets/artwork/finished_artwork.jpg')
    deleteExist('assets/artwork/google_artwork.jpg')
    deleteExist('assets/artwork/audible_artwork.jpg')
    deleteExist('assets/artwork/ff_artwork.jpg')
    deleteExist('assets/artwork/original_artwork.jpg')


def deleteExist(path):
    file = pathlib.Path(path)
    if file.exists():
        os.remove(path)
