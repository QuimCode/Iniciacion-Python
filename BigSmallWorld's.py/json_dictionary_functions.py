import os
import json

def register_json_data(name, age, gmail, password, filename="register.json"):

    try:
        directory = "BigSmallWorld's.py/data"
        os.makedirs(directory, exist_ok=True)  # Crear el directorio si no existe
        filepath = os.path.join(directory, filename)  # Ruta completa del archivo JSON

        with open(filepath, "r") as file:
            data_user = json.load(file)
    except FileNotFoundError:
        data_user = {}

    user_id = len(data_user) + 1
    data_user[user_id] = {
        "name" : name,
        "age" : int(age),
        "gmail" : gmail,
        "password" : password
    }

    with open(filepath, "w") as file:
        json.dump(data_user, file, indent=4)
    print("Welcome to BigSmallWorld!")

