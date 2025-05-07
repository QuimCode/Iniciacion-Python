#PASAR AL INGLES LAS FUNCIONES!!!!!

def main():
    opciones_ingreso()

lista_diccionarios = []

def opciones_ingreso():
    while True:
        print("""
            Bienvenido a BigSmallWorld (Carga de productos)
            1. Cargar producto
            2. Buscar producto
            3. Modificar producto
            4. Eliminar producto
            5. Salir
            """)
        
        opciones = int(input("Seleccione una opción: "))

        match opciones:
            case 1:
                cargar_producto()
            case 2:
                buscar_producto()
            case 3:
                pass
            case 4:
                eliminar_producto()
            case 5:
                break

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

def buscar_producto():
    nombre_producto = str(input("Ingrese el nombre del producto a buscar: "))
    for producto in lista_diccionarios:
        if producto["Nombre Producto"] == nombre_producto:
            print(f"Producto encontrado: {producto}")
            return
    print(f"Producto '{nombre_producto}' no encontrado.")

def eliminar_producto():
    nombre_producto = str(input("Ingrese el nombre del producto a eliminar: "))
    for producto in lista_diccionarios:
        if producto["Nombre Producto"] == nombre_producto:
            lista_diccionarios.remove(producto)
            print(f"Producto '{nombre_producto}' eliminado.")
            return
    print(f"Producto '{nombre_producto}' no encontrado.")

main()