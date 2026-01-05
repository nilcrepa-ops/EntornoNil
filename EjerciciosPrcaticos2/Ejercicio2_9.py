#Estadisticas de jugadores

jugadores ={
    "Rafa Mora": {
        "nivel": 10, "puntos": 2000
    },
    "Falete": {
        "nivel": 12, "puntos": 2400
    },
    "Antonio Recio":{
        "nivel": 15, "puntos": 4500
    }
}

nombre = input("Que jugador quieres ver?")
if nombre in jugadores:
    puntos = jugadores[nombre]["puntos"]
    print("Puntuacion de", nombre, ":", puntos)
    if puntos > 2500:
        print("Sigue subiendo de nivel!")

