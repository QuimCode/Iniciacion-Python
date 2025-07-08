SPANISH & ENGLISH

# BigSmallWorld

**BigSmallWorld** es una aplicación de consola en Python para la gestión de usuarios y productos, con almacenamiento en SQLite y una interfaz interactiva usando [rich](https://github.com/Textualize/rich) y [questionary](https://github.com/tmbo/questionary).

## Características

- Registro, login y eliminación de usuarios.
- Modificación de perfil de usuario.
- Alta, baja, modificación y consulta de productos.
- Filtros y búsquedas por stock.
- Interfaz amigable en consola.

## Requisitos

- Python 3.10 o superior

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu_usuario/BigSmallWorld.git
   cd BigSmallWorld
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecuta la aplicación:**
   ```bash
   python main.py
   ```

## Dependencias principales

- rich
- questionary

## Estructura del proyecto

```
BigSmallWorld's.py/
│
├── data/
│   ├── database_user.db
│   ├── database.py
│   └── ...
├── products_functions.py
├── register_functions.py
├── utilities_menu_bsm.py
├── main.py
└── ...
```

## Notas

- La base de datos SQLite se crea automáticamente al ejecutar la app.
- Si tienes problemas con las dependencias, revisa el archivo `requirements.txt`.

=============================================================================================

#BigSmallWorld

**BigSmallWorld** is a Python console application for user and product management, with SQLite storage and an interactive interface using [rich](https://github.com/Textualize/rich) and [questionary](https://github.com/tmbo/questionary).

## Features

- User registration, login, and deletion.
- User profile modification.
- Product addition, deletion, modification, and query.
- Filters and searches by stock.
- User-friendly console interface.

## Requirements

- Python 3.10 or higher

## Installation

1. Clone the repository:
bash
git clone https://github.com/your_user/BigSmallWorld.git
cd BigSmallWorld
bash

2. Install the dependencies:
bash
pip install -r requirements.txt
bash

3. Run the application:
bash
python main.py
bash

## Main Dependencies

- rich
- questionary

## Project Structure

bigsmallworld.py/
│
├── data/
│ ├── database_user.db
│ ├── database.py
│ └── ...
├── products_functions.py
├── register_functions.py
├── utilities_menu_bsm.py
├── main.py
└── ...
```

## Notes

- The SQLite database is created automatically when you run the app.
- If you have problems with dependencies, check the `requirements.txt` file.
