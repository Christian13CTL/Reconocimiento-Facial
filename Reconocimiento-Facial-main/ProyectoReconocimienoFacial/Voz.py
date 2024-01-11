# import pyttsx3

# texto_a_convertir = "hello, esto es un ejemplo de texto a voz."

# engine = pyttsx3.init()
# engine.setProperty('rate', 150)  # Ajusta la velocidad de reproducción (opcional)
# engine.say(texto_a_convertir)
# engine.runAndWait()

import pyttsx3

# Inicializar el motor de texto a voz
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Ajusta la velocidad de reproducción (opcional)

nombre_actual = None  # Variable para almacenar el nombre actualmente reconocido
persona_detectada = False  # Variable de estado para controlar la lectura del nombre

def leer_nombre(nombre):
    global nombre_actual, persona_detectada
    if nombre != nombre_actual:
        nombre_actual = nombre
        persona_detectada = True
        engine.say(f"Bienvenido, {nombre}!")
        engine.runAndWait()

# Ejemplo de reconocimiento facial en tiempo real (sustituye por tu código real)
while True:
    # Realizar el reconocimiento facial y obtener el nombre de la persona detectada
    nombre_reconocido = obtener_nombre_reconocido()

    if nombre_reconocido is not None:
        leer_nombre(nombre_reconocido)
    elif persona_detectada:
        persona_detectada = False
        engine.say("Persona no reconocida.")
        engine.runAndWait()