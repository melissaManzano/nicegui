from nicegui import ui

# Definir las coordenadas (ejemplo: Ciudad de México)
lat = 20.08406
lon = -98.77505

# Crear un enlace de Google Maps con la ubicación
map_url = f"https://www.google.com/maps?q={lat},{lon}&hl=es"

# Crear un botón que ejecuta JavaScript para abrir Google Maps en una nueva ventana
ui.label('📍 Ubicación en el mapa').style('font-size: 20px; font-weight: bold; margin-bottom: 10px;')
ui.button('Ver mapa en Google Maps', on_click=lambda: ui.run_javascript(f'window.open("{map_url}", "_blank")'))

ui.run()
