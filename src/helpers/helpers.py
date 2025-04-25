import os
from time import sleep

from termcolor import cprint


def sleep_menu(time: int = 2):
    sleep(time)


def clear_console():
    if os.name == "nt":  # Sistema Windows
        os.system("cls")
    else:
        os.system("clear")  # Sistema Linux o Mac


def mostrar_menu():
    cprint("\n📋  MENÚ DE EMPLEADOS", "cyan", attrs=["bold"])
    cprint("1️⃣  ➕ Agregar empleado", "green")
    cprint("2️⃣  🔍 Consultar empleado", "yellow")
    cprint("3️⃣  📝 Modificar empleado", "blue")
    cprint("4️⃣  ❌ Eliminar empleado", "red")
    cprint("0️⃣  🚪 Salir", "magenta")
