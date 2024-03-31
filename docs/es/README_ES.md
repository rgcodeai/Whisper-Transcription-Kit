# **Kit de Transcripción con Whisper**

## **Descripción**

Este proyecto utiliza el modelo Whisper de OpenAI para transcribir archivos de audio y video a texto. Está diseñado para ser sencillo de utilizar, permitiendo a los usuarios convertir sus archivos multimedia en contenido escrito mediante tecnologías avanzadas de aprendizaje automático.

## **Requisitos**

- Python 3.8 o superior.
- Chocolatey
- CUDA (para usuarios con gpu NVIDIA)

## **Descripción de los Archivos**

- **`requirements.txt`**: Contiene una lista de los paquetes de Python necesarios para ejecutar los scripts de transcripción, incluyendo el modelo Whisper para el manejo de archivos multimedia.
- **`setup_environment.bat`**: Este script en formato batch está diseñado para preparar el entorno de Python requerido para el proyecto. Su función principal es automatizar varios procesos, incluyendo la creación de un entorno virtual y la instalación de las dependencias especificadas en **`requirements.txt`**. Además, se encarga de la instalación de FFmpeg a través de Chocolatey y de PyTorch versión 12.1.
- **`run_script.bat`**: Este archivo batch se utiliza para iniciar el proceso de transcripción. Proporciona un método sencillo para que se inicie la transcripción con un doble clic.
- **`transcribe.py`**: El script principal de Python que utiliza el modelo Whisper para transcribir archivos de audio y video. Incluye la lógica para el procesamiento de los archivos multimedia y la generación de la transcripción.

## **Estructura de Carpetas**

- **`input/`**: Carpeta donde los usuarios deben colocar los archivos de audio o video que desean transcribir.
- **`output/`**: Carpeta donde se guardarán las transcripciones generadas por el script. Cada transcripción se nombra de acuerdo con su archivo de origen. Las transcripciones se guardan en los formatos (srt, tsv, txt, vtt).

## **Instalación**

1. **Clonar el Proyecto**: Inicia clonando el repositorio o descargando los archivos del proyecto en tu máquina local.
2. **Configurar el Entorno**:
    - Navega hasta el directorio del proyecto.
    - Ejecuta **`setup_environment.bat`** como administrador. Este script creará un entorno virtual de Python e instalará las dependencias necesarias.

Consulta nuestra guía detallada para [instalar Whisper en Windows](https://mistercontenidos.com/como-instalar-whisper-en-windows-guia-sencilla-paso-a-paso/).

## **Uso**

1. **Preparar tus Archivos Multimedia**: Coloca los archivos de audio o video que deseas transcribir en la carpeta **`input/`**.
2. **Ejecutar la Transcripción**:
    - Haz doble clic en **`run_script.bat`** para iniciar el proceso de transcripción.
    - El script procesa automáticamente todos los archivos presentes en la carpeta **`input/`** y genera las transcripciones en la carpeta **`output/`**.
3. **Acceder a las Transcripciones**: Una vez completado el proceso de transcripción, podrás encontrar los textos resultantes en la carpeta **`output/`**. Cada archivo de transcripción llevará el nombre del archivo original para fácil identificación.

## Languages

- [Ingles](README.md)
- [Português](docs/pt/README_PT.md)