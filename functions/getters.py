#Functions to get the content of tables, for display or selection

from base import *
import numpy as np
import time

#Display getters

def get_users(search=None) :
    if search is None or search[1] == '' :
        cursor.execute(f"SELECT id, f_name, l_name, tel, mail, loan_nb, max_loan_nb FROM Users;")
    else :
        cursor.execute(f"SELECT id, f_name, l_name, tel, mail, loan_nb, max_loan_nb FROM Users WHERE {search[0][0]}_name LIKE '%{search[1]}%';")

    table = cursor.fetchall()
    newtable = []
    for line in table :
        today = time.strftime("%Y-%m-%d")
        cursor.execute(f"SELECT COUNT() FROM Loans WHERE end_date IS NOT NULL AND id_user='{line[0]}' AND end_date<'{today}';")
        late_loans, = cursor.fetchone()
        newtable.append(line[:5]+(f"{line[5]}/{line[6]}",late_loans))
    return np.asarray(newtable, dtype=str).tolist()

def get_books(search=None) : # Restrictions have to be done on a low level to manipulate less data
    if search is None or search[1] == '' :
        cursor.execute(f"""SELECT b.id, s.full_name, b.vol_num, b.vol_name, b.ex_num, s.category, s.kind, b.editor, b.buy_date, b.dispo, b.old_id
        FROM
            (SELECT b.id, b.vol_num, b.vol_name, b.ex_num, e.full_name AS editor, b.buy_date, b.dispo, b.id_series, b.old_id
            FROM BOOKS AS b LEFT JOIN EDITORS AS e ON b.id_editor=e.id)
        AS b JOIN
            (SELECT s.full_name, s.id, c.name AS category, s.kind
            FROM Series AS s LEFT JOIN Categories AS c ON c.id=s.category)
        AS s ON b.id_series=s.id;""")
    
    elif search[0] == "Id" :    #Searching a book by its Id
        cursor.execute(f"""SELECT b.id, s.full_name, b.vol_num, b.vol_name, b.ex_num, s.category, s.kind, b.editor, b.buy_date, b.dispo, b.old_id
        FROM
            (SELECT b.id, b.vol_num, b.vol_name, b.ex_num, e.full_name AS editor, b.buy_date, b.dispo, b.id_series, b.old_id
            FROM BOOKS AS b LEFT JOIN EDITORS AS e ON b.id_editor=e.id
            WHERE b.id='{search[1]}')
        AS b JOIN
            (SELECT s.full_name, s.id, c.name AS category, s.kind
            FROM Series AS s LEFT JOIN Categories AS c ON c.id=s.category)
        AS s ON b.id_series=s.id;""")

    elif search[0] == "Series" :  # Searching for a series
        cursor.execute(f"""SELECT b.id, s.full_name, b.vol_num, b.vol_name, b.ex_num, s.category, s.kind, b.editor, b.buy_date, b.dispo, b.old_id
        FROM 
            (SELECT b.id, b.vol_num, b.vol_name, b.ex_num, e.full_name AS editor, b.buy_date, b.dispo, b.id_series, b.old_id
            FROM BOOKS AS b LEFT JOIN EDITORS AS e ON b.id_editor=e.id)
        AS b JOIN
            (SELECT s.full_name, s.id, c.name AS category, s.kind
            FROM
                (SELECT * FROM SERIES WHERE full_name LIKE '%{search[1]}%')
            AS s LEFT JOIN Categories AS c ON c.id=s.category)
        AS s ON b.id_series=s.id;""")

    
    elif search[0] == "Category" :  # Searching for a category
        cursor.execute(f"""SELECT b.id, s.full_name, b.vol_num, b.vol_name, b.ex_num, s.category, s.kind, b.editor, b.buy_date, b.dispo, b.old_id
        FROM 
            (SELECT b.id, b.vol_num, b.vol_name, b.ex_num, e.full_name AS editor, b.buy_date, b.dispo, b.id_series, b.old_id
            FROM BOOKS AS b LEFT JOIN EDITORS AS e ON b.id_editor=e.id)
        AS b JOIN
            (SELECT s.full_name, s.id, c.name AS category, s.kind 
            FROM SERIES AS s JOIN
                (SELECT * FROM Categories WHERE name LIKE '%{search[1]}%')
            AS c ON c.id=s.category)
        AS s ON b.id_series=s.id;""")
    
    elif search[0] == "Editor" :  # Searching for an editor
        cursor.execute(f"""SELECT b.id, s.full_name, b.vol_num, b.vol_name, b.ex_num, s.category, s.kind, b.editor, b.buy_date, b.dispo, b.old_id
        FROM 
            (SELECT b.id, b.vol_num, b.vol_name, b.ex_num, e.full_name AS editor, b.buy_date, b.dispo, b.id_series, b.old_id
            FROM BOOKS AS b JOIN 
                (SELECT * FROM EDITORS WHERE full_name LIKE '%{search[1]}%')
            AS e ON b.id_editor=e.id)
        AS b JOIN
            (SELECT s.full_name, s.id, c.name AS category, s.kind
            FROM Series AS s LEFT JOIN Categories AS c ON c.id=s.category)
        AS s ON b.id_series=s.id;""")

    #TODO : cast disponibility to bool
    
    return np.asarray(cursor.fetchall(), dtype=str).tolist()

def get_loans(search=None) :
    if search is None or search[1] == '' :
        cursor.execute(f"""SELECT t2.f_name, t2.l_name, t2.id_book, t1.full_name, t1.vol_num, t2.start_date, t2.end_date FROM
            (SELECT s.full_name, b.vol_num, b.id FROM Books AS b JOIN Series AS s ON s.id=b.id_series)
        AS t1 JOIN
            (SELECT u.f_name, u.l_name, l.id_book, l.start_date, l.end_date FROM Loans AS l JOIN Users AS u ON l.id_user=u.id)
        AS t2 ON t1.id=t2.id_book;""")

    elif search[0] == "First name" :
        cursor.execute(f"""SELECT t2.f_name, t2.l_name, t2.id_book, t1.full_name, t1.vol_num, t2.start_date, t2.end_date FROM
            (SELECT s.full_name, b.vol_num, b.id FROM Books AS b JOIN Series AS s ON s.id=b.id_series)
        AS t1 JOIN
            (SELECT u.f_name, u.l_name, l.id_book, l.start_date, l.end_date FROM Loans AS l JOIN
                (SELECT * FROM USERS WHERE f_name LIKE '%{search[1]}%')
            AS u ON l.id_user=u.id)
        AS t2 ON t1.id=t2.id_book;""")

    elif search[0] == "Last name" :
        cursor.execute(f"""SELECT t2.f_name, t2.l_name, t2.id_book, t1.full_name, t1.vol_num, t2.start_date, t2.end_date FROM
            (SELECT s.full_name, b.vol_num, b.id FROM Books AS b JOIN Series AS s ON s.id=b.id_series)
        AS t1 JOIN
            (SELECT u.f_name, u.l_name, l.id_book, l.start_date, l.end_date FROM Loans AS l JOIN
                (SELECT * FROM Users WHERE l_name LIKE '%{search[1]}%')
            AS u ON l.id_user=u.id)
        AS t2 ON t1.id=t2.id_book;""")

    elif search[0] == "Book name" :
        cursor.execute(f"""SELECT t2.f_name, t2.l_name, t2.id_book, t1.full_name, t1.vol_num, t2.start_date, t2.end_date FROM
            (SELECT s.full_name, b.vol_num, b.id FROM Books AS b JOIN
                (SELECT * FROM Series WHERE full_name LIKE '%{search[1]}%')
            AS s ON s.id=b.id_series)
        AS t1 JOIN
            (SELECT u.f_name, u.l_name, l.id_book, l.start_date, l.end_date FROM Loans AS l JOIN Users AS u ON l.id_user=u.id)
        AS t2 ON t1.id=t2.id_book;""")
    
    return np.asarray(cursor.fetchall(), dtype=str).tolist()

def get_series(search=None) :
    if search is None or search[1] == '' :
        cursor.execute(f"""SELECT s.id, s.full_name, c.name, s.kind FROM SERIES AS s LEFT JOIN CATEGORIES AS c ON s.category=c.id;""")

    elif search[0] == "ID" :
        cursor.execute(f"""SELECT s.id, s.full_name, c.name, s.kind FROM SERIES AS s LEFT JOIN CATEGORIES AS c ON s.category=c.id
        WHERE s.id LIKE '%{search[1]}%';""")

    elif search[0] == "Full name" :
        cursor.execute(f"""SELECT s.id, s.full_name, c.name, s.kind FROM SERIES AS s LEFT JOIN CATEGORIES AS c ON s.category=c.id
        WHERE s.full_name LIKE '%{search[1]}%';""")

    elif search[0] == "Authors" :  # Searching for an author
        cursor.execute(f"""SELECT s.id, s.full_name, c.name, s.kind FROM
                (SELECT id, full_name, kind, category FROM SERIES JOIN
                    (SELECT series_id FROM WROTE JOIN AUTHORS ON author_id=id WHERE full_name LIKE '%{search[1]}%')
                ON id=series_id)
            AS s LEFT JOIN CATEGORIES AS c ON s.category=c.id;""")

    table = cursor.fetchall()

    #Converting authors id into names
    res = []
    for v in table :
        cursor.execute(f"""SELECT full_name FROM AUTHORS JOIN WROTE ON id=author_id WHERE series_id='{v[0]}';""")
        v = list(v)
        line = v[:2]+[', '.join([name for (name,) in cursor.fetchall()])]+v[2:]
        line = list(map(str, line))
        res.append(line)
    return np.asarray(res, dtype=str).tolist()

def get_authors(search=None) :
    if search is None or search[1] == '' :
        cursor.execute(f"SELECT * FROM Authors;")
    else :
        cursor.execute(f"SELECT * FROM Authors WHERE full_name LIKE '%{search[1]}%';")
    return np.asarray(cursor.fetchall(), dtype=str).tolist()

def get_editors(search=None) :
    if search is None or search[1] == '' :
        cursor.execute(f"SELECT * FROM Editors;")
    else :
        cursor.execute(f"SELECT * FROM Editors WHERE full_name LIKE '%{search[1]}%';")
    return np.asarray(cursor.fetchall(), dtype=str).tolist()

#Selection getters

def get_auths_select() :
    cursor.execute("SELECT * FROM AUTHORS")
    return {name:id for (id, name) in cursor.fetchall()}

def get_cats_select() :
    cursor.execute("SELECT * FROM CATEGORIES")
    return {name:id for (id, name) in cursor.fetchall()}

def get_edits_select() :
    cursor.execute("SELECT * FROM EDITORS")
    return {name:id for (id, name) in cursor.fetchall()}

def get_series_select() :
    cursor.execute("SELECT id, full_name FROM SERIES")
    return {full_name:id for (id, full_name) in cursor.fetchall()}

def get_books_select() :
    cursor.execute("SELECT id FROM BOOKS")
    return [line[0] for line in cursor.fetchall()]

def get_users_select() :
    cursor.execute("SELECT id, f_name, l_name FROM USERS")
    return {f"{f_name} {l_name}":id for (id, f_name, l_name) in cursor.fetchall()}

def get_loans_select() :
    cursor.execute("SELECT DISTINCT id, f_name, l_name FROM USERS JOIN LOANS ON id=id_user")
    users = {f"{f_name} {l_name}":id for (id, f_name, l_name) in cursor.fetchall()}
    cursor.execute("SELECT id_user, id_book FROM LOANS")
    table = cursor.fetchall()
    loans = {user:[] for (user, _) in table}
    for (user, book) in table :
        loans[user].append(book)
    return users, loans

#Raw data getter

def get_book_data(book_id:str) :
    cursor.execute(f"""SELECT b.id, b.full_name, b.vol_num, b.vol_name, e.full_name, b.buy_date
    FROM
        (SELECT b.id, s.full_name, b.vol_num, b.vol_name, b.id_editor, b.buy_date
        FROM BOOKS AS b JOIN SERIES AS s ON b.id_series=s.id
        WHERE b.id='{book_id}')
    AS b LEFT JOIN EDITORS AS e ON b.id_editor=e.id""")
    return cursor.fetchone()