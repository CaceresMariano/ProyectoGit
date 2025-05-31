from typing import Optional

from src.data.data import employees_db, save_employees
from src.data.models.employees_model import EmployeesModel
from src.helpers.helpers import clear_console, sleep_menu, get_string, get_int, get_bool


class EmployeesController():
    def view_employed(self):
        if not self.__check_employee():
            return print("No hay mas empleados en la base de datos.")
        employee = self.__find_employee()
        if employee is None:
            return
        print(employee)
        sleep_menu(2)

    def add_employed(self):
        clear_console()
        name: str = get_string("Nombre: ", accept_blank=False)
        last_name: str = get_string("Apellido: ", accept_blank=False)
        dni: str = get_int("DNI: ", accept_blank=False)
        position: str = get_string("Puesto: ", accept_blank=False)
        check: str = get_bool(
            "Apto fisico con estudios (si), sin estudios (no): ", accept_blank=False)
        employee = EmployeesModel(name, last_name, dni, position, check)
        employees_db.append(employee.data_employee())
        save_employees()
        print(f"Empleado agregado!")
        sleep_menu(1)

    def update_employed(self):
        clear_console()
        if not self.__check_employee():
            return
        employee = self.__find_employee()
        if employee is None:
            return
        employee["nombre"] = get_string(
            "Ingrese el nuevo Nombre: ") or employee["nombre"]
        employee["apellido"] = get_string(
            "Ingrese el nuevo Apellido: ") or employee["apellido"]
        employee["dni"] = get_int("Ingrese el nuevo DNI: ") or employee["dni"]
        employee["puesto"] = get_string(
            "Ingrese el nuevo puesto: ") or employee["puesto"]
        employee["apto"] = get_bool(
            "Ingrese el nuevo estado con estudios (si), sin estudios (no): ") or employee["apto"]
        print("Datos del empleado actualizados con exito.")
        save_employees()
        sleep_menu(1)

    def delete_employed(self):
        if self.__check_employee():
            self.list_employeed()
            option = get_int(
                f"Elija el numero del empleado a eliminar [1- {len(employees_db)}]: ",
                accept_blank=True
            )
            register_deleted = employees_db.pop(option - 1)
            if register_deleted:
                print(
                    f"El empleado {register_deleted["nombre"]} {register_deleted["apellido"]} fue eliminado con exito.")
        save_employees()
        sleep_menu(2)

    def __check_employee(self):
        clear_console()
        if not employees_db:
            print("No se han cargado empleados en los registros")
            sleep_menu(2)
            return False
        return True

    def list_employeed(self):
        self.__check_employee()
        for index, employees in enumerate(employees_db, start=1):
            print(f"{index}- {employees["nombre"]}, {employees["apellido"]}")

    def __find_employee(self) -> Optional[dict]:
        self.list_employeed()
        option = get_int(
            f"Elija un empleado de la lista [1- {len(employees_db)}]: ",
            accept_blank=False
        )
        for index, employees in enumerate(employees_db, start=1):
            if option == index:
                return employees
        print("Empleado no encontrado")
