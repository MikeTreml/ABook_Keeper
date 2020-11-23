import sqlite3

import requests

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
        # query = "INSERT INTO googlebooks" + str(keys) + " values (" + sql + ") ON CONFLICT(" + conflict + ") DO UPDATE SET " + dupSQL[:-2] + ';'
        # con.execute(query)
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
