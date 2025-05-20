# Tabla simple con datos de usuarios
from nicegui import ui

# Título de la aplicación
ui.label('Tabla de Usuarios').classes('text-h4')

# Datos de ejemplo
datos = [
    {'Nombre': 'Ana', 'Edad': 21},
    {'Nombre': 'Luis', 'Edad': 23},
    {'Nombre': 'Carla', 'Edad': 22},
]

# Definición de columnas para la tabla
columnas = [
    {'name': 'Nombre', 'label': 'Nombre', 'field': 'Nombre'},
    {'name': 'Edad', 'label': 'Edad', 'field': 'Edad'},
]

# Crear tabla con los datos
ui.table(columns=columnas, rows=datos, row_key='Nombre')

# Ejecutar la aplicación
ui.run()