from typing import Optional


class EmployeesModel():
    def __init__(self, name: str, last_name: str, dni: str, position: str, check: Optional[bool]):
        self.nombre: str = name
        self.apellido: str = last_name
        self.dni: str = dni
        self.puesto: str = position
        self.apto: Optional[bool] = check

    def data_employee(self) -> dict:
        return self.__dict__.copy()
