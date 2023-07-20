import sqlite3

DATABASE_NAME = "copa.db"
#importo y me conecto

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

#creo la tabla
#recorro la lista de tablas, hay una sola
def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS copa(
                id  PRIMARY KEY,
                estadio TEXT NOT NULL,
                partido TEXT NOT NULL,
                precio REAL NOT NULL,
                sector TEXT NOT NULL
            )
        """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
#le agrego los datos que me da el ejercicio
def insert_initial_data():
    data = [
        ("C001", "Buenos Aires Lawn Tennis Club", "Argentina-Lituania", 10000, "Esquina"),
        ("C002", "Buenos Aires Lawn Tennis Club", "Argentina-Lituania", 12000, "Plateas"),
        ("C003", "Buenos Aires Lawn Tennis Club", "Argentina-Lituania", 50000, "Palcos")
        
    ]
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='copa'")
    table_exists = cursor.fetchone()

    if not table_exists:
        # La tabla "copa" no existe, proceder con la inserción de datos
        cursor.executemany("INSERT INTO copa (id, estadio, partido, precio, sector) VALUES (?, ?, ?, ?, ?)", data)


    db.commit()



create_tables()
insert_initial_data()
