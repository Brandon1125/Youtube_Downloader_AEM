# Guía para Crear un Entorno en Anaconda y Ejecutar el Script de Descarga de Videos

Este documento describe los pasos necesarios para crear un entorno en Anaconda, instalar las dependencias requeridas y ejecutar un script en Python para descargar videos de un canal de YouTube utilizando `yt-dlp`.

## Requisitos Previos
- Tener instalado [Anaconda](https://www.anaconda.com/)
- Acceso a internet

## 1. Crear un Entorno en Anaconda
Abre una terminal o Anaconda Prompt y ejecuta el siguiente comando para crear un nuevo entorno llamado `yt_downloader` con Python 3.9:

```bash
conda create --name yt_downloader python=3.9 -y
```

## 2. Activar el Entorno
Una vez creado el entorno, actívalo con el siguiente comando:

```bash
conda activate yt_downloader
```

## 3. Instalar `ffmpeg` con Conda
`ffmpeg` es necesario para la conversión de video y audio. Instálalo con:

```bash
conda install -c conda-forge ffmpeg -y
```

## 4. Instalar `yt-dlp` con Pip
`yt-dlp` es la herramienta utilizada para descargar los videos de YouTube. Instálala ejecutando:

```bash
pip install yt-dlp
```

Guarda el archivo y ejecútalo con el siguiente comando en la terminal:

```bash
python downloader.py
```

El script descargará todos los videos del canal especificado en la carpeta `videos`.

## Errores
En dado caso que se detenga la descarga, vuelve a ejecutar el script y volverá a reanudar la descarga desde el último video descargado.
