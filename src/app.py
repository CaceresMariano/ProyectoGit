from termcolor import cprint

from src.controllers.employees import add_employed, view_employed, update_employed, delete_employed
from src.helpers.helpers import clear_console, sleep_menu
from src.helpers.helpers import mostrar_menu

def run():
    while True:
        clear_console()
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                add_employed()
            case "2":
                view_employed()
            case "3":
                update_employed()
            case "4":
                delete_employed()
            case "0":
                cprint("👋Saliendo del programa...", "magenta", attrs=["bold"])
                break
            case _:  # Este es el "else" de match-case
                cprint("Opción no válida. Intente de nuevo.", "red")
                sleep_menu(2)
