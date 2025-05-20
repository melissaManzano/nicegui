from nicegui import ui

# Título
ui.label('Calculadora de suma simple').classes('text-h4')

# Entrada de datos
num1 = ui.number(label='Número 1', value=0)
num2 = ui.number(label='Número 2', value=0)

# Resultado
resultado = ui.label('Resultado: 0').classes('text-h6')

# Funciones de operaciones
def suma():
    suma = num1.value + num2.value
    resultado.set_text(f'Resultado: {suma}')
    ui.notify(f'La suma es: {suma}')

def resta():
    resta = num1.value - num2.value
    resultado.set_text(f'Resultado: {resta}')
    ui.notify(f'La resta es: {resta}')

def multi():
    multi = num1.value * num2.value
    resultado.set_text(f'Resultado: {multi}')
    ui.notify(f'La multiplicación es: {multi}')

def division():
    try:
        if num2.value == 0:
            raise ZeroDivisionError
        division = num1.value / num2.value
        resultado.set_text(f'Resultado: {division}')
        ui.notify(f'La división es: {division}')
    except ZeroDivisionError:
        resultado.set_text('Error: División por cero')
        ui.notify('Error: No se puede dividir por cero', type='error')

# Botones
with ui.row():
    ui.button('Sumar', on_click=suma)
    ui.button('Restar', on_click=resta)
    ui.button('Multiplicar', on_click=multi)
    ui.button('Dividir', on_click=division)

# Ejecutar la app
ui.run()