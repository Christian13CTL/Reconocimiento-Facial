import os
import imgaug.augmenters as iaa
from PIL import Image
import numpy as np

# Directorio de entrada que contiene las carpetas con imágenes originales
directorio_entrada = "dataAugmentationImagenes"

# Directorio de salida para las imágenes aumentadas
directorio_salida = "Segundaiteracion"

# Crear el directorio de salida si no existe
if not os.path.exists(directorio_salida):
    os.makedirs(directorio_salida)

# Definir una semilla para controlar la generación de números aleatorios
semilla = 123

# Definir las transformaciones de aumento de datos
seq = iaa.Sequential([
    iaa.Affine(rotate=(-45, 360)),
    iaa.Affine(scale={"x": (0.8, 1.2), "y": (0.8, 1.2)}),
    iaa.AdditiveGaussianNoise(scale=(0, 0.15 * 255)),
    iaa.Multiply((0.8, 1.2), per_channel=True),
], random_order=True, random_state=semilla)

# Recorrer los directorios y archivos dentro del directorio de entrada
for raiz, carpetas, archivos in os.walk(directorio_entrada):
    # Recorrer cada archivo en el directorio actual
    for archivo in archivos:
        # Ruta de la imagen original
        ruta_imagen = os.path.join(raiz, archivo)

        # Abrir la imagen original
        imagen = Image.open(ruta_imagen)

        # Convertir la imagen al modo RGB si tiene un canal alfa
        if imagen.mode == 'RGBA':
            imagen = imagen.convert('RGB')

        # Convertir la imagen a un arreglo numpy
        imagen_array = np.array(imagen)

        # Generar las imágenes aumentadas
        for i in range(20):
            # Aplicar las transformaciones a la imagen
            imagen_aug = seq(image=imagen_array)

            # Convertir la imagen aumentada de nuevo a PIL Image
            imagen_aug_pil = Image.fromarray(imagen_aug.astype('uint8'))

            # Guardar la imagen aumentada con un nombre único en el directorio de salida
            ruta_salida = os.path.join(directorio_salida, os.path.relpath(raiz, directorio_entrada), f"{archivo}_{i+1}.jpg")
            os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
            imagen_aug_pil.save(ruta_salida)

            #print(f"Imagen aumentada {i+1} de {archivo} guardada en {ruta_salida}")

print("Proceso completado.")
