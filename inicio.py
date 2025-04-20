import os
from time import sleep
from termcolor import cprint


def mostrar_menu():
    cprint("\n=== MENÚ DE EMPLEADOS ===", "cyan", attrs=["bold"])
    cprint("1. Agregar empleado", "green")
    cprint("2. Consultar empleado", "yellow")
    cprint("3. Modificar empleado", "blue")
    cprint("4. Eliminar empleado", "red")
    cprint("0. Salir", "magenta")


def menu():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "0":
                cprint("Saliendo del programa...", "magenta", attrs=["bold"])
                break
            case _:  # Este es el "else" de match-case
                cprint("Opción no válida. Intente de nuevo.", "red")
                sleep(2)                
