#Contador de puntos en un videojuego
#Genera el numero de rondas que pide el usuario con una cantidad de puntos aleatoria entre 10 y 30
import random

ronda = 1

rondas = int(input("Cuantas rondas desea realizar? "))

for i in range(rondas):
    print("Ronda " + str(i+1) + ": ", random.randint(10,30))
