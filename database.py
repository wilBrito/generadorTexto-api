import sqlite3

def db_connection():
    """
    OBJ: Establecer conexión con la base de datos SQLite creada
    """
    conn = sqlite3.connect('historialTextos.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_db():
    """
    OBJ: Creación de la base de datos, tabla historial donde se almacenaran los textos propuestos por usuario y los generados por IA
    """
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS historial (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   prompt TEXT NOT NULL,
                   texto_generado TEXT NOT NULL
                   )
    ''')
    conn.commit()
    conn.close()
