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
   git clone https://github.com/QuimCode/Iniciacion-Python.git
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
