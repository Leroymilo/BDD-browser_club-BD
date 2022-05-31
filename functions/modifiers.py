#Functions to modifies tuples of the database

from base import *

def modif_book(id:str, vol_name:str, editor_id:int, buy_date:str) :
    cursor.execute(f"""UPDATE BOOKS
    SET vol_name='{vol_name}', id_editor={editor_id}, buy_date='{buy_date}'
    WHERE id='{id}'""")
    db.commit()
    return True

def modif_series(old_id:str, id:str, full_name:str, category:int, kind:str, author_ids:list[int]) :
    if old_id != id :
        cursor.execute(f"SELECT * FROM SERIES WHERE id='{id}';")
        if len(cursor.fetchall()) != 0 :
            return 1
    
    cursor.execute(f"SELECT full_name FROM SERIES WHERE id='{old_id}'")
    old_name, = cursor.fetchone()
    if old_name != full_name :
        cursor.execute(f"SELECT * FROM SERIES WHERE full_name='{full_name}';")
        if len(cursor.fetchall()) != 0 :
            return 2
    
    #Updating books id and id_series
    cursor.execute(f"SELECT category FROM SERIES WHERE id='{old_id}'")
    old_cat = cursor.fetchone()
    if old_cat != category or old_id != id :
        cursor.execute(f"SELECT id, old_id FROM BOOKS WHERE id_series='{old_id}'")
        books = cursor.fetchall()
        for book in books :
            new_book_id = str(category).rjust(2, '0') + id + book[0][5:]
            #Updating loans :
            cursor.execute(f"UPDATE LOANS SET book_id='{new_book_id}' WHERE id='{book[0]}'")
            #Updating the book :
            if book[1] is None :
                cursor.execute(f"UPDATE BOOKS SET old_id='{book[0]}' WHERE id='{book[0]}'")
            cursor.execute(f"""UPDATE BOOKS
            SET id_series='{id}', id='{new_book_id}'
            WHERE id='{book[0]}'""")

    cursor.execute(f"""UPDATE SERIES
    SET id='{id}', full_name='{full_name}', category={category}, kind='{kind}'
    WHERE id='{old_id}';""")

    #Updating authors
    cursor.execute(f"DELETE FROM WROTE WHERE series_id='{id}';")
    for auth_id in author_ids :
        cursor.execute(f"""INSERT INTO WROTE VALUES
        ({auth_id}, '{id}');""")
    
    db.commit()
    return 0

def modif_author(id:int, name:str) :
    cursor.execute(f"SELECT * FROM AUTHORS WHERE full_name='{name}'")
    if len(cursor.fetchall()) != 0 :
        return False
    cursor.execute(f"UPDATE AUTHORS SET full_name='{name}' WHERE id='{id}'")
    db.commit()
    return True

def modif_editor(id:int, name:str) :
    cursor.execute(f"SELECT * FROM EDITORS WHERE full_name='{name}'")
    if len(cursor.fetchall()) != 0 :
        return False
    cursor.execute(f"UPDATE EDITORS SET full_name='{name}' WHERE id='{id}'")
    db.commit()
    return True

def modif_user(id:int, f_name:str, l_name:str, tel:str, mail:str, max_loan_nb:int) :
    cursor.execute(f"""SELECT * FROM USERS WHERE f_name="{f_name}" AND l_name="{l_name}" AND id!={id};""")
    if len(cursor.fetchall()) != 0 :
        return False
    cursor.execute(f"""UPDATE USERS
    SET f_name="{f_name}", l_name="{l_name}", tel='{tel}', mail="{mail}", max_loan_nb={max_loan_nb}
    WHERE id={id};""")
    db.commit()
    return True