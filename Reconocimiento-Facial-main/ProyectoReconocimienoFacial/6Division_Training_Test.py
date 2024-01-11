import os
import random
import shutil

directorio_origen = './Entrenamiento1'
directorio_destino = './Testeo'
percentage_to_move = 0.076923

for root, dirs, files in os.walk(directorio_origen):
    for dir_name in dirs:
        source_folder = os.path.join(root, dir_name)
        destination_folder = os.path.join(directorio_destino, dir_name)
        os.makedirs(destination_folder, exist_ok=True)

        image_files = [file for file in os.listdir(source_folder) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        num_images = len(image_files)
        num_images_to_move = int(num_images * percentage_to_move)

        images_to_move = random.sample(image_files, num_images_to_move)
        for image in images_to_move:
            source_file = os.path.join(source_folder, image)
            destination_file = os.path.join(destination_folder, image)
            shutil.move(source_file, destination_file)
            # print(f"Moved: {source_file} -> {destination_file}")
print("Proceso completado")