import os
import json
from book import Book
from ui import get_read_book_rating_review

DATA_DIR = 'data'
BOOKS_FILE_NAME = os.path.join(DATA_DIR, 'wishlist.txt')
COUNTER_FILE_NAME = os.path.join(DATA_DIR, 'counter.txt')

book_list = []
counter = 0


def setup():
    """ read(): Read book info from file, if file exists. """
    read()


def shutdown():
    """write(): Save all data to a file - one for books, one for the current counter value, for persistent storage"""
    write()


def get_books(**kwargs):
    """ Return books from data store. With no arguments, returns everything. """

    global book_list

    if len(kwargs) == 0:
        return book_list
    elif 'read' in kwargs:
        read_books = [book for book in book_list if book.read == kwargs['read']]
        return read_books
    else:
        found_books = [book for book in book_list if book.title == kwargs['title']]
        return found_books


def add_book(book):
    """ Add to db, set id value, return Book"""

    global book_list

    book.id = generate_id()
    book_list.append(book)


def generate_id():
    global counter
    counter += 1
    return counter


def set_read(book_id, read):
    """ Update book with given book_id to read. Return True if book is found in DB and update is made,
    False otherwise. Set a rating and review for book"""

    global book_list

    for book in book_list:

        if book.id == book_id:
            rating, review = get_read_book_rating_review()
            book.rating = rating
            book.review = review
            book.read = True
            return True

    return False  # return False if book id is not found


def book_json_manipulation(json_as_dict):
    """ converts json to list """
    global book_list

    for key, value in json_as_dict.items():
        book_container = json_as_dict[key]
        book = Book(book_container['title'],
                    book_container['author'],
                    book_container['read'] == 'True',
                    int(book_container['id']))
        book.rating = book_container['rating']
        book.review = book_container['review']
        book_list.append(book)
    except Exception as e:
        print("Error: Not located in index!", e)


def book_list_manipulation():
    """ converts list to json """
    global book_list
    book_json = {}
    for book in book_list:
        book_container = {'title': book.title,
                          'author': book.author,
                          'read': str(book.read),
                          'rating': book.rating,
                          'review': book.review,
                          'id': str(book.id)}
        book_json[str(book.id)] = book_container

    return book_json


def read():
    """ Read book info from file, if file exists. """
    global counter

    try:
        with open(BOOKS_FILE_NAME) as f:
            book_json = json.load(f)
            book_json_manipulation(book_json)
    except FileNotFoundError:
        # First time program has run. Assume no books.
        pass

    try:
        with open(COUNTER_FILE_NAME) as f:
            try:
                counter = int(f.read())
            except:
                counter = 0
    except:
        counter = len(book_list)


def write():
    """Save all data to a file - one for books, one for the current counter value, for persistent storage"""

    output_data = book_list_manipulation()

    # Create data directory
    try:
        os.mkdir(DATA_DIR)
    except FileExistsError:
        pass  # Ignore - if directory exists, don't need to do anything.

    with open(BOOKS_FILE_NAME, 'w') as f:
        json.dump(output_data, f)

    with open(COUNTER_FILE_NAME, 'w') as f:
        f.write(str(counter))
