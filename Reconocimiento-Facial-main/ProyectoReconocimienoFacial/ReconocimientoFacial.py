import cv2
import os
import pyttsx3


engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Ajusta la velocidad de reproducción (opcional)
engine.runAndWait()
nombre_actual = None
def leer_nombre(nombre):
    global nombre_actual, persona_detectada
    if nombre != nombre_actual:
        nombre_actual = nombre
        if nombre == 'Desconocido':
            engine.say(f"Rostro, {nombre}!")
        else:
            engine.say(f"Rostro de, {nombre}!")
        engine.runAndWait()
######
dataPath = "./Entrenamiento"
peopleList = os.listdir(dataPath)
print("Lista de personas: ", peopleList)

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
#lee el modelo
face_recognizer.read("modeloLBPHFace.xml")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()
    if ret == False:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()

    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        rostro = auxFrame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (168, 200), interpolation=cv2.INTER_CUBIC)
        result = face_recognizer.predict(rostro)  # Corrección: predicción del rostro

        cv2.putText(frame, '{}'.format(result), (x, y-5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)


        if result[1] < 95: #los valores mas bajos o cercanos a cero quiere decir que el rostros tiene similitud a los entrenados
                    nombre =peopleList[result[0]]
                    leer_nombre(nombre)
                    cv2.putText(frame, '{}'.format(peopleList[result[0]]), (x, y-25), 2, 1.1, (0, 255, 0), 1, cv2.LINE_AA)
                    cv2.rectangle(frame, (x,y), (x + w, y + h),(0, 255, 0),2)
        else:
                    nombre ='Desconocido'
                    cv2.putText(frame,'Desconocido', (x, y-20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                    cv2.rectangle(frame, (x,y), (x + w, y + h),(0, 0, 255),2)

    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
