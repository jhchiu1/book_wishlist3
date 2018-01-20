#Main program

import ui, datastore
from book import Book


def handle_choice(choice):

    if choice == '1':
        show_unread()

    elif choice == '2':
        show_read()

    elif choice == '3':
        book_read()

    elif choice == '4':
        new_book()

    elif choice == '5':
        search_book()

    elif choice == '6':
        edit()

    elif choice == '7':
        delete()

    elif choice == 'q':
        quit()

    else:
        ui.message('Please enter a valid selection')


def show_unread():
    '''Fetch and show all unread books'''
    unread = datastore.get_books(read=False)
    ui.show_list(unread)


def show_read():
    '''Fetch and show all read books'''
    read = datastore.get_books(read=True)
    ui.show_list(read)


def book_read():
    ''' Get choice from user, edit datastore, display success/error'''
    book_id = ui.ask_for_book_id()
    if datastore.set_read(book_id, True):
        ui.message('Successfully updated')
    else:
        ui.message('Book id not found in database')


def new_book():
    '''Get info from user, add new book'''
    new_book = ui.get_new_book_info()
    datastore.add_book(new_book)
    ui.message('Book added: ' + str(new_book))


def search_book():
    '''Get choice from user, search datastore, display found/not found'''
    book_title = ui.ask_for_book_title()
    found = datastore.get_books(title=book_title)
    ui.show_list(found)

def edit():
    '''Get info from user, edit book title, author'''
    id = ui.ask_for_book_id()
    to_edit = ui.ask_what_to_edit()
    new_book = ui.get_new_book_info()
    for book in datastore.show_list:
        if book.id == id:
            read = book.read
            title = book.title
            author = book.author
            if to_edit == 'author':
                datastore.book_list.remove(book)
                datastore.book_list.append(Book(title, new_book_info, read, id))
            elif to_edit == 'title':
                datastore.show_list.remove(book)
                datastore.show_list.append(Book(new_book_info, author, read, id))

    ui.message("Successfully updated.")

def check_book_in_system(title, author):
    ''' Check to see if book has been read '''
    for book in datastore.book_list:
        if book.author == author and book.title == title and book.read is True:
            return "read"
        elif book.author == author and book.title == title and book.read is False:
            return "unread"
        elif book.author != author or book.title != title:
            return False
    if len(datastore.book_list) == 0:
        return False

def quit():
    '''Perform shutdown tasks'''
    datastore.shutdown()
    ui.message('Bye!')

def sort_by_title():
    ''' Sort by book title '''
    unread = datastore.get_sorted_books_by_title()
    ui.show_list(unread)

def sort_by_author():
    ''' Sort by book author '''
    unread = datastore.get_sorted_books_by_author()
    ui.show_list(unread)

def main():

    datastore.setup()

    quit = 'q'
    choice = None

    while choice != quit:
        choice = ui.display_menu_get_choice()
        handle_choice(choice)


if __name__ == '__main__':
    main()
