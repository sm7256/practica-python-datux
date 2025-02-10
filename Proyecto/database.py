import sqlite3

def conectar_db():
    conn = sqlite3.connect('mi_base_de_datos.db')
    cursor = conn.cursor()
    return conn, cursor

