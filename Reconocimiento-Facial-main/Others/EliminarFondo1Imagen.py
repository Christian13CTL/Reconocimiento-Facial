from rembg import remove
import io  # Importar el módulo io

input_path = "ImagenesRostros/Abraham Danilo Miranda Lopez/rostro_recortado_ADML (8).png"
output_path = "pruebas/rostro_recortado_ADML1 (8).png"

with open(input_path, "rb") as i:
    with open(output_path, "wb") as o:
        input = i.read()
        output = remove(input)
        o.write(output)
