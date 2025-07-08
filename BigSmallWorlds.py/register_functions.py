from rich.console import Console
from rich.panel import Panel
import questionary
import time
from data.database import insert_user, find_user, eliminate_user, modificate_user

#=================================================================================

console = Console()

def register():
    # """Permite al usuario registrarse ingresando sus datos personales.
    # Esta función solicita al usuario su nombre, edad, correo electrónico, contraseña y número de teléfono.
    # Valida los datos ingresados y, si son correctos, los guarda en la base de datos.
    # Si hay errores en los datos, se informa al usuario y se le permite volver a intentarlo.
    # Returns:
    #     None
    # """

    while True:
        console.print(Panel("[bold cyan]Welcome to Registration![/bold cyan]", title="📝 Register", style="blue"))

        name = questionary.text("👤 Enter your name:").ask()
        age = questionary.text("🎂 Enter your age:").ask()
        gmail = questionary.text("📧 Enter your email:").ask()
        password = questionary.password("🔒 Enter your password:").ask()
        phone = questionary.text("📞 Enter your phone:").ask()

        console.print("[bold yellow]=============================[/bold yellow]")

        errors = verificaton_execute(name, age, gmail, password, phone)

        if errors:
            error_msg = "\n".join(f"- {e}" for e in errors)
            console.print(Panel(f"[bold red]The following errors were found:[/bold red]\n{error_msg}", style="red"))
            retry = questionary.confirm("Do you want to try registering again?").ask()
            if retry:
                continue
            else:
                console.print("[bold green]Returning to the main menu...[/bold green]")
                console.clear()
                break
        else:
            success = insert_user(name, age, gmail, password, phone)
            if success:
                success_msg = (
                    f"[green]✅ Successfully registered![/green]\n\n"
                    f"[bold]Name:[/bold] {name}\n"
                    f"[bold]Age:[/bold] {age}\n"
                    f"[bold]Email:[/bold] {gmail}\n"
                    f"[bold]Password:[/bold] {password}\n"
                    f"[bold]Phone:[/bold] {phone}"
                )
                console.print(Panel(success_msg, title="🎉 Registration Complete", style="green"))
            else:
                console.print(Panel("[bold red]A user with that name, email, or phone already exists.[/bold red]", style="red"))

            retry = questionary.confirm("Do you want to register another user?").ask()
            if retry:
                continue
            else:
                console.print("[bold green]Returning to the main menu...[/bold green]")
                console.clear()
                break

#=================================================================================

def login():
    """Permite al usuario iniciar sesión ingresando su correo electrónico y contraseña.
    Esta función solicita al usuario su correo electrónico y contraseña, valida los datos ingresados
    y, si son correctos, muestra un mensaje de bienvenida. Si los datos son incorrectos, informa al usuario y le permite volver a intentarlo.
    Returns:
        int: El ID del usuario si el inicio de sesión es exitoso, None en caso contrario.
    """
    console.print(Panel("[bold cyan]Welcome to Login![/bold cyan]", title="🔐 Login", style="blue"))

    gmail = questionary.text("📧 Enter your email:").ask()
    password = questionary.password("🔑 Enter your password:").ask()

    console.print("[bold yellow]=============================[/bold yellow]")

    user = find_user(gmail, password)
    if user:
        user_id, username = user
        welcome_msg = f"✅ Welcome back, [bold green]{username} ... Wait a few seconds [/bold green]!"
        console.print(Panel(welcome_msg, title="🎉 Success", style="green"))
        time.sleep(1.5)
        console.clear()
        return user_id
    else:
        console.print(Panel("❌ [bold red]Invalid email or password. Please try again.[/bold red]", style="red"))
        time.sleep(1)
        console.clear()
        return None

#=================================================================================

def eliminate_user_app():
    """Permite al usuario eliminar su cuenta ingresando su correo electrónico y contraseña.
    Esta función solicita al usuario su correo electrónico y contraseña, valida los datos ingresados
    y, si son correctos, elimina la cuenta del usuario. Si los datos son incorrectos, informa al usuario y le permite volver a intentarlo.
    Returns:
        bool: True si la cuenta fue eliminada exitosamente, False en caso contrario.
    """

    console.print(Panel("[bold cyan]Welcome to User Elimination![/bold cyan]", title="🗑️ Eliminate User", style="blue"))

    gmail = questionary.text("📧 Enter the email of the user to eliminate:").ask()
    password = questionary.password("🔑 Enter the password of the user to eliminate:").ask()

    console.print("[bold yellow]=============================[/bold yellow]")

    user = find_user(gmail, password)
    if user:
        username = user
        eliminate_user(gmail, password)
        console.print(Panel(f"✅ User [bold green]{username}[/bold green] has been eliminated successfully! Wait a few seconds", title="🎉 Success", style="green"))
        time.sleep(4)
        console.clear()
        return True
    else:
        console.print(Panel("❌ [bold red]Invalid email or password. Please try again.[/bold red]", style="red"))
        time.sleep(1.5)
        return False

#=================================================================================

def modificate_user_app(user_id):
    """Permite al usuario modificar su perfil ingresando nuevos datos.
    Esta función solicita al usuario nuevos datos como nombre de usuario, edad, correo electrónico, contraseña y teléfono.
    Valida los datos ingresados y, si son correctos, actualiza la información del usuario en la base de datos.
    Si hay errores en los datos, se informa al usuario y se le permite volver a intentarlo.
    Args:
        user_id (int): El ID del usuario que está modificando su perfil.
    Returns:
        None
    """

    while True:
        console.print(Panel("[bold cyan]Welcome to User Modification![/bold cyan]", title="🛠️ Modify User", style="blue"))

        new_username = questionary.text("👤 Enter new username (leave blank to keep current):").ask() or None
        new_age = questionary.text("🎂 Enter new age (leave blank to keep current):").ask() or None
        new_email = questionary.text("📧 Enter new email (leave blank to keep current):").ask() or None
        new_password = questionary.password("🔒 Enter new password (leave blank to keep current):").ask() or None
        new_phone = questionary.text("📞 Enter new phone (leave blank to keep current):").ask() or None

        errors = verification_modification(new_username, new_age, new_email, new_password, new_phone)
        if errors:
            error_msg = "\n".join(f"- {e}" for e in errors)
            console.print(Panel(f"[bold red]The following errors were found:[/bold red]\n{error_msg}", style="red"))
            retry = questionary.confirm("Do you want to try again?").ask()
            if not retry:
                break
            continue

        if new_age is not None and new_age != "":
            new_age = int(new_age)

        if new_username or new_age or new_email or new_password or new_phone:
            success = modificate_user(user_id, new_username, new_age, new_email, new_password, new_phone)
            if success:
                console.print(Panel(f"✅ Your profile has been modified successfully! Wait a few seconds", title="🎉 Success", style="green"))
                time.sleep(1.9)
            else:
                console.print(Panel("[bold red]Failed to modify user. Please check the data and try again.[/bold red]", style="red"))
                time.sleep(1)
        break

#=================================================================================

#=================================================================================

def verificaton_execute(name, age, gmail, password, phone):
        """Verifica los datos ingresados por el usuario durante el registro.
        Esta función valida el nombre, la edad, el correo electrónico, la contraseña y el número de teléfono.
        Args:
            name (str): El nombre del usuario.
            age (str): La edad del usuario.
            gmail (str): El correo electrónico del usuario.
            password (str): La contraseña del usuario.
            phone (str): El número de teléfono del usuario.
        Returns:
            list: Una lista de errores encontrados durante la validación. Si no hay errores, la lista estará vacía.
        """

        errors = []

        if len(name) < 3:
            errors.append("The name must be longer than 3 digits, if it is a short name, complete with your middle name.")
        if not age.isdigit() or int(age) < 18 or int(age) > 100:
            errors.append("You must be at least 18 years old to register.")
        if (gmail.count("@") != 1) or (gmail.count(".") != 1) or (gmail.index("@") > gmail.index(".")):
            errors.append("Invalid email format. Please enter a valid email address.")
        if not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password) or len(password) < 8:
            errors.append("Password must be at least 8 characters long and contain both letters or numbers'.")
        if not phone.isdigit() or len(phone) < 10 or len(phone) > 10:
            errors.append("Phone number must be at least 10 digits long and contain only numbers.")
        return errors

def verification_modification(new_username=None, new_age=None, new_email=None, new_password=None, new_phone=None):
    """Verifica los datos ingresados por el usuario durante la modificación de su perfil.
    Esta función valida el nuevo nombre de usuario, la nueva edad, el nuevo correo electrónico,
    la nueva contraseña y el nuevo número de teléfono.
    Args:
        new_username (str): El nuevo nombre de usuario del usuario.
        new_age (str): La nueva edad del usuario.
        new_email (str): El nuevo correo electrónico del usuario.
        new_password (str): La nueva contraseña del usuario.
        new_phone (str): El nuevo número de teléfono del usuario.
    Returns:
        list: Una lista de errores encontrados durante la validación. Si no hay errores, la lista estará vacía.
    """

    errors = []

    if new_username is not None and new_username != "":
        if len(new_username) < 3:
            errors.append("The name must be longer than 3 digits, if it is a short name, complete with your middle name.")
    if new_age is not None and new_age != "":
        if not new_age.isdigit() or int(new_age) < 18 or int(new_age) > 100:
            errors.append("You must be at least 18 years old to register.")
    if new_email is not None and new_email != "":
        if (new_email.count("@") != 1) or (new_email.count(".") != 1) or (new_email.index("@") > new_email.index(".")):
            errors.append("Invalid email format. Please enter a valid email address.")
    if new_password is not None and new_password != "":
        if not any(char.isdigit() for char in new_password) or not any(char.isalpha() for char in new_password) or len(new_password) < 8:
            errors.append("Password must be at least 8 characters long and contain both letters or numbers.")
    if new_phone is not None and new_phone != "":
        if not new_phone.isdigit() or len(new_phone) < 10:
            errors.append("Phone number must be at least 10 digits long and contain only numbers.")
    return errors

#=================================================================================


# def register():
#     flag = True
#     while flag:
#         print("""
#         =============================
#         Welcome to Registration!
#         """)
#         name = input("\tEnter your name: ")
#         age = input("\tEnter your age: ")
#         gmail = input("\tEnter your email: ")
#         password = input("\tEnter your password: ")
#         print("\t=============================")

#         errors = verificaton_execute(name, age, gmail, password)
#         if errors:
#             print("The following errors were found:")
#             for error in errors:
#                 print(f"- {error}")
#             continue
#         else:
#             print(f"""
#         It has been successfully registered !
#         Yor registe name is: {name}
#         Your age is: {age}
#         Your email is: {gmail}
#         Your password is: {password}
#         """)
#             register_json_userData(name, age, gmail, password)
#             flag = False

# def register():
#     while True:
#         console.print(Panel("[bold cyan]Welcome to Registration![/bold cyan]", title="📝 Register", style="blue"))

#         name = questionary.text("👤 Enter your name:").ask()
#         age = questionary.text("🎂 Enter your age:").ask()
#         gmail = questionary.text("📧 Enter your email:").ask()
#         password = questionary.password("🔒 Enter your password:").ask()

#         console.print("[bold yellow]=============================[/bold yellow]")

#         errors = verificaton_execute(name, age, gmail, password)

#         if errors:
#             error_msg = "\n".join(f"- {e}" for e in errors)
#             console.print(Panel(f"[bold red]The following errors were found:[/bold red]\n{error_msg}", style="red"))
#             continue
#         else:
#             success_msg = (
#                 f"[green]✅ Successfully registered![/green]\n\n"
#                 f"[bold]Name:[/bold] {name}\n"
#                 f"[bold]Age:[/bold] {age}\n"
#                 f"[bold]Email:[/bold] {gmail}\n"
#                 f"[bold]Password:[/bold] {password}"
#             )
#             console.print(Panel(success_msg, title="🎉 Registration Complete", style="green"))
#             register_json_userData(name, age, gmail, password)
#             # break

#         return_to_menu = questionary.confirm("Return to main menu?").ask()

#         if return_to_menu:
#             console.print("[bold green]Redirecting to the main menu...[/bold green]")
#             console.clear()
#             break
#         else:
#             console.print("[bold yellow]You chose to stay here. Let's register someone else![/bold yellow]\n")
#             console.print("-" * 50)

# def login():
#     data_user = open_json_userData()
#     if not data_user:
#         print("No users are registered yet.")
#         return None  

#     print("""
#     =============================
#     Welcome to Login!
#     =============================
#     """)
#     gmail = input("\tEnter your email: ")
#     password = input("\tEnter your password: ")
#     print("\t=============================")

#     for user_id, user_data in data_user.items():
#         if user_data["gmail"] == gmail and user_data["password"] == password:
#             print(f"\nWelcome back, {user_data['name']}!")
#             return user_id  

#     print("\nInvalid email or password. Please try again.")
#     return None

# def login():
#     data_user = open_json_userData()
#     if not data_user:
#         console.print(Panel("🚫 [bold red]No users are registered yet.[/bold red]", style="red"))
#         return None

#     console.print(Panel("[bold cyan]Welcome to Login![/bold cyan]", title="🔐 Login", style="blue"))

#     gmail = questionary.text("📧 Enter your email:").ask()
#     password = questionary.password("🔑 Enter your password:").ask()

#     console.print("[bold yellow]=============================[/bold yellow]")

#     for user_id, user_data in data_user.items():
#         if user_data["gmail"] == gmail and user_data["password"] == password:
#             welcome_msg = f"✅ Welcome back, [bold green]{user_data['name']}[/bold green]!"
#             console.print(Panel(welcome_msg, title="🎉 Success", style="green"))
#             return user_id

#     console.print(Panel("❌ [bold red]Invalid email or password. Please try again.[/bold red]", style="red"))
#     return None