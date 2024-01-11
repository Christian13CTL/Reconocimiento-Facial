import os
from rembg import remove
from tqdm import tqdm

input_directory = "Imagenes"
output_directory = "ImagenesSinFondo"

# Crea el directorio de salida si no existe
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Obtiene la lista de carpetas en el directorio de entrada
folders = [folder for folder in os.listdir(input_directory) if os.path.isdir(os.path.join(input_directory, folder))]

# Configura la barra de progreso
progress_bar = tqdm(total=len(folders), desc="Procesamiento de imágenes", unit="carpeta")

# Procesa cada carpeta del directorio de entrada
for folder in folders:
    # Rutas de entrada y salida
    input_folder = os.path.join(input_directory, folder)
    output_folder = os.path.join(output_directory, folder)

    # Crea la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Obtiene la lista de archivos en la carpeta de entrada
    files = os.listdir(input_folder)

    # Procesa cada archivo de la carpeta de entrada
    for file in files:
        # Rutas de entrada y salida
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, file)

        # Leer el archivo de entrada
        with open(input_path, "rb") as i:
            with open(output_path, "wb") as o:
                input_data = i.read()
                output_data = remove(input_data)
                o.write(output_data)

    progress_bar.update(1)  # Actualiza la barra de progreso
    progress_bar.set_postfix({"Carpeta": folder})

progress_bar.close()  # Cierra la barra de progreso
