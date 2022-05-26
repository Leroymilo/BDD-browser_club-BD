#Functions to add tuples in the tables of the database

from base import *

def add_user(f_name:str, l_name:str, tel:str, mail:str, max_loan_nb:int) :
    cursor.execute(f"""SELECT * FROM USERS WHERE f_name="{f_name}" AND l_name="{l_name}";""")
    if len(cursor.fetchall()) != 0 :
        return False
    cursor.execute("SELECT MAX(id) FROM USERS;")
    result, = cursor.fetchone()
    if result is None :
        user_id = 1
    else :
        user_id = result+1
    cursor.execute(f"""INSERT INTO USERS VALUES ({user_id}, "{f_name}", "{l_name}", '{tel}', "{mail}", 0, {max_loan_nb});""")
    db.commit()
    return True

def add_author(full_name:str) :
    cursor.execute(f"""SELECT * FROM AUTHORS WHERE full_name="{full_name}";""")
    if len(cursor.fetchall()) != 0 :
        return False
    cursor.execute("SELECT MAX(id) FROM AUTHORS;")
    result, = cursor.fetchone()
    if result is None :
        aut_id = 1
    else :
        aut_id = result+1
    cursor.execute(f"""INSERT INTO AUTHORS VALUES ({aut_id}, "{full_name}");""")
    db.commit()
    return True
    
def add_editor(full_name:str) :
    cursor.execute(f"""SELECT * FROM EDITORS WHERE full_name="{full_name}";""")
    if len(cursor.fetchall()) != 0 :
        return False
    cursor.execute("SELECT MAX(id) FROM EDITORS;")
    result, = cursor.fetchone()
    if result is None :
        edit_id = 1
    else :
        edit_id = result+1
    cursor.execute(f"""INSERT INTO EDITORS VALUES ({edit_id}, "{full_name}");""")
    db.commit()
    return True

def add_category(id:int, text:str) :
    cursor.execute(f"INSERT INTO CATEGORIES VALUES ({id}, '{text}');")

def add_series(id:str, full_name:str, category:int, kind:str, author_ids:list[int]) :
    cursor.execute(f"SELECT * FROM SERIES WHERE id='{id}';")
    if len(cursor.fetchall()) != 0 :
        return False
    cursor.execute(f"""SELECT * FROM SERIES WHERE full_name="{full_name}";""")
    if len(cursor.fetchall()) != 0 :
        return False
    cursor.execute(f"""INSERT INTO SERIES VALUES
    ('{id}', "{full_name}", {category}, '{kind}');""")
    for auth_id in author_ids :
        cursor.execute(f"""INSERT INTO WROTE VALUES
        ({auth_id}, '{id}');""")
    db.commit()
    return True

def add_book(series:str, vol_num:int, vol_name:str, editor_id:int, buy_date:str, old_id='NULL') :
    # series is the 3 char id of the series.
    cursor.execute(f"SELECT COUNT(*) FROM BOOKS WHERE id_series='{series}' AND vol_num={vol_num};")
    ex_num = cursor.fetchone()[0]+1
    cursor.execute(f"SELECT category FROM SERIES WHERE id='{series}';")
    category = str(cursor.fetchone()[0]).rjust(2, '0')
    id = category+series+str(vol_num).rjust(2, '0')+str(ex_num)
    if old_id != 'NULL' :
        old_id = "'"+old_id+"'"
    if editor_id is None :
        editor_id = 'NULL'
    cursor.execute(f"""INSERT INTO BOOKS VALUES ('{id}', '{series}', {vol_num}, "{vol_name}", {ex_num}, {editor_id}, '{buy_date}', TRUE, {old_id});""")
    db.commit()

def add_loan(id_book:str, id_user:int, start_date:str, end_date:str) :
    cursor.execute(f"SELECT dispo FROM BOOKS WHERE id='{id_book}';")
    dispo, = cursor.fetchone()
    cursor.execute(f"SELECT max_loan_nb-loan_nb FROM USERS WHERE id={id_user};")
    in_debt = cursor.fetchone()[0]<=0
    if dispo and not in_debt:
        cursor.execute(f"INSERT INTO LOANS VALUES ('{id_book}', {id_user}, '{start_date}', '{end_date}');")
        cursor.execute(f"UPDATE BOOKS SET dispo=FALSE WHERE id='{id_book}';")
        cursor.execute(f"UPDATE USERS SET loan_nb=loan_nb+1 WHERE id={id_user};")
        db.commit()
        return 0
    elif not dispo :
        return 1
        print(f"book {id_book} is not available")
    elif in_debt :
        return 2
        print(f"user {id_user} has too many loans")