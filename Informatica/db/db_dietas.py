import sqlite3
DATABASE_NAME = "dieta.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS dieta(
                id INTEGER PRIMARY KEY,
                restriction TEXT NOT NULL,
                restriccion INTEGER NOT NULL,
                USD REAL NOT NULL
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
