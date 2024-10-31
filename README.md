# Proyecto de Manipulación y Visualización de Archivos GIF

**Autor:** Rubén Fernando Espinoza Fernández  
**Carnet:** 1525620  
**Sistema Operativo:** Windows 11  
**Versión de Python:** 3.12.6  

Este proyecto fue desarrollado como parte del curso "Manejo e Implementación de Archivos". La aplicación permite analizar, visualizar y editar metadatos de archivos GIF. Incluye una interfaz gráfica construida con PyQt6 y una versión en consola, ofreciendo flexibilidad en su uso.

## Descripción de la Aplicación

La aplicación permite:
- Cargar una carpeta que contenga archivos GIF.
- Extraer información clave de cada archivo GIF, como versión, tamaño de la imagen, cantidad de colores, color de fondo, cantidad de frames, y comentarios.
- Guardar los metadatos extraídos en un archivo `.txt` para fácil consulta y edición.
- Editar los metadatos almacenados en el archivo `.txt` sin modificar el archivo GIF original.

## Requisitos

- **Python 3.12.6** o superior
- **Bibliotecas**: 
  - PyQt6 (para la versión gráfica)
  - os y datetime (bibliotecas estándar de Python)
Instala PyQt6 ejecutando:
pip install PyQt6
