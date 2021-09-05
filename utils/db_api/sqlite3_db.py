import logging
import sqlite3
import os

patch_db = '/utils/db_api/'


def create_table():
    try:
        sqlite3_connection = sqlite3.connect(os.getcwd() + '/sqlite_books.db')
        cursor = sqlite3_connection.cursor()
        logging.info('sqlite3 connection')
        # cursor.execute(
        #     """
        #         CREATE TABLE IF NOT EXISTS programming_language (
        #         name TEXT NOT NULL UNIQUE PRIMARY KEY);
        #      """)
        # cursor.execute("""
        #             CREATE TABLE books_language (
        #             name TEXT NOT NULL UNIQUE PRIMARY KEY);""")
        cursor.execute(
            """
            CREATE TABLE books (
            uid TEXT NOT NULL UNIQUE PRIMARY KEY,
            name TEXT NOT NULL,
            author TEXT NOT NULL,
            year INT NOT NULL,
            programming_language TEXT NOT NULL,
            book_language TEXT NOT NULL,
            active BOOLEAN NOT NULL DEFAULT 'false');
            """)
        cursor.execute(
                """
                    CREATE TABLE books_address (
                    file_unique_id TEXT NOT NULL UNIQUE PRIMARY KEY,
                    mime_type TEXT NOT NULL,
                    file_id TEXT NOT NULL,
                    book TEXT NOT NULL,
                    file_name TEXT NOT NULL,
                    file_size INT NOT NULL,
                    FOREIGN KEY(book) REFERENCES books(uid));
                """
            )
        sqlite3_connection.commit()
    except sqlite3.Error as error:
        logging.info(f'Error connection sqlite3 --- {error} ---')
    finally:
        if sqlite3_connection:
            sqlite3_connection.close()
            logging.info('sqlite3 disconnect')


def insert_programming_language_table(name_language):

    add_programming_language = True
    try:
        sqlite3_connection = sqlite3.connect(os.getcwd() + f'{patch_db}sqlite_books.db')
        cursor = sqlite3_connection.cursor()
        logging.info('sqlite3 connection')
        cursor.execute(f"""INSERT INTO programming_language
                          VALUES ('{name_language}')"""
                       )
        sqlite3_connection.commit()
    except sqlite3.Error as error:
        logging.info(f'Error connection sqlite3 --- {error} ---')
        add_programming_language = False
    finally:
        if sqlite3_connection:
            sqlite3_connection.close()
            logging.info('sqlite3 disconnect')

    return add_programming_language


def insert_language_table(name_books_language):

    add_book_language = True
    try:
        sqlite3_connection = sqlite3.connect(os.getcwd() + f'{patch_db}sqlite_books.db')
        cursor = sqlite3_connection.cursor()
        logging.info('sqlite3 connection')
        cursor.execute(f"""INSERT INTO books_language
                          VALUES ('{name_books_language}')"""
                       )
        sqlite3_connection.commit()
    except sqlite3.Error as error:
        logging.info(f'Error connection sqlite3 --- {error} ---')
        add_book_language = False
    finally:
        if sqlite3_connection:
            sqlite3_connection.close()
            logging.info('sqlite3 disconnect')

    return add_book_language


def create_books(data_book):

    add_book = True
    try:
        sqlite3_connection = sqlite3.connect(os.getcwd() + f'{patch_db}sqlite_books.db')
        cursor = sqlite3_connection.cursor()
        logging.info('sqlite3 connection')
        cursor.execute(f"""INSERT INTO books
                          VALUES (?,?,?,?,?,?,?)""", data_book
                       )
        sqlite3_connection.commit()
    except sqlite3.Error as error:
        logging.info(f'Error connection sqlite3 --- {error} ---')
        add_book = False
    finally:
        if sqlite3_connection:
            sqlite3_connection.close()
            logging.info('sqlite3 disconnect')

    return add_book


def create_books_address(book_address):

    add_book = True
    try:
        sqlite3_connection = sqlite3.connect(os.getcwd() + f'{patch_db}sqlite_books.db')
        cursor = sqlite3_connection.cursor()
        logging.info('sqlite3 connection')
        cursor.executemany("INSERT INTO books_address VALUES (?,?,?,?,?,?)", book_address)
        sqlite3_connection.commit()
    except sqlite3.Error as error:
        logging.info(f'Error connection sqlite3 --- {error} ---')
        add_book = False
    finally:
        if sqlite3_connection:
            sqlite3_connection.close()
            logging.info('sqlite3 disconnect')

    return add_book


def select_all_books_witch_language_programming(language_name):

    data = []
    try:
        sqlite3_connection = sqlite3.connect(os.getcwd() + f'{patch_db}sqlite_books.db')
        cursor = sqlite3_connection.cursor()
        sql = "SELECT * FROM books WHERE programming_language=?"
        logging.info('sqlite3 connection')
        cursor.execute(sql, [(language_name)])
        data = cursor.fetchall()
    except sqlite3.Error as error:
        logging.info(f'Error connection sqlite3 --- {error} ---')
    finally:
        if sqlite3_connection:
            sqlite3_connection.close()
            logging.info('sqlite3 disconnect')

    return data
