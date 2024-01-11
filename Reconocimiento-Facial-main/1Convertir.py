# from PIL import Image
# import pillow_heif


# pillow_heif.register_heif_opener()

# img = Image.open("20230628_143543073_iOS.heic")
# img.save("image_name.png", format("png"))

# import os
# from PIL import Image
# import pillow_heif

# pillow_heif.register_heif_opener()


# def convert_heic_images_to_png(input_folder, output_folder):
#     # Crea la carpeta de salida si no existe
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     # Recorre todos los archivos en la carpeta de entrada
#     for filename in os.listdir(input_folder):
#         if filename.endswith(".heic"):
#             # Ruta completa del archivo de entrada
#             input_file = os.path.join(input_folder, filename)

#             # Nombre de archivo sin extensión
#             file_name = os.path.splitext(filename)[0]

#             # Ruta completa del archivo de salida
#             output_file = os.path.join(output_folder, file_name + ".png")

#             # Convierte la imagen HEIC a PNG
#             img = Image.open(input_file)
#             img.save(output_file, format="PNG")

#             print(f"Convertido {input_file} -> {output_file}")


# # Rutas de la carpeta de entrada y la carpeta de salida
# input_folder = "Imagenes/Bryan Eduardo Martínez Núñez"
# output_folder = "destino/Bryan Eduardo Martínez Núñez"

# # Llama a la función para convertir las imágenes
# convert_heic_images_to_png(input_folder, output_folder)

import os
from PIL import Image
import pillow_heif

pillow_heif.register_heif_opener()


def convert_heic_images_in_directory(input_directory, output_directory):
    # Crea el directorio de salida si no existe
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Recorre todas las carpetas en el directorio de entrada
    for folder_name in os.listdir(input_directory):
        # Ruta completa de la carpeta en el directorio de entrada
        input_folder = os.path.join(input_directory, folder_name)

        # Si es una carpeta, convierte las imágenes y las almacena en el directorio de destino
        if os.path.isdir(input_folder):
            # Ruta completa del directorio de destino para las imágenes de la carpeta actual
            output_folder = os.path.join(output_directory, folder_name)

            # Crea el directorio de destino para las imágenes de la carpeta actual
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            # Recorre todos los archivos en la carpeta de entrada
            for filename in os.listdir(input_folder):
                if filename.endswith(".heic"):
                    # Ruta completa del archivo de entrada
                    input_file = os.path.join(input_folder, filename)

                    # Nombre de archivo sin extensión
                    file_name = os.path.splitext(filename)[0]

                    # Ruta completa del archivo de salida
                    output_file = os.path.join(output_folder, file_name + ".png")

                    # Convierte la imagen HEIC a PNG
                    img = Image.open(input_file)
                    img.save(output_file, format="PNG")

                    print(f"Convertido {input_file} -> {output_file}")


# Directorio de entrada y directorio de salida
input_directory = "Imagenes"
output_directory = "destino"

# Llama a la función para convertir las imágenes
convert_heic_images_in_directory(input_directory, output_directory)
