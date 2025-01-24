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
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS historial (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   prompt TEXT NOT NULL,
                   texto_generado TEXT NOT NULL
                   )
    """)
    conn.commit()
    conn.close()

def guardar_respuesta(prompt: str, texto_generado: str):
    """
    OBJ: Función que guarda los textos en la base de datos
    """
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO historial (prompt, texto_generado) VALUES (?,?)", (prompt,texto_generado))
    conn.commit()
    conn.close()

def ver_historial()->list:
    """
    OBJ: Función que devuelve todos los datos almacenados en la tabla historial en forma de Lista de tuplas
    """
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM historial")
    filas = cursor.fetchall()
    conn.close()
    return filas

create_db()

