# import cv2
# import os 

# dataPath="ImagenesRedimencionadas"
# peopleList= os.listdir(dataPath)
# print("Lista de personas: ", peopleList)
# #imprime la lista de las clases 

# face_recognizer = cv2.face.EigenFaceRecognizer_create()

# #Leyendo el modelo
# face_recognizer.read("modeloEngenface.xml")
# cap = cv2.VideoCapture("Imagenes y videos de/christiantest0.mp4")
# faceClassif = cv2.CascadeClassifier( cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
# while True :
#     ret, frame = cap.read()
#     if ret == False: break
#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     auxFrame = gray.copy()
#     #Copia del marco para mostrar en pantalla
#     faces = faceClassif.detectMultiScale(gray , 1.3 ,5 )

#     for (x,y,w,h) in faces:
#         rostro= auxFrame[y:y+h,x:x+w]
#         rostro = cv2.resize(rostro,(168,200), interpolation=cv2.INTER_CUBIC)
#         result = face_recognizer.predrict(rostro)
#         cv2.putText(frame,'{}'.format(result),(x,y-5), 1, 1.3 (255, 255, 0),1,cv2.LINE_AA)

#     cv2.imshow('frame',frame)
#     k= cv2.waitKey(1)
#     if k == 27:
#         break
# cap.release()
# cv2.destroyAllWindows()



import cv2
import os

dataPath = "Pruebas"
peopleList = os.listdir(dataPath)
print("Lista de personas: ", peopleList)

face_recognizer = cv2.face.EigenFaceRecognizer_create()
#lee el modelo
face_recognizer.read("modeloEngenface.xml")

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


        if result[1] < 12500:#los valores mas bajos o cercanos a cero quiere decir que el rostros tiene similitud a los entrenados
                    cv2.putText(frame, '{}'.format(peopleList[result[0]]), (x, y-25), 2, 1.1, (0, 255, 0), 1, cv2.LINE_AA)
                    cv2.rectangle(frame, (x,y), (x + w, y + h),(0, 255, 0),2)
        else:
                    cv2.putText(frame,'Desconocido', (x, y-20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                    cv2.rectangle(frame, (x,y), (x + w, y + h),(0, 0, 255),2)

    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
