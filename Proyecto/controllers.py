from database import conectar_db
from models import Producto

def agregar_producto(nombre, precio):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", (nombre, precio))
    conn.commit()
    conn.close()
