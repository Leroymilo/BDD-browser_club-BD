#Script imported everywhere to get the db and cursor objects

from sqlite3 import *

db = connect("db.db")
cursor = db.cursor()