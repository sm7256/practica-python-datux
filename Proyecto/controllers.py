from database import conectar_db

def agregar_producto(nombre, precio):
    conn, cursor = conectar_db()
    
    cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", (nombre, precio))
    
    conn.commit()  # Guardar cambios
    conn.close()   # Cerrar conexión
def obtener_productos():
    conn, cursor = conectar_db()
    
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    
    conn.close()  # Cerrar conexión
    return productos
