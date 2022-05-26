#Functions to modifies tuples of the database

from base import *

def modif_series(id:str, old_name:str, full_name:str, category:int, kind:str, author_ids:list[int]) :
    if old_name != full_name :
        cursor.execute(f"SELECT * FROM SERIES WHERE full_name='{full_name}';")
        if len(cursor.fetchall()) != 0 :
            return False
    cursor.execute(f"""UPDATE SERIES SET
    full_name='{full_name}', category={category}, kind='{kind}' WHERE id='{id}';""")
    cursor.execute(f"DELETE FROM WROTE WHERE id_series='{id}';")
    for auth_id in author_ids :
        cursor.execute(f"""INSERT INTO WROTE VALUES
        ({auth_id}, '{id}');""")
    db.commit()
    return True