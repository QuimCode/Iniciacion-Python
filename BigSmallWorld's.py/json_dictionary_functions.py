import os
import json
#=================================================================================

#=================================================================================
#Funcion dedicada a la creacion/verificacion de la carpeta y el archivo JSON donde se guardaran los datos de los usuarios
#Recibe un directorio y un nombre de archivo, si no existe lo crea y si existe lo abre para agregar los datos de los usuarios
#Si el archivo no existe se crea un diccionario vacio y se guarda en el archivo JSON
#Si el archivo existe se carga el diccionario existente y se le agrega el nuevo usuario

def register_json_userData(name, age, gmail, password, filename="register.json"):
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

#=================================================================================
#Funcion dedicada a la creacion/verificacion de la carpeta y el archivo JSON donde se guardaran los datos de los usuarios
#Recibe un directorio y un nombre de archivo, si no existe lo crea y si existe lo abre para agregar los datos de los usuarios
#Si el archivo no existe se crea un diccionario vacio y se guarda en el archivo JSON
#Si el archivo existe se carga el diccionario existente y se le agrega el nuevo usuario

def open_json_userData(filename="BigSmallWorld's.py/data/register.json"):
    try:
        if os.path.exists(filename):
            with open(filename, "r") as file:
                return json.load(file) 
        else:
            return {} 
    except FileNotFoundError:
        print("The file does not exist.")
        return {}
    
#=================================================================================

def register_json_productData(user_id, name, price, description, filename="products.json"):
    try:
        directory = "BigSmallWorld's.py/data"
        os.makedirs(directory, exist_ok=True) 
        filepath = os.path.join(directory, filename)  

        with open(filepath, "r") as file:
            data_product = json.load(file)
    except FileNotFoundError:
        data_product = {}

    product_id = len(data_product) + 1
    data_product[product_id] = {
        "user_id": user_id,  
        "name": name,
        "price": float(price),
        "description": description
    }

    with open(filepath, "w") as file:
        json.dump(data_product, file, indent=4)
    print("\tYour product has been saved successfully!")


def json_search_product(filename="BigSmallWorld's.py/data/products.json"):
    try:
        if os.path.exists(filename):
            with open(filename, "r") as file:
                data_product = json.load(file)
        else:
            print("No products have been registered yet.")
            return

        search_name = input("Enter the name of the product to search: ").capitalize()

        found = False
        for product_id, product_data in data_product.items():
            if product_data["name"] == search_name:
                print(f"\nProduct found (ID: {product_id}):")
                print(f"Name: {product_data['name']}")
                print(f"Price: {product_data['price']}")
                print(f"Description: {product_data['description']}")
                print(f"Added by User ID: {product_data['user_id']}")
                found = True
                break

        if not found:
            print("\nProduct not found.")

    except Exception as e:
        print(f"An error occurred while searching for the product: {e}")


def json_delete_product(filename="BigSmallWorld's.py/data/products.json"):
    try:
        if os.path.exists(filename):
            with open(filename, "r") as file:
                data_product = json.load(file)
        else:
            print("No products have been registered yet.")
            return

        print("\nAvailable products:")
        for product_id, product_data in data_product.items():
            print(f"ID: {product_id} | Name: {product_data['name']} | Price: {product_data['price']}")

        product_id = input("\nEnter the ID of the product to delete: ")

        if product_id in data_product:
            confirm = input(f"Are you sure you want to delete the product '{data_product[product_id]['name']}'? (y/n): ").lower()
            if confirm == "y":
                del data_product[product_id] 


                with open(filename, "w") as file:
                    json.dump(data_product, file, indent=4)
                print("\nProduct deleted successfully!")
            else:
                print("\nDeletion canceled.")
        else:
            print("\nInvalid product ID.")

    except Exception as e:
        print(f"An error occurred while deleting the product: {e}")