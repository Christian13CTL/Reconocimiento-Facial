from PIL import Image
import os
# Ruta de la imagen a leer
ruta_imagen = "./Pruebas/Abraham/ADML (1).png_1.jpg"
#Dimensiones de la imagen: 168 x 200
# Abrir la imagen
imagen = Image.open(ruta_imagen)

# Obtener las dimensiones de la imagen
width, height = imagen.size

# Imprimir las dimensiones de la imagen
print(f"Dimensiones de la imagen: {width} x {height}")
