#Metronomo musical
#Genera un metronomo hasta 4 tiempos con un delay de 1 segundo entre tics

import time

metronomo = 1


while metronomo <=4:
    print("tic ", str(metronomo))
    metronomo+=1
    time.sleep(1)

print("Compás completado")
