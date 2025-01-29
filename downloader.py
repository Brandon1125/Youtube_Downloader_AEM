import os
import yt_dlp

def descargar_videos_canal(url_canal, carpeta_destino="videos"):  
    opciones = {
        'outtmpl': f'{carpeta_destino}/%(title)s.%(ext)s',  # Guardar con el título del video
        'format': 'bestvideo+bestaudio/best',  # Mejor calidad disponible
        'merge_output_format': 'mkv',  # Formato final
        'noplaylist': True,  # Descargar todos los videos (incluyendo playlists)
        'quiet': False,  # Mostrar información en la consola
        'force_ipv4': True
    }
    
    # Crear carpeta destino si no existe
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
    
    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url_canal])

if __name__ == "__main__":
    url_canal = "https://www.youtube.com/@AgenciaEspacialMexicana"
    descargar_videos_canal(url_canal)
