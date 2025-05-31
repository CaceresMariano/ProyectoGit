import json
import os

# Ruta relativa desde src/data/ hasta output/employees.json
FILE_PATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../../output/employees.json"))

# Base de datos en memoria
employees_db: list[dict] = []

# Cargar empleados desde el archivo JSON si existe


def load_employees():
    global employees_db
    if os.path.exists(FILE_PATH):
        if os.path.getsize(FILE_PATH) > 0:  # solo si tiene contenido
            with open(FILE_PATH, "r", encoding="utf-8") as f:
                employees_db.extend(json.load(f))
        else:
            employees_db = []
# Guardar empleados en el archivo JSON


def save_employees():
    # Asegurarse de que la carpeta output existe
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(employees_db, f, indent=4, ensure_ascii=False)
