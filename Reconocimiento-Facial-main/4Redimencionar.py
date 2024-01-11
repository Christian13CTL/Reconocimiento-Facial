import os
from PIL import Image

# Directorio de entrada con las carpetas de imágenes originales
directorio_entrada = "p1"

# Dimensiones deseadas para las imágenes redimensionadas
new_width = 168
new_height = 200

# Directorio de salida para las imágenes redimensionadas
directorio_salida = "pruebas"

# Crear el directorio de salida si no existe
if not os.path.exists(directorio_salida):
    os.makedirs(directorio_salida)

# Obtener la lista de carpetas en el directorio de entrada
carpetas = os.listdir(directorio_entrada)

# Procesar cada carpeta de imágenes
for carpeta in carpetas:
    # Ruta de la carpeta de entrada
    ruta_carpeta_entrada = os.path.join(directorio_entrada, carpeta)

    # Ruta de la carpeta de salida correspondiente
    ruta_carpeta_salida = os.path.join(directorio_salida, carpeta)

    # Crear la carpeta de salida correspondiente si no existe
    if not os.path.exists(ruta_carpeta_salida):
        os.makedirs(ruta_carpeta_salida)

    # Obtener la lista de archivos en la carpeta de entrada
    archivos = os.listdir(ruta_carpeta_entrada)

    # Redimensionar cada imagen en la carpeta de entrada
    for archivo in archivos:
        # Ruta de la imagen original
        ruta_imagen = os.path.join(ruta_carpeta_entrada, archivo)

        # Abrir la imagen original
        imagen = Image.open(ruta_imagen)

        # Redimensionar la imagen
        imagen_redimensionada = imagen.resize((new_width, new_height))

        # Guardar la imagen redimensionada en la carpeta de salida correspondiente
        ruta_salida = os.path.join(ruta_carpeta_salida, archivo)
        imagen_redimensionada.save(ruta_salida)

        print(f"Imagen redimensionada guardada en {ruta_salida}")

print("Proceso completado.")
