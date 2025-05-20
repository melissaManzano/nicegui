# Dashboard con tarjetas de estadísticas
from nicegui import ui

# Título del dashboard
ui.label('Dashboard de Estadísticas').classes('text-h4')

# Fila de tarjetas con estadísticas
with ui.row().style('gap: 20px;'):
    # Tarjeta de Ventas
    with ui.card().style('background-color: #FFEBEE; width: 200px; height: 120px;'):
        ui.label('Ventas').style('font-weight: bold; font-size: 20px;')
        ui.label('$1,200').style('font-size: 24px; color: #C62828;')

    # Tarjeta de Usuarios
    with ui.card().style('background-color: #E3F2FD; width: 200px; height: 120px;'):
        ui.label('Usuarios').style('font-weight: bold; font-size: 20px;')
        ui.label('342').style('font-size: 24px; color: #1565C0;')

    # Tarjeta de Tickets
    with ui.card().style('background-color: #E8F5E9; width: 200px; height: 120px;'):
        ui.label('Tickets').style('font-weight: bold; font-size: 20px;')
        ui.label('18').style('font-size: 24px; color: #2E7D32;')

# Ejecutar la aplicación
ui.run()