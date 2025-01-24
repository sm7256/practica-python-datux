# Realice un programa que pueda gestionar tickets de buses
# las clases a usar seran buses  , conductores
# 1. Un menu iteractivo con las siguiente opciones: agregar bus , agregar ruta a bus 
# registrar horario a bus, agregar conductor , agregar horario a conductor(*) y asignar bus a conductor(**)
# * consideremos que el horario de los conductores solo es a nivel de horas mas no dias ni fechas
# **validar que no haya conductores en ese horario ya asignados

class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = []

    def agregar_horario(self, hora):
        if hora not in self.horarios:
            self.horarios.append(hora)
        else:
            print(f"El conductor {self.nombre} ya tiene asignado el horario {hora}.")

class Bus:
    def __init__(self, id_bus):
        self.id_bus = id_bus
        self.ruta = None
        self.horarios = []
        self.conductores_asignados = []

    def agregar_ruta(self, ruta):
        self.ruta = ruta

    def registrar_horario(self, horario):
        self.horarios.append(horario)

    def asignar_conductor(self, conductor, horario):
        if horario in self.horarios:
            for c in self.conductores_asignados:
                if horario in c.horarios:
                    print(f"El horario {horario} ya está asignado a otro conductor.")
                    return
            self.conductores_asignados.append(conductor)
            conductor.agregar_horario(horario)
        else:
            print(f"El horario {horario} no está registrado para el bus {self.id_bus}.")

class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []

    def agregar_bus(self, bus):
        self.buses.append(bus)

    def agregar_conductor(self, conductor):
        self.conductores.append(conductor)

    def mostrar_menu(self):
        while True:
            print("\nMenú:")
            print("1. Agregar bus")
            print("2. Agregar ruta a bus")
            print("3. Registrar horario a bus")
            print("4. Agregar conductor")
            print("5. Agregar horario a conductor")
            print("6. Asignar bus a conductor")
            print("7. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                id_bus = input("Ingrese el ID del bus: ")
                bus = Bus(id_bus)
                self.agregar_bus(bus)
                print(f"Bus {id_bus} agregado.")
            elif opcion == "2":
                id_bus = input("Ingrese el ID del bus: ")
                ruta = input("Ingrese la ruta del bus: ")
                for bus in self.buses:
                    if bus.id_bus == id_bus:
                        bus.agregar_ruta(ruta)
                        print(f"Ruta {ruta} agregada al bus {id_bus}.")
                        break
                else:
                    print(f"No se encontró el bus con ID {id_bus}.")
            elif opcion == "3":
                id_bus = input("Ingrese el ID del bus: ")
                horario = input("Ingrese el horario del bus: ")
                for bus in self.buses:
                    if bus.id_bus == id_bus:
                        bus.registrar_horario(horario)
                        print(f"Horario {horario} registrado para el bus {id_bus}.")
                        break
                else:
                    print(f"No se encontró el bus con ID {id_bus}.")
            elif opcion == "4":
                nombre = input("Ingrese el nombre del conductor: ")
                conductor = Conductor(nombre)
                self.agregar_conductor(conductor)
                print(f"Conductor {nombre} agregado.")
            elif opcion == "5":
                nombre = input("Ingrese el nombre del conductor: ")
                hora = input("Ingrese el horario del conductor: ")
                for conductor in self.conductores:
                    if conductor.nombre == nombre:
                        conductor.agregar_horario(hora)
                        print(f"Horario {hora} agregado al conductor {nombre}.")
                        break
                else:
                    print(f"No se encontró el conductor con nombre {nombre}.")
            elif opcion == "6":
                id_bus = input("Ingrese el ID del bus: ")
                nombre = input("Ingrese el nombre del conductor: ")
                horario = input("Ingrese el horario: ")
                for bus in self.buses:
                    if bus.id_bus == id_bus:
                        for conductor in self.conductores:
                            if conductor.nombre == nombre:
                                bus.asignar_conductor(conductor, horario)
                                print(f"Conductor {nombre} asignado al bus {id_bus} en el horario {horario}.")
                                break
                        else:
                            print(f"No se encontró el conductor con nombre {nombre}.")
                        break
                else:
                    print(f"No se encontró el bus con ID {id_bus}.")
            elif opcion == "7":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

admin = Admin()
admin.mostrar_menu()
