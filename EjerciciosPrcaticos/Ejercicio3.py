#El DJ matematico (beats de una cancion)

bpm = int(input("BPM de la cancion: "))
minutos = float (input("Duracion en minutos: "))
beats = bpm*minutos
round(beats)


print ("Esta cancion tiene aproximadamente ", beats, " beats.")