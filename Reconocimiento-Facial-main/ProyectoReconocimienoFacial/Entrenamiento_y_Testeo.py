import cv2
import os
import numpy as np
import psutil

def load_data(dataPath):
    peopleList = os.listdir(dataPath)
    print("\nLista de personas: ", peopleList)

    labels = []
    facesData = []
    label = 0

    for nameDir in peopleList:
        personPath = dataPath + "/" + nameDir
        for fileName in os.listdir(personPath):
            labels.append(label)
            facesData.append(cv2.imread(personPath + "/" + fileName, 0))
            image = cv2.imread(personPath + "/" + fileName, 0)
        label += 1

    return labels, facesData

def train_model(labels, facesData):
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    print("\nEntrenando....")
    start_time = cv2.getTickCount()
    face_recognizer.train(facesData, np.array(labels))
    end_time = cv2.getTickCount()
    time_taken = (end_time - start_time) / cv2.getTickFrequency()
    return face_recognizer, time_taken

def evaluate_model(face_recognizer, data_labels, data_faces):
    predictions = []
    for test_image in data_faces:
        test_image_resized = cv2.resize(test_image, (train_facesData[0].shape[1], train_facesData[0].shape[0]))
        label, confidence = face_recognizer.predict(test_image_resized)
        predictions.append(label)

    accuracy = np.mean(np.array(predictions) == np.array(data_labels))
    return accuracy

def compute_resource_usage():
    process = psutil.Process(os.getpid())
    memory_usage = process.memory_info().rss / 1024 / 1024
    return memory_usage

dataPath = "./Entrenamiento"
testDataPath = "./Testeo"

# Carga de datos de entrenamiento
train_labels, train_facesData = load_data(dataPath)

# Entrenamiento del modelo
face_recognizer, train_time = train_model(train_labels, train_facesData)

# Cálculo de recursos utilizados en entrenamiento
train_memory_usage = compute_resource_usage()

# Evaluación en conjunto de entrenamiento
train_accuracy = evaluate_model(face_recognizer, train_labels, train_facesData)

print("\nExactitud en el conjunto de entrenamiento: {:.2%}".format(train_accuracy))
print("Consumo total de memoria en entrenamiento: {:.2f} MB".format(train_memory_usage))
print("Tiempo total de entrenamiento: {:.2f} segundos".format(train_time))

# Carga de datos de prueba
test_labels, test_facesData = load_data(testDataPath)

# Cálculo de recursos utilizados en prueba
test_memory_usage = compute_resource_usage()

# Evaluación en conjunto de prueba
test_accuracy = evaluate_model(face_recognizer, test_labels, test_facesData)

print("\nExactitud en el conjunto de prueba: {:.2%}".format(test_accuracy))
print("Consumo total de memoria en prueba: {:.2f} MB".format(test_memory_usage))

# Cálculo del costo computacional en entrenamiento y prueba
train_cost = train_memory_usage * train_time
test_cost = test_memory_usage * train_time

print("Costo computacional total en entrenamiento: {:.2f} MB-seconds".format(train_cost))
print("Costo computacional total en prueba: {:.2f} MB-seconds".format(test_cost))

# Almacenar el modelo obtenido
print("\nEntrenamiento terminado")
face_recognizer.write("modeloLBPHFace.xml")
