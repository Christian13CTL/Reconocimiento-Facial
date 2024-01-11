import cv2
import os
import numpy as np

dataPath="Pruebas"
peopleList= os.listdir(dataPath)
print("Lista de personas: ", peopleList)
#imprime la lista de las clases 

labels=[]
facesData=[]
label = 0

for nameDir in peopleList:
  personPath = dataPath + "/"+ nameDir
  print("Leyendo las imagenes")
  for fileName in os.listdir(personPath):
    #print("Rostros: ", nameDir+"/"+fileName)
    labels.append(label)
    facesData.append(cv2.imread(personPath+"/"+fileName,0))
    image=cv2.imread(personPath+"/"+fileName,0)
#     cv2.imshow("image",image)
#     cv2.waitKey(10)
# cv2.destroyAllWindows
  label=label+1

#print("Labels: ",labels)
print("Numero de etiquetas 0: ",np.count_nonzero(np.array(labels)==0))
print("Numero de etiquetas 1: ",np.count_nonzero(np.array(labels)==1))
# print("Numero de etiquetas 2: ",np.count_nonzero(np.array(labels)==2))
# print("Numero de etiquetas 3: ",np.count_nonzero(np.array(labels)==3))
# print("Numero de etiquetas 4: ",np.count_nonzero(np.array(labels)==4))
# print("Numero de etiquetas 5: ",np.count_nonzero(np.array(labels)==5))
# print("Numero de etiquetas 6: ",np.count_nonzero(np.array(labels)==6))
# print("Numero de etiquetas 7: ",np.count_nonzero(np.array(labels)==7))
# print("Numero de etiquetas 8: ",np.count_nonzero(np.array(labels)==8))
# print("Numero de etiquetas 9: ",np.count_nonzero(np.array(labels)==9))
# print("Numero de etiquetas 10: ",np.count_nonzero(np.array(labels)==10))
# print("Numero de etiquetas 11: ",np.count_nonzero(np.array(labels)==11))
# print("Numero de etiquetas 12: ",np.count_nonzero(np.array(labels)==12))
# print("Numero de etiquetas 13: ",np.count_nonzero(np.array(labels)==13))
# print("Numero de etiquetas 14: ",np.count_nonzero(np.array(labels)==14))
# print("Numero de etiquetas 15: ",np.count_nonzero(np.array(labels)==15))
# print("Numero de etiquetas 16: ",np.count_nonzero(np.array(labels)==16))
# print("Numero de etiquetas 17: ",np.count_nonzero(np.array(labels)==17))
# print("Numero de etiquetas 18: ",np.count_nonzero(np.array(labels)==18))
# print("Numero de etiquetas 19: ",np.count_nonzero(np.array(labels)==19))
# print("Numero de etiquetas 20: ",np.count_nonzero(np.array(labels)==20))
# print("Numero de etiquetas 21: ",np.count_nonzero(np.array(labels)==21))
# print("Numero de etiquetas 22: ",np.count_nonzero(np.array(labels)==22))
# print("Numero de etiquetas 23: ",np.count_nonzero(np.array(labels)==23))
# print("Numero de etiquetas 24: ",np.count_nonzero(np.array(labels)==24))
# print("Numero de etiquetas 25: ",np.count_nonzero(np.array(labels)==25))
# print("Numero de etiquetas 26: ",np.count_nonzero(np.array(labels)==26))
# print("Numero de etiquetas 27: ",np.count_nonzero(np.array(labels)==27))


face_recognizer = cv2.face.EigenFaceRecognizer_create()

#entrenando el reconocedor de rostros
print("Entrenando....")
face_recognizer.train(facesData, np.array(labels))
#Almacenar el modelo obtenido

face_recognizer.write("modeloEngenface.xml")

print("Modelo almacenado")