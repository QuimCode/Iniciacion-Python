#PASAR AL INGLES LAS FUNCIONES!!!!!

#Lista de alcance general para guardar el diccionario y almacenar los productos con sus respectos atributos y valores
lista_diccionarios = []

#=================================================================================
#Funcion dedicada a la carga de productos
#Recibe los datos ingresados por el usuario y los valida  ! FALTA IMPLEMENTAR LA VALIDACION DE LOS DATOS ¡
#Si no hay errores se guarda el producto en un diccionario y se agrega a la lista de diccionarios

def cargar_producto():
    while True:
        nombre_producto = str(input("Ingrese el nombre del producto: "))
        precio_producto = float(input("Ingrese el precio del producto: "))
        stock_producto = int(input("Ingrese la cantidad de stock del producto: "))
        categoria_producto = str(input("Ingrese la categoría del producto: "))
        descripcion_producto = str(input("Ingrese la descripción del producto: "))

        productos = {
            "Nombre Producto": nombre_producto.capitalize(),
            "Precio Producto": precio_producto,
            "Stock Producto": stock_producto,
            "Categoría Producto": categoria_producto.capitalize(),
            "Descripción Producto": descripcion_producto.capitalize()
        }

        lista_diccionarios.append(productos)
        print(f"\n Producto cargado: {productos}")

        print("¿Desea cargar otro producto? (s/n)")
        respuesta = input().lower()
        if respuesta == "s":
            continue
        elif respuesta == "n":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Saliendo del programa...")
#=================================================================================

#=================================================================================
#Funcion dedicada a la busqueda de productos
#Recibe el nombre del producto a buscar y lo busca en la lista de diccionarios a travez de un bucle for
#Si lo encuentra lo imprime y si no lo encuentra informa al usuario que no se ha encontrado el producto

def buscar_producto():
    nombre_producto = str(input("Ingrese el nombre del producto a buscar: "))
    for producto in lista_diccionarios:
        if producto["Nombre Producto"] == nombre_producto:
            print(f"Producto encontrado: {producto}")
            return
    print(f"Producto '{nombre_producto}' no encontrado.")
#=================================================================================

#=================================================================================
#Funcion dedicada a la modificacion(ELIMINACION) de productos
#Recibe el nombre del producto a eliminar y lo busca en la lista de diccionarios a travez de un bucle for al igual que en buscar producto (RECICLAJE DE CODIGO) posible reinvencion de funciones
##Si lo encuentra lo elimina de la lista y si no lo encuentra informa al usuario que no se ha encontrado el producto

def eliminar_producto():
    nombre_producto = str(input("Ingrese el nombre del producto a eliminar: "))
    for producto in lista_diccionarios:
        if producto["Nombre Producto"] == nombre_producto:
            lista_diccionarios.remove(producto)
            print(f"Producto '{nombre_producto}' eliminado.")
            return
    print(f"Producto '{nombre_producto}' no encontrado.")
#=================================================================================


