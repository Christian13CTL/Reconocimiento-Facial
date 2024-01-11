import os

import shutil

def copy_folders_without_content(source_dir, destination_dir):
    # Crea el directorio de destino si no existe
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Recorre todas las carpetas en el directorio fuente
    for folder_name in os.listdir(source_dir):
        # Ruta completa de la carpeta en el directorio fuente
        source_folder = os.path.join(source_dir, folder_name)

        # Si es una carpeta, copia solo la estructura sin contenido
        if os.path.isdir(source_folder):
            # Ruta completa de la carpeta en el directorio de destino
            destination_folder = os.path.join(destination_dir, folder_name)

            # Crea la carpeta en el directorio de destino
            os.makedirs(destination_folder)

            print(f"Copiada la carpeta: {source_folder} -> {destination_folder}")


# Ejemplo de uso
source_directory = "./Testeo"
destination_directory = "./Labels"

# Llama a la función para copiar las carpetas sin contenido
copy_folders_without_content(source_directory, destination_directory)
