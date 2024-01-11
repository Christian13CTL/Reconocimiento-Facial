import cv2
import os

# Cargar el clasificador preentrenado de detección de rostros
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Ruta del directorio de entrada con las carpetas de imágenes
input_directory = "ImagenesSinFondo"

# Ruta del directorio de salida donde se guardarán los rostros recortados
output_directory = "ImagenesRostros"

# Crear el directorio de salida si no existe
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Obtener la lista de carpetas en el directorio de entrada
folders = os.listdir(input_directory)

# Procesar cada carpeta dentro del directorio de entrada
for folder in folders:
    # Rutas de entrada y salida
    input_folder = os.path.join(input_directory, folder)
    output_folder = os.path.join(output_directory, folder)

    # Crear la carpeta de salida para la carpeta actual si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Obtener la lista de archivos en la carpeta de entrada
    files = os.listdir(input_folder)

    # Procesar cada archivo de la carpeta de entrada
    for file in files:
        # Rutas de entrada y salida para cada archivo
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, f"rostro_recortado_{file}")

        # Leer la imagen
        image = cv2.imread(input_path)

        # Convertir la imagen a escala de grises
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detectar rostros en la imagen
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

        # Verificar si se detectaron rostros en la imagen
        if len(faces) > 0:
            # Obtener las coordenadas y dimensiones del primer rostro detectado
            x, y, w, h = faces[0]

            # Recortar la imagen del rostro
            face_image = image[y : y + h, x : x + w]

            # Guardar la imagen del rostro recortado
            cv2.imwrite(output_path, face_image)
            print(f"Rostro recortado de {file} en la carpeta {folder} guardado exitosamente.")
        else:
            print(f"No se detectaron rostros en {file} en la carpeta {folder}.")
