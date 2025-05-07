from register_functions import register, login

#Inicio del programa
#Se crea un bucle infinito que solo se detiene cuando el usuario elige la opcion 3 (salir)
#Se le presenta al usuario un menu con las opciones disponibles y se le pide que elija una opcion con el match tomando la respuesta del input
def main():
    while True:
        answer = int(input(
        """ 
        =============================
        Welcome BigSmallWorld, choose an option \n
        1. Sign Up
        2. Log in
        3. Exit 
        =============================\n
        Option: """))

        match answer:
            case 1:
                register()
            case 2:
                login()
            case 3:
                break

main()
