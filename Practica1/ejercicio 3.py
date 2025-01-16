# Escribe un programa que pida un numero entero y determine si es par o impar 
# Solicitar un número entero al usuario
numero = int(input("Por favor introduce un numero entero: "))

# Verificar si el número es par o impar
if numero % 2 == 0:
    print("El numero es par.")
else:
    print("El numero es impar.")
