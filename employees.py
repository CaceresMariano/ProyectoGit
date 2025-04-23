from typing import Optional

from data import employees_db
from utils import clear_console, sleep_menu
from constants import CHEQUEADO, NO_CHEQUEADO


def view_employed():
    clear_console()
    if not __check_employee():
       return
    employee = __find_employee()
    if employee is None:
        return
    print(employee)


def add_employed():
    clear_console()
    name: str = input("Nombre: ")
    last_name: str = input("Apellido: ")
    dni: str = input("DNI: ").zfill(8)
    position: str = input("Puesto: ")
    check: str = input("Apto fisico con estudios (si), sin estudios (no): ")
    employee = {
        "nombre": name,
        "apellido": last_name,
        "dni": f"{dni[:2]}.{dni[2:5]}.{dni[5:]}",
        "puesto": position,
        "apto": CHEQUEADO if check.lower() == "si" else NO_CHEQUEADO
    }
    employees_db.append(employee)
    print(f"Empleado agregado!")
    sleep_menu(1)

def update_employed():
    clear_console()
    if not __check_employee():
       return
    employee = __find_employee()
    if employee is None:
        return
    new_name: str = input("Ingrese el nuevo Nombre: ")
    new_LastName: str = input("Ingrese el nuevo Apellido: ")
    new_dni: str = input("Ingrese el nuevo DNI: ").zfill(8)
    new_position: str = input("Ingrese el nuevo puesto: ")
    new_check: str = input(
        "Ingrese el nuevo estado con estudios (si), sin estudios (no): ")
    if new_name:
        employee["nombre"] = new_name.title()
    if new_LastName:
        employee["apellido"] = new_LastName.title()
    if new_dni:
        employee["dni"] = f"{new_dni[:2]}.{new_dni[2:5]}.{new_dni[5:]}"
    if new_position:
        employee["puesto"] = new_position
    if new_check:
        employee["apto"] = CHEQUEADO if new_check.lower(
        ) == "si" else NO_CHEQUEADO

    sleep_menu(1)

def delete_employed():
    clear_console()
    if not __check_employee():
       return
    view_employed()
    option = int(
        input(f"Elija el numero del empleado a eliminar [1- {len(employees_db)}]: "))
    employees_db.pop(option - 1)
    sleep_menu(1)


def __check_employee():
    if not employees_db:
        print("No se han cargado empleados en los registros")
        sleep_menu(1)
        return False
    return True


def __find_employee() -> Optional[dict]:
    view_employed()
    option = int(
        input(f"Elija un empleado de la lista [1- {len(employees_db)}]: "))
    for index, employees in enumerate(employees_db, start=1):
        if option == index:
            return employees
    print("Empleado no encontrado")
