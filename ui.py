from book import Book
import wishlist


def display_menu_get_choice():
    '''Display choices for user, return users' selection'''

    print('''
        1. Show unread books (wishlist)
        2. Show books that have been read
        3. Mark a book as read
        4. Add book to wishlist
        5. Search for book by title
        6. Edit a title or author
        7. Delete a book
        8. Sort books by title
        9. Sort books by author
        q. Quit
    ''')

    choice = input('Enter your selection: ')

    return choice


def show_list(books):
    ''' Format and display a list of book objects'''

    if len(books) == 0:
        print('* No books *')
        return

    for book in books:
        print(book)

    print('* {} book(s) *'.format(len(books)))


def ask_for_book_id():
    ''' Ask user for book id, validate to ensure it is a positive integer '''

    while True:
        try:
            id = int(input('Enter book id:'))
            if id >= 0:
                return id
            else:
                print('Please enter a positive number ')
        except ValueError:
            print('Please enter an integer number')

def ask_for_book_title():
    ''' Ask user for book title, validate to ensure it is a string '''
    while True:
        search_string = input('Enter book title: ')
        if isinstance(search_string, str):
            return search_string
        else:
            print('Please enter a string')
            continue

def get_date_read():
    ''' Added date read for user input with no rigid format '''
    date = input("When did you finish this book? ")
    return date    

def get_new_book_info():
    ''' Get title and author of new book from user '''

    title = input('Enter title: ')
    author = input('Enter author: ')
    return Book(title, author)

def get_read_book_rating_review():
    ''' Get a rating and review about recently read book from user '''
    while True:
        try:
            while True:
                rating = int(input('Enter Rating (1-5): '))
                if 1 <= rating <= 5:
                    rating = '*' * rating
                    break
                else:
                    print('Please input a number between 1 and 5')
                    continue
        except ValueError:
            print('Please enter a positive number')
            continue

        review = input('Enter review: ')
        return rating, review

def message(msg):
    '''Display a message to the user'''
    print(msg)
