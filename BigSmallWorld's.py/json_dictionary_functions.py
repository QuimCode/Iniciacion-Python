import os
import json
#=================================================================================

#=================================================================================
#Funcion dedicada a la creacion/verificacion de la carpeta y el archivo JSON donde se guardaran los datos de los usuarios
#Recibe un directorio y un nombre de archivo, si no existe lo crea y si existe lo abre para agregar los datos de los usuarios
#Si el archivo no existe se crea un diccionario vacio y se guarda en el archivo JSON
#Si el archivo existe se carga el diccionario existente y se le agrega el nuevo usuario

def register_json_data(name, age, gmail, password, filename="register.json"):
    try:
        directory = "BigSmallWorld's.py/data"
        os.makedirs(directory, exist_ok=True) 
        filepath = os.path.join(directory, filename)  

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
    print("\tYour data has been saved successfully!")
#=================================================================================
