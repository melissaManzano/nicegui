# Selector de color favorito y tema oscuro
from nicegui import ui

def mostrar():
    """Muestra las preferencias seleccionadas (color y tema oscuro)."""
    ui.notify(f'Color: {color.value}, Tema oscuro: {tema.value}', type='positive')

# Título de la aplicación
ui.label('Configuración de Preferencias').classes('text-h4')

# Selector de color
color = ui.select(['Rojo', 'Verde', 'Azul'], label='Color favorito', value='Rojo')

# Interruptor para tema oscuro
tema = ui.switch('Tema oscuro')

# Botón para guardar preferencias
ui.button('Guardar preferencias', on_click=mostrar)

# Ejecutar la aplicación
ui.run()