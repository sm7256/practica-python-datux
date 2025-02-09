from controllers import agregar_producto
from views import mostrar_menu

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            agregar_producto(nombre, precio)
            print("Producto agregado exitosamente.")
        elif opcion == '2':
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
