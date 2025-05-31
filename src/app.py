from termcolor import cprint

from src.controllers import crud
from src.data.data import load_employees
from src.helpers.helpers import clear_console, sleep_menu
from src.helpers.helpers import mostrar_menu


def run():
    load_employees()
    while True:
        clear_console()
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                crud.add_employed()
            case "2":
                crud.view_employed()
            case "3":
                crud.update_employed()
            case "4":
                crud.delete_employed()
            case "0":
                cprint("👋Saliendo del programa...", "magenta", attrs=["bold"])
                break
            case _:  # Este es el "else" de match-case
                cprint("Opción no válida. Intente de nuevo.", "red")
                sleep_menu(2)
