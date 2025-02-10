from controllers import agregar_producto, obtener_productos
from views import mostrar_menu

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == '1':  # Agregar producto
            nombre = input("Ingrese el nombre del producto: ")
            try:
                precio = float(input("Ingrese el precio del producto: "))
                agregar_producto(nombre, precio)
                print("✅ Producto agregado exitosamente.")
            except ValueError:
                print("❌ Error: El precio debe ser un número.")
        elif opcion == '2':  # Ver productos
            productos = obtener_productos()
            if productos:
                print("\n📋 Lista de productos:")
                for producto in productos:
                    print(f"🆔 ID: {producto[0]}, 📌 Nombre: {producto[1]}, 💰 Precio: {producto[2]}")
            else:
                print("⚠️ No hay productos registrados.")
        elif opcion == '3':  # Salir
            print("👋 Saliendo...")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()

