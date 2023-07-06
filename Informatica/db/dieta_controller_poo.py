from db_dietas import get_db
from clase_dietas import Dieta


def insert_dieta(id, Restriction, Restriccion, USD):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO dieta (id, Restriction, Restriccion, USD) \
    VALUES ( ?, ?, ?, ?)"
    cursor.execute(statement, [id, Restriction, Restriccion, USD])
    db.commit()
    return True

def update_dieta(id, Restriction, Restriccion, USD):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE dietas SET Restriiction = ?, Restriccion = ?, USD= ?\
    WHERE id = ?"
    cursor.execute(statement, [Restriction, Restriccion, USD, id])
    db.commit()
    return True

def get_dietas():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, Restriction, Restriccion, USD FROM dietas"
    cursor.execute(query)
    dieta_list = cursor.fetchall()
    list_of_dietas=[]
    for rdieta in dieta_list:
        id = dieta[0]
        Restriction = dieta[1]
        Restriccion = dieta[2]
        USD = dieta[3]
        dieta_to_add = Dieta(id, Restriction, Restriccion, USD)
        list_of_dietas.append(dieta_to_add)
    return list_of_dietas
    
def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, Restriccion, USD FROM dietas \
    WHERE id = ?"
    cursor.execute(statement, [id])
    single_dieta = cursor.fetchone()
    id = single_dieta[0]
    Restriccion = single_dieta[2]
    USD = single_dieta[3]
    dieta = Dieta (id, Restriccion, USD) 
    return dieta.serialize.details()
