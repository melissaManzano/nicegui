from nicegui import ui
#Función para que cuando se nevi de la notificacion de que se ha registrado el usuario
def enviar():
 ui.notify(f'Usuario {nombre.value} registrado con éxito')
#Ingresa nombre, email, contraseña
nombre = ui.input(label='Nombre')
email = ui.input(label='Email')
contraseña = ui.input(label='Contraseña', password=True)
#Botón para aceptar términos
ui.checkbox('Acepto los términos')
#Botón para enviar el formulario y llamar la función enviar para aparecer la notificación
ui.button('Registrarse', on_click=enviar)
ui.run()