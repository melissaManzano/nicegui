# Calculadora de edad de mascota en años perrunos
from nicegui import ui

def calcular():
    """Calcula la edad de la mascota en años perrunos (edad humana * 7)."""
    try:
        edad_mascota = int(humano.value) * 7
        resultado.set_text(f'Edad estimada en años perrunos: {edad_mascota}')
        ui.notify(f'Edad calculada: {edad_mascota} años perrunos', type='positive')
    except ValueError:
        resultado.set_text('Error: Ingresa un número válido')
        ui.notify('Por favor, ingresa un número válido', type='error')

# Título de la aplicación
ui.label('Calculadora de Edad de Mascota').classes('text-h4')

# Campo de entrada numérica
humano = ui.number(label='Edad humana', value=0).props('clearable')

# Etiqueta para mostrar el resultado
resultado = ui.label('Edad estimada en años perrunos: 0')

# Botón para calcular
ui.button('Calcular edad de mascota', on_click=calcular)

# Ejecutar la aplicación
ui.run()