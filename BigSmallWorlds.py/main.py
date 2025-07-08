import questionary

from rich.console import Console
from rich.panel import Panel
from utilities_menu_bsm import menu_products_bsm
from register_functions import register, login, eliminate_user_app

console = Console()

def main():
    # """
    # Función principal que muestra el menú de bienvenida y permite al usuario registrarse, iniciar sesión o eliminar su cuenta.
    # Esta función utiliza la biblioteca questionary para interactuar con el usuario y rich para mostrar mensajes en la consola.
    # Si el usuario elige iniciar sesión, se le redirige al menú de productos. Si elige registrarse, se llama a la función de registro o
    # si elige eliminar su cuenta, se llama a la función de eliminación de cuenta.
    # Args:
    #     None
    # Returns:
    #     None
    # """

    user_id = None
    while True:
        console.print(Panel("[bold cyan]Welcome to BigSmallWorld[/bold cyan]", title="🌍 BigSmallWorld", style="green"))
        option = questionary.select(
            "Choose an option:",
            choices=["📝 - Sign Up", "🔑 - Log In", "❌ - Eliminate Your Account", "🚪 - Exit"]
        ).ask()

        if option is None:
            console.print("[bold red]Cancelled or closed by user. Exiting...[/bold red]")
            break

        if option.startswith("📝 - Sign Up"):
            register()

        elif option.startswith("🔑 - Log In"):
            user_id = login()
            if user_id:
                console.print(f"[bold green]User ID {user_id} logged in successfully![/bold green]")
                menu_products_bsm(user_id)
        
        elif option.startswith("❌ - Eliminate Your Account"):
            eliminate_user_app()

        elif option.startswith("🚪 - Exit"):
            console.print("[bold yellow]Exiting the program...[/bold yellow]")
            break

main()




#Menu Viejo

# def main():
#     user_id = None

#     while True:
#         answer = int(input(
#         """ 
#         =============================
#         Welcome BigSmallWorld, choose an option \n
#         1. Sign Up
#         2. Log in
#         3. Exit 
#         =============================\n
#         Option: """))

#         match answer:
#             case 1:
#                 register()
#             case 2:
#                 user_id = login() 
#                 if user_id:
#                     print(f"User ID {user_id} logged in successfully!")
#                     menu_products_bsm(user_id)  
#             case 3:
#                 break

