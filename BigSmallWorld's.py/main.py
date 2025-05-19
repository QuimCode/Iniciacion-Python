from utilities_menu_bsm import menu_products_bsm
from register_functions import register, login

#Inicio del programa
#Se crea un bucle infinito que solo se detiene cuando el usuario elige la opcion 3 (salir) (ARREGLAR ERROR, EL BUCLE NO PARA)
#Se le presenta al usuario un menu con las opciones disponibles y se le pide que elija una opcion con el match tomando la respuesta del input
def main():
    user_id = None

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
                user_id = login() 
                if user_id:
                    print(f"User ID {user_id} logged in successfully!")
                    menu_products_bsm(user_id)  
            case 3:
                break

main()
