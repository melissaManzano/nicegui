from nicegui import ui

# Puedes usar una URL de un archivo de audio público o uno local en tu proyecto
AUDIO_URL = 'https://samplelib.com/lib/preview/mp3/sample-3s.mp3'

ui.label('🎵 Reproductor de audio').style('font-size: 20px; font-weight: bold; margin-bottom: 10px;')

# Control de audio
audio = ui.audio(AUDIO_URL, autoplay=False, controls=True)

# Botones para controlar manualmente desde Python
with ui.row().style('margin-top: 10px; gap: 10px;'):
    ui.button('Reproducir', on_click=lambda: audio.run_method('play'))
    ui.button('Pausar', on_click=lambda: audio.run_method('pause'))

ui.run()
