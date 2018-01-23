db.py

import sqlite3

# Creating database, cursor, and table
try:
    db = sqlite3.connect('jugglers.db')
    cursor = db.cursor()
    cursor.execute('create table if not exists jugglers (name text, country text, catches int)')
except sqlite3.Error:
    print('Error creating table')
finally:
    db.close()

# Adding sample information to table
try:
    db = sqlite3.connect('jugglers.db')
    cursor = db.cursor()
    with db:
        cursor.execute('insert into jugglers values ("Ian Stewart", "Canada", 94)')
        cursor.execute('insert into jugglers values ("Aaron Gregg", "Canada", 88)')
        cursor.execute('insert into jugglers values ("Chad Taylor", "USA", 78)')
except sqlite3.Error as e:
    print('Error adding rows:')
    print(e)
finally:
    db.close()


# Gets name, country, and catches from user and adds data to database
def add_juggler(name, country, catches):
    try:
        db = sqlite3.connect('jugglers.db')
        cursor = db.cursor()
        with db:
            cursor.execute('insert into jugglers values (?, ?, ?)', (name, country, catches))
    except sqlite3.Error as e:
        print('Error adding data to table:')
        print(e)
    finally:
        db.close()


# Gets juggler's name from the user, removes them from the database
def remove_juggler(name):
    try:
        db = sqlite3.connect('jugglers.db')
        cursor = db.cursor()
        with db:
            cursor.execute('delete from jugglers where name=?', (name,))
    except sqlite3.Error as e:
        print('Error removing data from table:')
        print(e)


# Prints contents of jugglers table
def view_all():
    try:
        db = sqlite3.connect('jugglers.db')
        cursor = db.cursor()
        for row in cursor.execute('select * from jugglers'):
            print(row)
    except sqlite3.Error as e:
        print('Error printing data:')
        print(e)
    finally:
        db.close()


# Edits a juggler's number of catches
def edit(name, catches):
    try:
        db = sqlite3.connect('jugglers.db')
        cursor = db.cursor()
        with db:
            cursor.execute('update jugglers set catches=? where name=?', (catches, name))
    except sqlite3.Error as e:
        print('Error updating data:')
        print(e)
    finally:
        db.close()