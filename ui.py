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

def ask_what_to_edit():
    ''' Get new edit values to append '''
    response = input("Do you wish to edit the Author or Title? Enter 1 for Author or 2 for Title: ")
    while response != "1" and response != "2":
        response = input("Please try again, enter 1 or 2.\nDo you wish to edit the Author or Title? Enter 1 for Author or 2 for Title: ")
    if response == "1":
        response = "author"
    elif response == "2":
        response = "title"
    return response

def get_date_read():
    ''' Added date read for user input with no rigid format '''
    date = input("When did you finish this book? ")
    return date    

def get_new_book_info():
    ''' Get title and author of new book from user '''

    title = input('Enter title: ')
    author = input('Enter author: ')
    in_system = wishlist.check_book_in_system(title, author)
    if in_system is False:
        return Book(title, author)
    elif in_system == "read":
        answer = input("You already marked a book as Read with the same title and author. Are you sure "
                           "you want to add this book again? Enter 1 for yes or 2 for no.")
        while answer != "1" and answer != "2":
            answer = input("Please try again, enter 1 for yes, 2 for no. You already marked a book as Read with the same "
                               "title and author. Are you sure you want to add this book again? Enter 1 for yes or 2 for no.")
        if answer == "1":
            return Book(title, author)
        elif answer == "2":
            return "null"
    elif in_system == "unread":
        print("This book is already in the system and listed as unread; please mark that book as Read or "
                  "change the title/author to add this book again.")
        return "null"


def get_new_value():
    ''' Ask uer for new values to append book '''
    new_value = input("What is the new value? ")
    return new_value

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

        '''review = input('Enter review: ')'''
        return rating

def get_search_term():
    ''' Ask user for keyword to perform book search '''
    search_term = input("Please enter a title or author keyword: ")
    return search_term

def message(msg):
    '''Display a message to the user'''
    print(msg)
