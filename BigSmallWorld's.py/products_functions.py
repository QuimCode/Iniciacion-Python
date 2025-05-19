from json_dictionary_functions import register_json_productData, json_search_product, json_delete_product

#PASAR AL INGLES LAS FUNCIONES!!!!!

#Lista de alcance general para guardar el diccionario y almacenar los productos con sus respectos atributos y valores
product_list = []

#=================================================================================
#Funcion dedicada a la carga de productos
#Recibe los datos ingresados por el usuario y los valida  ! FALTA IMPLEMENTAR LA VALIDACION DE LOS DATOS ¡
#Si no hay errores se guarda el producto en un diccionario y se agrega a la lista de diccionarios

def load_product(user_id):
    while True:
        product_name = str(input("Enter the product name: "))
        product_price = float(input("Enter the product price: "))
        product_stock = int(input("Enter the product stock quantity: "))
        product_category = str(input("Enter the product category: "))
        product_description = str(input("Enter the product description: "))

        product = {
            "Product Name": product_name.capitalize(),
            "Product Price": product_price,
            "Product Stock": product_stock,
            "Product Category": product_category.capitalize(),
            "Product Description": product_description.capitalize()
        }

        product_list.append(product)
        print(f"\nProduct added: {product}")

        register_json_productData(user_id, product_name, product_price, product_description)

        print("Do you want to add another product? (y/n)")
        response = input().lower()
        if response == "y":
            continue
        elif response == "n":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Exiting program...")
#=================================================================================

#=================================================================================
#Funcion dedicada a la busqueda de productos
#Recibe el nombre del producto a buscar y lo busca en la lista de diccionarios a travez de un bucle for
#Si lo encuentra lo imprime y si no lo encuentra informa al usuario que no se ha encontrado el producto

def search_product():
    json_search_product()
#=================================================================================

#=================================================================================
#Funcion dedicada a la modificacion(ELIMINACION) de productos
#Recibe el nombre del producto a eliminar y lo busca en la lista de diccionarios a travez de un bucle for al igual que en buscar producto (RECICLAJE DE CODIGO) posible reinvencion de funciones
##Si lo encuentra lo elimina de la lista y si no lo encuentra informa al usuario que no se ha encontrado el producto

def delete_product():
    json_delete_product()
#=================================================================================


