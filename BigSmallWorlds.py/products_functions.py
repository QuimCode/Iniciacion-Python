import time

from rich.table import Table
from rich.console import Console
from data.database import insert_product, get_all_products, find_product_by_id, eliminate_product, modificate_product

#Lista de alcance general para guardar el diccionario y almacenar los productos con sus respectos atributos y valores
product_list = []

#=================================================================================

def load_product(user_id):
    """Carga un producto en la base de datos.
    Esta función solicita al usuario los detalles del producto, valida los campos y lo inserta en la base de datos.
    Si hay errores de validación, los muestra y permite al usuario intentar nuevamente o salir.
    Args:
        user_id (int): El ID del usuario que está cargando el producto.
    """

    console = Console()
    while True:
        console.print("[bold cyan]=== Product Registration ===[/bold cyan]")
        product_name = console.input("[green]Enter the product name:[/green] ")
        product_price = console.input("[yellow]Enter the product price:[/yellow] ")
        product_stock = console.input("[blue]Enter the product stock quantity:[/blue] ")
        product_category = console.input("[magenta]Enter the product category:[/magenta] ")
        product_description = console.input("[white]Enter the product description:[/white] ")

        errors = validate_product_fields(product_name, product_price, product_stock, product_category, product_description)
        if errors:
            error_msg = "\n".join(f"- {e}" for e in errors)
            console.print(f"[bold red]The following errors were found:[/bold red]\n{error_msg}")
            retry = console.input("[bold yellow]Do you want to try again? (y/n):[/bold yellow] ").lower()
            if retry == "y":
                continue
            else:
                break

        product_price = float(str(product_price).replace(",", "."))
        product_stock = int(product_stock)

        success = insert_product(user_id, product_name, product_price, product_stock, product_category, product_description)
        if success:
            console.print(f"\n[bold green]✅ Product '{product_name}' added successfully![/bold green]")
        else:
            console.print(f"\n[bold red]❌ Failed to add product '{product_name}'. It may already exist or there was an error.[/bold red]")

        response = console.input("[bold yellow]Do you want to add another product? (y/n):[/bold yellow] ").lower()
        if response == "y":
            continue
        else:
            console.print("[bold cyan]Exiting product entry...[/bold cyan]")
            time.sleep(1)
            break

#=================================================================================

def view_products():
    """Muestra todos los productos registrados en la base de datos.
    Esta función obtiene todos los productos de la base de datos y los muestra en una tabla formateada.
    Si no hay productos, informa al usuario.
    """

    console = Console()
    products = get_all_products()
    if not products:
        console.print("[bold yellow]No products found in the database.[/bold yellow]")
        return

    console.print("[bold cyan]====== Product Table Registration ======[/bold cyan]")
    table = Table(title="All Products", show_lines=True)
    table.add_column("ID", style="cyan", justify="center")
    table.add_column("User ID", style="magenta", justify="center")
    table.add_column("Name", style="green")
    table.add_column("Price", style="yellow")
    table.add_column("Stock", style="blue")
    table.add_column("Category", style="white")
    table.add_column("Description", style="white")

    for prod in products:
        price_str = str(prod[3]).replace(",", ".")
        table.add_row(
            str(prod[0]), 
            str(prod[1]),  
            prod[2],      
            f"${float(price_str):.2f}",
            str(prod[4]), 
            prod[5],      
            prod[6]  
        )

    console.print(table)
    console.input("[bold cyan]Press Enter to return to the menu...[/bold cyan]")

#=================================================================================

def search_product(user_id):
    """Busca un producto por su ID y permite eliminarlo si es del usuario actual.
    Esta función solicita al usuario el ID del producto, valida que sea un número,
    busca el producto en la base de datos y muestra sus detalles en una tabla.
    Si el producto pertenece al usuario actual, permite eliminarlo.
    Args:
        user_id (int): El ID del usuario que está buscando el producto.
    """

    console = Console()
    product_id = console.input("[cyan]Enter the product ID to search:[/cyan] ")
    if not product_id.isdigit():
        console.print("[bold red]Invalid ID. Must be a number.[/bold red]")
        return

    product = find_product_by_id(int(product_id))
    if not product:
        console.print("[bold yellow]No product found with that ID.[/bold yellow]")
        time.sleep(1)
        return

    table = Table(title="Product Found", show_lines=True)
    table.add_column("ID", style="cyan", justify="center")
    table.add_column("User ID", style="magenta", justify="center")
    table.add_column("Name", style="green")
    table.add_column("Price", style="yellow")
    table.add_column("Stock", style="blue")
    table.add_column("Category", style="white")
    table.add_column("Description", style="white")

    price_str = str(product[3]).replace(",", ".")
    table.add_row(
        str(product[0]), 
        str(product[1]),  
        product[2],       
        f"${float(price_str):.2f}",
        str(product[4]),  
        product[5],       
        product[6]       
    )

    console.print(table)

    if product[1] != user_id:
        console.print("[bold red]You can only delete your own products![/bold red]")
        time.sleep(2.8)
        return

    delete = console.input("[bold red]Do you want to delete this product? (y/n):[/bold red] ").lower()
    if delete == "y":
        success = delete_product(int(product_id))
        if success:
            console.print("[bold green]Product deleted successfully![/bold green]")
            time.sleep(2.5)
        else:
            console.print("[bold red]Failed to delete product.[/bold red]")
            time.sleep(2.5)
    else:
        console.print("[bold yellow]Product was not deleted.[/bold yellow]")
        time.sleep(2.5)

#=================================================================================

def delete_product(product_id):
    """Elimina un producto de la base de datos por su ID.
    Esta función recibe el ID del producto a eliminar y llama a la función de eliminación de la base de datos.
    Args:
        product_id (int): El ID del producto a eliminar.
    Returns:
        bool: True si el producto fue eliminado exitosamente, False en caso contrario.
    """
    return eliminate_product(product_id)

#=================================================================================

def modificate_product_app(user_id):
    """Permite al usuario modificar un producto existente.
    Esta función solicita al usuario el ID del producto a modificar, valida que sea un número,
    busca el producto en la base de datos y muestra sus detalles.
    Si el producto pertenece al usuario actual, permite modificar sus campos.
    Args:
        user_id (int): El ID del usuario que está modificando el producto.
    """

    console = Console()
    product_id = console.input("[cyan]Enter the product ID to modify:[/cyan] ")
    if not product_id.isdigit():
        console.print("[bold red]Invalid ID. Must be a number.[/bold red]")
        time.sleep(2)
        return

    product = find_product_by_id(int(product_id))
    if not product:
        console.print("[bold yellow]No product found with that ID.[/bold yellow]")
        time.sleep(2)
        return

    # Verificar que el producto pertenece al usuario
    if product[1] != user_id:
        console.print("[bold red]You can only modify your own products![/bold red]")
        time.sleep(2.5)
        return

    console.print("[bold cyan]Leave blank any field you don't want to change.[/bold cyan]")

    new_name = console.input(f"[green]New name (current: {product[2]}):[/green] ") or None
    new_price = console.input(f"[yellow]New price (current: {product[3]}):[/yellow] ") or None
    new_stock = console.input(f"[blue]New stock (current: {product[4]}):[/blue] ") or None
    new_category = console.input(f"[magenta]New category (current: {product[5]}):[/magenta] ") or None
    new_description = console.input(f"[white]New description (current: {product[6]}):[/white] ") or None

    errors = validate_product_modification_fields(
        name=new_name,
        price=new_price,
        stock=new_stock,
        category=new_category,
        description=new_description
    )
    if errors:
        error_msg = "\n".join(f"- {e}" for e in errors)
        console.print(f"[bold red]The following errors were found:[/bold red]\n{error_msg}")
        time.sleep(3)
        return

    if all(x is None for x in [new_name, new_price, new_stock, new_category, new_description]):
        console.print("[bold yellow]No changes made.[/bold yellow]")
        time.sleep(2)
        return

    success = modificate_product(
        int(product_id),
        new_name=new_name,
        new_price=new_price,
        new_stock=new_stock,
        new_category=new_category,
        new_description=new_description
    )
    if success:
        console.print("[bold green]Product modified successfully![/bold green]")
    else:
        console.print("[bold red]Failed to modify product. Please try again.[/bold red]")
    time.sleep(2.5)

#=================================================================================

def stock_products():
    """Muestra los productos con stock menor o igual a un valor especificado por el usuario.
    Esta función solicita al usuario un valor mínimo de stock y muestra una tabla con los productos que cumplen con ese criterio.
    Si no hay productos con el stock especificado, informa al usuario.
    """

    console = Console()
    min_stock = console.input("[cyan]Show products with stock greater than or equal to:[/cyan] ")
    if not min_stock.isdigit():
        console.print("[bold red]Invalid stock value. Must be a number.[/bold red]")
        time.sleep(2)
        return

    from data.database import get_products_by_min_stock
    products = get_products_by_min_stock(int(min_stock))
    if not products:
        console.print(f"[bold yellow]No products found with stock <= {min_stock}.[/bold yellow]")
        time.sleep(2)
        return

    table = Table(title=f"Products with Stock <= {min_stock} (Ordered by Stock)", show_lines=True)
    table.add_column("ID", style="cyan", justify="center")
    table.add_column("User ID", style="magenta", justify="center")
    table.add_column("Name", style="green")
    table.add_column("Price", style="yellow")
    table.add_column("Stock", style="blue")
    table.add_column("Category", style="white")
    table.add_column("Description", style="white")

    for prod in products:
        price_str = str(prod[3]).replace(",", ".")
        table.add_row(
            str(prod[0]), 
            str(prod[1]),  
            prod[2],      
            f"${float(price_str):.2f}",
            str(prod[4]), 
            prod[5],      
            prod[6]  
        )

    console.print(table)
    console.input("[bold cyan]Press Enter to return to the menu...[/bold cyan]")

#=================================================================================


def validate_product_fields(name, price, stock, category, description):
    """Valida los campos de un producto.
    Esta función verifica que los campos del producto cumplan con los requisitos mínimos.
    Args:
        name (str): Nombre del producto.
        price (float): Precio del producto.
        stock (int): Cantidad de stock del producto.
        category (str): Categoría del producto.
        description (str): Descripción del producto.
    Returns:
        list: Una lista de errores encontrados. Si no hay errores, la lista estará vacía
    """

    errors = []
    if not name or len(name) < 2:
        errors.append("The product name must have at least 2 characters.")
    try:
        price = float(str(price).replace(",", "."))
        if price < 1:
            errors.append("The price must be at least 1.")
    except ValueError:
        errors.append("The price must be a valid number.")
    try:
        stock = int(stock)
        if stock < 0:
            errors.append("Stock must be a non-negative integer.")
    except ValueError:
        errors.append("Stock must be a valid integer.")
    if not category or len(category) < 2:
        errors.append("The category must have at least 2 characters.")
    if not description or len(description) < 5:
        errors.append("The description must have at least 5 characters.")
    return errors

def validate_product_modification_fields(name=None, price=None, stock=None, category=None, description=None):
    """Valida los campos de modificación de un producto.
    Esta función verifica que los campos del producto a modificar cumplan con los requisitos mínimos.
    Args:
        name (str): Nuevo nombre del producto.
        price (float): Nuevo precio del producto.
        stock (int): Nueva cantidad de stock del producto.
        category (str): Nueva categoría del producto.
        description (str): Nueva descripción del producto.
    Returns:
        list: Una lista de errores encontrados. Si no hay errores, la lista estará vacía
    """

    errors = []
    if name is not None and name != "" and len(name) < 2:
        errors.append("The product name must have at least 2 characters.")
    if price is not None and price != "":
        try:
            price_val = float(str(price).replace(",", "."))
            if price_val < 1:
                errors.append("The price must be at least 1.")
        except ValueError:
            errors.append("The price must be a valid number.")
    if stock is not None and stock != "":
        try:
            stock_val = int(stock)
            if stock_val < 0:
                errors.append("Stock must be a non-negative integer.")
        except ValueError:
            errors.append("Stock must be a valid integer.")
    if category is not None and category != "" and len(category) < 2:
        errors.append("The category must have at least 2 characters.")
    if description is not None and description != "" and len(description) < 5:
        errors.append("The description must have at least 5 characters.")
    return errors