import questionary
import time

from rich.console import Console
from rich.panel import Panel
from products_functions import load_product, search_product, view_products, modificate_product_app, stock_products
from register_functions import modificate_user_app

console = Console()

def menu_products_bsm(user_id):
    """Muestra el menú de productos y permite al usuario interactuar con diferentes opciones.
    Este menú incluye opciones para cargar productos, ver productos, gestionar stock,
    eliminar productos, modificar productos y modificar el perfil del usuario.
    Args:
        user_id (int): El ID del usuario que está accediendo al menú de productos.
    """

    while True:
        console.clear()
        console.print(Panel(
            "[bold cyan]Welcome to the Product Menu[/bold cyan]",
            title="🛍️ Products Menu",
            subtitle=f"[green]User ID: {user_id}[/green]",
            style="blue"
        ))

        option = questionary.select(
            "Choose an option:",
            choices=[
                "📦🔃 - Load Products",
                "📦🔍 - View Products",
                "📦🛒 - Products Stock",
                "📦🗑️ - Eliminate Your Products",
                "📦🔧 - Update Your Products",  
                "💻🧷 - Modificate Your Profile",
                "💻🔙 - Main Menu"
            ]
        ).ask()

        if option is None:
            console.print("[bold red]Cancelled or closed. Returning to main menu...[/bold red]")
            time.sleep(1.5)
            console.clear()
            break

        if option.startswith("📦🔃"):
            load_product(user_id)

        elif option.startswith("📦🔍"):
            view_products()

        elif option.startswith("📦🛒"):
            stock_products()

        elif option.startswith("📦🗑️"):
            search_product(user_id)

        elif option.startswith("📦🔧"):
            modificate_product_app(user_id)

        elif option.startswith("💻🧷"):
            modificate_user_app(user_id)

        elif option.startswith("💻🔙"):
            console.print("[bold green]Returning to main menu...[/bold green]")
            time.sleep(1)
            console.clear()
            break
