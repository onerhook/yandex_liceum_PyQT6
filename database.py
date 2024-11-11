import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS books
                          (id INTEGER PRIMARY KEY,
                           title TEXT,
                           author TEXT,
                           year INTEGER,
                           image TEXT)''')
        conn.commit()
        conn.close()

    def add_book(self, title, author, year, image):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO books (title, author, year, image)
                          VALUES (?, ?, ?, ?)''', (title, author, year, image))
        conn.commit()
        conn.close()

    def search_books(self, title):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM books WHERE title LIKE ?''', ('%' + title + '%',))
        books = cursor.fetchall()
        conn.close()
        return books

    def get_all_books(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()
        conn.close()
        return books
