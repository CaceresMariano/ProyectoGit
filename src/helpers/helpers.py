import os
from time import sleep
from typing import Optional

from termcolor import cprint, colored

from src.config.constants import CHECK, NO_CHECK


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


def get_string(message:  str, accept_blank: bool = True) -> str:
    while True:
        data = input(message)
        if not data and not accept_blank:
            cprint("Debe ingresar un valor!", "cyan")
            continue
        return data


def get_int(message: str, accept_blank: bool = True) -> Optional[int]:
    try:
        data = get_string(message, accept_blank)  # código que puede fallar
        if not data and not accept_blank:
            return None
        if not data.isnumeric():
            raise ValueError("Ingrese solo numeros.")
        data = int(data.zfill(8))
        return data
    except ValueError as ex:
        cprint(f"{ex}", "red")
        return get_int(message, accept_blank)


def get_bool(message: str, accept_blank: bool = True) -> Optional[bool]:
    VALID_ARGUMENTS = ("SI", "NO", "S", "N")
    try:
        # código que puede fallar
        data = get_string(message, accept_blank).upper()
        if not data and accept_blank:
            None
        if data not in VALID_ARGUMENTS:
            raise ValueError(
                colored(f"Respuesta Invalidad! Debe colocar {VALID_ARGUMENTS}", "red"))
        value = [CHECK for argument in ("SI", "S") if data == argument]
        return value[0] if value else NO_CHECK
    except ValueError as ex:
        print(f"Error: {ex}")
        return get_bool(message, accept_blank)
