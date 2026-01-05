#Decisiones en el gimnasio

objetivo = input("Objetivo: Bajar/Subir/Mantener: ")
if objetivo == "Bajar":
    print ("Déficit calórico, entrenamiento de fuerza y más cardio")
elif objetivo == "Subir":
    print ("Superávit calórico y entrenamiento de fuerza")
elif objetivo == "Mantener":
    print ("Dieta normocalórica y entrenamiento de fuerza")
else: print ("Respuesta incorrecta")