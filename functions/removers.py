#Functions to remove tuples from the database

from base import *

def end_loan(f_name:str, l_name:str, id_book:str) :
    cursor.execute(f"SELECT id FROM USERS WHERE f_name='{f_name}' AND l_name='{l_name}'")
    id_user, = cursor.fetchone()
    cursor.execute(f"DELETE FROM LOANS WHERE id_user={id_user} AND id_book='{id_book}';")
    cursor.execute(f"UPDATE BOOKS SET dispo=TRUE WHERE id='{id_book}';")
    cursor.execute(f"UPDATE USERS SET loan_nb=loan_nb-1 WHERE id={id_user};")
    db.commit()

def remove_users(id) :
    cursor.execute(f"UPDATE BOOKS SET dispo=TRUE WHERE id IN (SELECT id_book FROM LOANS WHERE id_user={id});")
    cursor.execute(f"DELETE FROM LOANS WHERE id_user={id};")
    cursor.execute(f"DELETE FROM USERS WHERE id={id};")
    db.commit()

def remove_book(id) :
    cursor.execute(f"UPDATE USERS SET loan_nb=loan_nb-1 WHERE id IN (SELECT id_user FROM LOANS WHERE id_book='{id}');")
    cursor.execute(f"DELETE FROM LOANS WHERE id_book='{id}';")
    cursor.execute(f"DELETE FROM BOOKS WHERE id='{id}';")
    db.commit()

def remove_series(id) :
    cursor.execute(f"SELECT id FROM BOOKS WHERE id_series='{id}';")
    id_books = cursor.fetchall()
    for (id_book, ) in id_books :
        remove_book(id_book)
    cursor.execute(f"DELETE FROM SERIES WHERE id='{id}';")
    cursor.execute(f"DELETE FROM WROTE WHERE series_id='{id}'")
    db.commit()

def remove_author(id) :
    id = str(id).rjust(3, '0')
    cursor.execute(f"DELETE FROM WROTE WHERE author_id={id};")
    cursor.execute(f"DELETE FROM AUTHORS WHERE id={id};")
    db.commit()
        
def remove_editor(id) :
    cursor.execute(f"UPDATE BOOKS SET id_editor=NULL WHERE id_editor={id};")
    cursor.execute(f"DELETE FROM EDITORS WHERE id={id};")
    db.commit()