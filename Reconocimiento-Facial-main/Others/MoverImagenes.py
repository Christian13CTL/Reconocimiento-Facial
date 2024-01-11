import os
import shutil

# Directorio de origen
directorio_origen = 'Segundaiteracion'

# Directorio de destino
directorio_destino = 'DatasetImagenes'

# Obtener la lista de carpetas en el directorio de origen
carpetas_origen = os.listdir(directorio_origen)

# Recorrer cada carpeta en el directorio de origen
for carpeta in carpetas_origen:
    # Rutas de la carpeta de origen y destino correspondientes
    ruta_origen = os.path.join(directorio_origen, carpeta)
    ruta_destino = os.path.join(directorio_destino, carpeta)
    
    # Verificar si las rutas de origen y destino existen
    if os.path.exists(ruta_origen) and os.path.exists(ruta_destino):
        # Obtener la lista de archivos en la carpeta de origen
        archivos_origen = os.listdir(ruta_origen)
        
        # Recorrer cada archivo en la carpeta de origen y copiarlo a la carpeta de destino
        for archivo in archivos_origen:
            ruta_archivo_origen = os.path.join(ruta_origen, archivo)
            ruta_archivo_destino = os.path.join(ruta_destino, archivo)
            shutil.copy(ruta_archivo_origen, ruta_archivo_destino)
    else:
        print(f'La carpeta "{carpeta}" no existe en una de las ubicaciones.')
