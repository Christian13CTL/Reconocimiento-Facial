# import os
# import imgaug.augmenters as iaa
# from PIL import Image
# import numpy as np


# # Ruta de la imagen original
# ruta_imagen = "ImagenesRedimencionadas/Abraham Danilo Miranda Lopez/rostro_recortado_ADML (2).png"

# # Número de imágenes aumentadas que deseas generar
# numero_imagenes_aumentadas = 20

# # Directorio de salida para las imágenes aumentadas
# directorio_salida = "aleatorio"

# # Crear el directorio de salida si no existe
# if not os.path.exists(directorio_salida):
#     os.makedirs(directorio_salida)

# # Definir una semilla para controlar la generación de números aleatorios
# semilla = 123

# # Definir las transformaciones de aumento de datos
# seq = iaa.Sequential([
#     iaa.Affine(rotate=(-45, 360)),
#     iaa.Affine(scale={"x": (0.8, 1.2), "y": (0.8, 1.2)}),
#     iaa.AdditiveGaussianNoise(scale=(0, 0.15* 255)),
#     #iaa.Multiply((0.8, 1.2), per_channel=True),
#     iaa.MultiplyAndAddToBrightness(mul=(0.8, 1.2), add=(-30, 30)),
# ], random_order=True, random_state=semilla)

# # Abrir la imagen original
# imagen = Image.open(ruta_imagen)

# # Generar las imágenes aumentadas
# for i in range(numero_imagenes_aumentadas):
#     # Convertir la imagen en un arreglo numpy
#     imagen_array = np.array(imagen)

#     # Aplicar las transformaciones a la imagen
#     imagen_aug = seq(image=imagen_array)

#     # Convertir la imagen aumentada de nuevo a PIL Image
#     imagen_aug_pil = Image.fromarray(imagen_aug.astype('uint8'))

#     # Guardar la imagen aumentada con un nombre único en la carpeta de salida
#     ruta_salida = os.path.join(directorio_salida, f"imagen_aumentada_{i+1}1.jpg")
#     imagen_aug_pil.save(ruta_salida)

#     print(f"Imagen aumentada {i+1} guardada en {ruta_salida}")
#################################################################################

# import os
# import imgaug.augmenters as iaa
# from PIL import Image
# import numpy as np

# # Directorio de entrada que contiene las carpetas con imágenes originales
# directorio_entrada = "ImagenesRedimencionadas"

# # Directorio de salida para las imágenes aumentadas
# directorio_salida = "aleatorio"

# # Crear el directorio de salida si no existe
# if not os.path.exists(directorio_salida):
#     os.makedirs(directorio_salida)

# # Definir una semilla para controlar la generación de números aleatorios
# semilla = 123

# # Transformación de rotación
# transformacion_rotacion = iaa.Affine(rotate=(-45, 360))

# # Transformación de escala
# transformacion_escala = iaa.Affine(scale={"x": (0.8, 1.2), "y": (0.8, 1.2)})

# # Transformación de ruido gaussiano
# transformacion_ruido = iaa.AdditiveGaussianNoise(scale=(0, 0.15 * 255))

# # Transformación de multiplicación de brillo
# transformacion_brillo = iaa.MultiplyAndAddToBrightness(mul=(0.8, 1.2), add=(-30, 30))

# # Transformación de multiplicación de iluminación
# transformacion_iluminacion = iaa.Multiply((0.8, 1.2), per_channel=True)

# # Recorrer los directorios y archivos dentro del directorio de entrada
# for raiz, carpetas, archivos in os.walk(directorio_entrada):
#     # Recorrer cada archivo en el directorio actual
#     for archivo in archivos:
#         # Ruta de la imagen original
#         ruta_imagen = os.path.join(raiz, archivo)

#         # Abrir la imagen original
#         imagen = Image.open(ruta_imagen)

#         # Convertir la imagen al modo RGB si tiene un canal alfa
#         if imagen.mode == 'RGBA':
#             imagen = imagen.convert('RGB')

#         # Convertir la imagen a un arreglo numpy
#         imagen_array = np.array(imagen)

#         # Generar las imágenes aumentadas
#         for i in range(20):
#             # Crear una copia de la imagen original
#             imagen_aumentada = imagen_array.copy()

#             # Aplicar cada transformación individualmente en cada iteración
#             imagen_aumentada = transformacion_rotacion(image=imagen_aumentada)
#             imagen_aumentada = transformacion_escala(image=imagen_aumentada)
#             imagen_aumentada = transformacion_ruido(image=imagen_aumentada)
#             imagen_aumentada = transformacion_brillo(image=imagen_aumentada)
#             imagen_aumentada = transformacion_iluminacion(image=imagen_aumentada)

#             # Convertir la imagen aumentada de nuevo a PIL Image
#             imagen_aug_pil = Image.fromarray(imagen_aumentada.astype('uint8'))

#             # Guardar la imagen aumentada con un nombre único en el directorio de salida
#             ruta_salida = os.path.join(directorio_salida, os.path.relpath(raiz, directorio_entrada), f"{archivo}_{i+1}.jpg")
#             os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
#             imagen_aug_pil.save(ruta_salida)

# print("Proceso completado.")
#############################################################




import os
import imgaug.augmenters as iaa
from PIL import Image
import numpy as np
import time
import psutil

# Directorio de entrada que contiene las carpetas con imágenes originales
directorio_entrada = "pruebas"

# Directorio de salida para las imágenes aumentadas
directorio_salida = "aleatorio"

# Crear el directorio de salida si no existe
if not os.path.exists(directorio_salida):
    os.makedirs(directorio_salida)

# Definir una semilla para controlar la generación de números aleatorios
semilla = 123

# Transformación de rotación
transformacion_rotacion = iaa.Affine(rotate=(-45, 360))

# Transformación de escala
transformacion_escala = iaa.Affine(scale={"x": (0.8, 1.2), "y": (0.8, 1.2)})

# Transformación de ruido gaussiano
transformacion_ruido = iaa.AdditiveGaussianNoise(scale=(0, 0.15 * 255))

# Transformación de multiplicación de brillo
transformacion_brillo = iaa.MultiplyAndAddToBrightness(mul=(0.8, 1.2), add=(-30, 30))

# Transformación de multiplicación de iluminación
transformacion_iluminacion = iaa.Multiply((0.8, 1.2), per_channel=True)

# Transformación de espejo
transformacion_espejo = iaa.Fliplr(1.0)

def main():
    # Recorrer los directorios y archivos dentro del directorio de entrada
    tiempo_inicial = time.time()  # Tiempo inicial
    total_iteraciones = 0

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
                # Crear una copia de la imagen original
                imagen_aumentada = imagen_array.copy()

                # Aplicar cada transformación individualmente en cada iteración
                imagen_aumentada = transformacion_rotacion(image=imagen_aumentada)
                imagen_aumentada = transformacion_escala(image=imagen_aumentada)
                imagen_aumentada = transformacion_ruido(image=imagen_aumentada)
                imagen_aumentada = transformacion_brillo(image=imagen_aumentada)
                imagen_aumentada = transformacion_iluminacion(image=imagen_aumentada)
                imagen_aumentada = transformacion_espejo(image=imagen_aumentada)

                # Convertir la imagen aumentada de nuevo a PIL Image
                imagen_aug_pil = Image.fromarray(imagen_aumentada.astype('uint8'))

                # Guardar la imagen aumentada con un nombre único en el directorio de salida
                ruta_salida = os.path.join(directorio_salida, os.path.relpath(raiz, directorio_entrada), f"{archivo}_{i+1}.jpg")
                os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
                imagen_aug_pil.save(ruta_salida)

                total_iteraciones += 1

    tiempo_final = time.time()  # Tiempo final
    tiempo_total = tiempo_final - tiempo_inicial
    costo_computacional = tiempo_total / total_iteraciones if total_iteraciones > 0 else 0

    print(f"Proceso completado. Tiempo total: {tiempo_total:.2f} segundos")
    print(f"Costo computacional por iteracion: {costo_computacional:.4f} segundos")
    
    # Retornar el tiempo total, costo computacional por iteración y total de iteraciones
    return tiempo_total, costo_computacional, total_iteraciones

# Ejecutar el código principal
if __name__ == '__main__':
    tiempo_total, costo_computacional, total_iteraciones = main()

# Calcular el consumo de memoria
pid = os.getpid()
process = psutil.Process(pid)
consumo_memoria_total = process.memory_info().rss / (1024 * 1024)  # Convertir a MiB

# Imprimir los valores totales al final de la ejecución
print("----- Valores totales -----")
total_iteraciones *= 20  # Multiplicar por 20 para obtener el total de iteraciones
costo_computacional_total = tiempo_total / total_iteraciones if total_iteraciones > 0 else 0

print(f"Tiempo total: {tiempo_total:.2f} segundos")
print(f"Costo computacional total por iteracion: {costo_computacional_total:.4f} segundos")
print(f"Consumo de memoria total: {consumo_memoria_total:.2f} MB")
