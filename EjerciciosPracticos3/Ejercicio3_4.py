#Juego de adivinar el número

import random

respuesta = 0


randomN = random.randint(1,10)

intentos = 3

print(randomN)

while intentos >0:
    turno = int(input("Adivina el numero entre 1 y 10: "))

    if turno < randomN:
       print("Demasiado bajo")
       intentos -=1
       print("Numero incorrecto. Intentos: ", intentos)
    elif turno > randomN:
       print("Demasiado alto")
       intentos -=1
       print("Numero incorrecto. Intentos: ", intentos)
    elif turno == randomN:
        print("Has acertado!")
        break

if intentos > 0:
    print("Has ganado el juego")
else:
    print(f"Has perdido el juego. El numero era ", {randomN})       