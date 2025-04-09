# Desarrollar un pequeño programa en Python que pueda: Solicitar al cliente su nombre, apellido, edad y correo electrónico,
# almacene estos datos en variables y los muestre organizados en forma de una tarjeta de presentación en la pantalla.

''' 
Funcion que se ocupa de tomar el registro de los campos informativos del usuario, como nombre, apellido, edad y correo electronico.
El registro se realiza mediante las variable con input, donde se valida que el nombre y apellido contengan solo caracteres alfabeticos, 
la edad contenga solo valores numericos y el correo electronico contenga @ y .
'''
def get_register():
    print("Bienvenido usuario al apartado de registro de Talento Lab, porfavor rellene los campos asignados a continuacion (Nombre, Apellido, Edad y Email)/n")

    name= input("Rellene el campo con su Nombre por favor: ")
    while not name.isalpha():
        print("El nombre debe contener solamente caracteres alfabeticos.")
        name= input("Rellene el campo con su Nombre por favor: ")

    last_name= input("Rellene el campo con su Apellido por favor: ")
    while not last_name.isalpha():
        print("El Apellido debe contener solamente caracteres alfabeticos.")
        last_name= input("Rellene el campo con su Apellido por favor: ")        

    age= input("Rellene el campo con su Edad por favor: ")
    while not age.isdigit():
        print("Ingrese solo valores numericos, correspondiente a su edad.")
        age= input("Rellene el campo con su Edad por favor: ")       

    email= input("Rellene el campo con su Correo Electronico por favor: ")
    while not "@" in email and "." in email:
        email= input("El correo electronico no es valido, porfavor vuelva a ingresarlo. Debe contener @ y . : ")

    print("===========================================================================")
    show_register(name, last_name, age, email)
    print("Gracias por registrarse, su registro ha sido exitoso.")
    return name, last_name, age, email

'''
Funcion que se encarga de retomar los datos del usuario, como nombre, apellido, edad y correo electronico dentro de la funcion principal, 
reciebiendo los argumentos de la funcion get_register y mostrando los datos en pantalla en forma de "tarjeta".
'''
def show_register(name, last_name, age, email):
    print(f"Nombre: {name}")
    print(f"Apellido: {last_name}")
    print(f"Edad: {age}")
    print(f"Email: {email}")
    print("===========================================================================")

get_register()

