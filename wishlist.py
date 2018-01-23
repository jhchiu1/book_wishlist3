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

    elif choice == '8':
        sort_by_title()

    elif choice == '9':
        sort_by_author()

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
    if datastore.set_read(book_id, ui.get_date_read(), ui.get_read_book_rating_review()):
        ui.message('Successfully updated')
    else:
        ui.message('Book id not found in database')

def new_book():
    '''Get info from user, add new book'''
    new_book = ui.get_new_book_info()
    datastore.add_book(new_book)
    ui.message('Book added: ' + str(new_book))

def search_book(**kwargs):
    ''' Get choice from user, search datastore, display found/not found'''
    book_title = ui.get_new_book_title()
    found = datastore.get_books(title=book_title)
    ui.show_list(found)

def quit():
    '''Perform shutdown tasks'''
    datastore.shutdown()
    ui.message('Bye!')

def delete():
    ''' Ask user input for book id, remove book from db if deleted, show message if action completed '''
    id = ui.ask_for_book_id()
    for book in datastore.book_list:
        if book.id == id:
            datastore.book_list.remove(book)
            ui.message("Successfully deleted.")

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