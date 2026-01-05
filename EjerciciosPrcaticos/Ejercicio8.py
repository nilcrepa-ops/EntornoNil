#Clasificador deportivo simple

edad = 18
horasMenor = 15
horasMayor = 20

edadU = int(input("Edad: "))
horasU = float(input("Horas de entrenamiento a la semana: "))

if edadU < edad and horasU > horasMenor:
    print ("Joven deportista de elite")
elif edadU < edad and horasU < horasMenor:
    print ("Joven deportista")
elif edadU >= edad and horasU >= horasMayor:
    print ("Adulto deportista de elite")
elif edadU >= edad and horasU < horasMayor:
    print ("Adulto deportista")

