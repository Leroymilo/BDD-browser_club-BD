# The structure of the tables.
#/!\ WARNING : running this script will reset the database ! (If you uncomment stuff)

from numpy import full
from base import *

from functions.adders import *

editors = """CREATE TABLE EDITORS
(id INTEGER PRIMARY KEY, full_name VARCHAR(64) UNIQUE);"""
authors = """CREATE TABLE AUTHORS
(id INTEGER PRIMARY KEY, full_name VARCHAR(64) UNIQUE);"""
categories = """CREATE TABLE CATEGORIES (id INTEGER PRIMARY KEY, name VARCHAR(32));"""
series = """CREATE TABLE SERIES
(id VARCHAR(3) PRIMARY KEY, full_name VARCHAR(64) NOT NULL, category INTEGER NOT NULL, kind VARCHAR(16));"""
#"Connecting" authors to series :
wrote = """CREATE TABLE WROTE
(author_id INTEGER, series_id VARCHAR(3), PRIMARY KEY (author_id, series_id));"""
books = """CREATE TABLE BOOKS
(id VARCHAR(8) PRIMARY KEY, id_series VARCHAR(3) NOT NULL, vol_num INTEGER NOT NULL, vol_name VARCHAR(64), ex_num INTEGER NOT NULL,
id_editor INTEGER, buy_date DATE, dispo BOOLEAN, old_id VARCHAR(12) NULL);"""

# cursor.execute("DROP TABLE IF EXISTS EDITORS;")
# cursor.execute(editors)
# cursor.execute("DROP TABLE IF EXISTS AUTHORs;")
# cursor.execute(authors)
# cursor.execute("DROP TABLE IF EXISTS CATEGORIES;")
# cursor.execute(categories)
# cursor.execute("DROP TABLE IF EXISTS SERIES;")
# cursor.execute(series)
# cursor.execute("DROP TABLE IF EXISTS WROTE;")
# cursor.execute(wrote)
# cursor.execute("DROP TABLE IF EXISTS BOOKS;")
# cursor.execute(books)

users = """CREATE TABLE USERS
(id INTEGER PRIMARY KEY, f_name VARCHAR(32) NOT NULL, l_name VARCHAR(32), tel VARCHAR(10), mail VARCHAR(64),
loan_nb INTEGER, max_loan_nb iNTEGER, UNIQUE (f_name, l_name));"""
loans = """CREATE TABLE LOANS
(id_book VARCHAR(8) PRIMARY KEY, id_user INTEGER NOT NULL, start_date DATE, end_date DATE);"""

# cursor.execute("DROP TABLE IF EXISTS USERS;")
# cursor.execute(users)
# cursor.execute("DROP TABLE IF EXISTS LOANS;")
# cursor.execute(loans)

db.commit()

db.close()