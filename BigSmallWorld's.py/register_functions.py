from json_dictionary_functions import register_json_data
#=================================================================================

#=================================================================================
#Funcion dedicada al registro de lo usuarios que es llamada desde el main por opcion 1
#Toma los datos ingresados por el usuario y los valida, si no hay errores se guardan en un archivo json
#Si hay errores se le informa al usuario y se le pide que vuelva a ingresar los datos
#Se utiliza un bucle while para permitir al usuario volver a intentar el registro hasta que lo logre

def register():
    flag = True
    while flag:
        print("""
        =============================
        Welcome to Registration!
        """)
        name = input("\tEnter your name: ")
        age = input("\tEnter your age: ")
        gmail = input("\tEnter your email: ")
        password = input("\tEnter your password: ")
        print("\t=============================")

        errors = verificaton_execute(name, age, gmail, password)
        if errors:
            print("The following errors were found:")
            for error in errors:
                print(f"- {error}")
            continue
        else:
            print(f"""
        It has been successfully registered !
        Yor registe name is: {name}
        Your age is: {age}
        Your email is: {gmail}
        Your password is: {password}
        """)
            register_json_data(name, age, gmail, password)
            flag = False
#=================================================================================

#=================================================================================
#Funcion dedicada al login de los usuarios que es llamada desde el main por opcion 2
#Toma los datos ingresados por el usuario y los valida con el JSON, si no hay errores se le informa al usuario que ha iniciado sesion correctamente
#HAY QUE IMPLEMENTAR LA FUNCION DE LOGIN, LUEGO SE PUEDE USAR UN MENU PPARA CARGAR PRODUCTOS, BUSCAR PRODUCTOS, MODIFICAR PRODUCTOS Y ELIMINAR PRODUCTOS

def login():
    print("Implement login functionality here :P")
    pass
#=================================================================================

#=================================================================================
#Funcion dedicada a la verificacion de los datos ingresados por el usuario en el registro
#Recibe los datos ingresados por el usuario y los valida, si no hay errores se devuelve una lista vacia, si hay errores se devuelve una lista con los errores encontrados

def verificaton_execute(name, age, gmail, password):
        errors = []

        if len(name) < 3:
            errors.append("The name must be longer than 3 digits, if it is a short name, complete with your middle name.")
        if not age.isdigit() or int(age) < 18:
            errors.append("You must be at least 18 years old to register.")
        if (gmail.count("@") != 1) or (gmail.count(".") != 1) or (gmail.index("@") > gmail.index(".")):
            errors.append("Invalid email format. Please enter a valid email address.")
        if not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password) or len(password) < 8:
            errors.append("Password must be at least 8 characters long and contain both letters or numbers'.")
        return errors
#=================================================================================




