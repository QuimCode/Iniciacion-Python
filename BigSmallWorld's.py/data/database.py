import os
import sqlite3

# Establesco la conexion a la base de datos
# Esta base de datos almacena los usuarios, incluyendo su ID, nombre, edad, email, contraseña y telefono.
# Tambien de paso se ocupa de los productos, incluyendo su ID, nombre, precio, stock, categoria y descripcion.

def get_connection():
    ''' Establece una conexión a la base de datos SQLite
    La funcion no recibe parametros, ya que la base de datos se encuentra en el mismo directorio que este script.
    Devuelve un objeto de conexión a la base de datos, o None si ocurre un error.'''
    try:
        db_path = os.path.join(os.path.dirname(__file__), "database_user.db")
        return sqlite3.connect(db_path)
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

#=================================================================================

def create_users_table():
    ''' Crea la tabla de usuarios en la base de datos
    La funcion no recibe parametros, ya que crea la tabla de usuarios si no existe.
    La tabla tiene los campos: id, username, age, email, password y phone.'''

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            age INTEGER NOT NULL CHECK(age >= 18),
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            phone TEXT NOT NULL UNIQUE
        )
    ''')
    connection.commit()
    connection.close()

#=================================================================================

def insert_user(username, age, email, password, phone):
    ''' Inserta un nuevo usuario en la base de datos
    La funcion recibe los datos del usuario y los inserta en la tabla de usuarios.
    Tiene try y except para manejar errores de integridad, como duplicados en email, username o telefono.'''

    create_users_table()
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO users (username, age, email, password, phone) VALUES (?, ?, ?, ?, ?)",
                (username, age, email, password, phone)
            )
            connection.commit()
        return True
    except sqlite3.IntegrityError as e:
        if "email" in str(e):
            print("Error: El correo electrónico ya está registrado.")
        elif "username" in str(e):
            print("Error: El nombre de usuario ya existe.")
        elif "phone" in str(e):
            print("Error: El número de teléfono ya está en uso.")
        else:
            print(f"Error de integridad: {e}")
        return False

#=================================================================================

def find_user(email, password):
    ''' Busca un usuario por email y contraseña
    La funcion recibe el email y la contraseña del usuario y busca en la base de datos.
    Si encuentra un usuario con esos datos, devuelve su ID y nombre de usuario.
    Devuelve None si no existe, o (id, username) si existe.'''

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT id, username FROM users WHERE email = ? AND password = ?",
        (email, password)
    )
    user = cursor.fetchone()
    connection.close()
    return user 

#=================================================================================

def get_user_by_id(user_id):
    ''' Obtiene un usuario por su ID
    La funcion recibe el ID del usuario y busca en la base de datos.
    Si encuentra un usuario con ese ID, devuelve una tupla con su ID, nombre de usuario, edad, email y telefono. '''

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, username, age, email, phone FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    connection.close()
    return user

#=================================================================================

def eliminate_user(email, password):
    ''' Elimina un usuario de la base de datos
    La funcion recibe el email y la contraseña del usuario y elimina su registro de la base de datos.
    Devuelve True si se eliminó un usuario, False si no se encontró o no se pudo eliminar.'''

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE email = ? AND password = ?", (email, password,))
    connection.commit()
    connection.close()
    return cursor.rowcount > 0 

#=================================================================================

def modificate_user(user_id, new_username=None, new_age=None, new_email=None, new_password=None, new_phone=None):
    ''' Modifica los datos de un usuario
    La funcion recibe el ID del usuario y los nuevos datos (opcionalmente) y actualiza su registro en la base de datos.
    Si no se proporciona un nuevo dato, no se actualiza ese campo.'''

    connection = get_connection()
    cursor = connection.cursor()
    
    updates = []
    params = []
    
    if new_username:
        updates.append("username = ?")
        params.append(new_username)
    if new_age is not None:
        updates.append("age = ?")
        params.append(new_age)
    if new_email:
        updates.append("email = ?")
        params.append(new_email)
    if new_password:
        updates.append("password = ?")
        params.append(new_password)
    if new_phone:
        updates.append("phone = ?")
        params.append(new_phone)
    
    if not updates:
        print("No se proporcionaron datos para actualizar.")
        return False

    params.append(user_id)
    query = f"UPDATE users SET {', '.join(updates)} WHERE id = ?"
    
    try:
        cursor.execute(query, tuple(params))
        connection.commit()
        return cursor.rowcount > 0
    except sqlite3.IntegrityError as e:
        if "email" in str(e):
            print("Error: El correo electrónico ya está registrado.")
        elif "username" in str(e):
            print("Error: El nombre de usuario ya existe.")
        elif "phone" in str(e):
            print("Error: El número de teléfono ya está en uso.")
        else:
            print(f"Error de integridad: {e}")
        return False
    finally:
        connection.close()


#============================================================================================================
#=========================================  DATABASE PRODUCTS FUNCTIONS   ===================================
#============================================================================================================

def create_product_table():
    ''' Crea la tabla de productos en la base de datos
    La funcion no recibe parametros, ya que crea la tabla de productos si no existe.
    La tabla tiene los campos: id, user_id, name, price, stock, category y description.'''

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            price REAL NOT NULL CHECK(price >= 1),
            stock INTEGER NOT NULL CHECK(stock >= 0),
            category TEXT NOT NULL,
            description TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id),
            UNIQUE(user_id, name)
        )
    ''')
    connection.commit()
    connection.close()

#=================================================================================

def insert_product(user_id, name, price, stock, category, description):
    ''' Inserta un nuevo producto en la base de datos
    La funcion recibe los datos del producto y los inserta en la tabla de productos.
    Tiene try y except para manejar errores de integridad, como duplicados en el nombre del producto para un usuario.'''

    create_product_table() 
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO products (user_id, name, price, stock, category, description) VALUES (?, ?, ?, ?, ?, ?)",
            (user_id, name, price, stock, category, description)
        )
        connection.commit()
        connection.close()
        return True
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
        return False
    
#=================================================================================

def get_all_products():
    ''' Obtiene todos los productos de la base de datos
    La funcion no recibe parametros, ya que devuelve todos los productos de la base de datos.
    Devuelve una lista de tuplas, cada una representando un producto con su ID, user_id, nombre, precio, stock, categoria y descripcion. '''

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT id, user_id, name, price, stock, category, description FROM products"
    )
    products = cursor.fetchall()
    connection.close()
    return products

#=================================================================================

def find_product_by_id(product_id):

    ''' Busca un producto por su ID
    La funcion recibe el ID del producto y busca en la base de datos.
    Si encuentra un producto con ese ID, devuelve una tupla con su ID, user_id, nombre, precio, stock, categoria y descripcion. '''

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT id, user_id, name, price, stock, category, description FROM products WHERE id = ?",
        (product_id,)
    )
    product = cursor.fetchone()
    connection.close()
    return product

#=================================================================================

def modificate_product(product_id, new_name=None, new_price=None, new_stock=None, new_category=None, new_description=None):
    ''' Modifica los datos de un producto
    La funcion recibe el ID del producto y los nuevos datos (opcionalmente) y actualiza su registro en la base de datos.
    Si no se proporciona un nuevo dato, no se actualiza ese campo.'''

    connection = get_connection()
    cursor = connection.cursor()
    
    updates = []
    params = []
    
    if new_name:
        updates.append("name = ?")
        params.append(new_name)
    if new_price is not None:
        updates.append("price = ?")
        params.append(new_price)
    if new_stock is not None:
        updates.append("stock = ?")
        params.append(new_stock)
    if new_category:
        updates.append("category = ?")
        params.append(new_category)
    if new_description:
        updates.append("description = ?")
        params.append(new_description)
    
    if not updates:
        return False 
    
    params.append(product_id)  
    query = f"UPDATE products SET {', '.join(updates)} WHERE id = ?"
    
    cursor.execute(query, tuple(params))
    connection.commit()
    connection.close()
    
    return cursor.rowcount > 0

#=================================================================================

def get_products_by_min_stock(min_stock):
    ''' Obtiene productos con stock menor o igual al valor especificado
    La funcion recibe un valor minimo de stock y devuelve todos los productos con stock menor o igual a ese valor.
    Devuelve una lista de tuplas, cada una representando un producto con su ID, user_id, nombre, precio, stock, categoria y descripcion. '''

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT id, user_id, name, price, stock, category, description FROM products WHERE stock <= ? ORDER BY stock DESC",
        (min_stock,)
    )
    products = cursor.fetchall()
    connection.close()
    return products

#=================================================================================

def eliminate_product(id_product):
    ''' Elimina un producto de la base de datos
    La funcion recibe el ID del producto y elimina su registro de la base de datos.
    Devuelve True si se eliminó un producto, False si no se encontró o no se pudo eliminar.'''
    
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (id_product,))
    connection.commit()
    connection.close()
    return cursor.rowcount > 0