from typing import Optional

from src.data.data import employees_db
from src.helpers.helpers import clear_console, sleep_menu, get_string, get_int
from src.config.constants import CHEQUEADO, NO_CHEQUEADO


def view_employed():
    if not __check_employee():
        return print("No hay mas empleados en la base de datos.")
    employee = __find_employee()
    if employee is None:
        return
    print(employee)
    sleep_menu(2)


def add_employed():
    clear_console()
    name: str = get_string("Nombre: ", accept_blank=False)
    last_name: str = get_string("Apellido: ", accept_blank=False)
    dni: str = get_int("DNI: ", accept_blank=False)
    position: str = get_string("Puesto: ", accept_blank=False)
    check: str = input("Apto fisico con estudios (si), sin estudios (no): ")
    employee = {
        "nombre": name,
        "apellido": last_name,
        "dni": dni,
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
    print("Datos del empleado actualizados con exito.")
    sleep_menu(1)


def delete_employed():
    if __check_employee():
        list_employeed()
        option = int(
            input(f"Elija el numero del empleado a eliminar [1- {len(employees_db)}]: "))
        register_deleted = employees_db.pop(option - 1)
        if register_deleted:
            print(
                f"El empleado {register_deleted["nombre"]} {register_deleted["apellido"]} fue eliminado con exito.")
    sleep_menu(2)


def __check_employee():
    clear_console()
    if not employees_db:
        print("No se han cargado empleados en los registros")
        sleep_menu(2)
        return False
    return True


def list_employeed():
    __check_employee()
    for index, employees in enumerate(employees_db, start=1):
        print(f"{index}- {employees["nombre"]}, {employees["apellido"]}")


def __find_employee() -> Optional[dict]:
    list_employeed()
    option = int(
        input(f"Elija un empleado de la lista [1- {len(employees_db)}]: "))
    for index, employees in enumerate(employees_db, start=1):
        if option == index:
            return employees
    print("Empleado no encontrado")
